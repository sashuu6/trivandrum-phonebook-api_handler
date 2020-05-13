import pymysql


class userManagement:

    def userLogin(self, username, password):
        try:
            connection = pymysql.connect(
                host=self.serverHostName, database=self.serverDatabaseName, user=self.serverDatabaseUsername, password=self.serverDatabasePassword)
            cursor = connection.cursor()

            # Definition to check if user exists or not
            def userChecker():
                if username == "admin" and password == "admin":
                    return 1
                else:
                    return 0

            # defintion to get API key of authenticated user
            def apiKey(id):
                return id

            # definition statements
            value = userChecker()
            if value != 0:
                return apiKey(value)
            else:
                return "Invalid username or password"

        except pymysql.Error as error:
            connection.rollback()
            dupError = format(error)
            if dupError.find(' Duplicate entry') != -1:
                return "Database data error"
            else:
                return "Database error"
        finally:
            cursor.close()
            connection.close()

    def __init__(self, hostName, databaseName, databaseUserName, databasePassWord):
        self.serverHostName = hostName
        self.serverDatabaseName = databaseName
        self.serverDatabaseUsername = databaseUserName
        self.serverDatabasePassword = databasePassWord
