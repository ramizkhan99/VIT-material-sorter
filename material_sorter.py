import os
import pprint
import random

pp = pprint.PrettyPrinter(indent=4)

def get_rank(file_name):
    months = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12
    }
    date = file_name[:11].split('-')
    if len(date) != 3:
        return 0
    date[0] = int(date[0])
    date[2] = int(date[2])
    date[1] = 100 * months[date[1]]
    return  sum(date) 

def sort_by_date(arr):
    ranks = dict()
    for i in arr:
        if get_rank(i) in ranks.keys():
            ranks[get_rank(i) + random.random()] = i
        else:
            ranks[get_rank(i)] = i
    keys = sorted(list(ranks))
    for (i, j) in zip(range(len(keys)), keys):
        if i != 0:
            ranks[i] = ranks.pop(j)
    pp.pprint(ranks)
    return ranks

def rename_files(sorted_files):
    i = 0
    for i in sorted_files.keys():
        if i == 0:
            continue
        os.rename(sorted_files[i], str(i) + '. ' + sorted_files[i][12:])
    print("Done!")

files = os.listdir()
files = list(filter(lambda x: x.split('.')[-1] in ['pdf', 'ppt', 'pptx', 'doc', 'docx'], files))
sorted_files = sort_by_date(files)
rename_files(sorted_files)
