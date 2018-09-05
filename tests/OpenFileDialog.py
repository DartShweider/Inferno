import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore
from PyQt5 import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import config_openFile_dialog


class OpenFileDialog(QtWidgets.QMainWindow, config_openFile_dialog.Ui_openFile_Dialog):
    def __init__(self, parent = None):
        #   Это здесь нужно для доступа к переменным, методам
        #   и т.д. в файле config_main_window.py
        super().__init__(parent)
        self.initUi()
        self.main = parent

    def initUi(self):
        self.setupUi(self)
        self.browse_Button.clicked.connect(self.browse_file)
        self.load_And_Display_Button.clicked.connect(self.display_data)

    def browse_file(self):
        self.path_To_File_lineEdit.clear()  #  На случай, если в списке уже есть элементы
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        #   directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        #   открыть диалог выбора директории и установить значение переменной
        #   равной пути к выбранной директории

        #if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
        #    for file_name in os.listdir(directory):  # для каждого файла в директории
        #        self.listWidget.addItem(file_name)  # добавить файл в listWidget
        self.path_To_File_lineEdit.setText(file_path)

    def get_name_of_sheet(self):
        return self.name_Of_Sheet_LineEdit.text()

    def get_cell_range(self):
        return self.cell_Range_LineEdit.text()

    def load_data_from_file(self):
        from data_functions import create_data_arrays_from_file
        filename = self.get_path_to_file()
        sheetname = self.get_name_of_sheet()
        cell_range = self.get_cell_range()
        return create_data_arrays_from_file(filename = filename, sheetname = sheetname, cell_range = cell_range)

    def display_data(self):
        data_arrays = self.load_data_from_file()
        self.main.set_size_data_Table_Widget(data_arrays)
        self.main.fill_data_Table(data_arrays)

    def get_path_to_file(self):
          return  self.path_To_File_lineEdit.text()

