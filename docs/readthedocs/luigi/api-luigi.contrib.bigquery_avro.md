# luigi.contrib.bigquery_avro

Specialized tasks for handling Avro data in BigQuery from GCS.

Classes

`BigQueryLoadAvro`(*args, **kwargs)

A helper for loading specifically Avro data into BigQuery from GCS.

class luigi.contrib.bigquery_avro.BigQueryLoadAvro(**args*, ***kwargs*)

A helper for loading specifically Avro data into BigQuery from GCS.

Copies table level description from Avro schema doc,
BigQuery internally will copy field-level descriptions to the table.

Suitable for use via subclassing: override requires() to return Task(s) that output
to GCS Targets; their paths are expected to be URIs of .avro files or URI prefixes
(GCS “directories”) containing one or many .avro files.

Override output() to return a BigQueryTarget representing the destination table.

source_format = 'AVRO'

source_uris()

The fully-qualified URIs that point to your data in Google Cloud Storage.

Each URI can contain one ‘*’ wildcard character and it must come after the ‘bucket’ name.

run()

The task run method, to be overridden in a subclass.

See Task.run