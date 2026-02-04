# 📘 Day 3 — Functions  
**Date:** 03/02/2026  
**Week:** 1 (Python Basics)  
**Theme:** Function Basics, Arguments, Returns  
**Duration:** 1.5 hours

---

# 🎯 Learning Objectives
Today you will learn:

- What functions are and why they are used  
- How to define and call functions  
- How arguments & parameters work  
- Default values in functions  
- How return values work  
- The difference between *returning* and *printing*  
- How to write reusable code blocks  

---

# 📚 Required Reading

## 📘 From *Python Crash Course (PCC)*  
- **Chapter 8 — Functions**
  - Defining a function  
  - Passing information to a function  
  - Return values  
  - Using functions with lists  
  - Default values  
  - Keyword arguments  

---

## 📗 From *Automate the Boring Stuff (ATBS)*  
- **Chapter 3 — Functions**
  - def statements  
  - parameters  
  - return keyword  
  - local vs global scope  
  - None value  

---

# 🧠 Key Concepts (With Examples)

---

## 🔹 1. Defining a Function

```python
def greet():
    print("Hello!")
```

Calling it:
```python
greet()
```

---

## 🔹 2. Parameters & Arguments

```python
def greet(name):
    print("Hello,", name)

greet("Shashank")
```

---

## 🔹 3. Return Values

```python
def add(a, b):
    return a + b

result = add(5, 10)
print(result)
```

⚠ *Return ≠ Print*  
Return sends data BACK to the caller.

---

## 🔹 4. Default Arguments

```python
def welcome(name="Guest"):
    print("Welcome,", name)

welcome()           # Welcome, Guest
welcome("Ravi")     # Welcome, Ravi
```

---

## 🔹 5. Keyword Arguments

```python
def display_info(name, age):
    print("Name:", name)
    print("Age:", age)

display_info(age=25, name="Shashank")
```

---

## 🔹 6. Functions Returning Multiple Values

```python
def math_ops(a, b):
    return a + b, a - b, a * b

add, sub, mul = math_ops(5, 3)
```

---

## 🔹 7. Scope (Local & Global Variables)

```python
x = 10  # global

def func():
    x = 5  # local
    print(x)   # prints 5
```

---

# 📝 My Notes (Fill This Section)

## 🔹 What I Learned Today
-  
-  
-  

## 🔹 Concepts I Found Interesting
-  

## 🔹 Mistakes / Confusions I Had
-  

## 🔹 Summary in My Own Words
Write 3–5 sentences describing:
- what functions are  
- how return values work  
- why functions make code reusable  

---

# 💻 Practice Exercises (Mandatory)

Write **8 functions**:

### 1️⃣ Function to add 2 numbers  
### 2️⃣ Function to check even or odd  
### 3️⃣ Function to return factorial  
### 4️⃣ Function to reverse a string  
### 5️⃣ Function to count vowels  
### 6️⃣ Function to find max of a list  
### 7️⃣ Function to convert Celsius → Fahrenheit  
### 8️⃣ Function to check if a string is palindrome  

---

# 🧩 Extra Practice (Optional)

### ✔ Function to remove duplicates from a list  
### ✔ Function to return sum of numbers 1–N  
### ✔ Function to return only even numbers from a list  

---

# 🧪 Mini Quiz (Self-Test)

1. What is the difference between *argument* and *parameter*?  
2. What does the `return` keyword do?  
3. What is a default argument?  
4. Write a function that returns the square of a number.  
5. What is the difference between `print()` and `return`?  

---

# 🗂 Sample Code Snippets

### Adding numbers
```python
def add(a, b):
    return a + b
```

### Checking palindrome
```python
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]
```

---

# ✅ End-of-Day Checklist

✔ Read PCC Chapter 8  
✔ Read ATBS Chapter 3  
✔ Understood functions & return values  
✔ Completed 8 practice functions  
✔ Wrote notes  
✔ Uploaded Day 3 folder to GitHub  
✔ Ready for Day 4 (Lists & Dictionaries)  

---

# 🚀 Tomorrow (Day 4 — Lists & Dictionaries)
- List methods  
- Dictionary operations  
- List/dict comprehensions  
- Sorting, slicing, transformations

