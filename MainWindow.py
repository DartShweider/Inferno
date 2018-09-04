import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore
from PyQt5 import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import config_main_window
from OptionsDialog import OptionsDialog
from EnterTableWidget import EnterTableWidget

class MainWindow(QtWidgets.QMainWindow, config_main_window.Ui_MainWindow):
    def __init__(self):
        #   Это здесь нужно для доступа к переменным, методам
        #   и т.д. в файле config_main_window.py
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setupUi(self) #   Это нужно для инициализации нашего дизайна
        self.browse_Button.clicked.connect(self.browse_file)
        self.actionSettings.triggered.connect(self.open_settings_dialog)
        self.actionEnter_table.triggered.connect(self.open_enterTable_widget)
        #self.copy_Table_RadioButton.setChecked(True)

        #self.load_And_Display_Button.clicked.connect(self.display_data)
        #self.copy_Table_RadioButton_Checked = True
        #self.load_File_RadioButton_Checked = False
        #self.path_To_File_lineEdit.clicked.connect(self.get_path_to_file)
        #self.load_File_RadioButton.clicked.connect(self.load_data_from_file_enable)
        #self.copy_Table_RadioButton.clicked.connect(self.load_data_from_table_enable)
        #self.load_from_file_objects_group = [self.path_To_File_lineEdit, self.path_To_File_Label, self.browse_Button,
                                     #self.name_Of_Sheet_Label, self.name_Of_Sheet_LineEdit, self.cell_Range_LineEdit,
                                     #self.cell_Range_Label]
        #self.load_from_table_objects_group = [self.input_Label, self.entry_Field_PlainText_Widget
                                              #]
        #for x in self.load_from_file_objects_group:
            #x.setEnabled(False)

    def open_enterTable_widget(self):
        self.EnterTableWindow = EnterTableWidget(self)
        self.EnterTableWindow.show()


    def open_settings_dialog(self):
        self.OptionsWindow = OptionsDialog(self)
        self.OptionsWindow.setWindowModality(QtCore.Qt.WindowModal)
        self.OptionsWindow.show()

    def load_data_from_file(self):
        from data_functions import create_data_arrays_from_file
        filename = self.get_path_to_file()
        sheetname = self.get_name_of_sheet()
        cell_range = self.get_cell_range()
        return create_data_arrays_from_file(filename = filename, sheetname = sheetname, cell_range = cell_range)

    def load_data_from_input_field(self):
        from data_functions import create_data_arrays_from_str
        data_str = self.entry_Field_PlainText_Widget.toPlainText() + '\n'
        return create_data_arrays_from_str(data_str)

    def get_name_of_sheet(self):
        return self.name_Of_Sheet_LineEdit.text()

    def get_cell_range(self):
        return self.cell_Range_LineEdit.text()

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

    def get_path_to_file(self):
          return  self.path_To_File_lineEdit.text()

    def display_data(self):
        self.data_Table_Widget.clear()
        if self.copy_Table_RadioButton_Checked == True:
            data_arrays = self.load_data_from_input_field()
            self.set_size_data_Table_Widget(data_arrays)
            self.fill_data_Table(data_arrays)
        elif self.load_File_RadioButton_Checked == True:
            data_arrays = self.load_data_from_file()
            self.set_size_data_Table_Widget(data_arrays)
            self.fill_data_Table(data_arrays)

    #def load_data_from_file_enable(self):
        #for object in self.load_from_file_objects_group:
            #object.setEnabled(True)
        #for object in self.load_from_table_objects_group:
            #object.setEnabled(False)
        #self.copy_Table_RadioButton_Checked = False
        #self.load_File_RadioButton_Checked = True

    #def load_data_from_table_enable(self):
        #for object in self.load_from_file_objects_group:
            #object.setEnabled(False)
        #for object in self.load_from_table_objects_group:
            #object.setEnabled(True)
        #self.copy_Table_RadioButton_Checked = True
        #self.load_File_RadioButton_Checked = False


def main():
    app = QtWidgets.QApplication(sys.argv)  #   Новый экземпляр QApplication
    window = MainWindow()  #    Создаём объект класса MainApp
    window.show()  #    Показываем окно
    app.exec_()  #  и запускаем приложение


if __name__ == '__main__':  #   Если мы запускаем файл напрямую, а не импортируем
    main()  #   то запускаем функцию main()


