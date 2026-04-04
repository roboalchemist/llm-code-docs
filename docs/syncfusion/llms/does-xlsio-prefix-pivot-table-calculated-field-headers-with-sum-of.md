# Source: https://docs.syncfusion.com/document-processing/excel/excel-library/net/faqs/does-xlsio-prefix-pivot-table-calculated-field-headers-with-sum-of.md

# Does XlsIO prefix PivotTable calculated field headers with "Sum of"?

Yes. When a calculated field is added to a PivotTable, Microsoft Excel automatically prefixes the column header with **Sum of** before the original name. For example, a field named **Profit** becomes **Sum of Profit**. XlsIO follows the same behavior to remain consistent with Excel.