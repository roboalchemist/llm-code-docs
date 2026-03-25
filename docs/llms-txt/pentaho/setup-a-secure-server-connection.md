# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/configuring-ael-with-spark-in-a-secure-cluster/authentication-with-kerberos/setup-a-secure-server-connection.md

# Setup a secure server connection

Complete the following steps to set up a secure connection from the AEL daemon to the cluster:

1. Create a keytab and server principal to use for your server access.
2. Navigate to the `adaptive-execution/config/application.properties` file and open it with a text editor. Set the values for your environment as in the following table:

   | Parameter             | Value                                                                                                                                                                                                                     |
   | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **keytabLocation**    | Path to the keytab used for the Kerberos principal.                                                                                                                                                                       |
   | **kerberosPrincipal** | Path to the Kerberos service principal that has the authority to impersonate another user.                                                                                                                                |
   | **disableProxyUser**  | The AEL daemon can impersonate a proxy user when authenticating to your secure cluster. Set to `true` to disable the proxy user. The acting user will then be the Kerberos service principal. The default value is false. |

You can now test your AEL configuration by creating a run configuration using the Spark engine. See **Run configurtaions** in the **Pentaho Data Integration** document for instructions.
