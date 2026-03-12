# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/advanced-topics/configuring-ael-with-spark-in-a-secure-cluster/using-ssl-encryption/configure-the-daemon-for-ssl.md

# Configure the daemon for SSL

Complete the following to configure the AEL daemon for SSL:

1. Navigate to the `adaptive-execution/config/application.properties` file and open it with a text editor.
2. Set the values for your environment as in the following table:

| Parameter                      | Value                                                                                                                                     |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **websocketURL**               | The fully-qualified domain name of the node where the AEL daemon is installed. For example,`websocketURL=wss://localhost:${ael.ssl.port}` |
| **ael.ssl.enabled**            | `true`                                                                                                                                    |
| **ael.ssl.key-store**          | `/users/myusername/pentaho/mycertificate.p12`                                                                                             |
| **ael.ssl.key-store-type**     | `PKCS12`                                                                                                                                  |
| **ael.ssl.key-store-password** | The SSL keystore password. This must be set to your keystore password.                                                                    |
| **ael.ssl.key-password**       | The SSL key password. This must be set to your key password.                                                                              |

You can now test your AEL configuration by creating a run configuration using the Spark engine. See \*\*Run configurtaions\*\* in the \*\*Pentaho Data Integration\*\* document for instructions.

The first time you start the AEL daemon, it will prompt you to enter the SSL keystore and key passwords.
