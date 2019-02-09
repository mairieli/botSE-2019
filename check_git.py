import iocsv
import csv
import requests

repos = iocsv.read_csv_repos("projects.csv")

out = open('checked_projects.csv', 'w')
w_out = csv.writer(out)

def get(url):
    try:
        response = requests.get(url)
        if response.status_code is 200:
            return True
        return False
    except:
        return False

if __name__ == "__main__":

    for r in repos:
        line = [r, "False"]
        if get(r):
            line = [r, "True"]
        w_out.writerow(line)
        out.flush()
    out.close()