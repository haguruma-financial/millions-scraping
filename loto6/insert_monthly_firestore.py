
import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 指定
MONTH = '201409'
CSV_FILE = '../assets/loto6/{0}.csv'.format(MONTH) 

# 忘れずに
# 201902
# 201409

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
                    u'num1': row[2],  # data[2] (str)
                    u'num2': row[3],  # data[3] (str)
                    u'num3': row[4],  # data[4] (str)
                    u'num4': row[5],  # data[5] (str)
                    u'num5': row[6],  # data[5] (str)
                    u'num6': row[7],  # data[7] (str)
                    u'bonus': row[8]# data[8] (str)
                },
                # 結果
                u'result': {
                    # ストレート
                    u'top1': {
                        u'num': row[14].replace('口', ''), # data[14] (int)
                        u'price': row[15].replace('円', '') # data[15] (str)

                    },
                    u'top2': {
                        u'num': row[16].replace('口', ''), # data[16] (int)
                        u'price': row[17].replace('円', '') # data[17] (str)

                    },
                    u'top3': {
                        u'num': row[18].replace('口', ''), # data[18] (int)
                        u'price': row[19].replace('円', '') # data[19] (str)

                    },
                    u'top4': {
                        u'num': row[20].replace('口', ''), # data[20] (int)
                        u'price': row[21].replace('円', '') # data[21] (str)

                    },
                    u'top5': {
                        u'num': row[22].replace('口', ''), # data[22] (int)
                        u'price': row[23].replace('円', '') # data[23] (str)

                    },
                    u'carry_over': row[24].replace('円', '') # data[24]
                },
            }
        }
        data.append(params)


for _i in range(0, len(data)):
    print(data[_i])
    db.collection(u'loto6').document(MONTH).update(data[_i])

print('{0} end'.format(MONTH))