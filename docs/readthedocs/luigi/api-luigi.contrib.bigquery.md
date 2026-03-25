# luigi.contrib.bigquery

Functions

`is_error_5xx`(err)

Classes

`BQDataset`(project_id, dataset_id, location)

Create new instance of BQDataset(project_id, dataset_id, location)

`BQTable`(project_id, dataset_id, table_id, ...)

Create new instance of BQTable(project_id, dataset_id, table_id, location)

`BigQueryClient`([oauth_credentials, ...])

A client for Google BigQuery.

`BigQueryCreateViewTask`(*args, **kwargs)

Creates (or updates) a view in BigQuery.

`BigQueryExtractTask`(*args, **kwargs)

Extracts (unloads) a table from BigQuery to GCS.

`BigQueryLoadTask`(*args, **kwargs)

Load data into BigQuery from GCS.

`BigQueryRunQueryTask`(*args, **kwargs)

`BigQueryTarget`(project_id, dataset_id, table_id)

`BigqueryClient`

`BigqueryCreateViewTask`

`BigqueryLoadTask`

`BigqueryRunQueryTask`

`BigqueryTarget`

`Compression`()

`CreateDisposition`()

`DestinationFormat`()

`Encoding`()

[Optional] The character encoding of the data.

`ExternalBigQueryTask`(*args, **kwargs)

An external task for a BigQuery target.

`ExternalBigqueryTask`

`FieldDelimiter`()

The separator for fields in a CSV file.

`MixinBigQueryBulkComplete`()

Allows to efficiently check if a range of BigQueryTargets are complete.

`MixinBigqueryBulkComplete`

`PrintHeader`()

`QueryMode`()

`SourceFormat`()

`WriteDisposition`()

Exceptions

`BigQueryExecutionError`(job_id, error_message)

luigi.contrib.bigquery.is_error_5xx(*err*)

class luigi.contrib.bigquery.CreateDisposition

CREATE_IF_NEEDED = 'CREATE_IF_NEEDED'

CREATE_NEVER = 'CREATE_NEVER'

class luigi.contrib.bigquery.WriteDisposition

WRITE_TRUNCATE = 'WRITE_TRUNCATE'

WRITE_APPEND = 'WRITE_APPEND'

WRITE_EMPTY = 'WRITE_EMPTY'

class luigi.contrib.bigquery.QueryMode

INTERACTIVE = 'INTERACTIVE'

BATCH = 'BATCH'

class luigi.contrib.bigquery.SourceFormat

AVRO = 'AVRO'

CSV = 'CSV'

DATASTORE_BACKUP = 'DATASTORE_BACKUP'

NEWLINE_DELIMITED_JSON = 'NEWLINE_DELIMITED_JSON'

PARQUET = 'PARQUET'

class luigi.contrib.bigquery.FieldDelimiter

The separator for fields in a CSV file. The separator can be any ISO-8859-1 single-byte character.
To use a character in the range 128-255, you must encode the character as UTF8.
BigQuery converts the string to ISO-8859-1 encoding, and then uses the
first byte of the encoded string to split the data in its raw, binary state.
BigQuery also supports the escape sequence “        “ to specify a tab separator.
The default value is a comma (‘,’).

https://cloud.google.com/bigquery/docs/reference/v2/jobs#configuration.load

COMMA = ','

TAB = '\t'

PIPE = '|'

class luigi.contrib.bigquery.PrintHeader

TRUE = True

FALSE = False

class luigi.contrib.bigquery.DestinationFormat

AVRO = 'AVRO'

CSV = 'CSV'

NEWLINE_DELIMITED_JSON = 'NEWLINE_DELIMITED_JSON'

class luigi.contrib.bigquery.Compression

GZIP = 'GZIP'

NONE = 'NONE'

class luigi.contrib.bigquery.Encoding

[Optional] The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. The default value is UTF-8.

BigQuery decodes the data after the raw, binary data has been split using the values of the quote and fieldDelimiter properties.

UTF_8 = 'UTF-8'

ISO_8859_1 = 'ISO-8859-1'

class luigi.contrib.bigquery.BQDataset(*project_id*, *dataset_id*, *location*)

Create new instance of BQDataset(project_id, dataset_id, location)

dataset_id

Alias for field number 1

location

Alias for field number 2

project_id

Alias for field number 0

class luigi.contrib.bigquery.BQTable(*project_id*, *dataset_id*, *table_id*, *location*)

Create new instance of BQTable(project_id, dataset_id, table_id, location)

property dataset

property uri

class luigi.contrib.bigquery.BigQueryClient(*oauth_credentials=None*, *descriptor=''*, *http_=None*)

A client for Google BigQuery.

For details of how authentication and the descriptor work, see the
documentation for the GCS client. The descriptor URL for BigQuery is
https://www.googleapis.com/discovery/v1/apis/bigquery/v2/rest

dataset_exists(*dataset*)

Returns whether the given dataset exists.
If regional location is specified for the dataset, that is also checked
to be compatible with the remote dataset, otherwise an exception is thrown.

param dataset:

type dataset:

BQDataset