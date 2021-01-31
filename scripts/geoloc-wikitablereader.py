import pandas as pd
import types
from botocore.client import Config
import ibm_boto3

url='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

df=pd.read_html(url, header=0)[0]

df.groupby(['Postal Code','Borough']).Neighbourhood.agg([('Neighbourhood',', '.join)])

df = df[df.Borough != 'Not assigned']
df.loc[df.Neighbourhood == 'Not assigned', 'Neighbourhood'] = df['Borough']

df.shape

def __iter__(self): return 0

# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. It includes your credentials.
# You might want to remove those credentials before you share the notebook.
client_4e4732a63acd4b36bedec4d7f1949809 = ibm_boto3.client(service_name='s3',
    ibm_api_key_id='VUQamRn2vwB45Jv-31F0TxA5b6cpSr7R_YESwCZnXpAB',
    ibm_auth_endpoint="https://iam.cloud.ibm.com/oidc/token",
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.eu-geo.objectstorage.service.networklayer.com')

body = client_4e4732a63acd4b36bedec4d7f1949809.get_object(Bucket='pythonparsing-donotdelete-pr-4ntaizombpepd3',Key='Geospatial_Coordinates.csv')['Body']
# add missing __iter__ method, so pandas accepts body as file-like object
if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )

df_data_1 = pd.read_csv(body)
df_data_1.head()

pd.merge(df, df_data_1, on='Postal Code')
