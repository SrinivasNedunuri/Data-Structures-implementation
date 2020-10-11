class heap:
    def __init__(self):
        self.heaplist = [0]
        self.size = 0
    def parent(self, index):
        return index-1//2
    def leftChild(self, index):
        return 2*index + 1
    def rightChild(self, index):
        return 2*index + 2
    def getMax(self):
        if self.size == 0:
            return -1
        return self.heaplist[0]

    def getMin(self):
        if self.size == 0:
            return -1
        return self.heaplist[0]

    def percolateDown(self, i):
        while i*2 <= self.size:
            minimumChild = self.minChild(i)
            if self.heaplist[i] > self.heaplist[minimumChild]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[minimumChild]
                self.heaplist[minimumChild] = tmp
            i = minimumChild

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                tmp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i//2

    def minChild(self, i):
        if i*2 + 1 > self.size:
            return i*2 + 1
        else:
            if self.heaplist[i*2 +1] < self.heaplist[i*2 +2]:
                return i*2 + 1
            else:
                return i*2 + 2

    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(nums, n, i):
            l = 2 * i + 1
            r = 2 * i + 2

            largest = i
            if l < n and nums[largest] < nums[l]:
                largest = l

            if r < n and nums[largest] < nums[r]:
                largest = r

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]

                heapify(nums, n, largest)

        n = len(nums)

        for i in range(n // 2 + 1)[::-1]:
            heapify(nums, n, i)

        for i in range(n)[::-1]:
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)
        return nums

