import copy
import itertools
import json
from pathlib import Path
import subprocess
import sys
import unittest

from code import check_array, find_arrays, format_result, parse_array, validate_array

ROOT = Path(__file__).parent


class UnitTests(unittest.TestCase):
    def test_sorted(self): self.assertTrue(check_array(*"abcxyz"))
    def test_reverse(self): self.assertFalse(check_array(*"cba"))
    def test_duplicates(self): self.assertTrue(check_array(*"aabbzz"))
    def test_uppercase(self): self.assertTrue(check_array(*"aZbAc"))
    def test_uppercase_between_reverse(self): self.assertFalse(check_array(*"zAa"))
    def test_empty(self): self.assertTrue(check_array())
    def test_no_lowercase(self): self.assertTrue(check_array(*"ZYX"))
    def test_length_boundary(self): validate_array(list("a" * 100))
    def test_too_long(self):
        with self.assertRaises(ValueError): validate_array(list("a" * 101))
    def test_invalid_elements(self):
        for item in ["я", "é", "1", "-", "", "ab", 1, None]:
            with self.subTest(item=item):
                with self.assertRaises(ValueError): validate_array([item])
    def test_parse(self):
        self.assertEqual(parse_array("a B c"), list("aBc"))
        self.assertEqual(parse_array("abc"), list("abc"))
        self.assertEqual(parse_array(""), [])
    def test_exhaustive_short_sequences(self):
        # Независимый эталон: сравнение со списком после сортировки.
        for size in range(6):
            for elements in itertools.product("abAB", repeat=size):
                lower = [x for x in elements if x in "ab"]
                self.assertEqual(check_array(*elements), lower == sorted(lower))


class IntegrationTests(unittest.TestCase):
    def test_validation_and_check(self):
        with self.assertRaises(ValueError): check_array("a", "я")
    def test_one_based_numbers(self):
        self.assertEqual(find_arrays([list(x) for x in ["abc","ba","Z","dc","xyz"]]), [1,3,5])
    def test_exactly_five(self):
        for count in [0,4,6]:
            with self.subTest(count=count):
                with self.assertRaises(ValueError): find_arrays([[]] * count)
    def test_no_mutation(self):
        arrays = [list(x) for x in ["abc","ba","Z","dc","xyz"]]
        before = copy.deepcopy(arrays)
        find_arrays(arrays)
        self.assertEqual(arrays, before)
    def test_complete_pipeline(self):
        arrays = [parse_array(x) for x in ["a B c","ba","Z","dc","xyz"]]
        self.assertEqual(format_result(find_arrays(arrays)), "Номера массивов: 1, 3, 5")
    def test_negative_output(self):
        self.assertEqual(format_result(find_arrays([list("ba")] * 5)),
                         "Нет массивов, удовлетворяющих условию")


class SystemTests(unittest.TestCase):
    pass


def lines_for(case):
    return case.get("lines") or [char * size for char, size in zip(case["chars"], case["repeat"])]


def make_system_test(case):
    def test(self):
        result = subprocess.run([sys.executable, str(ROOT / "code.py")],
            input="\n".join(lines_for(case)) + "\n", text=True,
            encoding="utf-8", capture_output=True, env={**__import__('os').environ,
            "PYTHONIOENCODING":"utf-8"}, timeout=10)
        self.assertEqual(result.returncode, case["exit"])
        self.assertEqual(result.stdout.strip(), case["result"])
        self.assertEqual(result.stderr, "")
    return test


for scenario in json.loads((ROOT / "scenarios.json").read_text(encoding="utf-8")):
    setattr(SystemTests, "test_" + scenario["id"], make_system_test(scenario))


if __name__ == "__main__":
    unittest.main(verbosity=2)
