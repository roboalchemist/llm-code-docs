# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/initialize-slave-servers.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/set-up-a-carte-cluster/initialize-slave-servers.md

# Initialize Slave Servers

Follow the instructions below to configure PDI to work with Carte slave servers.

1. Open a transformation.
2. In the **Explorer View** in the PDI client(Spoon), select the **Slave** tab.
3. Select the **New** button.

   The Slave Server dialog window appears.
4. In the Slave Server dialog window, enter the appropriate connection information for the Pentaho (or Carte) slave server.

   | Option                                     | Description                                                                                                     |
   | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
   | Server name                                | The name of the slave server.                                                                                   |
   | Hostname or IP address                     | The address of the device to be used as a slave.                                                                |
   | Port (empty is port 80)                    | Defines the port you are for communicating with the remote server. If you leave the port blank, 80 is used.     |
   | Web App Name (required for Pentaho Server) | Leave this blank if you are setting up a Carte server. This field is used for connecting to the Pentaho server. |
   | User name                                  | Enter the user name for accessing the remote server.                                                            |
   | Password                                   | Enter the password for accessing the remote server.                                                             |
   | Is the master                              | Enables this server as the master server in any clustered executions of the transformation.                     |

   **Note:** When executing a transformation or job in a clustered environment, you should have one server set up as the master and all remaining servers in the cluster as slaves.

   Below are the proxy tab options:

   | Option                                      | Description                                                                                                                                                                                                                      |
   | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Proxy server hostname                       | Sets the host name for the proxy server you are using.                                                                                                                                                                           |
   | The proxy server port                       | Sets the port number used for communicating with the proxy.                                                                                                                                                                      |
   | Ignore proxy for hosts: regexp \| separated | Specify the server(s) for which the proxy should not be active. This option supports specifying multiple servers using regular expressions. You can also add multiple servers and expressions separated by the ' \| ' character. |
5. Click **OK** to exit the dialog box. Notice that a plus sign (+) appears next to **Slave Server**in the Explorer View.
