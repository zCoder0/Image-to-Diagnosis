import streamlit as st
def login_page():
    st.title("Login Page")
    
    # Login Form
    username = st.text_input("Username or Email ")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
   
    if login_button:
        
        try:
            if username == "admin" and password == "admin":
        # Replace with your authentication logic
        
                st.session_state.is_logged_in = True
                st.session_state.username = data[0][0]
                st.success("Logged in successfully! Redirecting to Home...")
                
                # Redirect to Home page
                st.session_state.current_page = "Home"
            
            else:
                st.error("Invalid username or password.")
        except Exception as e:
            st.error("An error occurred: " + str(e))
