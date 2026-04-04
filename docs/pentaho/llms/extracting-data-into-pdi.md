# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi.md

# Extracting data into PDI

Connect Pentaho Data Integration (PDI) to databases, file systems, clusters, and other data sources, and configure advanced options for integration.

* [Defining PDI database connections](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/defining-pdi-database-connections)

  You can use Pentaho Data Integration (PDI) to access data from various databases. You
  \
  must connect to the database before accessing its records. You define database connections
  \
  in PDI through the Database Connection dialog box.
* [Edit database connections in PDI](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/edit-database-connections-in-pdi)

  Once a connection has been established, you can open the Database Connection dialog box to refine and change aspects of the connection.
* [Specify advanced configuration of PDI database connections](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/specify-advanced-configuration-of-pdi-database-connections)

  Use the **Advanced** option in the Database Connection dialog box to configure properties associated with how SQL is generated. With these properties, you can set a standard across all your SQL tools, ETL tools, and design tools.
* [Quoting PDI database connections](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/quoting-pdi-database-connections)

  Pentaho uses a database-specific quoting system. With this system, you can use any name or character that complies with the supported databases' naming conventions.
* [Set specific options for PDI database connections](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/set-specific-options-for-pdi-database-connections)

  Use the **Advanced** option in the Database Connection dialog box to configure properties associated with how SQL is generated. With these properties, you can set a standard across all your SQL tools, ETL tools, and design tools.
* [Define PDI database connection pooling](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/define-pdi-database-connection-pooling)

  You can use the **Pooling** option in the Database Connection dialog box to set up a connection pool and define options like the initial pool size, maximum pool size, and connection pool parameters. By default, a connection remains open for each individual report or set of reports in PUC and for each individual step in a transformation in PDI.
* [Connect to clusters (PDI only)](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connect-to-clusters-pdi-only)

  Use the **Clustering** options in the Database Connection dialog box to cluster the database connection and create connections to data partitions in PDI.&#x20;
* [Modify connections from PDI](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/modify-connections-from-pdi)

  Access other database-related connection tasks in PDI by right-clicking on the connection name in the **View** tab of the **Explorer** pane.
* [PDI and Hitachi Content Platform (HCP)](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/pdi-and-hitachi-content-platform-hcp)

  Hitachi Content Platform (HCP) is the distributed, fixed-content, data storage system from Hitachi Vantara. HCP provides a scalable, easy-to-use repository that can accommodate all types of data, from simple text files to medical images to multigigabyte database images.
* [Hierarchical data](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/hierarchical-data)

  Pentaho supports a hierarchical data type (HDT) by means of the Pentaho EE Marketplace hierarchical data type plugin that adds the data type and creates five steps. These steps are designed to simplify string manipulation, with the ability to convert between HDT fields and formatted strings.
* [PDI and Snowflake](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/pdi-and-snowflake-cp)

  Snowflake is an analytic data warehouse running completely on a cloud infrastructure. Snowflake supports loading popular data formats like JSON, Avro, Parquet, ORC, and XML. Using Pentaho Data Integration (PDI), you can load your data into Snowflake and define jobs in PDI to efficiently orchestrate warehouse operations, paying only for the storage and computing resources actually used when you use them.&#x20;
* [Copybook steps in PDI](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/copybook-steps-in-pdi-cp)

  Pentaho Data Integration supports simplified integration with fixed-length records in binary mainframe data files, so more users can ingest, integrate, and blend mainframe data as part of their data integration pipelines. This capability is critical if your business relies on massive amounts of customer and transactional datasets generated in mainframes that you want to search and query to create reports.
* [Work with the Streamlined Data Refinery](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery)

  The Streamlined Data Refinery (SDR) is a simplified and specific ETL refinery composed of a series of Pentaho Data Integration (PDI) jobs that take raw data, augment and blend it through the request form, and then publish it for report designers to use in Analyzer.
* [Connecting to a Hadoop cluster with the PDI client](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article)

  To connect to a Hadoop cluster, you must access a driver, create a named connection, then configure and test the connection.&#x20;
* [Connecting to Virtual File Systems](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/virtual-file-system-browser)

  You can connect to most Virtual File Systems (VFS) through VFS connections in PDI. A VFS connection is a stored set of VFS properties that you can use to connect to a specific file system.&#x20;
* [Streaming analytics](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/streaming-analytics)

  With streaming analytics, you can constantly perform statistical analysis while moving within a data stream.
* [Web services steps](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/web-services-steps)

  PDI jobs and transformations can interact with a variety of Web services through specialized steps. How you use these steps, and which ones you use, is largely determined by your definition of Web services.&#x20;
