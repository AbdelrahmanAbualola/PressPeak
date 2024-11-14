#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Import Libraries
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
from goose3 import Goose
from newspaper import Article
from Webtrench import TextScrapper
import concurrent.futures

#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# Scrappers Functions
#■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
class Scrapper():
    #—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    # Function (1) extract_summary
    #—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    def extract_summary(link):
        Summary = 'NA'

        # Try using Goose
        try:
            Extractor_Goose = Goose()
            Summary = Extractor_Goose.extract(link).meta_description
            if Summary:
                return {'Link': link, 'Summary': Summary}
        except Exception as e:
            print(f'Goose Failed for {link}: {e}')

        # Try using Newspaper if Goose fails
        try:
            Extractor_Newspaper = Article(link)
            Extractor_Newspaper.download()
            Extractor_Newspaper.parse()
            Extractor_Newspaper.nlp()
            Summary = Extractor_Newspaper.summary.split('\n')
            if Summary:  # Check if summary is not empty
                return {'Link': link, 'Summary': "\n".join(Summary)}
        except Exception as e:
            print(f'Newspaper Failed for {link}: {e}')

        # Try using Webtrench if Newspaper fails
        try:
            Extractor_Webtrench = TextScrapper.paragraph_from_url(link)
            Extractor_Webtrench = ([p.text.strip() for p in Extractor_Webtrench if p.text.strip()])
            Summary = "\n".join(Extractor_Webtrench)
            if Summary:
                return {'Link': link, 'Summary': Summary}
        except Exception as e:
            print(f'Webtrench Failed for {link}: {e}')

        # If all attempts failed and Summary is still 'NA', return it
        return {'Link': link, 'Summary': Summary}
    #—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————



    #—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    # Function (2) Multi_Scrapper
    #—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    def Multi_Scrapper(links):
        Extracts = []
        
        # Use ThreadPoolExecutor to run extractions concurrently
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Map each link to the extract_summary function
            results = list(executor.map(Scrapper.extract_summary, links))

        # Collect the results
        Extracts.extend(results)
        
        return Extracts

    #—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
