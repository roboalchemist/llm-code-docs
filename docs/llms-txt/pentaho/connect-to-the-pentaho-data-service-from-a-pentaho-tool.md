# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/connect-to-the-pentaho-data-service-from-a-pentaho-tool.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/share-a-pentaho-data-service-with-others/connect-to-the-pentaho-data-service-from-a-pentaho-tool.md

# Connect to the Pentaho Data Service from a Pentaho tool

A Pentaho Data Service is a virtual table that contains the output of a step in a PDI transformation. You can connect to and query a [regular](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/creating-a-regular-or-streaming-pentaho-data-service) Pentaho Data Service from any Pentaho tool, such as Report Designer, the PDI client (Spoon), and Analyzer. You can connect to and query a streaming Pentaho Data Service from a dashboard created with CTools. For more information, see **Pentaho CTools**.

**Note:** To connect and query the Pentaho Data Service, you need to know the data service name and have permission to run the transformation and to access the Pentaho Server where it is published.

Connecting to the data service from another Pentaho tool is the same as connecting to a database. The following tables describe the parameters needed to make a Pentaho Data Service connection:

| Required Parameters | Description                                                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Connection Name** | The unique name of the data service you want to access                                                             |
| **Connection Type** | Pentaho Data Services                                                                                              |
| **Access**          | Native (JDBC)                                                                                                      |
| **Hostname**        | Hostname of the Pentaho Server or IP address. By default, this is localhost if running the Pentaho Server locally. |
| **Port Number**     | Port number of the Pentaho Server the data service will run on. The default is 8080.                               |
| **Web App Name**    | Name of the web application. The default value is pentaho, which is typically used by the other Pentaho tools.     |
| **Username**        | Name of a user who has permission to run the data service.                                                         |
| **Password**        | Password for a user who has permission to run the data service.                                                    |

You can also set the following optional parameters.

| Optional Parameters              | Description                                                                                                                                                                                                                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **proxyhostname**                | Proxy server for HTTP connection(s).                                                                                                                                                                                                                                                               |
| **proxyport**                    | Proxy server port.                                                                                                                                                                                                                                                                                 |
| **nonproxyhosts**                | Hosts that do not use the proxy server. If there is more than one host name, separate them with commas.                                                                                                                                                                                            |
| **debugtrans**                   | Optional name of the file where the generated transformation is stored. This transformation is generated to debug it. Example: `/tmp/debug.ktr`. Specify the name of the transformation or a path plus the name of the transformation.                                                             |
| `PARAMETER_[optionname]=*value*` | Sets the value for a parameter in the transformation. `[optionname]` is the name of the parameter, and `[*value*]` is the value assigned to it. `PARAMETER_` is placed before the option name. For example, if the name of the parameter is **model**, set the parameter: `PARAMETER_model=E6530`. |
| **secure**                       | Set this parameter to `TRUE` to use the HTTPS secure protocol connect to the data service. If you omit this parameter or set it to `FALSE`, the standard HTTP unsecure protocol is used.                                                                                                           |
