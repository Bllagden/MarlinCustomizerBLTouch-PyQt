import sys
import glob

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox

from qt_design import Ui_Main
from qt_design import Ui_BLTouch
from qt_design import Ui_LimitSwitch

from parameters_and_functions import convert_to_limit_switch, \
    convert_to_bltouch, comm, uncomm, clear_parameters

global dir_path_global


# =====================================================================================================
# Это мой первый настоящий университетский проект (2021), поэтому код в нем выглядит не лучшим образом :)
# This is my first real university project (2021), so the code in it does not look the best :)
# =====================================================================================================


class MainWindow(QWidget, Ui_Main):
    """Класс основного окна"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        global dir_path_global  # глобальная переменная содержащая в себе путь к файлу с настройками.
        dir_path_global = ""
        self.ui.pushButton_to_firmware.clicked.connect(
            self.selection_file)  # связь нажатий на кнопки с методами.
        self.ui.pushButton_to_blt.clicked.connect(self.select_for_blt)
        self.ui.pushButton_to_li_sw.clicked.connect(
            self.select_for_limit_switch)

    @staticmethod
    def q_message_box(output_title, output_area):
        """метод создания всплывающего окна"""
        msgbox = QMessageBox()
        msgbox.setWindowTitle(output_title)
        msgbox.setText(output_area)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgbox.exec()

    def selection_file(self):
        """метод выбора папки содержащей файл настроек и нахождения его адреса"""
        global dir_path_global
        if dir_path_global != "":
            self.q_message_box("Предупреждение", "Прошивка уже выбрана")
        # проверка: выбран файл или нет.

        dir_path_current = QFileDialog.getExistingDirectory(self,
                                                            "Выберите папку с прошивкой",
                                                            "C:\\")
        if not dir_path_current:
            return
        # if not dir_path_current позволяет корректно вернуться в главное окно без выбора папки.

        dir_path_current = dir_path_current + "/**/Configuration.h"  # дописываем к пути файла его имя.
        list_with_dir_path = glob.glob(dir_path_current,
                                       recursive=True)  # поиск файла во всех папках выбранной папки.
        if len(list_with_dir_path) == 0:  # проверка на наличие файла в каталоге.
            self.q_message_box("Выберите другую папку",
                               "В данной директории прошивка не найдена")
            return
        part_of_path = "Marlin\\Configuration.h"  # проверка на корректность файловой директории; поиск файла.
        tmp = 0
        for i in list_with_dir_path:
            if part_of_path in i:
                dir_path_current = i
                tmp += 1
                break
        if tmp == 0:
            self.q_message_box("Выберите другую папку",
                               "В данной директории файл настройки прошивки находится отдельно от нее")
            return

        dir_path_global = dir_path_current
        self.q_message_box("Прошивка выбрана", "Выберите тип настройки")
        # в глобальную переменную dir_path_global записывается путь к файлу.
        self.change_color_button()

    def change_color_button(self):
        """метод перекрашивания рамки нижних кнопок в зеленый"""
        self.ui.pushButton_to_blt.setStyleSheet(
            "QPushButton {\n""border-color: #38BD80;\n""}")
        self.ui.pushButton_to_li_sw.setStyleSheet(
            "QPushButton {\n""border-color: #38BD80;\n""}")

    def select_for_blt(self):
        """метод перехода к окну с настройками для датчика BLTouch"""
        if dir_path_global == "":
            self.q_message_box("Ошибка", "Сначала выберите папку")
        else:
            self.close()
            self.ui.window_next = BLTouchWindow()
            self.ui.window_next.show()

    def select_for_limit_switch(self):
        """метод перехода к окну с настройками для датчика концевика"""
        if dir_path_global == "":
            self.q_message_box("Ошибка", "Сначала выберите папку")
        else:
            self.close()
            self.ui.window_next = LimitSwitchWindow()
            self.ui.window_next.show()


# BLTouchWindow ===============================================================

class BLTouchWindow(QWidget, Ui_BLTouch):
    """Класс окна с настройками датчика BLTouch"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_BLTouch()
        self.ui.setupUi(self)
        self.ui.pushButton_bltouch_cancel.clicked.connect(
            self.go_to_main_blt)  # связь нажатий на кнопки с методами.
        self.ui.pushButton_bltouch_save.clicked.connect(self.check_for_fill)

    @staticmethod
    def q_message_box_blt(output_title, output_area):
        """метод создания всплывающего окна"""
        msgbox = QMessageBox()
        msgbox.setWindowTitle(output_title)
        msgbox.setText(output_area)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgbox.exec()

    def go_to_main_blt(self):
        """метод возвращения в основное окно"""
        self.close()
        self.ui.window_next = MainWindow()
        self.ui.window_next.show()

    def check_for_fill(self):
        """метод проверки заполненности полей"""
        n = 0
        if self.ui.lineEdit_bltouch_1_1.text() == "":
            n += 1
        if self.ui.lineEdit_bltouch_1_2.text() == "":
            n += 1
        if self.ui.lineEdit_bltouch_5_1.text() == "":
            n += 1
        if self.ui.lineEdit_bltouch_5_2.text() == "":
            n += 1
        if self.ui.lineEdit_bltouch_5_3.text() == "":
            n += 1
        if self.ui.lineEdit_bltouch_5_4.text() == "":
            n += 1
        if n != 0:
            self.q_message_box_blt("Ошибка", "Заполните все поля")
        else:
            self.open_file_blt()

    def open_file_blt(self):
        """метод открытия файла с настройками по полученному адресу и копирование его содержимого"""
        # global dir_path_global
        configuration = open(dir_path_global, "r")
        configuration_list = configuration.read().splitlines()
        configuration.close()
        self.search_area_blt(configuration_list)

    def search_area_blt(self, configuration_list):
        """метод поиска нужного блока настроек, чтобы потом в цикле проверять только его"""
        start_working_area = 0
        end_working_area = 0
        for i in range(len(configuration_list)):
            if "Z Probe Options" in configuration_list[i]:
                start_working_area = i
            if "Unified Bed Leveling" in configuration_list[i]:
                end_working_area = i
                break
        self.checking_buttons_and_text_blt(configuration_list,
                                           start_working_area, end_working_area)

    def checking_buttons_and_text_blt(self, configuration_list,
                                      start_working_area, end_working_area):
        """метод проверки кнопок и полей для ввода и записи этих данных в кортежи"""
        region_1 = (self.ui.lineEdit_bltouch_1_1.text(),
                    self.ui.lineEdit_bltouch_1_2.text())
        region_2 = (self.ui.radioButton_bltouch_2_1.isChecked(),
                    self.ui.radioButton_bltouch_2_2.isChecked())
        region_3 = (self.ui.radioButton_bltouch_3_1.isChecked(),
                    self.ui.radioButton_bltouch_3_2.isChecked(),
                    self.ui.radioButton_bltouch_3_3.isChecked(),
                    self.ui.radioButton_bltouch_3_4.isChecked())
        region_4 = (self.ui.radioButton_bltouch_4_1.isChecked(),
                    self.ui.radioButton_bltouch_4_2.isChecked())
        region_5 = (self.ui.lineEdit_bltouch_5_1.text(),
                    self.ui.lineEdit_bltouch_5_2.text(),
                    self.ui.lineEdit_bltouch_5_3.text(),
                    self.ui.lineEdit_bltouch_5_4.text())
        self.change_settings_blt_1(configuration_list, start_working_area,
                                   end_working_area, region_1, region_2,
                                   region_3, region_4, region_5)

    def change_settings_blt_1(self, configuration_list, start_working_area,
                              end_working_area, region_1, region_2,
                              region_3, region_4, region_5):
        """метод частичного изменения настроек для использования датчика BLTouch"""
        for i in range(start_working_area, end_working_area):
            for j in range(len(convert_to_bltouch)):
                if convert_to_bltouch[j][1] in configuration_list[i]:
                    if convert_to_bltouch[j][0] == "comm":
                        configuration_list[i] = comm(configuration_list[i])
                    elif convert_to_bltouch[j][0] == "uncomm":
                        configuration_list[i] = uncomm(configuration_list[i])
                    elif convert_to_bltouch[j][0] == "edit":
                        tmp = clear_parameters(configuration_list[i],
                                               "EXTRUDER")
                        configuration_list[i] = tmp
                    elif convert_to_bltouch[j][0] == "uncomm + edit":
                        tmp = clear_parameters(configuration_list[i],
                                               "POSITION")
                        configuration_list[i] = uncomm(tmp)
        self.change_settings_blt_2(configuration_list, start_working_area,
                                   end_working_area, region_1, region_2,
                                   region_3, region_4, region_5)
        # convert_to_bltouch, comm, uncomm, clear_parameters - импортированы из parameters_and_functions.py;
        # parameters_and_functions.py - модуль с необходимыми параметрами и функциями.

    def change_settings_blt_2(self, configuration_list, start_working_area,
                              end_working_area, region_1, region_2,
                              region_3, region_4, region_5):
        """метод финального изменения настроек для использования датчика BLTouch"""
        for i in range(start_working_area, end_working_area):
            # 1)
            configuration_list[i] = self.for_change_blt_2_lineedit(
                "#define X_PROBE_OFFSET_FROM_EXTRUDER",
                configuration_list[i], region_1[0])
            configuration_list[i] = self.for_change_blt_2_lineedit(
                "#define Y_PROBE_OFFSET_FROM_EXTRUDER",
                configuration_list[i], region_1[1])

            # 2)
            if "#define MULTIPLE_PROBING 2" in configuration_list[i]:
                if region_2[0] is True:
                    configuration_list[i] = comm(configuration_list[i])
                else:
                    configuration_list[i] = uncomm(configuration_list[i])

            # 3)
            configuration_list[i] = self.for_change_blt_2_radbutton(
                "#define AUTO_BED_LEVELING_3POINT",
                configuration_list[i], region_3[0])
            configuration_list[i] = self.for_change_blt_2_radbutton(
                "#define AUTO_BED_LEVELING_LINEAR",
                configuration_list[i], region_3[1])
            configuration_list[i] = self.for_change_blt_2_radbutton(
                "#define AUTO_BED_LEVELING_BILINEAR",
                configuration_list[i], region_3[2])
            configuration_list[i] = self.for_change_blt_2_radbutton(
                "#define AUTO_BED_LEVELING_UBL",
                configuration_list[i], region_3[3])

            # 4)
            configuration_list[i] = self.for_change_blt_2_radbutton(
                "#define GRID_MAX_POINTS_X 3",
                configuration_list[i], region_4[0])
            configuration_list[i] = self.for_change_blt_2_radbutton(
                "#define GRID_MAX_POINTS_X 4",
                configuration_list[i], region_4[1])

            # 5)
            configuration_list[i] = self.for_change_blt_2_lineedit(
                "#define LEFT_PROBE_BED_POSITION",
                configuration_list[i], region_5[0])
            configuration_list[i] = self.for_change_blt_2_lineedit(
                "#define RIGHT_PROBE_BED_POSITION",
                configuration_list[i], region_5[1])
            configuration_list[i] = self.for_change_blt_2_lineedit(
                "#define FRONT_PROBE_BED_POSITION",
                configuration_list[i], region_5[2])
            configuration_list[i] = self.for_change_blt_2_lineedit(
                "#define BACK_PROBE_BED_POSITION",
                configuration_list[i], region_5[3])
        self.writing_to_file_blt(configuration_list)

    @staticmethod
    def for_change_blt_2_lineedit(context, configuration_list_i, region_i):
        """метод проверяет наличие нужной настройки и дописывает в ее конец параметры (связь с lineEdit)"""
        if context in configuration_list_i:
            configuration_list_i = configuration_list_i + " " + region_i
        return configuration_list_i

    @staticmethod
    def for_change_blt_2_radbutton(parameter, configuration_list_i, region_i):
        """метод проверяет наличие нужной настройки и комментрирует ее или раскомментирует (связь с radioButton)"""
        if parameter in configuration_list_i:
            if region_i is True:
                configuration_list_i = uncomm(configuration_list_i)
            else:
                configuration_list_i = comm(configuration_list_i)
        return configuration_list_i

    def writing_to_file_blt(self, configuration_list):
        """метод записи измененных настроек в файл"""
        f = open(dir_path_global, "w")
        for i in configuration_list:
            print(i, file=f)
        f.close()
        self.close()


