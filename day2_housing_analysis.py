import MySQLdb
db = MySQLdb.connect(host=”127.0.0.1”, user=”root”, passwd=”TimC00k@123”, db=”houses”)
cur = db.cursor()
cur.execute(“select avg(price) from house_prices;”)
result = cur.fetchone()
print str(result[0])