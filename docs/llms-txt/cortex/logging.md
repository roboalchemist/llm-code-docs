# Source: https://docs.cortexlabs.com/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.41/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.40/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.39/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.38/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.37/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.36/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.35/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.34/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.33/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.32/clusters/observability/logging.md

# Source: https://docs.cortexlabs.com/0.31/workloads/observability/logging.md

# Source: https://docs.cortexlabs.com/0.30/workloads/observability/logging.md

# Source: https://docs.cortexlabs.com/0.29/clusters/cortex-cloud-on-gcp/logging.md

# Source: https://docs.cortexlabs.com/0.29/clusters/cortex-cloud-on-aws/logging.md

# Source: https://docs.cortexlabs.com/0.28/clusters/cortex-cloud-on-gcp/logging.md

# Source: https://docs.cortexlabs.com/0.28/clusters/cortex-cloud-on-aws/logging.md

# Logging

By default, logs will be pushed to [CloudWatch](https://console.aws.amazon.com/cloudwatch/home) using fluent-bit. A log group with the same name as your cluster will be created to store your logs. API logs are tagged with labels to help with log aggregation and filtering. Below are some sample CloudWatch Log Insight queries:

RealtimeAPI:

```
fields @timestamp, log
| filter labels.apiName="<INSERT API NAME>"
| filter labels.apiKind="RealtimeAPI"
| sort @timestamp asc
| limit 1000
```

BatchAPI:

```
fields @timestamp, log
| filter labels.apiName="<INSERT API NAME>"
| filter labels.jobID="<INSERT JOB ID>"
| filter labels.apiKind="BatchAPI"
| sort @timestamp asc
| limit 1000
```

TaskAPI:

```
fields @timestamp, log
| filter labels.apiName="<INSERT API NAME>"
| filter labels.jobID="<INSERT JOB ID>"
| filter labels.apiKind="TaskAPI"
| sort @timestamp asc
| limit 1000
```

Please make sure to select the log group for your cluster and adjust the time range accordingly before running the queries.

## Structured logging

You can use Cortex's logger in your Python code to log in JSON, which will enrich your logs with Cortex's metadata, and enable you to add custom metadata to the logs. See the structured logging docs for [Realtime](https://docs.cortexlabs.com/0.28/workloads/realtime-apis/predictors#structured-logging), [Batch](https://docs.cortexlabs.com/0.28/workloads/batch-apis/predictors#structured-logging), and [Task](https://docs.cortexlabs.com/0.28/workloads/task-apis/definitions#structured-logging) APIs.
