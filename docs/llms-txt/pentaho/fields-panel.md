# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-writer/options-microsoft-excel-writer/content-tab/fields-panel.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/microsoft-excel-writer/options-microsoft-excel-writer/content-tab/fields-panel.md

# Fields panel

This panel includes the **Fields** table for specifying the fields written to Excel files. The **Fields** table contains the following columns:

| Column                            | Description                                                                                                                                                                                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Name**                          | The name of the field.                                                                                                                                                                           |
| **Type**                          | The data type of a field: String, Date, or Number.                                                                                                                                               |
| **Format**                        | The Excel format to use in the sheet. Consult the MS Excel documentation or online references for valid formats.                                                                                 |
| **Style from cell**               | A cell in the Excel spreadsheet (letter column, number row) such as `A1`, `B4`, etc., to copy the styling from for this column. This value is usually a pre-styled cell in a template.           |
| **Field title**                   | If set, this is used for the Header/Footer instead of the Kettle field name.                                                                                                                     |
| **Header/Footer style from cell** | A cell to copy the styling from for the Header/Footer (usually some pre-styled cell in a template).                                                                                              |
| **field contains formula**        | <p>Set to <code>Yes</code> if the field contains an Excel formula.</p><p>You do not need to include the notation <code>=</code> before your field value.</p>                                     |
| **Hyperlink**                     | A field that contains the target to link to. Supported targets can be links to other Excel spreadsheet cells, website URL's, ftp's, email addresses, or local documents.                         |
| **Cell comment (XLSX)**           | The .`.xlsx` format allows you to put comments on cells. If you would like to generate comments, you may specify fields holding the comment for a given column.                                  |
| **Cell comment author (XLSX)**    | The `.xlsx` format allows you to put the author's name of a comment on cells. If you would like to generate comments, you may specify fields holding the author of a comment for a given column. |
