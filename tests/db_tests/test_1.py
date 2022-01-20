import sqlite3
import pathlib

import pytest
from _pytest.tmpdir import tmpdir_factory, tmp_path

from wargaming import db_filepath

from pathlib import Path



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


@pytest.fixture(scope='session', autouse=True)
def get_all_pairs(tmpdir_factory):
    conn_origin_db = sqlite3.connect(db_filepath)
    test_db_filepath = tmpdir_factory.getbasetemp().join('test_db.db')

    conn_test_db = sqlite3.connect(test_db_filepath)
    curs_test = conn_test_db.cursor()
    curs_origin = conn_origin_db.cursor()

    ship_list_test = curs_test.execute('SELECT * from ships').fetchall()
    ship_list_origin = curs_origin.execute('SELECT * from ships').fetchall()

    ship_pairs = []
    for ship in ship_list_test:
        for ship_origin in ship_list_origin:
            if ship[0] == ship_origin[0]:
                ship_pairs.append((ship, ship_origin))

    return ship_pairs

    # pairs = get_ship_pairs()
    # print(get_ship_pairs)


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


# def test_some_data3(create_and_fill_test_db):
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
#     # print(weapons)
#     # print(engines)
#     # print(hulls)
#     # print(ships)
#     # print(ships_old)
#     # assert a == b
#     assert [] == []


def test_db():
    BASE_DIR = Path(__file__).resolve().parent.parent
    print('asdsadasdas', BASE_DIR)
    # ships = curs.execute('select * from ships').fetchall()
    # print(ships)


# @pytest.mark.parametrize('ship1', 'ship2', [(1, 1), (2, 2)])
# def test_ships_are_equal(ship1, ship2):
#     assert ship1 == ship2


