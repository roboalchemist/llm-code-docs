# Source: https://docs.pentaho.com/pba/data-source-wizard-cp-overview/get-started-with-the-data-source-wizard.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/data-source-wizard-cp-overview/get-started-with-the-data-source-wizard.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/data-source-wizard-cp-overview/get-started-with-the-data-source-wizard.md

# Get started with the Data Source Wizard

When you configured your Pentaho Server, you defined the connection information, including where the data is stored and what protocol or driver to use to connect to it. The **Install Pentaho Data Integration and Analytics** document shows you how to change or add connection information.

To create a data source, pick one of the connections that you have already defined, then use the wizard's interactive data modeling tool to select tables and columns to drag onto the model canvas. You can then use the Data Source Model Editor to refine the model further.

The Data Source Wizard guides you through setting up CSV files, as well as [relational](http://en.wikipedia.org/wiki/Relational_model) and [multidimensional](http://en.wikipedia.org/wiki/Multidimensional_database#Multidimensional_databases) data models, as data sources for building interactive and analysis reports. The initial data models you create with this tool enable you to immediately see how your data looks in Interactive Reports and Analyzer. Your results appear in Interactive Reports and Analyzer as you change model structures, and add tables and columns.

When you want to add more security, localization, or advanced modifications to your model, export the initial model created with the Data Source Wizard, and import it into either the **Pentaho Metadata Editor** for relational data models or **Pentaho Schema Workbench** for multidimensional data models.

**Note:** Relational and multidimensional models that were edited in Metadata Editor and Schema Workbench can no longer be edited in the Data Source Model Editor.

![Create New menu in the Pentaho User Console](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-a750d1e752ead96c6904e4d13bf421cec824493f%2FPUC_Create_New_Data_Sources.png?alt=media)

If you are not logged in with permissions to create, edit, and delete data sources, you are limited to view-only permissions and do not see any icons associated with adding, editing, or deleting data sources.

![Manage Data Sources dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-c926141d1584eef7786018db5282f8c1caf897a9%2FPUC_Manage_Data_Sources_dialog.png?alt=media)

There are several ways to access the Data Source Wizard within the User Console, so you do not have to backtrack to create a data source.

| If You Are In                                      | Then Follow These Steps                                                      |
| -------------------------------------------------- | ---------------------------------------------------------------------------- |
| Home perspective                                   | Click **Create New** > **Data Source**.                                      |
| Home perspective                                   | Click **Manage Data Sources** and then **New Data Source**.                  |
| Home perspective                                   | Click **Create New** > **Analysis Report** and then the **New** icon.        |
| Home perspective                                   | Click **Create New** > **Interactive Report** and then the **New** icon.     |
| Opened perspective                                 | Click the **New**\*\*\*\* icon and then select **Data Source Wizard**.       |
| Any perspective, from the menu bar                 | Click **File** > **New** > **Data Source**.                                  |
| Any perspective, from the menu bar                 | Click **File** > **Manage Data Sources** and then click **New Data Source**. |
| **Dashboard** pane, creating a chart or data table | Click the **Add** icon in the Select Data Source dialog box.                 |

![Data Source Wizard dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-bd328a9037ea1dfc3dcbcd64df578aee88f0d3c0%2FPUC_Data_SourceWizard_dialog.png?alt=media)

After accessing the Data Source Wizard, you are ready to begin creating your first data source.
