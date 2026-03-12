# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/driver-timeout-and-deployment-errors-with-ael-on-secured-clusters-ael-troubleshooting/driver-session-timeout-ael-secured-cluster-errors-ael-troubleshooting.md

# Driver session timeout

The AEL daemon log may indicate that the “Server not found in Kerberos database” and the PDI client log may contain the following text:

```
2020/01/22 13:33:00 - HiveSmokeTest - Finalizing execution: Driver Session Timeout Expired
2020/01/22 13:33:00 - Spoon - The transformation has finished!!

```

This issue occurs because the **websocketURL** property is not set to a fully qualified host name for the node running the AEL daemon. To resolve this issue, obtain the fully qualified host name by using the hostname command, as shown in the following example:

```
[devuser@hito31-n2 adaptive-execution]$ hostname -f
hito31-n2.cs1cloud.internal

```

Then, set the resulting host name to the **websocketURL** property, as shown in the following example:

```
websocketURL=ws://hito31-n2.cs1cloud.internal:${ael.unencrypted.port}
```
