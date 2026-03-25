# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/manual-installation/manual-installation-process/use-mysql-or-mariadb-as-your-repository-database-manual-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-3-replace-default-version-of-audit-log-file-with-mysql-version-shared.md

# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-3-replace-default-version-of-audit-log-file-with-mysql-version-shared.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-mysql-or-mariadb-as-your-repository-database-archive-installation/configure-mysql-or-mariadb-pentaho-repository-database-shared/step-3-replace-default-version-of-audit-log-file-with-mysql-version-shared.md

# Step 3: Replace default version of audit log file with MySQL version

Since you are using MySQL to host the Pentaho Repository, you need to replace the `audit_sql.xml` file with one that is configured for MySQL. If you are using MariaDB, use the same `audit_sql.xml` as for MySQL.

1. Locate the `pentaho-solutions/system/dialects/mysql5/audit_sql.xml` file.
2. Copy it into the `pentaho-solutions/system` directory.
