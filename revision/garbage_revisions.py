#all the programs that have been attempted before, repetitives ought to be deleted on finding time, attempt each using 
#do factors, prime, power, 
import random
arr = [1]
arr.extend([random.randint(10,190) for _ in range(5)])
l = [_ for _ in range(-5,5)]
lx = [x**2 if x<0 else x for x in l]
lxl = lambda x: x**2 if x<0 else x # working lambda
lxone = lambda x: x**2 if x<0 else x for x in l

class IntegerOperations_March_24:
    def __init__(self,num=2,power=5):
        self.num = num
        self.power = power
        
class LCM_HCF(IntegerOperations_March_24):
    "all ways LCM and HCF can be computed for,while,array,min,max"
    def __init__(self,a=20,b=12,l=[12,24,30,36]):
        self.a=a
        self.b=b
        self.l=l
    def using_for(self):
        pass
    