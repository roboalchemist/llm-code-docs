# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/google-dataproc.md

# Google Dataproc

To use Google Dataproc with AEL, you must first complete the AEL setup, including the steps in the [Configure the AEL daemon for a Hive service](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/hive-ael-setup-specific-to-hive/configure-the-ael-daemon-for-a-hive-service) topic. You do not have to use any vendor-specific Spark client with Dataproc, or install the Linux LZO compression library.

Perform the following steps to use the AEL engine with Hive on a GDP cluster:

1. Navigate to the `etc/hive/conf` directory on the master node of the Pentaho instance on the GDP cluster.
2. Open the `hive-site.xml` with any text editor.
3. Locate the **hive.execution.engine** property and change the tez default value to `spark`.
4. Save and close the file.

Hive is now set up to run on GDP
