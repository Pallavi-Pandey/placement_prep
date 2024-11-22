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
---

### **What is `collections.Counter`?**
- `Counter` is a class in the `collections` module that is specifically designed to count the occurrences of elements in a collection like a list, tuple, or string.
- It returns a dictionary-like object where keys are the elements, and values are the counts of those elements.

---

### **Why Use `Counter` for Finding the Most Common Elements?**
- The `Counter` class has a method called `.most_common(n)` that retrieves the `n` most frequent elements in descending order of their frequency.
- This makes it a concise and efficient way to find the most common elements in a list.

---

### **Example and Explanation**
**Code:**
```python
from collections import Counter

lst = [1, 2, 2, 3]
most_common = Counter(lst).most_common(1)  # Find the most common element
print(most_common)
```

**Steps Explained:**
1. **Create a `Counter` object**:
   ```python
   counts = Counter(lst)
   ```
   This produces:
   ```python
   Counter({2: 2, 1: 1, 3: 1})
   ```
   - The keys are the elements from the list.
   - The values are their respective counts.

2. **Use `.most_common(1)`**:
   ```python
   most_common = counts.most_common(1)
   ```
   - This retrieves the single most frequent element.
   - The result is:
     ```python
     [(2, 2)]
     ```
     - `2` is the most common element.
     - It appears `2` times in the list.

3. **Print the Result**:
   ```python
   print(most_common)
   ```
   The output is:
   ```python
   [(2, 2)]
   ```
   - The list contains tuples, where the first element of the tuple is the item, and the second is the count.

---

### **Accessing the Most Common Element Only**
If you want just the most common element (without the count), you can extract it like this:
```python
most_common_element = most_common[0][0]
print(most_common_element)  # Output: 2
```

---

### **Finding More Than One Common Element**
To find the top `n` most common elements, pass `n` to `.most_common(n)`:
```python
most_common_2 = Counter(lst).most_common(2)
print(most_common_2)  # Output: [(2, 2), (1, 1)]
```

---

### **Handling Ties**
If multiple elements have the same frequency, `most_common()` orders them by their first appearance in the iterable.

**Example:**
```python
lst = [3, 1, 2, 2, 1, 3]
most_common = Counter(lst).most_common(2)
print(most_common)  # Output: [(3, 2), (1, 2)]
```

---

### **Use Case**
`Counter` and `.most_common()` are particularly useful when:
1. Analyzing data for frequently occurring elements (e.g., words in a text).
2. Summarizing data frequency in lists or strings.

---

### **Full Example**
```python
from collections import Counter

# Sample list
lst = [1, 2, 2, 3, 3, 3, 4]

# Count the elements
counts = Counter(lst)

# Find the most common element
most_common = counts.most_common(1)

# Print the results
print(f"Counts: {counts}")                # Output: Counts: Counter({3: 3, 2: 2, 1: 1, 4: 1})
print(f"Most Common: {most_common}")      # Output: Most Common: [(3, 3)]
```

---
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
---

### **What is `iter()`?**
- The `iter()` function is used to convert an **iterable** (like a list, tuple, or string) into an **iterator**. 
- An **iterator** is an object that allows you to traverse through its elements one at a time.

**Example:**  
```python
lst = [1, 2, 3]
itr = iter(lst)  # `itr` is now an iterator object created from the list.
```

At this point, `itr` is ready to provide elements of the list **sequentially**, one at a time, when accessed with the `next()` function.

---

### **What is `next()`?**
- The `next()` function is used to fetch the **next element** from an iterator. 
- Each time you call `next()`, the iterator returns the next item in the sequence.
- If the iterator reaches the end of the sequence and you call `next()` again, it raises a **`StopIteration`** exception.

**Example:**  
```python
print(next(itr))  # Output: 1 (fetches the first element)
print(next(itr))  # Output: 2 (fetches the second element)
print(next(itr))  # Output: 3 (fetches the third element)
print(next(itr))  # Raises StopIteration
```

---

### **How They Work Together**
- `iter()` creates the iterator, and `next()` is used to retrieve items from it.  
- Without `iter()`, you cannot use `next()` on an iterable because it is not yet an iterator.

---

### **Key Differences Between `iter()` and `next()`**
1. **Purpose**:
   - `iter()` is used to **create** an iterator from an iterable.
   - `next()` is used to **retrieve the next item** from an iterator.

2. **Return Value**:
   - `iter()` returns an iterator object.
   - `next()` returns the next item from the iterator.

---

### **Complete Example**:
```python
lst = [10, 20, 30]   # A list (iterable)
itr = iter(lst)      # Convert the list into an iterator

print(next(itr))     # Output: 10 (first element)
print(next(itr))     # Output: 20 (second element)
print(next(itr))     # Output: 30 (third element)
# If you call next(itr) again, it will raise StopIteration
```

---

### **How Does `StopIteration` Work?**
The iterator tracks the current position in the sequence. Once all elements are exhausted, calling `next()` will raise `StopIteration` to signal that there are no more items left.

**Example:**
```python
itr = iter([1])  # Single-element list
print(next(itr))  # Output: 1
print(next(itr))  # Raises StopIteration
```

---