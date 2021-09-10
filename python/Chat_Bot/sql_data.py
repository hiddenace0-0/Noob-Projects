import sqlite3
import re

sql = sqlite3.connect('responses.db')

c = sql.cursor()

# c.execute("""CREATE TABLE responses(
#             Num integer,
#             ListOfWords text
#             )""")

def insert_response(response):
    with sql:
        c.execute("INSERT INTO responses VALUES(:Num, :ListOfWords)", {'Num': 1, 'ListOfWords':str(response)})

    
def get_response_by_num():
        with sql:
            c.execute("SELECT * FROM responses WHERE Num=:Num",{'Num': 1})
            ans = c.fetchall()
            # print(ans)
            return ans
def remove_responses(response):
    with sql:
        c.execute("DELETE from responses WHERE ListOfWords = :ListOfWords",{'Num': 1, 'ListOfWords':str(response)})
# remove_responses('i hate you ')
# get_response_by_num()
# c.close()

