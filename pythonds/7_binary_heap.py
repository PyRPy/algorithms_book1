# 7_binary_heap.py
from pythonds.trees import BinHeap 
bh = BinHeap() 
bh.insert(5) 
bh.insert(7) 
bh.insert(3) 
bh.insert(11) 

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
