import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore
from PyQt5 import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import config_main_window
from OptionsDialog import OptionsDialog
from EnterTableWidget import EnterTableWidget
from OpenFileDialog import OpenFileDialog
from GraphSettingsDialog import GraphSettingsDialog


class MainWindow(QtWidgets.QMainWindow, config_main_window.Ui_MainWindow):
    def __init__(self):
        #   Это здесь нужно для доступа к переменным, методам
        #   и т.д. в файле config_main_window.py
        super().__init__()
        self.setupUi(self) #   Это нужно для инициализации нашего дизайна
        self.initActions()

    def initActions(self):
        self.actionSettings.triggered.connect(self.open_settings_dialog)
        self.actionEnter_table.triggered.connect(self.open_enterTable_widget)
        self.actionOpen_file.triggered.connect(self.open_loadFile_dialog)
        self.graphSettings_Button.clicked.connect(self.open_graphSettings_dialog)
        self.graphSettings_Button.clicked.connect(self.create_main_data_arrays)

    def create_main_data_arrays(self):
        self.main_data_arrays = []
        for column in range(self.data_Table_Widget.columnCount()):
            self.main_data_arrays.append([])
            for row in range(self.data_Table_Widget.rowCount()):
                self.main_data_arrays[column].append(self.data_Table_Widget.item(row, column))

    def open_graphSettings_dialog(self):
        self.GraphSettingsDialog = GraphSettingsDialog(self)
        self.GraphSettingsDialog.show()

    def open_enterTable_widget(self):
        self.EnterTableWindow = EnterTableWidget(self)
        self.EnterTableWindow.show()

    def open_loadFile_dialog(self):
        self.OpenFileDialog = OpenFileDialog(self)
        self.OpenFileDialog.show()

    def open_settings_dialog(self):
        self.OptionsWindow = OptionsDialog(self)
        self.OptionsWindow.setWindowModality(QtCore.Qt.WindowModal)
        self.OptionsWindow.show()

    def set_size_data_Table_Widget(self, data_arrays):
        rows = max(len(array) for array in data_arrays)
        columns = len(data_arrays)
        self.data_Table_Widget.setRowCount(rows + 10)
        self.data_Table_Widget.setColumnCount(columns + 2)

    def fill_data_Table(self, data_arrays):
        for data_array in data_arrays:
            for number in data_array:
                self.data_Table_Widget.setItem(data_array.index(number), data_arrays.index(data_array),
                                               QTableWidgetItem(f'{number}'))


def main():
    app = QtWidgets.QApplication(sys.argv)  #   Новый экземпляр QApplication
    window = MainWindow()  #    Создаём объект класса MainApp
    window.show()  #    Показываем окно
    app.exec_()  #  и запускаем приложение


if __name__ == '__main__':  #   Если мы запускаем файл напрямую, а не импортируем
    main()  #   то запускаем функцию main()
