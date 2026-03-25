# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/big-data-issues/spark-issues/table-input-step-fails/method-2-increase-the-driver-side-memory-configuration.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/table-input-step-fails/method-2-increase-the-driver-side-memory-configuration.md

# Method 2: Increase the driver side memory configuration

1. Navigate to the `config/` folder and open the `application.properties` file.
2. Increase the value of the **sparkDriverMemory** parameter, then save and close the file.

See [Configuring application tuning parameters for Spark](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/spark-tuning-landing-page-cp/configuring-application-tuning-parameters-for-spark) for further information.
