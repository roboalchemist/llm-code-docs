# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/before-you-begin-mysql-archive-and-manual-repository-shared.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/before-you-begin-mysql-archive-and-manual-repository-shared.md

# Before you begin

## Prerequisite

Before you prepare your Pentaho Repository, you must prepare either a [Windows](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Install/Pentaho%20installation/Pentaho%20Installation%20\(overview%20cp\)/Archive%20installation/Archive%20installation%20process/Prepare%20your%20Windows%20environment%20for%20an%20archive%20install=GUID-B3F10607-0F15-48A2-9000-586C36CE7811=2=en=.md) or [Linux](https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/prepare-your-linux-environment-for-an-archive-install) environment.

**Note:** The MySQL Connector/J 8.0 cannot be used when configuring Tomcat with the JDBC driver JAR.

## Components

The Pentaho Repository resides on the database that you installed during the Windows or Linux environment preparation step, and consists of the following components:

* **Jackrabbit**

  Contains the solution repository, examples, security data, and content data from reports that you use Pentaho software to create.
* **Quartz**

  Holds data that is related to scheduling reports and jobs.
* **Hibernate**

  Holds data that is related to audit logging.
* **(Optional) Pentaho Operations Mart**

  To report on system usage and performance.
