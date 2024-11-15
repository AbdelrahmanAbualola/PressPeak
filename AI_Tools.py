#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Import Libraries
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import spacy
import os
from pathlib import Path



#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Download and Load a pre-trained model
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Global variable for the NLP model
nlp = None

# Initialization function to download and load the model
def initialize_nlp_model():
    global nlp
    model_name = "en_core_web_md"

    try:
        # Try to load the model
        nlp = spacy.load(model_name)
    except OSError:
        try:
            # Download the model using SpaCy's CLI
            from spacy.cli import download
            download(model_name)
            nlp = spacy.load(model_name)  # Load the model after downloading
        except Exception as e:
            print(f"Error downloading or loading {model_name}: {e}")
            raise

# Call the initialization function during module import
initialize_nlp_model()





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
