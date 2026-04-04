# Source: https://docs.shaped.ai/docs/api/v2

Title: Shaped Docs

URL Source: https://docs.shaped.ai/docs/api/v2

Markdown Content:
Skip to main content
Docs
ShapedQL
API
Playground
Sign up
Search docs
Table
POST
Create Table
PATCH
Update Table
GET
List Tables
POST
Seed Table
GET
List Seed Tables
POST
Table Insert
GET
Get Table Details
DEL
Delete Table
View
POST
Create View
PATCH
Update View
GET
List Views
GET
Get View Details
DEL
Delete View
Engine
POST
Create Engine
PATCH
Update Engine
GET
List Engines
POST
Seed Engine
GET
List Engine Seeds
DEL
Delete Engine
GET
Get Engine Details
Engine Query
POST
Execute Query
GET
List Saved Queries
POST
Execute Saved Query
GET
Get Saved Query Details
Query
POST
Execute global query (ShapedQL data and engine catalog)
Shaped API (2.0.32)

Welcome to Shaped's API reference docs. These provide a detailed view of the endpoints and CLI commands that Shaped provides and brief explanations of how they should be used.

The Shaped API has four main endpoints:

Tables - Provision and manage batch and real-time data connectors.

Views - Configure SQL transformations and AI enrichment on your input data. Use SQL to combine multiple data sources or use an LLM to add new categories, extract specific attributes from descriptions, etc.

Engines - Deploy and manage your relevance engines. The Engine API exposes configuration for indexing logic, input datasets, externam embeddings, and more.

Query - Execute queries against your engines, to return data based on an input query or rerank an existing list. The Query API exposes the retrieve, filter, score, and ranking steps of the 4-stage ranking architecture.

The base URL for each endpoint is: https://api.shaped.ai/v2

Table

Tables store the foundational data for your relevance engines.

Tables are loaded to Shaped through connectors; batch connectors update data every 15 mins while real-time connectors are updated immediately.



Create Table
POST
/tables

Creates a new Table.

Use this endpoint to configure the schema, column structure, and metadata of the table. Use Insert Table Rows to add rows to your table.

If you want to upload a local dataset, use the CLI: shaped create_dataset_from_uri

Schema type: Different sources have different configuration. The schema_type argument specifies the type of table you are creating (Snowflake, SQL, Amplitude, etc).

Unique keys and replication keys: Tables are append-only. In case of duplicates, we use the unique_keys and replication_key attributes to determine the correct value for a record.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters
REQUEST BODY SCHEMA: application/json
required
Any of BigQueryTableConfigMongoDBTableConfigSnowflakeTableConfigAWSPinpointTableConfigCustomTableConfigRedshiftTableConfigPostgresTableConfigMySQLTableConfigMSSQLTableConfigAmplitudeTableConfigSegmentTableConfigRudderstackTableConfigIcebergTableConfigDynamoDBTableConfigShopifyTableConfigKinesisTableConfigPosthogTableConfigClickhouseTableConfigKafkaTableConfig
name
required
	
string (Name)

Unique identifier for the BigQuery dataset.


table
required
	
string (Table)

BigQuery table path in format 'projectID.datasetID.tableID'.


columns
required
	
Array of strings (Columns)

List of column names to sync from table.


datetime_key
required
	
string (Datetime Key)

Column name used for incremental replication. Must be a BigQuery column of type TIMESTAMP, DATETIME, or DATE.


schema_type	
string (Schema Type)
Default: "BIGQUERY"

Schema type discriminator for BigQuery datasets.

Value: "BIGQUERY"

description	
string or null (Description)

Optional description of the dataset.


schedule_interval	
string or null (Schedule Interval)
Default: "@hourly"

Cron expression for sync frequency.


filters	
Array of arrays or null or null (Filters)

Optional SQL WHERE clause filters.


start_datetime	
string or null (Start Datetime)

ISO timestamp for initial data sync start point.


batch_size	
integer or null (Batch Size)

Number of rows to process per batch.


unique_keys	
Array of arrays or null or null (Unique Keys)

Column names used for deduplication in ClickHouse.


service_account_key_json	
string or null (Service Account Key Json)

JSON string of the GCP service account key for the BigQuery connector. This is required for the BigQuery connector to authenticate.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
message
required
	
string (Message)

Confirmation message indicating table creation status.

400 

Invalid credentials

409 

Table already exists

422 

Request schema validation error

504 

Source connection timeout: could not reach your database within the timeout. Verify host, port, firewall, and that the database accepts connections.

