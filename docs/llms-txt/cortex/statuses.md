# Source: https://docs.cortexlabs.com/workloads/task/statuses.md

# Source: https://docs.cortexlabs.com/workloads/batch/statuses.md

# Source: https://docs.cortexlabs.com/workloads/async/statuses.md

# Source: https://docs.cortexlabs.com/workloads/realtime/statuses.md

# Source: https://docs.cortexlabs.com/0.41/workloads/task/statuses.md

# Source: https://docs.cortexlabs.com/0.41/workloads/batch/statuses.md

# Source: https://docs.cortexlabs.com/0.41/workloads/async/statuses.md

# Source: https://docs.cortexlabs.com/0.41/workloads/realtime/statuses.md

# Source: https://docs.cortexlabs.com/0.40/workloads/task/statuses.md

# Source: https://docs.cortexlabs.com/0.40/workloads/batch/statuses.md

# Source: https://docs.cortexlabs.com/0.40/workloads/async/statuses.md

# Source: https://docs.cortexlabs.com/0.40/workloads/realtime/statuses.md

# Source: https://docs.cortexlabs.com/0.39/workloads/task/statuses.md

# Source: https://docs.cortexlabs.com/0.39/workloads/batch/statuses.md

# Source: https://docs.cortexlabs.com/0.39/workloads/async/statuses.md

# Source: https://docs.cortexlabs.com/0.39/workloads/realtime/statuses.md

# Source: https://docs.cortexlabs.com/0.38/workloads/task/statuses.md

# Source: https://docs.cortexlabs.com/0.38/workloads/batch/statuses.md

# Source: https://docs.cortexlabs.com/0.38/workloads/async/statuses.md

# Source: https://docs.cortexlabs.com/0.38/workloads/realtime/statuses.md

# Source: https://docs.cortexlabs.com/0.37/workloads/task/statuses.md

# Source: https://docs.cortexlabs.com/0.37/workloads/batch/statuses.md

# Source: https://docs.cortexlabs.com/0.37/workloads/async/statuses.md

# Source: https://docs.cortexlabs.com/0.37/workloads/realtime/statuses.md

# Source: https://docs.cortexlabs.com/0.36/workloads/task/statuses.md

# Source: https://docs.cortexlabs.com/0.36/workloads/batch/statuses.md

# Source: https://docs.cortexlabs.com/0.36/workloads/async/statuses.md

# Source: https://docs.cortexlabs.com/0.36/workloads/realtime/statuses.md

# Source: https://docs.cortexlabs.com/0.35/workloads/task-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.35/workloads/batch-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.35/workloads/async-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.35/workloads/realtime-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.34/workloads/task-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.34/workloads/batch-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.34/workloads/async-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.34/workloads/realtime-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.33/workloads/task-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.33/workloads/batch-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.33/workloads/async-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.33/workloads/realtime-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.32/workloads/task-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.32/workloads/batch-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.32/workloads/async-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.32/workloads/realtime-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.31/workloads/task-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.31/workloads/batch-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.31/workloads/introduction/statuses.md

# Source: https://docs.cortexlabs.com/0.31/workloads/realtime-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.30/workloads/task-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.30/workloads/batch-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.30/workloads/realtime-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.29/workloads/task-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.29/workloads/batch-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.29/workloads/realtime-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.28/workloads/task-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.28/workloads/batch-apis/statuses.md

# Source: https://docs.cortexlabs.com/0.28/workloads/realtime-apis/statuses.md

# Statuses

| Status                | Meaning                                                                                                                                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| live                  | API is deployed and ready to serve prediction requests (at least one replica is running)                                                                                                             |
| updating              | API is updating                                                                                                                                                                                      |
| error                 | API was not created due to an error; run `cortex logs <name>` to view the logs                                                                                                                       |
| error (image pull)    | API was not created because one of the specified Docker images was inaccessible at runtime; check that your API's docker images exist and are accessible via your cluster operator's AWS credentials |
| error (out of memory) | API was terminated due to excessive memory usage; try allocating more memory to the API and re-deploying                                                                                             |
| compute unavailable   | API could not start due to insufficient memory, CPU, GPU or Inf in the cluster; some replicas may be ready                                                                                           |
