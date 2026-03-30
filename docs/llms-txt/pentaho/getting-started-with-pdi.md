# Source: https://docs.pentaho.com/pdia-try-pdia/getting-started-with-pdi.md

# Getting Started with PDI

If you are new to Pentaho Data Integration, start here.

Use these tutorials to build your first transformations and jobs in Spoon.

### In this topic

* [Pentaho Data Integration (PDI) tutorial](#pentaho-data-integration-pdi-tutorial)
* [PDI job tutorial](#pdi-job-tutorial)
* [Getting started with PDI and Hadoop](#getting-started-with-pdi-and-hadoop)

### Pentaho Data Integration (PDI) tutorial

The following tutorial is intended for users who are new to the Pentaho suite or who are evaluating Pentaho as a data integration and business analysis solution. The tutorial consists of six basic steps, demonstrating how to build a data integration transformation and a job using the features and tools provided by Pentaho Data Integration (PDI).

The Data Integration perspective of PDI allows you to create two basic file types: transformations and jobs. Transformations describe the data flows for ETL such as reading from a source, transforming data and loading it into a target location. Jobs coordinate ETL activities such as defining the flow and dependencies for what order transformations should be run, or prepare for execution by checking conditions such as, "Is my source file available?" or "Does a table exist in my database?"

The aim of this tutorial is to walk you through the basic concepts and processes involved in building a transformation with PDI in a typical business scenario. In this scenario, you are loading a flat file (CSV) of sales data into a database to generate mailing lists. Several of the customer records are missing postal codes that must be resolved before loading into the database. In the preview feature of PDI, you will use a combination of steps to cleanse, format, standardize, and categorize the sample data. The six basic steps are:

1. Step 1: Extract and load data
2. Step 2: Filter for missing codes
3. Step 3: Resolve missing data
4. Step 4: Clean the data
5. Step 5: Run the transformation
6. Step 6: Orchestrate with jobs

#### Prerequisites

To complete this tutorial, you need the following items:

* An installed version of the [Pentaho 30-day trial](https://www.hitachivantara.com/en-us/products/data-management-analytics/pentaho-platform/pentaho-data-integration/pentaho-trial-download.html).

#### Step 1: Extract and load data

In Step 1, you will retrieve data from a CSV flat file and use the Text File Input step to connect to a repository, view the file schema, and retrieve the data contents.

**Create a new transformation**

Follow these steps to create a new transformation.

If you want to insert a variable into a field that accepts variables, you can put your cursor in the fields and press **CTRL+Spacebar** to see a list of variables to insert. Fields that accept variables have a blue diamond.

1. Select **File** > **New** > **Transformation** in the upper-left corner of the PDI window.

   ![](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-2b2a8afe8c01bfdff955fc6c660fb69cf4e54917%2FDesign%20list%20with%20metatdata%20discovery.png?alt=media)
2. Under the **Design** tab, expand the **Input** node, then select and drag a Text File Input step onto the canvas.
3. Double-click the Text File input step. In the Text file input window, you can set the properties of the step.

   ![Text File Input File tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-7dcb73e05215aedada34b2cddb2af13df065de3a%2Fpdi_tutorial_text_file_input_step_w532.png?alt=media)
4. In the **Step Name** field, type `Read Sales Data`.

   The Text file input step is now renamed to Read Sales Data.
5. Click **Browse** to locate the `sales_data.csv` source file in the `...\design-tools\data-integration\samples\transformations\files` folder. The **Browse** button appears in the upper-right side of the window near the **File or Directory** field.
6. Change **File type** to `*.csv`. Select `sales_data.csv`, then click **OK**​.

   The path to the source file appears in the **File or directory** field.
7. Click **Add**.

   The path to the file appears under **Selected Files**.

**View the content in the sample file**

Follow these steps to look at the contents of the sample file.

1. Click the **Content** tab, then set the **Format** field to **Unix**​.
2. Click the **File** tab again and click the **Show file content** in the lower section of the window.
3. The Number of lines (0-all lines) window appears. Click **OK** to accept the default.
4. The Content of first file window shows the file. Examine the file to see how that input file is delimited, what enclosure character is used, and whether or not a header row is present.

   In the sample, the input file is comma delimited, using the enclosure character of a quotation mark ("). It contains a single header row containing field names.
5. Click the **Close** button to close the window.

**Edit and save the transformation**

Follow these steps to provide information about the data's content.

1. Click the **Content** tab. Use the fields under the **Content** tab to define how your data is formatted.
2. Verify that the **Separator** is set to comma (,) and that the **Enclosure** is set to quotation mark ("). Select **Header** and enter `1` in the **Number of header lines** field.

   ![Text File Input Content tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-3d044838f0a501a3bff891adeb4ff4451f4f6241%2Fpdi_tutorial_Text_File_Input_content_tab_w532.png?alt=media)
3. Click the **Fields** tab and click **Get Fields** to retrieve the input fields from your source file. When the Number of lines to sample window appears, enter `0` in the field, then click **OK**.
4. If the Scan Result window displays, click **Close** to close the window.

   ![Text File Input Fields tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-e7f38a3758b4da24d24d7c7c6b2e00799900af93%2Fpdi_tutorial_Text_File_Input_scan_results_w532.png?alt=media)
5. To verify that the data is read correctly, click the **Content** tab, then click **Preview Rows**.
6. In the Enter the number of rows you would like to preview window, click **OK** to accept the default.

   The Examine preview data window appears.
7. Review the data. Do you notice any missing, incomplete, or variations of the data?
   * `STATE & POSTALCODE` both contain `<null>`
   * `COUNTRY` contains both `USA` and `United States`.
8. Click **OK** to save the information that you entered in the step.
9. Enter a name for the transformation and provide additional properties using the Transformation Properties window. There are multiple ways to open the Transformation Properties window.
   * Right-click any empty space on the canvas and select **Properties**.
   * Double-click any empty space on the canvas to select **Properties**.
   * Enter the CTRL-T keyboard combination.
10. In the **Transformation Name** field, enter `Getting Started Transformation`.

    Below the name, the filename is empty.
11. Click **OK** to close the Transformation Properties window.
12. To save the transformation, select **File** > **Save**.

    When saving your transformation for the first time, you are prompted for a file location and name of your choice. The file extension `.ktr` is the usual file extension for transformations.

**Load data into a relational database**

Now you are ready to take all the records that are exiting the Filter Rows step (added in Step 2) where the **POSTALCODE** was not null (the **true** condition) and load them into a database table. You will use the Table Output step and a hop from the Text File Input step to direct the data stream into a database table. This section of the tutorial uses a pre-existing database established during the Pentaho installation, which is started along with the server.

**Create the Table Output step**

Follow these instructions to create the Table Output step.

1. Under the **Design** tab, expand the contents of the **Output** node.
2. Click and drag a Table Output step into your transformation.
3. Create a hop between the Read Sales Data and Table Output steps. To create the hop:
   1. Press the SHIFT key.
   2. Click the Read Sales Data (Text File Input) step and drag the mouse to draw a line to the Table Output step.
   3. Release the SHIFT key.
   4. Click the Table Output step.
4. Double-click the Table Output step to open its **Edit properties** dialog box.
5. Rename your Table Output step to Write to Database.

**Create a connection to the database**

Follow these steps to create a connection to the database.

1. Click **New** next to the **Connection** field. You must create a connection to the database.

   The Database Connection window appears.
2. Provide the settings for connecting to the database.

   | Field               | Setting                                                                              |
   | ------------------- | ------------------------------------------------------------------------------------ |
   | **Connection Name** | Sample Data                                                                          |
   | **Connection Type** | Hypersonic                                                                           |
   | **Host Name**       | localhost                                                                            |
   | **Database Name**   | sampledata                                                                           |
   | **Port Number**     | 9001                                                                                 |
   | **User Name**       | pentaho\_admin                                                                       |
   | **Password**        | password (If `password` does not work, please check with your system administrator.) |
3. Click **Test** to verify your entries are correct. A success message appears. Click **OK**.

   **Note:** If you get an error when testing your connection, ensure that you have provided the correct settings information as described in the table and that the sample database is running. Depending on your platform, see [Start and stop the Pentaho Server for configuration on Windows](https://github.com/pentaho/documentation/blob/main/PDIA/11.0/Get%20Started/Pentaho%20evaluation/Start%20and%20stop%20the%20Pentaho%20Server%20for%20configuration%20on%20Windows=GUID-2DF3CCF0-39D7-4BC4-8129-AE3C6A3FBD60=1=en=.md) or [Start and stop the Pentaho Server for configuration on Linux](https://docs.pentaho.com/pdia-try-pdia/archive-flattened-pages-do-not-use/install-trial-legacy-child-pages/start-and-stop-the-pentaho-server-for-configuration-on-linux).
4. Click **OK** to exit the Database Connections window.

**Define the Data Definition Language (DDL)**

DDLs are the SQL commands that define the different structures in a database such as `CREATE TABLE`. Fortunately, Pentaho can help you create the necessary DDL.

1. Enter `SALES_DATA` in the **Target Table** text field.
2. This table does not exist in the target database, so Pentaho can generate the DDL to create the table and execute it. In this scenario, the DDL is based on the stream of data coming from the previous step, which is the Read Sales Data step.
3. In the Table Output window, select the **Truncate Table** property.

   ![Table Output step Truncate table field](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-bbf4ec48bbf8594dffc1d93b8b8acef29c2b849c%2Fpdi_tutorial_table_output_truncate_table_property_532.png?alt=media)
4. Click the **SQL** button in the bottom of the Table output dialog box to generate the DDL for creating your target table.
5. The Simple SQL editor window appears with the SQL statements needed to create the table.

   ![Simple SQL editor](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-7e278b742b5d6a35af4ddf0197609dcf0613cc11%2Fpdi_tutorial_simple_sql_editor_w395.png?alt=media)
6. Click **Execute** to execute the SQL statement.

   The Results of the SQL statements window appears.
7. Examine the results, then click **OK** to close the Results of the SQL statements window.
8. Click **Close** in the Simple SQL editor window
9. Click **OK** to close the Table output window.
10. Save your transformation.

#### Step 2: Filter for missing codes

After completing Step 1: Extract and load data, you are ready to add a transformation component to your data pipeline. The source file contains several records that are missing postal codes. This section of the tutorial filters out those records that have missing postal codes, where the POSTALCODE is not null (the true condition), and ensures that only complete records are loaded into the database table.

**Preview the rows read by the input step**

Follow these steps to preview the rows read by the input step.

1. Right-click the Read Sales Data step and select **Preview**.

   ![Transformation Menu showing how to access Preview](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-093ee170a56a7addec5c96f105454723e81f15a4%2Fpdi_tutorial_new_transformation_how_to_access_preview_w499.png?alt=media)
2. Specify the number of rows to preview. Optionally, you can configure breakpoints which pause execution based on a defined condition, such as a field having a specific value or exceeding a threshold.
3. Click the **Quick Launch** button. Preview the data and notice that several of the input rows are missing values for the **POSTALCODE** field.

   ![Preview showing missing postalcode fields](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-e780416b1a3ef58c7b7cb9ce383e9dff046eac95%2Fpdi_tutorial_new_transformation_preview_with_missing_postal_codes_w532.png?alt=media)
4. Click **Stop** on the preview window to end the preview.

**Separate the records with missing postal codes**

Follow these instructions to use the Filter Rows transformation step to separate out those records missing postal codes. These records are resolved later in the tutorial.

1. Add a Filter Rows step to your transformation. Under the **Design** tab, select **Flow** > **Filter Rows**.
2. Insert your Filter Rows step between your Read Sales Data step and your Write to Database step.

   1. Right-click and delete the hop between the Read Sales Data step and Write to Database steps.
   2. Create a hop between the Read Sales Data step and the Filter Rows step. Create a hop by clicking the step, and then hold the SHIFT key down and click-and-drag to draw a line to the next step.
   3. Create a hop between the Filter Rows step and Write to Database step.
   4. In the dialog box that appears, select **Result is TRUE.**

   ![Hop dialog set to Result is True](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-1b5bbf3de80233c6470290e9aa25c65831a1e747%2Fpdi_tutorial_new_transformation_filter_results_is_true_w522.png?alt=media)
3. Double-click the Filter Rows step. The Filter Rows window appears.
4. In the **Step Name** field, enter `Filter Missing Zips`.
5. Click in **The condition** field to open the Fields window. The available conditions appear.
6. In the **Fields** window select **POSTALCODE** and click **OK**.
7. Click the comparison operator field, which is set to **=** by default. The Functions window appears.
8. Select **IS NOT NULL** from the list of functions, and then click **OK**​ to close the Functions window.

   ![Filter rows is set postalcode is not null](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-cf03b6964a3e2b63e8fd75ac7050a2eaf5c7c3fe%2Fpdi_tutorial_new_transformation_filter_rows_is_null_w532.png?alt=media)
9. Click **OK** to exit the Filter Rows window.

   **Note:** You will return to this step later to configure the **Send true data to step** and **Send false data to step** settings after adding their target steps to your transformation.
10. Save your transformation.

#### Step 3: Resolve missing data

After completing Step 2: Filter for missing codes, you are ready to resolve the missing postal codes. In this section, you will learn how to use a second text file containing a list of cities, states, and postal codes, to look up the postal codes for those records in which the fields are missing, which is the false branch of your Filter rows step.

First, you will use a Text file input step to read from the source file. Then, you will use a Stream lookup step to bring the resolved postal codes into the stream. Lastly, you will use the Select values step to rename fields on the stream, remove unnecessary fields, and more.

**Retrieve data from your lookup file**

Follow these steps to retrieve data from your lookup file.

1. Add a new Text File Input step to your transformation.

   This step retrieves the records from your lookup file. Do not add a hop yet.

   ![Add Text File Input step to canvas](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-859c25f009bd5760018f4f78493f7af4743c1af3%2Fpdi_tutorial_add_text_file_input_step_to_canvas_w391.png?alt=media)
2. Open the Text File Input step window, then enter `Read Postal Codes` in the **Step name** property.
3. Click **Browse** to navigate to the `Zipssortedbycitystate.csv` source file located in the directory `...\design-tools\data-integration\samples\transformations\files`.
4. Change **File type** to `*.csv`, select `Zipsortedbycitrystate.csv`, and click **OK**.

   The path to the source file appears in the **File or directory** field.
5. Click **Add**.

   The path to the file appears under **Selected files**.

**View the contents of the sample file**

Follow these steps to view the contents of the sample file.

1. Click the **Content** tab, then set the **Format** field to **Unix**​.
2. Click the **File** tab again and click the **Show file content** near the bottom of the window.
3. The Number of lines(0=all lines) window appears. Click the **OK**button to accept the default.
4. The **Content of first file** window shows the file. Examine the file to see how that input file is delimited, what enclosure character is used, and whether a header row is present. In the example, the input file is comma (,) delimited and the enclosure character is the quotation mark ("). A single header row contains field names.
5. Click **Close** to close the window.

**Edit and save the transformation**

Follow these steps to edit and save your transformation.

1. In the **Content** tab, change the **Separator** character to a comma (,) and confirm that the **Enclosure** setting is a quotation mark ("). Verify that the **Header** option is selected.
2. Under the **Fields** tab, click **Get Fields** to retrieve the data from your CSV file.
3. The Number of lines to sample window appears. Enter `0` in the field, then click **OK.**

   ![Results from Get Fields in the Fields tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-156081d05838b488762dbc18fbb967cb4ac94477%2Fpdi_tutorial_retrieve_fields_w532.png?alt=media)
4. If the Scan Result window displays, click **Close** to close it.
5. Click **Preview rows** to verify that your entries are correct.
   1. When prompted to enter the preview size, click **OK**.
   2. Review the information in the window, then click **Close**.
6. Click **OK** to exit the Text File input window.
7. Save the transformation.

**Resolve missing zip code information**

Follow these steps to resolve the missing postal code information.

1. Add a Stream Lookup step to your transformation by clicking the **Design** tab, expanding the **Lookup** folder, then selecting **Stream Lookup**.
2. Draw a hop from the Filter Missing Zips to the Stream lookup step. In the dialog box that appears, select **Result is FALSE**.
3. Create a hop from the Read Postal Codes step to the Stream lookup step.

   ![Add a hop from Read Postal Codes to Stream Lookup](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d123518de033472219109e298137fee0714c7069%2Fpdi_tutorial_add_hop_from_read_postal_codes_to_steam_lookup_w372.png?alt=media)
4. Double-click the Stream lookup step to open the Stream Value Lookup window.
5. Rename Stream Lookup to Lookup Missing Zips.
6. From the Lookup step drop-down box, select **Read Postal Codes** as the lookup step. Perform the following:
   1. In the **key(s) to look up the value(s)** table, define the **CITY** and **STATE** fields .
   2. In **row #1**, open the drop-down menu in the **Field** column and select **CITY**.
   3. Click in the **LookupField** column and select **CITY**.
   4. In **row #2**, open the drop-down menu in the **Field** column and select **STATE**.
   5. Click in the **LookupField** column and select **STATE**.

      ![Stream value lookup example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-566dab0ca0abadc797c3ea4c1faee737b6f4f34b%2Fpdi_tutorial_lookup_state_w532.png?alt=media)
7. Click **Get Lookup Fields** to pull the three fields from the Read Postal Code step.
8. **POSTALCODE** is the only field you want to retrieve. To delete the **CITY** and **STATE** lines, right-click in the line and select **Delete Selected Lines**.
9. In the **New Name** field, change the name **POSTALCODE** to **ZIP\_RESOLVED** and verify that **Type** is set to **String**.
10. Select **Use sorted list (i.s.o. hashtable)**.

    ![Value lookup example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-3e94f028e77815c72a691acd2f11e787b228bc63%2Fpdi_tutorial_use_sorted_list_w532.png?alt=media)
11. Click **OK** to close the Stream Value Lookup edit properties dialog box.​​
12. Save your transformation.

**Preview your transformation**

Follow these steps to preview your transformation.

1. To preview the data, select and right-click the Lookup Missing Zips step. From the menu that appears, select **Preview**.
2. In the Transformation debug dialog window, click **Quick Launch** to preview the data flowing through this step.
3. In the Examine preview data window that appears, note that the new field, **ZIP\_RESOLVED**, has been added to the stream containing your resolved postal codes.

   ![Examine ZIP\_RESOLVED field](broken-reference)
4. Click **Close** to close the window.
5. If the Select the preview step window appears, click **Close**.

The execution results near the bottom of the PDI window show updated metrics in the **Step Metrics** tab.

**Apply formatting to your transformation**

Follow these steps to clean up the field layout on your lookup stream so that it matches the format and layout of the other stream going to the Write to Database step.

1. Add a Select Values step to your transformation by expanding the **Transform** folder and clicking Select Values.
2. Create a hop from the Lookup Missing Zips to the Select Values step.

   ![Add hop from Lookup Missing Zips to Select Values](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-74f97aed4729d8d76a1886ad045ddd9c1d5595a4%2Fpdi_tutorial_add_hop_from_lookup_missing_zips_to_select_values_w466.png?alt=media)
3. Double-click the Select Values step to open its properties dialog box.
4. Rename the Select Values step to Prepare Field Layout.
5. Click **Get fields to select** to retrieve all fields and begin modifying the stream layout.
6. In the **Fields** list, find the **#** column and click the number for the **ZIP\_RESOLVED** field.

   Use CTRL+UP (Windows/Linux) or COMMAND+UP (macOS) to move **ZIP\_RESOLVED** just below the **POSTALCODE** field, which is the one that still contains null values.

   ![Move ZIP\_RESOLVED field under POSTALCODES field](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-08456645bd9a2a2664a986c4241e7b2ee96ae1b6%2Fpdi_tutorial_mov_zip_resolved_fields_under_postal_codes_field_w532.png?alt=media)
7. Select the old **POSTALCODE** field in the list (line 20), right-click in the line, and select **Delete Selected Lines**
8. The original **POSTALCODE** field was formatted as a 9-character string. You must modify your new field to match the form. Click the **Meta-Data** tab.
9. In the first row of the **Fields to alter table the meta-data for** section, click in the **Fieldname** column and select **ZIP\_RESOLVED**. Perform the following steps:
   1. Enter `POSTALCODE` in the **Rename to** column.
   2. Select **String** in the **Type** column and enter `9` in the **Length** column.

      ![POSTALCODE String type and length](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-bb60cad84959554e60f3912950667cab74be81db%2Fpdi_tutorial_postal_code_string_and_length_w532.png?alt=media)
   3. Click **OK** to exit the **edit properties** dialog box.
10. Draw a hop from the Prepare Field Layout (Select values) step to the Write to Database (Table output) step.
11. When prompted, select the **Main output of the step** option.
12. Save your transformation.

    ![Renaming fields workflow example](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-20b8a5eb7bef00edf14857e375ddeb6d0a61fd4c%2Fpdi_tutorial_save_transformation_w532.png?alt=media)

#### Step 4: Clean the data

After completing Step 3: Resolve missing data, you can further cleanse and categorize the data into buckets before loading it into a relational database. In this section, you will cleanse the `COUNTRY` field data by mapping `United States` to `USA` using the Value mapper step. Cleaning the data ensures there is only one version of `USA`.

In addition, you will learn how to use buckets for categorizing the `SALES` data into small, medium, and large categories using the Number range step. You will learn how to insert these cleaning and categorizing functions into your transformation just prior to the Write to Database step on the canvas.

**Add a Value mapper step to the transformation**

Follow these steps to add the Value mapper step to the transformation.

1. Delete both hops connected to the Write to Database step. For each hop, right-click and select **Delete**.
2. Create some extra space on the canvas. Drag the Write to Database step toward the right side of your canvas.

   ![Add space on canvas for Value mapper step](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-a2d7f9799a6ad39b29926b4aa5dcf46d5a75ecea%2Fpdi_tutorial_add_space_on_canvas_for_value_mapper_step_w532_001.png?alt=media)
3. Add the Value mapper step to your transformation by expanding the **Transform** folder and choosing **Value mapper**.
4. Create a hop between the Filter Missing Zips and Value mapper steps. In the dialog box that appears, select **Result is TRUE**.
5. Create a hop between the Prepare Field Layout and Value mapper steps. When prompted, select the **Main output of the step** option.

   ![Add Value mapper step to the canvas](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-c32e0e1552a581cbbbfc9b7f8a691005032ca507%2Fpdi_tutorial_add_value_mapper_step_to_canvas_w532_002.png?alt=media)

**Set the properties in the Value Mapper step**

Follow these steps to set the properties in the Value mapper step.

1. Double-click the Value mapper step to open its properties dialog box.
2. Click in the **Fieldname to use** field and select **COUNTRY**.
3. In the **Field Values** table, define the `United States` and `USA` field values.
   1. In row #1, click the field in the **Source value** column and enter `United States`
   2. Then, click the field in the **Target value** column and enter `USA`

      ![Set values for fields in the Value mapper step](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-2a10691c56f86b064acb287d8dbeffb425f81222%2Fpdi_tutorial_set_properties_in_value_mapper_step_w532_003.png?alt=media)
4. Click **OK**.
5. Save your transformation.

**Apply ranges**

Follow these steps to apply ranges to your transformation.

1. Add a Number range step to your transformation by expanding the **Transform** folder and selecting **Number range**.
2. Create a hop between the **Value mapper** and **Number range** steps.
3. Create a hop between the Number range and Write to Database (which was built using Table output) steps. When prompted, select the **Main output of the step** option.

   ![Add Number range step to the canvas](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-1f76478db2fd4f7dd9ddb8c3d0b9767f5e11f9c4%2Fpdi_tutorial_add_number_range_step_to_canvas_w532_004.png?alt=media)
4. Double-click the Number range step to open its **properties** dialog box.
5. Click in the **Input field** and select **SALES** from the list.
6. In the **Output field** enter `DEALSIZE`.
7. In the **Ranges (min <=x< max)** table, define the **Lower Bound** and **Upper Bound** field ranges along with the bucket **Value**.
   1. In row #1, click the field in the **Upper Bound** column and enter `3000.0`. Then, click the field in the **Value** column and enter `Small`.
   2. In row #2, click the field in the **Lower Bound** column and enter `3000.0`. Then, click the field in the **Upper Bound** column and enter `7000.0`. Click the field in the **Value** column and enter `Medium`.
   3. In row #3, click the field in the **Lower Bound** column and enter `7000.0`. Then, click the field in the **Value** column and enter `Large`.

      ![Set ranges in Number Range step](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-d5f484d9a0fa34538ced8412ad7a8b85bcd8e4ab%2Fpdi_tutorial_set_ranges_in_number_range_step_w532_005.png?alt=media)
8. Click **OK**.

**Execute the SQL statement**

Your database table does not yet contain the field `DEALSIZE`. Perform these steps to execute the SQL statement.

1. Double-click the Write to Database step to open its properties dialog box.
2. Click the **SQL** button at the bottom of the window to generate the new DDL for editing your original target table. Note that the Write to Database step was built using Table output.
   1. The **Simple SQL editor** window appears with the SQL statements needed to `alter` the table.

      ![Simple SQL editor to generate the DDL](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-e79f63e267d4a35d3835f29184d3a18a8785162b%2Fpdi_tutorial_simple_sql_editor_to_generate_ddl_w455_006.png?alt=media)
   2. Click **Execute** to execute the SQL statement.
   3. The Results of the SQL statements window appears. Examine the results, then click **OK** to close the window.
   4. Click **Close** in the Simple SQL editor window to close it.
   5. Click **OK** to close the Write to Database window. Note that the Write to Database step was built using Table output
3. Save your transformation.

#### Step 5: Run the transformation

Pentaho Data Integration provides a number of deployment options. The **Running a Transformation** section in the **Pentaho Data Integration** document explains these and other options available for execution. In this section of the tutorial, you create a transformation using the **Local** run option.

1. In the PDI client window, select **Action** > **Run**.

   The Run Options window appears.
2. Keep the default **Pentaho local** option for this exercise.

   It uses the native Pentaho engine and runs the transformation on your local machine. See the **Pentaho Data Integration** document if you are interested in setting up configurations that use another engine.
3. Click **Run**.

   The transformation executes.

   ![Transformation runs without errors](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-a9eb59d912a8c7a9e2bb4592cf9372ef3fef269c%2Fpdi_tutorial_transformation_ran_good_w552.png?alt=media)

After the transformation runs, the **Execution Results** panel opens below the canvas.

**Viewing the execution results**

Use the tabs in the **Execution Results** section of the window to view how the transformation executed, pinpoint errors, and monitor performance.

* **Step Metrics**

  Provides statistics for each step in your transformation including how many records were read, written, or caused an error, as well as processing speed (rows per second) and more. This tab also indicates whether an error occurred in a transformation step.

  This tutorial introduces no intentional transformation errors, so the transformation should run correctly. If a mistake does occur, you can view the steps that caused the transformation to fail highlighted in red. In the example below, the Lookup Missing Zips step caused an error.

  ![Error message display](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-845e491680e7ccbc8d7397d0e78bed87db04eece%2Fpdi_tutorial_transformation_ran_with_errors_w532.png?alt=media)
* **Logging**

  Shows the logging details for the most recent execution of the transformation. It also allows you to drill deeper to determine where errors occur. Error lines are highlighted in red. In the example below, the **Lookup Missing Zips** step caused an error because it attempted to look up values on a field called **POSTALCODE2** which did not exist in the lookup stream.

  ![Transformation logging display](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-9b168628910e2d5daa4b15ada360973c64f1ed73%2Fpdi_tutorial_transformation_logging_display_w532.png?alt=media)
* **Execution History**

  Provides access to the step metrics and log information from previous executions of the transformation. This feature works only if you have configured your transformation to log to a database through the **Logging** tab of the Transformation Settings dialog box.
* **Performance Graph**

  Analyzes the performance of steps based on a variety of metrics including how many records were read, written, or caused an error, as well as processing speed (rows per second) and more. Like the execution history, this feature requires you to configure your transformation to log to a database through the **Logging** tab found in the Transformation Settings dialog box.
* **Metrics tab**

  Shows a Gantt chart after the transformation or job runs. This information includes how long it takes to connect to a database, the time spent executing a SQL query, or the load time of a transformation.

  ![Step metrics tab](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-de2390bd39457804598553cd27afa48acd0e52de%2Fpdi_tutorial_transformation_metrics_tab_w532.png?alt=media)
* **Preview Data**

  Shows a preview of the data.

#### Step 6: Orchestrate with jobs

Jobs are used to coordinate ETL activities such as:

* Defining the flow and dependencies that control the linear order for the transformations to run.
* Preparing for execution by checking conditions such as, "Is my source file available?" or "Does a table exist?"
* Performing bulk load database operations.
* Assisting file management, such as posting or retrieving files using FTP, copying files, and deleting files.
* Sending success or failure notifications through email.

For this part of the tutorial, imagine that an external system is responsible for placing your `sales_data.csv` input in its source location every Saturday night at 9 p.m. You want to create a job that will verify that the file has arrived and then run the transformation to load the records into the database. In a subsequent exercise, you will schedule the job to run every Sunday morning at 9 a.m.

The following steps assume that you have built a Getting Started transformation as described in Step 1: Extract and load data of the tutorial.

1. Go to **File** > **New** > **Job**.

   ![PDI job window](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-191884ec46461d9ebaeef5f08f1d4dcbbc9f5728%2Fpdi_tutorial_screen_job_new_job_canvas_w552.png?alt=media)
2. Expand the **General** folder and drag a Start job entry onto the canvas.

   The **Start** job entry defines where the execution will begin.

   **Note:** Jobs run in a sequential order of steps and transformations can run in a parallel order of steps.
3. Expand the **Conditions** folder and add a File Exists job entry.
4. Draw a hop from the Start job entry to the File Exists job entry.

   ![Draw hop from Start to File exists](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-65f7466f6cc1e6dde485b8ee18917430c730bdc0%2Fpdi_tutorial_screen_job_draw_hop_w221.png?alt=media)
5. Double-click the File Exists job entry to open its properties dialog box. Click **Browse** and set the filter near the bottom of the window to **All Files**. Select the `sales_data.csv` from the following directory: `...\design-tools\data-integration\samples\transformations\files`.
6. Click **OK** to exit the Open File window.
7. Click **OK** to exit the Check if a file exists window.
8. Expand the **General** folder and add a Transformation job entry.
9. Draw a hop between the File Exists and the Transformation job entries.
10. Double-click the Transformation job entry to open its properties dialog box.
11. Click **Browse** to open the **Select repository object** window. Browse to and select the **Getting Started** transformation.
12. Click **OK** to close the Transformation window.
13. Save your job as **Sample Job**.
14. Click **Run** icon in the toolbar. When the Run Options window appears, select **Local** environment type and click **Run**. The **Execution Results** panel should open showing you the job metrics and log information for the job execution.

    ![Job sample](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-e138ad954c6675e8c2ceefcff122c9042d266e20%2Fpdi_tutorial_screen_job_sample_job_w552.png?alt=media)

### PDI job tutorial

This is a shorter, standalone version of the job exercise.

Jobs are used to coordinate ETL activities such as:

* Defining the flow and dependencies for what order transformations should be run.
* Preparing for execution by checking conditions such as, "Is my source file available?" or "Does a table exist?"
* Performing bulk load database operations.
* File management such as posting or retrieving files using FTP, copying files and deleting files.
* Sending success or failure notifications through email.

For this exercise, imagine that an external system is responsible for placing your `sales_data.csv` input in its source location every Saturday night at 9 p.m. You want to create a job that will check to see that the file has arrived and run your transformation to load the records into the database. In a subsequent exercise, you will schedule the job to be run every Sunday morning at 9 a.m.

To complete this exercise, you must have completed the exercises in the [Pentaho Data Integration (PDI) tutorial](#pentaho-data-integration-pdi-tutorial).

1. Go to **File** > **New** > **Job**.

   ![PDI Job Window](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-fe869e2bd6f8244f9d0606d6a5abac92fddc56fe%2FPDI_Job_Tutorial_PDI_Job_Window.png?alt=media)
2. Expand the **General** folder and drag a Start job entry onto the graphical workspace.

   The **Start** job entry defines where the execution will begin.
3. Expand the **Conditions** folder and add a File Exists job entry.
4. Draw a hop from the Start job entry to the File Exists job entry.
5. Double-click the File Exists job entry to open its Edit Properties dialog box. Click **Browse** and set the filter near the bottom of the window to **All Files**. Select the `sales_data.csv` from the following location: `...\design-tools\data-integration\samples\transformations\files`.
6. Click **OK** to exit from the Open File window.
7. Click **OK** to exit from the Check if a file exists window.
8. In Spoon, expand the **General** folder and add a Transformation job entry.
9. Draw a hop between the File Exists and the Transformation job entries.
10. Double-click the Transformation job entry to open its edit Properties dialog box.
11. Click **Browse** to open the **Select repository object** window. Browse to and select the transformation you created in the [Pentaho Data Integration (PDI) tutorial](#pentaho-data-integration-pdi-tutorial).
12. Expand the repository tree to find your sample transformation. Select it and click **OK**.

    ![Select repository object window](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-fa489220686f9ffd06b9bdfc7dd113b2069eb6bf%2FPDI_Job_Tutorial_Select_repository_object_window.png?alt=media)
13. Save your job as Sample Job.
14. Click **Run** icon in the toolbar. When the Run Options window appears, choose **Local** environment type and click **Run**. The **Execution Results** panel should open showing you the job metrics and log information for the job execution.

    ![Job Sample](https://2644763545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJoh7icY0spTuXsorFO9q%2Fuploads%2Fgit-blob-225ec0b5f2c087ef881f79d64b6b74e2c8e75b1a%2FPDI_Job_Tutorial_Sample_Job.png?alt=media)

### Getting started with PDI and Hadoop

Pentaho provides a complete big data analytics solution that supports the entire big data analytics process. From big data aggregation, preparation, and integration, to interactive visualization, analysis, and prediction, Pentaho allows you to harvest the meaningful patterns buried in big data stores. Analyzing your big data sets gives you the ability to identify new revenue sources, develop loyal and profitable customer relationships, and run your organization more efficiently and cost effectively.

### Next steps

The tutorials above are designed to quickly demonstrate basic PDI features.

For more detailed information about PDI features and functions, see the following topics in the **Pentaho Data Integration** document:

* **Learn about the PDI Client**
* **Use Pentaho Repositories in PDI**
* **Schedule Perspective in the PDI Client**
