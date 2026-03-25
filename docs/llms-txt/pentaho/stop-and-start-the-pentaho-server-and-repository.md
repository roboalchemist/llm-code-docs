# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/configure-the-pentaho-server/stop-and-start-the-pentaho-server-and-repository.md

# Stop and start the Pentaho Server and repository

To perform maintenance work on the Pentaho Server or components that use the Pentaho Server, such as the Pentaho User Console and Pentaho Data Integration, you must stop the repository and server, perform the work, and then restart the repository and server after you complete the work.

**Important:** The Pentaho Repository must be started before the Pentaho Server.

You must be an IT administrator and know where the data that you are managing is stored, how to access that stored data, details about the computing environment, and how to use the command line to issue commands for Microsoft Windows or Linux.

1. Run the following control scripts to stop and start the Pentaho Server and Pentaho Repository:

| **Start on Windows** | `...\pentaho\server\pentaho-server\start-pentaho.bat` |
| -------------------- | ----------------------------------------------------- |
| **Stop on Windows**  | `...\pentaho\server\pentaho-server\stop-pentaho.bat`  |
| **Start on Linux**   | `.../pentaho/server/pentaho-server/start-pentaho.sh`  |
| **Stop on Linux**    | `.../pentaho/server/pentaho-server/stop-pentaho.sh`   |

\*\*Notes:\*\*

```
-   If you installed the Pentaho repository as PostgreSQL, MySQL, MS SQL Server, or Oracle, consult the documentation for that relational database management system for information about starting and stopping the repository.
-   To create custom scripts for starting and stopping components, you can use the following script arguments and services:
    -   Arguments
        -   start
        -   stop
        -   restart
        -   status
        -   help
    -   Services
        -   pentahoserver
        -   Postgressql
```
