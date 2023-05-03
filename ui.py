# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginData.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MailMainUI(object):
    def setupUi(self, MailMainUI: QtWidgets.QMainWindow):
        MailMainUI.setObjectName("MailMainUI")
        MailMainUI.resize(800, 634)
        self.centralwidget = QtWidgets.QWidget(MailMainUI)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(180, 10, 611, 541))
        self.textBrowser.setObjectName("textBrowser")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 161, 541))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 560, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 560, 80, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        MailMainUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MailMainUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuMail = QtWidgets.QMenu(self.menubar)
        self.menuMail.setObjectName("menuMail")
        self.menuEinstellungen = QtWidgets.QMenu(self.menubar)
        self.menuEinstellungen.setObjectName("menuEinstellungen")
        self.menuSelenium = QtWidgets.QMenu(self.menubar)
        self.menuSelenium.setObjectName("menuSelenium")
        self.menuTreiber_w_hlen = QtWidgets.QMenu(self.menuSelenium)
        self.menuTreiber_w_hlen.setObjectName("menuTreiber_w_hlen")
        MailMainUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MailMainUI)
        self.statusbar.setObjectName("statusbar")
        MailMainUI.setStatusBar(self.statusbar)
        self.actionNach_Mail_suchen = QtWidgets.QAction(MailMainUI)
        self.actionNach_Mail_suchen.setObjectName("actionNach_Mail_suchen")
        self.actionAbmelden = QtWidgets.QAction(MailMainUI)
        self.actionAbmelden.setObjectName("actionAbmelden")
        self.actionRegelns = QtWidgets.QAction(MailMainUI)
        self.actionRegelns.setObjectName("actionRegelns")
        self.actionWeiterleitung = QtWidgets.QAction(MailMainUI)
        self.actionWeiterleitung.setObjectName("actionWeiterleitung")
        self.actionGeckodriver_Firefox = QtWidgets.QAction(MailMainUI)
        self.actionGeckodriver_Firefox.setObjectName(
            "actionGeckodriver_Firefox")
        self.actionChromedriver = QtWidgets.QAction(MailMainUI)
        self.actionChromedriver.setObjectName("actionChromedriver")
        self.menuMail.addAction(self.actionNach_Mail_suchen)
        self.menuMail.addAction(self.actionAbmelden)
        self.menuEinstellungen.addAction(self.actionRegelns)
        self.menuEinstellungen.addAction(self.actionWeiterleitung)
        self.menuTreiber_w_hlen.addAction(self.actionGeckodriver_Firefox)
        self.menuTreiber_w_hlen.addAction(self.actionChromedriver)
        self.menuSelenium.addAction(self.menuTreiber_w_hlen.menuAction())
        self.menubar.addAction(self.menuMail.menuAction())
        self.menubar.addAction(self.menuEinstellungen.menuAction())
        self.menubar.addAction(self.menuSelenium.menuAction())

        self.retranslateUi(MailMainUI)
        QtCore.QMetaObject.connectSlotsByName(MailMainUI)

    def retranslateUi(self, MailMainUI):
        _translate = QtCore.QCoreApplication.translate
        MailMainUI.setWindowTitle(
            _translate("MailMainUI", "Rainloop | Posteingang | 0 ungelesen"))
        self.pushButton.setText(_translate("MailMainUI", "Antworten"))
        self.pushButton_2.setText(_translate("MailMainUI", "Regeln setzen"))
        self.menuMail.setTitle(_translate("MailMainUI", "Mail"))
        self.menuEinstellungen.setTitle(
            _translate("MailMainUI", "Einstellungen"))
        self.menuSelenium.setTitle(_translate("MailMainUI", "Selenium"))
        self.menuTreiber_w_hlen.setTitle(
            _translate("MailMainUI", "Treiber wählen"))
        self.actionNach_Mail_suchen.setText(
            _translate("MailMainUI", "Nach Mail suchen"))
        self.actionAbmelden.setText(_translate("MailMainUI", "Abmelden"))
        self.actionRegelns.setText(_translate("MailMainUI", "Regeln"))
        self.actionWeiterleitung.setText(
            _translate("MailMainUI", "Weiterleitung"))
        self.actionGeckodriver_Firefox.setText(
            _translate("MailMainUI", "Geckodriver (Firefox)"))
        self.actionChromedriver.setText(
            _translate("MailMainUI", "Chromedriver"))


