import streamlit as st
import random
import os
from text_generator import create_ngram_model

# Directory containing text files
TEXT_FILES_DIR = 'data' 

def get_all_text_files():
    # Returns a list of all text files in the TEXT_FILES_DIR directory.
    return [f for f in os.listdir(TEXT_FILES_DIR) if f.endswith('.txt')]

def main():
    st.title('Streamlit N-Gram Text Generator')

    # Get all text files
    text_files = get_all_text_files()
    
    # set up sidebar
    st.sidebar.title('Settings')

    # Dropdown menu to select a file
    selected_file = st.sidebar.selectbox('Choose a text file:', text_files)
    N = st.sidebar.number_input('Choose the N-gram size', value=6)
    seed_int = st.sidebar.number_input('Choose a seed between 0 and 100', value=4)

    # Display the content of the selected file
    file_path = os.path.join(TEXT_FILES_DIR, selected_file)
    with open(file_path, 'r') as file:
        content = file.read()
        st.text_area('File Content', content, height=100)
        
    model = create_ngram_model(N, file_path)
    
    st.markdown("---")
    random.seed(seed_int)
    st.text_area("Generated Text:",model.generate_text(50), height=100)

if __name__ == '__main__':
    main()

