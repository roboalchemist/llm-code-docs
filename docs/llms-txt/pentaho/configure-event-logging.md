# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/configure-event-logging.md

# Configure event logging

Spark events can be captured in an event log that can be viewed with the Spark History Server. The Spark History Server is a web browser-based user interface to the event log. You can view either running or completed Spark transformations using the Spark History Server. Before you can use the Spark History Server, you must configure AEL to log the events.

Perform the following tasks to configure AEL to log events:

1. Have your cluster administrator enable the Spark History Server on your cluster and give you the location of the Spark event log directory.
2. Navigate to the `data-integration/adaptive-execution/config` directory and open the `application.properties` file.
3. Set the **sparkEventLogEnabled** property to `true`.

   If this field is missing or set to `false`, Spark does not log events.
4. Set the **sparkEventLogDir** property to a directory where you want to store the log.

   This location can either be a file system directory (for example, `file:///users/home/spark-events`), or an HDFS directory (for example, `hdfs:/usrs/home/spark-events`).
5. Set the **spark.history.fs.logDirectory** property to point to the same event log directory you configured in the previous step.

You can now view Spark-specific information for your PDI transformations using the Spark History Server.

Refer to the following documents for more information on running the Spark History Server:

* <https://spark.apache.org/docs/latest/monitoring.html>
* <https://docs.cloudera.com/HDPDocuments/HDP3/HDP-3.1.4/configuring-spark/content/configuring_the_spark_history_server_kerberos.html>
* <https://www.cloudera.com/documentation/enterprise/6-1-x/topics/operation_spark_applications.html>
* <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-application-history.html>
* <https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-history-server.html>
