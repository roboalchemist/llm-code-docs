# Source: https://docs.pentaho.com/install/10.2-install/pentaho-upgrade-cp/mandatory-quartz-upgrade-for-versions-10.2.0.1-and-later.md

# Mandatory Quartz upgrade for versions 10.2.0.1 and later

Initialize the new Quartz database according to your Pentaho repository database type. When upgrading from previous Pentaho versions, including 10.2.0.0 GA to 10.2.0.1 and later, you must manually initialize a new Quartz database. A new Quartz library is created in the repository database as a result. Always follow best practices and backup your data prior to proceeding. If you want to keep your existing Quartz library data, you can migrate the current tables to the new tables.

**CAUTION:**

Pentaho 10.2.0.0 and earlier versions use Quartz 1.x library, which is designated with a `QRTZ5_` prefix in the database. Newer versions, beginning with 10.2.0.1, use Quartz 2.x library, which is designated with a `QRTZ6_`prefix in the database. When upgrading from a previous version to Pentaho 10.2.0.1 and later, you must create the `QRTZ6_` prefixed table in the database by repeating the procedure for Quartz database creation, and then optionally migrating the existing Quartz schedules to the new Quartz database using the migration script. During this upgrade procedure, executing the SQL create script resets the corresponding database without loss of the original data. Always follow best practices and backup your data prior to proceeding.

**Important:** Failure to complete the Quartz upgrade results in a Pentaho Server error at start-up. In addition to the server error, the following exception message is generated in the `catalina.log` file:

```
Missing Quartz library database error
```
