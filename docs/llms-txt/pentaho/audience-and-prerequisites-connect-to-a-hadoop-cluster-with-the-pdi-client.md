# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/audience-and-prerequisites-connect-to-a-hadoop-cluster-with-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/audience-and-prerequisites-connect-to-a-hadoop-cluster-with-the-pdi-client.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/audience-and-prerequisites-connect-to-a-hadoop-cluster-with-the-pdi-client.md

# Audience and prerequisites

The audience for this article is ETL developers, data engineers, and data analysts.

Before you begin, verify that the Hadoop administrator has set up your user account on the cluster and granted permissions to access the applicable HDFS directories. You need access to the home directory and any other directories required for the tasks.

Pentaho ships with a default Apache Hadoop driver already installed. Supported versions of other drivers, including Amazon EMR, Apache Vanilla, Cloudera (CDP), and Google Dataproc, must be downloaded from the [Support Portal](https://support.pentaho.com/hc/en-us). You must have a driver for each vendor of Hadoop for connecting to each cluster, which should be preinstalled and available for selection before adding a cluster connection.

* To install a driver for the PDI client, see [Install a driver for the PDI client](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article/install-a-driver-for-the-pdi-client).

When drivers for new Hadoop versions are released, you can download them from the [Support Portal](https://support.pentaho.com/hc/en-us) and then add them to Pentaho to connect to the new Hadoop distributions. Install these drivers using the procedure specified in the **Install Pentaho Data Integration and Analytics** document.

Verify that the Hadoop administrator has configured the Pentaho Server to connect to the Hadoop cluster on the computer. Ask the Hadoop administrator to provide you with a copy of the `site.xml` files from the cluster and the following information:

* Distribution and version of the cluster.
* IP addresses and port numbers for HDFS, JobTracker, and Zookeeper (if used).
* Kerberos and cluster credentials if you are connecting to a secured cluster.
* Oozie URL (if used).
