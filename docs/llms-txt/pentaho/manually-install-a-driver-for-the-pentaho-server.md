# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/manually-install-a-driver-for-the-pentaho-server.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/manually-install-a-driver-for-the-pentaho-server.md

# Manually install a driver for the Pentaho Server

You can manually install a driver for the Pentaho Server, even when you are not connected to the Pentaho Server with the PDI client. This task assumes that you have downloaded your driver from the [Support Portal](https://support.pentaho.com/hc/en-us) or that you are using the Apache Hadoop driver that is shipped with Pentaho.

Perform the following steps to manually install a driver for the Pentaho Server :

1. Navigate to the directory where you downloaded your `.kar` file from the [Support Portal](https://support.pentaho.com/hc/en-us).
2. Select the driver (`.kar` file) you want to add and copy it to the `<pentaho home>/server/pentaho-server/pentaho-solutions/drivers` directory on the machine with the Pentaho Server.

   The vendor distribution files contain their abbreviations in the `.kar` file names as shown below:

   * Amazon EMR (emr)
   * Azure HDInsight (hdi)
   * Cloudera Data Platform (cdp)
   * Google Dataproc (dataproc)
3. Restart the Pentaho Server.
