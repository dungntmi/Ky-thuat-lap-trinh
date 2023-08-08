# Nguyễn Tiến Dũng - 20216805

class Matrix:

    # Khởi tạo ma trận với số hàng và số cột cho trước, tất cả các phần tử ban đầu được đặt giá trị 0
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]


    # Khi lựa chọn nhập ma trận từ một file được chỉ định
    def input_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                self.rows = len(lines)
                if self.rows > 0:
                    values = lines[0].strip().split()
                    self.cols = len(values)
                else:
                    print("File rỗng.")
                    return False

                self.data = [[float(value) for value in values.split()] for values in lines]

                return True
        except FileNotFoundError:
            print("Không tìm thấy file.")
            return False


    # Khi lựa chọn nhập ma trận từ bàn phím
    def input_from_keyboard(self):
        print("Nhập số liệu cho ma trận:")
        for i in range(self.rows):
            valid_input = False
            while not valid_input:
                try:
                    values = input(f"Nhập giá trị của hàng {i + 1} (các giá trị cách nhau bởi dấu cách): ").split()
                    if len(values) != self.cols:
                        raise ValueError("Số lượng giá trị không khớp với số cột của ma trận.\n")
                    self.data[i] = [float(value) for value in values]
                    valid_input = True
                except ValueError as e:
                    print(f"Lỗi: {str(e)} Vui lòng nhập lại.")


    # Hiển thị ma trận ra màn hình
    def display(self):
        print("Ma trận:")
        for row in self.data:
            print("    ".join("{:8.3f}".format(elem) for elem in row))


    # Nhân ma trận với một số (scalar).
    def multiply_scalar(self, scalar):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * scalar
        return result


    # Chuyển vị ma trận
    def transpose(self):
        result = Matrix(self.cols, self.rows)

        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]

        return result


    # Trả về ma trận con (submatrix) để tính định thức
    def submatrix(self, row, col):
        result = Matrix(self.rows - 1, self.cols - 1)
        r = 0

        for i in range(self.rows):
            if i == row:
                continue

            c = 0
            for j in range(self.cols):
                if j == col:
                    continue

                result.data[r][c] = self.data[i][j]
                c += 1

            r += 1

        return result


    # Tính định thức của ma trận
    def determinant(self):
        if self.rows != self.cols:
            print("Ma trận không vuông, không thể tính định thức.")
            return None

        if self.rows == 1:
            return self.data[0][0]

        if self.rows == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        det = 0
        for j in range(self.cols):
            det += (-1) ** j * self.data[0][j] * self.submatrix(0, j).determinant()

        return det


    # Tính ma trận liên hợp (adjoint) để tính ma trận nghịch đảo
    def adjoint(self):
        result = Matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                sign = (-1) ** (i + j)
                result.data[j][i] = sign * self.submatrix(i, j).determinant()

        return result


    # Tính ma trận nghịch đảo
    def inverse(self):
        if self.rows != self.cols:
            print("Ma trận không vuông, không thể tính nghịch đảo.")
            return None

        det = self.determinant()
        if det == 0:
            print("Ma trận không khả nghịch.")
            return None

        adj = self.adjoint()
        adj_scalar = 1 / det

        return adj.multiply_scalar(adj_scalar)


    # Cộng hai ma trận
    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Không thể thực hiện phép cộng vì kích thước của hai ma trận không khớp.")
            return None

        result = Matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result


    # Trừ hai ma trận
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Không thể thực hiện phép trừ vì kích thước của hai ma trận không khớp.")
            return None

        result = Matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]

        return result


    # Nhân hai ma trận
    def multiply(self, other):
        if self.cols != other.rows:
            print(
                "Không thể thực hiện phép nhân vì số cột của ma trận thứ nhất không bằng số hàng của ma trận thứ hai.")
            return None

        result = Matrix(self.rows, other.cols)

        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]

        return result


    # Loại bỏ các số 0 âm về 0
    def remove_negative_zero(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if abs(self.data[i][j]) == 0.0:
                    self.data[i][j] = 0.0


    # Lưu ma trận kết quả vào một file
    def save_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                for row in self.data:
                    file.write(" ".join("{:8.3f}".format(elem) for elem in row))
                    file.write("\n")
            print("Ma trận đã được lưu vào file:", filename)
        except IOError:
            print("Lỗi: Không thể ghi vào file.")


# Lưu kết quả định thức vào một file
    def save_determinant_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                determinant = self.determinant()
                if determinant is not None:
                    file.write(str(determinant))
                    print("Kết quả định thức đã được lưu vào file:", filename)
                else:
                    print("Không thể tính định thức của ma trận.")
        except IOError:
            print("Lỗi: Không thể ghi vào file.")