"""Usage example for the maxheap package.

This file is written so it works both when run as a module from the
package root (python -m maxheap.Usage) and when executed directly
from the package directory (python maxheap/Usage.py).
"""

try:
	# When used as a package (recommended): python -m maxheap.Usage
	from . import MaxHeap
except Exception:
	# When executed directly as a script from the package folder:
	# python maxheap/Usage.py
	from core import MaxHeap


def main():
	h = MaxHeap([3, 1, 9, 5])
	print(h)       # MaxHeap([9, 5, 3, 1])

	h.push(7)
	print(h.pop()) # 9
	print(h.peek()) # 7


if __name__ == "__main__":
	main()
