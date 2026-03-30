# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/driver-timeout-and-deployment-errors-with-ael-on-secured-clusters-ael-troubleshooting/web-socket-deployment-exception-ael-secured-cluster-errors-ael-troubleshooting.md

# Web socket deployment exception

You might execute a transformation and it completes immediately with the following error:

```
2020/01/22 14:40:01 - Spoon - Started the transformation execution.
2020/01/22 14:40:02 - Spoon - The transformation has finished!!
2020/01/22 14:40:02 - Spoon - ERROR (version 9.0.0.0-387, build 9.0.0.0-387 from 2020-01-09 11.20.10 by buildguy) : Error starting step threads
2020/01/22 14:40:02 - Spoon - ERROR (version 9.0.0.0-387, build 9.0.0.0-387 from 2020-01-09 11.20.10 by buildguy) : org.pentaho.di.core.exception.KettleException: 
2020/01/22 14:40:02 - Spoon - javax.websocket.DeploymentException: Connection failed.
2020/01/22 14:40:02 - Spoon - Connection failed.

```

This issue occurs because you do not have access to the AEL daemon, it is not running, or the **Spark host URL** setting is not correct in your PDI run configuration.

Perform the following workflow to resolve this issue.

1. Verify that you can access the node running the AEL daemon.

   If you cannot access the node, contact your cluster administrator for further instructions.
2. If you can access the node, verify that the AEL daemon is active (running) by using the **status** option while executing the `daemon` command from the `data-integration/adaptive-execution` directory, as shown in the following example:

   ```
   ./daemon.sh status
   ```
3. If the daemon is not active, enter the start option of the daemon command, as shown in the following example:

   ```
   ./daemon.sh start
   ```
4. If you can access the node and the daemon is active, but the error still occurs, verify that the port number specified in **Spark host URL** option of your run configuration for the Spark engine matches the **ael.unencrypted.port** property in the `application.properties` file.

   Also, verify that the hostname or IP address in the URL matches the **hostname** property in the `application.properties` file.
