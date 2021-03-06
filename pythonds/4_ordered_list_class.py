# 4_ordered_list_class.py
class Node:
    def __init__(self, initdata):
        self.data = initdata 
        self.next = None 

    def getData(self):
        return self.data 

    def getNext(self):
        return self.next 

    def setData(self, newdata):
        self.data = newdata 

    def setNext(self, newnext):
        self.next = newnext 

class OrderedList:
    def __init__(self):
        self.head = None 

    def search(self, item):
        current = self.head 
        found = False 
        stop = False 
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True 
            else:
                if current.getData() > item:
                    stop = True 
                else:
                    current = current.getNext() 

        return found 

    def add(self, item):
        current = self.head 
        previous = None 
        stop = False 
        while current != None and not stop:
            if current.getData() > item:
                stop = True 
            else: 
                previous = current 
                current = current.getNext() 
        
        temp = Node(item) 
        if previous == None:
            temp.setNext(self.head) 
            self.head = temp      
        else:
            temp.setNext(current) 
            previous.setNext(temp) 

    def isEmpty(self):
        return self.head == None 

    def size(self):
        current = self.head() 
        count = 0 
        while current != None:
            count = count + 1 
            current = current.getNext() 
        return count 

mylist = OrderedList() 
mylist.add(31)
mylist.add(77)
print(mylist.head.getData())

mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.head.getData())        
print(mylist.search(26))

# get the second item (second smallest)
print(mylist.head.getNext().getData())

# print all the data in a linked list
print('print all the data in each node: ')
head = mylist.head 
while head:
    print(head.getData())
    head = head.getNext() 

# print('another way to print all the data at each node: ') 
# print([node.getData() for node in mylist])
# # TypeError: 'OrderedList' object is not iterable
