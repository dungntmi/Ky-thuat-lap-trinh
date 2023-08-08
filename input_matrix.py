# Nguyễn Tiến Dũng - 20216805

from matrix import Matrix

def input_matrix():

    while True:
        print("Chọn cách thức để nhập ma trận\n1. Nhập từ bàn phím\n2. Đọc file\n")
        try:
            k = int(input("Chọn (1 hoặc 2): "))

            if k == 1:
                print("Xin mời bạn nhập ma trận từ bàn phím:")
                while True:
                    try:
                        rows = int(input("Nhập số hàng của ma trận (số nguyên dương): "))
                        if rows <= 0:
                            raise ValueError()
                        break
                    except ValueError:
                        print("Số hàng phải là số nguyên dương. Vui lòng nhập lại.")

                while True:
                    try:
                        cols = int(input("Nhập số cột của ma trận (số nguyên dương): "))
                        if cols <= 0:
                            raise ValueError()
                        break
                    except ValueError:
                        print("Số cột phải là số nguyên dương. Vui lòng nhập lại.")

                matrix = Matrix(rows, cols)
                matrix.input_from_keyboard()
                matrix.display()
                break

            elif k == 2:
                filename = input("Nhập tên file để đọc ma trận từ file: ")
                matrix = Matrix(0, 0)
                while not matrix.input_from_file(filename):
                    filename = input("Nhập lại tên file để đọc ma trận từ file: ")
                matrix.display()
                break

            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")
        except ValueError:
            print("Lựa chọn phải là số nguyên. Vui lòng chọn lại.\n")

    return matrix
