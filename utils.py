import sqlite3
import time

TABLE_NAME = "bingo.db"


class Record:
    name: str
    link: str
    keys: str

    def __init__(self, name, link, keys):
        self.name = name
        self.link = link
        self.keys = keys

    def __lt__(self, other):
        return self.name < other.name


def get_articles():
    records_array = []
    try:
        connection = sqlite3.connect(TABLE_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM 'Articles'")
        records = cursor.fetchall()
        for record in records:
            records_array.append(Record(name=record[0], link=record[1], keys=record[2]))
        cursor.close()
        connection.close()
    except sqlite3.Error:
        print("SQL error")

    return records_array


class Theme:
    name: str
    key: str

    def __init__(self, name, key):
        self.name = name
        self.key = key


def get_themes():
    records_array = []
    try:
        connection = sqlite3.connect(TABLE_NAME)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM 'Themes'")
        records = cursor.fetchall()
        for record in records:
            records_array.append([record[0], record[1]])
        cursor.close()
        connection.close()
    except sqlite3.Error:
        print("SQL error")

    return records_array


def log(message):
    with open('logging.log', "a") as file:
        file.write(f"{time.asctime()}  {message.from_user.id}, {message.from_user.first_name}\n")
