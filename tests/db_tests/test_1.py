import os
import sqlite3
import pathlib

import pytest
from _pytest.tmpdir import tmpdir_factory, tmp_path

from wargaming import DB_FILEPATH

from pathlib import Path

import tempfile

import logging


logging.basicConfig(level=logging.INFO)


FOLDER_FOR_TESTS = r'D:\folder_to_tests'

# test_db_filepath2 = pytest.TempdirFactory.getbasetemp().join('test_db.db')
# test_db_filepath = ':memory:'
#
#
# @pytest.mark.parametrize('filepath', [DB_FILEPATH, test_db_filepath,
#                                       # test_db_filepath2
#                                       ])
# def test_ship_1_is_in_db(create_and_fill_test_db, filepath):
#     con = sqlite3.connect(filepath)
#     cur = con.cursor()
#     ship = cur.execute('SELECT ship from ships').fetchone()[0]
#     assert ship == 'Ship-1'
#     con.close()
#

#
# def test_simple(create_and_fill_test_db):
#     a = create_and_fill_test_db
#     print(a*5)
#     assert 1 == 1


# @pytest.fixture(params=get_ship_pairs(create_and_fill_test_db))
# def param_test(request):
#     return request.param

# @pytest.fixture()

# @pytest.fixture(params=range(1, 11, 2))
# def odd(request):
#     return request.param
#
#
# def test_sum_odd_even_returns_odd(odd):
#     assert odd == 1
#
# @pytest.fixture(scope='session', autouse=True)
# def get_all_pairs(tmpdir_factory):
#     conn_origin_db = sqlite3.connect(db_filepath)
#     test_db_filepath = tmpdir_factory.getbasetemp().join('test_db.db')
#
#     conn_test_db = sqlite3.connect(test_db_filepath)
#     curs_test = conn_test_db.cursor()
#     curs_origin = conn_origin_db.cursor()
#
#     ship_list_test = curs_test.execute('SELECT * from ships').fetchall()
#     ship_list_origin = curs_origin.execute('SELECT * from ships').fetchall()
#
#     ship_pairs = []
#     for ship in ship_list_test:
#         for ship_origin in ship_list_origin:
#             if ship[0] == ship_origin[0]:
#                 ship_pairs.append((ship, ship_origin))
#
#     return ship_pairs
#
#     # pairs = get_ship_pairs()
#     # print(get_ship_pairs)

# def test_db_909(get_all_pairs):
#     a = get_all_pairs
#     print(a)


# @pytest.fixture(params=get_all_pairs())
# def func_name(request):
#     return request.param

#
# def test_parametrized_username(non_parametrized_username):
#     assert non_parametrized_username in ['one', 'two', 'three']


# ships = adsdsd_111(tmpdir_factory)
# print(ships)

# @pytest.fixture(params=adsdsd_111)
# def odd(request):
#     return request.param


# @pytest.mark.parametrize("ship_from_test_db, ship_from_origin_db", get_ship_pairs)
# def test_some_data(create_and_fill_test_db, ship_from_test_db, ship_from_origin_db):

"""
def test_some_data(create_and_fill_test_db):
    conn_origin_db = sqlite3.connect('E:/Documents/Python3/2021/Junior_QA_Automation_wargaming_test/wargaming.db')
    conn_test_db = sqlite3.connect('E:/Documents/Python3/2021/Junior_QA_Automation_wargaming_test/tests/db_tests.db')

    curs_test = conn_test_db.cursor()
    curs_origin = conn_origin_db.cursor()

    # print(get_ship_pairs)

    # curs_test = create_and_fill_test_db.cursor()
    # weapons = curs_test.execute('SELECT * from weapons').fetchall()
    # engines = curs_test.execute('SELECT * from engines').fetchall()
    # hulls = curs_test.execute('SELECT * from hulls').fetchall()
    ship_list_test = curs_test.execute('SELECT * from ships').fetchall()
    ship_list_origin = curs_origin.execute('SELECT * from ships').fetchall()

    for ship in ship_list_test:
        for ship_origin in ship_list_origin:
            if ship[0] == ship_origin[0]:
                # assert ship == ship_origin
                # print(ship, ship_origin)
                pass
"""

