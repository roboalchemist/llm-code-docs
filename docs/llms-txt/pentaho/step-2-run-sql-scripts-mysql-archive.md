# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-mysql-or-mariadb-as-your-repository-database-manual-installation/initialize-mysql-or-mariadb-pentaho-repository-database/step-2-run-sql-scripts-mysql-archive.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/initialize-mysql-or-mariadb-pentaho-repository-database/step-2-run-sql-scripts-mysql-archive.md

# Step 2: Run SQL scripts

Run the SQL scripts in the table below.

**Note:** These scripts require administrator permissions on the server to run them.

**CAUTION:**

If you have a different port or different password, make sure that you change the password and port numbers in these examples to match the ones in your configuration.

Run these scripts from the MySQL Command Prompt window or from MySQL Workbench.

| Action                         | SQL Script                                             |
| ------------------------------ | ------------------------------------------------------ |
| Create Quartz                  | `> source <your filepath>/create_quartz_mysql.sql`     |
| Create Hibernate repository    | `> source <your filepath>/create_repository_mysql.sql` |
| Create Jackrabbit              | `> source <your filepath>/create_jcr_mysql.sql`        |
| Create Pentaho Operations mart | `> source <your filepath>/pentaho_mart_mysql.sql`      |

**Note:** You unpacked the Pentaho Operations mart SQL file while preparing your environment for the archive installation process. Depending on your environment, see [Prepare your Windows environment for an archive install](https://github.com/pentaho/documentation/blob/main/PDIA/9.3/Install/Pentaho%20installation/Pentaho%20Installation%20\(overview%20cp\)/Archive%20installation/Archive%20installation%20process/Prepare%20your%20Windows%20environment%20for%20an%20archive%20install=GUID-B3F10607-0F15-48A2-9000-586C36CE7811=2=en=.md) or [Prepare your Linux environment for an archive install](https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install) for details.
