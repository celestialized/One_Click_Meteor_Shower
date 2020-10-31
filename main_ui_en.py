# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 1024)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(20, 10, 160, 160))
        self.logoLabel.setMinimumSize(QtCore.QSize(160, 160))
        self.logoLabel.setMaximumSize(QtCore.QSize(160, 160))
        self.logoLabel.setObjectName("logoLabel")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 221, 360, 770))
        self.groupBox_3.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("color: rgb(187, 187, 187);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 108, 0);")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.folderNameText = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.folderNameText.setFont(font)
        self.folderNameText.setStyleSheet("color: rgb(255, 255, 0);")
        self.folderNameText.setReadOnly(True)
        self.folderNameText.setObjectName("folderNameText")
        self.verticalLayout_3.addWidget(self.folderNameText)
        self.selectFolderButton = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.selectFolderButton.setFont(font)
        self.selectFolderButton.setStyleSheet("background-color: rgb(205, 205, 205);\n"
"color: rgb(0, 0, 255);")
        self.selectFolderButton.setObjectName("selectFolderButton")
        self.verticalLayout_3.addWidget(self.selectFolderButton)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.listView = QtWidgets.QListView(self.groupBox_3)
        self.listView.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"color: rgb(187, 187, 187);")
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.fileNumberLabel = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.fileNumberLabel.setFont(font)
        self.fileNumberLabel.setObjectName("fileNumberLabel")
        self.verticalLayout_3.addWidget(self.fileNumberLabel)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(380, 10, 450, 981))
        self.groupBox.setMinimumSize(QtCore.QSize(360, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(187, 187, 187);")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.isEQmountCheckBox = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.isEQmountCheckBox.setFont(font)
        self.isEQmountCheckBox.setStyleSheet("color: rgb(255, 108, 0);")
        self.isEQmountCheckBox.setObjectName("isEQmountCheckBox")
        self.verticalLayout.addWidget(self.isEQmountCheckBox)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_16.setFont(font)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.doDetectionButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.doDetectionButton.setFont(font)
        self.doDetectionButton.setStyleSheet("background-color: rgb(205, 205, 205);\n"
"alternate-background-color: rgb(187, 187, 187);\n"
"color: rgb(0, 0, 255);")
        self.doDetectionButton.setObjectName("doDetectionButton")
        self.verticalLayout.addWidget(self.doDetectionButton)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setStyleSheet("background-color: rgb(187, 187, 187);")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_10.setFont(font)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 191, 0);")
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.openDetectionFolderButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.openDetectionFolderButton.setFont(font)
        self.openDetectionFolderButton.setStyleSheet("background-color: rgb(205, 205, 205);\n"
"color: rgb(0, 0, 255);")
        self.openDetectionFolderButton.setObjectName("openDetectionFolderButton")
        self.verticalLayout.addWidget(self.openDetectionFolderButton)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setStyleSheet("background-color: rgb(187, 187, 187);")
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.generateMaskButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.generateMaskButton.setFont(font)
        self.generateMaskButton.setStyleSheet("background-color: rgb(205, 205, 205);\n"
"color: rgb(0, 0, 255);")
        self.generateMaskButton.setObjectName("generateMaskButton")
        self.verticalLayout.addWidget(self.generateMaskButton)
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setStyleSheet("background-color: rgb(187, 187, 187);")
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_12.setFont(font)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(0, 191, 0);")
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.openMaskFolderButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.openMaskFolderButton.setFont(font)
        self.openMaskFolderButton.setStyleSheet("background-color: rgb(205, 205, 205);\n"
"color: rgb(0, 0, 255);")
        self.openMaskFolderButton.setObjectName("openMaskFolderButton")
        self.verticalLayout.addWidget(self.openMaskFolderButton)
        self.line_4 = QtWidgets.QFrame(self.groupBox)
        self.line_4.setStyleSheet("background-color: rgb(187, 187, 187);")
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.generateFinalButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.generateFinalButton.setFont(font)
        self.generateFinalButton.setStyleSheet("background-color: rgb(205, 205, 205);\n"
"color: rgb(0, 0, 255);")
        self.generateFinalButton.setObjectName("generateFinalButton")
        self.verticalLayout.addWidget(self.generateFinalButton)
        self.line_7 = QtWidgets.QFrame(self.groupBox)
        self.line_7.setStyleSheet("background-color: rgb(187, 187, 187);")
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout.addWidget(self.line_7)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.openFinalFolderButton = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.openFinalFolderButton.setFont(font)
        self.openFinalFolderButton.setStyleSheet("background-color: rgb(205, 205, 205);\n"
"color: rgb(0, 0, 255);")
        self.openFinalFolderButton.setObjectName("openFinalFolderButton")
        self.verticalLayout.addWidget(self.openFinalFolderButton)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(840, 11, 591, 981))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("color: rgb(187, 187, 187);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.processLogsEdit = QtWidgets.QTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.processLogsEdit.setFont(font)
        self.processLogsEdit.setAutoFillBackground(False)
        self.processLogsEdit.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"color: rgb(187, 187, 187);")
        self.processLogsEdit.setReadOnly(True)
        self.processLogsEdit.setObjectName("processLogsEdit")
        self.verticalLayout_2.addWidget(self.processLogsEdit)
        self.meteorLabel = QtWidgets.QLabel(self.centralwidget)
        self.meteorLabel.setGeometry(QtCore.QRect(180, 10, 190, 160))
        self.meteorLabel.setMinimumSize(QtCore.QSize(190, 160))
        self.meteorLabel.setMaximumSize(QtCore.QSize(190, 160))
        self.meteorLabel.setObjectName("meteorLabel")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(10, 180, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_20.setStyleSheet("color: rgb(170, 255, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto meteor shower"))
        self.logoLabel.setText(_translate("MainWindow", "Logo"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Selected image folder:"))
        self.label.setText(_translate("MainWindow", "Notice: The images need to be star-aligned !"))
        self.selectFolderButton.setText(_translate("MainWindow", "Select folder"))
        self.label_2.setText(_translate("MainWindow", "Image file list in folder (jpg / bmp / png / tif)"))
        self.fileNumberLabel.setText(_translate("MainWindow", "0 image file(s) in the list"))
        self.groupBox.setTitle(_translate("MainWindow", "Process steps"))
        self.label_4.setText(_translate("MainWindow", "Step 1: Detect meteor objects"))
        self.isEQmountCheckBox.setText(_translate("MainWindow", " Taken on equatorial mount"))
        self.label_15.setText(_translate("MainWindow", "Note:"))
        self.label_16.setText(_translate("MainWindow", "Select the above checkbox if the images were taken on an equatorial mount. Otherwise (images were taken on fixed tripod) don\'t select this option."))
        self.doDetectionButton.setText(_translate("MainWindow", "Do the detection"))
        self.label_5.setText(_translate("MainWindow", "Step 2: Manually filter detected objects"))
        self.label_3.setText(_translate("MainWindow", "Note:"))
        self.label_10.setText(_translate("MainWindow", "Some objects would still be mis-classified as a meteor. Still needs further improvement here."))
        self.label_11.setText(_translate("MainWindow", "You can delete the non-meteor objects from the \"good\" folder. And move the meteor objects from the \"removed\" folder back to the \"good\" folder."))
        self.openDetectionFolderButton.setText(_translate("MainWindow", "Open the detected folder"))
        self.label_6.setText(_translate("MainWindow", "Step 3: Generate meteor mask"))
        self.generateMaskButton.setText(_translate("MainWindow", "Generate meteor mask"))
        self.label_7.setText(_translate("MainWindow", "Step 4: Manually check the quality of the mask files"))
        self.label_13.setText(_translate("MainWindow", "Note:"))
        self.label_12.setText(_translate("MainWindow", "Some generated mask would have some \"noise\" left. And some may not cover the meteor object well."))
        self.label_14.setText(_translate("MainWindow", "You can use photo processing tool to adjust the mask files. Remove those \"noise\" by black brush. Extend the mask range with white brush if needed."))
        self.openMaskFolderButton.setText(_translate("MainWindow", "Open the mask file folder"))
        self.label_8.setText(_translate("MainWindow", "Step 5: Generate the final mask files and the combined meteor shower"))
        self.generateFinalButton.setText(_translate("MainWindow", "Generate final output"))
        self.label_9.setText(_translate("MainWindow", "Step 6: Get the final output files"))
        self.openFinalFolderButton.setText(_translate("MainWindow", "Open the final output folder"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output logs"))
        self.meteorLabel.setText(_translate("MainWindow", "Logo"))
        self.label_20.setText(_translate("MainWindow", "Auto Meteor-Shower Processing"))