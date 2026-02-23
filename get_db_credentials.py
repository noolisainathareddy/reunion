
import json
import boto3

def get_db_pass():
    session = boto3.session.Session(profile_name="root")
    client = session.client(
        service_name= 'secretsmanager',
        region_name = 'us-east-1'
    )

    try:
        get_secret_val = client.get_secret_value(
            SecretId = "postgres_password"
        )
        val = json.loads(get_secret_val['SecretString'])
        return val['postgrespassword']
    except Exception as e:
        print(e)

db_pass = get_db_pass()