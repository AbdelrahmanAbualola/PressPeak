#████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
#████████████████████████████████████████████████████████████████████████████████████████████ Version 1.0.0 █████████████████████████████████████████████████████████████████████████████████████████████
#████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Import Libraries
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import streamlit as st
from streamlit_tags import st_tags
from stqdm import stqdm

from Instructions import *
from Searchers import *
from Scrappers import *
from Parameters import *
from API import *
from AI_Tools import *
import pandas as pd
import io
import os

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■



#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Main (1): App Style
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#————————————————————————————————————————————————————————————————————————————————————————————————————
# 1.1) Create a session to save data:
#————————————————————————————————————————————————————————————————————————————————————————————————————
Session = st.session_state
#————————————————————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————
# 1.2) Main Page Style:
#————————————————————————————————————————————————————————————————————————————————————————————————————
st.set_page_config(page_title='PressPeak',layout="wide")
css_path = os.path.join(os.path.dirname(__file__), "style.css")
with open(css_path) as css:
    st.markdown(f'<style>{css.read()}</style>',unsafe_allow_html=True)
    
st.title('Get Started with :blue[PressPeek]')
st.markdown("Streamlined News Research and Analysis for Business Insights.")
st.divider()
#————————————————————————————————————————————————————————————————————————————————————————————————————

#————————————————————————————————————————————————————————————————————————————————————————————————————
# 1.3) Setting Main Tabs:
#————————————————————————————————————————————————————————————————————————————————————————————————————
Guidelines_Tab, Google_Tab, Scrapping_Tab = st.tabs(['Guidelines', 'Google', 'Scrape'])
#————————————————————————————————————————————————————————————————————————————————————————————————————       
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Main (2): Search Parameters & user inputs
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
with st.sidebar:
    #————————————————————————————————————————————————————————————————————————————————————————————————
    # 2.1) Sidebar Style:
    #————————————————————————————————————————————————————————————————————————————————————————————————
    st.image('https://infomineo.com/wp-content/uploads/2023/03/Logo-2-bleus.png', width=160,clamp=True)
    #————————————————————————————————————————————————————————————————————————————————————————————————

    #————————————————————————————————————————————————————————————————————————————————————————————————
    # 2.2) User Inputs
    #————————————————————————————————————————————————————————————————————————————————————————————————
    st.divider()
    st.subheader('Search Parameters:',divider='rainbow')
    #————————————————————————————————————————————————————————————————————————————————————————————————
    
    #———————————————————————————————————————————————————————————————————————————————————————————
    # 2.2.1) Keywords
    #———————————————————————————————————————————————————————————————————————————————————————————
    for key in ['keywords_variable', 'keywords_excluded','keywords_fixed']:
        if key not in st.session_state:
            st.session_state[key] = []

    if 'additional_fixed_keywords' not in st.session_state:
        st.session_state['additional_fixed_keywords'] = 0

    if 'additional_keywords' not in st.session_state:
        st.session_state['additional_keywords'] = []    
        
    Session = st.session_state

    with st.popover("Keywords", use_container_width=True):
        # Render st_tags and update session state if the input changes
        keywords_variable = st_tags(label="Any of Keywords",text="Any should be in results",maxtags=20,key="keywords_variable",value=Session['keywords_variable'])
        keywords_excluded = st_tags(label="None of Keywords",text="Must not be in results",maxtags=20,key="keywords_excluded",value=Session['keywords_excluded'])
        keywords_fixed = st_tags(label='All of Keywords', text='Must be in results', maxtags = 20, key='keywords_fixed',value=Session['keywords_fixed'])
              
        updated_values = {'keywords_variable': keywords_variable, 'keywords_excluded': keywords_excluded,'keywords_fixed':keywords_fixed}
        for key, value in updated_values.items():
            if Session[key] != value:
                Session[key] = value

        # Add/Remove buttons for additional keyword fields
        btn1, btn2 = st.columns(2)
        
        with btn1:
            if st.button('➕ Add', help='Add an additional keyword input field',use_container_width=True):
                st.session_state['additional_fixed_keywords'] += 1
                st.session_state['additional_keywords'].append([])  # Append a new empty list for new input

        with btn2:    
            if st.button('❌ Remove', help='Remove the last additional keyword input field',use_container_width=True):
                if st.session_state['additional_fixed_keywords'] > 0:
                    st.session_state['additional_fixed_keywords'] -= 1
                    st.session_state['additional_keywords'].pop()  # Remove the last input field data

        # Render additional st_tags input fields
        for i in range(st.session_state['additional_fixed_keywords']):
            key = f'additional_keywords_{i}'  # Unique key for each input
            if key not in st.session_state['additional_keywords']:
                st.session_state['additional_keywords'].append([])  # Initialize if not present

            # Create the st_tags input field for the additional fixed keyword
            st.session_state['additional_keywords'][i] = st_tags(
                label=f'Additional Keywords ({i + 1})',
                key=key,
                value=st.session_state['additional_keywords'][i]
            )
    #———————————————————————————————————————————————————————————————————————————————————————————
    
    
    #———————————————————————————————————————————————————————————————————————————————————————————
    # 2.2.2) Countries
    #———————————————————————————————————————————————————————————————————————————————————————————
    with st.popover('Countries',use_container_width=True):
        countries = st.multiselect('Countries *',list(Google_Parameters.countries_acronyms().keys()),max_selections=20)
    #———————————————————————————————————————————————————————————————————————————————————————————



    #———————————————————————————————————————————————————————————————————————————————————————————
    # 2.2.3) Websites
    #———————————————————————————————————————————————————————————————————————————————————————————
    if 'websites' not in st.session_state:
        st.session_state['websites'] = []
        
    with st.popover('Websites',use_container_width=True):
        websites= st_tags(label='Websites', text='Restrict to these sites', maxtags = 10, key='websites',value=st.session_state['websites'])
        
    if st.session_state['websites'] != websites:
        st.session_state['websites'] = websites
    #———————————————————————————————————————————————————————————————————————————————————————————



    #———————————————————————————————————————————————————————————————————————————————————————————
    # 2.2.4) Filters
    #———————————————————————————————————————————————————————————————————————————————————————————
    with st.popover('Filters',use_container_width=True):
        location = st.selectbox('Location',Google_Parameters.countries_acronyms().keys(),placeholder="Choose a Country",help='This optional parameter determins search relevance to a particular location, even if the content doesn’t strictly originate from that location.')
        geolocation = st.selectbox('Geolocation',Google_Parameters.geolocation().keys(),placeholder="Choose a Country",help='This optional parameter determines where your Google search originates')
        date_range = st.date_input ('Date Range',value=[],format="DD/MM/YYYY",help='Select the Start and End dates for the search')    
        colQuantity, colLanguage = st.columns(2)
        with colQuantity:
            quantity = st.number_input('Quantity',min_value=10,max_value=100,help='Enter the number of Google results to get per search query')
        with colLanguage:
            language = st.selectbox('Language',Google_Parameters.languages().keys(),placeholder="Choose a language",help='Language of results')   
    #———————————————————————————————————————————————————————————————————————————————————————————
    st.divider()
    st.info('**ℹ️) Note :** Google imposes a 2048 characters limit on inputs. Exceeding this will result in ignored parameters')

    try:
        QUERIES = Serper.Queries(keywords_variable, keywords_fixed, keywords_excluded, websites,countries, date_range)
        Query_Limit = len(max(QUERIES, key=len))
        Results_Quantity = quantity * len(QUERIES)
    except:
        Query_Limit = 0
        Results_Quantity = 0
    limit,qant = st.columns(2)
    with limit:
        st.metric("Characters Limit",Query_Limit,F"{2048-Query_Limit} Characters" )
    with qant:
        st.metric("Results Quantity", Results_Quantity,f"{2000-Results_Quantity} Articles")
    
    
    
    #————————————————————————————————————————————————————————————————————————————————————————————————
    # 2.3) Buttons: Start Search & Refresh All
    #————————————————————————————————————————————————————————————————————————————————————————————————
    st.divider()
    st.subheader('Search Actions',divider='rainbow')
    Start_Search = st.button ('⚡ Start Search',use_container_width=True)
    Refresh_All = st.button('⟳ Refresh All',use_container_width=True)
        
    if Refresh_All:
        st.cache_data.clear()
        Session.clear()
        st.rerun()
        
    st.divider()
    st.caption('PressPeak - v1.0.0')
    #————————————————————————————————————————————————————————————————————————————————————————————————    
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■



