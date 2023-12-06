import mysql.connector

config = {
  'user': 'root',
  'password': 'password',
  'host': '10.100.151.31',
  'database': 'ayush',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()
