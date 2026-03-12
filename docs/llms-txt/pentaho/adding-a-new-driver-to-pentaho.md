# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/before-you-begin-pentaho-server-to-hadoop-cluster-connection/adding-a-new-driver-to-pentaho.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/adding-a-new-driver-to-pentaho.md

# Adding a new driver

Pentaho connects to Hadoop clusters using a compatibility layer called a driver. These drivers are Apache Karaf archive files (`.kar` format) that connect Pentaho services to Hadoop clusters. You must use a driver to connect each vendor and version of your Hadoop clusters for the following Pentaho products:

* PDI client
* Pentaho Server
* Analyzer
* Interactive Reports
* Pentaho Report Designer (PRD)
* Pentaho Metadata Editor (PME)

Pentaho ships with an Apache Hadoop driver. For specific vendor drivers, visit the [Support Portal](https://support.pentaho.com/hc/en-us) to download the drivers. Install the drivers on the PDI client or [Pentaho Server](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/install-a-driver-for-the-pentaho-server) before using them. See the **Pentaho Data Integration** document for instructions on installinh a driver on the PDI client.

When drivers for new Hadoop versions are released, you can add them to Pentaho, then install them to connect to the new Hadoop distributions.

**CAUTION:**

When you add a driver, it is loaded into the runtime cache. There are several best practices for adding drivers to the runtime cache.

* If you add multiple drivers, you need to allocate 8 to 10 GB of disk space for each driver to your runtime cache.
* If you are running an environment that manages multiple instances (executions) of the PDI engine, then allocate enough space for each runtime cache. For example, environments running 50+ concurrent instances require 75GB or more of cache space during peak processing times.
