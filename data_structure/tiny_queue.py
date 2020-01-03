
#https://github.com/mourner/tinyqueue
import math


class TinyQueue:
    default_compare = lambda a, b: -1 if a < b else 1 if a > b else 0

    def __init__(self, data=[], compare=default_compare):
        self.data = data
        self.length = len(self.data)
        self.compare = compare
        if self.length > 0:
            i = (self.length >> 1) - 1
            while i >= 0:
                self._down(i)
                i -= 1

    def push(self, item):
        self.data.append(item)
        self.length += 1
        self._up(self.length - 1)

    def pop(self):
        if self.length == 0:
            return None
        top = self.data[0]
        bottom = self.data.pop()
        self.length -= 1
        if self.length > 0:
            self.data[0] = bottom
            self._down(0)
        return top

    def peek(self):
        return self.data[0]

    def _up(self, pos):
        data, compare = self.data, self.compare
        item = data[pos]
        while pos > 0:
            parent = (pos - 1) >> 1
            current = data[parent]
            if compare(item, current) >= 0:
                break
            data[pos] = current
            pos = parent
        data[pos] = item

    def _down(self, pos):
        data, compare = self.data, self.compare
        half_length = self.length >> 1
        item = data[pos]
        while pos < half_length:
            left = (pos << 1) + 1
            best = data[left]
            right = left + 1
            if right < self.length and compare(data[right], best) < 0:
                left = right
                best = data[right]
            if compare(best, item) >= 0:
                break
            data[pos] = best
            pos = left
        data[pos] = item


# create an empty priority queue
queue = TinyQueue()

# add some items
queue.push(7)
queue.push(5)
queue.push(10)

# remove the top item
top = queue.pop()  # returns 5

# return the top item (without removal)
top = queue.peek()  # returns 7

# get queue length
queue.length  # returns 2

items = [1, 3, 2, 467, 89, 4, 869]
queue = TinyQueue(items, lambda a, b: b - a)
# while queue.length:
#     print(queue.pop())


def minSum(num, k):
    queue = TinyQueue(num[:], lambda a, b: b - a)
    def do_one_op():
        item = queue.pop()
        queue.push(int(math.ceil(item/2)))
        # print(m)
    for j in range(k):
        do_one_op()
    return sum(queue.data)

num = [10,20,7]
k = 4
print(minSum(num, k))