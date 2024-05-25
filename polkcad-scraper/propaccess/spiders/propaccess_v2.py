# Use this scraper when product url is already available
import pandas as pd
import scrapy
from bs4 import BeautifulSoup


urls = pd.read_csv('polkcad_urls.csv')
url_list = urls.url.tolist()


def extract_table_data(table):
    data = []
    try:
        for row in table.find_all("tr"):
            row_data = []
            for cell in row.find_all(["th", "td"]):
                row_data.append(cell.text.strip())
            if row_data:
                data.append(row_data)

        result = {data[0][i]: [row[i] for row in data[1:]] for i in range(len(data[0]))}
        return result
    except:
        return {}


def sum_values(data_dict, col):
    col_values = data_dict.get(col)
    if not col_values:
        return ''

    total_sum = 0
    for value in col_values:
        value = value.replace('$', '').replace(',', '').strip()
        try:
            total_sum += float(value)
        except:
            pass

    return total_sum


class PropaccessV2Spider(scrapy.Spider):
    name = "propaccess_v2"
    start_urls = url_list[:10]

    def parse(self, response, **kwargs):
        land_table = BeautifulSoup(response.text, 'html.parser').select_one('div#landDetails table')
        table_data_dict = extract_table_data(land_table)
        # print(table_data_dict)
        total_acers = sum_values(table_data_dict, 'Acres')

        yield {
            'Property ID': response.css('td:contains("Property ID:") + td::text').get(),
            'Owner Name': response.css('td:contains("Name:") + td::text').get(),
            'Market Value': response.css('td:contains("Market Value:") + td + td::text').get(),
            # 'Owner Address': "".join(response.css('td:contains("Mailing Address:") + td *::text').getall()),
            '% Ownership:': response.css('td:contains("% Ownership:") + td::text').get(),
            'Zoning:': response.css('td:contains("Zoning:") + td::text').get(),
            'Size/Acres': total_acers,
            'url': response.url,
        }

