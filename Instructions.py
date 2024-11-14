import streamlit as st
#————————————————————————————————————————————————————————————————————————————————————————————————————
# Function 1: General_Instructions
#————————————————————————————————————————————————————————————————————————————————————————————————————
def Introduction():
#————————————————————————————————————————————————————————————————————————————————————————————————————
    Introduction =  '''
                    ##### **Overview:** 
                    Presspeak is a research tool that accelerates the news-gathering process. It’s tailored for business research analysts, helping them to conduct comprehensive Google News searches using multiple keywords, regions, timeframes, and sources.
                    
                    ##### **Core Purpose:** 
                    This app is designed to streamline tasks like creating newsletters or conducting detailed press searches, by automating query generation and extraction from Google News.
                    
                    ##### **Key Benefits:**
                    - Reduces the time needed for press research from hours to minutes.
                    - Increases comprehensiveness by covering multiple search parameters and queries in one go.
                    - Offers AI assistance to filter and rank the most relevant news articles, ensuring high-quality research results.

                  '''
    return Introduction
#————————————————————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————
# Function 2: Features
#————————————————————————————————————————————————————————————————————————————————————————————————————
def Features():
#————————————————————————————————————————————————————————————————————————————————————————————————————
    Features = '''
                ##### **Key Features**
                - **Automated Multi-Query Search:** Presspeak allows you to define search parameters and then automatically generates and executes numerous queries.
                - **Result Compilation and Export:** View all results in a structured table with options to edit and export data as an Excel file.
                - **Article Scraping:** Extract full article texts for selected results, displaying them alongside search data in a comprehensive table.
                - **AI-Powered Relevancy Analysis:** Analyze articles for relevance to original search criteria, with AI highlighting the most pertinent results.
                '''
    return Features
#————————————————————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————
# Function 3: How_it_works: Search Parameters
#————————————————————————————————————————————————————————————————————————————————————————————————————
def How_it_words_Step_1():
    How_it_words_Step_1 = '''
                    ### **Step 1: Enter Search Parameters**
                    To start your search, fill out the fields in the main input boxes. Each box has a specific purpose, helping you define exactly what you’re looking for in the news search.

                    --- 
                    ##### **1) Keywords:**
                    - **Any of Keywords:** Broad keywords related to your topic.
                    - **None of Keywords:** Words you don’t want to appear in the results.
                    - **All of Keywords:** Key phrases that must be included in each query to narrow down results.
                    
                    ---
                    ##### **2) Countries:**
                    Choose specific countries to include in the search (e.g., selecting "USA" will include variations like "United States" or "America").
                    
                    ---
                    ##### **3) Websites:**
                    List specific domains or websites where you want the news results to come from.
                   
                    ---
                    ##### **4) Filters:**
                    - **Geolocation:** Simulate the search from another location.
                    - **Location:** Focus results from a specific origin point.
                    - **Result Quality:** Adjust the number of results per query.
                    - **Search Language:** Select the language of the results you need.
                    '''
    return How_it_words_Step_1
#————————————————————————————————————————————————————————————————————————————————————————————————————



#————————————————————————————————————————————————————————————————————————————————————————————————————
# Function 3: How_it_works: Review Results
#————————————————————————————————————————————————————————————————————————————————————————————————————
def How_it_words_Step_2():
    How_it_words_Step_2 = '''
                    ### **Step 2: Review Results in the Tabs**
                    :this After entering your search criteria, press "Start Search" to initiate the query process. Presspeak will then generate multiple queries, retrieving and displaying the results in a structured, step-by-step format across three tabs.
                    
                    ---
                    ##### **Tab 1 – Google Results:**
                    a) **Purpose:** This tab shows the initial search results in a table, listing headlines, descriptions, dates, sources, and URLs.
                    
                    b) **Features:**
                    - **View and Edit:** Explore the results, make notes, or highlight key information.
                    - **Select Rows:** Choose specific rows if you want to narrow down to certain articles.
                    - **Relevant Keywords:** View the top 5 relevant keywords to each article using AI.
                    - **Relevancy Score:** Articles are sorted by how relevant they are to your search parameters using AI.
                    - **Download:** Export the table as an Excel file, if desired.
                    - **Scrape Articles:** Choose to scrape either all results or only selected rows for a deeper analysis in the next step.
                    
                    ---
                    ##### **Tab 2 – Scraping Results:**
                    a) **Purpose:** Extracts full text from each selected article, displaying it alongside the original information.
                    
                    b) **Features:**
                    - **New Column with Article Text:** This additional column contains the article text for quick reference, saving you time from visiting each article link.
                    - **Download:** As with the first tab, download the table with scraped data as an Excel file if needed.
                    
                    '''
    return How_it_words_Step_2
