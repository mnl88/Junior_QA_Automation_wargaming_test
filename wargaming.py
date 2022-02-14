# https://docs.python.org/3/library/sqlite3.html

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

DB_FILEPATH = os.path.realpath(os.path.dirname(__file__)) + '/wargaming.db'
# DB_FILEPATH = 'E:/Documents/Python3/2021/Junior_QA_Automation_wargaming_test/wargaming.db'

con = sqlite3.connect(DB_FILEPATH)
con.row_factory = sqlite3.Row
cur = con.cursor()


def make_db(create_db_statements: list[str]):
    for s in create_db_statements:
        cur.execute(s)


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


if __name__ == '__main__':
    main()
    cur.close()
    con.close()
