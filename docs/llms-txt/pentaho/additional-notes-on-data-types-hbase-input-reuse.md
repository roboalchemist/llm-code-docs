# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-input-cp-main-page/select-an-engine-hbase-input/using-hbase-input-step-on-the-pentaho-engine-cp/options-hbase-input-reuse/createedit-mappings-tab-hbase-input-reuse/additional-notes-on-data-types-hbase-input-reuse.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hbase-input-cp-main-page/options-hbase-input-reuse/createedit-mappings-tab-hbase-input-reuse/additional-notes-on-data-types-hbase-input-reuse.md

# Additional notes on data types

For keys to sort properly in HBase, you must note the distinction between signed and unsigned numbers. Because of the way that HBase stores integer and long data internally, the sign bit must be flipped before storing the signed number so that positive numbers will sort after negative numbers. Unsigned integer and unsigned long data can be stored directly without inverting the sign.

* **String columns**

  May optionally have a set of legal values defined for them by entering comma-separated data into the **Indexed values** column in the fields table.
* **Date keys**

  Can be stored as either signed or unsigned long data types, with epoch-based timestamps. If you have a date key mapped as a **String** type, PDI can change the type to **Date** for manipulation in the transformation. No distinction is made between signed and unsigned numbers for the **Date** type because HBase only sorts on the key.
* **Boolean values**

  May be stored in HBase as 0/1 integer/long or as strings (Y/N, yes/no, true/false, T/F).
* **BigNumber**

  May be stored as either a serialized BigDecimal object or in string form (that is, a string that can be parsed by BigDecimal's constructor).
* **Serializable**

  Any serialized Java object.
* **Binary**

  A raw array of bytes.
