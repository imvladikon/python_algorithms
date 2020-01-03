# https://github.com/mourner/flatqueue

class PriorityQueue:

    def __init__(self):
        self.ids = []
        self.values = []
        self.length = 0

    def clear(self):
        self.length, self.ids.length, self.values.length = 0, 0, 0

    def push(self, id, value):
        self.ids.append(id)
        self.values.append(value)
        pos = self.length
        self.length += 1
        while pos > 0:
            parent = (pos - 1) >> 1
            parent_value = self.values[parent]
            if value >= parent_value:
                break
            self.ids[pos] = self.ids[parent]
            self.values[pos] = parent_value
            pos = parent
        self.ids[pos] = id
        self.values[pos] = value

    def pop(self):
        if self.length == 0:
            return None
        top = self.ids[0]
        self.length -= 1
        if self.length > 0:
            id = self.ids[0] = self.ids[self.length]
            value = self.values[0] = self.values[self.length]
            half_length = self.length >> 1
            pos = 0
            while pos < half_length:
                left = (pos << 1) + 1
                right = left + 1
                best_index = self.ids[left]
                best_value = self.values[left]
                right_value = self.values[right]
                if right < self.length and right_value < best_value:
                    left = right
                    best_index = self.ids[right]
                    best_value = right_value
                if best_value >= value:
                    break
                self.ids[pos] = best_index
                self.values[pos] = best_value
                pos = left
            self.ids[pos] = id
            self.values[pos] = value
        self.ids.pop()
        self.values.pop()
        return top

    def peek(self):
        return self.ids[0]

    def peek_value(self):
        return self.values[0]


if __name__ == "__main__":
    # queue = PriorityQueue()
    # queue.push(0, 2)
    # queue.push(1, 1)
    # queue.pop()
    # queue.pop()
    # queue.pop()
    # queue.push(2, 2)
    # queue.push(3, 1)
    # print(queue.pop() == 3)
    # print(queue.pop() == 2)
    # print(queue.pop() is None)
    items = [1, 3, 2, 467, 89, 4, 869]
    q = PriorityQueue()
    # push an item by passing its id and value
    for i in range(len(items)):
        q.push(i, items[i])
    print(q.peek_value())  # top item value
    print(q.peek())  # top item index
    print(q.pop())  # remove and return the top item index
