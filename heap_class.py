'''"math" module is used in the function for printing and
"copy" module is used for doing shallow copy in various lines.'''
import math
import copy

class Heap :

    '''This class is used to build one of
    the most important data structures which is Heap.
    this class can build both Max and/or Min Heap.'''

    def __init__ (self):

        self.list = []
        self.size = 0
        self.min_max = 0


    def append_to_list (self):

        '''This Method is used to append
        any number of elements to the attribute of Heap class
        named "list" which is an empty list.'''

        new_element = input("""
        |do you want to enter any element? 
        |if yes enter "y" and when you are done enter "00".
        |""")
        print()
        while new_element != "00":
            ele = input("Enter a number.")
            if ele == "00":
                print("--------------------------------------------------")
                break
            self.list.append(int(ele))
            self.size = self.size + 1
        print("Your input:", self.list)


    def right (self, i):

        '''return the index of right child of the element
        which is at index i.'''

        return 2 * i + 2


    def left (self, i):

        '''return the index of left child of the element
        which is at index i.'''

        return 2 * i + 1


    def max_heap (self, i):

        '''Checks the Max_Heap condition for a node
        in index i and it's subtree.'''

        left_child = self.left(i)
        right_child = self.right(i)
        if left_child < self.size and self.list[left_child] > self.list[i]:
            largest = left_child
        else:
            largest = i
        if right_child < self.size and self.list[right_child] > self.list[largest]:
            largest = right_child
        if largest != i:
            self.list[i], self.list[largest] = self.list[largest], self.list[i]
            self.max_heap(largest)


    def min_heap (self, i):

        '''Checks the Min_Heap condition for a node
        in index i and it's subtree.'''

        left_child = self.left(i)
        right_child = self.right(i)
        if left_child < self.size and self.list[left_child] < self.list[i]:
            smallest = left_child
        else:
            smallest = i
        if right_child < self.size and self.list[right_child] < self.list[smallest]:
            smallest = right_child
        if smallest != i:
            self.list[i], self.list[smallest] = self.list[smallest], self.list[i]
            self.min_heap(smallest)


    def build_heap (self):

        '''Using the two previous functions,
        builds a heap.
        It is note worthy that all these Methods,
        perform some form of action on the attribute "list".'''

        if self.min_max == 0:
            self.min_max = int(input("If you want to build a min heap enter 1 otherwise, enter 2."))
        var = (self.size) // 2 -1
        for i in range(var, -1, -1):
            if self.min_max == 2:
                self.max_heap(i)
            else:
                self.min_heap(i)
        return self.list


    def insert (self):

        '''The insert function can be used to insert
        any number of elements to the heap.'''

        self.append_to_list()
        inserted = self.build_heap()
        return inserted


    def delete (self):

        '''This Method deletes the root of heap.'''

        self.list[0], self.list[-1] = self.list[-1], self.list[0]
        self.list.pop(-1)
        self.size = self.size - 1
        if self.min_max == 2:
            self.max_heap(0)
        else:
            self.min_heap(0)
        return self.list


    def __str__ (self):

        listt = copy.deepcopy(self.list)
        num_surface = int(math.log(len(listt), 2))
        num_leaf = 2 ** num_surface
        spaces = (num_leaf+1)*4 + num_leaf
        final_string = ""

        for i in range (0, num_surface + 1):
            each_surface_space = spaces - (2 ** i)
            divided_space = each_surface_space // ((2**i)+1)
            element_list = []

            for _ in range (0, 2**i):
                element_list.append(listt[0])
                if len(listt) == 1:
                    break
                listt.pop(0)

            string = ""

            for _ , ele in enumerate(element_list):
                string += " "*divided_space
                string += str(ele)

            final_string += "\n\n"
            final_string += string

        return final_string + "\n\n"


##################################################
#Test Cases:
##################################################


a = Heap()

a.append_to_list()
a.build_heap()
print(a)

a.insert()
print("""you have called the "insert" method on your heap.
The output is as follows:\n""")
print(a)

a.delete()
print("--------------------------------------------------")
print("""you have called the "delete" method on your heap.
The output is as follows:\n""")
print(a)
