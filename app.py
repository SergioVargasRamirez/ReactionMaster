import streamlit as st
from config.settings import APP_NAME
from ui.exercise import exercise_view
from core.chemicals import LATEX_FORMULAS
from core.reaction import Reaction, to_latex


st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title(APP_NAME)

exercise_view()

st.markdown("""
<div style='position:fixed; bottom:0; left:0; width:100%; padding:20px; font-size: 16px; text-align:center; color: gray;'>
ReaktionMaster by Sergio Vargas. &nbsp; 
This work is licensed under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
</div>
""", unsafe_allow_html=True)
