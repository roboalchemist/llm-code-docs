# Source: https://docs.pentaho.com/pba/data-source-wizard-cp-overview/choose-a-data-source-type/create-a-csv-data-source.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/data-source-wizard-cp-overview/choose-a-data-source-type/create-a-csv-data-source.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/data-source-wizard-cp-overview/choose-a-data-source-type/create-a-csv-data-source.md

# Create a CSV data source

Before you begin working with CSV data sources, there are a few key terms that you should know.

* **Delimiter**

  A character, such as a comma, used to specify a boundary between separate regions in a data stream.
* **Enclosure**

  A container that holds a collection of other data objects.
* **Length**

  Indicates the maximum number of characters allowed in a field.
* **Precision**

  The number of digits after a decimal point.

1. Log in to the **User Console**.
2. Click **Create New**, then choose **Data Source**from the menu.
3. Click **New Data Source**. The **Data Source Wizard** appears.
4. Enter a name that identifies your new data source in the **Data Source Name** field. The following characters are not allowed in data source names:

   ```
   %/:[]*|\t\r\n
   ```

   ![Data Source Wizard](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-5dd3beda253496e95bfda946357556af67372117%2FPUC_Data_Source_Wizard_CSV.png?alt=media)
5. Select **CSV File** from the **Source Type** drop-down menu.
6. Click **Import** to browse for your CSV file. Double-click to select the CSV file you want to upload.
7. Choose your delimiter and enclosure types.

   If you want to use the first row as data, disable the **First row is header** check box.

   ![Data Source Wizard CSV First row is header](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-373791ec8b7aa312a4af9d6bc8d51e08bc0e7675%2FPUC_Data_Source_Wizard_CSV_First_row_is_header.png?alt=media)
8. The **File Preview** window displays the first few lines of your CSV file based on the selections you made for the delimiter, enclosure, and header. Once the columns align correctly in the preview, the delimiter and enclosure have been set correctly.

   If you want to use the first row of your CSV file as headings for columns in the file, leave **First row is header** check box selected.
9. Click **Next**.

   The **Staging Settings** screen displays a list of columns from your CSV source file. All columns are enabled.

   ![Data Source Wizard Staging Settings](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-7500fd0c2c1da50579bf90637e3d4f243802a1fc%2FPUC_Data_Source_Wizard_Staging_Settings.png?alt=media)
10. Choose the columns that you want to use in your data source, either individually or by clicking **Select All**.

    You can deselect all columns by clicking **Deselect All**.
11. Change the **Name** and **Type** values, if applicable.
    1. Choose the options that you want to use from the drop-down menu for dates and numeric values.
    2. You can enter a value manually in the **Source Format** text box.**Note:** Drop-down lists are not enabled for certain data types such as the String data type. Boolean values are rendered as **true** or **false**.
12. Click **Show File Contents** to look at a sample of the data in your source file. Click **Close** to return to the **Staging Settings** screen.

    ![Data Source Wizard File Preview](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-c3ed3a9670a8e3bd4121e13584c4769fe0fedfcc%2FPUC_Data_Source_Wizard_File_Preview.png?alt=media)
13. Continue to work with your CSV data settings or click **Finish**.

    The **Data Source Created** window appears.
14. You can choose to **Keep default model** or click **Customize model now** to launch the Data Source Model Editor and refine the model. Click **OK**.

Your new data source is now available for use in Analyzer, Interactive Reports, and Dashboard Designer reports, or the [Data Source Model Editor](https://docs.pentaho.com/pba/10.2-analytics/data-source-model-editor-cp) appears.
