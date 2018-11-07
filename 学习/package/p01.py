class Student():
    def __init__(self,name):
        self.name=name
    def say(self):
        print("hello,i'm ",self.name)

def sayHello():
    print("这是公共hello方法")

if __name__ == '__main__':
    print("这个是模块说明")