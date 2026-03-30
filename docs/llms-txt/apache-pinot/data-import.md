# Source: https://docs.pinot.apache.org/release-0.4.0/basics/data-import.md

# Source: https://docs.pinot.apache.org/release-0.9.0/basics/data-import.md

# Source: https://docs.pinot.apache.org/release-0.10.0/basics/data-import.md

# Source: https://docs.pinot.apache.org/release-0.11.0/basics/data-import.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/data-import.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/data-import.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/data-import.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/data-import.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/data-import.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/data-import.md

# Source: https://docs.pinot.apache.org/release-1.4.0/manage-data/data-import.md

# Source: https://docs.pinot.apache.org/manage-data/data-import.md

# Import Data

There are multiple options for importing data into Apache Pinot™. The pages in this section provide step-by-step instructions for importing records into Pinot, supported by our [plugin architecture](https://docs.pinot.apache.org/developers/plugin-architecture). The intent is to get you up and running with imported data as quickly as possible.

Pinot supports multiple file input formats without needing to change anything other than the file name. Each example imports a ready-made dataset so you can see how things work without needing to find or create your own dataset.

## Pinot Batch Ingestion

These guides show you how to import data from popular big data platforms.

{% content-ref url="data-import/batch-ingestion/spark" %}
[spark](https://docs.pinot.apache.org/manage-data/data-import/batch-ingestion/spark)
{% endcontent-ref %}

{% content-ref url="data-import/batch-ingestion/hadoop" %}
[hadoop](https://docs.pinot.apache.org/manage-data/data-import/batch-ingestion/hadoop)
{% endcontent-ref %}

## Pinot Stream Ingestion

This guide shows you how to import data using stream ingestion from Apache Kafka topics.

{% content-ref url="data-import/pinot-stream-ingestion/import-from-apache-kafka" %}
[import-from-apache-kafka](https://docs.pinot.apache.org/manage-data/data-import/pinot-stream-ingestion/import-from-apache-kafka)
{% endcontent-ref %}

This guide shows you how to import data using stream ingestion with upsert.

{% content-ref url="data-import/upsert-and-dedup/upsert" %}
[upsert](https://docs.pinot.apache.org/manage-data/data-import/upsert-and-dedup/upsert)
{% endcontent-ref %}

This guide shows you how to import data using stream ingestion with deduplication.

{% content-ref url="data-import/upsert-and-dedup/dedup" %}
[dedup](https://docs.pinot.apache.org/manage-data/data-import/upsert-and-dedup/dedup)
{% endcontent-ref %}

This guide shows you how to import data using stream ingestion with CLP.

{% content-ref url="data-import/pinot-stream-ingestion/clp" %}
[clp](https://docs.pinot.apache.org/manage-data/data-import/pinot-stream-ingestion/clp)
{% endcontent-ref %}

## Pinot file systems

By default, Pinot does not come with a storage layer, so all the data sent won't be stored in case of system crash. In order to persistently store the generated segments, you will need to change controller and server configs to add a deep storage. See [File systems](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system) for all the info and related configs.

These guides show you how to import data and persist it in these file systems.

{% content-ref url="data-import/pinot-file-system/amazon-s3" %}
[amazon-s3](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system/amazon-s3)
{% endcontent-ref %}

{% content-ref url="data-import/pinot-file-system/import-from-adls-azure" %}
[import-from-adls-azure](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system/import-from-adls-azure)
{% endcontent-ref %}

{% content-ref url="data-import/pinot-file-system/import-from-gcp" %}
[import-from-gcp](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system/import-from-gcp)
{% endcontent-ref %}

{% content-ref url="data-import/pinot-file-system/import-from-hdfs" %}
[import-from-hdfs](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system/import-from-hdfs)
{% endcontent-ref %}

## Pinot input formats

This guide shows you how to import data from various Pinot-supported input formats.

{% content-ref url="data-import/pinot-input-formats" %}
[pinot-input-formats](https://docs.pinot.apache.org/manage-data/data-import/pinot-input-formats)
{% endcontent-ref %}

This guide shows you how to handle the complex type in the ingested data, such as map and array.

{% content-ref url="data-import/complex-type" %}
[complex-type](https://docs.pinot.apache.org/manage-data/data-import/complex-type)
{% endcontent-ref %}

This guide shows additional examples on how to work with complex types.

{% content-ref url="data-import/complex-type/complex-type-examples" %}
[complex-type-examples](https://docs.pinot.apache.org/manage-data/data-import/complex-type/complex-type-examples)
{% endcontent-ref %}

This guide shows you how to handle records with dynamic schemas, like JSON log events.

{% content-ref url="data-import/schema-conforming-transformer" %}
[schema-conforming-transformer](https://docs.pinot.apache.org/manage-data/data-import/schema-conforming-transformer)
{% endcontent-ref %}

## Reloading and uploading existing Pinot segments

This guide shows you how to reload Pinot segments from your deep store.

{% content-ref url="../operators/tutorials/segment-reload" %}
[segment-reload](https://docs.pinot.apache.org/operators/tutorials/segment-reload)
{% endcontent-ref %}

This guide shows you how to upload Pinot segments from an old, closed Pinot instance.

{% content-ref url="data-import/segment-upload" %}
[segment-upload](https://docs.pinot.apache.org/manage-data/data-import/segment-upload)
{% endcontent-ref %}
