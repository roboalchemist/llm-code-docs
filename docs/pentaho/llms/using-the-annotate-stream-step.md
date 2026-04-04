# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step.md

# Using the Annotate Stream step

The Annotate Stream step helps you refine your data for the Streamlined Data Refinery by creating measures, link dimensions, or attributes on stream field(s) which you specify. If you want, you can create multiple annotations on the same field. For example, you might want to create an average measure and a sum measure on the same field. You can also annotate multiple streams to modify the same data model. Additionally, you can create and add calculated measures to the data model.

The Annotate Stream modifies the default model produced from the [Build Model](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr) job entry.

![SDR workflow](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-53a84bd94baa7b3bde899d690fb4fe074ebf2e76%2FSDRBasicWorkflow_AnnotateStream.png?alt=media)

After you are done annotating your data model, you are ready to [publish](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-publish-model-job-entry-for-sdr) it.
