import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from load_docs import load_and_embed_docs
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="GitHub Project Chatbot", layout="wide")
st.title("🧠 Conversational GitHub Chatbot")

@st.cache_resource(show_spinner="Embedding docs and loading model...")
def get_chain():
    vectorstore = load_and_embed_docs()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(temperature=0),
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return chain

qa_chain = get_chain()

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask something about the project:", key="input")

if user_input:
    result = qa_chain({"question": user_input, "chat_history": st.session_state.chat_history})
    answer = result["answer"]
    
    # Update chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", answer))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")
