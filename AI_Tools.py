#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Import Libraries
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import spacy
from transformers import BertTokenizer, BertModel
import torch
import concurrent.futures

#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Load Spacy pre-trained model
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
try:
    nlp = spacy.load("en_core_web_md")
except:
    spacy.cli.download('en_core_web_md')
    nlp = spacy.load("en_core_web_md")
    
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Load MiniLM-L6-H384-uncased pre-trained model
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————    
tokenizer = BertTokenizer.from_pretrained('nreimers/MiniLM-L6-H384-uncased')
model = BertModel.from_pretrained('nreimers/MiniLM-L6-H384-uncased')
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————



#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Functions (1) Relevancy SCore
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def get_bert_embedding(text):
    """Converts a text to its BERT embedding."""
    # Tokenize input text
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    
    # Get BERT output (we'll take the last hidden state of the model)
    with torch.no_grad():
        outputs = model(**inputs)
    
    # We take the mean of the token embeddings from the last layer
    embeddings = outputs.last_hidden_state.mean(dim=1)
    
    return embeddings.squeeze()
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————



#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Function (4) add_relevancy_score_column
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def relevancy_score(description, keywords):
    """Calculate the relevancy score between description and keywords."""
    # Convert the keywords into a single string
    keyword_str = " ".join(keywords)
    
    # Get BERT embeddings for both description and keywords
    description_embedding = get_bert_embedding(description)
    keyword_embedding = get_bert_embedding(keyword_str)
    
    # Calculate cosine similarity between the embeddings
    cos_sim = torch.nn.functional.cosine_similarity(description_embedding, keyword_embedding, dim=0)
    
    return cos_sim.item()
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Functions () 
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def process_row(row, input_keywords):
    """Process a single row to calculate relevancy score."""
    description = row['Short Description']
    return relevancy_score(description, input_keywords)
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————



#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Functions () 
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def add_relevancy_score_column(df, input_keywords):
    """Add a relevancy score column to the dataframe using parallel processing."""
    
    # Use ThreadPoolExecutor for parallel processing
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # We use df.iterrows() but unpack properly to access 'Short Description'
        results = list(executor.map(lambda row: process_row(row[1], input_keywords), df.iterrows()))
    
    # Add the relevancy score as a new column in the dataframe
    df["Relevancy Score"] = results
    
    return df
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————



#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Functions (2) Extract Keywords
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
# Function () add_keywords_column
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
def add_keywords_column(df, input_keywords):
    df["Relevant Keywords"] = df["Short Description"].apply(lambda x: extract_keywords(x, input_keywords))
    return df
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
