import streamlit as st

st.set_page_config(
    page_title='Energy Advisor',
    initial_sidebar_state="expanded"
)



st.header("Energy Advisor")
st.sidebar.header("Sources")
...
st.sidebar.header("Full Disclosure")
...

expander = st.expander("Know about me")
expander.write(...)
