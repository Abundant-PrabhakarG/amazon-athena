from pyathena import connect

cursor = connect(aws_access_key_id='XXXXXXXXXXXXXXXXXXXX',
                 aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                 s3_staging_dir='s3://athenatest1032020/test/',
                 region_name='us-west-2').cursor()
cursor.execute("CREATE database pythenadb")
print(cursor.description)
print(cursor.fetchall())