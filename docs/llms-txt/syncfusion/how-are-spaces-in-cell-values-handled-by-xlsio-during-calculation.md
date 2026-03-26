# Source: https://docs.syncfusion.com/document-processing/excel/excel-library/net/faqs/how-are-spaces-in-cell-values-handled-by-xlsio-during-calculation.md

# How are spaces in cell values handled by XlsIO during calculation?

In Microsoft Excel, leading and trailing spaces in cell values are preserved for display purposes. However, when performing calculations (for example, **=A1+5** where A1 contains **" 25 "** with spaces), Excel automatically ignores those spaces and treats the underlying numeric value. Spaces are always shown in the cell but ignored in calculations. Syncfusion XlsIO follows the same behavior.