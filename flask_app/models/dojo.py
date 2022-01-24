from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL('dojos_and_ninja_schema').query_db(query)
        dojos = []

        for dojo in result:
            dojos.append(cls(dojo))
        return dojos


    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES ( %(dname)s, NOW(), NOW() );"
        return connectToMySQL('dojos_and_ninja_schema').query_db(query,data)

    @classmethod
    def show(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_ninjas_for_dojo(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)
        # print(results)

        dojo = cls(results[0])

        for row_from_db in results:

            ninja_data = {
                "id" : row_from_db['ninjas.id'],
                "first_name" : row_from_db['first_name'],
                "last_name" : row_from_db['last_name'],
                "age" : row_from_db['age'],
                "created_at" : row_from_db['ninjas.created_at'],
                "updated_at" : row_from_db['ninjas.updated_at'],
                "dojo_id": row_from_db['dojo_id']
            }
            print(ninja_data)
            dojo.ninjas.append( ninja.Ninja (ninja_data))
        return dojo