# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/table-input/ael-considerations/connect-to-a-hive-database-table-input-step-ael-considerations-reused.md

# Connect to a Hive database

When using the **Table input** and **Table output** steps, you can connect to Hive in one of two ways to achieve the best processing rate for small and large tables within the same cluster:

* Use AEL to access small unmanaged Hive tables on a secure HDP cluster or an Amazon EMR cluster.
* Use AEL with the Hive Warehouse Connector (HWC) to access managed tables or large unmanaged tables in Hive on a secure HDP cluster.

See the **Administer Pentaho Data Integration and Analytics** document for details.
