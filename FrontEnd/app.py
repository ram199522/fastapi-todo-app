import streamlit as st
import requests as req
from config import API_URL  # Import API_URL securely


API_URL = "http://127.0.0.1:8000"

#Adding title to the Application
st.title("TODO Application With FastAPI")


#sending post request functionality
st.header("Add new task")

new_task = st.text_input("Enter new task: ")
new_status = st.selectbox("Status Selection",["Pending","Completed"])


if st.button("Add Task"):
    # checking wheather user entered the task or not 
    if new_task:
       res = req.post(f"{API_URL}/tasks/",json={"task":new_task,"status":new_status})

       if res.status_code == 200:
            st.success("Task added successfully.")
       else:
           st.error("Failed to add task")
    else:
        st.warning("Please enter the task before clicking 'Add Task' button")

#getting a task by id functionality

st.header("Get a task by Id")

task_id = st.text_input("Enter task id: ")

if st.button("Get Task"):

    if task_id:
        res = req.get(f"{API_URL}/tasks/{task_id}")

        if res.status_code == 200:
            task_data = res.json()
            st.write(f"Task:        {task_data["task"]}")
            st.write(f"Task_status: {task_data["status"]}")
        else:
            st.error("Task not found or invalid task id")
    else:
        st.warning("Please enter task id")

#updating the task functionality

st.header("Update a task")#header for the update task

task_id = st.text_input("Enter task Id to update: ")#gettting task_id and storing it into varaiable(task_id)

new_task = st.text_input("Enter task(Optional):")
new_status = st.selectbox("Select new Status(Optional): ",["Keep Unchanged","Pending","Completed"])


if st.button("Update Task"):
    if not task_id:
        st.warning("Please enter task_id")
    else:
        data = {}

        if new_task:
            data["task"] = new_task

        if new_status != "Keep Unchanged":
            data["status"] = new_status

        if data:
            res = req.put(f"{API_URL}/tasks/{task_id}",json=data)

            if res.status_code == 200:
                st.success("Task updated successfully")
            else:
                st.error("Failed to update the task")
        else:
            st.warning("Please enter atleast one field to update")


#delete task functionality

st.header("Deleting a task")

task_id = st.text_input("Enter task Id to delete:")

if st.button("Delete task"):
    
    if task_id:
        res = req.delete(f"{API_URL}/tasks/{task_id}")
        
        if res.status_code == 200:
            st.success("task deleted successfully")
        else:
            st.error("task not found")
    else:
        st.warning("Please enter task id")

#getting all the tasks functionality

st.header("Get all the tasks")

if st.button("Get Tasks"):
    res = req.get(f"{API_URL}/tasks/")

    if res.status_code == 200:
        tasks = res.json()
        if tasks:
            st.markdown("---------")
            for task in tasks:
                st.write(f"Task_id:{task["id"]}")
                st.write(f"Task_name:{task["task"]}")
                st.write(f"Task_status:{task["status"]}")
                st.markdown("-------")
        else:
            st.warning("No tasks available")
