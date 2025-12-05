import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000/doctors/"

st.header("👨‍⚕️ Find a Doctor")

search_term = st.text_input("Search by Department")

if st.button("Search") or search_term == "":
    params = {"specialty": search_term} if search_term else {}
    try:
        response = requests.get(API_URL, params=params)
        
        if response.status_code == 200:
            doctors = response.json()
            
            if doctors:
                df = pd.DataFrame(doctors)
                
                # 1. Define the columns we WANT to show
                desired_cols = ["name", "department", "hospital", "position", "profile_url"]
                
                # 2. Filter to keep only columns that ACTUALLY EXIST in the data
                # This prevents the "not in index" crash
                available_cols = [col for col in desired_cols if col in df.columns]
                
                # 3. Show the table
                st.dataframe(
                    df[available_cols],
                    use_container_width=True,
                    column_config={
                        "profile_url": st.column_config.LinkColumn("Profile")
                    }
                )
            else:
                st.info("No doctors found.")
        else:
            st.error("Failed to fetch doctor list.")
            
    except Exception as e:
        st.error(f"Error: {e}")