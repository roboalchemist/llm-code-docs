# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer/select-an-engine-mqtt-consumer/using-the-mqtt-consumer-step-on-the-spark-engine-cp.md

# Using the MQTT Consumer step on the Spark engine

You can set up the MQTT Consumer step to run on the Spark engine. If your MQTT is configured to accept SSL connections, you need to adjust the AEL daemon `application.properties` file for SSL keystore. For more information, see [Using MQTT with SSL on AEL](https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mqtt-consumer/select-an-engine-mqtt-consumer/using-the-mqtt-consumer-step-on-the-spark-engine-cp/using-mqtt-with-ssl-on-ael-mqtt-consumer-spark)

**Note:** When running on Spark, you must execute the child transformation using the **Duration (ms)** option only. See the [Batch tab](https://github.com/pentaho/documentation/blob/main/PDIA/9.3/PDI/Batch%20tab%20\(MQTT%20Consumer\)%20\(Spark\).md) for more information.
