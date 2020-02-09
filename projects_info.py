import csv
import requests

ACCESS_TOKEN = 'fe75f3bb5c64db4faf2cf99d37c59c6b049a84d5'

def get_infos(owner, name):
    url = 'https://api.github.com/repos/{}/{}?access_token={}'.format(owner, name, ACCESS_TOKEN)
    print(url)
    response = requests.get(url)
    data_all = response.json()

    infos = {}
    infos['owner'] = owner
    infos['name'] = name
    infos['stars'] = data_all['stargazers_count']
    infos['forks'] = data_all['forks_count']

    return infos



def get_writer(file, fieldnames):
    return csv.DictWriter(file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

if __name__ == '__main__':
    data_file = open('data/project_info.csv', 'w')
    writer_data_file = None

    projects_file = open('data/data_filtered.csv', 'r')
    reader_projects = csv.reader(projects_file, delimiter=',')

    for row in reader_projects:
        owner = row[0]
        name = row[1]

        print('Coletando... {} {}'.format(owner, __name__))
        data = get_infos(owner, name)
        
        if not writer_data_file:
            writer_data_file = get_writer(data_file, data.keys())
            writer_data_file.writeheader()
        writer_data_file.writerow(data)
        data_file.flush()

    data_file.close()


