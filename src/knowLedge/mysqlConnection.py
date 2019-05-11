
# 安装pip
# 1 sudo easy_install pip
# 2 sudo pip install wheel
# 3 sudo easy_install mysql-connector-python ||  sudo  pip install mysql-connector || pip install mysql-connector-python --allow-external mysql-connector-python
#

# 导入MySQL驱动:
import mysql.connector

from config.Constant import root
from config.Constant import dbPassword
from config.Constant import dbHost

# 注意把password设为你的root口令:
conn = mysql.connector.connect(user=root, password=dbPassword, database='db_blog',host=dbHost)
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from posts')
values = cursor.fetchall()

for item in values:
    print(item)
    print('\n')


# 关闭Cursor和Connection:
cursor.close()
conn.close()





