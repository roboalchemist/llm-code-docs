# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-input-cp-main-page/select-an-engine-hbase-input/using-hbase-input-step-on-the-pentaho-engine-cp/options-hbase-input-reuse/filter-result-set-tab-hbase-input-pentaho.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hbase-input-cp-main-page/options-hbase-input-reuse/filter-result-set-tab-hbase-input-pentaho.md

# Filter result set tab

Use the **Filter result set** tab fields to further refine the set of rows returned by specifying filtering operations on the values of columns other than the key. You can enter row-filtering criteria against one or more columns defined in the mapping.

![Filter result set tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-358f41da6100f6fa98b89c8b76b7796f5f056b46%2FPDI_HBase_filter-result-set.png?alt=media)

This tab includes the following fields:

| Option                       | Description                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Match all**/ **Match any** | When multiple column filters have been defined, you have the option returning only those rows that match all filters, or any single filter. You can set bounded ranges on a single numeric column by defining upper bound and lower bound filters and selecting the **Match all** option. Open-ended ranges can be defined by selecting the **Match any** option. |
