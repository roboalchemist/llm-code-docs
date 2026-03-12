# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/driver-timeout-and-deployment-errors-with-ael-on-secured-clusters-ael-troubleshooting.md

# Driver timeout and deployment errors with AEL on secured clusters

You may receive driver timeout and web socket deployment error messages when running Spark with AEL on a secured cluster.

Before trying to address any issues while running Spark with AEL on a secured cluster, verify the following:

* The cluster has been secured by your cluster administrator.
* The user associated with the AEL daemon has a valid Kerberos certificate.

If the expiration date and time returned by the `klist` command is less than the date and time returned by the `date` command, you must obtain a new ticket by using the `kinit` command. Contact your cluster administrator to determine what `kinit` approach was set up on your system.
