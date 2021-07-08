# Add the functions in this file
import json
import math 

def load_journal(file_name):
    f = open(file_name,)
    datas = json.load(f)
    f.close()
    return datas

def compute_phi(file_name, event):
    datas = load_journal(file_name)
    n11 = n00 = n10 = n01 = n1p = n0p = np1 = np0 = 0
    for data in datas:
        if event in data['events']:
            n1p = n1p + 1
            if data['squirrel']:
                n11 = n11 + 1
                np1 = np1 + 1
            else:
                n10 = n10 + 1
                np0 = np0 + 1
        else:
            n0p = n0p + 1
            if data['squirrel']:
                n01 = n01 + 1
                np1 = np1 + 1
            else:
                n00 = n00 + 1
                np0 = np0 + 1
    return (n11 * n00 - n10 * n01) / math.sqrt(n1p * n0p * np1 * np0)

def compute_correlations(file_name):
    datas = load_journal(file_name)
    map = {}
    for data in datas:
        for event in data['events']:
            if event not in map.keys():
                map[event] = 0
    for event in map.keys():
        map[event] = compute_phi(file_name, event)
    return map

def diagnose(file_name):
    map = compute_correlations(file_name)
    map =  list(sorted(map.items(), key=lambda item: item[1]))
    return (map[len(map)-1][0], map[0][0])


if __name__ == '__main__':
    print(diagnose('journal.json'))