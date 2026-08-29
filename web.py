import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()

def add_todo():
    todo = (st.session_state['new_todo'] + '\n').strip()
    todos.append(todo)
    write_todos(todos)
    st.session_state['new_todo'] = ''

st.title("My TODO App")
st.subheader("This is my TODO app")
st.write("This app is to increase your productivity")

for index, item in enumerate(todos):
    checkbox_state = st.checkbox(item, key=item)

    if checkbox_state:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label="", placeholder="Type a text",
              on_change=add_todo, key="new_todo")

print(todos)
print("hello")
st.session_state