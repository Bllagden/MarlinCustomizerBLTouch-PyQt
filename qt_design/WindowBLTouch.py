# Form implementation generated from reading ui file 'WindowBLTouch.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BLTouch(object):
    def setupUi(self, BLTouch):
        BLTouch.setObjectName("BLTouch")
        BLTouch.resize(700, 750)
        BLTouch.setStyleSheet("QWidget {    \n"
                              "    color: white;\n"
                              "    background-color: #121212;\n"
                              "    font-size: 8pt;\n"
                              "    font-weight: 600;\n"
                              "}\n"
                              "\n"
                              "QPushButton {    \n"
                              "    border-style: solid;\n"
                              "    border-width: 3px;\n"
                              "    border-radius: 5px;\n"
                              "    border-color: #38BD80;\n"
                              "    font: bold 16px;\n"
                              "}\n"
                              "\n"
                              "QPushButton:hover {    \n"
                              "    background-color: #292927;\n"
                              "}")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(BLTouch)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem)
        self.label_bltouch_0_1 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_0_1.setStyleSheet("font-size: 11pt;")
        self.label_bltouch_0_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_bltouch_0_1.setObjectName("label_bltouch_0_1")
        self.verticalLayout_13.addWidget(self.label_bltouch_0_1)
        self.label_bltouch_0_2 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_0_2.setStyleSheet("font-size: 11pt;")
        self.label_bltouch_0_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_bltouch_0_2.setObjectName("label_bltouch_0_2")
        self.verticalLayout_13.addWidget(self.label_bltouch_0_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_bltouch_1 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_1.setStyleSheet("font-size: 11pt;")
        self.label_bltouch_1.setObjectName("label_bltouch_1")
        self.verticalLayout_3.addWidget(self.label_bltouch_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_bltouch_1_1 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_1_1.setStyleSheet("")
        self.label_bltouch_1_1.setObjectName("label_bltouch_1_1")
        self.verticalLayout_2.addWidget(self.label_bltouch_1_1)
        self.label_bltouch_1_2 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_1_2.setObjectName("label_bltouch_1_2")
        self.verticalLayout_2.addWidget(self.label_bltouch_1_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_bltouch_1_1 = QtWidgets.QLineEdit(BLTouch)
        self.lineEdit_bltouch_1_1.setObjectName("lineEdit_bltouch_1_1")
        self.verticalLayout.addWidget(self.lineEdit_bltouch_1_1)
        self.lineEdit_bltouch_1_2 = QtWidgets.QLineEdit(BLTouch)
        self.lineEdit_bltouch_1_2.setObjectName("lineEdit_bltouch_1_2")
        self.verticalLayout.addWidget(self.lineEdit_bltouch_1_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_13.addLayout(self.verticalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_bltouch_2 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_2.setStyleSheet("font-size: 11pt;")
        self.label_bltouch_2.setObjectName("label_bltouch_2")
        self.verticalLayout_5.addWidget(self.label_bltouch_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_bltouch_2_1 = QtWidgets.QRadioButton(BLTouch)
        self.radioButton_bltouch_2_1.setObjectName("radioButton_bltouch_2_1")
        self.buttonGroup_bltouch_2 = QtWidgets.QButtonGroup(BLTouch)
        self.buttonGroup_bltouch_2.setObjectName("buttonGroup_bltouch_2")
        self.buttonGroup_bltouch_2.addButton(self.radioButton_bltouch_2_1)
        self.verticalLayout_4.addWidget(self.radioButton_bltouch_2_1)
        self.radioButton_bltouch_2_2 = QtWidgets.QRadioButton(BLTouch)
        self.radioButton_bltouch_2_2.setChecked(True)
        self.radioButton_bltouch_2_2.setObjectName("radioButton_bltouch_2_2")
        self.buttonGroup_bltouch_2.addButton(self.radioButton_bltouch_2_2)
        self.verticalLayout_4.addWidget(self.radioButton_bltouch_2_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_13.addLayout(self.verticalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem4)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_bltouch_3 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_3.setStyleSheet("font-size: 11pt;")
        self.label_bltouch_3.setObjectName("label_bltouch_3")
        self.verticalLayout_7.addWidget(self.label_bltouch_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButton_bltouch_3_1 = QtWidgets.QRadioButton(BLTouch)
        self.radioButton_bltouch_3_1.setObjectName("radioButton_bltouch_3_1")
        self.buttonGroup_bltouch_3 = QtWidgets.QButtonGroup(BLTouch)
        self.buttonGroup_bltouch_3.setObjectName("buttonGroup_bltouch_3")
        self.buttonGroup_bltouch_3.addButton(self.radioButton_bltouch_3_1)
        self.verticalLayout_6.addWidget(self.radioButton_bltouch_3_1)
        self.radioButton_bltouch_3_2 = QtWidgets.QRadioButton(BLTouch)
        self.radioButton_bltouch_3_2.setObjectName("radioButton_bltouch_3_2")
        self.buttonGroup_bltouch_3.addButton(self.radioButton_bltouch_3_2)
        self.verticalLayout_6.addWidget(self.radioButton_bltouch_3_2)
        self.radioButton_bltouch_3_3 = QtWidgets.QRadioButton(BLTouch)
        self.radioButton_bltouch_3_3.setChecked(True)
        self.radioButton_bltouch_3_3.setObjectName("radioButton_bltouch_3_3")
        self.buttonGroup_bltouch_3.addButton(self.radioButton_bltouch_3_3)
        self.verticalLayout_6.addWidget(self.radioButton_bltouch_3_3)
        self.radioButton_bltouch_3_4 = QtWidgets.QRadioButton(BLTouch)
        self.radioButton_bltouch_3_4.setObjectName("radioButton_bltouch_3_4")
        self.buttonGroup_bltouch_3.addButton(self.radioButton_bltouch_3_4)
        self.verticalLayout_6.addWidget(self.radioButton_bltouch_3_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_13.addLayout(self.verticalLayout_7)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem5)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_bltouch_4 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_4.setStyleSheet("font-size: 11pt;")
        self.label_bltouch_4.setObjectName("label_bltouch_4")
        self.verticalLayout_9.addWidget(self.label_bltouch_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.radioButton_bltouch_4_1 = QtWidgets.QRadioButton(BLTouch)
        self.radioButton_bltouch_4_1.setObjectName("radioButton_bltouch_4_1")
        self.buttonGroup_bltouch_4 = QtWidgets.QButtonGroup(BLTouch)
        self.buttonGroup_bltouch_4.setObjectName("buttonGroup_bltouch_4")
        self.buttonGroup_bltouch_4.addButton(self.radioButton_bltouch_4_1)
        self.verticalLayout_8.addWidget(self.radioButton_bltouch_4_1)
        self.radioButton_bltouch_4_2 = QtWidgets.QRadioButton(BLTouch)
        self.radioButton_bltouch_4_2.setChecked(True)
        self.radioButton_bltouch_4_2.setObjectName("radioButton_bltouch_4_2")
        self.buttonGroup_bltouch_4.addButton(self.radioButton_bltouch_4_2)
        self.verticalLayout_8.addWidget(self.radioButton_bltouch_4_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem6)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_bltouch_5 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_5.setStyleSheet("font-size: 11pt;")
        self.label_bltouch_5.setObjectName("label_bltouch_5")
        self.verticalLayout_12.addWidget(self.label_bltouch_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_bltouch_5_1 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_5_1.setObjectName("label_bltouch_5_1")
        self.verticalLayout_10.addWidget(self.label_bltouch_5_1)
        self.label_bltouch_5_2 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_5_2.setObjectName("label_bltouch_5_2")
        self.verticalLayout_10.addWidget(self.label_bltouch_5_2)
        self.label_bltouch_5_3 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_5_3.setObjectName("label_bltouch_5_3")
        self.verticalLayout_10.addWidget(self.label_bltouch_5_3)
        self.label_bltouch_5_4 = QtWidgets.QLabel(BLTouch)
        self.label_bltouch_5_4.setObjectName("label_bltouch_5_4")
        self.verticalLayout_10.addWidget(self.label_bltouch_5_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.lineEdit_bltouch_5_1 = QtWidgets.QLineEdit(BLTouch)
        self.lineEdit_bltouch_5_1.setObjectName("lineEdit_bltouch_5_1")
        self.verticalLayout_11.addWidget(self.lineEdit_bltouch_5_1)
        self.lineEdit_bltouch_5_2 = QtWidgets.QLineEdit(BLTouch)
        self.lineEdit_bltouch_5_2.setObjectName("lineEdit_bltouch_5_2")
        self.verticalLayout_11.addWidget(self.lineEdit_bltouch_5_2)
        self.lineEdit_bltouch_5_3 = QtWidgets.QLineEdit(BLTouch)
        self.lineEdit_bltouch_5_3.setObjectName("lineEdit_bltouch_5_3")
        self.verticalLayout_11.addWidget(self.lineEdit_bltouch_5_3)
        self.lineEdit_bltouch_5_4 = QtWidgets.QLineEdit(BLTouch)
        self.lineEdit_bltouch_5_4.setObjectName("lineEdit_bltouch_5_4")
        self.verticalLayout_11.addWidget(self.lineEdit_bltouch_5_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.pushButton_bltouch_save = QtWidgets.QPushButton(BLTouch)
        self.pushButton_bltouch_save.setMinimumSize(QtCore.QSize(190, 0))
        self.pushButton_bltouch_save.setObjectName("pushButton_bltouch_save")
        self.horizontalLayout_3.addWidget(self.pushButton_bltouch_save)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.pushButton_bltouch_cancel = QtWidgets.QPushButton(BLTouch)
        self.pushButton_bltouch_cancel.setMinimumSize(QtCore.QSize(190, 0))
        self.pushButton_bltouch_cancel.setObjectName("pushButton_bltouch_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_bltouch_cancel)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout_13.addLayout(self.horizontalLayout_3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_13.addItem(spacerItem12)

        self.retranslateUi(BLTouch)
        QtCore.QMetaObject.connectSlotsByName(BLTouch)

    def retranslateUi(self, BLTouch):
        _translate = QtCore.QCoreApplication.translate
        BLTouch.setWindowTitle(_translate("BLTouch", "Настройка датчика высоты для TEVO Black Widow"))
        self.label_bltouch_0_1.setText(
            _translate("BLTouch", "Выставлены оптимальные настройки для конкретного TEVO Black Widow,"))
        self.label_bltouch_0_2.setText(_translate("BLTouch", "можете выставить свои"))
        self.label_bltouch_1.setText(_translate("BLTouch", "1) Смещение датчика относительно сопла (offset):"))
        self.label_bltouch_1_1.setText(_translate("BLTouch",
                                                  "По оси X (датчик относительно сопла: если слева, то со знаком -; если справа, то со знаком +):"))
        self.label_bltouch_1_2.setText(_translate("BLTouch",
                                                  "По оси Y (датчик относительно сопла: если спереди, то со знаком -; если сзади, то со знаком +):"))
        self.lineEdit_bltouch_1_1.setText(_translate("BLTouch", "49"))
        self.lineEdit_bltouch_1_2.setText(_translate("BLTouch", "-18"))
        self.label_bltouch_2.setText(_translate("BLTouch", "2) Количество сканирований датчика в одной точке:"))
        self.radioButton_bltouch_2_1.setText(_translate("BLTouch", "1 - (Одна проба в каждой точке)"))
        self.radioButton_bltouch_2_2.setText(
            _translate("BLTouch", "2 - (Две пробы в каждой точке, одна быстрая, вторая медленная)"))
        self.label_bltouch_3.setText(_translate("BLTouch", "3) Методы автоматического выравнивания стола:"))
        self.radioButton_bltouch_3_1.setText(
            _translate("BLTouch", "3POINT (три точки для определения наклона, подходит для очень плоских столов)"))
        self.radioButton_bltouch_3_2.setText(
            _translate("BLTouch", "LINEAR (сканирование матрицей точек, для плоского стола; точнее, чем 3POINT)"))
        self.radioButton_bltouch_3_3.setText(
            _translate("BLTouch", "BILINEAR (сканирование матрицей точек, для кривого стола)"))
        self.radioButton_bltouch_3_4.setText(
            _translate("BLTouch", "UBL (сложный метод выравнивания объединяющий в себе предыдущие)"))
        self.label_bltouch_4.setText(_translate("BLTouch", "4) Размерность матрицы сканирования стола:"))
        self.radioButton_bltouch_4_1.setText(_translate("BLTouch", "3x3"))
        self.radioButton_bltouch_4_2.setText(_translate("BLTouch", "4x4"))
        self.label_bltouch_5.setText(_translate("BLTouch", "5) Границы зондирования (куда датчик может добраться):"))
        self.label_bltouch_5_1.setText(
            _translate("BLTouch", "Слева (если blt слева от сопла, то 15; если справа, то X offset + 15):"))
        self.label_bltouch_5_2.setText(_translate("BLTouch",
                                                  "Справа: (если blt слева от сопла, то размер стола -  X offset - запас; если справа, то размер стола - 15):"))
        self.label_bltouch_5_3.setText(
            _translate("BLTouch", "Спереди: (если blt спереди сопла, то 15; если сзади, то Y offset + 15):"))
        self.label_bltouch_5_4.setText(_translate("BLTouch",
                                                  "Сзади: (если blt спереди сопла, то размер стола -  Y offset - запас; если сзади, то размер стола - 15):"))
        self.lineEdit_bltouch_5_1.setText(_translate("BLTouch", "64"))
        self.lineEdit_bltouch_5_2.setText(_translate("BLTouch", "345"))
        self.lineEdit_bltouch_5_3.setText(_translate("BLTouch", "15"))
        self.lineEdit_bltouch_5_4.setText(_translate("BLTouch", "225"))
        self.pushButton_bltouch_save.setText(_translate("BLTouch", "Сохранить"))
        self.pushButton_bltouch_cancel.setText(_translate("BLTouch", "Отмена"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    BLTouch = QtWidgets.QWidget()
    ui = Ui_BLTouch()
    ui.setupUi(BLTouch)
    BLTouch.show()
    sys.exit(app.exec())