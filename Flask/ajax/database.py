# coding: utf8

# Copyright 2017 Jacques Berger
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sqlite3


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/location.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_pays(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select id, nom from pays")
        pays = cursor.fetchall()
        return [(unPays[0],unPays[1]) for unPays in pays]

    # def insert_artist(self, name):
        # connection = self.get_connection()
        # cursor = connection.cursor()
        # cursor.execute(("insert into artiste(nom, est_solo, nombre_individus) "
                        # "values(?, ?, ?)"), (name, 0, 0))
        # connection.commit()