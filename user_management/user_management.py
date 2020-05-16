import pymysql
import sys


class userManagement:

    def userLogin(self, username, password):
        try:
            connection = pymysql.connect(
                host=self.serverHostName, database=self.serverDatabaseName, user=self.serverDatabaseUsername, password=self.serverDatabasePassword)
            cursor = connection.cursor()

            # Definition to check if user exists or not
            def userChecker():
                checkUserCredQuery = """SELECT `secret` FROM `users` WHERE `email` = %s AND `password` = %s"""
                checkUserValue = (username, password)
                flag = cursor.execute(checkUserCredQuery, checkUserValue)

                if flag == 1:
                    result = cursor.fetchone()
                    return result[0]
                else:
                    return 0

            # definition statements
            value = userChecker()
            if value != 0:
                return value
            else:
                return 0

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

    def __init__(self, hostName, databaseName, databaseUserName, databasePassWord, theReceivedToken):
        self.serverHostName = hostName
        self.serverDatabaseName = databaseName
        self.serverDatabaseUsername = databaseUserName
        self.serverDatabasePassword = databasePassWord
