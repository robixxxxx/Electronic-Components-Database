from PyQt5.QtWidgets import QWidget
from stateChangeForm_ui import Ui_increaseReduce

class StateChange(QWidget, Ui_increaseReduce):
    def __init__(self):
        super(StateChange, self).__init__()
        self.setupUi(self)
        self.buttonBox.rejected.connect(lambda: self.close())
    def getValue(self):
        return self.spinBox.value()
        