#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Tab (1): Guidelines
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
with Guidelines_Tab:
    st.subheader('Overview',divider='rainbow')

    with st.expander('**Introduction**',expanded=False):
        st.info(Introduction(), icon='ℹ️')
    
    with st.expander('**Features**',expanded=False):
        st.info(Features(), icon='ℹ️')
    
    
    
    st.subheader('How it Works',divider='rainbow')
    with st.expander('**Step 1: Search Parameters**',expanded=False):
        st.info(How_it_words_Step_1(), icon='ℹ️')
    
    with st.expander('**Step 2: Review Results**',expanded=False):
        st.info(How_it_words_Step_2(), icon='ℹ️')  
        
    with st.expander('**ℹ️) Tips**',expanded=False):
        st.info(Tips(), icon='ℹ️')
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■



#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Tab (2): Results
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Process (1) Prepare Results
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
@st.cache_data(show_spinner=True)
def Articles(keywords_variable, keywords_fixed, keywords_excluded, websites,countries, date_range,location,geolocation,language,quantity):
    # Get Results from Serper API
    QUERIES = Serper.Queries(keywords_variable, keywords_fixed, keywords_excluded, websites,countries, date_range)
    PAYLOAD = Serper.Payloads(QUERIES,location,geolocation,language,quantity)
    RESULTS = Serper.Results(PAYLOAD)
    
    Session['QUERIES'] = QUERIES
    Session['PAYLOAD'] = PAYLOAD
    Session['RESULTS'] = RESULTS
    
    # Prepare Articles table
    ARTICLES = pd.DataFrame(RESULTS)
    try:
        ARTICLES = ARTICLES.drop(['imageUrl','position'],axis=1).rename(columns={'title':'Headline','link':'Link','snippet':'Short Description','date':'Date','source':'Source'})
    except Exception as e:
        st.error("An Error Occured with Getting Google Results: {e}")
        
    ARTICLES['Select'] = False
    ARTICLES = pd.DataFrame(ARTICLES)
    ARTICLES = ARTICLES.drop_duplicates(subset=["Headline", "Link"], keep="first").reset_index(drop=True)
    
    keywords = keywords_variable + keywords_fixed + countries
    ARTICLES = add_keywords_column(ARTICLES, keywords)
    ARTICLES = add_relevancy_score_column(ARTICLES, keywords)
    
    column_order = ['Select','Headline','Short Description','Date','Source','Relevant Keywords', 'Relevancy Score', 'Link']
    ARTICLES = ARTICLES[column_order]
    ARTICLES = ARTICLES.sort_values(by='Relevancy Score', ascending=False)

    return ARTICLES
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Process (2) Get Results
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
if Start_Search:
    st.cache_data.clear()
    try:
        Google_Results = Articles(keywords_variable, keywords_fixed, keywords_excluded, websites,countries, date_range,location,geolocation,language,quantity)
        Session['Google_Results'] = Google_Results
    except Exception as e:
        st.error(f"Couldn't Get Google Results, Error: {e}")
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    
    
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
# Process (3) Display Results
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
with Google_Tab:
    #————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    # 3.1) Style:
    #————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    
    #————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    
    #————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    # 3.2) Results:
    #————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    if 'Google_Results' in Session.keys():
        st.subheader('Google Results',divider='rainbow')
        
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # a) Display Results
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
        with st.spinner('Google Results Extraction'):
            Google_Results_All = st.data_editor(Session['Google_Results'],
                            column_config={
                                'Select':st.column_config.CheckboxColumn(),
                                "Link": st.column_config.LinkColumn("Link",display_text="Link"),
                                'Relevancy Score': st.column_config.NumberColumn("Relevancy Score", format="%0.2f")
                                },
                            hide_index=True)

        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
    
    
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # b) Show Start Scrapping, Download All, Download Selected Buttons
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
        Google_Results = Session['Google_Results']
        Google_Results_Selected = Google_Results_All[Google_Results_All['Select']]
        
        col3,col4 = st.columns(2)
        with col3:
            with st.popover('Scrape',use_container_width=True):
                Scrape_All = st.button('All Results',use_container_width=True)
                Scrape_Selected = st.button('Selected Only',use_container_width=True)
                
        with col4:
            with st.popover('Download',use_container_width=True):
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                    Google_Results.to_excel(writer, sheet_name='Google Results', index=False)
                Donwload = st.download_button('Download All Results',data=buffer,file_name=f"All_Google_Results.xlsx",mime='textcsv',use_container_width=True)
                
                buffer2 = io.BytesIO()
                with pd.ExcelWriter(buffer2, engine='xlsxwriter') as writer:
                    Google_Results_Selected.to_excel(writer, sheet_name='Google Results', index=False)
                Donwload = st.download_button('Download Selected Results',data=buffer2,file_name=f"Selected_Google_Results.xlsx",mime='textcsv',use_container_width=True)
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
        


        
            

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Tab (3): Scrapping
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
with Scrapping_Tab:
    if 'Google_Results' in Session.keys():
        st.subheader('Scrapping Results',divider='rainbow')
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # a) Start Scrapping
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
        with st.spinner('Scrapping Results' ):
            if Scrape_All:
                LINKS = Google_Results['Link']
                Scrapped_Articles = Scrapper.Multi_Scrapper(stqdm(LINKS))
                Session['Scrapped_Articles'] = Scrapped_Articles
            if Scrape_Selected:
                LINKS = Google_Results_Selected['Link']
                Scrapped_Articles = Scrapper.Multi_Scrapper(stqdm(LINKS))
                Session['Scrapped_Articles'] = Scrapped_Articles
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————


        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # d) Compine Scrapped results to Google Results
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
            if 'Scrapped_Articles' in Session.keys():
                Scrapped_Articles = pd.DataFrame(Session['Scrapped_Articles'])
                Combined_Results = pd.merge(Google_Results,Scrapped_Articles, on='Link', how='inner')
                column_order = ['Select','Headline','Short Description', 'Summary','Date','Source','Relevant Keywords', 'Relevancy Score', 'Link']
                Combined_Results = Combined_Results[column_order]
                Session['Combined_Results'] = Combined_Results
            
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
        
        
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————
        # d) Show Combined Results
        #————————————————————————————————————————————————————————————————————————————————————————————————————————————   
        if 'Combined_Results' in Session.keys():
            Combined_Results= st.data_editor(Combined_Results,
                                            column_config={
                                                'Select':st.column_config.CheckboxColumn(),
                                                "Link": st.column_config.LinkColumn("Link",display_text="Link")},
                                            hide_index=True)   
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
