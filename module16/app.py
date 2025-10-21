import streamlit as st

def main():
    st.title("Hello World")
    age = st.number_input("enter your age", min_value=0, max_value=100)
    st.write("Your age is:", {age})
    user_input1 = st.text_input("Enter text", "Sample Text")
    st.write("You entered:", user_input1)
    if st.button("Click Me"):
         st.write("Button Pressed")
    if st.checkbox("Check me"):
        st.write("You're seeing this message beacuse you checked this checkbox")
if  __name__ == "__main__":
    main()