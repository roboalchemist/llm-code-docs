# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-row-decoder-pdi/options-hbase-row-decoder-step/createedit-mappings-tab-hbase-row-decoder-step/key-fields-table-hbase-row-decoder-step/additional-notes-on-data-types-hbase-row-decoder-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hbase-row-decoder-pdi/options-hbase-row-decoder-step/createedit-mappings-tab-hbase-row-decoder-step/key-fields-table-hbase-row-decoder-step/additional-notes-on-data-types-hbase-row-decoder-step.md

# Additional notes on data types

For keys to sort properly in HBase, you must make the distinction between signed and unsigned numbers. Because of the way that HBase stores integer and long data internally, the sign bit must be flipped before storing the signed number so that positive numbers sort after negative numbers. Unsigned integer and unsigned long data can be stored directly without inverting the sign.

The following data types have these additional options or requirements:

* **String columns**

  May optionally have a set of legal values defined for them by entering comma-separated data into the **Indexed values** column in the key fields table.
* **Date keys**

  Can be stored as either signed or unsigned long data types, with epoch-based timestamps. If you have a date key mapped as a **String** type, PDI can change the type to **Date** for manipulation in the transformation. No distinction is made between signed and unsigned numbers for the **Date** type because HBase only sorts on the key.
* **Boolean values**

  May be stored in HBase as a 0/1 **Integer**/**Long**, or as a **String** (Y/N, yes/no, true/false, T/F).
* **BigNumber**

  May be stored as either a serialized BigDecimal object or in string form (a string that can be parsed by BigDecimal's constructor).
* **Serializable**

  Any serialized Java object.
* **Binary**

  A raw array of bytes.
