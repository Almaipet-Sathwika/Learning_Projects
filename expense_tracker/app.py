import streamlit as st
from services import auth_service
from services import expense_service




st.title("Expense Tracker")

# Create login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""


menu = ["Login", "Create Account"]

choice = st.sidebar.selectbox("Menu", menu)


# CREATE ACCOUNT
if choice == "Create Account":

    st.subheader("Create Account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Create"):
        auth_service.create_user(username, password)
        st.success("Account Created")


# LOGIN
elif choice == "Login":

    if not st.session_state.logged_in:

        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if auth_service.authenticate(username, password):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Invalid credentials")

    else:

        username = st.session_state.username

        st.success(f"Welcome {username}")

        menu2 = [
            "Add Expense",
            "View Expenses",
            "Filter by Category",
            "Total Expense",
            "Logout"
        ]

        option = st.selectbox("Select Option", menu2)


        if option == "Add Expense":

            category = st.text_input("Category")
            amount = st.number_input("Amount")

            if st.button("Add Expense"):
                expense_service.add(username, category, amount)
                st.success("Expense Added")


        elif option == "View Expenses":

            data = expense_service.view(username)
            st.write(data)


        elif option == "Filter by Category":

            category = st.text_input("Category")

            if st.button("Fetch"):
                data = expense_service.fetch(username, category)
                st.write(data)


        elif option == "Total Expense":

            total = expense_service.total(username)
            st.write("Total Expense:", total)


        elif option == "Logout":

            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()
