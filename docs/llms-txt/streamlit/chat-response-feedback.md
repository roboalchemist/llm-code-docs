# Collect user feedback about LLM responses

A common task in a chat app is to collect user feedback about an LLM's responses. Streamlit includes `st.feedback` to conveniently collect user sentiment by displaying a group of selectable sentiment icons.

This tutorial uses Streamlit's chat commands and `st.feedback` to build a simple chat app that collects user feedback about each response.

## Initialize your app

1. In `your_repository`, create a file named `app.py`.
2. In a terminal, change directories to `your_repository`, and start your app:

   ```bash
   streamlit run app.py
   ```

   Your app will be blank because you still need to add code.

3. In `app.py`, write the following:

   ```python
   import streamlit as st
   import time

   def chat_stream(prompt):
       response = f'You said, \"{prompt}\" ...interesting.'
       for char in response:
           yield char
           time.sleep(0.02)

   def save_feedback(index):
       st.session_state.history[index]["feedback"] = st.session_state[f"feedback_{index}"]

   if "history" not in st.session_state:
       st.session_state.history = []

   for i, message in enumerate(st.session_state.history):
       with st.chat_message(message["role"]):
           st.write(message["content"])
           if message["role"] == "assistant":
               feedback = message.get("feedback", None)
               st.session_state[f"feedback_{i}"] = feedback
               st.feedback(
                   "thumbs",
                   key=f"feedback_{i}",
                   disabled=feedback is not None,
                   on_change=save_feedback,
                   args=[i],
               )
   st.session_state.history.append({"role": "assistant", "content": response})
   ```

4. Save your file and go to your browser to try your new app.

## Optional: Change the feedback behavior

Your app currently allows users to rate any response once. They can submit their rating at any time, but can't change it.

If you want users to rate only the _most recent_ response, you can remove the widgets from the chat history:

```python
for i, message in enumerate(st.session_state.history):
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if message["role"] == "assistant":
            feedback = message.get("feedback", None)
            st.session_state[f"feedback_{i}"] = feedback
            st.feedback(
                "thumbs",
                key=f"feedback_{i}",
                disabled=feedback is not None,
                on_change=save_feedback,
                args=[i],
            )
```

Or, if you want to allow users to change their responses, you can just remove the `disabled` parameter:

```python
for i, message in enumerate(st.session_state.history):
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if message["role"] == "assistant":
            feedback = message.get("feedback", None)
            st.session_state[f"feedback_{i}"] = feedback
            st.feedback(
                "thumbs",
                key=f"feedback_{i}",
                on_change=save_feedback,
                args=[i],
            )