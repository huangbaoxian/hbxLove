
# 安装pip
# 1 sudo easy_install pip
# 2 sudo pip install wheel
# 3 sudo easy_install mysql-connector-python ||  sudo  pip install mysql-connector || pip install mysql-connector-python --allow-external mysql-connector-python
#

# 导入MySQL驱动:
import mysql.connector

# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='fladsjf12@110UQ', database='db_test',host='47.104.172.172')
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from users')
values = cursor.fetchall()
print(values);
# 关闭Cursor和Connection:
cursor.close()
conn.close()





