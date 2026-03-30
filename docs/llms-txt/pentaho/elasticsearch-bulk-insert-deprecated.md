# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-bulk-insert-deprecated.md

# ElasticSearch Bulk Insert (deprecated)

**Important:** This documentation applies to an earlier version of the step based on Elasticsearch transport client, version 6.4.2, which is deprecated. While the step will continue to be compatible with transformations created in Pentaho version 9.2 and earlier, you should use the [Elasticsearch REST Bulk Insert](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert) step in your new transformations.

Elastic is a platform that consists of products that search, analyze, and visualize data. The Elastic platform includes ElasticSearch, which is a Lucene-based, multi-tenant capable, and distributed search and analytics engine. The ElasticSearch Bulk Insert step sends one or more batches of records to an ElasticSearch server for indexing. Because you can specify the size of a batch, you can use this step to send one, a few, or many records to ElasticSearch for indexing.

Use this step if you have records that you want to submit to an ElasticSearch server to be indexed. When record data flows out of the ElasticSearch Bulk Insert step, PDI sends it to ElasticSearch along with metadata that you indicate such as the index and type. This step is commonly used when you want to send a batch of data to an ElasticSearch server and create new indexes of a certain type (category). It is also used when you want to add a batch of data to an index or category.

Because this is an output step, it is often placed at the end of the transformation.

**Note:** Since ElasticSearch has a REST web interface you can also use the **REST Client** step to send data to an ElasticSearch server and to perform other REST functions.
