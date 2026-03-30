# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr/create-a-build-model-job-entry.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr/create-a-build-model-job-entry.md

# Create a Build Model job entry

This task assumes you are in the job canvas of the PDI client.

Use the Build Model job entry to create a model for publishing directly to the Pentaho Server.

1. In the **Design** tab, click the **Modeling** folder, and then double-click the Build Model job entry. Alternatively, you can drag the job entry icon on to the job canvas.

   ![Build Model job entry](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-2ec6dbaf8190ea3ba44e39b32965cc32f9e95667%2FBuildModelIcon2.png?alt=media)
2. Double-click the **Build Model** icon to open the Build Model dialog box.
3. Enter a name for the entry in the **Entry name** field.

   **Note:** The following characters are not valid in Data Source Wizard source names:

   ```
   % ? : [] * \t \r \n
   ```
4. In the **Source** field, select an output step or a Pentaho Data Service from the drop-down menu, or press CTRL Space to select a variable.

   The selected output step or data service provides the source data in the model. If no data is written to the table by the selected source, then the Build Model job entry will not build a model.

   **Note:** When you select a Pentaho Data Service as the source, previously defined link dimensions will not be linked to your model. Link dimension annotations are dependent on shared dimensions, and shared dimensions cannot use a data service for their source. See [Pentaho Data Services](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services) for more information about data services.
5. Enter a name for your data model in the**Model Name** field. Optionally, click in the field and press CTRL Space to select a variable.

   The model name entered here will appear in the list of data sources in the Pentaho Server.
6. In the **Modeling Method** section, you can select the modeling method for the entry.
   * **Auto Model** if you want to build a new model. When you choose to auto model, your annotations will be applied to the model when it is opened in Analyzer.
   * **Use Existing** if you want to base your model on one which already exists in the Pentaho Server. Click the **Select** button below to enter the name of an existing model from the server in the required field. See [Select existing model options](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr/select-existing-model-options). When you use an existing model, your annotations will not be applied to the model when it is opened in Analyzer.**Note:** When you select **Auto Model** and you have modified a measure in Analyzer, the inline model editing changes you made in Analyzer will take priority over any annotations added to the measure in PDI. In addition, annotations you add in PDI will not be visible for that measure when viewed in Analyzer.
7. Click **OK** to save your changes and close the dialog box, or click **Cancel** to discard your changes and close the dialog box.
