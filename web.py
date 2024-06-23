import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("Hey! You probably came from my Portfolio.")
st.subheader("Thanks for stopping by (please hire me!)")

st.write("So write something here and click it to delete it. You can also refresh and it will still be here. ")
st.text_input(label="Express thyself:", placeholder="Just do it!",
              on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


