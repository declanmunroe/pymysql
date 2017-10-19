# import pymysql.cursors
import pymysql


# Connect to the database
connection = pymysql.connect(host='localhost',
                            user='declanmunroe',
                            password='',
                            db='Chinook')
                            
"""
DictCursor specifies that you want your output in dictionary format for example
"""

try:
   with connection.cursor(pymysql.cursors.DictCursor) as cursor:
       sql = "SELECT * FROM `Genre`"
       cursor.execute(sql)
       rows = cursor.fetchall()
       for row in rows: #looping through a list with dictionary objects inside
           print(row)
finally:
   connection.close()