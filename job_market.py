import pandas as pd
import requests
from bs4 import BeautifulSoup
#
# def scrap_job_listings():
#     job_listings = []
#     #urls = ['https://www.cvbankas.lt/', 'https://www.cv.lt/', 'https://www.cvmarket.lt/', 'https://www.cvonline.lt/lt/']
#     websites = [{
#         'url': 'https://www.cvbankas.lt/'
#         'job_listing_selector': 'div#js_id_id_job_ad_list',
#         'title': 'h3.list_h3',
#         'company': 'span.heading_secondary',
#         'location': 'span.list_city',
#         'salary': 'span.salary_amount'
#         },
#         {'url': 'https://www.cv.lt/darbas',
#         'job_listing_selector': 'main.col-xs-12.col-12.col-lg-8.main-content',
#         'title': 'button.title',
#         'company': 'span.company',
#         'location': 'span.company',
#         'salary': 'span.salary'
#          }
#     ]
#
#     for website in websites:
#         url = website['url']
#         response = requests.get(url)
#
#         soup = BeautifulSoup(response.text, 'html.parser')
#         job_elements = soup.select(website['job_listing_selector'])
#         for job_element in job_elements:
#             title = job_element.select_one(website['title']).text.strip()
#             company = job_element.select_one(website['company']).text.strip()
#             location = job_element.select_one(website['location']).text.strip()
#             city = location[:1]
#             salary = job_element.select_one(website['salary']).text.strip()
#             job_listings.append({
#                 'Title': title,
#                 'Company': company,
#                 'Location': city,
#                 'Salary': salary
#             })
#
#     return job_listings
#
# job_listings = scrap_job_listings()
# data = pd.DataFrame(job_listings)
#
# print(data)

# Modesto

def scrape_job_listings():
    job_listing = []

    websites = [
        {
            'url': 'https://www.cvbankas.lt',
            'job_listing_selector': 'div#js_id_id_job_ad_list',
            'title': 'h3.list_h3',
            'company': 'span.heading_secondary',
            'location': 'span.list_city',
            'salary': 'span.salary_amount'
        },
        {
            'url': 'https://www.cv.lt/darbas',
            'job_listing_selector': 'main.col-xs-12.col-12.col-lg-8.main-content',
            'title': 'button.title',
            'company': 'span.company',
            'location': 'span.company',
            'salary': 'span.salary'
        }
    ]

    for website in websites:
        url = website['url']
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        job_elements = soup.select(website['job_listing_selector'], limit=1000)

        for job_element in job_elements:
            title_elements = job_element.select(website['title'])
            titles = [element.text.strip() for element in title_elements]
            title = '\n'.join(titles)

            company_elements = job_element.select(website['company'])
            companies = [element.text.strip() for element in company_elements]
            company = '\n'.join(companies)

            location_elements = job_element.select(website['location'])
            locations = [element.text.strip() for element in location_elements]
            location = '\n'.join(locations)

            salary_elements = job_element.select(website['salary'])
            salaries = [element.text.strip() for element in salary_elements]
            salary = '\n'.join(salaries)

            job_listing.append({
                'Title': title,
                'Company': company,
                'Location': location,
                'Salary': salary
            })

    return job_listing


job_listings = scrape_job_listings()
df = pd.DataFrame(job_listings)
df.to_csv('job_listings.csv', index=False)
print('Data successfully scraped and saved to "job_listings.csv".')
