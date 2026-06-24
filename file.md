# Python Arrays and Lists - Complete Notes

## What is an Array?

An Array is a data structure used to store multiple values under a single name.

### Example

```python
numbers = [10, 20, 30, 40, 50]
```

Instead of creating multiple variables:

```python
a = 10
b = 20
c = 30
d = 40
e = 50
```

we store them in a single collection.

---

## Formal Definition

> An array is a collection of elements stored in contiguous memory locations and accessed using an index.

---

# Why Are Python Arrays Different?

In languages like C, C++, and Java, arrays store elements of the same data type.

## C Array

```c
int arr[5] = {10,20,30,40,50};
```

Only integers are allowed.

## Python List

```python
arr = [10, "Hello", 3.14, True]
```

Python allows different data types because Lists store references to objects.

---

# Array vs Python List

| Feature          | C/C++ Array | Python List |
| ---------------- | ----------- | ----------- |
| Fixed Size       | Yes         | No          |
| Dynamic Size     | No          | Yes         |
| Mixed Data Types | No          | Yes         |
| Memory Efficient | More        | Less        |
| Flexible         | Less        | More        |

---

# How Arrays Access Memory

Array:

```text
[10,20,30,40,50]
```

Memory:

```text
Address      Value

1000 -----> 10
1004 -----> 20
1008 -----> 30
1012 -----> 40
1016 -----> 50
```

Elements are stored one after another.

This is called:

```text
Contiguous Memory Allocation
```

---

# How Indexing Works

Array:

```python
arr = [10,20,30,40,50]
```

Formula:

```text
Address = Base Address + (Index × Size)
```

Example:

```text
arr[2]

Address = 1000 + (2 × 4)

Address = 1008
```

Value:

```text
30
```

---

# Why Array Access is O(1)

```python
print(arr[3])
```

The computer directly calculates:

```text
Base Address + Index
```

This is called:

```text
Random Access
```

Time Complexity:

```text
O(1)
```

---

# Stack and Heap Memory

## Python Example

```python
arr = [10,20,30]
```

Memory:

```text
STACK

arr
 |
 v

HEAP

[10][20][30]
```

### Stack Stores

```text
Reference Variable
```

### Heap Stores

```text
Actual List Object
```

---

# Accessing arr[1]

```python
print(arr[1])
```

Steps:

1. Find `arr` in Stack
2. Get Heap Address
3. Calculate Index Position
4. Return Value

Output:

```text
20
```

---

# Python Internal Representation

```python
arr = [10,20,30]
```

```text
STACK

arr
 |
 v

HEAP

List Object
 |
 +----> Integer Object 10
 |
 +----> Integer Object 20
 |
 +----> Integer Object 30
```

Python stores references to objects.

---

# Why Python Lists Can Store Mixed Types

```python
arr = [10, "Hello", True]
```

Each element is an object reference.

Therefore different data types can exist together.

---

# Real Array in Python

```python
from array import array

arr = array('i', [10,20,30,40])
```

Here:

```text
i = integer
```

Only integers are allowed.

This follows the homogeneous array rule.

---

# Creating Lists

## Integer List

```python
numbers = [10,20,30,40,50]
```

## String List

```python
fruits = ["Apple","Banana","Mango"]
```

## Mixed List

```python
data = [10,"Python",3.14,True]
```

## Empty List

```python
arr = []
```

## Using range()

```python
numbers = list(range(1,6))
```

Output:

```python
[1,2,3,4,5]
```

---

# List Characteristics

## Ordered

```python
fruits = ["Apple","Banana","Mango"]
```

## Mutable

```python
fruits[0] = "Orange"
```

## Dynamic

```python
arr.append(30)
```

## Mixed Data Types

```python
data = [10,"Hello",True]
```

---

# Accessing Elements

```python
arr = [10,20,30]

print(arr[0])
print(arr[1])
```

Output:

```text
10
20
```

---

# Negative Indexing

```python
print(arr[-1])
```

| Index | Meaning      |
| ----- | ------------ |
| -1    | Last Element |
| -2    | Second Last  |
| -3    | Third Last   |

---

# Traversing a List

```python
for item in arr:
    print(item)
```

---

# Length of List

```python
len(arr)
```

---

# Add Elements

## append()

```python
arr.append(40)
```

## insert()

```python
arr.insert(1,15)
```

## extend()

```python
a.extend(b)
```

---

# Remove Elements

## remove()

```python
arr.remove(20)
```

## pop()

```python
arr.pop()
```

## clear()

```python
arr.clear()
```

---

# Searching

```python
20 in arr
```

Output:

```text
True
```

---

# Sorting

```python
arr.sort()
```

---

# Reverse Sorting

```python
arr.sort(reverse=True)
```

---

# Reverse List

```python
arr.reverse()
```

---

# Slicing

```python
arr[1:4]
```

Output:

```python
[20,30,40]
```

---

# List Comprehension

```python
numbers = [x for x in range(5)]
```

Output:

```python
[0,1,2,3,4]
```

---

# 2D List

```python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[1][2])
```

Output:

```text
6
```

---

# Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Access    | O(1)       |
| Update    | O(1)       |
| Search    | O(n)       |
| Append    | O(1)       |
| Insert    | O(n)       |
| Delete    | O(n)       |
| Sort      | O(n log n) |

---

# List vs Tuple

| Feature       | List | Tuple |
| ------------- | ---- | ----- |
| Mutable       | Yes  | No    |
| Syntax        | []   | ()    |
| Faster        | No   | Yes   |
| Change Values | Yes  | No    |

---

# Viva Answer

A List in Python is a dynamic, ordered, and mutable collection of elements. Python lists are implemented as dynamic arrays and provide O(1) access using indexes. Unlike traditional arrays, Python lists can store different data types because they store references to objects rather than actual values.
