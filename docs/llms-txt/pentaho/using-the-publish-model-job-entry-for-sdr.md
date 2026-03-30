# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-publish-model-job-entry-for-sdr.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-publish-model-job-entry-for-sdr.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-publish-model-job-entry-for-sdr.md

# Using the Publish Model job entry for SDR

The Publish Model job entry allows you to publish the data model created with the [Build Model](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr) job entry so it is available for use on the Pentaho Server. Before publishing the model, you will have the option of sharing the data model with everyone, or a specific user or role.

When you are building your job in Pentaho Data Integration (PDI), you will need to place the Build Model job entry before the Publish Model job entry, as shown here in this example, to publish the model properly.

![SDR workflow](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-53a84bd94baa7b3bde899d690fb4fe074ebf2e76%2FSDRBasicWorkflow.png?alt=media)

After it is published to the Pentaho Server, the Data Source Wizard data source has the same name as the model in the Build Model job entry. Note that once the model is published, you won't be able to use the Data Source Wizard to edit the connection information since the connection information for this model is stored in the Build Model job entry in PDI.
