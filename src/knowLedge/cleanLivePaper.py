# 导入MySQL驱动:

#新增桌面题库答案选项
from config.Constant import root
from config.Constant import dbPassword
from config.Constant import dbHost




import mysql.connector


periodId = ("2047",)
virtualPaperId = ("121552",)

conn = mysql.connector.connect(user=root, password=dbPassword,host=dbHost)
# 运行查询:
cursor = conn.cursor()
sql1 = "update db_play.live_paper set cur_model_id = 0, question_count = 0, status = 0 where period_id = %s"
sql2 = "DELETE FROM db_play.live_paper_record where period_id = %s"
sql3 = "UPDATE `zongjie-tiku`.virtual_paper SET start_time = null, end_time = null where id in (SELECT virtual_paper_id FROM `zongjie-tiku`.real_vitual_paper where paper_id = %s)"
sql4 = "DELETE from `zongjie-tiku`.question_statistic where virtual_paper_id in (SELECT virtual_paper_id FROM `zongjie-tiku`.real_vitual_paper where paper_id = %s)"
sql5 = "DELETE from `zongjie-tiku`.trainning where paper_id in (SELECT virtual_paper_id FROM `zongjie-tiku`.real_vitual_paper where paper_id = %s)"

cursor.execute(sql1,periodId);
cursor.execute(sql2,periodId);
cursor.execute(sql3, virtualPaperId);
cursor.execute(sql4,virtualPaperId);
cursor.execute(sql5,virtualPaperId);

conn.commit();
# 关闭Cursor和Connection:
cursor.close()
conn.close()