# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert.md

# Source: https://docs.pentaho.com/pdia-data-integration/pentaho-data-integration-plugins/elasticsearch-rest-bulk-insert.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert.md

# Elasticsearch REST bulk insert

This step is available as a separate plugin from the [Pentaho EE Marketplace](https://support.pentaho.com/hc/en-us/categories/200568085-Downloads).

Use the Elasticsearch REST bulk insert step if you have records that you want to submit to an Elasticsearch server for indexing. Elastic® is a platform of products to search, analyze, and visualize data. The Elastic platform includes Elasticsearch, which is a Lucene-based, multi-tenant capable, and distributed search and analytics engine. Use this step to send one or more batches of records to an Elasticsearch server for indexing. Because you can specify the size of a batch, you can use this step to send one, a few, or many records to Elasticsearch for indexing.

When record data flows out of the Elasticsearch REST bulk insert step, PDI sends it to Elasticsearch along with your index as metadata. This step is commonly used when you want to send a batch of data to an Elasticsearch server and create new indexes. You can also use this step to add a batch of data to an index.

For more information on Elasticsearch, see [https://www.elastic.co/guide/en/ElasticSearch/reference/current/index.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html) and <https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html>.
