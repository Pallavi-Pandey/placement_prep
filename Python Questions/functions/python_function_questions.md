# 30 Practical Python Function Questions with Test Cases

---

## 1. Write a function `add(a, b)` that returns the sum of two numbers.

```python
add(1, 2)         # 3
add(0, 0)         # 0
add(-1, 1)        # 0
add(100, 200)     # 300
add(-5, -7)       # -12
```

## 2. Write a function `is_even(n)` that checks if a number is even.
```python
is_even(2)        # True
is_even(3)        # False
is_even(0)        # True
is_even(-2)       # True
is_even(-5)       # False
```

## 3. Write a function `max_of_three(a, b, c)` that returns the maximum of three numbers.
```python
max_of_three(1, 2, 3)       # 3
max_of_three(3, 2, 1)       # 3
max_of_three(0, 0, 0)       # 0
max_of_three(-1, -5, -3)    # -1
max_of_three(10, 100, 50)   # 100
```

## 4. Write a function `greet(name)` that returns a greeting string.
```python
greet("Alice")     # "Hello, Alice!"
greet("Bob")       # "Hello, Bob!"
greet("Charlie")   # "Hello, Charlie!"
greet("")          # "Hello, !"
greet("123")       # "Hello, 123!"
```

## 5. Write a function `reverse_string(s)` that returns the reversed string.
```python
reverse_string("hello")      # "olleh"
reverse_string("")           # ""
reverse_string("a")          # "a"
reverse_string("racecar")    # "racecar"
reverse_string("Python")     # "nohtyP"
```

## 6. Write a function `factorial(n)` that returns the factorial of a number.
```python
factorial(0)     # 1
factorial(1)     # 1
factorial(3)     # 6
factorial(5)     # 120
factorial(7)     # 5040
```

## 7. Write a function `is_palindrome(s)` that checks if a string is a palindrome.
```python
is_palindrome("madonna")   # False
is_palindrome("madam")     # True
is_palindrome("racecar")   # True
is_palindrome("a")         # True
is_palindrome("ab")        # False
```

## 8. Write a function `count_vowels(s)` that returns the number of vowels in a string.
```python
count_vowels("hello")       # 2
count_vowels("world")       # 1
count_vowels("AEIOU")       # 5
count_vowels("xyz")         # 0
count_vowels("education")   # 5
```

## 9. Write a function `fibonacci(n)` that returns the nth Fibonacci number.
```python
fibonacci(0)      # 0
fibonacci(1)      # 1
fibonacci(5)      # 5
fibonacci(7)      # 13
fibonacci(10)     # 55
```

## 10. Write a function `is_prime(n)` that checks if a number is prime.
```python
is_prime(1)       # False
is_prime(2)       # True
is_prime(3)       # True
is_prime(4)       # False
is_prime(13)      # True
```

## 11. Write a function `sum_list(lst)` that returns the sum of all elements in a list.
```python
sum_list([1, 2, 3])        # 6
sum_list([])               # 0
sum_list([-1, -2, 3])      # 0
sum_list([10, 20, 30])     # 60
sum_list([0, 0, 0])        # 0
```

## 12. Write a function `find_max(lst)` that returns the maximum number in a list.
```python
find_max([1, 2, 3])        # 3
find_max([-1, -2, -3])     # -1
find_max([5])              # 5
find_max([3, 3, 3])        # 3
find_max([10, 20, 5])      # 20
```

## 13. Write a function `is_anagram(s1, s2)` that checks if two strings are anagrams.
```python
is_anagram("listen", "silent")   # True
is_anagram("triangle", "integral") # True
is_anagram("hello", "world")     # False
is_anagram("rat", "car")         # False
is_anagram("a", "a")             # True
```

## 14. Write a function `square_list(lst)` that returns a list of squares of the numbers.
```python
square_list([1, 2, 3])        # [1, 4, 9]
square_list([0])              # [0]
square_list([-1, 2])          # [1, 4]
square_list([])               # []
square_list([10])             # [100]
```

## 15. Write a function `remove_duplicates(lst)` that removes duplicates from a list.
```python
remove_duplicates([1, 2, 2, 3])    # [1, 2, 3]
remove_duplicates([])             # []
remove_duplicates([5, 5, 5])      # [5]
remove_duplicates([1, 2, 3])      # [1, 2, 3]
remove_duplicates([4, 4, 4, 4])   # [4]
```

## 16. Write a function `multiply_list(lst)` that multiplies all numbers in a list.
```python
multiply_list([1, 2, 3])      # 6
multiply_list([0, 1, 2])      # 0
multiply_list([5])            # 5
multiply_list([-1, 2, -3])    # 6
multiply_list([])             # 1 (identity)
```