class Ui_AddFilter(object):
    def setupUi(self, AddFilter):
        AddFilter.setObjectName("AddFilter")
        AddFilter.resize(400, 220)
        self.lineEdit = QtWidgets.QLineEdit(AddFilter)
        self.lineEdit.setGeometry(QtCore.QRect(10, 90, 381, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(AddFilter)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 381, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(AddFilter)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 60, 381, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(AddFilter)
        self.label.setGeometry(QtCore.QRect(144, 0, 61, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddFilter)
        self.label_2.setGeometry(QtCore.QRect(140, 120, 55, 18))
        self.label_2.setObjectName("label_2")
        self.comboBox_3 = QtWidgets.QComboBox(AddFilter)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 140, 381, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton = QtWidgets.QPushButton(AddFilter)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(AddFilter)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 180, 80, 26))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(AddFilter)
        QtCore.QMetaObject.connectSlotsByName(AddFilter)

    def retranslateUi(self, AddFilter):
        _translate = QtCore.QCoreApplication.translate
        AddFilter.setWindowTitle(_translate("AddFilter", "Filter hinzufügen"))
        self.comboBox.setItemText(0, _translate("AddFilter", "Betreff"))
        self.comboBox.setItemText(1, _translate("AddFilter", "Absender"))
        self.comboBox.setItemText(2, _translate("AddFilter", "Inhalt"))
        self.comboBox_2.setItemText(0, _translate("AddFilter", "Ist"))
        self.comboBox_2.setItemText(1, _translate("AddFilter", "Ist nicht"))
        self.comboBox_2.setItemText(2, _translate("AddFilter", "Enthält"))
        self.comboBox_2.setItemText(3, _translate("AddFilter",
                                                  "Enthält nicht"))
        self.label.setText(_translate("AddFilter", "WENN"))
        self.label_2.setText(_translate("AddFilter", "DANN"))
        self.comboBox_3.setItemText(
            0, _translate("AddFilter", "Behalte die Nachricht"))
        self.comboBox_3.setItemText(
            1, _translate("AddFilter", "Beende die Filterung"))
        self.comboBox_3.setItemText(
            2, _translate("AddFilter", "Lösche die Nachricht"))
        self.pushButton.setText(_translate("AddFilter", "Hinzufügen"))
        self.pushButton_2.setText(_translate("AddFilter", "Abbrechen"))


class Ui_SendMailUI(object):
    def setupUi(self, SendMailUI):
        SendMailUI.setObjectName("SendMailUI")
        SendMailUI.resize(800, 599)
        self.centralwidget = QtWidgets.QWidget(SendMailUI)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 70, 791, 481))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 151, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 10, 55, 18))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 10, 521, 24))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 55, 18))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 40, 551, 24))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 40, 80, 26))
        self.pushButton.setObjectName("pushButton")
        SendMailUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SendMailUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        SendMailUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SendMailUI)
        self.statusbar.setObjectName("statusbar")
        SendMailUI.setStatusBar(self.statusbar)

        self.retranslateUi(SendMailUI)
        QtCore.QMetaObject.connectSlotsByName(SendMailUI)

    def retranslateUi(self, SendMailUI):
        _translate = QtCore.QCoreApplication.translate
        SendMailUI.setWindowTitle(
            _translate("SendMailUI", "Rainloop | Neue Mail"))
        self.label.setText(_translate("SendMailUI", "Empfänger"))
        self.label_2.setText(_translate("SendMailUI", "CC"))
        self.label_3.setText(_translate("SendMailUI", "Betreff"))
        self.pushButton.setText(_translate("SendMailUI", "Senden"))


class Ui_MailRules(object):
    def setupUi(self, MailRules):
        MailRules.setObjectName("MailRules")
        MailRules.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MailRules)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 520, 80, 26))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 461, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 101, 18))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 141, 22))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 60, 581, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 110, 55, 18))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 90, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 130, 256, 291))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 150, 191, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 180, 191, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        MailRules.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MailRules)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MailRules.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MailRules)
        self.statusbar.setObjectName("statusbar")
        MailRules.setStatusBar(self.statusbar)

        self.retranslateUi(MailRules)
        QtCore.QMetaObject.connectSlotsByName(MailRules)

    def retranslateUi(self, MailRules):
        _translate = QtCore.QCoreApplication.translate
        MailRules.setWindowTitle(_translate("MailRules", "Regeln festlegen"))
        self.pushButton.setText(_translate("MailRules", "Anwenden"))
        self.lineEdit.setToolTip(
            _translate("MailRules", "E-Mail Adressen (Durch Komma getrennt)"))
        self.label.setText(_translate("MailRules", "E-Mail Adressen:"))
        self.checkBox.setText(_translate("MailRules", "E-Mails weiterleiten"))
        self.checkBox_2.setText(
            _translate(
                "MailRules",
                "Immer weiterleiten (Weiterleitung von Mails vor Anwendung von Filtern)"
            ))
        self.label_2.setText(_translate("MailRules", "Filter"))
        self.pushButton_2.setText(
            _translate("MailRules", "Ausgewählte Filter löschen"))
        self.pushButton_3.setText(_translate("MailRules", "Filter hinzufügen"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 331)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 381, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.passwd = QtWidgets.QLineEdit(self.centralwidget)
        self.passwd.setGeometry(QtCore.QRect(10, 120, 381, 24))
        self.passwd.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setClearButtonEnabled(False)
        self.passwd.setObjectName("passwd")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 100, 61, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 101, 18))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 250, 80, 26))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "RainLoop | Anmelden"))
        self.label.setText(_translate("MainWindow", "Passwort"))
        self.label_2.setText(_translate("MainWindow", "Nutzername"))
        self.pushButton.setText(_translate("MainWindow", "Anmelden"))
