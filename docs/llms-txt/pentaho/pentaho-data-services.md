# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services.md

# Pentaho Data Services

Prototyping a data model can be time consuming, particularly when it involves setting up databases, creating the data model and setting up a data warehouse, then negotiating accesses so that analysts can visualize the data and provide feedback.

One way to streamline this process is to make the output of a [transformation](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/basic-concepts-of-pdi) step a Pentaho Data Service. The output of the transformation step is exposed by the data service so that the output data can be queried as if it were stored in a physical table, even though the results of the transformation are not stored in a physical database. Instead, results are published to the Pentaho Server as a virtual table.

**Note:** You must have a Pentaho Server and repository to publish the data service.

The virtual table is a JDBC-compliant data source that you and others can connect to or query with SQL, provided they can access the server and the transformation. The Pentaho Data Service can be connected to or queried by a JDBC-compliant tool such as Pentaho Report Designer, Pentaho Interactive Reports, and CTools as well as other compatible tools like RStudio, DBVisualizer, or SQuirreL.

The Pentaho Data Service can also be used in some instances where building and maintaining a data warehouse is sometimes impractical or inefficient, especially when you need to quickly blend and visualize fast-moving or quickly evolving data sets on the fly. For example, if you want to compare your product prices with your competitors, you can create a transformation that blends prices from your in-house data sources and competitor prices. Then, you can convert the output step in the transformation into a Pentaho Data Service that creates a virtual table for querying when you connect to the Pentaho Server. You or others can connect to and query the virtual table, as you would any other JDBC data source to visualize the results in Analyzer or another tool.

The Pentaho Data Service also has a testing tool. This tool generates several logs and reports that you can use to refine the data service and determine where to apply specialized optimizations. You can also define parameters that others can use to pose customized queries. For example, you can create a data service that publishes a virtual “fact” table of a moderately-sized research dataset to a Pentaho Server. You can test and add optimizations and parameters, such as gender or test type so that the data service runs more quickly. Then, you can share connection and parameter information with a group of researchers, who can query the virtual table. Researchers can use Pentaho Interactive Reporting, a dashboard created with CTools, or an application of their choice, such as RStudio, to analyze and visualize the research dataset.

Pentaho Data Services support a subset of SQL. For more details on what is supported, see [Pentaho Data Service SQL support reference and other development considerations](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results/pentaho-data-service-sql-support-reference-and-other-development-considerations). Also, see Components reference in the **Try Pentaho Data Integration and Analytics** document for a complete list of traditional supported data sources.

**Note:** Pentaho Data Services must be installed as part of the Pentaho Data Integration Hadoop add-on. For more information, see the **Install Pentaho Data Integration and Analytics** document.
