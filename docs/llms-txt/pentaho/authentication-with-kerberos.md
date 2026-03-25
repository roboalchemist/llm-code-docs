# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/configuring-ael-with-spark-in-a-secure-cluster/authentication-with-kerberos.md

# Authentication with Kerberos

To enable security, you can configure the AEL daemon to work in a secure cluster using impersonation. Kerberos authentication can be used with AEL in two ways: with the connection from the client to the AEL daemon and with the Spark submit process.
