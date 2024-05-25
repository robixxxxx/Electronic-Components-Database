import sys
from PySide6.QtWidgets import QApplication
from database import Database
from mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db=Database(dbName="ECD.sqlite", dbType="QSQLITE")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())