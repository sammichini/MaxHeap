import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):


    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")


class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)

        self.assertEqual(pq.extract_max(), 3)
        print("\n")


class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        max = sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual(sorted_list, [3, 4, 7, 10, 24, 37, 57, 67, 87])
        print("\n")

class T6_built_heap(unittest.TestCase):

    def test_built_heap(self):
        print("\n")
        newHeap = mheap.max_heap(3, [4,7,11])
        newHeap.build_heap()
        max = -1
        for i in newHeap:
            if i > max:
                max = i
        temp = newHeap.extract_max()
        self.assertEqual(temp, max)
        print("\n")

class T7_raise_index(unittest.TestCase):

    def test_IndexError(self):
        newHeap = mheap.max_heap(1, [4])
        newHeap.build_heap()
        self.assertRaises(IndexError, newHeap.insert, 5)
        print("\n")




class T8_raise_key(unittest.TestCase):

    def test_IndexError(self):
        print("Raises key error when extracting from empty")
        print("\n")
        pq = pqueue.pqueue(5)
        self.assertRaises(KeyError, pq.extract_max)
        print("\n")

class T9_peek_none(unittest.TestCase):

    def test_peek(self):
        pq = pqueue.pqueue(5)
        temp = pq.peek()
        self.assertIsNone(None, temp)
        print("\n")

class T10_heap_is_valid(unittest.TestCase):

    def test_valid_heap(self):
        print("Testing heap is valid after extracts and inserts")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(55)
        pq.insert(9)
        pq.insert(23)
        max = -1
        temp = pq.extract_max()
        pq.insert(51)
        for i in pq:
            if i > max:
                max = i
        temp = pq.extract_max()
        self.assertEqual(temp, max)
        print("\n")

class T11_empty(unittest.TestCase):

    def test_empty_heap(self):
        heap = mheap.max_heap(1)
        boolean = heap.isEmpty()
        self.assertEqual(True, boolean)
        print("\n")


class T12_max_of_negative(unittest.TestCase):

    def test_negative_max(self):
        pq = pqueue.pqueue(3)
        pq.insert(-1)
        pq.insert(-4)
        pq.insert(-22)
        max = pq.extract_max()
        self.assertEqual(max, -1)
        print("\n")

class T13_insert_root_is_less(unittest.TestCase):

    def test_root_less(self):
        pq = pqueue.pqueue(3)
        pq.insert(-1)
        pq.insert(-4)
        pq.insert(-22)
        max = pq.extract_max()
        pq.insert(-2)
        self.assertNotEqual(max, pq.extract_max())
        print("\n")

class T14_max_removed(unittest.TestCase):

    def test_max_removed(self):
        pq = pqueue.pqueue(3)
        pq.insert(-1)
        pq.insert(-4)
        pq.insert(-22)
        max = pq.extract_max()
        self.assertNotIn(max, pq)
        print("\n")

class T15_list_not_none(unittest.TestCase):

    def test_not_none(self):
        pq = pqueue.pqueue(3)
        pq.insert(5)
        pq.insert(8)
        pq.insert(13)
        l = [None]*3
        for i in pq:
            k = 0
            l[k] = i
            ++k
        self.assertIsNotNone(l[0])
        print("\n")


# lengths, ranges, off by 1,
# double check heap size, length
    
if __name__ == '__main__':
    unittest.main()

#Help on class range in module builtins:

#class range(object)
# |  range(stop) -> range object
 #|  range(start, stop[, step]) -> range object
# |
# |  Return an object that produces a sequence of integers from start (inclusive)
# |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
# |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
# |  These are exactly the valid indices for a list of 4 elements.
# |  When step is given, it specifies the increment (or decrement).
# |
# |  Methods defined here:
# |
# |  __contains__(self, key, /)
# |      Return key in self.
# |
# |  __eq__(self, value, /)
# |      Return self==value.
# |
# |  __ge__(self, value, /)
# |      Return self>=value.
# |
# |  __getattribute__(self, name, /)

#range object
#range(4,1)
#range(4,1,-1)
#range(4,0,-1)
#4, 3, 2, 1, [=0 so stop]
