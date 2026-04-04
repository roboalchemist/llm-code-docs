# Source: https://docs.pentaho.com/whats-new/10.2-whats-new/pentaho-ee-marketplace-plugins-release-notes.md

# Pentaho EE Marketplace Plugins

The plug-ins listed on this page are available from the [Support Portal](https://support.pentaho.com/home) home page.

## Pentaho 10.0.2

You can use the Salesforce bulk operation step plug-in for bulk operations on Salesforce objects. This step can significantly increase performance of Salesforce operations.

With the Bulk load into Databricks job entry, you can load large amounts of data from files in your cloud accounts into Databricks tables.

## Pentaho 10.0.1

You can use the new Google Analytics v4 plug-in to generate reports and populate your data warehouse.

A new Hitachi Data Connector for SAP and Business Warehouse plug-in is available. This new plug-in is the ideal Pentaho Data Integration plug-in to use SAP data in your data integration work flows. It enables the querying and extraction of complex and nested SAP structures. The plug-in supports both full and incremental (delta) load scenarios and bi-directional (read from and write to SAP) transfers. In addition, it integrates with SAP security allowing you to manage access within your existing setup. For more information, ask your customer support representative.

## Pentaho 10.0

The Elasticsearch REST Bulk Insert step now supports Elasticsearch version 8 and has been made available as a Pentaho EE Marketplace plug-in.

## Pentaho 9.5

For the Pentaho EE 9.5 GA release, two new plugins were released as part of the Pentaho EE Marketplace Plugin release with new features to improve your data management operations. The plugins are available from the [Support Portal](https://support.pentaho.com/home) home page. Sign into the portal using the Pentaho support username and password provided in your Pentaho Welcome Packet. The plugins are:

* A hierarchical data plugin that adds five new steps for working with hierarchical data.
* A Kafka streaming plugin that enhances the Kafka consumer and producer steps and adds a **Kafka Offset** job with the ability to reset the offset.

## Hierarchical data type steps

Pentaho has added an hierarchical data type, and has five new steps for processing structured, complex, and nested data types. This new data type is supported in steps in previous releases of Pentaho that can handle hierarchical data. These five new steps consist of the following:

* **Hierarchical JSON Input**

  This step accepts a JSON file or JSONL from a previous step or a file location and converts it into a hierarchical object.
* **Hierarchical JSON Output**

  This step accepts hierarchical data from a previous step and converts it into a JSON formatted string. 
* **Extract to Rows**

  This step parses hierarchical data from input steps.
* **Modify values from a single row**

  This step modifies the hierarchical data using incoming columns or create hierarchical data output to another step.
* **Modify values from grouped rows**

  This step builds complex hierarchical data or group data based on a field.

The last three steps are used within the transformation flow for interacting with the hierarchical data type structure in-place, without needing to flatten the data to a row structure.​

## Kafka Improvements

A new job entry called Kafka Offset has been added to enable you to change the offset of a topic partition. This Job entry has fields to connect to a Kafka broker or cluster in the **Setup** and **Options** tabs.

The following improvements have been made to the Kafka Consumer and Kafka Producer steps:

* Encryption is supported for connection parameters.
* SSL and Kerberos (SASL) connectivity have been certified.
* You can now use variables from Kettle properties, PDI environment variables. and parameter variables in the Kafka properties settings on the **Options** tab.
* The Kafka client library has been upgraded to 3.4.0.
* Logging has been improved to make debugging easier.
* Improved the Kafka consumer step to consume messages until the time stamp set using the **Offset Settings** tab in the Kafka Offset job.
* An offset rebalancer has been added to correctly commit offsets if a rebalance occurs when a new consumer is added or an existing consumer removed from the consumer group.
