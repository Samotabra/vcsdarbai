import numpy as np
import products as products
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

# Rugiles
# delay = 2

# url = "https://pigu.lt/lt/"

# response = requests.get(url)

# # tikriname ar uzklausa buvo sekminga
# if response.status_code == 200:
#     #print("status code: " + str(response.status_code))
#     content = response.content
#     soup = BeautifulSoup(response.content, 'html.parser')
#     category_links = soup.find_all('atag', class_='department-link')


#     categories = []
#     prices = []
#     counter = 0   #sis kodas reikalingas, kai apsirasinesim salyga nustatytam skaiciui.

#     for link in category_links:
#         category_url = link['href']                 # pagal 'href' zinos, kad tai linkas
#         category_name = link.text.strip()

#         category_response = requests.get(category_url)
#         category_content = category_response.content
#         category_soup = BeautifulSoup(category_content, 'html.parser')
#         product_price = category_soup.find_all('div', class_='product-price')
#         product_name = category_soup.find_all('p', class_='product-name')

#         # reikia for, kuris eis per prod.kainas ir jas prides i musu list su kategorijomis.

#         for price, name in zip(product_price, product_name):

#             numeric_price = re.sub('[^0-9]','',price.text.strip())
#             prices.append(numeric_price)
#             categories.append(category_name)
#             products.append(name.text.strip())

#             counter += 1

#             # if patikrina ar musu counter pasieke 1000
#             if counter == 1000:
#                 break

#         if counter == 1000:
#             break

# df = pd.DataFrame({
#     'kategorija': categories,
#     'pavadinimas': products,
#     'kaina': prices
#     })

# df['kaina'] = pd.to_numeric(df['kaina'])
# print(df)

# df_sorted = df.sort_values(by='kaina', ascending=False)

# print(df_sorted)    # YRA KLAIDU
 #...................................................

#  is Modesto.

delay = 2

url = "https://pigu.lt/lt/"

# Send a request to the page
response = requests.get(url)

 # Check if the request was successful
if response.status_code == 200:

    # Get the page content
    content = response.content

    # Create a BeautifulSoup object
    soup = BeautifulSoup(content, 'html.parser')

    # Find the category links
    category_links = soup.find_all('atag', class_='department-link')

    # Initialize lists to store data
    prices = []
    categories = []
    product_names = []
    counter = 0   #sis kodas reikalingas, kai apsirasinesim salyga nustatytam skaiciui.

    # Iterate over category links
     for link in category_links[:10]:
         category_url = f"https://pigu.lt/lt/{link['href']}"                 # pagal 'href' zinos, kad tai linkas
         category_name = link.text.strip()

         # Send a request to the category page
         category_response = requests.get(category_url)
         category_content = category_response.content
         category_soup = BeautifulSoup(category_content, 'html.parser')

         # Find the product prices in the category page
         product_price = category_soup.find_all('div', class_='product-price')
         product_name = category_soup.find_all('p', class_='product-name')

         # Extract the prices and append them to the list
         for price, name in zip(product_price, product_name):

            # Remove non numeric characters from the price using regex
            numeric_price = re.sub('[^0-9]', '',price.text.strip())
            prices.append(numeric_price)
            categories.append(category_name)
            products_names.append(name.text.strip())

            counter += 1

            # Check if the counter reaches 1000
            if counter == 1000:
                break

        # Brake out of the loop if the counter reaches 1000
        if counter == 10:
            break

    # Create a pandas DataFrame with the category, price and name columns

    df = pd.DataFrame({'Kategorija': categories, 'Kaina': prices, 'Produkto pavadinimas': product_names})

    # replace empty strings with  a default value
    df['Kaina'].replace('', 0, inplace=True)

    # # Replace non-finite values (NA or inf) with a default value
    df['Kaina'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)

    # # Convert the Kaina column to float with two decimal places
    df['Kaina'] = df['Kaina'].astype(float).round(2)

    # Calculate the average price for each category
    average_prices = df.groupby('Kategorija')['Kaina'].mean().sort_values(ascending=False)
    print(average_prices)

    # Plot the bar chart of average prices by category
    # average_prices.plot(kind='bar')

    # Show the chart
    # plt.show()

else:
    print('Failed to retrieve page data.')

