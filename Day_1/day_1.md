1. **What is mutable and immutable? What are Python’s mutable and immutable data types?**  
- Mutable objects can be changed after creation, while immutable objects cannot be changed after creation.
   - **Mutable**: Lists, Sets, Dictionaries.
   - **Immutable**: Tuples, Strings.

---

2. **What is the difference between a shallow copy and a deep copy?**  
   - **Shallow copy** copies the top-level object but not nested objects.  
   - **Deep copy** copies the top-level and nested objects.

---

3. **What are Python’s membership operators?**  
   - `in`: Checks if an element is in a sequence.  
   - `not in`: Checks if an element is not in a sequence.

---

4. **What is a Python lambda function?**  
   - A small, anonymous function defined using the `lambda` keyword. Example:  
     ```python
     x = lambda a, b: a + b
     print(x(3, 4))  # Output: 7
     ```

---

5. **How do you create a dictionary comprehension?**  
   - Example:  
     ```python
     squares = {x: x**2 for x in range(5)}
     print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
     ```

---

6. **What is the difference between `is` and `==`?**  
   - `is`: Checks object identity (memory address).  
   - `==`: Checks object equality (values).  
     Example:  
     ```python
     a = [1, 2]
     b = [1, 2]
     print(a == b)  # True
     print(a is b)  # False
     ```

---

7. **What's the difference between sets and dictionary?**  
   - **Sets**: Unordered collection of unique elements. Mutable.
   - **Dictionaries**: Key-value pairs with unique keys. Mutable.

---

8. **Differentiate between List and Tuple?**
    - **List**: Mutable, denoted by square brackets `[]`.
    - **Tuple**: Immutable, denoted by parentheses `()`.

---

9. **What is Python’s `zip()` function used for?**  
   - Combines elements from multiple iterables into tuples. Example:  
     ```python
     a = [1, 2]
     b = ['x', 'y']
     print(list(zip(a, b)))  # Output: [(1, 'x'), (2, 'y')]
     ```

---

10. **What is the difference between `append()` and `extend()` in Python?**  
    - `append()`: Adds an element to the end of a list.  
    - `extend()`: Adds elements from an iterable to the end of a list.  
      Example:  
      ```python
      a = [1, 2]
      a.append([3, 4])
      print(a)  # Output: [1, 2, [3, 4]]
      b = [1, 2]
      b.extend([3, 4])
      print(b)  # Output: [1, 2, 3, 4]
      ```

---

11. **How to remove duplicates from a list in Python?**  
    - Using a set to remove duplicates:  
      ```python
      a = [1, 2, 2, 3]
      print(list(set(a)))  # Output: [1, 2, 3]
      ```

---

12. **What are Python’s `args` and `kwargs`?**  
    - `*args`: Accepts variable-length positional arguments.  
    - `**kwargs`: Accepts variable-length keyword arguments.  
      Example:  
      ```python
      def func(*args, **kwargs):
          print(args, kwargs)
      func(1, 2, a=3, b=4)  # Output: (1, 2) {'a': 3, 'b': 4}
      ```

---

13. **Explain Python’s generator functions.**  
    - Use `yield` instead of `return` to generate values one at a time. They save memory by not storing all values at once.  
      Example:  
      ```python
      def gen():
          for i in range(3):
              yield i
      print(list(gen()))  # Output: [0, 1, 2]
      ```

---

14. **How does Python’s garbage collection work?**  
    - Python uses reference counting and cyclic garbage collection to reclaim unused memory.

---

15. **which is faster list comprehension or for loop?**  
    - List comprehension is faster than a for loop because it is optimized for the Python interpreter.

---

16. **How does Python handle errors?**  
    - Using `try-except` blocks. Example:  
      ```python
      try:
          x = 1 / 0
      except ZeroDivisionError as e:
          print(e)
      ```

---

17. **What are Python decorators?**  
    - Functions that modify the behavior of other functions.  
      Example:  
      ```python
      def decorator(func):
          def wrapper():
              print("Before the function")
              func()
              print("After the function")
          return wrapper

      @decorator
      def say_hello():
          print("Hello!")
      say_hello()
      ```
    Here `decorator` is a decorator function that modifies the behavior of `say_hello` by adding print statements before and after the function call.

---

18. **What is a Python metaclass?**  
    - A metaclass is a class of a class that defines how a class behaves.

---

19. **What are Python’s list comprehensions?**  
    - Syntax for creating a list from an iterable in a single line.  
      Example:  
      ```python
      nums = [x for x in range(5) if x % 2 == 0]
      print(nums)  # Output: [0, 2, 4]
      ```

---

20. **How can you reverse a string in Python?**  
    - Using slicing:  
      ```python
      s = "hello"
      print(s[::-1])  # Output: "olleh"
      ```  

--- 
