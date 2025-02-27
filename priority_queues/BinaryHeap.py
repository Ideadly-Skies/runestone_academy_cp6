class BinaryHeap:
    def __init__(self):
        """Constructor for the binary heap"""
        self._heap = []

    def _perc_up(self, i):
        """Restore min heap property""" 
        while (i - 1) // 2 >= 0: # parent pos
            parent_idx = (i - 1) // 2
            if self._heap[i] < self._heap[parent_idx]:
                self._heap[i], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[i]
                )
            i = parent_idx

    def insert(self, item):
        """Insert new item into the heap"""
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)

    def _perc_down(self, i):
        """Restore min heap property when removing root from the heap""" 
        while 2 * i + 1 < len(self._heap):
            sm_child = self._get_min_child(i)
            if self._heap[i] > self._heap[sm_child]:
                self._heap[i], self._heap[sm_child] = (
                    self._heap[sm_child],
                    self._heap[i],
                )
            else:
                break
            i = sm_child

    def _get_min_child(self, i):
        """Get min child of the heap"""
        if 2 * i + 2 > len(self._heap) - 1:
            return 2 * i + 1
        if self._heap[2 * i + 1] < self._heap[2 * i + 2]:
            return 2 * i + 1
        return 2 * i + 2
    
    def delete(self):
        """Delete the minimum heap"""
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result
    
    def heapify(self, not_a_heap):
        """
        A method to build an entire heap from a list of keys. Given a list of keys, you could easily build a heap
        by inserting each key one at a time. Since you are starting with an empty list, it is sorted and you could
        use binary search to find the right position to insert the next key at a cost of approximately O(log(n)) ops.

        However remember that inserting an item in the middle of the list may require O(n) operations to shift the
        rest of the list over to make room for the new key. Therefore to insert n keys into the heap would require
        a total of O(nlogn) operations. 

        However if we start with an entire list then we can build the whole heap in O(n) operations
        """
        self._heap = not_a_heap[:]
        i = len(self._heap) // 2 - 1
        while i >= 0:
            self._perc_down(i)
            i = i - 1

if __name__ == "__main__":
    a_heap = BinaryHeap()
    a_heap.heapify([9, 6, 5, 2, 3])
    print(a_heap._heap)