# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/troubleshooting-database-connections/database-locks-when-reading-and-updating-from-a-single-table.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/troubleshooting-database-connections/database-locks-when-reading-and-updating-from-a-single-table.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/troubleshooting-database-connections/database-locks-when-reading-and-updating-from-a-single-table.md

# Database locks when reading and updating from a single table

If you create, read, and update steps to or from a single table within a transformation, you will may experience database locking or slowed processing speeds. Reading and updating rows on a table within a single transformation can cause the database to stop updating.

For example, if you have a step which reads from a row within a table (a Table Input step) and you need to update the transformation with the Update step, this could cause locking issues, especially with MS SQL databases. Reading and updating rows in the same transformation in the same table should be avoided.

A general solution compatible with all databases is to duplicate the table to be read/updated, and then create separate read/update steps. Arrange the steps to be executed sequentially within the transformation, each on a different, yet identical, version of the same table. Adjusting database row locking parameters or mechanisms will also resolve this issue.
