# Source: https://docs.pentaho.com/install/9.3-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/configure-oracle-pentaho-repository-database/step-3-replace-default-version-of-audit-log-file-with-oracle-version.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/archive-installation/archive-installation-process/use-oracle-as-your-repository-database-archive-installation/configure-oracle-pentaho-repository-database/step-3-replace-default-version-of-audit-log-file-with-oracle-version.md

# Step 3: Replace default version of audit log file with Oracle version

Since you are using Oracle to host the Pentaho Repository, you need to replace the `audit_sql.xml` file with one that is configured for Oracle.

1. Locate the `pentaho-solutions/system/dialects/oracle10g/audit_sql.xml` file.
2. Copy it into the `pentaho-solutions/system` directory.
