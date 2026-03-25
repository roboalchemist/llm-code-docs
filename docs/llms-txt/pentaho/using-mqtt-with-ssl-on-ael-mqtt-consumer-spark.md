# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer/select-an-engine-mqtt-consumer/using-the-mqtt-consumer-step-on-the-spark-engine-cp/using-mqtt-with-ssl-on-ael-mqtt-consumer-spark.md

# Using MQTT with SSL on AEL

Complete the following steps to use the MQTT Consumer step with the Pentaho Adaptive Execution Layer (AEL) when connecting to an SSL-enabled MQTT server.

1. Navigate to the `data-integration/adaptive-execution/config` directory and open the `application.properties` file with any text editor.
2. Add the following parameters.

   1. Add the **DriverExtraJavaOptions** parameter for the Spark driver application and specify the file path for `client.ks` and its associated password on the cluster:

      ```
      sparkDriverExtraJavaOptions=-Dlog4j.configuration=file:${sparkApp}/classes/log4j.xml -Djavax.net.ssl.trustStore=*\[filepath to client.ks on the cluster\]*
      -Djavax.net.ssl.trustStorePassword=password

      ```

      ```
      sparkDriverExtraJavaOptions=-Dlog4j.configuration=file:${sparkApp}/classes/log4j.xml -Djavax.net.ssl.trustStore=/home/cloudera/client.ks
      -Djavax.net.ssl.trustStorePassword=password

      ```
   2. Add the **ExtraJavaOptions** parameter for the Spark executors and specify the file path for `client.ks` and its password on the cluster:

      ```
      sparkExecutorExtraJavaOptions=-Djavax.net.ssl.trustStore=*\[filepath to client.ks on the cluster\]* 
      -Djavax.net.ssl.trustStorePassword=password

      ```

   ```
   sparkExecutorExtraJavaOptions=-Djavax.net.ssl.trustStore=/home/cloudera/client.ks
   -Djavax.net.ssl.trustStorePassword=password

   ```
3. Save and close the file.
4. Navigate to the `data-integration/adaptive-execution` folder and run the `daemon.sh` command from the command line interface.
