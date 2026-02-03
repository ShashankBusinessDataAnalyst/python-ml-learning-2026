# 📘 Day 2 — Loops & Conditions  
**Date:** 02/02/2026  
**Topic:** Flow Control (if/elif/else, loops, boolean logic)  
**Books Covered:**  
- Python Crash Course — Chapter 5  
- Automate the Boring Stuff — Chapter 2  

---

# 🧠 Key Concepts Learned

## 🔹 1. Conditional Statements (if / elif / else)
- `if` is used to check a condition and execute code when it is true.
- `elif` (else if) allows multiple conditional checks.
- `else` runs only when all previous conditions fail.

### Example:
```python
score = 85

if score >= 90:
    print("A Grade")
elif score >= 75:
    print("B Grade")
else:
    print("C Grade")
```

---

## 🔹 2. Conditional Tests / Comparison Operators
| Operator | Meaning | Example |
|---------|----------|---------|
| == | Equal to | x == 10 |
| != | Not equal | x != 5 |
| > | Greater than | x > 3 |
| < | Less than | x < 8 |
| >= | Greater or equal | age >= 18 |
| <= | Less or equal | marks <= 40 |

These return **True** or **False**.

---

## 🔹 3. Boolean Logic (and, or, not)
Combine multiple conditions:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
```

---

## 🔹 4. For Loops
Used for iterating over sequences.

```python
for item in ["apple", "banana", "orange"]:
    print(item)
```

### Using range():
```python
for i in range(1, 6):
    print(i)
```

---

## 🔹 5. While Loops
Runs as long as a condition is **True**.

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

---

## 🔹 6. break & continue

### break → exits loop immediately
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### continue → skips current iteration
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

---

# 📝 My Notes & Understanding (Fill This Section)

## 🔹 What I Learned Today
- I learned how to use conditional statements (`if`, `elif`, `else`) to make decisions in a Python program.
- I understood how and when to use different types of loops (`for` and `while`) based on the situation.
- I practiced using comparison and logical operators to build smarter conditions.
- I learned how `break` and `continue` control the flow inside loops.
- I now understand how loops can repeat tasks efficiently without writing repetitive code.



## 🔹 Summary in My Own Words
Conditions allow a program to make decisions by checking whether certain expressions are true or false. Loops help repeat tasks multiple times without rewriting code, making programs more efficient. A for loop is best used when you know exactly how many times you want to iterate (like iterating over a list or a range). A while loop is used when you want the loop to run until a condition becomes false (like a guessing game or waiting for user input). Together, conditions and loops form the foundation of all logical programming and automation tasks.

---

# 💻 Practice Code from Today

### ✔ Positive / Negative / Zero Checker
```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

### ✔ Print Numbers 1–50
```python
for i in range(1, 51):
    print(i)
```

### ✔ Even Numbers 1–100
```python
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
```

### ✔ Loop Through Names
```python
names = ["Shashank", "Ravi", "Anita"]

for name in names:
    print("Hello", name)
```

### ✔ Number Guessing (while loop)
```python
target = 7
guess = 0

while guess != target:
    guess = int(input("Guess the number: "))

print("Correct!")
```


