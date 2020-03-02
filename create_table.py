from pyathena import connect

cursor = connect(aws_access_key_id='XXXXXXXXXXXXXXXXXXXX',
                 aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                 s3_staging_dir='s3://athenatest1032020/file2-stage/',
                 region_name='us-west-2').cursor()
cursor.execute("CREATE EXTERNAL TABLE IF NOT EXISTS pythenadb.example40 ( slno INT, name STRING, mail STRING) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' WITH SERDEPROPERTIES ('serialization.format' = ',','field.delim' = ',') LOCATION 's3://athenatest1032020/file2/' TBLPROPERTIES ('has_encrypted_data'='false', 'skip.header.line.count'='1')")
print(cursor.description)
print(cursor.fetchall())


