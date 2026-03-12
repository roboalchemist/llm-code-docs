# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/pentaho-mapreduce-workflow/pdi-transformation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/pentaho-mapreduce-workflow/pdi-transformation.md

# PDI Transformation

Start by deciding what you want to do with your data, open a PDI transformation, and drag the appropriate steps onto the canvas, configuring the steps to meet your data requirements. Drag the specifically-designed Hadoop MapReduce Input and Hadoop MapReduce Output steps onto the canvas. PDI provides these steps to completely avoid the need to write Java classes for this functionality. Configure both of these steps as needed. Once you have configured all the steps, add hops to sequence the steps as a transformation. Follow the workflow as shown in this sample transformation in order to properly communicate with Hadoop. Name this transformation Mapper.

![Big Data Key Value Pair Example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-6a3ecb8f9b0472fb91c257827b32297d7ca69cad%2FBigDataKeyValuePairExample.png?alt=media)

Hadoop communicates in key/value pairs. PDI uses the MapReduce Input step to define how key/value pairs from Hadoop are interpreted by PDI. The MapReduce Input dialog box enables you to configure the MapReduce Input step.

![MapReduce Input Step dialog](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-7cfd55ee190f2236a21c0ed5ca87b765e64312e2%2FssPDIMapReduceInputStep.png?alt=media)

PDI uses a MapReduce Output step to pass the output back to Hadoop. The **MapReduce Output** dialog box enables you to configure the MapReduce Output step.

![MapReduce Output Step dialog](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-71d6fbd1edd7366758cd6eefe579243737c2255b%2FssPDIMapReduceOutputStep.png?alt=media)

What happens in the middle is entirely up to you. Pentaho provides many sample steps you can alter to create the functionality you need.
