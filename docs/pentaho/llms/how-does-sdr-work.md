# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery/how-does-sdr-work.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/how-does-sdr-work.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/how-does-sdr-work.md

# How does SDR work?

The components that make up the data refinery are PDI, used for parameter entry, working in conjunction with an app for refining the data. This app calls to the Pentaho Server for the main job: refining data through Spoon using the new [Build Model](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Advanced%20Pentaho%20Data%20Integration%20topics/Advanced%20topics%20\(Pentaho%20Data%20Integration%20overview\)/Work%20with%20the%20Streamlined%20Data%20Refinery/Use%20the%20Streamlined%20Data%20Refinery/Building%20blocks%20for%20the%20SDR/Use%20the%20Build%20Model%20job%20entry%20for%20SDR=GUID-7FAB840B-9B79-440E-AE59-31C3F5B5EACA=4=en=.md) job entry, then publishing the data source back to the Pentaho Server through the [Publish Model](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/use-the-streamlined-data-refinery/building-blocks-for-the-sdr/using-the-publish-model-job-entry-for-sdr) job entry. Once it is published, the refined data is available for use in creating Analyzer reports. This process is shown in the graphic.

![SDR overview](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-b7e2a0a5d4cbd5434d2cd3c89170701e2f5b70d8%2FSDR_Diagram.png?alt=media)
