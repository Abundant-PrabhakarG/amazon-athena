from pyathena import connect

cursor = connect(aws_access_key_id='XXXXXXXXXXXXXXXXXXXX',
                 aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                 s3_staging_dir='s3://athenatest1032020/file1/',
                 region_name='us-west-2').cursor()
#SELECT count(*) FROM pythenadb.example3 where slno > 5;
#SELECT distinct * FROM pythenadb.example3 where slno > 5;			
#SELECT * FROM pythenadb.example3 where slno > 5;			 
cursor.execute("SELECT distinct mail FROM pythenadb.example40")
print(cursor.description)
print(cursor.fetchall())