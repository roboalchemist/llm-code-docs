# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert/before-you-begin-elasticsearch-rest-bulk-insert.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/elasticsearch-rest-bulk-insert/before-you-begin-elasticsearch-rest-bulk-insert.md

# Before you begin

Before you begin, gather the following items:

* The Elasticsearch REST bulk insert plugin. For installation details, see [Install plugins](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-the-pentaho-marketplace-to-manage-plugins/install-plugins).
* A working server with Elasticsearch version 7.x or 8.x installed or create a SaaS offering for your Elasticsearch server. You should be able to connect to Elasticsearch from the computer running PDI.

  **Note:** As a best practice, use compatibility mode when connecting to Elasticsearch 8.x with older clients, see [Connecting to Elasticsearch v8.x using the v7.17.x client](https://www.elastic.co/guide/en/elasticsearch/client/net-api/7.17/connecting-to-elasticsearch-v8.html) for details.
* Privileges to create, insert, and update on the directories that you need to access on the Elasticsearch server.
* Files or data that you want Elasticsearch to index.