Request samples
PayloadFile uploadCLIcURL
Content type
application/json
Example
BigQueryTableConfig
MongoDBTableConfig
SnowflakeTableConfig
AWSPinpointTableConfig
CustomTableConfig
RedshiftTableConfig
PostgresTableConfig
MySQLTableConfig
MSSQLTableConfig
AmplitudeTableConfig
SegmentTableConfig
RudderstackTableConfig
IcebergTableConfig
DynamoDBTableConfig
ShopifyTableConfig
KinesisTableConfig
PosthogTableConfig
ClickhouseTableConfig
KafkaTableConfig
BigQueryTableConfig
Copy
Expand allCollapse all
{
"schema_type": "BIGQUERY",
"name": "string",
"description": "string",
"table": "string",
"columns": 
[
"string"
],
"datetime_key": "string",
"schedule_interval": "@hourly",
"filters": [ ],
"start_datetime": "string",
"batch_size": 0,
"unique_keys": [ ],
"service_account_key_json": "string"
}
Response samples
200400409422504
Content type
application/json
Copy
{
"message": "string"
}
Update Table
PATCH
/tables

Update the config of an existing table.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters
REQUEST BODY SCHEMA: application/json
required
Any of BigQueryTableConfigMongoDBTableConfigSnowflakeTableConfigAWSPinpointTableConfigCustomTableConfigRedshiftTableConfigPostgresTableConfigMySQLTableConfigMSSQLTableConfigAmplitudeTableConfigSegmentTableConfigRudderstackTableConfigIcebergTableConfigDynamoDBTableConfigShopifyTableConfigKinesisTableConfigPosthogTableConfigClickhouseTableConfigKafkaTableConfig
name
required
	
string (Name)

Unique identifier for the BigQuery dataset.


table
required
	
string (Table)

BigQuery table path in format 'projectID.datasetID.tableID'.


columns
required
	
Array of strings (Columns)

List of column names to sync from table.


datetime_key
required
	
string (Datetime Key)

Column name used for incremental replication. Must be a BigQuery column of type TIMESTAMP, DATETIME, or DATE.


schema_type	
string (Schema Type)
Default: "BIGQUERY"

Schema type discriminator for BigQuery datasets.

Value: "BIGQUERY"

description	
string or null (Description)

Optional description of the dataset.


schedule_interval	
string or null (Schedule Interval)
Default: "@hourly"

Cron expression for sync frequency.


filters	
Array of arrays or null or null (Filters)

Optional SQL WHERE clause filters.


start_datetime	
string or null (Start Datetime)

ISO timestamp for initial data sync start point.


batch_size	
integer or null (Batch Size)

Number of rows to process per batch.


unique_keys	
Array of arrays or null or null (Unique Keys)

Column names used for deduplication in ClickHouse.


service_account_key_json	
string or null (Service Account Key Json)

JSON string of the GCP service account key for the BigQuery connector. This is required for the BigQuery connector to authenticate.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
message
required
	
string (Message)

Confirmation message indicating table update status.

400 

Invalid credentials

404 

Table not found

422 

Request schema validation error

504 

Source connection timeout: could not reach your database within the timeout. Verify host, port, firewall, and that the database accepts connections.

Request samples
Content type
application/json
Example
BigQueryTableConfig
MongoDBTableConfig
SnowflakeTableConfig
AWSPinpointTableConfig
CustomTableConfig
RedshiftTableConfig
PostgresTableConfig
MySQLTableConfig
MSSQLTableConfig
AmplitudeTableConfig
SegmentTableConfig
RudderstackTableConfig
IcebergTableConfig
DynamoDBTableConfig
ShopifyTableConfig
KinesisTableConfig
PosthogTableConfig
ClickhouseTableConfig
KafkaTableConfig
BigQueryTableConfig
Copy
Expand allCollapse all
{
"schema_type": "BIGQUERY",
"name": "string",
"description": "string",
"table": "string",
"columns": 
[
"string"
],
"datetime_key": "string",
"schedule_interval": "@hourly",
"filters": [ ],
"start_datetime": "string",
"batch_size": 0,
"unique_keys": [ ],
"service_account_key_json": "string"
}
Response samples
200400404422504
Content type
application/json
Copy
{
"message": "string"
}
List Tables
GET
/tables

List the tables in your account and basic metadata like schema type and status.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
tables
required
	
Array of objects (Tables)

List of tables and their metadata.



Array 
name
required
	
string (Name)

Unique identifier for the table.


uri
required
	
string (Uri)

URI to access the table.


created_at
required
	
