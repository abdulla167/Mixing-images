# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1208, 867)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.Add2 = QtWidgets.QPushButton(self.frame)
        self.Add2.setObjectName("Add2")
        self.gridLayout_2.addWidget(self.Add2, 0, 2, 1, 1)
        self.Add1 = QtWidgets.QPushButton(self.frame)
        self.Add1.setObjectName("Add1")
        self.gridLayout_2.addWidget(self.Add1, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Image1_display1 = QtWidgets.QLabel(self.frame)
        self.Image1_display1.setFrameShape(QtWidgets.QFrame.Panel)
        self.Image1_display1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Image1_display1.setObjectName("Image1_display1")
        self.horizontalLayout_3.addWidget(self.Image1_display1)
        self.Image1_display2 = QtWidgets.QLabel(self.frame)
        self.Image1_display2.setFrameShape(QtWidgets.QFrame.Panel)
        self.Image1_display2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Image1_display2.setObjectName("Image1_display2")
        self.horizontalLayout_3.addWidget(self.Image1_display2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Image2_display1 = QtWidgets.QLabel(self.frame)
        self.Image2_display1.setFrameShape(QtWidgets.QFrame.Panel)
        self.Image2_display1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Image2_display1.setObjectName("Image2_display1")
        self.horizontalLayout_2.addWidget(self.Image2_display1)
        self.Image2_display2 = QtWidgets.QLabel(self.frame)
        self.Image2_display2.setFrameShape(QtWidgets.QFrame.Panel)
        self.Image2_display2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Image2_display2.setObjectName("Image2_display2")
        self.horizontalLayout_2.addWidget(self.Image2_display2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 2, 1, 2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Slider2 = QtWidgets.QSlider(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider2.sizePolicy().hasHeightForWidth())
        self.Slider2.setSizePolicy(sizePolicy)
        self.Slider2.setMaximum(100)
        self.Slider2.setOrientation(QtCore.Qt.Horizontal)
        self.Slider2.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Slider2.setObjectName("Slider2")
        self.gridLayout_4.addWidget(self.Slider2, 6, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Output1_display = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Output1_display.sizePolicy().hasHeightForWidth())
        self.Output1_display.setSizePolicy(sizePolicy)
        self.Output1_display.setFrameShape(QtWidgets.QFrame.Panel)
        self.Output1_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Output1_display.setObjectName("Output1_display")
        self.gridLayout_3.addWidget(self.Output1_display, 0, 0, 1, 1)
        self.Output2_display = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Output2_display.sizePolicy().hasHeightForWidth())
        self.Output2_display.setSizePolicy(sizePolicy)
        self.Output2_display.setFrameShape(QtWidgets.QFrame.Panel)
        self.Output2_display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Output2_display.setObjectName("Output2_display")
        self.gridLayout_3.addWidget(self.Output2_display, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 1, 7, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_5)
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_7)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.Slider1 = QtWidgets.QSlider(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider1.sizePolicy().hasHeightForWidth())
        self.Slider1.setSizePolicy(sizePolicy)
        self.Slider1.setMaximum(100)
        self.Slider1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider1.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Slider1.setObjectName("Slider1")
        self.gridLayout_4.addWidget(self.Slider1, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_4)
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_6)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_image = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_image.setObjectName("menuOpen_image")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionimage1 = QtWidgets.QAction(MainWindow)
        self.actionimage1.setObjectName("actionimage1")
        self.actionimage2 = QtWidgets.QAction(MainWindow)
        self.actionimage2.setObjectName("actionimage2")
        self.menuOpen_image.addAction(self.actionimage1)
        self.menuOpen_image.addAction(self.actionimage2)
        self.menuFile.addAction(self.menuOpen_image.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Phase"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Real"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.Add2.setText(_translate("MainWindow", "Add"))
        self.Add1.setText(_translate("MainWindow", "Add"))
        self.Image1_display1.setText(_translate("MainWindow", "       image1 here"))
        self.Image1_display2.setText(_translate("MainWindow", "        image here"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Phase"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Real"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.Image2_display1.setText(_translate("MainWindow", "         image2 here"))
        self.Image2_display2.setText(_translate("MainWindow", "         image here"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "output1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "output2"))
        self.Output1_display.setText(_translate("MainWindow", "                                                   Output1"))
        self.Output2_display.setText(_translate("MainWindow", "                                                       Output2"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "image1"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "image2"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Phase"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Real"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.comboBox_7.setItemText(5, _translate("MainWindow", "Uniform_Magnitude"))
        self.comboBox_7.setItemText(6, _translate("MainWindow", "Uniform_Phase"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "image1"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "image2"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Phase"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Real"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "Uniform_Magnitude"))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "Uniform_Phase"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_image.setTitle(_translate("MainWindow", "Open image"))
        self.actionimage1.setText(_translate("MainWindow", "image1"))
        self.actionimage2.setText(_translate("MainWindow", "image2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

