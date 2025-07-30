# 🐍 Python Learning Journey: Zero To Mastery Exercises 🐍

This repository documents my progress and solutions to exercises from the
Zero To Mastery (ZTM) Python programming course. It serves as a practical
portfolio of fundamental Python concepts, scripting techniques, and web
development basics.

---

## 📁 Repository Structure

The exercises are organized into directories corresponding to different topics or phases of the course:

* `fondation/`: Contains fundamental Python concepts and exercises.
* `scrapingData/`: Focuses on web scraping projects.
* `scripting/`: Includes general Python scripting exercises, often related to system interaction or utilities.
* `my_env/` and `__pycache__/`: Virtual environment and Python's compiled bytecode cache (ignored by Git).

---

## ✨ Highlighted Projects & Concepts

Here's a brief overview of some of the key projects and concepts demonstrated in this repository:

### 1. **Core Python Fundamentals (`fondation/`)**

This directory contains exercises designed to solidify understanding of Python's basic building blocks.

* **`gessingGame.py`**: A simple interactive guessing game, demonstrating basic input/output, loops (`while`), and conditional statements (`if/else`).
* **`list_comp.py`**: Explores the use of list comprehensions, a concise and efficient way to create lists in Python.
* **`decorator.py`**: Illustrates the concept of Python decorators, powerful tools for modifying functions without changing their source code.
* **`ft_lamba.py`**: Demonstrates the use of `lambda` functions (anonymous functions) and higher-order functions (like `map`, `filter`).

### 2. **Web Scraping (`scrapingData/`)**

This section dives into extracting data from websites.

* **`scrap.py`**: A web scraping script designed to extract information (titles, links, points) from a popular news aggregator website (e.g., Hacker News). It demonstrates:
    * Making HTTP requests (`requests`).
    * Parsing HTML content (`BeautifulSoup4`).
    * Handling website-specific pagination (navigating through multiple pages of results).
    * Extracting specific data elements.

### 3. **Python Scripting Utilities (`scripting/`)**

This directory contains utility scripts that showcase practical Python applications.

* **`password_check.py`**: A security utility that checks if a given password has been exposed in known data breaches (using the Have I Been Pwned API). It features:
    * Secure password input (`getpass`).
    * Hashing passwords (`hashlib`).
    * Interacting with external APIs (`requests`).
    * Parsing API responses.
    * Basic output formatting with colors.

### 4. **Web Development with Flask (`web-dev/`)**

This directory contains a web application built using the Flask microframework. It focuses on creating dynamic web pages and handling user input.

* **`server.py`**: The core Flask application file, defining routes, handling HTTP requests (GET/POST), and serving dynamic content.
* **`templates/`**: Houses Jinja2 HTML templates for rendering web pages, including a main page, portfolio details, service details, and a "thank you" page for form submissions.
* **`static/`**: Contains static assets like CSS stylesheets, JavaScript files for client-side interactivity, and images.
* **Form Handling**: Implements a contact form, demonstrating:
    * Processing form submissions (POST requests).
    * Accessing and validating user-submitted data.
    * Rendering different pages based on form success (e.g., a "thank you" message).
* **Database Integration (in progress)**: Explores connecting the Flask application to a database (MariaDB using Flask-SQLAlchemy) for persistent data storage, including defining models and interacting with the database from within Flask routes.

---

## 🛠️ Technologies Used

* Python 3.x
* `Flask` (for web application development)
* `Flask-SQLAlchemy` (for ORM with databases)
* `PyMySQL` (database connector for MariaDB/MySQL)
* `requests` library (for HTTP requests in scraping/API interaction)
* `BeautifulSoup4` (for HTML parsing in scraping)
* `hashlib` (for hashing)
* `getpass` (for secure input)
* `smtplib` (for email sending - if applicable)
* `PyPDF2` (for PDF manipulation - if applicable)
* **HTML5, CSS3, JavaScript** (for front-end development)

---
## 💡 Lessons Learned

This course and these exercises have been instrumental in deepening my understanding of Python's core features, object-oriented programming, file handling, API interactions, and best practices for writing robust and organized Python code.

Furthermore, the `web-dev` project has provided practical experience in:
* Building dynamic web applications with Flask.
* Handling web forms and user input securely.
* Structuring Flask projects with templates and static files.
* Connecting Flask applications to relational databases (MariaDB) using an ORM like SQLAlchemy for persistent data management.
* The interplay between front-end (HTML, CSS, JS) and back-end (Flask, Python) in a web application.
---
