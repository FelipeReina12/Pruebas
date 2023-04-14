import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

def organize_by_country(data):
    countries = {}
    for company in data:
        country = company['country']
        if country not in countries:
            countries[country] = []
        countries[country].append(company)
    return countries

if __name__ == '__main__':
    data = read_csv('data.csv')
    organized_data = organize_by_country(data)
    print(organized_data)
