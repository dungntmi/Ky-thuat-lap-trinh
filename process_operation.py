# Nguyễn Tiến Dũng - 20216805

from input_matrix import input_matrix

def process_operation(matrix):
    while True:
        print("----- MENU -----")
        print("1. Nhân ma trận với một số")
        print("2. Chuyển vị")
        print("3. Nghịch đảo")
        print("4. Tính định thức")
        print("5. Cộng hai ma trận")
        print("6. Trừ hai ma trận")
        print("7. Nhân hai ma trận")
        try:
            t = int(input("Chọn phép toán muốn thực hiện (1-7): "))
            if 1 <= t <= 7:
                if t == 1:
                    scalar = float(input("Nhập số nguyên để nhân với ma trận: "))
                    print("Kết quả nhân ma trận với", scalar, "là:")
                    result = matrix.multiply_scalar(scalar)
                    result.remove_negative_zero()
                    result.display()
                    result.save_to_file("Kết quả nhân ma trận với một số.txt")

                elif t == 2:
                    print("Ma trận chuyển vị là:")
                    result = matrix.transpose()
                    result.remove_negative_zero()
                    result.display()
                    result.save_to_file("Kết quả ma trận chuyển vị.txt")

                elif t == 3:
                    if matrix.rows != matrix.cols:
                        print("Không thể thực hiện vì ma trận không vuông.")
                    else:
                        print("Ma trận nghịch đảo là:")
                        result = matrix.inverse()
                        if result is not None:
                            result.remove_negative_zero()
                            result.display()
                            result.save_to_file("Kết quả ma trận nghịch đảo.txt")

                elif t == 4:
                    if matrix.rows != matrix.cols:
                        print("Không thể thực hiện vì ma trận không vuông.")
                    else:
                        result = matrix.determinant()
                        if result is not None:
                            print("Định thức của ma trận là:", result)
                        matrix.save_determinant_to_file("Kết quả định thức.txt")

                elif t == 5:
                    print("Nhập ma trận thứ hai:")
                    matrix2 = input_matrix()
                    print("Kết quả cộng hai ma trận là:")
                    result = matrix.add(matrix2)
                    result.remove_negative_zero()
                    result.display()
                    result.save_to_file("Kết quả cộng hai ma trận.txt")

                elif t == 6:
                    print("Nhập ma trận thứ hai:")
                    matrix2 = input_matrix()
                    print("Kết quả trừ hai ma trận là:")
                    result = matrix.subtract(matrix2)
                    result.remove_negative_zero()
                    result.display()
                    result.save_to_file("Kết quả trừ 2 ma trận.txt")

                elif t == 7:
                    print("Nhập ma trận thứ hai:")
                    matrix2 = input_matrix()
                    print("Kết quả nhân hai ma trận là:")
                    result = matrix.multiply(matrix2)
                    result.remove_negative_zero()
                    result.display()
                    result.save_to_file("Kết quả nhân 2 ma trận.txt")

                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")
        except ValueError:
            print("Lựa chọn phải là số nguyên từ 1 đến 7. Vui lòng chọn lại.\n")