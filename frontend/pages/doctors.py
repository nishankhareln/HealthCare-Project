import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000/doctors/"

st.header("👨‍⚕️ Find a Doctor")

search_term = st.text_input("Search by Specialty or Language")

if st.button("Search") or search_term == "":
    params = {"specialty": search_term} if search_term else {}
    try:
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            doctors = response.json()
            if doctors:
                df = pd.DataFrame(doctors)
                st.dataframe(
                    df[["name", "specialization", "languages", "is_available"]],
                    use_container_width=True
                )
            else:
                st.info("No doctors found matching your criteria.")
        else:
            st.error("Failed to fetch doctor list.")
    except Exception as e:
        st.error(f"Error: {e}")