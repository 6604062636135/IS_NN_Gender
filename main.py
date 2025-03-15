import streamlit as st
from components.navbar import navbar  # นำเข้า Navbar
from pages import home, doc1, doc2, ML, NN  # นำเข้าแต่ละหน้า

# เรียกใช้ Navbar
navbar()

# อ่านค่าพารามิเตอร์จาก URL
query_params = st.query_params
page = query_params.get("page", "Home")  # Default to "Home"

# แสดงหน้าที่เลือก
if page == "Home":
    home.app()
elif page == "Doc1":
    doc1.app()
elif page == "Doc2":
    doc2.app()
elif page == "ML":
    ML.app()
elif page == "NN":
    NN.app()

