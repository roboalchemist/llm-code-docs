# Source: https://docs.syncfusion.com/document-processing/excel/excel-library/net/faqs/why-formulas-referencing-the-deleted-column-show-ref-errors.md

# Why do formulas referencing a deleted column show #REF! errors?
When a column is deleted either directly in Excel or programmatically using Syncfusion XlsIO the entire column is removed and the columns to the right shift left. If any formula referenced cells within the deleted column, Excel can no longer resolve those references. As a result, the affected formulas display #REF! errors to indicate that the referenced cells no longer exist. Syncfusion XlsIO follows the same behavior as Microsoft Excel in this scenario.
