import sqlite3


def main():
    """
    Передаем данные из старой таблицы в новую
    """
    connection = sqlite3.connect('animal.db')
    cursor = connection.cursor()

    with open('migrates.sql') as file:
        query = file.read()

    cursor.executescript(query)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()