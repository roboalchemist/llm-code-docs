# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/work-with-the-streamlined-data-refinery/install-and-configure-the-streamlined-data-refinery/use-hadoop-with-the-sdr.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/install-and-configure-the-streamlined-data-refinery/use-hadoop-with-the-sdr.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/work-with-the-streamlined-data-refinery/install-and-configure-the-streamlined-data-refinery/use-hadoop-with-the-sdr.md

# Use Hadoop with the SDR

There are a [few prerequisites](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/connecting-to-a-hadoop-cluster-with-the-pdi-client-article) that you need to make sure are satisfied before you can begin using SDR with Hadoop.

1. Open the `ML_SDR_REFINERY.ktr` and locate the Hadoop File Input step in the upper-left.
2. Click to activate the hop between the Hadoop File Input and Parse weblog steps.
3. Click to deactivate all of the hops between the Log File List and Read Weblog Files steps.

   ![SDR transformation with Hadoop](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f3828d5f082f435000fdd88cd86baf7ba5ce08b4%2FSDR_PDI_Hadoop.png?alt=media)
4. Right-click to edit the Out to Staging DB step and select your staging database from the drop-down menu.
5. Click **OK** to close the window and save the transformation.
