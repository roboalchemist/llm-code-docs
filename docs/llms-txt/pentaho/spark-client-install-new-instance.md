# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/before-you-begin/spark-client-cp/spark-client-install-new-instance.md

# Install a new instance of the Spark client

If you do not have a supported Spark client installed, you need to install your own instance. Perform the following steps:

1. Download the Spark client from the following location to the machine where you will run the AEL daemon: <http://spark.apache.org/downloads.html>

   As a best practice, use Apache Spark client 2.3 or 2.4. Version 2.3 is used in the following examples.

   For example, download `spark-2.3.0-bin-hadoop2.7.tgz` if you are using Spark 2.3 on Hadoop 2.7
2. Extract the downloaded TGZ file to a designated folder where the Spark client will reside.

   For AEL installation, the folder name you designate is the target folder for the **sparkHome=** parameter.

   For example, this extraction command: `tar zxf /your_path/spark-2.3.0-bin-hadoop2.7.tgz` results in the following path:

   `/your_path/spark-2.3.0-bin-hadoop2.7/`

   where: `/your_path` is the designated folder.
3. Copy the path that was created to the `application.properties` file and the**sparkHome=** parameter as shown below.

   `sparkHome=/your_path/spark-x.x.x-bin-hadoopx.x/`

   where:

   `your_path:` is the folder where you downloaded or unzipped the TGZ file.

   `spark-x.x.x-bin-hadooop.x:` is the version of the Spark client you are using.

   For example, if your folder is called `spark230`:

   `sparkHome=/spark230/spark-2.3.0-bin-hadoop2.7/`
