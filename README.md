# Conversational GitHub Chatbot

Welcome to the Conversational GitHub Chatbot project! This project is designed to create an interactive chatbot that can answer questions related to GitHub documentation using Langchain models.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Acknowledgements](#acknowledgements)

## Introduction

This project leverages Langchain models and Streamlit to create a chatbot that provides insights into GitHub project documentation. The bot is built using Langchain's conversational retrieval capabilities and integrates OpenAI's embeddings for document processing.

## Features

- Interactive conversational chatbot interface using Streamlit.
- Uses Langchain ConversationalRetrievalChain for robust question answering.
- Efficient storage and retrieval of document embeddings with FAISS.
- Session management for maintaining the chat history.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.7 or later
- Git (for cloning the repository)
- Access to OpenAI's API (you will need an API key)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/conversational-github-chatbot.git
   cd conversational-github-chatbot
   
## File Structure:
.
├── app.py                # Main application code
├── load_docs.py          # Document loading and embedding logic
├── requirements.txt      # List of Python dependencies
├── .env                  # Environment variables for storing API keys
└── docs/                 # Directory containing markdown documents to be processed

## Acknowledgements
 - This project utilizes the Langchain library for leveraging advanced linguistic models.
 - The chatbot interface is developed using Streamlit, which provides an easy-to-use platform for deploying apps.
 - FAISS is used for efficient storage and retrieval of document embeddings.
 - Feel free to contribute and enhance the Conversational GitHub Chatbot! If you encounter any issues or have suggestions for improvements, please reach out or open an issue in the repository.