string (Created At)

ISO timestamp when the table was created.


schema_type
required
	
string (Schema Type)

Type of table schema (e.g., BIGQUERY).


status
required
	
string (Status)

Current deployment status of the table.


description	
string or null (Description)

Optional description of the table.

422 

Validation Error

Request samples
CLIcURL
Copy
$ shaped list-datasets
Response samples
200422
Content type
application/json
Copy
Expand allCollapse all
{
"tables": 
[
{}
]
}
Seed Table
POST
/tables/seed

Seed a pre-built demo table into your account.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

REQUEST BODY SCHEMA: application/json
required
name
required
	
string (Name) non-empty

Name of the seed table to create.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
name
required
	
string (Name)

Name of the created table.


schema_type
required
	
string (Schema Type)

Type of table schema.

404 

Seed table not found

409 

Table already exists

422 

Validation Error

Request samples
Content type
application/json
Copy
{
"name": "string"
}
Response samples
200404409422
Content type
application/json
Copy
{
"name": "string",
"schema_type": "string"
}
List Seed Tables
GET
/tables/seeds

List available seed tables.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
tables
required
	
Array of objects (Tables)

Available seed tables.



Array 
name
required
	
string (Name)

Table name to pass to seed endpoint.


description
required
	
string (Description)

What this table contains.

422 

Validation Error

Response samples
200422
Content type
application/json
Copy
Expand allCollapse all
{
"tables": 
[
{}
]
}
Table Insert
POST
/tables/{table_name}/insert

Insert dictionary data into Shaped table. The schema must match the schema of the table or it'll throw an error.

Tables are append-only. In case of duplicates, we use the unique_keys and replication_key attributes to determine the correct value for a record.

Batch tables are updated every 15 minutes while real-time tables are updated immediately.

PATH PARAMETERS
table_name
required
	
string (Table Name)

Name of the table to insert data into.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters
REQUEST BODY SCHEMA: application/json
required
data
required
	
Array of objects (Data)
Examples: {"event":"click","item_id":"item1","timestamp":1680116390,"user_id":"user1"}

List of dictionaries representing rows to insert.



Array 
property name*
additional property
	
any
Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
message
required
	
string (Message)

Results of the insert operation.

400 

Rows do not match table schema

404 

Table does not exist

422 

Validation Error

Request samples
PayloadCLIcURL
Content type
application/json
Copy
Expand allCollapse all
{
"data": 
{
"event": "click",
"item_id": "item1",
"timestamp": 1680116390,
"user_id": "user1"
}
}
Response samples
200400404422
Content type
application/json
Copy
{
"message": "string"
}
Get Table Details
GET
/tables/{table_name}

Get detailed information about a table, such as its columns structure and any errors or warnings.

PATH PARAMETERS
table_name
required
	
string (Table Name)

Name of the table to retrieve.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
name
required
	
string (Name)

Unique identifier for the table.


uri
required
	
string (Uri)

URI to access the table.


schema_type
required
	
string (Schema Type)

Type of table schema (e.g., BIGQUERY).


status
required
	
string (TableStatusType)
Enum: "SCHEDULING" "DEPLOYING" "ACTIVE" "INACTIVE" "DESTROYING" "ERROR"

Current deployment status.


created_at
required
	
string <date-time> (Created At)

Timestamp when the table was created.


schema	
object or null (Schema)

Table column names and their corresponding types.


kinesis_stream_arn	
string or null (Kinesis Stream Arn)

ARN of the Kinesis stream for real-time tables.


kinesis_iam_role_arn	
string or null (Kinesis Iam Role Arn)

ARN of the IAM role for Kinesis stream access.


description	
string or null (Description)

Optional description of the table.


error_message	
string or null (Error Message)

Error message if table is in error state.


warning_message	
string or null (Warning Message)

Warning message if there are any warnings.

404 

Invalid Table Name

422 

Validation Error

Request samples
CLIcURL
Copy
$ shaped view-dataset 
  --dataset-name dataset-name
Response samples
200404422
Content type
application/json
Copy
Expand allCollapse all
{
"name": "string",
"uri": "string",
"schema_type": "string",
"schema": { },
"kinesis_stream_arn": "string",
"kinesis_iam_role_arn": "string",
"status": "SCHEDULING",
"description": "string",
"error_message": "string",
"warning_message": "string",
"created_at": "2019-08-24T14:15:22Z"
}
Delete Table
DELETE
/tables/{table_name}

Delete the table with identifier: {table_name}.

PATH PARAMETERS
table_name
required
	
string (Table Name)

