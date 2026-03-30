# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/kinesis-producer.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/kinesis-producer.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/kinesis-producer.md

# Kinesis Producer

The Kinesis Producer step pushes data from a PDI transformation to an existing stream in a specific region within the Amazon Kinesis Data Streams (KDS) service. You can use this step to publish a [stream of data](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/streaming-analytics) to KDS for storage in S3, Redshift, or EMR HDFS. For more information about the Amazon Kinesis Data Streams protocol, see <https://aws.amazon.com/kinesis/>.

For the Kinesis Producer step, configure the connection to Amazon and specify the target Amazon region and KDS stream. Only one region can be selected.
