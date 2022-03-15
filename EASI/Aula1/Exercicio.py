import requests
import bs4
import lxml

result = requests.get('https://pt.wikipedia.org/wiki/Faculdade_de_Tecnologia_do_Estado_de_S%C3%A3o_Paulo')
soup = bs4.BeautifulSoup(result.text, 'lxml')

paragraph = soup.select('p')
cont = 0
palavra = 'Fatec'

print("\n")
print(len(paragraph))
for i in paragraph:
    #print(i.text)
    if palavra in i.text:
        #print('\n')
        #print('\033[31m*******************')
        #print(f'         {(i.text).count(palavra)}')
        #print('*******************\033[0;0m')

        cont += (i.text).count(palavra)

print(f'\033[32mA palavra {palavra} aparece {cont} vezes\033[0;0m')
print("\n")
