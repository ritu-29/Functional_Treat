# Functional_Treat.py

This project is a **menu-driven Python program** that demonstrates important **Python concepts** such as:
- Functions
- Methods
- Lists (1D & 2D)
- Recursion
- Lambda, filter
- *args and **kwargs
- Built-in functions

---

## 📌 Program Overview

The program allows the user to:
1. Enter **1D or 2D data**
2. Display **dataset summary**
3. Calculate **factorial using recursion**
4. Filter data using **lambda function**
5. Sort data (ascending/descending)
6. Get multiple statistics from a function

---

## 🧠 Concepts Explained (Simple)

### 1️⃣ Functions
Functions are reusable blocks of code.

Example:
```python
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
```
👉 This function calculates **factorial** using **recursion**.

---

### 2️⃣ Global Variable
```python
data = []
dataset = {}
```
👉 These variables are accessible across functions.

---

### 3️⃣ 1D and 2D List Input
- **1D list**: `[1, 2, 3]`
- **2D list (matrix)**:
```python
[[1,2,3],
 [4,5,6],
 [7,8,9]]
```

The function `input_data()` takes user input for both.

---

### 4️⃣ Built-in Methods Used
| Method | Use |
|------|-----|
| `min()` | Find minimum |
| `max()` | Find maximum |
| `sum()` | Total |
| `len()` | Count elements |
| `sort()` | Sort list |

---

### 5️⃣ Lambda & Filter
```python
filter(lambda x: x >= t, flat)
```
👉 Filters values **greater than or equal to threshold**.

---

### 6️⃣ *args
```python
def show_args(*args):
```
👉 Accepts **multiple values** as arguments.

---

### 7️⃣ **kwargs
```python
def show_kwargs(**kwargs):
```
👉 Accepts **key-value pairs** (dictionary style).

---

### 8️⃣ Return Multiple Values
```python
return min(flat), max(flat), sum(flat), avg
```
👉 Python can return **multiple values at once**.

---

## ▶ How to Run
```bash
python Functional_Treat.py
```

---

## ✅ Learning Outcome
After this program, you will understand:
- How to work with lists
- How functions work
- Recursion logic
- Data filtering & sorting
- args & kwargs usage

---

✨ **Perfect for beginners & practice**
