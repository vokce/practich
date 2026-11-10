# Работа с ветками в GitHub

В архиве есть настоящая локальная история Git и файл history.bundle.
Репозиторий работы: https://github.com/vokce/practich
Этот файл описывает порядок выполнения и повторения операции.

## Выполнение в веб-интерфейсе

1. Создайте пустой репозиторий в своём аккаунте GitHub.
2. В main создайте code.py, вставив содержимое initial_code.py. Сохраните коммит
   `Add initial array checker`.
3. Создайте из main ветку fix-code-issues.
4. В этой ветке замените code.py исправленной версией, добавьте test_code.py,
   scenarios.json и README.md. Сохраните коммит `Fix array validation and ordering`.
5. Откройте Compare & pull request. Проверьте base: main, compare: fix-code-issues.
6. Заголовок: `Refactor array checking functions`.
   Описание: `Исправлены нумерация массивов, обработка повторов и проверка входных данных.
   Добавлены модульные, интеграционные и системные тесты. Все 36 тестов проходят.`
7. Создайте Pull Request. Проверьте изменения и результаты тестов.
8. Выполните Merge pull request и Confirm merge, если это разрешено правилами
   репозитория. Удалите уже слитую временную ветку fix-code-issues.
9. Откройте историю main и проверьте наличие исходного коммита, исправления и слияния.
10. Для отчёта сохраните скриншоты: исходный файл в main; исправленная версия в
    fix-code-issues; открытый Pull Request; отметка Merged; история main.

## Восстановление локальной истории

    git clone history.bundle array-practice
    cd array-practice
    python -m unittest -v

Локальная демонстрация уже содержит merge-коммит. Для нового Pull Request
используйте последовательность веб-интерфейса выше: публикация готового merge-коммита
сама по себе не создаёт Pull Request.

Официальные справки:
https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request
https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-a-pull-request
