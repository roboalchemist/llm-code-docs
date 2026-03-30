# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/stop-carte-from-the-command-line-interface-or-url.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/use-carte-clusters/stop-carte-from-the-command-line-interface-or-url.md

# Stop Carte from the Command Line Interface or URL

Perform the following steps to stop Carte either from the CLI or URL:

1. Open the command line interface by clicking **Start** and typing `cmd`. Press Enter.
2. In the command line interface, enter the location of the Carte server.
3. Enter a space, then type the arguments for stopping the server.
4. Press Enter after the arguments are typed.

   Arguments:

   ```
   Carte <Interface address> <Port> [-s] [-p <arg>] [-u <arg>]
   ```

   Example:

   ```
   Carte 127.0.0.1 8080 -s -p amidala4ever -u dvader
   ```

   You can also now use a URL to stop Carte:

   ```
   http://localhost:8080/kettle/stopCarte
   ```

   | Command Option       | Description                                                                                           | Type         |
   | -------------------- | ----------------------------------------------------------------------------------------------------- | ------------ |
   | -h, --help           | Help text.                                                                                            | n/a          |
   | -p,--password \<arg> | The administrator password. Required only if stopping the Carte server.                               | Alphanumeric |
   | -s,--stop            | Stop the running Carte server. This is only allowed when using the hostname/port form of the command. | Alphanumeric |
   | -u,--username \<arg> | The administrator user name. Required only if stopping the Carte server.                              | Alphanumeric |
