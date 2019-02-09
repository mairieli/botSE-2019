import pandas as pd
import numpy as np
import re

def search(regex, code):
    if type(code) is str:
        attribute = re.search(regex, code)
        if attribute:
            return attribute.group(0)
    return None

def findall(regex, code):
    if type(code) is str:
        attribute = re.findall(regex, code)
        if attribute:
            return attribute
    return None

def parse_attributes(df):
    code = df['source_code']

    days_until_stale = search('(?<=daysUntilStale:) \d+', code)
    days_until_close = search('(?<=daysUntilClose:) \d+', code)
    stale_label = search('(?<=staleLabel:) \w+', code)

    return df['owner'], df['project_name'], days_until_stale, days_until_close, stale_label

def parse_exempt_labels(df):
    code = df['source_code']

    exempt_labels = findall(r'(?<= - )[-\w]+[ \w]*(?=\\n)', code)

    return df['owner'], df['project_name'], exempt_labels

if __name__ == "__main__":
    df = pd.read_csv("project_bot.csv", sep=";") 
    attr = pd.DataFrame(pd.np.empty((0, 3249))), columns=['A']) 

    attr["owner"] = attr["project_name"] = attr["days_until_stale"] = attr["days_until_close"] = attr["stale_label"] = ""

    attr[['owner', 'project_name', 'days_until_stale', 'days_until_close', 'stale_label']] = list(df.apply(parse_attributes, axis=1))
    attr.to_csv("atributos.csv", sep=';', index=False)

    exempt_labels = pd.DataFrame(np.random.randint(10, size=(3249,1)), columns=['A']) 
    exempt_labels["owner"] = exempt_labels["project_name"] = exempt_labels["exempt_labels"] = ""

    exempt_labels[['owner', 'project_name', 'exempt_labels']] = list(df.apply(parse_exempt_labels, axis=1))
    exempt_labels.to_csv("labels.csv", sep=';', index=False)