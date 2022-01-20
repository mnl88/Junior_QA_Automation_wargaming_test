import os
import random
import sqlite3
import pytest
import pathlib

from wargaming import create_db_instructions


# def create_test_db(tmp_path_factory):
#     img = compute_expensive_image()
#     fn = tmp_path_factory.mktemp("data") / "img.png"


def create_test_db(tmpdir_factory: pytest.TempdirFactory) -> sqlite3.Connection:
    # test_db_filepath = tmpdir_factory.getbasetemp().join('test_db.db')
    test_db_filepath = tmpdir_factory.getbasetemp().join('test_db.db')
    print('\ntest_db_filepath', test_db_filepath)
    test_db = sqlite3.connect(test_db_filepath)
    curs = test_db.cursor()
    for s in create_db_instructions:
        curs.execute(s)
    return test_db


def paste_rows_into_test_db_with_correction_of_one_parameter(
        conn_origin_db: sqlite3.Connection, conn_test_db: sqlite3.Connection, table_name: str):
    curs_o = conn_origin_db.cursor()
    curs_t = conn_test_db.cursor()
    rows = curs_o.execute(f'SELECT * from {table_name}').fetchall()

    update_script_1st_part = f'INSERT INTO {table_name} VALUES (?'
    update_script_2st_part = ''
    for i in range(len(rows[0]) - 1):
        update_script_2st_part += ', ?'
    update_script_3rd_part = ')'
    update_script = update_script_1st_part + update_script_2st_part + update_script_3rd_part

    for row in rows:
        random_param = random.randint(1, len(row) - 1)
        new_weapon = list(row)
        new_weapon[random_param] = random.randint(1, 20)

        with conn_test_db:
            curs_t.execute(update_script, [*new_weapon])
    curs_t.close()
    curs_o.close()


def paste_ships_into_test_db_with_correction_of_one_parameter(
        conn_origin_db: sqlite3.Connection, conn_test_db: sqlite3.Connection):
    curs_o = conn_origin_db.cursor()
    curs_t = conn_test_db.cursor()
    ships = curs_o.execute(f'SELECT * from ships').fetchall()
    weapon_list = curs_o.execute(f'SELECT weapon from weapons').fetchall()
    engine_list = curs_o.execute(f'SELECT engine from engines').fetchall()
    hull_list = curs_o.execute(f'SELECT hull from hulls').fetchall()

    for row in ships:
        random_param = random.randint(1, len(row) - 1)
        ship = list(row)
        if random_param == 1:  # weapon
            ship[random_param] = random.choice(weapon_list)[0]
        elif random_param == 2:  # hull
            ship[random_param] = random.choice(hull_list)[0]
        else:  # engine
            ship[random_param] = random.choice(engine_list)[0]

        with conn_test_db:
            curs_t.execute('INSERT INTO ships VALUES (? ,? ,? , ?)', ship)
    curs_t.close()
    curs_o.close()


@pytest.fixture(scope='session', autouse=True)
def create_and_fill_test_db(tmpdir_factory: pytest.TempdirFactory):

    conn_origin_db = sqlite3.connect('E:/Documents/Python3/2021/Junior_QA_Automation_wargaming_test/wargaming.db')
    # https://habr.com/ru/post/448792/

    conn_test_db = create_test_db(tmpdir_factory)

    paste_ships_into_test_db_with_correction_of_one_parameter(conn_origin_db, conn_test_db)

    for table_name in ['weapons', 'hulls', 'engines']:
        paste_rows_into_test_db_with_correction_of_one_parameter(conn_origin_db, conn_test_db, table_name)

    conn_origin_db.close()
    conn_test_db.close()

    yield


# @pytest.fixture(scope='session', autouse=False)
# def get_ship_pairs(create_and_fill_test_db) -> list[tuple]:
#     print('\n\nget_ship_pairs\n\n')
#     conn_origin_db, conn_test_db = create_and_fill_test_db
#     curs_test = conn_test_db.cursor()
#     curs_origin = conn_origin_db.cursor()
#
#     # curs_test = create_and_fill_test_db.cursor()
#     # weapons = curs_test.execute('SELECT * from weapons').fetchall()
#     # engines = curs_test.execute('SELECT * from engines').fetchall()
#     # hulls = curs_test.execute('SELECT * from hulls').fetchall()
#     ship_list_test = curs_test.execute('SELECT * from ships').fetchall()
#     ship_list_origin = curs_origin.execute('SELECT * from ships').fetchall()
#
#     ship_pairs = []
#     for ship in ship_list_test:
#         for ship_origin in ship_list_origin:
#             if ship[0] == ship_origin[0]:
#                 ship_pairs.append((ship, ship_origin))
#                 # print(ship, ship_origin)
#     yield ship_pairs


# @pytest.fixture(params=get_ship_pairs)
# def get_ship_pair(request):
#     return request.param
