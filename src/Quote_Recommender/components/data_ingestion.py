import os
import requests
import pandas as pd
from collections import OrderedDict
from bs4 import BeautifulSoup
from pathlib import Path
import random
from src.Quote_Recommender.utils.common import get_size
from src.Quote_Recommender import logger
from src.Quote_Recommender.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config = DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.save_path):
            quotes = []
            author = []
            tags_mul = []
            tags = self.config.tags

            for tag in tags:
                ran_pag = list(set([random.randint(1,100) for _ in range(self.config.num_pages)]))
                for page in ran_pag:
                    url = f"https://www.goodreads.com/quotes/tag/{tag}?page={page}"
                    page_res = requests.get(url)
                    content = BeautifulSoup(page_res.content, 'html.parser')
                    quotes_html_page = content.find_all('div',{'class':'quoteDetails'})

                    for quote_html in quotes_html_page:
                        quotes.append(quote_html.find('div',{'class':'quoteText'}).get_text().strip().split('\n')[0])
                        author.append(quote_html.find('span',{'class':'authorOrTitle'}).get_text().strip())
                        if quote_html.find('div',{'class':'greyText smallText left'}) is not None:
                            tags_list = [tag.get_text() for tag in quote_html.find('div',{'class':'greyText smallText left'}).find_all('a')]
                            tags_ls = list(OrderedDict.fromkeys(tags_list))
                            if 'attributed-no-source' in tags_ls:
                                tags_ls.remove('attributed-no-source')
                        else:
                            tags_ls = None
                        tags_mul.append(tags_ls)
            
            data_frame = pd.DataFrame({
                "Quotes": quotes,
                "Author": author,
                "Tags": tags_mul
            })

            data_frame.to_csv(self.config.save_path)
            logger.info(f"data scraped/collected at {self.config.save_path}")
        
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.save_path))}")