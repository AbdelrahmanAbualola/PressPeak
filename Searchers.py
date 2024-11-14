#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Import Libraries
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import requests
import json
import pandas as pd

from API import Keys
from Parameters import Google_Parameters

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■



#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Searchers Functions
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
class Serper():
    #————————————————————————————————————————————————————————————————————————————————————————————————————
    # Function 1 : Queries Preperation
    #————————————————————————————————————————————————————————————————————————————————————————————————————
    def Queries(keywords_variable='', keywords_fixed='', keywords_excluded='', websites='', 
                   countries='', date_range=''):
        
        # Input Preparation: 
        START_DATE = ' after:' + date_range[0].strftime("%Y-%m-%d") if date_range else ' after:1900-01-01'
        END_DATE = ' before:' + date_range[1].strftime("%Y-%m-%d") if date_range else ' before:2050-12-31'
        
        EXCLUDED_KEYWORDS = ' '.join([' -' + word for word in keywords_excluded]) if keywords_excluded else ''
        
        # Prepare countries synonyms subqueries
        COUNTRIES_SYNONYMS = []
        try:
            for country in countries:
                country_synonyms = Google_Parameters.countries_acronyms()[country.title()]
                country_acronyms_subquery = '(' + ' OR '.join(['"' + word + '"' for word in country_synonyms]) + ')' if isinstance(country_synonyms, list) else '("' + country_synonyms + '")'
                COUNTRIES_SYNONYMS.append(country_acronyms_subquery)
        except:
            pass

        # Prepare fixed keywords
        try:
            FIXED_KEYWORDS = []
            for keyword_list in keywords_fixed:
                if isinstance(keyword_list, list):
                    fixed_keywords = "(" + ' OR '.join(['"' + word + '"' for word in keyword_list]) + ")"
                else:
                    fixed_keywords = "(" + ' OR '.join(['"' + word + '"' for word in keywords_fixed]) + ")"
                    FIXED_KEYWORDS.append(fixed_keywords)
                    break
                FIXED_KEYWORDS.append(fixed_keywords)

            FIXED_KEYWORDS = " AND ".join(FIXED_KEYWORDS)
        except:
            pass

        # Prepare websites filter
        WEBSITES_FILTER = ' OR '.join(['site:' + site for site in websites]) if websites else ''

        #-----------------------
        # Generate Queries:
        QUERIES = []

        # Handle case where there are no countries
        if not COUNTRIES_SYNONYMS:
            COUNTRIES_SYNONYMS = ['']  # Placeholder to allow for keyword combinations without countries

        for country in COUNTRIES_SYNONYMS:
            for keyword in keywords_variable:
                # Individual keyword queries
                query = f'("{keyword}")'
                if country:
                    query += f' AND {country}'
                if FIXED_KEYWORDS:
                    query += f' AND {FIXED_KEYWORDS}'
                if EXCLUDED_KEYWORDS:
                    query += f' {EXCLUDED_KEYWORDS}'
                query += f'{START_DATE}{END_DATE}'
                if WEBSITES_FILTER:
                    query += f' {WEBSITES_FILTER}'
                if query not in QUERIES:
                    QUERIES.append(query) 

            # Combined variable keywords query
            if keywords_variable:
                combined_keywords = ' OR '.join([f'"{keyword}"' for keyword in keywords_variable])
                query = f'({combined_keywords})'
                if country:
                    query += f' AND {country}'
                if FIXED_KEYWORDS:
                    query += f' AND {FIXED_KEYWORDS}'
                if EXCLUDED_KEYWORDS:
                    query += f' {EXCLUDED_KEYWORDS}'
                query += f'{START_DATE}{END_DATE}'
                if WEBSITES_FILTER:
                    query += f' {WEBSITES_FILTER}'
                if query not in QUERIES:
                    QUERIES.append(query) 

        return QUERIES
    #————————————————————————————————————————————————————————————————————————————————————————————————————
    
    
    
    #————————————————————————————————————————————————————————————————————————————————————————————————————
    # Function 2 : Payload Preperation
    #————————————————————————————————————————————————————————————————————————————————————————————————————
    def Payloads(queries,location='Egypt',geolocation='Egypt',language='English',quantity=10):
        GEOLOCATION = Google_Parameters.geolocation()[geolocation]
        LANGUAGE = Google_Parameters.languages()[language]
        PAYLOADS = []
        for query in queries:
            load = ({
                            "q": query,
                            'location':location,
                            "gl": GEOLOCATION,
                            "hl": LANGUAGE,
                            "num": quantity,
                            "autocorrect": True
            })
            PAYLOADS.append(load)
                    
        return PAYLOADS
    #————————————————————————————————————————————————————————————————————————————————————————————————————

    
    
    #————————————————————————————————————————————————————————————————————————————————————————————————————
    # Function 3 : Search Results
    #————————————————————————————————————————————————————————————————————————————————————————————————————
    # Step 2 use converted queries to get reuslts
    def Results(payloads):  
        # Get list of API keys
        api_keys = Keys.Serper()
        api_key_index = 0
        api_status = None
        RESULTS = None  # Initialize results
        
        # Set Serper search URL
        url = "https://google.serper.dev/news"
        
        # Try each API key with the actual payload until a working key is found
        while api_key_index < len(api_keys):
            api_key = api_keys[api_key_index]
            headers = {'X-API-KEY': f'{api_key}', 'Content-Type': 'application/json'}
            
            # Attempt to send actual payload
            response = requests.post(url, headers=headers, data=json.dumps(payloads))
            api_status = response.status_code
            
            # If the response is successful, process and return results
            if api_status == 200:
                RESULTS = []
                for batch in response.json(): 
                    RESULTS.extend(batch['news'])
                break  # Exit loop since a valid response was obtained
            
            # Move to the next API key if the current one fails
            api_key_index += 1

        # Return the results if successful, or an empty list if all keys failed
            print(RESULTS)
        return RESULTS if RESULTS is not None else []
    #————————————————————————————————————————————————————————————————————————————————————————————————————
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■