# LimitSwitchWindow ===========================================================

class LimitSwitchWindow(QWidget, Ui_LimitSwitch):
    """Класс окна с настройками датчика концевика"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_LimitSwitch()
        self.ui.setupUi(self)
        self.ui.pushButton_li_sw_cancel.clicked.connect(
            self.go_to_main_ls)  # связь нажатий на кнопки с методами.
        self.ui.pushButton_li_sw_save.clicked.connect(self.open_file_ls)

    def go_to_main_ls(self):
        """метод возвращения в основное окно"""
        self.close()
        self.ui.window_next = MainWindow()
        self.ui.window_next.show()

    def open_file_ls(self):
        """метод открытия файла с настройками по полученному адресу и копирование его содержимого"""
        # global dir_path_global
        configuration = open(dir_path_global, "r")
        configuration_list = configuration.read().splitlines()
        configuration.close()
        self.search_area_ls(configuration_list)

    def search_area_ls(self, configuration_list):
        """метод поиска нужного блока настроек, чтобы потом в цикле проверять только его"""
        start_working_area = 0
        end_working_area = 0
        for i in range(len(configuration_list)):
            if "Z Probe Options" in configuration_list[i]:
                start_working_area = i
            if "Unified Bed Leveling" in configuration_list[i]:
                end_working_area = i
                break
        self.change_settings_ls(configuration_list, start_working_area,
                                end_working_area)

    def change_settings_ls(self, configuration_list, start_working_area,
                           end_working_area):
        """метод изменения настроек для использования датчика концевика"""
        for i in range(start_working_area, end_working_area):
            for j in range(len(convert_to_limit_switch)):
                if convert_to_limit_switch[j][1] in configuration_list[i]:
                    if convert_to_limit_switch[j][0] == "comm":
                        configuration_list[i] = comm(configuration_list[i])
                    elif convert_to_limit_switch[j][0] == "uncomm":
                        configuration_list[i] = uncomm(configuration_list[i])
                    elif convert_to_limit_switch[j][0] == "edit":
                        tmp = clear_parameters(configuration_list[i],
                                               "EXTRUDER")
                        configuration_list[i] = tmp + " 10"
        # convert_to_limit_switch, comm, uncomm, clear_parameters - импортированы из parameters_and_functions.py;
        # parameters_and_functions.py - модуль с необходимыми параметрами и функциями.
        self.writing_to_file_ls(configuration_list)

    def writing_to_file_ls(self, configuration_list):
        """метод записи измененных настроек в файл"""
        f = open(dir_path_global, "w")
        for i in configuration_list:
            print(i, file=f)
        f.close()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
