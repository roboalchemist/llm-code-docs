# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/specify-data-connections-for-the-pentaho-server.md

# Specify data connections for the Pentaho Server

For business analytics, you can use the Pentaho User Console to define the connection to where you store data.

We support accessing data stored in the following ways:

* Comma separated values (CSV) files or any file that can be converted to CSV, such as spreadsheets, XML, or other semi-structured or tabular data file. To work with CSV files, you only need to know the location of the files. Use CSV files if you are evaluating Pentaho or you want to get started quickly.
* JDBC drivers to help with database connections.

In Pentaho Data Integration (PDI), you can make connections in each job and transformation through an input step. Although users can create connections themselves, it is best to set up shared connections for your users so that they can simply select the connection they need from a list. We help you download the correct JDBC drivers, choose the connection type, and then create the connection.
