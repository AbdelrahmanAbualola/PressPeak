#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Import Libraries
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import spacy
import os
import shutil
from pathlib import Path


#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Download and Load a pre-trained model
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def get_spacy_model():
    model_name = "en_core_web_md"
    local_model_dir = Path("./models")  # Local directory to store the model
    model_path = local_model_dir / model_name

    # Check if the model exists locally
    if not model_path.exists():
        # Create the local directory if it doesn't exist
        local_model_dir.mkdir(parents=True, exist_ok=True)
        try:
            # Download the model into the local directory
            from spacy.cli import download
            download(model_name, dir=str(local_model_dir))
        except Exception as e:
            print(f"Error downloading {model_name}: {e}")
            raise

    # Load the model from the local directory
    try:
        return spacy.load(model_path)
    except Exception as e:
        print(f"Error loading {model_name} from {model_path}: {e}")
        raise

# Initialize the model
try:
    nlp = get_spacy_model()
except Exception as e:
    print(f"Failed to initialize Spacy model: {e}")



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
