class Cal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def add():
        return num.x + num.y
    
    @staticmethod
    def sub():
        return num.x - num.y

    @staticmethod
    def mul():
        return num.x * num.y

    @staticmethod
    def div():
        if num.y != 0:
            return num.x / num.y
        else:
            return "0으로 나눌 수 없습니다."
    


num = Cal(10, 20)
print(num.add())
print(num.sub())
print(num.mul())
print(num.div())