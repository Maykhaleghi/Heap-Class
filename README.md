
__prepared by: [@AnooshaMohammadi](https://www.github.com/AnooshaMohammadi) and [@MiaKhaleghi](https://www.github.com/MiaKhaleghi)__


# Heap:

The heap is one maximally efficient implementation of an abstract data type called a priority queue, and in fact, priority queues are often referred to as "heaps", regardless of how they may be implemented.
In a heap, the highest (or lowest) priority element is always stored at the root. However, a heap is not a sorted structure; it can be regarded as being partially ordered.
A heap is a useful data structure when it is necessary to repeatedly remove the object with the highest (or lowest) priority, or when insertions need to be interspersed with removals of the root node.

## Heap Class:

```py
class Heap : 

    def __init__ (self):

        self.list = []
        self.size = 0
        self.min_max = 0
```

In this part of the code, we create a heap class. Each heap that is created will be an object of this class. Every object will have **three** attributes. <u>A list</u>, <u>an integer</u> (which is the number of elements in our heap) and <u>another integer named min_max</u> which tells us if the list has been turned to a heap or not. if yes, what sort of heap it is.
There can be three case for the value that min_max is holding.
- **0:** This means that our list is yet to be made into a heap.
- **1:** The list is a Min_Heap.
- **2:** The list is a Max_Heap.

Now that we have mentioned max/min heap, let's first understand what they mean.

## Max/Min_Heap:

The one thing that makes a heap is just one condition.
The root/node key is compared with its children and arranged accordingly. If **α** has child node **β** then −

<center>key(α) ≥ key(β)</center>

As the value of parent is greater than that of child, this property generates Max Heap. Based on this criteria, a heap can be of two types:
### Min-Heap:
Where the value of the root node is less than or equal to either of its children.


```py
    def right (self, i):

        '''return the index of right child of the element
        which is at index i.'''

        return 2 * i + 2


    def left (self, i):

        '''return the index of left child of the element
        which is at index i.'''

        return 2 * i + 1

  

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
```



### Max-Heap:
Where the value of the root node is greater than or equal to either of its children.

```py
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
```

## Built_heap:

```py
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
```

input:
```txt
 [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
```
output:
```txt
        |do you want to enter any element? 
        |if yes enter "y" and when you are done enter "00".
        |y


enter your number.35
enter your number.33
enter your number.42
enter your number.10
enter your number.14
enter your number.19
enter your number.27
enter your number.44
enter your number.26
enter your number.31
enter your number.00
--------------------------------------------------
your list [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
If you want to build a min heap enter 1 otherwise, enter 2.1


                      10


              14               19


        26        31        42        27


    44    33    35

If you want to build a min heap enter 1 otherwise, enter 2.2


                     44


              35              42


        33        31        19        27


    10    26    14
```


## Insert:

When we have a list of integers, generally there are two ways to build a heap.

### First Method:
we insert the elements one by one and each time we check if the element breaches the heap condition. This method is known as William's Method.



### Second Method:
We get all the elements as list. Then turn them into binary tree. 
Afterwards we call the build_heap function for the lowest to the hightest non_leaf element.

```py
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

    def insert (self):

        '''The insert function can be used to insert
        any number of elements to the heap.'''

        self.append_to_list()
        inserted = self.build_heap()
        return inserted
```

input:
```txt
 [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
```
output:
```txt
If you want to build a min heap enter 1 otherwise, enter 2.2
 [44, 35, 42, 33, 31, 19, 27, 10, 26, 14]

        |do you want to enter any element? 
        |if yes enter "y" and when you are done enter "00".
        |y


enter your number.36
enter your number.00
--------------------------------------------------
your list [44, 35, 42, 33, 31, 19, 27, 10, 26, 14, 36]


                     44


              36              42


        33        35        19        27


    10    26    14    31



```

>[Note]
>The insert function can be used to insert any number of elements to a heap.





## Delete:

```py
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
```


output:
```txt

                     44


              35              42


        33        31        19        27


    10    26    14




                     42


              35              33


        31        19        27        10


    26    14
```



## Print:

```py
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
```

# Building a Heap using Python libraries:

In Python, Heap is available using the “heapq” module.
In this module, there are many functions but the three main functions are :
1. heapify: This function is used to make Max or Min heap. The default of this function is min heap. If you need to build a max heap then you should multiply each element with -1 and then build a heap with these numbers.
3. heappush: This function is used to push one element in the heap.
4. heappop: The function pops the root of the heap.
 ```py
 from heapq import heappop, heappush, heapify
 A = [5,7,9,1,3]
 B = []

for i in A:
    B.append(-1 * i)

print("Min heap A")
heapify(A)
printt(A)
print("---------------------")
print("pushed")
heappush(A,4)
printt(A)
print("---------------------")
print("poped")
heappop(A)
printt(A)

print("#########################")
print("Max heap A")
heapify(B)

for i in range(len(B)):
   B[i] = -B[i]
    
printt(B)
```

output:
```txt
Min heap A

           1

       3       9

    7    5

---------------------
pushed

           1

       3       4

    7    5    9

---------------------
poped

           3

       5       4

    7    9

#########################
Max heap A

           9

       7       5

    1    3

```
