from PyQt5 import QtCore
from PyQt5 import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import config_enterTable_widget


class EnterTableWidget(QtWidgets.QMainWindow, config_enterTable_widget.Ui_enter_Table_Widget):
    def __init__(self, parent = None):
        #   Это здесь нужно для доступа к переменным, методам
        #   и т.д. в файле config_options_dialog.py
        super().__init__(parent)
        self.main = parent
        self.initUi()

    def initUi(self):
        self.setupUi(self)
        self.load_And_Display_Button.clicked.connect(self.display_data)

    def set_size_data_Table_Widget(self, data_arrays):
        rows = max(len(array) for array in data_arrays)
        columns = len(data_arrays)
        self.main.data_Table_Widget.setRowCount(rows + 10)
        self.main.data_Table_Widget.setColumnCount(columns + 2)

    def fill_data_Table(self, data_arrays):
        for data_array in data_arrays:
            for number in data_array:
                self.main.data_Table_Widget.setItem(data_array.index(number), data_arrays.index(data_array),
                                               QTableWidgetItem(f'{number}'))

    def load_data_from_input_field(self):
        from data_functions import create_data_arrays_from_str
        data_str = self.entry_Field_PlainText_Widget.toPlainText() + '\n'
        return create_data_arrays_from_str(data_str)

    def display_data(self):
        self.main.data_Table_Widget.clear()
        data_arrays = self.load_data_from_input_field()
        self.main.set_size_data_Table_Widget(data_arrays)
        self.main.fill_data_Table(data_arrays)