Name of the table to delete.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
message
required
	
string (Message)

Confirmation message indicating table deletion status.

404 

Invalid Table Name

422 

Validation Error

Request samples
CLIcURL
Copy
$ shaped delete-dataset 
  --dataset-name dataset-name
Response samples
200404422
Content type
application/json
Copy
{
"message": "string"
}
View

Transform your data into new formats or views using SQL statements or LLM-powered enrichment.

Create View
POST
/views
HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters
REQUEST BODY SCHEMA: application/json
required
Any of SQLViewConfigAIEnrichmentViewConfig
name
required
	
string (Name)

Unique identifier for the SQL transform.


sql_query
required
	
string (Sql Query)

SQL query to execute for the transform.


sql_transform_type
required
	
string (SQLTransformType)
Enum: "VIEW" "MATERIALIZED_VIEW"

Type of SQL transform (VIEW or MATERIALIZED_VIEW).


transform_type	
string (Transform Type)
Default: "SQL"

Transform type discriminator for SQL transforms.

Value: "SQL"

description	
string or null (Description)

Optional description of the transform.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
message
required
	
string (Message)

Confirmation message indicating view creation status.

422 

Validation Error

Request samples
PayloadCLIcURL
Content type
application/json
Example
SQLViewConfig
AIEnrichmentViewConfig
SQLViewConfig
Copy
{
"name": "string",
"transform_type": "SQL",
"description": "string",
"sql_query": "string",
"sql_transform_type": "VIEW"
}
Response samples
200422
Content type
application/json
Copy
{
"message": "string"
}
Update View
PATCH
/views
HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters
REQUEST BODY SCHEMA: application/json
required
Any of SQLViewConfigAIEnrichmentViewConfig
name
required
	
string (Name)

Unique identifier for the SQL transform.


sql_query
required
	
string (Sql Query)

SQL query to execute for the transform.


sql_transform_type
required
	
string (SQLTransformType)
Enum: "VIEW" "MATERIALIZED_VIEW"

Type of SQL transform (VIEW or MATERIALIZED_VIEW).


transform_type	
string (Transform Type)
Default: "SQL"

Transform type discriminator for SQL transforms.

Value: "SQL"

description	
string or null (Description)

Optional description of the transform.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
message
required
	
string (Message)

Confirmation message indicating view update status.

404 

View not found

422 

Validation Error

Request samples
PayloadCLIcURL
Content type
application/json
Example
SQLViewConfig
AIEnrichmentViewConfig
SQLViewConfig
Copy
{
"name": "string",
"transform_type": "SQL",
"description": "string",
"sql_query": "string",
"sql_transform_type": "VIEW"
}
Response samples
200404422
Content type
application/json
Copy
{
"message": "string"
}
List Views
GET
/views

List all views for the authenticated tenant.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
views
required
	
Array of objects (Views)

List of views and their metadata.



Array 
name
required
	
string (Name)

Unique identifier for the view.


uri
required
	
string (Uri)

URI to access the view.


created_at
required
	
string (Created At)

ISO timestamp when view was created.


type
required
	
string (Type)

Type of view (SQL or AI_ENRICHMENT).


status
required
	
string (Status)

Current deployment status of the view.


source_table_names
required
	
Array of strings (Source Table Names)

List of source table names used by this view.


description	
string or null (Description)

Optional description of the view.

422 

Validation Error

Request samples
CLIcURL
Copy
$ shaped list-transforms
Response samples
200422
Content type
application/json
Copy
Expand allCollapse all
{
"views": 
[
{}
]
}
Get View Details
GET
/views/{view_name}

Get detailed information about a specific view.

PATH PARAMETERS
view_name
required
	
string (View Name)

Name of the view to retrieve.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
Any of ViewDetailsSQLViewDetailsAI
name
required
	
string (Name)

Unique identifier for the view.


uri
required
	
string (Uri)

URI to access the view.


status
required
	
string (TransformStatus)
Enum: "ACTIVE" "SCHEDULING" "BACKFILLING" "DESTROYING" "INACTIVE" "ERROR"

Current deployment status.


created_at
required
	
string <date-time> (Created At)

Timestamp when view was created.


source_table_names
required
	
Array of strings (Source Table Names)

List of source table names used by this view.


type
required
	
string (Type)

View type discriminator for SQL views.

Value: "SQL"

schema	
object or null (Schema)

Schema definition mapping column names to value types.


description	
string or null (Description)

Optional description of the view.


error_message	
string or null (Error Message)

Error message if view is in error state.

404 

