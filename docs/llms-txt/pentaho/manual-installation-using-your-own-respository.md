# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/start-and-stop-the-pentaho-server-for-configuration/starting-and-stopping-the-pentaho-server-on-windows/manual-installation-using-your-own-respository.md

# Manual installation using your own respository

If you installed Pentaho using your own repository, we provide individual control scripts to start and stop the Pentaho Server and Pentaho Repository. Here is where you can find the individual control scripts.

Pentaho Server

* `/pentaho/server/pentaho-server/start-pentaho.bat and stop-pentaho.bat`

Pentaho Repository

* Installing Pentaho using your own repository enables you to install PostgreSQL, MySQL, MS SQL Server, or Oracle as the repository. Consult the documentation for the relational data base management system (RDBMS) you selected for information about starting and stopping the repository.
* The Pentaho Repository must be started before the Pentaho Server.
