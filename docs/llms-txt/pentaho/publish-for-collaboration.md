# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/inspect-your-data/publish-for-collaboration.md

# Publish for collaboration

When you are ready to make your content available for others, you can publish it as a **data source**. The data source uses a **data service** that is automatically created on the step, and is available to other tools. You must be connected to your **repository** to publish the data source.

1. Click the **Publish data source** button ( ![Publish Data Source Button](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-739fe22e1a10fab605224d1c2ec5ce5ee6e3854f%2FDET_publish_button.jpg?alt=media) ) at the top right of the header bar to open the Publish Data Source window.
2. Click **Get Started** to open the Publish Details window.

   Enter the data source information in the following fields:

   | Fields               | Description                                                                                                                                                             |
   | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Data Source Name** | The name used by other Pentaho applications when accessing your data source.                                                                                            |
   | **Server**           | The default value for this field is your current repository. You can select other repository connections, if you have created them, through the **Repository Manager**. |
   | **URL**              | The base URL string used to connect to the server.                                                                                                                      |
   | **User Name**        | The user name required to access the server. The user must also have publishing permissions.                                                                            |
   | **Password**         | The password associated with the provided user name.                                                                                                                    |
3. When you are done, click **Finish**.
4. Once your data source is created, a confirmation will appear. The data source should now be available on the server. Click **Close** to continue inspecting your data or click **View this in User Console** to open a new browser window and work with the data source in Analyzer.