View not found

422 

Validation Error

Request samples
CLIcURL
Copy
$ shaped view-transform --transform-name transform-name
Response samples
200404422
Content type
application/json
Example
ViewDetailsSQL
ViewDetailsAI
ViewDetailsSQL
Copy
Expand allCollapse all
{
"name": "string",
"uri": "string",
"status": "ACTIVE",
"created_at": "2019-08-24T14:15:22Z",
"schema": { },
"source_table_names": 
[
"string"
],
"description": "string",
"error_message": "string",
"type": "SQL"
}
Delete View
DELETE
/views/{view_name}
PATH PARAMETERS
view_name
required
	
string (View Name)

Name of the view to delete.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
message
required
	
string (Message)

Confirmation message indicating view deletion status.

422 

Validation Error

Request samples
CLIcURL
Copy
$ shaped delete-transform --transform-name transform-name
Response samples
200422
Content type
application/json
Copy
{
"message": "string"
}
Engine

Configure, monitor, and manage the core ranking and retrieval engines in your Shaped account.

Create Engine
POST
/engines

Create Engine creates a retrieval engine that can be used for any down-stream retrieval-search, ranking-recommendation and user-understanding use-case.The create engine endpoint will do some validation of the input request (including verifying connected datasets are active and validating the fetch SQL). It then asynchronously provisions your data pipelines, and training and serving infrastructure. Use the View Engine and List Engines endpoints to view the status of the underlying asynchronous setup request.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

REQUEST BODY SCHEMA: application/json
required
name
required
	
string (Name)

Unique identifier for the engine.


data
required
	
object (DataConfig)

Data preparation workflow configuration.


description	
string or null (Description)

Optional description of the engine.


tags	
object or null (Tags)

Optional key-value tags for organization.


index	
object (IndexConfig)

Index configuration.


training	
object (TrainingConfig)

Model training and evaluation configuration.


deployment	
object (DeploymentConfig)

Inference serving infrastructure configuration.


queries	
object (Queries)

Dictionary of named query definitions (saved queries).


version	
string (Version)
Default: "v2"

API version discriminator for v2 configs.

Value: "v2"
Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
engine_url
required
	
string (Engine Url)

URL to the console run-health monitor for the engine.

400 

Invalid credentials

404 

Table not found

409 

Engine already exists

422 

Request schema validation error

Request samples
PayloadCLIcURL
Content type
application/json
Copy
Expand allCollapse all
{
"name": "string",
"description": "string",
"tags": { },
"data": 
{
"interaction_table": 
{},
"user_table": 
{},
"item_table": 
{},
"schedule": "@hourly",
"schema_override": 
{},
"compute": 
{},
"filters": 
[]
},
"index": 
{
"lexical_search": 
{},
"embeddings": 
[],
"user_column_indices": [ ],
"item_column_indices": [ ]
},
"training": 
{
"schedule": "@once",
"compute": 
{},
"data_split": 
{},
"evaluation": 
{},
"models": 
[],
"tuning": 
{}
},
"deployment": 
{
"data_tier": "fast_tier",
"rollout": 
{},
"autoscaling": 
{},
"pagination": 
{},
"online_store": 
{}
},
"queries": 
{
"property1": 
{},
"property2": 
{}
},
"version": "v2"
}
Response samples
200400404409422
Content type
application/json
Copy
{
"engine_url": "string"
}
Update Engine
PATCH
/engines

Update engine is used to update the configurations of a currently hosted engine within the ERROR or ACTIVE states.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

REQUEST BODY SCHEMA: application/json
required
name
required
	
string (Name)

Unique identifier for the engine.


data
required
	
object (DataConfig)

Data preparation workflow configuration.


description	
string or null (Description)

Optional description of the engine.


tags	
object or null (Tags)

Optional key-value tags for organization.


index	
object (IndexConfig)

Index configuration.


training	
object (TrainingConfig)

Model training and evaluation configuration.


deployment	
object (DeploymentConfig)

Inference serving infrastructure configuration.


queries	
object (Queries)

Dictionary of named query definitions (saved queries).


version	
string (Version)
Default: "v2"

API version discriminator for v2 configs.

Value: "v2"
Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
engine_url
required
	
string (Engine Url)

URL to the console run-health monitor for the engine.

400 

Invalid credentials

404 

Table not found

409 

Engine already exists

422 

Request schema validation error

