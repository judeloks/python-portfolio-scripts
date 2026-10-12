import re
from collections import Counter


def analyze_text(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден!")
        return

    # Считаем символы и строки
    characters_count = len(text)
    characters_no_spaces = len(text.replace(" ", "").replace("\n", ""))

    # Считаем слова (игнорируем знаки препинания)
    words = re.findall(r"\b\w+\b", text.lower())
    words_count = len(words)

    # Считаем предложения (по точкам, восклицательным и вопросительным знакам)
    sentences_count = len(re.split(r"[.!?]+", text)) - 1

    # Находим самые частые слова
    most_common_words = Counter(words).most_common(5)

    # Выводим отчет в консоль
    print(f"\n--- Анализ текста: {file_path} ---")
    print(f"• Всего символов (с пробелами): {characters_count}")
    print(f"• Всего символов (без пробелов): {characters_no_spaces}")
    print(f"• Всего слов: {words_count}")
    print(f"• Всего предложений: {sentences_count}")
    print(f"• Топ-5 частых слов:")
    for word, count in most_common_words:
        print(f"  - '{word}': {count} раз(а)")

    # Сохраняем отчет в файл
    report_name = "analysis_report.txt"
    with open(report_name, "w", encoding="utf-8") as report_file:
        report_file.write(f"Отчет анализа файла: {file_path}\n")
        report_file.write(f"Слов: {words_count}, Предложений: {sentences_count}\n")
    print(f"\nОтчет успешно сохранен в файл '{report_name}'!")


if __name__ == "__main__":
    path = input("Введите путь к текстовому файлу для анализа: ").strip()
    analyze_text(path)
