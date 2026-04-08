import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Student Result Analysis Dashboard")

file = st.file_uploader("Upload your student results CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader(" Dataset Preview")
    st.write(df)

    st.subheader("Average Marks")
    df["Average"] = df.iloc[:, 1:].mean(axis=1)
    st.write(df[["Name", "Average"]])

    st.subheader(" Topper")
    topper = df.iloc[df["Average"].idxmax()]
    st.success(f"{topper['Name']} with {topper['Average']:.2f} marks")

    st.subheader(" Marks Visualization")
    fig, ax = plt.subplots()
    df.set_index("Name").plot(kind="bar", ax=ax)
    st.pyplot(fig)

st.markdown("---")
st.subheader(" Enter Student Marks")

name = st.text_input("Enter Student Name")

sub1 = st.number_input("English", min_value=0, max_value=100, step=1)
sub2 = st.number_input("Java", min_value=0, max_value=100, step=1)
sub3 = st.number_input("Computers", min_value=0, max_value=100, step=1)
sub4 = st.number_input("Python", min_value=0, max_value=100, step=1)
sub5 = st.number_input("DBMS", min_value=0, max_value=100, step=1)

# ---------------- BUTTON ----------------
if st.button("✅ Calculate Result"):
    if name == "":
        st.warning("Please enter student name")
    else:
        marks = [sub1, sub2, sub3, sub4, sub5]

        total = sum(marks)
        percentage = total / len(marks)

        # -------- RESULT --------
        st.subheader("📋 Result Summary")
        st.write(f"👤 Name: {name}")
        st.write(f"🧮 Total Marks: {total}")
        st.write(f"📊 Percentage: {percentage:.2f}%")

        if percentage >= 65:
            st.success("✅ Status: Passed")
        else:
            st.error("❌ Status: Failed")

        # -------- VISUALIZATION (NOW INSIDE BUTTON) --------
        st.subheader("📊 Marks Visualization")

        subjects = ["English", "Java", "Computers", "Python", "DBMS"]

        fig, ax = plt.subplots()
        ax.bar(subjects, marks)

        ax.set_title(f"{name}'s Marks Distribution")
        ax.set_xlabel("Subjects")
        ax.set_ylabel("Marks")

        plt.xticks(rotation=30)

        st.pyplot(fig)