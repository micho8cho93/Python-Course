import streamlit as st

# Predefined list of student names
students = [
    "Alice", "Ben", "Chloe", "David", "Ella",
    "Finn", "Grace", "Henry", "Isla", "Jack",
    "Kylie", "Liam", "Mia", "Noah", "Olivia"
]

st.title("Class Attendance")

# Create checkboxes for each student to mark if they're PRESENT
st.write("### Mark Attendance (Check = Present, Unchecked = Absent)")
attendance = {}

# Display checkboxes
for student in students:
    attendance[student] = st.checkbox(student, value=True)

# Submit button
if st.button("Submit Attendance"):
    present = [name for name, is_present in attendance.items() if is_present]
    absent = [name for name, is_present in attendance.items() if not is_present]

    st.success("✅ Attendance Recorded!")

    st.write("### Summary")
    st.write(f"**Present:** {len(present)}")
    st.write(f"**Absent:** {len(absent)}")

    st.write("#### Present Students")
    st.write(present if present else "None")

    st.write("#### Absent Students")
    st.write(absent if absent else "None")
