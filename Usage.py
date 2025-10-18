from maxheap import maxHeap

h = MaxHeap([3, 1, 9, 5])
print(h)       # MaxHeap([9, 5, 3, 1])

h.push(7)
print(h.pop()) # 9
print(h.peek()) # 7
