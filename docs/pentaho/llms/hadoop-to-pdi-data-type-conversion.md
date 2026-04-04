# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/hadoop-to-pdi-data-type-conversion.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce/use-pdi-outside-and-inside-the-hadoop-cluster/hadoop-to-pdi-data-type-conversion.md

# Hadoop to PDI data type conversion

The Hadoop Job Executor and Pentaho MapReduce steps have an advanced configuration mode that enables you to specify data types for the job's input and output. PDI is unable to detect foreign data types on its own; therefore you must specify the input and output data types in the **Job Setup** tab.

This table explains the relationship between Hadoop data types and their PDI equivalents.

| PDI (Kettle) Data Type               | Apache Hadoop Data Type             |
| ------------------------------------ | ----------------------------------- |
| `java.lang.Integer`                  | `org.apache.hadoop.io.IntWritable`  |
| `java.lang.Long`                     | `org.apache.hadoop.io.IntWritable`  |
| `java.lang.Long`                     | `org.apache.hadoop.io.LongWritable` |
| `org.apache.hadoop​.io.IntWritable`  | `java.lang.Long`                    |
| `java.lang.String`                   | `org.apache.hadoop.io.Text`         |
| `java.lang.String`                   | `org.apache.hadoop​.io.IntWritable` |
| `org.apache.hadoop.io​.LongWritable` | `org.apache.hadoop.io​.Text`        |
| `org.apache.hadoop.io​.LongWritable` | `java.lang.Long`                    |

For more information on configuring Pentaho MapReduce to convert to additional data types, see [Pentaho MapReduce.](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-job-entries-reference-overview/pentaho-mapreduce)
