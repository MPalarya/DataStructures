from threading import Lock

# TODO: limit max size


class Stack:
    def __init__(self):
        self.items = []
        self.__size = 0
        self.__lock = Lock()

    def push(self, item):
        with self.__lock:
            self.__size += 1
            self.items.append(item)

    def pop(self):
        with self.__lock:
            if not self.is_empty():
                self.__size -= 1
                return self.items.pop()

    def peek(self):
        return self.items[self.size() - 1]

    def size(self):
        return self.__size

    def is_empty(self):
        return len(self.items) > 0

    def clear(self):
        with self.__lock:
            for i in range(self.size()):
                self.pop()

