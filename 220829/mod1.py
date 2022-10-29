x = "module test"

def func_1(a,b):
    return a + b

class Class_1():
    def __init__(self,input_data):
        self.data = input_data

    def view_data(self):
        return f"Class 에서 입력받은 data의 값은 {self.data}이다"  #f 함수는 찾아서 집어 넣어주겠다