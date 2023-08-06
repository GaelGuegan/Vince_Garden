from PySide6.QtCore import (QTimer, QSize)
from PySide6.QtGui import (QIcon, QPixmap)

import src.rc_resource
from src.ui_mainwindow import Ui_MainWindow
from src.relay import Relay

from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.qt import QtScheduler
from apscheduler.schedulers.background import BackgroundScheduler


class GardenWindow(Ui_MainWindow):

        def __init__(self):
            super().__init__()
            self.relay_1 = Relay(1, "Vanne 1")
            self.relay_2 = Relay(2, "Vanne 2")
            self.relay_3 = Relay(3, "Vanne 3")
            self.manual_timer = QTimer()
            self.scheduler = BackgroundScheduler()

        def setupUi(self, MainWindow):
            super().setupUi(MainWindow)
            self.pushButtonManualStart.clicked.connect(self.manual_open)
            self.spinBoxManualSeconds.valueChanged.connect(self.manual_set_value)
            self.comboBoxVanne.currentTextChanged.connect(self.select_vanne)
            self.manual_timer.timeout.connect(self.manual_update_timer)
            self.comboBoxDays.currentTextChanged.connect(self.auto_launch)
            self.timeEditPlanningTime.dateTimeChanged.connect(self.auto_launch)
            #currentTextChanged.connect(self.auto_launch)
            #icon = QIcon(QPixmap(":/icons/start.jpg"))
            # icon = QIcon()
            # icon.addFile(u":/icons/stop.jpg", QSize(), QIcon.Normal, QIcon.Off)
            # icon.addFile(u":/icons/start.jpg", QSize(), QIcon.Normal, QIcon.On)
            # self.pushButtonManualStart.setIcon(icon)
            self.auto_launch()

        def _get_current_vanne(self):
             return self.comboBoxVanne.currentText()

        def select_vanne(self):
            if self._get_current_vanne() == self.relay_1.get_name():
                self.set_fields(self.relay_1)
            elif self._get_current_vanne() == self.relay_2.get_name():
                self.set_fields(self.relay_2)
            elif self._get_current_vanne() == self.relay_3.get_name():
                self.set_fields(self.relay_3)

        def set_fields(self, relay):
            self.spinBoxManualSeconds.setValue(relay.manual_get_timeout_sec())

        def vanne_open(self):
            if self._get_current_vanne() == self.relay_1.get_name():
                self.relay_1.open()
            elif self._get_current_vanne() == self.relay_2.get_name():
                self.relay_2.open()
            elif self._get_current_vanne() == self.relay_3.get_name():
                self.relay_3.open()

        def manual_open(self):
            if self.pushButtonManualStart.isChecked():
                self.vanne_open()
                self.manual_timer.start(100)
            else:
                self.manual_close()
                self.manual_timer.stop()
                self.lcdNumberTimeout.display(0)

            self.scheduler.print_jobs()

        def manual_close(self):
            if self._get_current_vanne() == self.relay_1.get_name():
                self.relay_1.close()
            elif self._get_current_vanne() == self.relay_2.get_name():
                self.relay_2.close()
            elif self._get_current_vanne() == self.relay_3.get_name():
                self.relay_3.close()
            self.pushButtonManualStart.setChecked(False)

        def manual_update_timer(self):
            self.lcdNumberTimeout.display(self.lcdNumberTimeout.value() + 0.1)
            if self.lcdNumberTimeout.intValue() == self.spinBoxManualSeconds.value():
                self.manual_timer.stop()
                self.lcdNumberTimeout.display(0)
                self.manual_close()

        def manual_set_value(self, val):
            if self._get_current_vanne() ==  self.relay_1.get_name():
                self.relay_1.manual_set_timeout_sec(val)
            elif self._get_current_vanne() ==  self.relay_2.get_name():
                self.relay_2.manual_set_timeout_sec(val)
            elif self._get_current_vanne() ==  self.relay_3.get_name():
                self.relay_3.manual_set_timeout_sec(val)

        def auto_launch(self):
            if self.scheduler.running is True:
                self.scheduler.shutdown()
            self.scheduler.add_job(self.manual_open, 'cron', day_of_week=self.comboBoxDays.currentIndex(),second=5)
            self.scheduler.start()
            print(self.scheduler.print_jobs())