## 17. Write a function `capitalize_words(s)` that capitalizes the first letter of each word.
```python
capitalize_words("hello world")      # "Hello World"
capitalize_words("python is fun")    # "Python Is Fun"
capitalize_words("a b c")            # "A B C"
capitalize_words("")                 # ""
capitalize_words("test")             # "Test"
```

## 18. Write a function `is_substring(s1, s2)` that checks if `s1` is a substring of `s2`.
```python
is_substring("he", "hello")          # True
is_substring("world", "hello")       # False
is_substring("", "text")             # True
is_substring("a", "abc")             # True
is_substring("text", "")             # False
```

## 19. Write a function `to_celsius(f)` that converts Fahrenheit to Celsius.
```python
to_celsius(32)       # 0.0
to_celsius(212)      # 100.0
to_celsius(98.6)     # 37.0
to_celsius(0)        # -17.78
to_celsius(-40)      # -40.0
```

## 20. Write a function `to_fahrenheit(c)` that converts Celsius to Fahrenheit.
```python
to_fahrenheit(0)       # 32.0
to_fahrenheit(100)     # 212.0
to_fahrenheit(37)      # 98.6
to_fahrenheit(-40)     # -40.0
to_fahrenheit(20)      # 68.0
```

## 21. Write a function `get_middle(s)` that returns the middle character(s) of a string.
```python
get_middle("abc")       # "b"
get_middle("abcd")      # "bc"
get_middle("a")         # "a"
get_middle("")          # ""
get_middle("middle")    # "dd"
```

## 22. Write a function `remove_spaces(s)` that removes all spaces from a string.
```python
remove_spaces("a b c")         # "abc"
remove_spaces(" hello ")       # "hello"
remove_spaces("no spaces")     # "nospaces"
remove_spaces("")              # ""
remove_spaces("    ")          # ""
```

## 23. Write a function `sum_even(lst)` that returns the sum of even numbers in a list.
```python
sum_even([1, 2, 3, 4])     # 6
sum_even([1, 3, 5])        # 0
sum_even([])               # 0
sum_even([2, 4, 6])        # 12
sum_even([10, -2])         # 8
```

## 24. Write a function `sum_odd(lst)` that returns the sum of odd numbers in a list.
```python
sum_odd([1, 2, 3, 4])      # 4
sum_odd([1, 3, 5])         # 9
sum_odd([])                # 0
sum_odd([2, 4, 6])         # 0
sum_odd([11, -3])          # 8
```

## 25. Write a function `flatten_list(nested)` that flattens a list of lists.
```python
flatten_list([[1, 2], [3, 4]])     # [1, 2, 3, 4]
flatten_list([[1], [], [2]])      # [1, 2]
flatten_list([])                  # []
flatten_list([[], []])            # []
flatten_list([[0], [1, 2, 3]])    # [0, 1, 2, 3]
```

## 26. Write a function `merge_dicts(d1, d2)` that merges two dictionaries.
```python
merge_dicts({'a': 1}, {'b': 2})               # {'a': 1, 'b': 2}
merge_dicts({}, {})                           # {}
merge_dicts({'a': 1}, {'a': 2})               # {'a': 2}
merge_dicts({'x': 10}, {'y': 20, 'z': 30})    # {'x': 10, 'y': 20, 'z': 30}
merge_dicts({'k': 1}, {})                     # {'k': 1}
```

## 27. Write a function `char_frequency(s)` that counts the frequency of each character.
```python
char_frequency("aab")         # {'a': 2, 'b': 1}
char_frequency("")            # {}
char_frequency("abcabc")      # {'a': 2, 'b': 2, 'c': 2}
char_frequency("x")           # {'x': 1}
char_frequency("mississippi")# {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

## 28. Write a function `is_uppercase(s)` that checks if all characters are uppercase.
```python
is_uppercase("HELLO")     # True
is_uppercase("Hello")     # False
is_uppercase("")          # False
is_uppercase("123")       # False
is_uppercase("UPPER")     # True
```

## 29. Write a function `title_case(s)` that converts a string to title case.
```python
title_case("hello world")    # "Hello World"
title_case("python code")    # "Python Code"
title_case("")               # ""
title_case("a")              # "A"
title_case("title case")     # "Title Case"
```

## 30. Write a function `unique_elements(lst)` that returns a list of unique elements.
```python
unique_elements([1, 2, 2, 3])       # [1, 2, 3]
unique_elements([])                # []
unique_elements([4, 4, 4])         # [4]
unique_elements([5, 6, 5, 6])      # [5, 6]
unique_elements([1, 2, 3])         # [1, 2, 3]
```
