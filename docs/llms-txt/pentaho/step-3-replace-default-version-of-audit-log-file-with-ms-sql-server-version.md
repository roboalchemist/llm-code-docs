# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/configure-ms-sql-server-pentaho-repository-database/step-3-replace-default-version-of-audit-log-file-with-ms-sql-server-version.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-ms-sql-server-as-your-repository-database-archive-installation/configure-ms-sql-server-pentaho-repository-database/step-3-replace-default-version-of-audit-log-file-with-ms-sql-server-version.md

# Step 3: Replace default version of audit log file with MS SQL Server version

Since you are using MS SQL to host the Pentaho Repository, you need to replace the `audit_sql.xml` file with one that is configured for MS SQL Server.

1. Locate the `pentaho-solutions/system/dialects/sqlserver/audit_sql.xml` file.
2. Copy it into the `pentaho-solutions/system` directory.
