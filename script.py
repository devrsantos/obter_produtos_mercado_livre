import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

nome_produto = input('Qual produto você deseja? ')

response = requests.get(url_base + nome_produto)

site = BeautifulSoup(response.text, 'html.parser')

lista_produto = site.find_all('li', attrs={'class': 'ui-search-layout__item shops__layout-item'})

for item in lista_produto:
    titulo = item.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})
    link = item.find('a', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-link'})['href']
    preco = item.find('div', attrs={'class': 'ui-search-price__second-line shops__price-second-line'}).find('span', attrs={'class': 'price-tag-fraction'})
    centavos = item.find('div', attrs={'class': 'ui-search-price__second-line shops__price-second-line'}).find('span', attrs={'class': 'price-tag-cents'})
    
    print(f'Titulo do Produto: {titulo.text}')
    print(f'Link do Produto: {link}')
    if centavos:
        print(f'Preco do Produto: R$ {preco.text},{centavos.text}')
    else:
        print(f'Preco do Produto: R$ {preco.text}')
    
    print('\n\n')