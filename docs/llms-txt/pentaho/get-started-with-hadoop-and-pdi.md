# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi.md

# Get started with Hadoop and PDI

Pentaho Data Integration (PDI) can operate in two distinct modes: job orchestration and data transformation. Within PDI they are called jobs and transformations.

PDI jobs sequence a set of entries that encapsulate actions. An example of a PDI big data job would be to check for new log files, copy the new files to HDFS, execute a MapReduce task to aggregate the weblog into a click stream, and stage that click stream data in an analytic database.

PDI transformations consist of a set of steps that execute in parallel and operate on a stream of data columns. Through the default Pentaho engine, columns usually flow from one system where new columns are calculated or values are looked up and added to the stream. The data stream is then sent to a receiving system like a Hadoop cluster, a database, or the Pentaho Reporting engine. PDI job entries and transformation steps are described in the **Pentaho Data Integration** document.
