# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-output/options-mongodb-output/configure-connection-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/options-mongodb-input/configure-connection-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-output/options-mongodb-output/configure-connection-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/mongodb-input/options-mongodb-input/configure-connection-tab.md

# Configure connection tab

You have two options when configuring a connection in the MongoDB Input step: configure using a connection string or configure using fields.

## Connection String

![MongoDB Input configure Connection String option](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-846d39c52340659367d6bac4df224551ead2f5ff%2FPDI%20MongoDB%20Input%20connection%20tab%20string.png?alt=media)

To configure using a connection string, select the **Connection String** option and enter a connection string containing the information for connecting to MongoDB in the text box provided. Verify your connection is working by clicking **Test Connection**. For information about the connection string formats and options, see the [MongoDB documentation](https://www.mongodb.com/docs/manual/reference/connection-string/).

Some common connection string example formats are listed in the following table:

| Connection Type                                             | Connection string format                                                                                                                |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| SSL                                                         | `mongodb://<hostname>:<port>/?tls=true`                                                                                                 |
| SSL and LDAP                                                | `mongodb://<username>:<password>@<hostname>:<port>/?tls=true&authSource=$external&authMechanism=PLAIN`                                  |
| LDAP                                                        | `mongodb://<username>:<password>@<hostname>:<port>/?authSource=$external&authMechanism=PLAIN`                                           |
| SSL and LDAP cluster servers with replicaSet options        | `mongodb://<username>:<password>@<hostname>:<port>/?tls=true&authsource=$external&authMechanism=PLAIN&replicaSet=rs0`                   |
| SSL and LDAP with `replicaSet` and `readPreference` options | `mongodb://<username>:<password>@<hostname>/?tls=true&authSource=$external&authMechanism=PLAIN&replicaSet=rs0&readPreference=secondary` |
| Kerberos                                                    | `mongodb://<service-principal>@<hostname>:<port>/?authSource=$external&authMechanism=GSSAPI`                                            |
| Kerberos and SSL                                            | `mongodb://<service-principal>@<hostname>:<port>/?authSource=$external&authMechanism=GSSAPI&tls=true`                                   |
| Atlas Cloud/SAAS                                            | `mongodb+srv://<username>:<password>@mycluster.qj8y0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`                           |

## Configure Fields

![MongoDB Input Configure Fields option](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-bf026e558c0cfef02d9863e7626983cd3a3bc522%2FPDI%20MongoDB%20Input%20configure%20tab%20fields.png?alt=media)

If you select **Configure Fields**, enter your connection information in the following fields.

| Field                                  | Description                                                                                                                                                                                                                                                                                                                             |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Host name(s) or IP address(es)**     | Specify the network name or address of the MongoDB instance or instances. You can also specify a different port number for each host name by separating the host name and port number with a colon. You can input multiple host names or IP addresses, separated by a comma.                                                            |
| **Port**                               | Specify the port number of the MongoDB instance or instances. Use this to specify a default port if no ports are given as part of the host name(s) or IP address(es) field. The default value is 27017.                                                                                                                                 |
| **Enable SSL connection**              | Specify to connect to a MongoDB Server that is configured with SSL.                                                                                                                                                                                                                                                                     |
| **Use all replica set members/mongos** | <p>Select to use all replica sets when multiple hosts are specified in the <strong>Host name(s) or IP address(s)</strong> field.</p><p>If a replica set contains more than one host, the Java driver discovers all hosts automatically. The driver connects to the next replica set in the list if the selected set is unavailable.</p> |
| **Authentication database**            | Specify the authentication database.                                                                                                                                                                                                                                                                                                    |
| **Authenticate Mechanism**             | Select the method used to verify the identity of users. The values are `SCRAM-SHA-1`, `MONGODB-CR`, and `PLAIN`.                                                                                                                                                                                                                        |
| **Username**                           | Specify the username required to access the database. When using Kerberos authentication, enter the Kerberos principal.                                                                                                                                                                                                                 |
| **Password**                           | Specify the password associated with the username. If you are using Kerberos authentication, you do not need to enter the password.                                                                                                                                                                                                     |
| **Authenticate using Kerberos**        | Select to specify authentication using Kerberos. When selected, enter the Kerberos principal as the **Username**.                                                                                                                                                                                                                       |
| **Connection timeout**                 | Specify (in milliseconds) how long to wait for a connection to a database before terminating the connection attempt. Leave blank to never terminate the connection.                                                                                                                                                                     |
| **Socket timeout**                     | Specify (in milliseconds) how long to wait for a write operation before terminating the operation. Leave blank to never terminate the operation.                                                                                                                                                                                        |
| **Preview**                            | Display the rows generated by this step. Enter the maximum number of records that you want to preview, then click **OK**. The preview data appears in the **Examine preview data** window.                                                                                                                                              |
