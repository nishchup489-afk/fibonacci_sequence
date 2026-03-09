# Fibonacci Sequence Generator

**Live Preview**
[https://fibonacci-sequence.onrender.com](https://fibonacci-sequence.onrender.com)

**GitHub Repository**
[https://github.com/nishchup489-afk/fibonacci_sequence](https://github.com/nishchup489-afk/fibonacci_sequence)

**Project #3 of 100 Python Live Projects**

---

## Overview

This project generates the **Fibonacci Sequence up to the Nth term** using Python.

What started as a simple algorithm exercise evolved into a **FastAPI web application** with a clean UI and dynamic rendering. The goal of this project is to demonstrate both **algorithmic implementation** and **web integration** using a modern Python stack.

---

## Project Versions

### CLI Version

The CLI implementation focuses purely on the **core algorithm**.

It generates Fibonacci numbers iteratively, which avoids recursion overhead and prevents stack overflow for larger inputs.

Run:

```
python sample.py
```

---

### Web Version

The web version allows users to enter the number of terms through a browser.

The request is handled by **FastAPI**, the sequence is generated on the backend, and the result is rendered dynamically using **Jinja2 templates**.

---

## Tech Stack

* Python 3.14
* FastAPI
* Jinja2
* Tailwind CSS
* Poetry
* Render

---

## Installation

Clone the repository:

```
git clone https://github.com/nishchup489-afk/fibonacci_sequence.git
cd fibonacci_sequence
```

Install dependencies with Poetry:

```
poetry install
```

Activate the environment:

```
poetry shell
```

Run the application:

```
uvicorn src.fibonacci.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## Mathematical Background

The Fibonacci sequence is defined as a series where each number is the sum of the two preceding numbers.

Sequence:

```
0, 1, 1, 2, 3, 5, 8, 13...
```

### Recurrence Relation

```
F(n) = F(n-1) + F(n-2)
```

With base values:

```
F(0) = 0
F(1) = 1
```

---

## Implementation Logic

This project uses an **iterative approach**.

Steps:

1. Accept input `n` from the user
2. Start with two variables `a = 0` and `b = 1`
3. Iterate `n` times
4. Append the current value
5. Update values using:

```
a, b = b, a + b
```

Time Complexity:

```
O(n)
```

---

## UI Design

The web interface follows a minimal modern style.

Features:

* Dark mode UI
* Glassmorphism card layout
* Responsive design
* Tailwind CSS styling

---

## Example

Input:

```
10
```

Output:

```
0 1 1 2 3 5 8 13 21 34
```

---

## Deployment

The application is deployed on **Render**.

Render provides:

* automatic builds
* HTTPS
* GitHub integration

---

## Project Series

This project is part of **100 Python Projects**, a series focused on building real-world Python applications covering algorithms, backend systems, and deployment.

---

## Author

Nishchup
[https://github.com/nishchup489-afk](https://github.com/nishchup489-afk)
