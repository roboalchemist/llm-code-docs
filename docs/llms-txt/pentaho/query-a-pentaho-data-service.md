# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/query-a-pentaho-data-service.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/query-a-pentaho-data-service.md

# Query a Pentaho Data Service

You can use SQL to query a data service. You can also add a conditional statement to the query if the data service transformation uses a parameter. The parameter must be added to the transformation by an ETL developer before the data service was created. See a [Creating a regular or streaming Pentaho Data Service](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/creating-a-regular-or-streaming-pentaho-data-service) for more details. You can then assign a value to the parameter in your query.

To find the name of the table to query, you can connect to the data service, then use explorer to find the name of the table. The name of table is usually the same as the name of the data service.

The Pentaho Data Service has the following limitations:

* There are SQL limitations for queries. See the [Pentaho Data Service SQL support reference and other development considerations](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results/pentaho-data-service-sql-support-reference-and-other-development-considerations) article for more details.
* Although you can use any Pentaho-supported input source, data services can only be queried with SQL.
