import mysql.connector
class DBConnection:
    @staticmethod
    def getConnection():
        database = mysql.connector.connect(host="localhost", user="root", passwd="", db='tbpa')
        return database
if __name__=="__main__":
    print(DBConnection.getConnection())