import unicodecsv as uc
from pprint import pprint
from datetime import datetime as dt



with open("D:\\Computer Science\\Python\\udacity\\data\\enrollments.csv","rb") as f:
    reader = uc.DictReader(f)
    enrolls = list(reader)

pprint(enrolls[0])


with open("D:\\Computer Science\\Python\\udacity\\data\\daily_engagement.csv","rb") as f1:
    reader1 = uc.DictReader(f1)
    daily_eng = list(reader1)

print("this is second")
pprint(daily_eng[0])

with open("D:\\Computer Science\\Python\\udacity\\data\\project_submissions.csv","rb") as f2:
    reader2 = uc.DictReader(f2)
    proj_sub = list(reader2)


def read_csv(filename):
    with open(filename,'rb') as f:
        reader = uc.DictReader(f)
        return list(reader)

project_subfile0 = read_csv("D:\\Computer Science\\Python\\udacity\\data\\project_submissions.csv")
print("this is third")
pprint(project_subfile0[0])



project_subfile1 = read_csv("D:\\Computer Science\\Python\\udacity\\data\\project_submissions.csv")
print("this is forth")
pprint(project_subfile1[1])

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

for enroll in enrolls:
    enroll['cancel_date'] = parse_date(enroll['cancel_date'])
    enroll['days_to_cancel'] = parse_maybe_int(enroll['days_to_cancel'])
    enroll['is_canceled'] = enroll['is_canceled'] == 'True'
    enroll['is_udacity'] = enroll['is_udacity'] == 'True'
    enroll['join_date'] = parse_date(enroll['join_date'])

pprint(enrolls[0])
