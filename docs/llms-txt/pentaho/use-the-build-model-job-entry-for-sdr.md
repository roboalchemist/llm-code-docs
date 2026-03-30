# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr.md

# Use the Build Model job entry for SDR

The Build Model job entry can be used to create Data Source Wizard data sources, which includes both a Metadata and a Mondrian model. It works by searching upstream for an output step or data service upon which to base your model, or you can select an existing Data Source Wizard or Analyzer model from the Pentaho Server. Note that if you are using a data service as the source in your Build Model job entry, you must be connected to a Pentaho Repository to successfully publish your model.

After you have run this job entry, a data model is created and can be published to the server for the creation of Analyzer reports in the Pentaho User Console. Business users will also be able to refine the data model with the Data Source Model Editor. If you selected an Analyzer model to build from, the Build Model job entry will only create an Analyzer model.

A Build Model job entry builds the model and sets variables into the job that can be modified or picked up by the [Publish Model](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-publish-model-job-entry-for-sdr) job entry. An example workflow is shown below.

![SDR basic workflow](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-53a84bd94baa7b3bde899d690fb4fe074ebf2e76%2FSDRBasicWorkflow.png?alt=media)

After the Build Model job runs successfully, you can publish the data source to the Pentaho Server.
