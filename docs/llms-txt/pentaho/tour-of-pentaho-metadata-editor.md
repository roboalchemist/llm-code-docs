# Source: https://docs.pentaho.com/pba-metadata-editor/readme/tour-of-pentaho-metadata-editor.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/get-started-with-pentaho-metadata-editor-cp/tour-of-pentaho-metadata-editor.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/get-started-with-pentaho-metadata-editor-cp/tour-of-pentaho-metadata-editor.md

# Tour of Pentaho Metadata Editor

The following steps show you how to use an example metadata model in Pentaho Metadata Editor to create an Interactive Reports.

**Note:** The Pentaho Server must be running for this process to work.

1. Start Metadata Editor and then go to **File** > **Import from XMI File**.

   The Open window opens.
2. Browse to `pentaho/design-tools/metadata-editor/samples`.

   The files in the `Samples` folder are shown.
3. Select the `steel-wheels` file and then click **Open**.

   The Save Model dialog box opens.
4. In the **Enter a name for this model** field, enter `Sample Data` and then click **OK**.

   If the message, This model already exists..., appears, click **Yes** to continue.

   The Sample Data domain page appears. The navigation pane on the left shows the **Connections** and **Business Models** that comprise the `Sample Data` model in the repository. The main pane on the page provides the **Graphical View**, **Locales**, and **Log View** tabs.

   ![Pentaho Metadata Editor, Sample Data example](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-14d4fdf0a5808a094459e48f262d9c504e8c1208%2FPME_main_page.png?alt=media)
5. Log in to the Pentaho User Console, and then click **Create New** > **Interactive Report**.

   The Select Data Source dialog box opens.

   ![Interactive Report's Select Data Source dialog box](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-8f64a90a41f2d0932b07d3ca53d2c55930638df8%2FPUC_InteractiveReport_Select_data_source_dialog.png?alt=media)
6. Choose the data source that you want to use for the report, then click **OK**.

   The Human Resources data source is chosen in this example. The data sources from Metadata Editor’s generated business models for the Sample Data model are listed.

   The report canvas opens.

   ![Interactive Report canvas](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-b11315c2a4cf544013822187896c0578ac8fcb0a%2FPUC_InteractiveReport_canvas.png?alt=media)
7. From the **Data** tab, drag and drop an Offices field onto the report canvas.

   The data populates a column in the report.
8. Drag and drop an Employees field onto the report canvas.

   The data populates a second column in the report.

The basic elements of the report are complete.

For additional report settings and options and to save the report, see **Create an Interactive Report** in the **Pentaho Business Analytics** document for details.
