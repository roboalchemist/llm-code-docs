# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-setup-for-spark.md

# HBase setup for Spark

The [HBase Input](https://github.com/pentaho/documentation/blob/main/PDIA/9.3/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/HBase%20Input%20cp%20\(main%20page\)=GUID-740AAAEF-4522-4C1C-B504-31A5DEE7CC32=3=en=.md) and [HBase Output](https://github.com/pentaho/documentation/blob/main/PDIA/9.3/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/HBase%20Output=GUID-59346D9E-9373-409F-B9A8-8F89D5D7DE5B=3=en=.md) steps can run on Spark with the [Adaptive Execution Layer](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/adaptive-execution-layer-cp-landing-page) (AEL). These steps can be used with the supported versions of Cloudera Distribution for Hadoop (CDH) and Hortonworks Data Platform (HDP). See the **Administer Pentaho Data Integration and Analytics** document for what versions are supported with AEL.To read or write data to HBase, you must have an HBase target table on the cluster. If one does not exist, you can create one using [HBase shell commands](https://learnhbase.wordpress.com/2013/03/02/hbase-shell-commands/).

**Note:** Due to Cloudera limitations, the HBase Input step fails when using the specific configuration of Spark in YARN mode with Kerberos.

This article explains how you can set up the Pentaho Server to run these steps.
