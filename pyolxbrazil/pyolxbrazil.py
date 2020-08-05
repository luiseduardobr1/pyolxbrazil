from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import json
import re
import datetime

# Fake user-agent
ua = UserAgent()
header = {'User-Agent': str(ua.random)}

# States - DDD
states_ddd = {"99": "Maranhão", "98": "Maranhão", "97": "Amazonas",
              "96": "Amapá", "95": "Roraima", "94": "Pará",
              "93": "Pará", "92": "Amazonas", "91": "Pará",
              "89": "Piauí", "88": "Ceará", "87": "Pernambuco",
              "86": "Piauí", "85": "Ceará", "84": "Rio Grande do Norte",
              "83": "Paraíba", "82": "Alagoas", "81": "Pernambuco",
              "79": "Sergipe", "77": "Bahia", "75": "Bahia",
              "74": "Bahia", "73": "Bahia", "71": "Bahia",
              "69": "Rondônia", "68": "Acre", "67": "Mato Grosso do Sul",
              "66": "Mato Grosso", "65": "Mato Grosso", "64": "Goiás",
              "63": "Tocantins", "62": "Goiás", "61": "Distrito Federal/Goiás",
              "55": "Rio Grande do Sul", "54": "Rio Grande do Sul",
              "53": "Rio Grande do Sul", "51": "Rio Grande do Sul",
              "49": "Santa Catarina", "48": "Santa Catarina",
              "47": "Santa Catarina", "46": "Paraná", "45": "Paraná",
              "44": "Paraná", "43": "Paraná", "42": "Paraná", "41": "Paraná",
              "38": "Minas Gerais", "37": "Minas Gerais", "35": "Minas Gerais",
              "34": "Minas Gerais", "33": "Minas Gerais", "32": "Minas Gerais",
              "31": "Minas Gerais", "28": "Espírito Santo",
              "27": "Espírito Santo", "24": "Rio de Janeiro",
              "22": "Rio de Janeiro", "21": "Rio de Janeiro",
              "19": "São Paulo", "18": "São Paulo", "17": "São Paulo",
              "16": "São Paulo", "15": "São Paulo", "14": "São Paulo",
              "13": "São Paulo", "12": "São Paulo", "11": "São Paulo"}

# Months - abbreviations
months = {'jan': '01 ',
          'fev': '02 ',
          'mar': '03 ',
          'abr': '04 ',
          'mai': '05 ',
          'jun': '06 ',
          'jul': '07 ',
          'ago': '08 ',
          'set': '09 ',
          'out': '10 ',
          'nov': '11 ',
          'dez': '12 '}


