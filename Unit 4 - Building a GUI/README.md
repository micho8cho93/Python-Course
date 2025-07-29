# 🖥️ Unit 4: Building a GUI with Streamlit

Welcome to **Unit 4**! In this unit, you'll learn how to build **Graphical User Interfaces (GUIs)** using a Python library called **Streamlit**. Instead of running code only in the terminal, you'll create interactive web apps that are easy to use and visually appealing.

---

## 🎯 Unit Objectives

By the end of this unit, you will:

- Understand how to use Streamlit to create simple browser-based apps.
- Learn how to use components like buttons, checkboxes, and text inputs.
- Build a fully functional **GUI version** of your Attendance Counter from Unit 2.

---

## 🗓️ Unit Breakdown

### 📘 Class 1: Introduction to Streamlit

- Learn what Streamlit is and why it’s useful.
- Explore basic commands: `st.title()`, `st.write()`, `st.text_input()`, `st.button()`.
- Create a simple greeting app that asks for your name and displays a message.

---

### 📘 Class 2: Handling User Input

- Practice using checkboxes, buttons, and `st.session_state`.
- Build a small form that takes in multiple names.
- Understand how to store and display dynamic data from user input.

---

### 📘 Class 3: Final Project – GUI Attendance Counter

- Use a **preloaded list of 15 students**.
- Add a **checkbox for each student** to mark attendance (checked = present).
- Use a **"Submit Attendance"** button to finalize and display results.
- Show:
  - Who is **present** and who is **absent**
  - Total count of present and absent students

---

## 🧪 Final Project Instructions

Build a GUI app with the following features:

### ✅ Requirements:

- A **fixed list of 15 student names**.
- A **checkbox** for each name to mark attendance.
- A **submit button** to finalize attendance.
- Display:
  - Names of present and absent students
  - A summary count

### 🔁 Sample Flow:

```plaintext
[ ] Alice
[✓] Ben
[✓] Chloe
...
[ Submit Attendance ]

=> ✅ Attendance Recorded!
=> Present: 12
=> Absent: 3
