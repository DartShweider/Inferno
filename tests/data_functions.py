import openpyxl

def load_file(filename, sheetname):
    workbook = openpyxl.load_workbook(filename = filename)
    sheet = workbook[sheetname]
    return sheet

def create_data_arrays_from_str(data_str):
    data_arrays = []
    number = ''
    space_check = 0
    enter_check = 0
    check_multiple_space = 0

    for symbol in data_str:
        if symbol != '\t' and symbol != '\n':
            if symbol == ',':
                number += '.'
            else:
                number += symbol
            check_multiple_space = 0

        elif symbol == '\n':
            check_multiple_space += 1
            if check_multiple_space == 1:
                if enter_check == 0:
                    data_arrays.append([])
                enter_check += 1
                data_arrays[space_check].append(float(number))
                number = ''
                space_check = 0

        else:
            check_multiple_space += 1
            if check_multiple_space == 1:
                if enter_check == 0:
                    data_arrays.append([])
                data_arrays[space_check].append(float(number))
                number = ''
                space_check += 1
    print(data_arrays)
    return data_arrays

def read_cell_range(cell_range):
    first_position_row = ''
    first_position_column = 0
    last_position_row = ''
    last_position_column = 0
    check_position = False

    for symbol in cell_range:
        if symbol == ':':
            check_position = True

        ord_symbol = ord(symbol)

        if check_position == False:
            if ord_symbol <= 57 and ord_symbol >= 48:
                first_position_row += symbol
            if ord_symbol >= 65 and ord_symbol <= 90:
                first_position_column += ord_symbol - 64
            if ord_symbol >= 97 and ord_symbol <= 122:
                first_position_column += ord_symbol - 96

        if check_position == True:
            if ord_symbol <= 57 and ord_symbol >= 48:
                last_position_row += symbol
            if ord_symbol >= 65 and ord_symbol <= 90:
                last_position_column += ord_symbol - 64
            if ord_symbol >= 97 and ord_symbol <= 122:
                last_position_column += ord_symbol - 96

    cell_area_coords = (int(first_position_column), int(first_position_row) ,int(last_position_column), int(last_position_row))
    return cell_area_coords

def create_data_arrays_from_file(filename, sheetname, cell_range):
    data_arrays = []
    sheet = load_file(filename, sheetname)
    cell_area_coords = read_cell_range(cell_range)
    first_cell_column = cell_area_coords[0]
    first_cell_row = cell_area_coords[1]
    last_cell_column = cell_area_coords[2]
    last_cell_row = cell_area_coords[3]

    for column in range(first_cell_column, last_cell_column + 1):
        data_arrays.append([])

        for row in range(first_cell_row, last_cell_row + 1):
            data_arrays[column - first_cell_column].append(sheet.cell(row = row, column = column).value)
    for data_array in data_arrays:
        for i in range(len(data_array)):
            if data_array[i] == None:
                data_array[i] = ''

    return data_arrays
