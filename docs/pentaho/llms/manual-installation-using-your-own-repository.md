# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/start-and-stop-the-pentaho-server-for-configuration/starting-and-stopping-the-pentaho-server-on-linux/manual-installation-using-your-own-repository.md

# Manual installation using your own repository

If you installed Pentaho using your own repository, Pentaho provides individual control scripts to start and stop the Tomcat application server, Pentaho Server, and Pentaho Repository. Here is where you can find the individual control scripts.

* **Pentaho Server**

  `pentaho/server/pentaho-server/start-pentaho.sh and stop-pentaho.sh`
* **Pentaho Repository**

  Installing with your own repository enables you to install PostgreSQL, MySQL, MS SQL Server, or Oracle as the Pentaho Repository. Consult the documentation for the relational data base management system (RDBMS) you selected for information about starting and stopping the repository.

  **Note:** The Pentaho Repository must be started before the Pentaho Server.
