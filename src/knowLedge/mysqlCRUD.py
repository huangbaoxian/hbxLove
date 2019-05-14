from config.Constant import root
from config.Constant import dbPassword
from config.Constant import dbHost
import mysql.connector



conn = mysql.connector.connect(user=root, password=dbPassword, database='db_blog',host=dbHost)
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from db_play.live_paper_record where  period_id=2047')
values = cursor.fetchall()



for x in values:
    print(x[2]);



