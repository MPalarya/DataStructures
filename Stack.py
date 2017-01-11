from threading import Lock


class Stack(object):
    def __init__(self, limit=0):
        self.__items = []
        self.__size = 0
        self.__lock = Lock()
        self.__limit = limit

    def push(self, item):
        with self.__lock:
            if not self.is_full():
                self.__size += 1
                self.__items.append(item)
                return True
            return False

    def pop(self):
        with self.__lock:
            if not self.is_empty():
                self.__size -= 1
                return self.__items.pop()

    def peek(self):
        with self.__lock:
            return self.__items[self.__size - 1]

    def size(self):
        return self.__size

    def is_empty(self):
        return len(self.__items) == 0

    def is_full(self):
        return self.__limit == self.__size or self.__limit <= 0

    def clear(self):
        with self.__lock:
            for i in range(self.__size):
                self.pop()

    def reverse(self):
        with self.__lock:
            self.__items.reverse()

    def reverse_recursive(self):
        if self.is_empty():
            return
        item = self.pop()
        self.reverse_recursive()
        self.__recursive_insert_at_bottom(item)

    def __recursive_insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            tmp = self.pop()
            self.__recursive_insert_at_bottom(item)
            self.push(tmp)

    def __str__(self):
        return "Stack: " + str(self.__items) + "< top"
