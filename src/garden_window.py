
from src.ui_mainwindow import Ui_MainWindow
from src.relay import Relay

class GardenWindow(Ui_MainWindow):

        def __init__(self):
            super().__init__()
            self.relay_1 = Relay(1, "Vanne 1")
            self.relay_2 = Relay(2, "Vanne 2")
            self.relay_3 = Relay(3, "Vanne 3")

        def setupUi(self, MainWindow):
            super().setupUi(MainWindow)
            self.pushButtonManualStart.clicked.connect(self.manual_open)
            self.spinBoxManualSeconds.valueChanged.connect(self.manual_set_value)
            self.comboBox.currentTextChanged.connect(self.select_vanne)

        def _get_current_vanne(self):
             return self.comboBox.currentText()

        def select_vanne(self):
            if self._get_current_vanne() == self.relay_1.get_name():
                self.set_fields(self.relay_1)
            elif self._get_current_vanne() == self.relay_2.get_name():
                self.set_fields(self.relay_2)
            elif self._get_current_vanne() == self.relay_3.get_name():
                self.set_fields(self.relay_3)

        def set_fields(self, relay):
            self.spinBoxManualSeconds.setValue(relay.manual_get_timeout_sec())

        def manual_open(self):
            if self._get_current_vanne() == self.relay_1.get_name():
                self.relay_1.manual_open()
            elif self._get_current_vanne() == self.relay_2.get_name():
                self.relay_2.manual_open()
            elif self._get_current_vanne() == self.relay_3.get_name():
                self.relay_3.manual_open()

        def manual_set_value(self, val):
            if self._get_current_vanne() ==  self.relay_1.get_name():
                self.relay_1.manual_set_timeout_sec(val)
            elif self._get_current_vanne() ==  self.relay_2.get_name():
                self.relay_2.manual_set_timeout_sec(val)
            elif self._get_current_vanne() ==  self.relay_3.get_name():
                self.relay_3.manual_set_timeout_sec(val)