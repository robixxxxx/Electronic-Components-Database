from PyQt5.QtSql import *
from PyQt5.QtWidgets import QMessageBox

class Database(QSqlDatabase):
    def __init__(self, dbName: str, dbType: str, parent=None)->None:
        super().__init__()
        self.dbName = dbName
        self.connection = self.addDatabase(dbType)
        self.connection.setDatabaseName(dbName)
        if not self.connection.open():
            QMessageBox.critical(None, "ECR - ERROR!", "Database Error: %s" % self.connection.lastError().databaseText())
        query = "CREATE TABLE IF NOT EXISTS components (id INTEGER PRIMARY KEY AUTOINCREMENT, element TEXT, value TEXT, category TEXT, mount TEXT, package TEXT, price REAL, qty REAL, unit TEXT, min REAL, docs TEXT, comment TEXT);"

        # query = "CREATE TABLE IF NOT EXISTS components(id INT PRIMARY KEY AUTOINCREMENT, element VARCHAR(20), value VARCHAR(20), category VARCHAR(20), mount VARCHAR(20), package VARCHAR(20), price REAL, qty REAL, unit VARCHAR(20), min REAL, docs VARCHAR(50), comment VARCHAR(100))"
        self.query(query)
        
    def insert(self, data:list[str]):
        query = "INSET INTO " + self.dbName + " values("
        for i in data:
            query += i
            if i!=data[-1]:
                query += ", "
            else:
                query += ")"
        self.query(query)
        
    def delete(self, id):
        query = "DELETE from " + self.dbName + " WHERE id = " + id
        self.query(query)
        
    def select(self, tableName:str, columns: (list[str] | None), filters: (list[str] | None), duplicatesAllowed: bool = True) -> QSqlQueryModel:
        query = "SELECT "
        if not duplicatesAllowed:
            query += "DISTINCT "
        if columns!=None:
            for column in columns:
                query += column
                if column != columns[-1]:
                    query += ", "
                else:
                    query += " "
        else:
            query += "* "
        query += "FROM " + tableName
        if len(filters)>0:
            query += " WHERE "
            for filter in filters:
                query += filter
                if filter!=filters[-1]:
                    query += " AND "
        query += ";"
        return self.query(query)
    
    def query(self, query:str, modelReturn:bool = False) -> QSqlQueryModel:
        sqlQuery = QSqlQuery(self)
        sqlQuery.prepare(query)
        sqlQuery.exec()
        if modelReturn:
            model = QSqlQueryModel()
            model.setQuery(sqlQuery)
            return model