#————————————————————————————————————————————————————————————————————————————————————————————————————



#————————————————————————————————————————————————————————————————————————————————————————————————————
# Function 4: Tips
#————————————————————————————————————————————————————————————————————————————————————————————————————
def Tips():
    Tips = '''
            ##### **Tips:**
            - **Experiment with Parameters:** Test different combinations of keywords, countries, and filters to get a feel for the kinds of results Presspeak can deliver.
            - **Download Options:** Each tab has an Excel download option, allowing you to keep organized records at each stage.
            - **AI Feature:** Using AI helps cut down on manual sorting and prioritization, especially when dealing with large volumes of articles.

            '''
    return Tips
#————————————————————————————————————————————————————————————————————————————————————————————————————



#————————————————————————————————————————————————————————————————————————————————————————————————————
# Function 4: Input_Instructions
#————————————————————————————————————————————————————————————————————————————————————————————————————
def Input_Instructions():
#————————————————————————————————————————————————————————————————————————————————————————————————————
    Instructions = '''
                ##### **Input Fields Descriptions and How to Use:**
                
                1) **Search Type**:
                :This Have you decided which type of search you want to conduct? 
                    - **Open Search**: Use Google Search Engine to find various content types (websites, articles, PDFs, etc.).
                    - **News**: Use Google News Search to find articles and press releases.
                ---
                
                2) **Date Range**:
                :This Do you have specific dates in mind for your search?
                    - Define the time period for the search results by selecting start and end dates.

                ---
                
                3) **Countries**:
                :This Which countries do you want to focus your search on?
                    - Type the country of interest name in the input box and Select the it.
                    - This field will use all the available variations for the country name in the search including: acronyms, initials, official names.
                
                ---
                
                4) **Variable Keywords**:
                :This What keywords best represent the topics or themes you're searching for?
                    - These keywords are **Dynamic** Meaning:
                        - Each keyword will be used alone with each country to create a search query [e.g "Country" AND "Keyword 1"].
                        - Also all the keywrods will be combined together with each country to create an additional comprehensive query [e.g "Country" AND "Keyword 1 OR "Keyword 2" OR ...]
                    - The tool will collect the results of each individual query search in addition to the results of the comprehensive query. 
                    - You can enter up to 10 keywords to be used in the search.
                    
                ---
                
                5) **Fixed Keywords**:
                :This Are there any additional keywords that should be included in all search queries?
                    - These keywords are **Fixed**, and will be used with all the Selected Coutnries and Main Keywords variations.
                    - To Use click "Add More" to add a new input field for Additional keywords.
                    - In every new Additional Keywords field you can add a list of keywords to be included in the search query.
                    - The Additional keywords will be used with the already defined parameters in this sense: [("Country") AND ("Main Keywords") AND ("Additional Keywords 1") AND ...].
                    
                ---

                6) **Results Quantity**:
                    :This How many search results do you need per query?
                    - The results quantity reflects the number of **results to get per query NOT the total count of the search results.**
                    - Determine the number of results to extract per search query then Use the plus sign or enter the desired quantity manually.

                ---

                7) **Excluded Keywords**:
                :This Are there any terms or topics you want to avoid in your search results?
                    - Enter keywords to exclude from all search queries.
                    - This option can be used to refine your search.

                ---

                8) **Websites & Domains**:
                :This Do you have specific websites or domains you want to focus your search on?
                    - This option is used to narrow the search results to be within certain websites/domains only.
                    - Specify websites or domains to search within using their full link, short link or domain name. 
                    - Input Examples: (https://www.google.com - google.com - .org)
                    
                ---

                9) **Results Language**:
                :This In which language do you want the search results to appear?
                    - This option defines the search results language.
                    - To use Select the target language from the dropdown list.
                    
                ---

                10) **Keywords Location**:
                :This Where do you want the keywords to appear in the search results?
                    - Define where keywords should appear in the search results.
                    - Select the target location from the dropdown list.

                ---

                11) **GEO Location**:
                :This Do you need to specify a specific geographical location for your search?
                    - This option is use to change the search geographical location.
                    - By changing the geo location the search results will also change.

                ---

                12) **Result Type**:
                :This Are you looking for webpages or PDF documents in your search results?
                    - Choose between "Webpages" or "PDFs" for the search results.
                    - Select the desired result type from the dropdown list.
                '''
    return Instructions
