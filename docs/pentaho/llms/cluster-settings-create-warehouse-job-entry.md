# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/create-warehouse-pdi-job-entry/options-create-warehouse-job-entry/cluster-settings-create-warehouse-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/create-warehouse-pdi-job-entry/options-create-warehouse-job-entry/cluster-settings-create-warehouse-job-entry.md

# Cluster settings

The maximum and minimum cluster settings work together. Depending on your processing needs, you can use the cluster settings to run a multi-cluster warehouse in either Maximized mode or Auto-scale mode.

* If you set the minimum and maximum cluster count with the same value, then the warehouse runs in Maximized mode.
* If you set the minimum cluster count less than the maximum cluster count, then the warehouse runs in Auto-scale mode.

See the [Snowflake documentation](https://docs.snowflake.net) for more details.

| Option                    | Description                                                                                                                                                                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Minimum cluster count** | If you are creating a multi-cluster warehouse, select the minimum number of server clusters for this virtual warehouse.Valid values are 1 to 10. The default value is 1. This value must be equal to or less than the Maximum cluster count. |
| **Maximum cluster count** | Select the maximum number of server clusters for this virtual warehouse. Valid values are 1 to 10. The default value is 1. **Note:** Higher values require the Snowflake Enterprise Edition.                                                 |
