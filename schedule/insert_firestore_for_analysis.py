
import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 指定
# ナンバーズ3
NUMBERS3 = {
    u'date': "20200120",
    u'week': { u'no': '1', u'ja': '月' },
    u'old_week': "先勝",
    u'no': "5350",
    u'start_time': 1579273200,
    u'end_time': 1579507200,
}

# ナンバーズ4
NUMBERS4 = {
    u'date': "20200120",
    u'week': { u'no': '1', u'ja': '月' },
    u'old_week': "先勝",
    u'no': "5350",
    u'start_time': 1579273200,
    u'end_time': 1579507200,
}

# ロト6
LOTO6 = {
    u'date': "20200120",
    u'week': { u'no': '1', u'ja': '月' },
    u'old_week': "先勝",
    u'no': "1449",
    u'start_time': 1579273200,
    u'end_time': 1579507200,
}


# firebase
cred = credentials.Certificate("millions-c0b31-firebase-adminsdk-terte-7c0d2a2204.json")
firebase_admin.initialize_app(cred)

# firestore
# コレクション取得
db = firestore.client()


data = {
    u'numbers3': NUMBERS3,
    u'numbers4': NUMBERS4,
    u'loto6': LOTO6
}

db.collection(u'available').document(u'analysis').update(data)

print('end')