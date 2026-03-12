# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/working-with-analyzer-fields/format-field-options.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/format-field-options.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/format-field-options.md

# Format field options

The **Format** field for [Properties](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/viewing-and-editing-field-properties) allows users to select values based on numerals and calendar dates. Below is a list of supported numeric and date formats you can select for the field or measure.

![Format field options](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-ed6fcf8177bee442dbe1c306af7e78fb78811429%2FAnalyzer_FormatFieldOptions.png?alt=media)

For more detailed information about numeric and date format strings, view [this article about MDX and format definitions](https://msdn.microsoft.com/en-us/library/ms146084.aspx).

| Format String         | Result         |
| --------------------- | -------------- |
| 0                     | 12345          |
| 0.00                  | 12345.09       |
| #,##0                 | 12, 345        |
| #,###.00              | 12, 345.09     |
| -#,###.00             | -12, 345.09    |
| (#,###.00)            | (12, 345.09)   |
| $ #,##0               | $ 12, 345      |
| $ #,##0.00            | $ 12, 345.09   |
| $ -#,##0.00           | $ -12, 345.09  |
| $ (#,##0.00)          | $ (12, 345.09) |
| $ #,##0.00;(#,##0.00) | $ 12, 345.09   |
| 0 %                   | 1234509 %      |
| 0.00 %                | 1234509.00 %   |
| #E+#                  | 1E+4           |
| 0.00E+00              | 1.23E+04       |
| ##0.0E+0              | 1.2E+4         |

| Format String     | Example          |
| ----------------- | ---------------- |
| M/d               | 4/1              |
| M/d/yy            | 4/1/16           |
| MM/dd/yy          | 04/01/16         |
| d-MMM             | 1-Apr            |
| d-MMM-yy          | 1-Apr-16         |
| MMM-yy            | Apr-16           |
| MMMMM-yy          | April-16         |
| MMMMM d, yyyy     | April 1, 2016    |
| M/d/yy h:mm AM/PM | 4/1/2016 8:09 PM |
| M/d/yy h:mm       | 4/1/2016 20:09   |
| M/d/yyyy          | 4/1/2016         |
| d-MMM-yyyy        | 1-Apr-2016       |
| h:mm              | 20:09            |
| h:mm AM/PM        | 8:09 PM          |
| h:mm:ss           | 20:09:06         |
| h:mm:ss AM/PM     | 8:09:06 PM       |
| \[h]:mm:ss        | \[20]:09:06      |