Request samples
PayloadCLIcURL
Content type
application/json
Copy
Expand allCollapse all
{
"name": "string",
"description": "string",
"tags": { },
"data": 
{
"interaction_table": 
{},
"user_table": 
{},
"item_table": 
{},
"schedule": "@hourly",
"schema_override": 
{},
"compute": 
{},
"filters": 
[]
},
"index": 
{
"lexical_search": 
{},
"embeddings": 
[],
"user_column_indices": [ ],
"item_column_indices": [ ]
},
"training": 
{
"schedule": "@once",
"compute": 
{},
"data_split": 
{},
"evaluation": 
{},
"models": 
[],
"tuning": 
{}
},
"deployment": 
{
"data_tier": "fast_tier",
"rollout": 
{},
"autoscaling": 
{},
"pagination": 
{},
"online_store": 
{}
},
"queries": 
{
"property1": 
{},
"property2": 
{}
},
"version": "v2"
}
Response samples
200400404409422
Content type
application/json
Copy
{
"engine_url": "string"
}
List Engines
GET
/engines

List Engines returns a list of your previously created engines and their associated metadata (e.g. status and last train time).

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
engines
required
	
Array of objects (Engines)

List of engines and their metadata.



Array 
engine_name
required
	
string (Engine Name)

Unique identifier for the engine.


engine_uri
required
	
string (Engine Uri)

URI to access the engine.


created_at
required
	
string (Created At)

Timestamp when the engine was created.


status
required
	
string (Status)

Current status of the engine.


version
required
	
string (Version)

Version of the engine: possible values are 'v1' or 'v2'.


description	
string or null (Description)

Optional description of the engine.


trained_at	
string or null (Trained At)

Timestamp when the engine was last trained.

422 

Validation Error

Request samples
CLIcURL
Copy
$ shaped list-models
Response samples
200422
Content type
application/json
Copy
Expand allCollapse all
{
"engines": 
[
{}
]
}
Seed Engine
POST
/engines/seed

Seed Engine copies a demo engine into your account. Required seed tables must be created first.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

REQUEST BODY SCHEMA: application/json
required
name
required
	
string (Name) non-empty

Name of the seed engine to create.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
name
required
	
string (Name)

Name of the created engine.


status
required
	
string (Status)

Current engine status.

404 

Seed engine not found

409 

Engine already exists or missing tables

422 

Validation Error

Request samples
Content type
application/json
Copy
{
"name": "string"
}
Response samples
200404409422
Content type
application/json
Copy
{
"name": "string",
"status": "string"
}
List Engine Seeds
GET
/engines/seeds

Returns the list of available demo engines that can be seeded.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
engines
required
	
Array of objects (Engines)

Available seed engines.



Array 
name
required
	
string (Name)

Engine name to pass to seed endpoint.


description
required
	
string (Description)

What this engine does.

422 

Validation Error

Response samples
200422
Content type
application/json
Copy
Expand allCollapse all
{
"engines": 
[
{}
]
}
Delete Engine
DELETE
/engines/{engine_name}

Delete the engine with identifier: {engine_name}.

PATH PARAMETERS
engine_name
required
	
string (Engine Name)

Name of the engine to delete.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
message
required
	
string (Message)

Confirmation message indicating the model deletion status.

404 

Invalid Engine Name

422 

Validation Error

Request samples
CLIcURL
Copy
$ shaped delete-model --model-name model-name
Response samples
200404422
Content type
application/json
Copy
{
"message": "string"
}
Get Engine Details
GET
/engines/{engine_name}

View Engines returns detailed information about the given {engine_name} including the input setup schemas details and status.

PATH PARAMETERS
engine_name
required
	
string (Engine Name)

Name of the engine to view.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
engine_uri
required
	
string (Engine Uri)

URI to access the engine.


created_at
required
	
string (Created At)

Timestamp when the engine was created.


status
required
	
string (Status)

Current status of the engine.


config
required
	
object (Config)

Engine configuration details.


engine_schema
required
	
object (EngineSchema)

Schema describing engine features.


error_message	
string or null (Error Message)

Error message if the engine is in an error state.


warning_message	
string or null (Warning Message)

Warning message if there are any warnings.


input_yaml	
string or null (Input Yaml)

Original YAML input used to create the engine.

404 

Invalid Engine Name

422 

Validation Error

Request samples
CLIcURL
Copy
$ shaped view-model 
  --model-name model-name
Response samples
200404422
Content type
application/json
Copy
Expand allCollapse all
{
"engine_uri": "string",
"created_at": "string",
"status": "string",
"config": { },
"engine_schema": 
{
"user": 
[],
"item": 
[],
"interaction": 
[]
},
"error_message": "string",
"warning_message": "string",
"input_yaml": "string"
}
Engine Query

