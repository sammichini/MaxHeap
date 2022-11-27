# max heap class finished by Sequoia anichini
# resources:
# https://softwareengineering.stackexchange.com/questions/237883/is-recursive-code-slower-than-non-recursive-code#:
# ~:text=Recursion%20is%20slower%20and%20it,doesn't%20fill%20the%20stack.
# https://www.w3schools.com/python/python_ref_list.asp
# Worked with peers Ash, Lynette, Bella

from math import floor



class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.
    """
    """
    Attributes
    --------------
    max_size : int
    length : int
    heap : list or single data type
    ROOT : const that reps heap[0]
    
    Methods 
    --------------
    insert(data)
        inserts item at the minimum index available
    peek()
        Return the root of the heap without removing
    extractMax()
        removes and returns the max valued item in heap
    __heapify()
        private method that organizes the heap to follow heap definition for each subtree
    build_heap()
        public method that uses heap's attributes and __heapify to make correct heap
    __get_parent()
        calculates index of a heap item's parent
    __get_left()
        calculates index of a heap item's left child
    __get_right()
        calculates index of a heap item's right child
    __swap(a, b)
        swaps element at heap[a] with element at heap[b]
    isEmpty()
        returns None if no items in the heap
    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap.

        size: Total capacity of the heap.
        data: List containing the desired heap contents. 
              The list is used in-place, not copied, so its contents 
              will be modified by heap operations.
              If data is specified, then the size field is ignored."""

        # Add to this constructor as needed

        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
            self.ROOT = 0
        else:
            self.max_size = size
            self.length = 0
            self.length = 0
            self.heap = [None] * size
            self.ROOT = 0
        
    def get_heap(self):
        return self.heap


    def insert(self, data):
        """Insert an element into the heap.

        Raises IndexError if the heap is full."""
        # Tips : insert 'data' at the end of the list initially
        #      : swap with its parent until the parent is larger or you 
        #      : reach the root
        if self.length >= self.max_size:
            raise IndexError('Heap is full!')


        if(self.length == 0):
            self.heap[self.ROOT] = data
            self.length += 1
            return
        self.heap[self.length] = data
        if(self.length < self.max_size):
            self.length += 1


        currentIndex = self.length - 1



        parent = self.__get_parent(currentIndex)
        # make sure we're not comparing None with ints
        while ((self.heap[currentIndex] and self.heap[parent]) and (currentIndex != self.ROOT) and (self.heap[currentIndex] > self.heap[parent])):
            self.__swap(currentIndex, parent)
            currentIndex = parent
            parent = self.__get_parent(currentIndex)

        


    def peek(self):
        """Return the maximum value in the heap."""
        if (self.length == 0):
            return None
        return self.heap[self.ROOT]

    def extract_max(self):
        """Remove and return the maximum value in the heap.

        Raises KeyError if the heap is empty."""
        # Tips: Maximum element is first element of the list
        #     : swap first element with the last element of the list.
        #     : Remove that last element from the list and return it.
        #     : call __heapify to fix the heap
        if self.length <= 0 or self.length == None: # none check may be unnecessary
            raise KeyError("There is no max to extract!!!")
            return None

        maximum = self.heap[0]

        self.heap[self.ROOT] = self.heap[self.length - 1]
        # need to fix the index that was removed from with None
        self.heap[self.length - 1] = None
        # Make sure that count of items in heap is accurate
        self.length = self.length - 1
        self.__heapify(self.ROOT, self.length)
        return maximum

    def __iter__(self):
        return self.__traverse()

    def __traverse(self):
        for i in range(self.length-1):
            yield self.heap[i]



    def __heapify(self, curr_index, list_length = None):
        """ recursively ensure that each subtree of the heap contains max at its root
        """
        # helper function for moving elements down in the heap
        # Page 157 of CLRS book

        self.length = list_length
        l = self.__get_left(curr_index)
        r = self.__get_right(curr_index)
        # is my left child larger?
        if l <= (self.length - 1) and self.heap[l] > self.heap[curr_index]:
            largest = l
        # if largest already current index we're done
        else:
            largest = curr_index
        # is my right child larger?
        if r <= (self.length - 1) and self.heap[r] > self.heap[largest]:
            largest = r
        # make sure heap property is maintained with recursion as our former larger was decreased
        if largest != curr_index:
            self.__swap(curr_index, largest)
            self.__heapify(largest, self.length)



    def build_heap(self):
        """Accesses non-leaf nodes and heapifies all of them"""
        # builds max heap from the list l.
        # Tip: call __heapify() to build to the list
        #    : Page 157 of CLRS book
        n = floor((self.length)/2)
        # for loop not going thru anything
        # n downto 1
        # start, stop,
        # help: range
       # max = -1
        for i in range(n, -1, -1):
            self.__heapify(i, self.length)



    ''' Optional helper methods may be used if required '''
    ''' You may create your own helper methods as required.'''
    ''' But do not modify the function definitions of any of the above methods'''

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        if loc % 2 == 0:
            parent = int((loc - 2) / 2)
        else:
            parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2
        

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp


    def isEmpty(self):
        return self.heap[0] == None




def heap_sort(l):
    """Sort a list in place using heapsort."""
    # Note: the heap sort function is outside the class
    #     : The sorted list should be in ascending order
    # Tips: Initialize a heap using the provided list
    #     : Use build_heap() to turn the list into a valid heap
    #     : Repeatedly extract the maximum and place it at the end of the list
    #     : Refer page 161 in the CLRS textbook for the exact procedure

    n = len(l)
    heap = max_heap(n, l)

    #update l to put item at end
    #have length of list

    heap.build_heap()


    while heap.length > 0:
        temp = heap.extract_max()

        l[heap.length] = temp
        # old length-1 or new length
    return l


    
