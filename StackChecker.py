from Stack import Stack

x = Stack()
x.push(1)
x.push(2)
x.push(3)  # top
print x

y = Stack()
y.push(1)
y.push(2)
y.push(3)  # top

x >> y
#x.reverse_recursive()
print x
print y

z = []
print type(x) is Stack
print type(z) is list