The Query API exposes a set of attributes to run custom retrieval, filtering and ordering logic against your Shaped engines.

We expose two methods for querying:
1) Use the query endpoint directly, for development and experimentation
2) Pass parameters like a user ID or search string to a saved query for execution, to minimize complexity for downstream clients

Execute Query
POST
/engines/{engine_name}/query

Delegate to execute_ad_hoc_query; engine_name is implicit at runtime.

PATH PARAMETERS
engine_name
required
	
string (Engine Name)

Name of the engine to query.

REQUEST BODY SCHEMA: application/json
required
query
required
	
RankQueryConfig (object) or SQLQueryString (string) (Query)

Query configuration or SQL query string. Can be either:

A QueryConfig object defining the retrieval, filtering, scoring, and reordering pipeline. Must include a 'type' field indicating the query type (rank_items, rank_users, rerank_items, etc.).
A SQL query string that will be transpiled to a QueryConfig. Supports a subset of SQL with custom REORDER BY clause.

parameters	
object (Parameters)

Query parameters that can be referenced in the query configuration using $parameter.name syntax. Supports int, float, str, bool, lists of these types, and dictionaries.


return_metadata	
boolean (Return Metadata)
Default: true

Whether to include entity metadata (attributes) in the response. When true, each result includes an 'attributes' field with entity metadata.


return_explanation	
boolean (Return Explanation)
Default: false

Whether to include a detailed explanation of query execution. When true, the response includes an 'explanation' field with information about retrieval, filtering, scoring, and reordering stages.


return_journey_explanations	
boolean (Return Journey Explanations)
Default: false

Whether to include per-entity journey tracking in results. When true, each result includes a 'journey' field showing how that entity moved through the query pipeline.


pagination_key	
string or null (Pagination Key)

Pagination key for retrieving the next page of results. Use the pagination_id from a previous response's explanation to continue pagination.


ignore_pagination	
boolean (Ignore Pagination)
Default: false

Whether to ignore pagination and return results from the beginning. When true, pagination_key is ignored and results start from the first page.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
results
required
	
Array of objects (Results)

List of ranked result entities. Each result contains an id, score, and optionally attributes, embeddings, and journey tracking. Results are ordered by score (descending) after all pipeline stages.


entity_type	
string or null (Entity Type)

Type of entities in the results. One of 'item', 'user', or 'attribute'. Indicates what kind of entities are being ranked.


explanation	
QueryExplanation (object) or null

Detailed explanation of query execution. Includes information about retrieval, filtering, scoring, and reordering stages. Only included if return_explanation is true in the request.

422 

Validation Error

Request samples
PayloadcURL
Content type
application/json
Copy
Expand allCollapse all
{
"parameters": 
{
"property1": 0,
"property2": 0
},
"query": 
{
"columns": [ ],
"embeddings": [ ],
"retrieve": 
[],
"filter": [ ],
"score": 
{},
"reorder": 
[],
"limit": 0,
"type": "rank",
"from": "user"
},
"return_metadata": true,
"return_explanation": false,
"return_journey_explanations": false,
"pagination_key": "string",
"ignore_pagination": false
}
Response samples
200422
Content type
application/json
Copy
Expand allCollapse all
{
"results": 
[
{}
],
"entity_type": "string",
"explanation": 
{
"query_name": "string",
"query_type": "string",
"parameters": { },
"pagination_id": "string",
"retrieve_stage": 
{},
"filter_stage": 
{},
"score_stage": 
{},
"reorder_stage": 
{},
"total_execution_time_ms": 0,
"final_result_count": 0,
"limit_applied": 0,
"inner_uid": 0,
"outer_uid": "string"
}
}
List Saved Queries
GET
/engines/{engine_name}/queries

Delegate to list_saved_queries; engine_name is implicit at runtime.

PATH PARAMETERS
engine_name
required
	
string (Engine Name)

Name of the engine to query.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
queries
required
	
Array of strings (Queries)

List of available saved query names.

422 

Validation Error

Response samples
200422
Content type
application/json
Copy
Expand allCollapse all
{
"queries": 
[
"string"
]
}
Execute Saved Query
POST
/engines/{engine_name}/queries/{query_name}

Delegate to execute_saved_query; engine_name is implicit at runtime.

PATH PARAMETERS
engine_name
required
	
string (Engine Name)

Name of the engine to query.


query_name
required
	
string (Query Name)
REQUEST BODY SCHEMA: application/json
required
parameters	
object (Parameters)

