# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/hbase-row-decoder-pdi/using-hbase-row-decoder-with-pentaho-mapreduce.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/hbase-row-decoder-pdi/using-hbase-row-decoder-with-pentaho-mapreduce.md

# Using HBase Row Decoder with Pentaho MapReduce

The HBase Row Decoder step is designed specifically for use in MapReduce transformations to decode the key and value data that is output by the TableInputFormat. The key output is the row key from HBase. The value is an HBase result object containing all the column values for the row.

The following use case shows you how to configure Pentaho MapReduce to use the TableInputFormat for reading data from HBase. It also shows you how to configure a MapReduce transformation to process that data using the HBase Row Decoder step.

**Note:** To process HBase data using incoming key and value data to produce a specified mapping, you will need to configure Hadoop to access HBase.

First, create a Pentaho MapReduce job entry that includes a transformation which uses a MapReduce Input step and an HBase row decoder step, as shown below:

![MapReduce transformation example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-1bd2e40875418a6f41be7e6c6013b84fdd70c892%2FPDI_PentahoMapreduce_Job_Entry_example.png?alt=media)

In the transformation, open the MapReduce Input step. Configure the **Key field** and **Value field** to produce a serialized result by selecting **Serializable** in the **Type** field:

![MapReduce input step example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-ffa30d6713f74afeda10bdc000d38e68994e1aad%2FPDI_MapReduce_Input_step_example.png?alt=media)

Next, open the HBase row decoder step and set the **Key field** to use the `key` and the **HBase result field** to use the `value` produced by the MapReduce Input step.

![HBase row decoder step example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-410977c0682dfecf405544c2bc822d4ddecce108%2FPDI_HBaseRowDecoder_example.png?alt=media)

Then, define or load a mapping in the **Create/Edit mappings** tab. Note that once defined (or loaded), this mapping is captured in the transformation metadata.

![HBase row decoder step, example 2](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-13367df96b6bf44bba6bc3eb91fc7a0940af6f34%2FPDI_HbaseRowDecoder_CreateEditMappings_DialogBox.png?alt=media)

Next, configure Pentaho MapReduce job entry to ensure that input splits are created using the TableInputFormat. Define the **Input Path** and **Input format** fields in the **Job Setup** tab, as shown below.

![Pentaho MapReduce entry example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-9cce03dbc74b62843b231954e72040a18f93e403%2FPentaho%20MapReduce%20entry%20example2.png?alt=media)

Finally, in the **User Defined** tab, assign a **Name** and **Value** for each property shown in the table below to configure the scan performed by the TableInputFormat:

| Name                                   | Value                                                                                                                                                   |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hbase.mapred.inputtable`              | The name of the HBase table to read from. (Required)                                                                                                    |
| `hbase.mapred.tablecolumns`            | The space delimited list of columns in ColFam:ColName format. Note that if you want to read all the columns from a family, omit the ColName. (Required) |
| `hbase.mapreduce.scan.cachedrows`      | (Optional) The number of rows for caching that will be passed to scanners.                                                                              |
| `hbase.mapreduce.scan.timestamp`       | (Optional) Time stamp used to filter columns with a specific time stamp.                                                                                |
| `hbase.mapreduce.scan.timerange.start` | (Optional) Starting time stamp to filter columns within a given starting range.                                                                         |
| `hbase.mapreduce.scan.timerange.end`   | (Optional) End time stamp to filter columns within a given ending range.                                                                                |

When you execute the job, the output is the row key from HBase and the value is an HBase result object containing all the column values for that row.
