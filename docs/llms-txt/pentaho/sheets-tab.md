# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-input/options-microsoft-excel-input/sheets-tab.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-input/options-microsoft-excel-input/sheets-tab.md

# Sheets tab

![Microsoft Excel Input step Sheets tab](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-63404395072d2eb02e6817049b69501872ef4729%2FPDI_TransStep_Microsoft_Excel_Input_Sheets_Tab.png?alt=media)

Use the table in the **Sheets** tab to specify which worksheets and grid locations for reading data from the Microsoft Excel source files.

The table contains the following columns:

| Column           | Description                                                                                          |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| **Sheet name**   | The name of the sheet in the Excel workbook to read                                                  |
| **Start row**    | The starting row in the sheet to read. The row numbers are zero-based (start at the number 0).       |
| **Start column** | The starting column in the sheet to read. The column numbers are zero-based (start at the number 0). |

You can also read all the sheets in a workbook by clearing the table and typing only the start row and column in the first row, which will be used for all sheets. To read all the sheets in a workbook, do not specify any sheet name (leave **Sheet name** blank). For this case, the field structure of each sheet needs to be the same.

Click **Get sheetname(s)** to fill out the table with all the sheets from your source specified by **File or directory** in the **Files** tab.
