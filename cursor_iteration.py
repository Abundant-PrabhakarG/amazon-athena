from pyathena import connect

cursor = connect(aws_access_key_id='XXXXXXXXXXXXXXXXXXXX',
                 aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                 s3_staging_dir='s3://athenatest1032020/bigfile-stage/',
                 region_name='us-west-2').cursor()
cursor.execute("SELECT * FROM pythenadb.examplebig limit 5000")
for row in cursor:
    print(row)