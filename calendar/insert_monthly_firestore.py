import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 指定
MONTH = '202001'

CSV_FILE_NUMERS3 = '../assets/numbers3/{0}.csv'.format(MONTH) 
CSV_FILE_NUMERS4 = '../assets/numbers4/{0}.csv'.format(MONTH) 
CSV_FILE_LOTO6   = '../assets/loto6/{0}.csv'.format(MONTH) 


# firebase
cred = credentials.Certificate("millions-c0b31-firebase-adminsdk-terte-7c0d2a2204.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {}

# ナンバーズ3
with open(CSV_FILE_NUMERS3) as f:
    reader = csv.reader(f)
    for row in reader:
        date = row[1].replace('/', '')
        data[date] = {
            u'numbers3': {
                u'no': row[0].replace('第', '').replace('回', ''),
                u'num': str(row[2])
            }
        }

# ナンバーズ4
with open(CSV_FILE_NUMERS4) as f:
    reader = csv.reader(f)
    for row in reader:
        date = row[1].replace('/', '')
        data[date]['numbers4'] = {
            u'no': row[0].replace('第', '').replace('回', ''),
            u'num': str(row[2])
        }

# ロト6
with open(CSV_FILE_LOTO6) as f:
    reader = csv.reader(f)
    for row in reader:
        date = row[1].replace('/', '')
        data[date]['loto6'] = {
            u'no': row[0].replace('第', '').replace('回', ''),
            u'num': [
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8]
            ]
        }
#         # ~ 200406
#         data[date] = {
#             u'loto6': {
#                 u'no': row[0].replace('第', '').replace('回', ''),
#                 u'num': [
#                     row[2],
#                     row[3],
#                     row[4],
#                     row[5],
#                     row[6],
#                     row[7],
#                     row[8]
#                 ]
#             }
#         }


lock = []
for _k, _v in data.items():
    lock.append({ _k: _v })


for _i in range(0, len(lock)):
    print(lock[_i])
    db.collection(u'calendar').document(MONTH).update(lock[_i])

print('end')