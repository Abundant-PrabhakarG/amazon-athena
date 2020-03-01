from pyathena import connect

cursor = connect(aws_access_key_id='AKIAT6ALRAZHH45J6EFH',
                 aws_secret_access_key='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',
                 s3_staging_dir='s3://athenatest1032020/bigfile-stage/',
                 region_name='us-west-2').cursor()
cursor.execute("CREATE EXTERNAL TABLE IF NOT EXISTS pythenadb.examplebig ( Year INT, Age INT, Ethnic INT, Sex INT, Area STRING, count STRING) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' WITH SERDEPROPERTIES ('serialization.format' = ',','field.delim' = ',') LOCATION 's3://athenatest1032020/bigfile/' TBLPROPERTIES ('has_encrypted_data'='false', 'skip.header.line.count'='1')")
print(cursor.description)
print(cursor.fetchall())

