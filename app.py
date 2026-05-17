import streamlit as st
st.set_page_config(page_title="My smart program")
if "page" not in st.session_state:
    st.session_state.page = "login"
if st.session_state.page == "login":
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("mon image.png", width=150) 
    with col2:
        st.title("My smart program")
        st.write("Hello, today we will learn how to program")

    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, step=1)

    if st.button("Enter"):
        if age < 8:
            st.error("Sorry, you are not allowed to enter this application.")
        else:
            st.session_state.user_name = name
            st.session_state.page = "menu"
            st.rerun()
elif st.session_state.page == "menu":
    st.title("Hello {st.session_state.user_name}!")
    st.subheader("Choose a level to start:")
    
    choice = st.radio("What do you want to learn?", 
                      ["1: Scratch", "2: MIT App Inventor", "3: Godot"])

    if st.button("Go to Lesson"):
        if "1" in choice:
            st.session_state.page = "Level 1"
        elif "2" in choice:
            st.session_state.page = "Level 2"
        elif "3" in choice:
            st.session_state.page = "Level 3"
elif st.session_state.page == "Level 1":
    st.title("Level 1: Scratch")
    st.write("Scratch is a software program used to make simple games using blocks.")
    st.video("https://www.youtube.com/watch?v=pdtMUgnmRa4")
    st.text("Now it's your turn: enter Scratch and make the sprite walk then turn left.")
    if st.button("Back to Menu"):
        st.session_state.page = "menu"
        st.rerun()
elif st.session_state.page == "Level 2":
    st.title("Level 2: MIT App Inventor")
    st.write("MIT App Inventor is a tool for Android programming. It is easy to use.")
    st.video("https://www.youtube.com/watch?v=yNdVSsW-2bo")
    st.text("Now write how to start a screen on MIT App Inventor.")
    if st.button("Back to Menu"):
        st.session_state.page = "menu"
        st.rerun()
elif st.session_state.page == "Level 3":
    st.title("Level 3: Godot")
    st.write("Godot is used to program games. This time you need to write your own code.")
    st.video("https://www.youtube.com/watch?v=LOhfqjmasi0")
    if st.button("Back to Menu"):
        st.session_state.page = "menu"
        st.rerun()
