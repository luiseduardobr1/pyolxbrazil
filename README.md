# PyOLXBrazil

Scrapper for [OLX Brazil](http://www.olx.com.br)


<p align="center">
  <img width="450" height="222" src="https://raw.githubusercontent.com/luiseduardobr1/pyolxbrazil/master/logo_oficial.png">
</p>

## Description
PyOLXBrazil is a simple python scrapper for ads information from OLX Brazil. It searches for an item and extracts all the available results sorted by relevance, price or date. If a specific ad information is necessary, it can also be extracted through its URL.

## Installation
Download using pip via pypi.
```
pip install pyolxbrazil
```

## Getting started
### First Search
Let's do a simple search for *raspberry* in the brazilian state of Ceará (*CE*):
```Python
from pyolxbrazil import OLXBrazil

results = OLXBrazil(search='raspberry', state='ce')
results.extract()
```

The output will be a list with the first page results for *raspberry*:
```
[{'Name': 'Raspberry pi 3 + fonte',
  'ID': '774669052',
  'Image': 'https://img.olx.com.br/thumbs256x256/78/788033318261916.jpg',
  'Price': '280',
  'Date': '04/08 20:09',
  'City': 'Fortaleza',
  'Neighborhood': 'José Bonifácio',
  'State': 'Ceará',
  'Link': 'https://ce.olx.com.br/fortaleza-e-regiao/computadores-e-acessorios/raspberry-pi-3-fonte-774669052'},

  ...

 {'Name': 'Fliperama Portatil Arcade Óptico 20 Mil Jogos 64gb - 68x24',
  'ID': '747325743',
  'Image': 'https://img.olx.com.br/thumbs256x256/02/021035042251688.jpg',
  'Price': '1190',
  'Date': '20/05 10:45',
  'City': 'Fortaleza',
  'Neighborhood': 'Centro',
  'State': 'Ceará',
  'Link': 'https://ce.olx.com.br/fortaleza-e-regiao/videogames/fliperama-portatil-arcade-optico-20-mil-jogos-64gb-68x24-747325743'},
 {'Name': 'Vendo controles novos USB',
  'ID': '747263722',
  'Image': 'https://img.olx.com.br/thumbs256x256/02/026020005031256.jpg',
  'Price': '40',
  'Date': '20/05 06:00',
  'City': 'Fortaleza',
  'Neighborhood': 'Maraponga',
  'State': 'Ceará',
  'Link': 'https://ce.olx.com.br/fortaleza-e-regiao/videogames/vendo-controles-novos-usb-747263722'}]
```
### Scrapping all the pages
If we want to scrape all the pages:
```Python
from pyolxbrazil import OLXBrazil

results = OLXBrazil(search='ipad 3', state='ce')
print('Total results: ' + str(len(results.extract(all_pages=True))))
results.extract(all_pages=True)
```
Ouput:
```
Total results: 167
[{'Name': 'IPad 3',
  'ID': '773392297',
  'Image': 'https://img.olx.com.br/thumbs256x256/75/750014311973959.jpg',
  'Price': '900',
  'Date': '1/08 12:32',
  'City': 'Fortaleza',
  'Neighborhood': 'Engenheiro Luciano Cavalcante',
  'State': 'Ceará',
  'Link': 'https://ce.olx.com.br/fortaleza-e-regiao/computadores-e-acessorios/ipad-3-773392297'},

  ...]
```

### Scraping some pages sorted by price
We can also specify the number of pages to scrape (*limit*) and sort the results by *relevance*, *price* (ascending) or *date* (newest):
```Python
from pyolxbrazil import OLXBrazil

results = OLXBrazil(search='ipad 3', state='ce')

# it'll scrape just 2 pages, sorted by price
my_extraction = results.extract(filter_by='price', all_pages=False, limit=2)

print('Total results: ' + str(len(my_extraction)))
my_extraction
```
Output:
```
Total results: 89
[{'Name': 'Cabo De áudio P2 p/ 2 RCA 1.5M',
  'ID': '632449877',
  'Image': 'https://img.olx.com.br/thumbs256x256/72/727924012289485.jpg',
  'Price': '10',
  'Date': '2/07 12:54',
  'City': 'Fortaleza',
  'Neighborhood': 'Bom Jardim',
  'State': 'Ceará',
  'Link': 'https://ce.olx.com.br/fortaleza-e-regiao/audio-tv-video-e-fotografia/cabo-de-audio-p2-p-2-rca-1-5m-632449877'},
 {'Name': 'Cabo Carregador iPhone 5 6 7 8 X Lightning 1M Apple',
  'ID': '651183643',
  'Image': 'https://img.olx.com.br/thumbs256x256/21/213913036044079.jpg',
  'Price': '15',
  'Date': '18/07 00:03',
  'City': 'Fortaleza',
  'Neighborhood': 'Bom Jardim',
  'State': 'Ceará',
  'Link': 'https://ce.olx.com.br/fortaleza-e-regiao/celulares/cabo-carregador-iphone-5-6-7-8-x-lightning-1m-apple-651183643'},

  ...]
```

### Get ad data from URL
If you want to scrape basic information about a specific ad:
```Python
from pyolxbrazil import OLXBrazil

url = 'https://ce.olx.com.br/fortaleza-e-regiao/moveis/armario-774482659'
results = OLXBrazil.unique_extract(url)
results
```
Output:
```
{'Name': 'Armário',
 'ID': 774482659,
 'Image': 'https://img.olx.com.br/images/78/786042436548103.jpg',
 'Price': '449',
 'Description': 'Armário Novo 5 portas e 1 gaveta da Loja PRONTA ENTREGA.<br><br>WhatsApp 9 XXXX-XXXX Luan',
 'Datetime (UTC)': '2020-08-04T16:08:09.000Z',
 'Author': 'luan Estofados',
 'Phone': '859XXXXXX',
 'Type': 'Para a sua casa',
 'Category': 'Móveis',
 'Location': {'address': None,
  'neighbourhood': 'Siqueira',
  'neighbourhoodId': 10731,
  'municipality': 'Fortaleza',
  'municipalityId': 3327,
  'zipcode': '60732330',
  'mapLati': 0,
  'mapLong': 0,
  'uf': 'CE',
  'ddd': '85',
  'zoneId': 2672,
  'zone': 'fortaleza',
  'region': 'Fortaleza e região, CE'}}
```

Otherwise, to get all ad information:
```Python
from pyolxbrazil import OLXBrazil

url = 'https://ce.olx.com.br/fortaleza-e-regiao/moveis/armario-774482659'
results = OLXBrazil.unique_extract(url, complete=True)
results
```
Output:
```
{'listId': 774482659,
 'body': 'Armário Novo 5 portas e 1 gaveta da Loja PRONTA ENTREGA.<br><br>WhatsApp 9 XXXX-XXXX Luan',
 'subject': 'Armário',
 'priceLabel': 'Preço',
 'priceValue': 'R$ 449',
 'oldPrice': None,
 'professionalAd': True,
 'category': 5020,
 'parentCategoryName': 'Para a sua casa',
 'categoryName': 'Móveis',
 'searchCategoryLevelZero': 5000,
 'searchCategoryLevelOne': 5020,
 'searchCategoryLevelTwo': 0,
 'origListTime': 1596557289,
 'adReply': '0',
 'friendlyUrl': 'https://ce.olx.com.br/fortaleza-e-regiao/moveis/armario-774482659',
 'user': {'userId': 83129463, 'userUid': 81412291, 'name': 'luan Estofados'},
 'phone': {'phone': '859XXXXXX',
  'phoneHidden': False,
  'phoneVerified': True},
 'images': [{'original': 'https://img.olx.com.br/images/78/786042436548103.jpg',
   'originalAlt': 'Armário',
   'thumbnail': 'https://img.olx.com.br/thumbs/78/786042436548103.jpg'},
  {'original': 'https://img.olx.com.br/images/78/787038438930941.jpg',
   'originalAlt': 'Armário - Foto 2',
   'thumbnail': 'https://img.olx.com.br/thumbs/78/787038438930941.jpg'}],
 'videos': [],
 'location': {'address': None,
  'neighbourhood': 'Siqueira',
  'neighbourhoodId': 10731,
  'municipality': 'Fortaleza',
  'municipalityId': 3327,
  'zipcode': '60732330',
  'mapLati': 0,
  'mapLong': 0,
  'uf': 'CE',
  'ddd': '85',
  'zoneId': 2672,
  'zone': 'fortaleza',
  'region': 'Fortaleza e região, CE'},
 'properties': [{'name': 'category',
   'label': 'Categoria',
   'value': 'Móveis',
   'values': None,
   'url': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/moveis'},
  {'name': 'furniture_type',
   'label': 'Tipo',
   'value': 'Sofás e poltronas',
   'values': None,
   'url': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/moveis/sofas-e-poltronas'}],
 'pubSpecificData': [{'context': 'width=300,height=250',
   'data': [{'key': 'appnexus_placement_id', 'value': '11647384'},
    {'key': 'aol_placement_id', 'value': '4349247,4349251'},
    {'key': 'criteo_zone_id', 'value': '802888'}]},
  {'context': 'width=*,height=*',
   'data': [{'key': 'afsh_channel_id', 'value': 'shopping_furniture_vi'},
    {'key': 'afsh_pub_id', 'value': 'partner-vert-pla-olx-pdp'}]}],
 'trackingSpecificData': [{'key': 'region', 'value': 'Fortaleza e região'}],
 'searchboxes': [{'label': 'Agro e indústria',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/agro-e-industria'},
  {'label': 'Animais de estimação',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/animais-de-estimacao'},
  {'label': 'Artigos infantis',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/artigos-infantis'},
  {'label': 'Autos e peças',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/autos-e-pecas'},
  {'label': 'Comércio e escritório',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/comercio-e-escritorio'},
  {'label': 'Eletrônicos e celulares',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/eletronicos-e-celulares'},
  {'label': 'Esportes e lazer',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/esportes-e-lazer'},
  {'label': 'Imóveis',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/imoveis'},
  {'label': 'Moda e beleza',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/moda-e-beleza'},
  {'label': 'Música e hobbies',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/musica-e-hobbies'},
  {'label': 'Para a sua casa',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/para-a-sua-casa'},
  {'label': 'Serviços',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/servicos'},
  {'label': 'Vagas de emprego',
   'link': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/vagas-de-emprego'}],
 'breadcrumbUrls': [{'label': 'Ceará', 'url': 'https://ce.olx.com.br'},
  {'label': 'Fortaleza e região',
   'url': 'https://ce.olx.com.br/fortaleza-e-regiao'},
  {'label': 'Móveis',
   'url': 'https://ce.olx.com.br/fortaleza-e-regiao/moveis'},
  {'label': 'Fortaleza',
   'url': 'https://ce.olx.com.br/fortaleza-e-regiao/fortaleza/moveis'}],
 'tags': None,
 'carSpecificData': None,
 'description': 'Armário Novo 5 portas e 1 gaveta da Loja PRONTA ENTREGA.<br><br>WhatsApp 9 8753-0298 Luan',
 'price': 'R$ 449',
 'listTime': '2020-08-04T16:08:09.000Z',
 'locationProperties': [{'label': 'CEP', 'value': '60732330'},
  {'label': 'Município', 'value': 'Fortaleza'},
  {'label': 'Bairro', 'value': 'Siqueira'}],
 'securityTips': ['Não faça pagamentos antes de verificar o que está sendo anunciado.',
  'Fique atento com excessos de facilidades e preços abaixo do mercado.',
  'Se está desapegando, limpe bem não só as mãos, como o produto e deixe-o também bem embrulhado.'],
 'slotsId': ['adBottomLocation'],
 'denounceLink': 'https://denuncia.olx.com.br/report?from=web&data=eyJsaXN0SWQiOjc3NDQ4MjY1OSwidGl0bGUiOiJBcm3DoXJpbyIsInByaWNlIjoiNDQ5In0=',
 'nativeVas': [],
 'isFeatured': False}
```

## Documentation
    OLXBrazil is class used to scrape ad data from http://www.olx.com.br.

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

## License
[MIT](https://github.com/luiseduardobr1/pyolxbrazil/blob/master/LICENSE)

## Sugestions/Problems
Contact us if there are any problems or suggestions for improvement.
