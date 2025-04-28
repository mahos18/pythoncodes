# 1(a) Generate odd and even numbers from start to end using for loop
start = int(input())
end = int(input())
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")

# 1(b) Generate table of a number using while loop
n = int(input())
i = 1
while i <= 10:
    print(n, 'x', i, '=', n * i)
    i += 1

# 2 Mini Calculator
a = int(input())
b = int(input())
op = input()
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("Invalid operator")

# 3 Check if number is Armstrong number
n = int(input())
s = 0
t = n
while t > 0:
    d = t % 10
    s += d ** 3
    t //= 10
if n == s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# 4(a) Return only even numbers from list
l = list(map(int, input().split()))
nl = [x for x in l if x % 2 == 0]
print(nl)

# 4(b) Return tuple with squares
t = tuple(map(int, input().split()))
nt = tuple(x**2 for x in t)
print(nt)

# 4(c) Unique words using set
s = input()
words = s.split()
unique = set(words)
print(unique)

# 5 Creation of class
class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
p = Person(input())
p.display()

# 6 Single and Multiple Inheritance
class A:
    def showA(self):
        print("A")
class B:
    def showB(self):
        print("B")
class C(A, B):
    def showC(self):
        print("C")
c = C()
c.showA()
c.showB()
c.showC()

# 7 Polymorphism with Shape
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        print(3.14 * self.r * self.r)
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        print(self.l * self.b)
s1 = Circle(5)
s2 = Rectangle(4, 6)
for shape in (s1, s2):
    shape.area()

# 8 Maths module for square, square root, factorial
def square(x):
    return x * x
def squareroot(x):
    return x ** 0.5
def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f
n = int(input())
print(square(n))
print(squareroot(n))
print(factorial(n))

# 9 Multithreading for sum and factorial
import threading
def calc_sum(n):
    print(sum(range(1, n+1)))
def calc_fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)
n = int(input())
t1 = threading.Thread(target=calc_sum, args=(n,))
t2 = threading.Thread(target=calc_fact, args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()

# 10 Writing data into CSV
import csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
    writer.writerow(["Bob", 30])

# 11 Menu creation using Tkinter
import tkinter as tk
root = tk.Tk()
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit", command=root.quit)
root.mainloop()

# 12 Application using Tkinter
import tkinter as tk
root = tk.Tk()
root.title("Simple App")
label = tk.Label(root, text="Hello World")
label.pack()
root.mainloop()

# 13 NumPy array operations
import numpy as np
a = np.array([1,2,3])
b = np.array([[1,2],[3,4]])
print(a)
print(b)
a[0] = 10
print(a)
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(np.mean(a))
print(np.reshape(b, (4,1)))
print(a[1:])

# 14 Data visualization using bar chart
import matplotlib.pyplot as plt
x = ['A', 'B', 'C']
y = [10, 20, 15]
plt.bar(x, y)
plt.show()

# 15 SQL Connectivity
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="password", database="testdb")
cur = con.cursor()
cur.execute("SELECT * FROM tablename")
for row in cur.fetchall():
    print(row)
con.close()
