
import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 指定
MONTH = '200001'
CSV_FILE = '../assets/numbers4/{0}.csv'.format(MONTH) 

# CSVファイル
# アウトプット情報
output = open(CSV_FILE, mode='r')


# firebase
cred = credentials.Certificate("millions-c0b31-firebase-adminsdk-terte-7c0d2a2204.json")
firebase_admin.initialize_app(cred)

# firestore
# コレクション取得
db = firestore.client()

# CSVファイル
# 読み込み
data = []
with open(CSV_FILE) as f:
    reader = csv.reader(f)
    for row in reader:
        date = row[1].replace('/', '')
        params = {
            date: {
                # 回号
                u'no': row[0].replace('第', '').replace('回', ''), # data[0] (int)
                # 抽選日
                u'date': row[1], # data[1] (str)
                # 抽選数字
                u'figure': {
                    u'num1': int(row[2]), # data[2] (int)
                    u'num2': str(row[2])  # data[2] (str)
                },
                # 結果
                u'result': {
                    # ストレート
                    u'straight': {
                        u'num': row[3].replace('口', ''), # data[3] (int)
                        u'price': row[4].replace('円', '') # data[3] (str)

                    },
                    # ボックス
                    u'box': {
                        u'num': row[5].replace('口', ''), # data[4] (int)
                        u'price': row[6].replace('円', '') # data[5] (str)

                    },
                    # セット
                    u'set': {
                        u'straight': {
                            u'num': row[7].replace('口', ''), # data[6] (int)
                            u'price': row[8].replace('円', '') # data[7] (str)
                        },
                        u'box': {
                            u'num': row[9].replace('口', ''), # data[8] (int)
                            u'price': row[10].replace('円', '') # data[9] (str)
                        },
                    },
                    # # ミニ
                    # u'mini': {
                    #     u'num': row[11].replace('口', ''), # data[10] (int)
                    #     u'price': row[12].replace('円', '') # data[11] (str)
                    # }
                },
            }
        }
        data.append(params)


for _i in range(0, len(data)):
    print(data[_i])
    db.collection(u'numbers4').document(MONTH).update(data[_i])

print('{0} end'.format(MONTH))