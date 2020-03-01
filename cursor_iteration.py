from pyathena import connect

cursor = connect(aws_access_key_id='AKIAT6ALRAZHH45J6EFH',
                 aws_secret_access_key='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',
                 s3_staging_dir='s3://athenatest1032020/bigfile-stage/',
                 region_name='us-west-2').cursor()
cursor.execute("SELECT count(*) FROM pythenadb.examplebig limit 1000")
for row in cursor:
    print(row)