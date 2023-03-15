from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
    
    @classmethod
    def create(cls, data):
        query = "INSERT into users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL('user_cr').query_db(query, data)

    @classmethod
    def read(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL('user_cr').query_db(query)

        users = []

        for user in result:
            users.append(cls(user))

        return users
