import json

class JsonIterator:

    def __init__(self, file_path):
        with open(file_path) as file:
            countries_data = json.load(file)
            country = (country['name']['common'] for country in countries_data)
            self.country_iter = iter(country)

    def __iter__(self):
        return self

    def __next__(self):
        country = next(self.country_iter)
        return country


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/'
    with open('links.txt', 'w', encoding='utf-8') as file_r:
        for country_name in JsonIterator('countries.json'):
            file_r.write(f'{country_name} - {url}{country_name}\n')
