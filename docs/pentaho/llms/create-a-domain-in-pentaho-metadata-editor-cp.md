# Source: https://docs.pentaho.com/pba-metadata-editor/create-a-domain-in-pentaho-metadata-editor-cp.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/create-a-domain-in-pentaho-metadata-editor-cp.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/create-a-domain-in-pentaho-metadata-editor-cp.md

# Create a domain

A metadata domain is a Pentaho term that represents all of the business objects created, stored and used in the metadata layer. A domain may consist of one or more connections, one or more models, security information, business tables, business views, categories, columns and concepts. You can create and save multiple metadata domains using the Metadata Editor.

A metadata domain is accessed through the Pentaho Server by publishing or exporting the domain to an `.xmi` file, and placing the file in your Pentaho solutions folder.

In summary, a domain represents all of the associated modeled business entities. A domain can be viewed as a metadata “document.” Each solution is restricted to have, at most, one domain. A solution repository can contain multiple solutions. A domain must be published as an XMI file in the solution repository root directory. The Metadata Editor works with one domain at time, for example, a `Sales` domain that defines the relationships and entities used by sales team.

When you first launch the Metadata Editor, a new domain is automatically created. You can immediately begin adding connections, tables, columns, and more. If you want to start fresh with a new domain, select **File** > **New** > **Domain File** from the main menu.

There are several procedures associated with creating a new domain.

* Setting up a database connection
* Import physical tables and columns
* Import tables inside a schema

## Setting up a database connection

A connection represents connection information of a specific database, and acts as the parent in the hierarchy for all physical tables and physical columns that are defined for that database.

Pentaho metadata models can connect to most common relational databases using JDBC. The Pentaho Metadata Editor (and the Pentaho metadata architecture) supports a vast and rich set of data sources. Before you begin defining your business model, you must first describe the database or data source that you would like to model. You do this by defining one or more connections in the editor.

![Database Connection](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-207dbe9162555498083a1e73fe24f086b7d72ea6%2F04_pme_data_source.png?alt=media)

**Note:** While the current implementation of Pentaho Metadata Editor supports multiple connections and multiple business models in the same domain, each business model must use physical objects (columns and tables) from a single connection only.

### Set up a database connection

Perform the following steps to create a new connection:

1. Right-click **Connections** in the navigation pane.
2. Select **New Connection**.

   The Database Connection dialog box appears.
3. Enter a **Connection Name**.
4. Define your database connection as needed.
5. Click **Test** to ensure that your entries are correct.
6. Click **OK** to save your connection. The list of tables in your database to be imported appear. If you want to find a specific table, enter the table name in the search box or use a regular expression. Select the tables you want to import and click **OK** or **Cancel** when you are done.

   **Note:** You do not need to import tables at this point. See [Import physical tables and columns](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/broken-reference) for more information.

### Add a new database type

First, note the **Connection Type** list in the dialog box. This is the list of database connections that the Pentaho Metadata Editor and metadata models can support. The list is quite extensive. If you do not see your database in the **Connection Type** list, you may be able to add it.

To add a new database type, you must copy the JDBC driver archive for your database into the PME install directory `...\metadata-editor\lib`. Restart the Pentaho Metadata Editor, and you will see your database in the **Connection Type** list.

### Method of access

Under **Connection Type**, you will see the **Access** list. Defining a JDBC or OBDC connection typically requires all of the remaining fields associated with the **General** tab to have the correct information. If you are into abstracting those details from your metadata domain, then use the JNDI method of access.

The JNDI access method keeps your server implementation cleaner as well; once you publish your domain to the server, as long as you have defined the JNDI connections with the same names, you still have a good implementation where your database information is only described to the JNDI layer. To take advantage of the JNDI method of access in the Pentaho Metadata Editor, you must define your database connection information in a properties file for the editor.

## Import physical tables and columns

After you define your database connections, the next step is to describe the physical database tables and columns that you want to include in your business model.

A business model contains all of the logical, abstract business objects and relationships that model your physical database objects in such a way that underlying changes to the physical database objects have minimal impact on your business, your business intelligence application, and your end users. There can be multiple business models in a single domain. A business model currently supports one database connection, and consists of business tables, relationships, and a multiple business views.

Fortunately, when you import a physical table, all of the table's columns come with it, so the import is a one step exercise instead of two. Later, you can remove the columns you do not want in the connection or the model. Below is an example of an import from HSQLDB (Hypersonic):

1. Right-click the **Sample Data Example** node in the navigation pane then select **Import Tables** from the menu.

   A dialog box that contains all physical tables available in the database appears.

   ![Import tables into PME](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-e67c73a4f5be23c72fb804f51a2aeafae3fd3263%2F05_pme_import_tables.png?alt=media)
2. Select the tables you want to include.

   **Note:** Press the SHIFT or CTRL key to select multiple tables.
3. Click **OK** when you are done.

The tables you selected appear in a list in the navigation pane in the left side of the workspace.

## Import tables inside a schema

If you are accessing a table inside a schema, use the **Import from Explorer** command.

![Database explorer, PME](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-c4ad12b85c38fcead244fb6071b6df079a3a2ebb%2F47_pme_import_pstgres_sample.png?alt=media)

1. Right-click on the connection and select **Import from Explorer**.

   A dialog box that contains all physical tables available in the database appears.
2. Navigate under the **Schema's** folder to locate the correct table(s) to import.

   **Note:** You must select the individual tables. Selecting the top level schema exclusively results in an error message.
3. Click **OK**.

The tables you selected appear in a list in the navigation pane in the left side of the workspace.

## Create a business model

Create the logical mapping of business objects to the physical tables and columns. See [Creating a business model](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/creating-a-business-model).

## Build a business view

Build a collection of business categories that represents the view of your model, typically used by your end users.  See [Build a business view](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/build-a-business-view).
