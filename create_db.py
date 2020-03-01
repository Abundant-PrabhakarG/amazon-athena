from pyathena import connect

cursor = connect(aws_access_key_id='AKIAT6ALRAZHH45J6EFH',
                 aws_secret_access_key='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',
                 s3_staging_dir='s3://athenatest1032020/test/',
                 region_name='us-west-2').cursor()
cursor.execute("CREATE database pythenadb")
print(cursor.description)
print(cursor.fetchall())