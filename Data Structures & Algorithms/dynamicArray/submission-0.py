class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dyn_arr = [0] * capacity
        self.length = 0


    def get(self, i: int) -> int:
        return self.dyn_arr[i]


    def set(self, i: int, n: int) -> None:
        self.dyn_arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.dyn_arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        res = self.dyn_arr[self.length - 1]
        self.dyn_arr[self.length - 1] = 0
        self.length -= 1
        return res

    def resize(self) -> None:
        new_arr = [0] * (self.capacity * 2)
        for i in range(self.length):
            new_arr[i] = self.dyn_arr[i]

        self.dyn_arr = new_arr
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
