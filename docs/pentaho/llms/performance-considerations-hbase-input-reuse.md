# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-input-cp-main-page/select-an-engine-hbase-input/using-hbase-input-step-on-the-pentaho-engine-cp/performance-considerations-hbase-input-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hbase-input-cp-main-page/performance-considerations-hbase-input-reuse.md

# Performance considerations

In addition to the standard HBase server configuration and tuning options, two HBase Input factors can also affect performance. The first is the scanner row cache size setting on the **Configure query** tab. No caching is performed when this field is blank (default); one row is returned per fetch request. Setting a value in this field results in faster scans, but will consume more memory.

The second involves the selection of columns from the specified mapping to return from a query. Specifying fields in the **Key** fields table on the **Configure query** tab results in scans that return just those columns, requiring HBase to check each row to see if it contains a specific column. Checking each row creates more lookups, resulting in reduced speed. Enabling and using [Bloom filters](http://en.wikipedia.org/wiki/Bloom_filter) on the table can reduce the number of lookups. If you leave the **Key** fields table in the **Configure query** tab blank, the scan returns rows that contain all columns in every row, not just those defined in the mapping. However, HBase Input will only output those columns that are defined in the mapping as being used. When all columns are returned, HBase does not have to do any lookups.
