from pyathena import connect

cursor = connect(aws_access_key_id='XXXXXXXXXXXXXXXXXXXX',
                 aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                 s3_staging_dir='s3://athenatest1032020/bigfile-stage/',
                 region_name='us-west-2').cursor()
#SELECT count(*) FROM pythenadb.example3 where slno > 5;
#SELECT distinct * FROM pythenadb.example3 where slno > 5;			
#SELECT * FROM pythenadb.example3 where slno > 5;		
#SELECT distinct count FROM pythenadb.examplebig limit 1000	 
cursor.execute("SELECT * FROM pythenadb.examplebig limit 5000")
print(cursor.description)
print(cursor.fetchall())