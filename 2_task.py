from collections import deque


# Использовать список для очереди не рекомендуется, он слишком медленный,
# но это подходит для малого количества элементов.
class FirstInFirstOut1:
    __queue = []

    def __init__(self, max_length):
        self.max_length = max_length

    def add(self, element):
        self.__queue.append(element)
        if len(self.__queue) > self.max_length:
            self.__queue.pop(0)

    def get(self):
        if self.__queue:
            element = self.__queue.pop(0)
            return element


# Такой циклический буфер более эффективен
class FirstInFirstOut2:

    class Node:
        def __init__(self, data, previous_node=None, next_node=None):
            self.data = data
            self.previous_node = previous_node
            self.next_node = next_node

    def __init__(self, max_length):
        self.head = None
        self.tail = None
        self.max_length = max_length
        self.length = 0

    def add(self, data):
        new_node = self.Node(data, previous_node=self.tail)
        if self.tail:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node
        if self.length < self.max_length:
            self.length += 1
        else:
            self.head = self.head.next_node
            self.head.previous_node = None

    def get(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next_node
            self.length -= 1
            if self.length == 0:
                self.tail = None
            else:
                self.head.previous_node = None
            return data
        else:
            return None


# deque поддерживает добавление и удаление с обоих концов
class FirstInFirstOut3:
    __queue = deque()

    def __init__(self, max_length):
        self.max_length = max_length

    def add(self, element):
        self.__queue.append(element)
        if len(self.__queue) > self.max_length:
            self.__queue.popleft()

    def get(self):
        if self.__queue:
            element = self.__queue.popleft()
            return element


fifo1 = FirstInFirstOut1(4)
for i in range(6):
    fifo1.add(i)
    print('ok')
for _ in range(7):
    print(fifo1.get())

fifo2 = FirstInFirstOut2(4)
for i in range(6):
    fifo2.add(i)
    print('ok')
for _ in range(7):
    print(fifo2.get())

fifo3 = FirstInFirstOut3(4)
for i in range(6):
    fifo3.add(i)
    print('ok')
for _ in range(7):
    print(fifo3.get())
