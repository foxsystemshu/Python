# @Author: Németh Szabocs 
import math

class ReadFile:
    def __init__(self, filename):
        self.file = filename
    def read(self):
        with open(self.file,'r') as f:
            for line in f:
              self.rows = line.split(" ")
            #print(self.rows)
        return list(map(float, self.rows))

class Meres:
    data = []
    def __init__(self, data_list):
        self.data =  data_list

    def get_num(self):
        return len(self.data)

    def Average(self):
        return sum(self.data) / self.get_num()

    def Median(self):
        db = self.get_num()
        self.data.sort()
        if (db % 2) != 0:
            x = int( (db) / 2)
            return self.data[x]
        else:
            l1 = (int(db/2)-1)
            l2 = (l1+1)
            avg = (self.data[l1] + self.data[l2]) / 2
        return avg  

    def Deviation(self):
        self.dev_list = []
        for x in self.data:
           self.dev_list.append(round(x - self.Average(), 2))
        return self.dev_list

    def DeviationSquare(self):
        self.dev_square_list = []
        for x in self.dev_list:
            self.dev_square_list.append(round(x*x,3))

        return self.dev_square_list

    def DeviationSquareSum(self):
        sum = 0
        for x in self.dev_square_list:
            sum = round(sum + x, 4)
        return sum
    def Variance(self):
        return round(self.DeviationSquareSum() / (self.get_num() - 1 ), 4)
    def Average_Abs_Deviation(self):
        abs_sum = 0
        for x in self.dev_list:
            abs_sum = abs_sum + abs(x)
        return ((1/self.get_num()) * abs_sum)

    def Range(self):
        L1 = round(max(self.data) - self.Average(),2) 
        L2 = round(self.Average() - min(self.data),2) * -1

        return [L1,L2]


lst = ReadFile("../adatsor.txt").read()
Meres = Meres(lst)
__range = []

#tOdO: 
# - printing will be also a different class
# - in a file, the separator could be ,;(space), readFile class must be able to handle it.  
#   
print("------------------")
print("Átlag:",round(Meres.Average(), 2))
print("------------------")
print("Medián:",round(Meres.Median(), 2))
print("------------------")
print("Dk eltérés: ",Meres.Deviation())
print("------------------")
print("DK^2:",Meres.DeviationSquare())
print("------------------")
print("DK^2 SUM =", Meres.DeviationSquareSum())
print("------------------")
print("Variancia =", Meres.Variance())
print("------------------")
print("Standard Eltérés= X +(-)", round(math.sqrt(Meres.Variance()), 3))
print("----------------------------------")
print("Az abszolút eltérés átlaga= X +(-)",round(Meres.Average_Abs_Deviation(), 2))
print("----------------------------------")
__range = Meres.Range()
print("Range:\n L1 =",__range[0])
print(" L2 =",__range[1])