Query parameters that can be referenced in the saved query configuration using $parameter.name syntax. Supports int, float, str, bool, and lists of these types.


return_metadata	
boolean (Return Metadata)
Default: true

Whether to include entity metadata (attributes) in the response. When true, each result includes an 'attributes' field with entity metadata.


return_explanation	
boolean (Return Explanation)
Default: false

Whether to include a detailed explanation of query execution. When true, the response includes an 'explanation' field with information about retrieval, filtering, scoring, and reordering stages.


return_journey_explanations	
boolean (Return Journey Explanations)
Default: false

Whether to include per-entity journey tracking in results. When true, each result includes a 'journey' field showing how that entity moved through the query pipeline.


pagination_key	
string or null (Pagination Key)

Pagination key for retrieving the next page of results. Use the pagination_id from a previous response's explanation to continue pagination.


ignore_pagination	
boolean (Ignore Pagination)
Default: false

Whether to ignore pagination and return results from the beginning. When true, pagination_key is ignored and results start from the first page.

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
results
required
	
Array of objects (Results)

List of ranked result entities. Each result contains an id, score, and optionally attributes, embeddings, and journey tracking. Results are ordered by score (descending) after all pipeline stages.


entity_type	
string or null (Entity Type)

Type of entities in the results. One of 'item', 'user', or 'attribute'. Indicates what kind of entities are being ranked.


explanation	
QueryExplanation (object) or null

Detailed explanation of query execution. Includes information about retrieval, filtering, scoring, and reordering stages. Only included if return_explanation is true in the request.

422 

Validation Error

Request samples
Content type
application/json
Copy
Expand allCollapse all
{
"parameters": 
{
"property1": 0,
"property2": 0
},
"return_metadata": true,
"return_explanation": false,
"return_journey_explanations": false,
"pagination_key": "string",
"ignore_pagination": false
}
Response samples
200422
Content type
application/json
Copy
Expand allCollapse all
{
"results": 
[
{}
],
"entity_type": "string",
"explanation": 
{
"query_name": "string",
"query_type": "string",
"parameters": { },
"pagination_id": "string",
"retrieve_stage": 
{},
"filter_stage": 
{},
"score_stage": 
{},
"reorder_stage": 
{},
"total_execution_time_ms": 0,
"final_result_count": 0,
"limit_applied": 0,
"inner_uid": 0,
"outer_uid": "string"
}
}
Get Saved Query Details
GET
/engines/{engine_name}/queries/{query_name}

Delegate to get_saved_query_info; engine_name is implicit at runtime.

PATH PARAMETERS
engine_name
required
	
string (Engine Name)

Name of the engine to query.


query_name
required
	
string (Query Name)
Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
name
required
	
string (Name)

The name of the saved query.


params
required
	
Array of strings (Params)

List of parameter names that this query accepts.


query	
string or null (Query)

The actual query configuration as YAML string (or SQL string if originally SQL).


query_type	
string or null (Query Type)

The type of query: 'sql' for SQL queries, 'yaml' for YAML/QueryConfig queries.

422 

Validation Error

Response samples
200422
Content type
application/json
Copy
Expand allCollapse all
{
"name": "string",
"params": 
[
"string"
],
"query": "string",
"query_type": "string"
}
Query

Execute a global SQL query (ShapedQL) against your data and engine catalog. Use FROM data.table_name or engine.engine_name.similarity(...) etc.

Execute global query (ShapedQL data and engine catalog)
POST
/query

Execute a global SQL query. Supports data.* (tables, views, data.engine_name.items) and engine.* (proxied to the engine endpoint). Use FROM data.table_name or FROM engine.engine_name.similarity(...) etc.

HEADER PARAMETERS
x-api-key
required
	
string (X-Api-Key) = 40 characters

API key for authentication.

REQUEST BODY SCHEMA: application/json
required
query
required
	
string (Query)

SQL query (e.g. SELECT * FROM data.my_table LIMIT 5)


parameters	
object or null (Parameters)

Optional parameters for the query (reserved for future use)

Responses
200 

Successful Response

RESPONSE SCHEMA: application/json
any
400 

Bad request (mixed namespaces or invalid FROM)

401 

Read-write API key required (read-only key not allowed).

404 

Table, view, or engine not found

422 

Invalid SQL

502 

Engine proxy failed (bad gateway)

504 

Engine query timeout

Request samples
PayloadcURL
Content type
application/json
Copy
Expand allCollapse all
{
"query": "string",
"parameters": { }
}
Response samples
200400401404422502504
Content type
application/json
Copy
null
