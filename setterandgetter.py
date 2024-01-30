class Test:
    def __init__(self, val):
        self.__val=val
    
    def __get_val(self):
        return self.__val
    
    def __set_val(self,new_val):
        if new_val < self.__val:
            self.__val=100
        else:
            self.__val=new_val

    val=property(__get_val, __set_val)

obj=Test(5)
#print(obj.val) # we cannot access obj.__val coz its private type 
obj.val=98   #__set_val will be called internally 
print(obj.val)
obj.val=10
print(obj.val)