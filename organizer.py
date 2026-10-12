import os
import shutil

# 1. Словарь с категориями и расширениями файлов
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Installers': ['.exe', '.msi'],
    'Audio_Video': ['.mp3', '.mp4', '.avi', '.mkdir', '.mov']
}

def organize_folder(folder_path):
    # Проверяем, существует ли указанная папка
    if not os.path.exists(folder_path):
        print(f"Ошибка: папка '{folder_path}' не найдена!")
        return

    # Счетчик перемещенных файлов
    stats = {category: 0 for category in FILE_CATEGORIES}
    stats['Other'] = 0

    # Проходим по всем файлам в папке
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Пропускаем, если это папка, а не файл
        if os.path.isdir(file_path):
            continue

        # Получаем расширение файла
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Определяем, в какую категорию отправить файл
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                target_dir = os.path.join(folder_path, category)
                os.makedirs(target_dir, exist_ok=True)  # Создаем папку, если ее нет
                shutil.move(file_path, os.path.join(target_dir, filename))
                stats[category] += 1
                moved = True
                break

        # Если расширение неизвестно — отправляем в папку 'Other'
        if not moved and extension:
            target_dir = os.path.join(folder_path, 'Other')
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(target_dir, filename))
            stats['Other'] += 1

    # Выводим отчет в консоль
    print("\n--- Сортировка завершена! ---")
    for category, count in stats.items():
        if count > 0:
            print(f"• В папку '{category}' перемещено файлов: {count}")

if __name__ == "__main__":
    # Запрашиваем у пользователя путь к папке (например: C:\Users\Имя\Downloads)
    path = input("Введите путь к папке для сортировки: ").strip()
    organize_folder(path)