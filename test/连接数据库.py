import pymysql
db = pymysql.Connect(host="localhost",port=3306,user="root",passwd="123",db="spider",charset="utf8")
cursor=db.cursor()
sql = "insert into phone (name,phone) values ('警察局','110')"
cursor.execute(sql)
db.commit()
db.close()
