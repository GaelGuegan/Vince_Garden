# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QSplitter, QTimeEdit,
    QWidget)
import rc_resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(653, 527)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBoxVanne = QComboBox(self.centralwidget)
        self.comboBoxVanne.addItem("")
        self.comboBoxVanne.addItem("")
        self.comboBoxVanne.addItem("")
        self.comboBoxVanne.setObjectName(u"comboBoxVanne")
        self.comboBoxVanne.setGeometry(QRect(40, 40, 111, 25))
        self.comboBoxVanne.setEditable(False)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 80, 521, 361))
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 20, 481, 141))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.splitter_3 = QSplitter(self.groupBox_3)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(20, 40, 231, 26))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_6 = QLabel(self.splitter_3)
        self.label_6.setObjectName(u"label_6")
        self.splitter_3.addWidget(self.label_6)
        self.spinBoxManualSeconds = QSpinBox(self.splitter_3)
        self.spinBoxManualSeconds.setObjectName(u"spinBoxManualSeconds")
        self.spinBoxManualSeconds.setSingleStep(5)
        self.spinBoxManualSeconds.setValue(5)
        self.splitter_3.addWidget(self.spinBoxManualSeconds)
        self.label_7 = QLabel(self.splitter_3)
        self.label_7.setObjectName(u"label_7")
        self.splitter_3.addWidget(self.label_7)
        self.splitter_5 = QSplitter(self.groupBox_3)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(270, 90, 191, 23))
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.label_8 = QLabel(self.splitter_5)
        self.label_8.setObjectName(u"label_8")
        self.splitter_5.addWidget(self.label_8)
        self.lcdNumberTimeout = QLCDNumber(self.splitter_5)
        self.lcdNumberTimeout.setObjectName(u"lcdNumberTimeout")
        self.splitter_5.addWidget(self.lcdNumberTimeout)
        self.splitter_4 = QSplitter(self.groupBox_3)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(20, 82, 171, 41))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label_9 = QLabel(self.splitter_4)
        self.label_9.setObjectName(u"label_9")
        self.splitter_4.addWidget(self.label_9)
        self.pushButtonManualStart = QPushButton(self.splitter_4)
        self.pushButtonManualStart.setObjectName(u"pushButtonManualStart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonManualStart.sizePolicy().hasHeightForWidth())
        self.pushButtonManualStart.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/start.jpg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/stop.jpg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButtonManualStart.setIcon(icon)
        self.pushButtonManualStart.setIconSize(QSize(30, 30))
        self.pushButtonManualStart.setCheckable(True)
        self.pushButtonManualStart.setChecked(False)
        self.splitter_4.addWidget(self.pushButtonManualStart)
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 190, 481, 141))
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.splitter_2 = QSplitter(self.groupBox_4)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(10, 90, 359, 26))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.labelQuantity = QLabel(self.splitter_2)
        self.labelQuantity.setObjectName(u"labelQuantity")
        self.splitter_2.addWidget(self.labelQuantity)
        self.spinBoxQuantity = QSpinBox(self.splitter_2)
        self.spinBoxQuantity.setObjectName(u"spinBoxQuantity")
        self.splitter_2.addWidget(self.spinBoxQuantity)
        self.labelQuantityUnits = QLabel(self.splitter_2)
        self.labelQuantityUnits.setObjectName(u"labelQuantityUnits")
        self.splitter_2.addWidget(self.labelQuantityUnits)
        self.widget = QWidget(self.groupBox_4)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 40, 371, 28))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBoxDays = QComboBox(self.widget)
        self.comboBoxDays.addItem("")
        self.comboBoxDays.addItem("")
        self.comboBoxDays.addItem("")
        self.comboBoxDays.addItem("")
        self.comboBoxDays.addItem("")
        self.comboBoxDays.addItem("")
        self.comboBoxDays.addItem("")
        self.comboBoxDays.setObjectName(u"comboBoxDays")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBoxDays.sizePolicy().hasHeightForWidth())
        self.comboBoxDays.setSizePolicy(sizePolicy2)
        self.comboBoxDays.setMinimumSize(QSize(60, 0))

        self.horizontalLayout.addWidget(self.comboBoxDays)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.timeEditPlanningTime = QTimeEdit(self.widget)
        self.timeEditPlanningTime.setObjectName(u"timeEditPlanningTime")
        self.timeEditPlanningTime.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(16, 30, 0)))
        self.timeEditPlanningTime.setTime(QTime(16, 30, 0))

        self.horizontalLayout.addWidget(self.timeEditPlanningTime)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButtonManualStart.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBoxVanne.setItemText(0, QCoreApplication.translate("MainWindow", u"Vanne 1", None))
        self.comboBoxVanne.setItemText(1, QCoreApplication.translate("MainWindow", u"Vanne 2", None))
        self.comboBoxVanne.setItemText(2, QCoreApplication.translate("MainWindow", u"Vanne 3", None))

        self.groupBox.setTitle("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Arrosage manuel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ouvrir pendant ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"secondes.", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Timeout", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Marchet / Arr\u00eat", None))
        self.pushButtonManualStart.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Planning", None))
        self.labelQuantity.setText(QCoreApplication.translate("MainWindow", u"Quantit\u00e9:", None))
        self.labelQuantityUnits.setText(QCoreApplication.translate("MainWindow", u"cL.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tous les", None))
        self.comboBoxDays.setItemText(0, QCoreApplication.translate("MainWindow", u"Lundi", None))
        self.comboBoxDays.setItemText(1, QCoreApplication.translate("MainWindow", u"Mardi", None))
        self.comboBoxDays.setItemText(2, QCoreApplication.translate("MainWindow", u"Mercredi", None))
        self.comboBoxDays.setItemText(3, QCoreApplication.translate("MainWindow", u"Jeudi", None))
        self.comboBoxDays.setItemText(4, QCoreApplication.translate("MainWindow", u"Vendredi", None))
        self.comboBoxDays.setItemText(5, QCoreApplication.translate("MainWindow", u"Samedi", None))
        self.comboBoxDays.setItemText(6, QCoreApplication.translate("MainWindow", u"Dimanche", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"jours \u00e0 ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"heures.", None))
    # retranslateUi

