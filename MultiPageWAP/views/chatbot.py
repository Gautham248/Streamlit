# import streamlit as st

# st.title("Echo Bot")

# # with st.chat_message(name="assistant",avatar="😁"):
# #     st.write("Hello 👋")



# # step 1: create session memory to store the chat history of the application
# if "messages" not in st.session_state:
#     st.session_state.messages=[]

# # Display the chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Reacting to user input
# if propmt := st.chat_input("What is up?"):
#     # Assigning the input to prompt and checking that it isnt null in a single line ( := )
#     # Display the message in the chat message container
#     with st.chat_message("user"):
#         st.markdown(propmt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role":"user","content":propmt})

#     response= f"Echo : {propmt}"
#     # Display assistant response in chat message container
#     with st.chat_message("assistant",avatar="😁"):
#         st.markdown(response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role":"assistant","content":response})


import streamlit as st
import openai


st.title("ChatGPT - like Clone")
openai.api_key=st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"]="gpt-3.5-turbo"

# step 1: create session storage

if "messages" not in st.session_state:
    st.session_state.messages=[]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input

# if prompt := st.chat_input("What is up ?"):
#     with st.chat_message("user"):
#         st.markdown(prompt)
    
#     st.session_state.messages.append({"role":"user","content":prompt})

#     with st.chat_message("assistant"):
#         message_placeholder=st.empty()
#         full_response=""
#         for response in openai.Chat.create(
#             model=st.session_state["openai_model"],
#             messages=[
#                 {
#                     "role":m["role"],"content": m["content"]
#                 }
#                 for m in st.session_state.messages
#             ],
#             stream=True
#         ):
#             full_response+=response.choices[0].delta.get("content","")
#             message_placeholder.markdown(full_response+" ")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role":"assistant","content":full_response})




# Corrected GPT Connection Code  
if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    # Store the user's message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Updated API usage
        response = openai.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )

        full_response = response.choices[0].message.content
        message_placeholder.markdown(full_response)

    # Store the assistant's response
    st.session_state.messages.append({"role": "assistant", "content": full_response})
