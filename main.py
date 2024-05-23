import sys
from PySide6.QtWidgets import QApplication
from database import Database
from mainwindow import MainWindow
import qtmodern.styles
import qtmodern.windows

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db=Database(dbName="ECD.sqlite", dbType="QSQLITE")
    window = MainWindow()
    qtmodern.styles.dark(app)
    styledWindow = qtmodern.windows.ModernWindow(window)
    styledWindow.show()
    sys.exit(app.exec_())