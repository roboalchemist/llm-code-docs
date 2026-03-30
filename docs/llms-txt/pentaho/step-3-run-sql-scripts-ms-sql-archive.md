# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/initialize-ms-sql-server-pentaho-repository-database/step-3-run-sql-scripts-ms-sql-archive.md

# Step 3: Run SQL scripts

Run the SQL scripts in the table below.

**Note:** These scripts require administrator permissions on the server to run them.

**CAUTION:**

If you have a different port or different password, make sure that you change the password and port numbers in these examples to match the ones in your configuration.

Run these scripts from the sqlcmd utility window or from Microsoft SQL Server Management Studio.

| Action                         | SQL Script                                             |
| ------------------------------ | ------------------------------------------------------ |
| Create Quartz                  | `-i <filepath to DDL>/create_quartz_sqlServer.sql`     |
| Create Hibernate repository    | `-i <filepath to DDL>/create_repository_sqlServer.sql` |
| Create Jackrabbit              | `-i <filepath to DDL>/create_jcr_sqlServer.sql`        |
| Create Pentaho Operations mart | `-i <filepath to DDL>/pentaho_mart_sqlserver.sql`      |

**Note:** You unpacked the Pentaho Operations mart SQL file while preparing your environment for the archive installation process. Depending on your environment, see [Prepare your Windows environment for an archive install](https://github.com/pentaho/documentation/blob/main/PDIA/9.3/Install/Pentaho%20installation/Pentaho%20Installation%20\(overview%20cp\)/Archive%20installation/Archive%20installation%20process/Prepare%20your%20Windows%20environment%20for%20an%20archive%20install=GUID-B3F10607-0F15-48A2-9000-586C36CE7811=2=en=.md) or [Prepare your Linux environment for an archive install](https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install) for details.