#————————————————————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————
# Function 5: Step_By_Step_Guide
#————————————————————————————————————————————————————————————————————————————————————————————————————
def Step_By_Step_Guide():
    Guide = f"""
    st.info('1. Navigate to https://newsgetter.streamlit.app/ using any web browser.')
        {st.image('https://i.postimg.cc/mgK3vPBf/1-Navigation.png',width=1366)}
        {st.divider()}
        {st.info('2. Input the desired search parameters in the sidebar. The mandatory parameters are "Search Type," "Countries," and "Main Keywords."')}
        {st.image('https://i.postimg.cc/1XzNnSsr/2-Main-Parameters.png',width=1366)}
        {st.divider()}
        {st.info('3. Optional: Add more keywords, define a specific date range, or increase the number of results to be extracted.')}
        {st.image('https://i.postimg.cc/G3BDCcgb/3-Additional-Parameters-1.png',width=1366)}
        {st.divider()}
        {st.info('4. Optional: Add Additional optional parameters which can be accessed by toggling the "Advanced Search Options" button.')}
        {st.image('https://i.postimg.cc/x1QNMLfd/3-Additional-Parameters-2.png',width=1366)}
        {st.divider()}
        {st.info('''5.Click the "Start Search" button to initiate the search process and go to the “Google Results” Tab,
                 A progress bar will indicate the search status, and once complete, the extracted results will be displayed in the Google Results tab.''')}
        {st.image('https://i.postimg.cc/BQH1jmGy/5-Start-Search.png',width=1366)}
        {st.divider()}
        {st.info('''6. In the Google Results tab, users can view the extracted results in a table format, the Search links used in the extraction are displayed in clickable buttons, 
                 The total number of extracted results is displayed on the top, and the results are displayed in a table below.''')}
        {st.image('https://i.postimg.cc/Cx4BNd5s/6-Google-Results.png',width=1366)}
        {st.divider()}
        {st.info('''7. Select Results of interest or leave it blank if you want, you can then click on “Download all Results” to download the whole table 
                 or click on “Download Selected Results” to download only the selected results, to proceed with the next step click on “Start Scrapping.”''')}
        {st.image('https://i.postimg.cc/Y2JW2JTY/7-Download-Google-Results.png',width=1366)}
        {st.divider()}
        {st.info('8. Once you click the "Start Scraping" button proceed to the “Scrapping Results” tab, where the program will scrape websites for further details. ')}
        {st.image('https://i.postimg.cc/LhK2dkCg/8-Start-Scrapping.png',width=1366)}
        {st.divider()}
        {st.info('9. Once complete, the combined scraped results with the Google results will be displayed in a table, and users can manipulate or download the results.')}
        {st.image('https://i.postimg.cc/TPYyHGWM/9-Scrapping-Results.png',width=1366)}
        {st.divider()}
        {st.info('10. Access the AI Tools tab to view a 10-point summary of the scraped results and interact with ChatGPT for additional insights and information.')}
        {st.image('https://i.postimg.cc/3wSks6gy/10-AI-Tools.png',width=1366)}
        {st.divider()}
    """
    
    return Guide
#————————————————————————————————————————————————————————————————————————————————————————————————————
