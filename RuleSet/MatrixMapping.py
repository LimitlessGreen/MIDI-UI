def map_2d_to_1d(row, column):
    # Umwandlung von 2D-Index zu 1D-Index
    index_1d = (7 - row) * 8 + column
    return index_1d

def map_1d_to_2d(index_1d):
    # Umwandlung von 1D-Index zu 2D-Index
    row = 7 - index_1d // 8
    column = index_1d % 8
    return row, column

if __name__ == "__main__":
    # Beispielverwendung
    new_2d_index = (6, 7)  # Unten links in neuer Darstellung
    old_1d_index = map_2d_to_1d(*new_2d_index)
    new_2d_index_back = map_1d_to_2d(old_1d_index)

    print("Neuer 2D-Index:", new_2d_index)
    print("Alter 1D-Index:", old_1d_index)
    print("Zurückgewandelter 2D-Index:", new_2d_index_back)
