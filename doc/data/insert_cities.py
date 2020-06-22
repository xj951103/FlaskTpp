import json

import pymysql

MYSQL_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",
    "db": "flaskApi",
    "port": 3306,
    "charset": "utf8"
}

conn = pymysql.connect(**MYSQL_CONFIG)
cur = conn.cursor()


def read_file():
    with open("./cities_json_file.py", "r", encoding="utf-8") as json_file:
        cities_json_str = json_file.read()
        cities_json = json.loads(cities_json_str)

    return cities_json


def insert_data(cities_json):
    return_value = cities_json.get("returnValue")
    letter_sql = """INSERT INTO letter (letter) VALUES('{}')"""
    city_sql = """INSERT INTO city(letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin) VALUES ({}, {}, {}, '{}', {}, '{}')"""
    for key, values in return_value.items():
        cur.execute(letter_sql.format(key))
        letter_id = conn.insert_id()
        conn.commit()
        for value in values:
            c_id = value.get("id")
            c_parent_id = value.get("parentId")
            c_region_name = value.get("regionName")
            c_city_code = value.get("cityCode")
            c_pinyin = value.get("pinYin")
            cur.execute(city_sql.format(letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin))

    conn.commit()


if __name__ == '__main__':
    cities_json = read_file()
    insert_data(cities_json)