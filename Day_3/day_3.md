### **1. What is the difference between `isinstance()` and `type()`?**  
- `isinstance()` checks if an object is an instance of a class or a subclass.  
- `type()` checks the exact type of an object and doesn’t consider inheritance.

**Example:**
```python
class Animal: pass
class Dog(Animal): pass

d = Dog()

print(isinstance(d, Dog))  # True
print(isinstance(d, Animal))  # True (Dog is a subclass of Animal)
print(type(d) == Dog)  # True
print(type(d) == Animal)  # False (type() doesn't consider inheritance)
```

---

### **2. What is the difference between `@staticmethod` and `@classmethod`?**  
- `@staticmethod`: Doesn't take the class instance (`self`) or class reference (`cls`) as the first parameter.  
- `@classmethod`: Takes `cls` as the first parameter and works with the class rather than instance-specific data.

**Example:**
```python
class MyClass:
    @staticmethod
    def static_method():
        print("I don't access class or instance.")

    @classmethod
    def class_method(cls):
        print(f"I access the class: {cls}")

MyClass.static_method()  # I don't access class or instance.
MyClass.class_method()   # I access the class: <class '__main__.MyClass'>
```

---

### **3. Explain the `super()` function.**  
- `super()` is used to call methods from the parent class in a child class.

**Example:**
```python
class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        super().greet()  # Calls Parent's greet()
        print("Hello from Child!")

c = Child()
c.greet()
# Output:
# Hello from Parent!
# Hello from Child!
```

---

### **4. What happens if you override a method in Python?**  
- The overridden method in the child class replaces the method in the parent class.

**Example:**
```python
class A:
    def display(self):
        print("A's display")

class B(A):
    def display(self):
        print("B's display")

obj = B()
obj.display()  # Output: B's display
```

---

### **5. What is method resolution order (MRO) in Python?**  
- MRO defines the order in which Python looks for a method in a hierarchy of classes.

**Example:**
```python
class A: pass
class B(A): pass
class C(B): pass

print(C.mro())
# Output: [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
```

---

### **6. What are abstract base classes (ABCs)?**  
- ABCs define a blueprint for derived classes and enforce the implementation of certain methods.

**Example:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())  # Output: 78.5
```

---

### **7. How to access key and value of a dictionary?**
- Use `items()` to access both key and value.
**Example:**
```python
d = {'name': 'Alice', 'age': 30}

for key, value in d.items():
    print(key, value)
# Output:
# name Alice
# age 30
``` 


---


### **8. Explain multiple inheritance with an example.**  
- A class can inherit from more than one class.

**Example:**
```python
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()  # Output: Hello from A (MRO determines this)
```

---

### **9. How does Python handle circular inheritance?**  
Python raises an error if circular inheritance is detected.

**Example:**
```python
# Invalid Code Example
class A(A):
    pass
# TypeError: a class cannot directly inherit from itself
```

---

### **10. What is `@property` in Python?**  
- `@property` is used to define getter methods that make attributes accessible like properties.

**Example:**
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

c = Circle(5)
print(c.radius)  # Output: 5
c.radius = 10
print(c.radius)  # Output: 10
```

---

### **11. What is the difference between `__str__` and `__repr__`?**  
- `__str__`: Returns a readable string representation for end users.
- `__repr__`: Returns an unambiguous string for developers.

**Example:**
```python
class Person:
    def __str__(self):
        return "Person: Human-readable representation"

    def __repr__(self):
        return "Person(name='John', age=30)"

p = Person()
print(str(p))  # Output: Person: Human-readable representation
print(repr(p))  # Output: Person(name='John', age=30)
```

---

### **12. What are `args` and `kwargs`?**  
- `*args`: Collects positional arguments into a tuple.  
- `**kwargs`: Collects keyword arguments into a dictionary.

**Example:**
```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, 3, name="Alice", age=30)
# Output:
# (1, 2, 3)
# {'name': 'Alice', 'age': 30}
```

---

### **13. Can you change a global variable inside a function?**  
- Use the `global` keyword to modify global variables.

**Example:**
```python
x = 10

def modify():
    global x
    x = 20

modify()
print(x)  # Output: 20
```

---

### **14. Explain `with` statement and context managers.**  
- Used to ensure resource cleanup (like file closing).

**Example:**
```python
with open('file.txt', 'w') as f:
    f.write("Hello, World!")
# Automatically closes the file
```

---

### **15. What are metaclasses in Python?**  
- Metaclasses control the creation of classes themselves.

**Example:**
```python
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass
# Output: Creating class MyClass
```

---

### **16. What are the types of inheritance in Python?**
- Single inheritance: A class inherits from a single base class.
- Multiple inheritance: A class inherits from multiple base classes.
- Multilevel inheritance: A class inherits from a class, which in turn inherits from another class.
- Hierarchical inheritance: Multiple classes inherit from a single base class.

---

### **17. How to implement a singleton class in Python?**  
- Singleton ensures only one instance exists.

**Example:**
```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True
```

---

### **18. What is the `__slots__` attribute?**  
- Restricts attribute creation to save memory.

**Example:**
```python
class MyClass:
    __slots__ = ['name', 'age']

obj = MyClass()
obj.name = "Alice"  # Allowed
# obj.address = "Wonderland"  # AttributeError
```

---

### **19. How does Python handle multiple `except` blocks?**  
- It checks them in order and runs the first matching block.

**Example:**
```python
try:
    1 / 0
except ZeroDivisionError:
    print("ZeroDivisionError")
except Exception:
    print("General Exception")
# Output: ZeroDivisionError
```

---

### **20. Explain Python’s garbage collection.**  
- Python uses reference counting and garbage collection to reclaim memory of unused objects.  
- The `gc` module controls garbage collection.

**Example:**
```python
import gc
gc.collect()  # Manually trigger garbage collection
``` 

---