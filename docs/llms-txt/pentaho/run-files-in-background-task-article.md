# Source: https://docs.pentaho.com/pba/pentaho-user-console/classic-design/about-pentaho-user-console-perspectives/browse-puc-perspective/run-files-in-background-task-article.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/browse-puc-perspective/run-files-in-background-task-article.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-user-console/about-pentaho-user-console-perspectives/browse-puc-perspective/run-files-in-background-task-article.md

# Run files in background

You can run reports in the background from the User Console using Run in Background. The types you can run include Report Designer Reports (.prpt), Analyzer Reports (.xanalyzer), and Interactive Reports (.prpti).

You must be connected to a Pentaho Repository and have your reports saved to that repository before running them.

Perform the following steps to run a report in the background:

1. Log in to the User Console, and then click the **Browse Files** button.
2. In the **Folders** pane, browse to the folder containing the file that you want to run.
3. In the **File** pane, click on the file that you want to run.
4. In the **File Actions** pane, click **Run in background**.

   The Run In Background dialog box appears.

   ![Run in Background dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-de88f7e3461ed5fc659c0b5db4f69d715d56e706%2FPUC_BrowseFiles_RunInBackground_DB.png?alt=media)
5. Enter your selections for the following fields:

   | Field                                                     | Description                                                                                                                                                                                                                                               |
   | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Generated Content Name**                                | Specify a name for the generated content. If no name is entered in the Name field, the default is the report name.                                                                                                                                        |
   | **Append timestamp to generated content**                 | Click this check box to append the value specified in the **Generated Content Name** with a timestamp. When selected, a menu shows a list of timestamp format options. Use the **Preview** panel to view how the name will display on the generated file. |
   | **Generated Content Location**                            | Specify a location for the generated content. Click **Select** to browse to a folder location to choose it.                                                                                                                                               |
   | **Overwrite existing files with same name and timestamp** | Click this check box to overwrite any existing files that have the same name and timestamp as the one you are running and saving to the specified location.                                                                                               |
6. Click **Next**. If the selected report has run parameters, such as Output Type, you will be asked to specify them here.
7. When you have completed your parameter selections, click **Finish**.

The file is now processing. The system will deliver the content generated from the report to your specified location.
