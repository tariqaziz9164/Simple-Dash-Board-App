import sqlite3
import streamlit as st

def create_database():
    
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='customers'
    """)
    if not c.fetchone():
        c.execute('''CREATE TABLE customers
                     (name text, address text, phone text)''')
        conn.commit()
    conn.close()

def add_customer(name, address, phone):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (name, address, phone))
    conn.commit()
    conn.close()

def delete_customer(name):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE name=?", (name,))
    conn.commit()
    conn.close()

def update_customer(name, address, phone):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("UPDATE customers SET address = ?, phone = ? WHERE name = ?", (address, phone, name))
    conn.commit()
    conn.close()

def view_customers():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    customers = c.fetchall()
    conn.close()
    return customers

def search_customer(name, phone):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE name=? OR phone=?", (name, phone))
    customers = c.fetchall()
    conn.close()
    return customers


def main():
    st.title("Customer Database App")
    
    
    create_database()

    name = st.text_input("Name")
    address = st.text_input("Address")
    phone = st.text_input("Phone Number")
    st.sidebar.header("Click for operations")
    if st.sidebar.button("Add"):
        add_customer(name, address, phone)

    if st.sidebar.button("Delete"):
        delete_customer(name)

    if st.sidebar.button("Update"):
        update_customer(name, address, phone)


    if st.sidebar.button("Search"):
        customers = search_customer(name, phone)
        st.header("Customers File")
        st.table(customers)   

    if st.sidebar.button("View"):
        customers = view_customers()
        st.header("Customers File")
        st.table(customers)

if __name__ == '__main__':
    main()