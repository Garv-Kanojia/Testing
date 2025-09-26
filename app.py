import streamlit as st
from codee2 import Prompts

st.title("Wellness Companion")

if "history" not in st.session_state:
    st.session_state["history"] = []

user_prompt = st.text_area("Enter your health goal:", "")

col1, col2 = st.columns([1, 1])
generate_clicked = col1.button("Generate Plan")
clear_clicked = col2.button("Erase History & Clear Screen")

if generate_clicked:
    if user_prompt.strip():
        agent = Prompts(user_prompt)
        result = agent.response()
        print("Plan created")
        if "error" in result:
            st.error(result["error"])
        else:
            st.session_state["history"].append(result)
    else:
        st.warning("Please enter your goal.")

if clear_clicked:
    st.session_state["history"] = []
    st.experimental_rerun()

for result in st.session_state["history"]:
    st.subheader("Nutrition Plan")
    st.markdown(result.get("NutritionPlan", result.get("NutritionAgent", "")))
    st.subheader("Fitness Plan")
    st.markdown(result.get("FitnessPlan", result.get("FitnessAgent", "")))