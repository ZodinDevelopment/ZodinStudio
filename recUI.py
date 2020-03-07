# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recorder.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(208, 121)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.recButton = QtWidgets.QPushButton(self.centralwidget)
        self.recButton.setEnabled(True)
        self.recButton.setCheckable(False)
        self.recButton.setChecked(False)
        self.recButton.setDefault(False)
        self.recButton.setFlat(False)
        self.recButton.setObjectName("recButton")
        self.verticalLayout.addWidget(self.recButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setEnabled(False)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout.addWidget(self.stopButton)
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setObjectName("playButton")
        self.verticalLayout.addWidget(self.playButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.saveButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 208, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionNew)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.recButton.clicked['bool'].connect(self.stopButton.setDisabled)
        self.recButton.clicked['bool'].connect(self.recButton.setEnabled)
        self.stopButton.clicked['bool'].connect(self.recButton.setDisabled)
        self.stopButton.clicked['bool'].connect(self.stopButton.setEnabled)
        self.recButton.clicked['bool'].connect(self.playButton.setEnabled)
        self.stopButton.clicked['bool'].connect(self.playButton.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recorder"))
        self.recButton.setText(_translate("MainWindow", "Start Recording"))
        self.stopButton.setText(_translate("MainWindow", "Stop Recording"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.saveButton.setText(_translate("MainWindow", "Save File"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save As"))
        self.actionNew.setText(_translate("MainWindow", "New.."))
