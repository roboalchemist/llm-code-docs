# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/hyperscalers-landing-page/installing-pentaho-on-aws/running-pdi-cli-on-aws/configure-and-execute-pdi-cli.md

# Configure and execute PDI-CLI

Configure and run AWS Batch using the PDI-CLI image.

See the AWS instructions for the following steps at [Getting Started with AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/Batch_GetStarted.html).

1. Navigate to the [AWS Batch home page](https://aws.amazon.com/batch/).
2. Create a compute environment by selecting **Compute environments** and follow the instructions.
3. Create a job queue by selecting **Job queues**and follow the instructions.
4. Create a job definition by selecting **Job definitions** and follow the instructions.

   Provide the image name in the section for configuring the container.
5. Create a job by selecting **Jobs** and follow the instructions.

   In the Environment Variables section, configure the following variables:

| Variable              | Description                                                                                                                                                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PROJECT\_S3\_LOCATION | <p>Configures the S3 path from where the data is downloaded. It is then uploaded to the container.</p><p>Example: Set <strong>PROJECT\_S3\_LOCATION</strong> to <code>s3://pentaho-samples/</code></p>                                                                               |
| METASTORE\_LOCATION   | <p>Configures the metastore path from where the metastore content and configuration will be downloaded. It is then uploaded to the path of the container: <code>/home/pentaho/.pentaho</code>.</p><p>Example: Set <strong>METASTORE\_LOCATION</strong> to <code>metastore</code></p> |
| PROJECT\_STARTUP\_JOB | <p>Path used to execute KJB files.</p><p>Example: Set <strong>PROJECT\_STARTUP\_JOB</strong> to <code>jobs/run\_job\_write\_to\_s3/read\_csv\_from\_s3\_job.kjb</code></p>                                                                                                           |
| LICENSE\_TOKEN        | License token or server URL that is used to provide access to Pentaho.Example: Set LICENSE\_TOKEN to `http://localhost:7070/license-server/request(Sample)`.                                                                                                                         |
| PARAMETERS            | Parameters passed to the running job or transformation. Example: Set **PARAMETERS** to `-param:my_param_name=MYVALUE`.                                                                                                                                                               |

You can now run Pentaho transformations and jobs using PDI-CLI.
