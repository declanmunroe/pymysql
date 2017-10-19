# import pymysql.cursors
import pymysql
#import os (os relates to envirnonment variables. These relate to proctecting my credendtial information such as password
            #and username when uploading to github)

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user='declanmunroe', #user=os.environ.get("C9_USER")
                            password='',
                            db='Chinook')

try:
   with connection.cursor() as cursor:
       sql = "SELECT * FROM `Artist`"
       cursor.execute(sql)
       result = cursor.fetchall()
       print(result)
finally:
   connection.close()