class OLXBrazil:

    """A class used to scrape ad data from OLX website (http://www.olx.com.br).

    Attributes
    ----------
    search : str
        searched item on OLX

    state : str
        initials of the brazilian state where the item is located.
        For example, state='ce' (for Ceará)
                  or state='rj' (for Rio de Janeiro)

    Methods
    -------
    extract(filter_by='relevance', all_pages=False, limit=None):
        Return a list containing all items available.
            filter_by (str):
                relevance (Default): most relevant items
                price: cheapest price for the items
                new: recently added items on the website

            all_pages (bool):
                False (Default): return the first page searched
                                 or until the "limit" (parameter) page
                True: return all the pages searched

            limit (int or None):
                Page limit searched.
                    If "all_pages" is True, then "limit" should be None (Default).
                    If "all_pages" is False, then "limit" can be None or int.

    unique_extract(url, complete=False):
        Return a dictionary containing the ad information.
            url (str):
                item URL
            complete (bool):
                False (Default): relevant ad information
                True: complete ad information
    """

    def __init__(self, search, state):
        self._search = search
        self._state = state

    def __str__(self):
        return OLXBrazil.__doc__

    # Get number of pages
    def __number_of_pages(self, soup):
        LAST_PAGES_TAG = 'sc-1m4ygug-4 cXxSMf'
        if soup.find('ul', {'class': LAST_PAGES_TAG}) is not None:
            last_page_link = soup.find('ul', {'class': LAST_PAGES_TAG}).find(
                'a', {'data-lurker-detail': 'last_page'})['href']
            last_page = re.findall('o=(\d*)|$', last_page_link)[0]
            return int(last_page)

    # Search by relevance, price or new products
    def __olx_requests(self, filter_by='relevance', page=1):
        # relevance = most relevant
        # price = cheapest
        # new = newest

        if filter_by == 'relevance':
            link = f'https://{self._state}.olx.com.br/?o={page}&q={self._search}'
            response = requests.get(link, headers=header)
            soup = BeautifulSoup(response.text, "html.parser")
            return soup

        elif filter_by == 'price':
            link = f'https://{self._state}.olx.com.br/?o={page}&q={self._search}&sp=1'
            response = requests.get(link, headers=header)
            soup = BeautifulSoup(response.text, "html.parser")
            return soup

        elif filter_by == 'new':
            link = f'https://{self._state}.olx.com.br/?o={page}&q={self._search}&sf=1'
            response = requests.get(link, headers=header)
            soup = BeautifulSoup(response.text, "html.parser")
            return soup

    # Get unique product information
    @staticmethod
    def unique_extract(url, complete=False):

        """Return a dictionary containing the ad information.
            url (str):
                item URL
            complete (bool):
                False (Default): relevant ad information
                True: complete ad information"""

        if 'olx.com' in url:
            response = requests.get(url, headers=header)
            soup = BeautifulSoup(response.text, "html.parser")

            # Information dictionary
            product_dict_unique = {}

            # JSON
            general_info = json.loads(
                soup.find('script', {'id': 'initial-data'})['data-json'])['ad']

            # Complete information
            if complete is True:
                return general_info

            # Partial information
            # Name
            product_dict_unique['Name'] = general_info['subject']
            # ID
            product_dict_unique['ID'] = general_info['listId']
            # Image
            product_dict_unique['Image'] = general_info['images'][0]['original']
            # Price
            product_dict_unique['Price'] = re.findall('R\$ (\d*,?\.?\d*)|$', general_info['priceValue'])[0].replace('.', '')
            # Description
            product_dict_unique['Description'] = general_info['description']
            # Date
            product_dict_unique['Datetime (UTC)'] = general_info['listTime']
            # Author
            product_dict_unique['Author'] = general_info['user']['name']
            # Phone
            product_dict_unique['Phone'] = general_info['phone']['phone']
            # Type
            product_dict_unique['Type'] = general_info['parentCategoryName']
            # Category
            product_dict_unique['Category'] = general_info['categoryName']
            # Location
            product_dict_unique['Location'] = general_info['location']

            return product_dict_unique

    # Scrapping
    def extract(self, filter_by='relevance', all_pages=False, limit=None):

        """Return a list containing all items available.
                filter_by (str):
                    relevance (Default): most relevant items
                    price: ascending price for the items
                    new: recently added items on the website

                all_pages (bool):
                    False (Default): return the first page searched
                                    or until the "limit" (parameter) page
                    True: return all the pages searched

                limit (int or None):
                    Page limit searched.
                        If "all_pages" is True, then "limit" should be None (Default).
                        If "all_pages" is False, then "limit" can be None or int."""

        page = 1
        total_of_pages = 1
        products_list = []

        while page <= total_of_pages:

            products_code = None
            while products_code is None:
                soup = self.__olx_requests(filter_by, page)
                products_code = soup.find('div', {'class': "sc-1fcmfeb-0 WQhDk"})

            if page == 1 and all_pages is True and limit is None:
                max_pages = self.__number_of_pages(soup)
                if max_pages is not None:
                    total_of_pages = max_pages

            elif page == 1 and all_pages is False and isinstance(limit, int):
                max_pages = self.__number_of_pages(soup)
                if max_pages is not None and limit <= max_pages:
                    total_of_pages = limit
                else:
                    total_of_pages = 1

            # Individual product - TAG
            for tags_products in ["sc-1fcmfeb-2 ggOGTJ", "sc-1fcmfeb-2 hFOgZc"]:
                for each_product in products_code.findAll('li', {'class': tags_products}):

                    # Each product dictionary
                    product_dict = {}

                    # Name
                    PRODUCT_NAME_TAG = 'fnmrjs-8 kRlFBv'
                    if each_product.find('div', {'class': PRODUCT_NAME_TAG}) is not None:
                        product_name = each_product.find('div', {'class': PRODUCT_NAME_TAG}).text
                        if 'Anunciante online' in product_name:
                            product_name = product_name.replace('Anunciante online', '')
                        product_dict['Name'] = product_name
                    else:
                        continue

                    # ID
                    product_id = each_product.find('a', {'data-lurker-detail': 'list_id'})['data-lurker_list_id']
                    product_dict['ID'] = product_id

                    # Image
                    PRODUCT_IMAGE_TAG = 'fnmrjs-5 jksoiN'
                    product_img = each_product.find('div', {'class': PRODUCT_IMAGE_TAG}).find('img')['src']
                    product_dict['Image'] = product_img

                    # Price
                    PRODUCT_PRICE_TAG = 'fnmrjs-15 clbSMi'
                    if each_product.find('div', {'class': PRODUCT_PRICE_TAG}).text:
                        product_price = each_product.find('div', {'class': PRODUCT_PRICE_TAG}).text
                        product_dict['Price'] = re.findall('R\$ (\d*,?\.?\d*)|$', product_price)[0].replace('.', '')
                    else:
                        product_dict['Price'] = '-'

                    # Date
                    PRODUCT_DATE_TAG = 'fnmrjs-18 gMKELN'
                    product_date = each_product.find('div', {'class': PRODUCT_DATE_TAG}).text
                    if 'Hoje' in product_date:
                        product_date = product_date.replace('Hoje', datetime.date.today().strftime("%d/%m "))
                        product_dict['Date'] = product_date

                    elif 'Ontem' in product_date:
                        product_date = product_date.replace('Ontem', (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d/%m "))
                        product_dict['Date'] = product_date

                    else:
                        product_date = product_date.replace(re.findall(' ([a-z]*)\d*', product_date)[0], months[re.findall(' ([a-z]*)\d*', product_date)[0]]).replace(' ', r'/', 1)
                        product_dict['Date'] = product_date

                    # Location
                    PRODUCT_LOCATION_PARENT_TAG = 'fnmrjs-21 bktOWr'
                    PRODUCT_LOCATION_CHILD_TAG = 'fnmrjs-13 hdwqVC'
                    product_location = each_product.find('div', {'class': PRODUCT_LOCATION_PARENT_TAG}).find('p', {'class': PRODUCT_LOCATION_CHILD_TAG}).text
                    product_dict['City'] = re.findall('(.*\w*),|$', product_location)[0]
                    product_dict['Neighborhood'] = re.findall(r',(.*\w*) - |$', product_location)[0].strip()
                    product_dict['State'] = states_ddd[re.findall(r'DDD (\d*)|$', product_location)[0]]

                    # Link
                    product_link = each_product.find('a', {'data-lurker-detail': 'list_id'})['href']
                    product_dict['Link'] = product_link

                    # List of Products
                    products_list.append(product_dict)

            # Next page
            page += 1

        return products_list
