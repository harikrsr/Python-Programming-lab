class A:
    __length=0
    __width=0
    __area=0
    def __init__(self,l,w):
        self.__length=l
        self.__width=w
    def rectarea(self):
        self.__area=self.__length*self.__width
    def __lt__(self,other):
        if(self.__area<other.__area):
             return True
        else:
            return False

ob1=A(13,10)
ob1.rectarea()
ob2=A(5,3)
ob2.rectarea()
if(ob1<ob2):
    print("Rect1 is less than Rect2")
else:
    print("Rect2 is less than Rect1")