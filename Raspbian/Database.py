import pymysql


def loadDB(result):
	conn = pymysql.connect(host='test-serv.mysql.database.azure.com', user='rooti',
	password='Threego!!', db='threego', charset='utf8')

	a=[]
	cur = conn.cursor()
	with conn:
		cur.execute("select * from state")
		result = cur.fetchall()
		result = [list(result[i]) for i in range (len(result))]
	return result

	

def updateDB(state, name):
	conn = pymysql.connect(host='test-serv.mysql.database.azure.com', user='rooti',
	password='Threego!!', db='threego', charset='utf8')
	cur = conn.cursor()

	sql = "UPDATE state SET state = %s where name = %s"
	cur.execute(sql, (state, name))
	
	conn.commit()
	conn.close()



