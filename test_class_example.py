class print_table:
    def __init__(self,num):
        self.num = num 

    def test_table_method(self):
        fl = open("class_example.txt", "w")
        for i in range(1,11):
            print(f"{self.num} X {i} = {self.num * i}", file=fl)

obj = print_table(5)
obj.test_table_method()