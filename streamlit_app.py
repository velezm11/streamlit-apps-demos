import streamlit as st

st.set_page_config(
    page_title="Energy Advisor",
    initial_sidebar_state="expanded"
)


if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


with col1:
    st.subheader("Chat")
    
    chat_history_container = st.container()
    
    with st.form("chat_form", clear_on_submit=True):
        input_text = st.text_area("Chat:", height=100, label_visibility="collapsed")
    
        send_button = st.form_submit_button("Send", type="primary")
    
    if send_button:
        st.session_state.chat_history.append({"role":"Me", "text":input_text})
        
        with st.spinner("Thinking..."):
            chat_response, prompt_text, prompt_summary_text = glib.get_chat_response_with_introspection(input_text=input_text)
        
        st.session_state.chat_history.append({"role":"Chatbot", "text":chat_response})

        with col2:
            st.subheader("Prompt with Memory")
            st.text_area("Prompt with Memory", value=prompt_text, height=500, label_visibility="collapsed")
            
        with col3:
            st.subheader("Summarization Prompt")
            st.text_area("Summarization Prompt", value=prompt_summary_text, height=500, label_visibility="collapsed")


with chat_history_container:
    
    for message in st.session_state.chat_history:
        text = message["text"]
        if message["role"] == "Me":
            st.warning(f"Me: {text}")
        else:
            st.info(f"Bot: {text}")
