#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Import Libraries
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import spacy
import spacy.cli
import subprocess



#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Download and Load a pre-trained model
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Global variable for the NLP model

try:
    nlp = spacy.load("en_core_web_md")
except OSError:
    subprocess.run(["sh", "setup.sh"])
    spacy.util.fix_globally_installed_model("en_core_web_md")
    nlp = spacy.load("en_core_web_md")
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

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
