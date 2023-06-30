#
# # URL: https://en.aruodas.lt/gyvenamieji-namai/
# # Nuskenuokite nekilnojamojo turto skelbimus iš nekilnojamojo turto svetainės naudodami BeautifulSoup biblioteką.
# # Išskirkite nekilnojamojo turto duomenis, įskaitant kainą, vietą, miegamųjų kambarių skaičių.
# # Įrašykite duomenis į Pandas DataFrame ir juos analizuokite, siekiant nustatyti tendencijas nekilnojamojo turto
# # rinkoje, pavyzdžiui, vidutines kainas skirtingose vietovėse ar populiarius nekilnojamojo turto ypatumus
# #
# # import requests
# # from bs4 import BeautifulSoup
# # import pandas as pd
# # from matplotlib import pyplot as plt
# #
# #
# # url = "https://en.aruodas.lt/gyvenamieji-namai/"
# # response = requests.get(url)
# # content = response.text
# # soup = BeautifulSoup(content, 'html.parser')
# #
# # skelbimai = soup.find_all('div', class_='list-row-v2 object-row selhouse advert')
# # duomenys = []
# # unikalus = set()  #naudoj.unikalioms reiksmems
# # for skelbimai in skelbimai:
# #     kaina = skelbimas.find('span', class_='list-item-price-v2').text.strip()
# #     lokacija = skelbimas.select_one('.list-adress-v2 h3').text.strip()    #h3 teksto dydis, selektorius
# #     plotas = skelbimas.find('div', class_='list-AreaOverall-v2').text.strip()
# #     kaina = ''.join(c for c in kaina if c.isdigit())
# #
# #     unikalus_id = (kaina, lokacija, plotas)
# #
# #     if unikalus_id not in unikalus:
# #         unikalus.add(unikalus_id)
# #
# #         duomenys.append({
# #             'kaina': kaina,
# #             'lokacija': lokacija,
# #             'plotas': plotas
# #         })
# #
# # df = pd.DataFrame(duomenys)
# # print(df)
#
# # ..........................................................
#
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
#import psycopg2
#from db_config import create_table, insert_data, db_params



delay = 2
# Nurodome norimą nekilnojamojo turto svetainę
for i in range(1, 5):
    url = f'https://en.aruodas.lt/gyvenamieji-namai/puslapis/{i}/?FBuildingType=box'
    time.sleep(delay)
# Siunciame užklausą į svetainę ir gauname turinį
    response = requests.get(url)
    content = response.text

    # Inicializuojame BeautifulSoup objektą ir nurodome naudojamą analizės būdą (pvz., 'html.parser')
    soup = BeautifulSoup(content, 'html.parser')

    # Randame visus nekilnojamojo turto skelbimus
    skelbimai = soup.find_all('div', class_='list-row-v2 object-row selhouse advert')

    # Inicializuojame tuščią sąrašą, kuriame bus saugomi nekilnojamojo turto duomenys
    duomenys = []
    unikalus = set()

    # Apsilankome per kiekvieną nekilnojamojo turto skelbimą ir išskirstome reikiamus duomenis
    for skelbimas in skelbimai:
        kaina = skelbimas.find('span', class_='list-item-price-v2').text.strip()
        vieta = skelbimas.select_one('.list-adress-v2 h3').text.strip()
        plotas = skelbimas.find('div', class_='list-AreaOverall-v2 list-detail-v2').text.strip()

        # Pašaliname ne-skaitmeninius simbolius iš kainos
        kaina = ''.join(c for c in kaina if c.isdigit())

        # Patikriname, ar duomenys jau yra sąraše, kad išvengtumėm dublikatų
        unikalus_id = (kaina, vieta, plotas)
        if unikalus_id not in unikalus:
            unikalus.add(unikalus_id)
            duomenys.append({
                'Kaina': kaina,
                'Vieta': vieta,
                'Plotas': plotas
            })

    # Sukuriame Pandas DataFrame iš duomenų sąrašo
    df = pd.DataFrame(duomenys)
    # print(df)
    # df['Kaina'] = pd.to_numeric(df['Kaina'])

    # skelbimu kainu statistika

    # avg_price = df.agg({'Kaina':[mean, min, max, size]})
    # print(avg_price)

    # avg_price_by_location = df.groupby('vieta')[Kaina].mean()
    # print(avg_price_by_location)

    # skelbimu ploto statistika

    # avg_square = df.agg({'Plotas':[mean, min, max, size]})
    # print(avg_square)



    # create_table()
    # insert_data(duomenys)

data_from_db = ikelti
df = pd.DataFrame(data_from_db, columns=['kaina', 'vieta', 'plotas'])
print(df)