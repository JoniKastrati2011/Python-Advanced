import streamlit as st
import requests
import pandas as pd

st.title("Project Management App")
dev_name = st.text_input("Enter Developer Name")
dev_experience = st.text_input("Enter Developer Experience")

if st.button("Create Project"):
    dev_data = {"name": dev_name, "experience": dev_experience}
    response = requests.post("http://localhost:8000/project", json=dev_data)
    st.json(response.json())

st.header("Create Project Details")
proj_title = st.text_input("Project Management App")
proj_desc = st.text_input("Project Description")
proj_lang = st.text_input("Languages Used(comma-separated)")
lead_dev_name = st.text_input("Lead Developer Name")
lead_dev_exp = st.number_input("Lead Developer Experience(Years)", main_value=0, max_value=50, value=0)

if st.button("Create Project"):
    lead_dev_data = {"name": lead_dev_name, "experience": lead_dev_exp}
    proj_data = {
        "title": proj_title,
        "description": proj_desc,
        "languages": proj_lang.split(","),
        "lead_developer": lead_dev_data
    }

    response = requests.post("http://localhost:8000/project", json=proj_data)
    st.json(response.json())


#Display Projects in a Dashboard Format
st.header("Project Dashboard")

if st.button("Get Projects"):
    response = requests.get("http://localhost:8000/project")
    project_data = response.json()["projects"]

    if project_data:
        projects_df = pd.DataFrame(project_data)

        st.subheader("Projects Overview")
        st.dataframe(projects_df)

        st.subheader("Project Details")
        for projects in project_data:
            st.markdown(f"### {projects['title']}")
            st.markdown(f"**Description: ** {projects['description']}")
            st.markdown(f"**Languages Used: ** {', '.join(projects['languages']) }")
            st.markdown(f"**Lead Developer: ** {projects['lead_developer']['name']} with {projects['lead_developer']
            ['experience']}")
            st.markdown("---")
    else:
        st.warning ("No Projects Found.")


