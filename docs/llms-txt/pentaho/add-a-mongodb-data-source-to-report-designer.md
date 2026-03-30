# Source: https://docs.pentaho.com/pba-report-designer/connect-report-designer-to-a-data-source-cp/add-a-mongodb-data-source-to-report-designer.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/connect-report-designer-to-a-data-source-cp/add-a-mongodb-data-source-to-report-designer.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp/add-a-mongodb-data-source-to-report-designer.md

# MongoDB

You can define a MongoDB data source query, then display query results in a report.

To establish a connection to a MongoDB data source, specify the input options and queries when you select **Configure Fields** in the Pentaho Data Integration MongoDB Input transformation step.Optionally, you can connect to a MongoDB data source using the **Connection String** option in the step.

To complete this task, you must have MongoDB database connection information, such as host names, port numbers and authentication credentials. If you need these items, contact your system administrator for help before you begin.

1. Open the Pentaho Report Designer window and either create a report or open an existing one.
2. Select **Data** > **Add Datasource** > **MongoDB** from the menu.

   The MongoDB Data Source window appears.
3. Click **Add New Query** to name the MongoDB data source definition.

   Fields in the window become active.
4. Type the name of the query in the **Name** field.
5. Configure the connection
   1. Enter the host name and port number for your MongoDB database.

      You can also specify a different port number for each host name by separating the host name and port number with a colon, and separating each combination of host name and port number with a comma like this:`localhost1:27017,localhost2:27018`. If you specify the port in the host field, leave the port field empty.
   2. If you want to MongoDB to automatically sense and attempt to connect to available hosts, even if one is down, select the **Use all replica set members** checkbox.
   3. Type the user name needed to access the MongoDB database in the **User** field, then type the password of the user in the **Password** field.
   4. Indicate how long the database should wait before terminating the connection attempt.

      If you do not want the database to ever terminate the connection, leave the **Connection timeout** field blank. Otherwise, enter a numerical value in milliseconds.
   5. In the **Socket timeout** field, indicate how long the database should wait for a write operation to occur before it terminates it.

      If you do not want the database to ever terminate it, leave this field blank.
6. To query the MongoDB server for available databases and collections, click the **Input Options** tab.

   You can also set the read preference and tag set specification, in this tab.

   1. Click **Get DBs** to populate the drop-down menu with names of available databases then select the appropriate database, or enter the database name.
   2. Click **Get collections** to populate the drop-down menu with names of available [Mongo collections](http://docs.mongodb.org/manual/reference/glossary/#term-collection).

      If an error message appears, check the host name and port numbers in the Configure connection tab.
   3. Select a database from the **Database** drop down menu.
   4. Click the **Get Collections** button, then select a collection from the **Collection** drop down menu.
   5. Indicate the read preference in the **Read** field.
   6. If you want to specify a tag set, click the **Get tags** button.

      Tag sets that have been specified on the MongoDB database appear in the **Tag Set** section of the window. If you want to append tag sets together so that they are processed at one time, select the tag sets, then click the **Join tags** button. Click the **Test tag** sets button to see a list of nodes that match the tag set criteria.
7. Click the **Query** tab.

   You can formulate a query using two different methods. You can either create the query as a JSON Query expression, or use the Aggregation Framework. The Aggregation Framework is explained in detail in the [MongoDB Aggregation Framework documentation](http://docs.mongodb.org/manual/core/aggregation/).

   * JSON Query Expression

     Using JSON Query Expressions is analogous to using the MongoDB `find()` command documented on the <http://docs.mongodb.org/manual/core/read-operations> page. The query argument to find is entered in the **Query expression (JSON)** field. The projection argument is supplied in the **Fields expression (JSON)** text box. In order to use the JSON Query Expression mode, ensure that the **Query is aggregation pipeline** checkbox is not selected.
   * Aggregation Framework

     To query MongoDB using the Aggregation Framework <http://docs.mongodb.org/manual/core/aggregation/> click the **Query is aggregation pipeline** checkbox. Enter a sequence of pipeline operations in the **Query expression (JSON)** field. This mode uses the same syntax as the MongoDB `aggregation()` command.
8. Click the **Fields** tab to view the fields that are in the database and collection you specified.

   You can also edit field names that appear in Report Designer, edit the path to the field that you want to include in the report, and make changes to the type.

   1. Click the **Get Fields** button.

      Pentaho's Schema on Read functionality samples the documents in the collection to determine which fields are available what their data types are.

      The fields are displayed.
   2. If desired, edit the names of the fields.

      The names are what the fields will be called in Data Integration and Report Designer.
   3. If desired, edit the path to the field in the MongoDB database.

      If an array was returned, you can specify the element in the array by indicating the number of the element in brackets, like this: `$.myArrayElement[0]`. In this example, which is of a zero-based array, the content of the first field is returned.

      **Note:** If you want to return all of the items in an array, place an asterisk in the bracket, like this:`$.myArrayElement[*]`
   4. Edit the data type if necessary.
9. You can paramaterize both JSON Query Expressions and Aggregation Pipeline queries using simple string replacement.

   Parameters are specified using Pentaho Reporting's parameter syntax `${param}` where param is the name of the parameter containing the data that you want to replace the param name. For example, if you have defined a report parameter named state, that you want to use to select documents for that state, your query could look like this: `{$match : { state : "${State}" }}`. So, if you set the state parameter to **FL** at runtime, the resulting query submitted to MongoDB would look like this:`{$match : { state : "FL" }}` If the parameter name used in the `${}` matches the name of existing parameter, the linkage between the parameter and the query are automatic. If you prefer to use a different name in the query, click the **Edit Parameter** button.

   1. Click the **Edit Parameter** button.
   2. In the Transformation Parameters window, click the **Add a New Parameter** button to add a row to the table.
   3. In the **DataRow** column, choose the parameter you want to add from the drop down list.
   4. Select the **Transformation Parameter** from the drop down list.
   5. If desired, add a transformation argument by clicking the **Add a New Transformation Argument** button and adding the argument in the row that appears.
   6. When complete, click **OK**.
10. Click **Preview** to test the connection and to see what the data will look like when it is brought into the report designer. When complete, click **OK**.

Report Designer can now access your MongoDB data source.
