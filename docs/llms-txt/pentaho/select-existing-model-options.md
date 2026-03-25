# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr/select-existing-model-options.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr/select-existing-model-options.md

# Select existing model options

If you selected to use an existing model to build upon, you will need to be connected to the Pentaho Server. Once you are connected, you can select an existing model with the same physical schema to base your new model on.

**Note:** If you select **Use Existing**, your annotations are not applied to the model when it is opened in Analyzer. If you want to apply your annotations to the model in Analyzer, select **Auto Model**.

1. Fill in or edit the fields in the **Pentaho Server Connection** section.

   | Field         | Description                                                                                            |
   | ------------- | ------------------------------------------------------------------------------------------------------ |
   | **URL**       | The base URL string used to connect to the server.                                                     |
   | **User Name** | The user name required to access the server.                                                           |
   | **Password**  | The password associated with the provided user name which is passed during the authentication process. |
2. Click the **Connect** button to connect to the server using the information provided in the above fields.

   If the connection was successful, the **Existing Models** drop-down menu will be available for selection with a list of models to choose from.
3. Select a model from the **Existing Models** drop-down menu.

   If no models are listed, verify that you are connected to the Pentaho Server.
4. (Optional) Select the **Create model if not found** check box to generate a model if the system cannot find an existing model with the entered name.
5. When finished, click **OK** to save your changes and close the dialog box, or **Cancel** to close the dialog box without saving your changes.

This is an example of the Select Existing Model dialog box.

![Select Existing Model dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-705933f94d1dee379c8df27a88a3acfc1ebe7188%2FSDR_select_existing_model.png?alt=media)
