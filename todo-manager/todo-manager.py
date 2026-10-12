import csv
import os

FILENAME = "tasks.csv"


def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    tasks.append({"title": row[0], "priority": row[1]})
    return tasks


def save_tasks(tasks):
    with open(FILENAME, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow([task["title"], task["priority"]])


def show_tasks(tasks):
    if not tasks:
        print("\nСписок задач пуст!")
        return
    print("\n--- Ваши задачи ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. [{task['priority']}] {task['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n1. Посмотреть задачи")
        print("2. Добавить задачу")
        print("3. Выйти")

        choice = input("Выберите действие (1-3): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Введите текст задачи: ").strip()
            priority = input("Введите приоритет (Низкий / Средний / Высокий): ").strip()
            if title:
                tasks.append({"title": title, "priority": priority or "Обычный"})
                save_tasks(tasks)
                print("Задача успешно сохранена!")
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
