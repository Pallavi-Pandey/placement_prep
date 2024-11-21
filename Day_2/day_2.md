1. **How do you check the type of a variable in Python?**  
   - Use the `type()` function.  
     ```python
     x = 42
     print(type(x))  # Output: <class 'int'>
     ```

---

2. **What is Python’s `None` keyword?**  
   - Represents the absence of a value or a null value. It is a singleton object of type `NoneType`.

---

3. **What are Python’s logical operators?**  
   - `and`, `or`, `not`. Example:  
     ```python
     print(True and False)  # Output: False
     print(not True)        # Output: False
     ```

---

4. **How do you combine multiple strings in Python?**  
   - Use concatenation (`+`) or the `join()` method.  
     ```python
     result = "Hello" + " " + "World"
     result = " ".join(["Hello", "World"])
     ```

---

5. **Can you insert a element at beginning of a list using `append()`?**  
   - No, `append()` adds an element at the end of a list. To add an element at the beginning, use the `insert()` method.  
     ```python
     lst = [2, 3]
     lst.insert(0, 1)
     print(lst)  # Output: [1, 2, 3]
     ```

---

6. **how to take more than one input in a single line in python?**  
   - Use the `split()` method.  
     ```python
     a, b = input().split()
     print(a, b)
     ```

---

7. **What is walrus operator in python?**  
   - The walrus operator `:=` is used to assign values to variables as part of a larger expression.  
     ```python
     if (n := len([1, 2, 3])) > 2:
         print(f"List is too long ({n} elements, expected <= 2)")
         # Output: List is too long (3 elements, expected <= 2)
         # Here, the length of the list is assigned to `n` and checked in the same line.
     ```
---

8. **Difference between set and tuple in python?**  
   - **Set**: An unordered collection of unique elements. Mutable.  
   - **Tuple**: An ordered collection of elements. Immutable.  
     ```python
     s = {1, 2, 3}
     t = (1, 2, 3)
     ```

---

9. **What is the difference between `split()` and `rsplit()` in Python?**  
   - `split()` splits from the left, `rsplit()` splits from the right.  
     ```python
     text = "1,2,3"
     print(text.split(',', 1))  # Output: ['1', '2,3']
     print(text.rsplit(',', 1))  # Output: ['1,2', '3']
     ```

---

10. **Can you add a list in tuple? If yes, then will it be mutable? Explain.**
    - Yes, you can add a list to a tuple. However, the list remains mutable.  
      ```python
      t = (1, [2, 3])
      t[1].append(4)
      print(t)  # Output: (1, [2, 3, 4])
      ```
---

11. **What is Python’s `enumerate()` function?**  
    - Returns an enumerate object that yields pairs of index and value.
      ```python
      for idx, val in enumerate(["a", "b"]):
          print(idx, val)  # Output: 0 a, 1 b
      ```

---

12. **How do you merge two dictionaries in Python?**  
    - Use the `update()` method or dictionary unpacking (`**`).  
      ```python
      d1 = {'a': 1}
      d2 = {'b': 2}
      d1.update(d2)
        print(d1)
        # Output: {'a': 1, 'b': 2}
      # OR
      merged = {**d1, **d2}
      # Output: {'a': 1, 'b': 2}
      ```

---

13. **What is the purpose of Python’s `id()` function?**  
    - Returns the unique identifier (memory address) of an object.  
      ```python
      x = 10
      print(id(x))
      # output: 140732674073552
      ```

---

14. **How to add element at the beginning of the list in Python?**  
    - Use the `insert()` method.  
      ```python
      lst = [2, 3]
      lst.insert(0, 1)
      print(lst)  # Output: [1, 2, 3]
      ```

---

15. **What is Python’s `any()` and `all()`?**  
    - **`any()`**: Returns `True` if any element in an iterable is true.  
    - **`all()`**: Returns `True` if all elements in an iterable are true.  
      ```python
      print(any([0, 1, 2]))  # True
      print(all([1, 2, 3]))  # True
      ```

---

16. **How do you reverse a list without using slicing?**  
    - Use the `reverse()` method or `reversed()`.  
      ```python
      lst = [1, 2, 3]
      lst.reverse()  # In-place
      print(list(reversed(lst)))  # Returns a new reversed list
      ```

---

17. **What is a Python property?**  
    - Allows you to define methods that can be accessed like attributes.  
      ```python
      class Person:
          def __init__(self, name):
              self._name = name
          @property
          def name(self):
              return self._name
      p = Person("Alice")
      print(p.name)  # Output: Alice
      ```

---

18. **What are Python’s string formatting options?**  
    - **`%` Operator**, `.format()`, and f-strings. Example:  
      ```python
      name = "John"
      print(f"Hello, {name}!")  # f-string
      print("Hello, {}!".format(name))  # .format()
      # output: Hello, John!
      ```

---

19. **How do you find the most common elements in a list?**  
    - Use `collections.Counter`.  
      ```python
      from collections import Counter
      lst = [1, 2, 2, 3]
      most_common = Counter(lst).most_common(1)
      print(most_common)  # Output: [(2, 2)]
      ```

---

20. **What is the difference between `iter()` and `next()`?**  
    - `iter()`: Returns an iterator from an iterable.  
    - `next()`: Fetches the next element from the iterator.  
      ```python
      itr = iter([1, 2, 3])
      print(next(itr))  # Output: 1
      # Here `iter()` creates an iterator from the list, and `next()` fetches the next element. The ouput is 1 because it fetches the first element.
      ```

---