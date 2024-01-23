## TO-DO: update the following bucket name to match the name of your S3 bucket and un-comment it:
#
airflow variables set s3_bucket data-pipelines-398321749864
#
## TO-DO: un-comment the below line:
#
airflow variables set s3_prefix data-pipelines

## TO-DO: run the follwing command and observe the JSON output:
airflow connections get redshift -o json

[{"id": "2", "conn_id": "redshift", "conn_type": "redshift", "description": "", "host": "default-workgroup.398321749864.us-east-1.redshift-serverless.amazonaws.com:5439/dev", "schema": "dev", "login": "patri-ariflow", "password": "R3dsh1ft", "port": "5439", "is_encrypted": "False", "is_extra_encrypted": "False", "extra_dejson": {}, "get_uri": "redshift://patri-ariflow:R3dsh1ft@default-workgroup.398321749864.us-east-1.redshift-serverless.amazonaws.com%3A5439%2Fdev:5439/dev?__extra__=%7B%7D"}]
