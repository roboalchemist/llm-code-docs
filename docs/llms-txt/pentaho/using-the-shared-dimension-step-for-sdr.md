# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-shared-dimension-step-for-sdr.md

# Using the Shared Dimension step for SDR

The Shared Dimension step works in much the same way as the [Annotate Stream](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-annotate-stream-step) step, refining your data through the creation of dimensions which can be shared for later use. You will need to designate one annotation in the shared dimension step as the dimension key.

You can create multiple annotations on the same field, such as an attribute and a dimension key. For example, in the Shared Dimension step, you can select the field **Year** and annotate it as a dimension key. You may also select the field **Year** again to annotate as an attribute. You can also create multiple annotations to modify the same data model.

The transformation which builds a shared dimension should run before the [Build Model job entry](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/use-the-build-model-job-entry-for-sdr) or in a separate job which runs before the Build Model. Here is an example transformation for a shared dimension.

![Shared dimension workflow](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-979bb0bedea71f12aaef7717667b0e3c81ab20ee%2FSDR_SharedDimensionWorkflow.png?alt=media)

After you are done with your data model, you will be ready to [publish](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-publish-model-job-entry-for-sdr) it.
