import math
import copy

class heap :

    def __init__ (self):
        self.A = []
        self.size = 0
        self.min_max = 0

    def Append (self):
        n = input("""
        |do you want to enter any element? 
        |if yes enter "y" and when you are done enter "00".
        |""")
        print()
        while n != "00":
            a = input("Enter a number.")
            if (a == "00"):
                print("--------------------------------------------------")
                break
            self.A.append(int(a))
            self.size = self.size + 1
        print("Your input:", self.A)
        
    def right (self, i):
        return 2 * i + 2

    def left (self, i):
        return 2 * i + 1

    def Max_Heap (self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r < self.size and self.A[r] > self.A[largest]:
            largest = r
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.Max_Heap(largest)

    def Min_Heap (self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.size and self.A[l] < self.A[i]:
            smallest = l
        else:
            smallest = i
        if r < self.size and self.A[r] < self.A[smallest]:
            smallest = r
        if smallest != i:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            self.Min_Heap(smallest)

    def build_heap (self):
        if self.min_max == 0:
            self.min_max = int(input("If you want to build a min heap enter 1 otherwise, enter 2."))
        n = (self.size) // 2 -1
        for i in range(n, -1, -1):
            if self.min_max == 2:
                self.Max_Heap(i)
            else:
                self.Min_Heap(i)
        return self.A

    def insert (self):
        self.Append()
        inserted = self.build_heap()
        return inserted

    def delete (self):
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.A.pop(-1)
        self.size = self.size - 1
        if self.min_max == 2:
            self.Max_Heap(0)
        else:
            self.Min_Heap(0)
        return self.A

    def print (self):

        listt = copy.deepcopy(self.A)
        num_surface = int(math.log(len(listt), 2))
        num_leaf = 2 ** num_surface
        spaces = (num_leaf+1)*4 + num_leaf
  
        for i in range (0, num_surface + 1):
            each_surface_space = spaces - (2 ** i)
            divided_space = each_surface_space // ((2**i)+1)
            element_list = []

            for k in range (0, 2**i):
                element_list.append(listt[0])
                if len(listt) == 1:
                    break
                listt.pop(0)
                
            strr = ""

            for z in range (len(element_list)):
                strr = strr + " "*divided_space
                strr = strr+ str(element_list[z]) 

            print()
            print(strr)

        print()





        
        
#Test Cases:        

a = heap()

a.Append()
a.build_heap()
a.print()

a.insert()
print("""you have called the "insert" method on your heap.
The output is as follows:\n""")
a.print()

a.delete()
print("--------------------------------------------------")
print("""you have called the "delete" method on your heap.
The output is as follows:\n""")  
a.print()
