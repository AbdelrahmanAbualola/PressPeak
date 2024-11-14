#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Import Libraries
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import spacy
import os
import subprocess
import sys


#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Download and Load a pre-trained model
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# Check if the model is already installed
try:
    nlp = spacy.load("en_core_web_md")
except OSError:
    spacy.cli.download("en_core_web_md")
    nlp = spacy.load("en_core_web_md")
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
# Define a custom directory for downloading the model
custom_model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')

# Check if the custom model directory exists, and create it if not
if not os.path.exists(custom_model_dir):
    os.makedirs(custom_model_dir)

# Set the environment variable to install spaCy models in the custom directory
os.environ["SPACY_DATA"] = custom_model_dir

try:
    # Use subprocess to download the model using pip (this can be removed if the model is already installed)
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_md", "--target", custom_model_dir])

    # Verify that the model directory exists and contains the necessary files
    model_path = os.path.join(custom_model_dir, 'en_core_web_md')
    if os.path.exists(model_path):
        # Load the model from the custom directory
        nlp = spacy.load(model_path)
        print("Model loaded successfully!")
    else:
        print(f"Model not found in {model_path}. Please check the installation.")

except subprocess.CalledProcessError as e:
    print(f"Error during subprocess execution: {e}")
    print(f"Return code: {e.returncode}")
    print(f"Command: {e.cmd}")
except Exception as e:
    print(f"Error loading model: {e}")


#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Function (1) Relevancy SCore
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def relevancy_score(description, keywords):
    # Combine keywords into a single string
    keyword_str = " ".join(keywords)
    # Process both description and keywords
    doc1 = nlp(description)
    doc2 = nlp(keyword_str)
    # Calculate similarity score
    return doc1.similarity(doc2)
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————



#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Function (2) Extract Keywords
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def extract_keywords(description, keywords_list):
    doc = nlp(description)
    keyword_scores = {}

    # Calculate the similarity of each keyword in the list to the description
    for keyword in keywords_list:
        # Create a spaCy doc for the keyword
        keyword_doc = nlp(keyword)
        
        # Calculate similarity of keyword to description
        similarity = doc.similarity(keyword_doc)
        
        # Store the keyword and its similarity score
        keyword_scores[keyword] = similarity

    # Sort the keywords by similarity score in descending order and return the top 5
    top_keywords = sorted(keyword_scores, key=keyword_scores.get, reverse=True)[:5]
    
    return top_keywords
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————



#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Function (3) add_keywords_column
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def add_keywords_column(df, input_keywords):
    df["Relevant Keywords"] = df["Short Description"].apply(lambda x: extract_keywords(x, input_keywords))
    return df
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————



#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Function (4) add_relevancy_score_column
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def add_relevancy_score_column(df, input_keywords):
    # Apply relevancy_score function to each row in the "Short Description" column
    df["Relevancy Score"] = df["Short Description"].apply(lambda x: relevancy_score(x, input_keywords))
    return df
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
