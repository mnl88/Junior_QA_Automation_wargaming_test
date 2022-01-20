# https://docs.python.org/3/library/sqlite3.html

"""

3. Создать session-scope фикстуру, которая получает текущее состояние базы данных и создает временную новую базу, в которой рандомизируются значения:

Для каждого корабля меняется на случайный один из компонентов: корпус, орудие или двигатель
В каждом компоненте меняется один из случайно выбранных параметров на случайное значение из допустимого диапазона (см. выше)


4. Написать автотесты, сравнивающие данные из исходной базы с полученной рандомизированной:

Для каждого корабля должно быть 3 теста, проверяющие его орудие, корпус и двигатель.
Тест должен падать с assert:
i. Когда значение параметра компонента не соответствует тому, что было до запуска рандомизатора.

Пример вывода:

Ship-2, weapon-1

     reload speed: expected 1, was 2

     diameter: expected 2, was 3

Ship-2, hull-3

     type: expected 1, was 2

Ship-3, engine-6

     power: expected 22, was 13

ii. Когда изменилось орудие, корпус или двигатель. Выводить, что было до этого и, что сейчас.

Пример вывода:

Ship-5, engine-4

     expected engine-1, was engine-4



Требования к выполненному заданию:

Версия Python – 3.8
Тесты должны быть написаны с использованием фрейморка pytest
В качестве параметризации использовать pytest.mark.parametrize или хук pytest_generate_tests.
В результате прогона должно получиться 600 тестов.
В результате выполнения задания должно быть по крайней мере следующее:
Скрипт, создающий и заполняющий исходную базу данных
Python-модуль, содержащий тесты
(Опционально) conftest.py, содержащий фикстуры и хукиъ
6. Стиль кода – PEP8
"""

import pathlib
import random
import sqlite3
import os

create_db_instructions = [
    """
    CREATE TABLE
    weapons (weapon TEXT PRIMARY KEY, reload_speed INT, rotation_speed INT, diameter INT, power_volley INT, count INT)
    """,
    """
    CREATE TABLE
    hulls (hull TEXT PRIMARY KEY, armor INT, type INT, capacity INT)
    """,
    """
    CREATE TABLE
    engines (engine TEXT PRIMARY KEY, power INT, type INT)
    """,
    """
    CREATE TABLE
    ships (
    ship TEXT PRIMARY KEY, weapon TEXT, hull TEXT, engine TEXT,
    FOREIGN KEY (weapon) REFERENCES weapons (weapon),
    FOREIGN KEY (hull) REFERENCES hulls (hull),
    FOREIGN KEY (engine) REFERENCES engines (engine)
    )
    """
]

ships_count = 200
weapons_count = 20
hulls_count = 5
engines_count = 6
range_values = (1, 20)

db_filepath = os.path.realpath(os.path.dirname(__file__)) + '/wargaming.db'

con = sqlite3.connect(db_filepath)
con.row_factory = sqlite3.Row
cur = con.cursor()


def make_db(create_db_statements: list[str]):
    for s in create_db_statements:
        cur.execute(s)


#  todo: delete before share
def drop_all_tables():
    cur.execute("""DROP TABLE Ships""")
    cur.execute("""DROP TABLE Weapons""")
    cur.execute("""DROP TABLE Hulls""")
    cur.execute("""DROP TABLE Engines""")


def fill_db(number_of_ships: int,
            number_of_weapons: int,
            number_of_hulls: int,
            number_of_engines: int,
            params_range_values: tuple[int, int]):
    def add_weapon(weapon: str, reload_speed: int, rotation_speed: int, diameter: int, power_volley: int, count: int):
        with con:
            cur.execute("INSERT INTO weapons VALUES (?, ?, ?, ?, ?, ?)",
                        (weapon, reload_speed, rotation_speed, diameter, power_volley, count))

    def add_hull(hull: str, armor: int, type: int, capacity: int):
        with con:
            cur.execute("INSERT INTO hulls VALUES (?, ?, ?, ?)", (hull, armor, type, capacity))

    def add_engine(engine: str, power: int, type: int):
        with con:
            cur.execute("INSERT INTO engines VALUES (?, ?, ?)", (engine, power, type))

    def add_ship(ship: str, weapon: str, hull: str, engine: str):
        with con:
            cur.execute("INSERT INTO ships VALUES (?, ?, ?, ?)", (ship, weapon, hull, engine))

    def get_name_of_random_ship_component(table_name_of_component: str) -> str:
        pk_name = cur.execute(f"PRAGMA table_info([{table_name_of_component}]);").fetchone()['name']
        return cur.execute(f"SELECT {pk_name} FROM {table_name_of_component} ORDER BY RANDOM() LIMIT 1").fetchone()[0]

    for _ in range(number_of_weapons):
        add_weapon(
            weapon=('Weapon-' + str(_ + 1)),
            reload_speed=random.randint(*params_range_values),
            rotation_speed=random.randint(*params_range_values),
            diameter=random.randint(*params_range_values),
            power_volley=random.randint(*params_range_values),
            count=random.randint(*params_range_values)
        )
    for _ in range(number_of_hulls):
        add_hull(
            hull=('Hull-' + str(_ + 1)),
            armor=random.randint(*params_range_values),
            type=random.randint(*params_range_values),
            capacity=random.randint(*params_range_values)
        )
    for _ in range(number_of_engines):
        add_engine(
            engine=('Engine-' + str(_ + 1)),
            power=random.randint(*params_range_values),
            type=random.randint(*params_range_values)
        )
    for _ in range(number_of_ships):
        add_ship(
            ship=('Ship-' + str(_ + 1)),
            weapon=get_name_of_random_ship_component('weapons'),
            hull=get_name_of_random_ship_component('hulls'),
            engine=get_name_of_random_ship_component('engines')
        )


def main():
    drop_all_tables()
    make_db(create_db_instructions)  # 1st task
    fill_db(ships_count, weapons_count, hulls_count, engines_count, range_values)  # 2nd task

    # table_name = 'ships'
    # a = cur.execute(f"PRAGMA table_info([{table_name}]);").fetchone()
    # pk_name = a['name']
    # rows = cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    # tables = [row[0] for row in rows]
    #
    # def sql_identifier(s):
    #     return '"' + s.replace('"', '""') + '"'
    #
    # for table in tables:
    #     print("table: " + table)
    #     rows = cur.execute("PRAGMA table_info({})".format(sql_identifier(table)))
    #     print(rows.fetchall())
    #     rows = cur.execute("PRAGMA foreign_key_list({})".format(sql_identifier(table)))
    #     print(rows.fetchall())


if __name__ == '__main__':
    main()
    cur.close()
    con.close()
