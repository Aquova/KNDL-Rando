# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 475)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 18, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 16, 0, 1, 1)
        self.randomizeButton = QtWidgets.QPushButton(self.centralWidget)
        self.randomizeButton.setObjectName("randomizeButton")
        self.gridLayout.addWidget(self.randomizeButton, 17, 0, 1, 1)
        self.starRodCheck = QtWidgets.QCheckBox(self.centralWidget)
        self.starRodCheck.setObjectName("starRodCheck")
        self.gridLayout.addWidget(self.starRodCheck, 8, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 15, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 13, 0, 1, 1)
        self.urlLabel = QtWidgets.QLabel(self.centralWidget)
        self.urlLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.urlLabel.setObjectName("urlLabel")
        self.gridLayout.addWidget(self.urlLabel, 19, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.romDisplay = QtWidgets.QLineEdit(self.centralWidget)
        self.romDisplay.setReadOnly(True)
        self.romDisplay.setObjectName("romDisplay")
        self.horizontalLayout_2.addWidget(self.romDisplay)
        self.findROMButton = QtWidgets.QPushButton(self.centralWidget)
        self.findROMButton.setObjectName("findROMButton")
        self.horizontalLayout_2.addWidget(self.findROMButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 14, 0, 1, 1)
        self.title = QtWidgets.QLabel(self.centralWidget)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 20, 0, 1, 1)
        self.enemyCheck = QtWidgets.QCheckBox(self.centralWidget)
        self.enemyCheck.setObjectName("enemyCheck")
        self.gridLayout.addWidget(self.enemyCheck, 6, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 12, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.kirbyColorLabel = QtWidgets.QLabel(self.centralWidget)
        self.kirbyColorLabel.setObjectName("kirbyColorLabel")
        self.horizontalLayout_3.addWidget(self.kirbyColorLabel)
        self.kirbyComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.kirbyComboBox.setObjectName("kirbyComboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/pinkSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/redSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/orangeSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/yellowSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/greenSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/cherrySprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/emeraldSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/oceanSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/sapphireSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/grapeSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/chocolateSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/chalkSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon11, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/snowSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon12, "")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/carbonSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon13, "")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/mirrorSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon14, "")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/stoneSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon15, "")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/iceSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon16, "")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/metaKnightSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon17, "")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/KDL3pinkSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon18, "")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("icons/KDL3blueSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon19, "")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("icons/waddleDeeSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon20, "")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("icons/lololoSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon21, "")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("icons/lalalaSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon22, "")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("icons/grayscaleSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon23, "")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("icons/randomSprayCan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kirbyComboBox.addItem(icon24, "")
        self.horizontalLayout_3.addWidget(self.kirbyComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 10, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.seedLabel = QtWidgets.QLabel(self.centralWidget)
        self.seedLabel.setObjectName("seedLabel")
        self.horizontalLayout.addWidget(self.seedLabel)
        self.seedValue = QtWidgets.QLineEdit(self.centralWidget)
        self.seedValue.setObjectName("seedValue")
        self.horizontalLayout.addWidget(self.seedValue)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 9, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.MKcolorLabel = QtWidgets.QLabel(self.centralWidget)
        self.MKcolorLabel.setObjectName("MKcolorLabel")
        self.horizontalLayout_4.addWidget(self.MKcolorLabel)
        self.MKcomboBox = QtWidgets.QComboBox(self.centralWidget)
        self.MKcomboBox.setObjectName("MKcomboBox")
        self.MKcomboBox.addItem("")
        self.MKcomboBox.addItem("")
        self.MKcomboBox.addItem("")
        self.MKcomboBox.addItem("")
        self.MKcomboBox.addItem("")
        self.MKcomboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.MKcomboBox)
        self.gridLayout.addLayout(self.horizontalLayout_4, 11, 0, 1, 1)
        self.noAbilitiesCheck = QtWidgets.QCheckBox(self.centralWidget)
        self.noAbilitiesCheck.setObjectName("noAbilitiesCheck")
        self.gridLayout.addWidget(self.noAbilitiesCheck, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kirby: Nightmare in Dream Land Randomizer"))
        self.randomizeButton.setText(_translate("MainWindow", "Randomize!"))
        self.starRodCheck.setText(_translate("MainWindow", "Use Star Rod"))
        self.urlLabel.setText(_translate("MainWindow", "https://github.com/Aquova/KNDL-Rando"))
        self.findROMButton.setText(_translate("MainWindow", "Choose ROM Location"))
        self.title.setText(_translate("MainWindow", "Kirby: Nightmare in Dream Land Randomizer - Version: "))
        self.enemyCheck.setText(_translate("MainWindow", "Randomize Enemies"))
        self.kirbyColorLabel.setText(_translate("MainWindow", "Kirby Color:"))
        self.kirbyComboBox.setItemText(0, _translate("MainWindow", "Default (Pink)"))
        self.kirbyComboBox.setItemText(1, _translate("MainWindow", "Red"))
        self.kirbyComboBox.setItemText(2, _translate("MainWindow", "Orange"))
        self.kirbyComboBox.setItemText(3, _translate("MainWindow", "Yellow"))
        self.kirbyComboBox.setItemText(4, _translate("MainWindow", "Green"))
        self.kirbyComboBox.setItemText(5, _translate("MainWindow", "Cherry"))
        self.kirbyComboBox.setItemText(6, _translate("MainWindow", "Emerald"))
        self.kirbyComboBox.setItemText(7, _translate("MainWindow", "Ocean"))
        self.kirbyComboBox.setItemText(8, _translate("MainWindow", "Sapphire"))
        self.kirbyComboBox.setItemText(9, _translate("MainWindow", "Grape"))
        self.kirbyComboBox.setItemText(10, _translate("MainWindow", "Chocolate"))
        self.kirbyComboBox.setItemText(11, _translate("MainWindow", "Chalk"))
        self.kirbyComboBox.setItemText(12, _translate("MainWindow", "Snow"))
        self.kirbyComboBox.setItemText(13, _translate("MainWindow", "Carbon"))
        self.kirbyComboBox.setItemText(14, _translate("MainWindow", "Mirror"))
        self.kirbyComboBox.setItemText(15, _translate("MainWindow", "Stone"))
        self.kirbyComboBox.setItemText(16, _translate("MainWindow", "Ice"))
        self.kirbyComboBox.setItemText(17, _translate("MainWindow", "Meta Knight"))
        self.kirbyComboBox.setItemText(18, _translate("MainWindow", "Kirby\'s Dream Land 3 Pink"))
        self.kirbyComboBox.setItemText(19, _translate("MainWindow", "Kirby\'s Dream Land 3 Blue"))
        self.kirbyComboBox.setItemText(20, _translate("MainWindow", "Waddle Dee"))
        self.kirbyComboBox.setItemText(21, _translate("MainWindow", "Lololo"))
        self.kirbyComboBox.setItemText(22, _translate("MainWindow", "Lalala"))
        self.kirbyComboBox.setItemText(23, _translate("MainWindow", "Grayscale"))
        self.kirbyComboBox.setItemText(24, _translate("MainWindow", "Random"))
        self.seedLabel.setText(_translate("MainWindow", "Seed:"))
        self.MKcolorLabel.setText(_translate("MainWindow", "Meta Knight Color:"))
        self.MKcomboBox.setItemText(0, _translate("MainWindow", "Default"))
        self.MKcomboBox.setItemText(1, _translate("MainWindow", "Kirby"))
        self.MKcomboBox.setItemText(2, _translate("MainWindow", "White"))
        self.MKcomboBox.setItemText(3, _translate("MainWindow", "Red"))
        self.MKcomboBox.setItemText(4, _translate("MainWindow", "Green"))
        self.MKcomboBox.setItemText(5, _translate("MainWindow", "Mirror"))
        self.noAbilitiesCheck.setText(_translate("MainWindow", "Enemies give no abilities"))

