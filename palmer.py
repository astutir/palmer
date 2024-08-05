import streamlit as st

home = st.Page(
    page="Home\Dataset_Overview.py",
    title="Home",
    icon=":material/dashboard:", default=True)
data = st.Page(
    page="Projects\Data_Info.py", title="Data Info", icon=":material/bug_report:")
prediction = st.Page(r"Projects\Prediction.py", title="Prediction", icon=":material/notification_important:")

pg = st.navigation({
    "Home": [home],
    "Projects": [data, prediction],
})

pg.run()