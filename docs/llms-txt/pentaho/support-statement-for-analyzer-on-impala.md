# Source: https://docs.pentaho.com/install/9.3-install/components-reference/support-statement-for-analyzer-on-impala.md

# Support statement for Analyzer on Impala

These are the minimum requirements for Analyzer to work with Impala:

* Pentaho 7.1 or later
* Cloudera CDH5.x, CDH 6.1, Impala 1.3.x or later
* Recommend using Parquet compressed file format for tables in Impala
* Recommendations for the Hive and Simba drivers. The driver to use depends on the following scenarios:

  | Scenario                                       | Recommended Driver                                                                                                     |
  | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
  | Pentaho 8.3 or later with the CDH 5.14 shim    | [Impala JDBC Connector 2.5.43 Cloudera](https://www.cloudera.com/downloads/connectors/impala/jdbc/2-5-43.html) driver. |
  | Pentaho 8.3 or later with the CDH 6.1 driver   | [Impala JDBC Connector 2.6.4. Cloudera](https://www.cloudera.com/downloads/connectors/impala/jdbc/2-6-4.html) driver.  |
  | Pentaho 9.0 or later with the CDH 6.1 driver   | [Impala JDBC Connector 2.6.4. Cloudera](https://www.cloudera.com/downloads/connectors/impala/jdbc/2-6-4.html) driver.  |
  | Pentaho 9.1 or later with the CDP 7.1.4 driver | [Impala JDBC Connector 2.6.4. Cloudera](https://www.cloudera.com/downloads/connectors/impala/jdbc/2-6-4.html) driver.  |
* Make sure that the JDBC driver is dropped into the Pentaho Server and Schema Workbench directories. See the **Install Pentaho Data Integration and Analytics** document for details.
* Turn off connection pooling in Pentaho Server.
* Set global order by limit in Cloudera manager.
* In Mondrian schemas, divide dimension tables with high cardinality into several levels

**Note:** As with any data source, the performance of Pentaho Analyzer on Impala will be dependent upon the data shape, Impala’s configuration, and the types of queries. See the best practice, "Pentaho Analyzer with Impala as a Data Source" located at: [https://support.pentaho.com/hc/en-us/articles/208652846](https://support.pentaho.com/hc/en-us/articles/360002913871-Big-Data-and-Pentaho) or download the [PDF](https://support.pentaho.com/hc/en-us/article_attachments/360012191711/Pentaho_Analyzer_and_Impala_Data_Source_Settings_and_Recommendations.pdf).

There are some compiled Mondrian automated test suite results for Analyzer on Impala with OEM Simba, as well as the community Apache Hive driver:

* [Analyzer on Impala with OEM Simba](http://wiki.pentaho.com/display/analysis/PA_CR_PA-3.7.0.0-752_impalad-1.3.0_simba-2.5.2)
* [Analyzer on Impala with community Apache Hive driver](http://wiki.pentaho.com/display/analysis/PA_CR_PA-3.7.0.0-752_impalad-1.3.0)