#
#
#     # print(weapons)
#     # print(engines)
#     # print(hulls)
#     # print(ships)
#     # print(ships_old)
#     # assert a == b
#     assert [] == []


# def test_some_data2(create_and_fill_test_db):
#     conn_origin_db, conn_test_db = create_and_fill_test_db
#     curs_test = conn_test_db.cursor()
#     curs_origin = conn_origin_db.cursor()
#
#     # print(get_ship_pairs)
#
#     # curs_test = create_and_fill_test_db.cursor()
#     # weapons = curs_test.execute('SELECT * from weapons').fetchall()
#     # engines = curs_test.execute('SELECT * from engines').fetchall()
#     # hulls = curs_test.execute('SELECT * from hulls').fetchall()
#     ship_list_test = curs_test.execute('SELECT * from ships').fetchall()
#     ship_list_origin = curs_origin.execute('SELECT * from ships').fetchall()
#
#     for ship in ship_list_test:
#         for ship_origin in ship_list_origin:
#             if ship[0] == ship_origin[0]:
#                 # assert ship == ship_origin
#                 # print(ship, ship_origin)
#                 pass
#
#
#     # print(weapons)
#     # print(engines)
#     # print(hulls)
#     # print(ships)
#     # print(ships_old)
#     # assert a == b
#     assert [] == []


def get_pairs_from_db():
    folder_name = 'python_test_data'
    file_name = "test_db.db"
    file_path = os.path.join(FOLDER_FOR_TESTS, folder_name, file_name)
    # file_path = os.path.join(r'C:\Users\Nikita\AppData\Local\Temp', folder_name, file_name)
    con_test_db = sqlite3.connect(file_path)
    cur_test = con_test_db.cursor()

    con_origin_db = sqlite3.connect(DB_FILEPATH)
    cur_origin = con_origin_db.cursor()

    ship_list_test = cur_test.execute('SELECT * from ships').fetchall()
    ship_list_origin = cur_origin.execute('SELECT * from ships').fetchall()

    ships_pairs = []
    for ship in ship_list_test:
        for ship_origin in ship_list_origin:
            if ship[0] == ship_origin[0]:
                ships_pairs.append((ship, ship_origin))
    for pair in ships_pairs:
        print(pair)

    cur_test.close()
    cur_origin.close()
    con_test_db.close()
    con_origin_db.close()
    #
    return ships_pairs
    # return [1, 2, 3]


# @pytest.mark.parametrize('pair', get_pairs_from_db())
# def test_simple_equals_always_pass(pair):
#     assert pair is 1


@pytest.fixture(params=get_pairs_from_db())
def odd(request):
    return request.param


def test_sum_odd_even_returns_odd(odd):
    assert odd == 1



# @pytest.mark.parametrize('pair', get_pairs_from_db())
# def test_simple_equals_in_pair(pair):
#     assert pair[0] == pair[1]


#
#     # print(weapons)
#     # print(engines)
#     # print(hulls)
#     # print(ships)
#     # print(ships_old)
#     # assert a == b
#     assert [] == []

"""
def test_db():

    a = tempfile.mkstemp('asd')
    print()
    print()
    print(a)
    print()
    print()
    print()
    BASE_DIR = Path(__file__).resolve().parent.parent
    print('asdsadasdas', BASE_DIR)
    # ships = curs.execute('select * from ships').fetchall()
    # print(ships)
"""

# @pytest.mark.parametrize('ship1', 'ship2', [(1, 1), (2, 2)])
# def test_ships_are_equal(ship1, ship2):
#     assert ship1 == ship2

