# Source: https://docs.startree.ai/corecapabilities/query_data/query_interfaces/connect-via-python.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting to StarTree Cloud using Python

Applications can use the Python client library to query StarTree Cloud.

## Prerequisites

1. Ensure you have the latest `pinotdb` library installed. To install the library, run the following command in your terminal:

```
pip install pinotdb
```

1. [Obtain username and password for authentication](#obtaining-username-and-password)

2. [Find your Pinot Broker URL](#finding-your-broker-url)

## Usage

### Query the Pinot Broker Directly

```
from pinotdb import connect

USERNAME = '<your-username>'
PASSWORD = '<your-password>'
BROKER_HOST_URL = 'broker.pinot.<your-url>.startree.cloud'

conn = connect(
    host=f'{USERNAME}:{PASSWORD}@{BROKER_HOST_URL}',
    port=443,
    path='/query/sql', 
    scheme='https'
)
curs = conn.cursor()
curs.execute("select * from myTable limit 10")

for row in curs:
    print(row)
```

### Use SQLAlchemy to Query Pinot

The db engine connection string is formatted like this: `pinot://:?controller=://:/`

```
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *

engine = create_engine('pinot://localhost:8099/query/sql?controller=http://localhost:9000/')  # uses HTTP by default
# engine = create_engine('pinot+http://localhost:8099/query/sql?controller=http://localhost:9000/')
# engine = create_engine('pinot+https://localhost:8099/query/sql?controller=http://localhost:9000/')

places = Table('places', MetaData(bind=engine), autoload=True)
print(select([func.count('*')], from_obj=places).scalar())
```

## Clone the Python pinot-dbapi Repository

```
git clone git@github.com:python-pinot-dbapi/pinot-dbapi.git
cd pinot-dbapi
```

## Obtaining Username and Password

You can cenerate an API token in the [Data Portal](/corecapabilities/security/manage-api-tokens#generating-an-api-token) or using the [REST API](/api-reference/introduction#authentication-%26-prerequisites). Then, [obtain the username and password from the service token](/corecapabilities/security/manage-api-tokens#extracting-username-and-password-from-a-startree-bearer-token)

Th username and password are used to authorize your API requests.

## Finding Your Broker URL

To find the correct Broker URL for your table in StarTree Cloud:

1. Access the Data Portal.
2. Click on **Tables**.
3. Select the specific table you want to query.
4. From the browser address bar, copy the URL to your Pinot cluster. For example, if the URL shown is `https://dp.1abcde6.cp.s7e.startree.cloud/tables`, then the Broker URL for the table will be `broker.pinot.1abcde6.cp.s7e.startree.cloud`.

Built with [Mintlify](https://mintlify.com).
