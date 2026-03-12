# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/configuring-ael-with-spark-in-a-secure-cluster/authentication-with-kerberos/setup-a-secure-client-connection.md

# Setup a secure client connection

Complete the following steps to set up a secure connection from the PDI client to the AEL daemon:

1. Download and install Kerberos server. Refer to the **Administer Pentaho Data Integration and Analytics** document for further details on installing the Kerberos server.
2. Create a keytab and principal to use for your client access.
3. Open the PDI client and choose **Edit** > **Edit the kettle.properties file**.
4. Add the properties **KETTLE\_AEL\_PDI\_DAEMON\_KEYTAB** and**KETTLE\_AEL\_PDI\_DAEMON\_PRINCIPAL** and set the values to the location of the keytab and principal, respectively.
5. Restart the PDI client.
