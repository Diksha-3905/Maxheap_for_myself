# pymaxheap/core.py

import heapq

class MaxHeap:
    """
    A simple MaxHeap implementation built on Python's heapq.
    Provides push, pop, peek, and heapify functionality.
    """

    def __init__(self, iterable=None):
        self.heap = []
        if iterable:
            self.heap = [-x for x in iterable]
            heapq.heapify(self.heap)

    def push(self, item):
        """Insert an element into the heap."""
        heapq.heappush(self.heap, -item)

    def pop(self):
        """Remove and return the maximum element."""
        return -heapq.heappop(self.heap)

    def peek(self):
        """Return the maximum element without removing it."""
        return -self.heap[0] if self.heap else None

    def heapify(self, iterable):
        """Transform an iterable into a max heap."""
        self.heap = [-x for x in iterable]
        heapq.heapify(self.heap)

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return f"MaxHeap({[-x for x in self.heap]})"
