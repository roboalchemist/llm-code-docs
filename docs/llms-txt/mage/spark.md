# Source: https://docs.mage.ai/production/executors/spark.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# PySpark executor

If the pipeline type is `pyspark`, we use PySpark executors for pipeline and
block executions.

You can customize the compute resource of PySpark executor by
updating the instance types of `emr_config` in project's metadata.yaml file.

## Example:

```yaml  theme={"system"}
emr_config:
  ec2_key_name: "xxxxx"
  master_instance_type: "r5.2xlarge"
  slave_instance_type: "r5.2xlarge"
```

## Spark compute resource manager

Manage your Spark compute resources and track Spark pipeline execution metrics.

[Learn more](/integrations/compute/management)


Built with [Mintlify](https://mintlify.com).