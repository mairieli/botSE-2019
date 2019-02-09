import csv

def read_csv(file):
    input_csv = open('{}'.format(file), 'r')
    reader_csv = csv.reader(input_csv, delimiter=',')

    repos = [{'url': r[1], 'owner': r[2], 'repo': r[3]} for r in reader_csv]
    input_csv.close()
    return repos

def read_csv_repos(file):
    input_csv = open('{}'.format(file), 'r')
    reader_csv = csv.reader(input_csv, delimiter=',')

    repos = [r[1] for r in reader_csv]
    input_csv.close()
    return repos

def read_csv_repos_fil(file):
    input_csv = open('{}'.format(file), 'r')
    reader_csv = csv.reader(input_csv, delimiter=',')

    repos = [r[2] for r in reader_csv]
    input_csv.close()
    return repos