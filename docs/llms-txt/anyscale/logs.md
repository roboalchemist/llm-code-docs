# Source: https://docs.anyscale.com/reference/logs.md

# Logs API Reference

[View Markdown](/reference/logs.md)

# Logs API Reference

#### Customer-hosted cloud features[​](#customer-hosted-only "Direct link to Customer-hosted cloud features")

note

Some features are only available on customer-hosted clouds. Reach out to <support@anyscale.com> for info.

## Logs CLI[​](#logs-cli "Direct link to Logs CLI")

### `anyscale logs workspace`[​](#anyscale-logs-workspace "Direct link to anyscale-logs-workspace")

**Usage**

`anyscale logs workspace [OPTIONS] [GLOB]`

Access log files of a workspace.

**Options**

* **`--id`**: Provide a workspace ID.
* **`-d/--download`**: Download logs to the current working directory, or a specified path.
* **`-t/--tail`**: Read the last N lines of logs.
* **`-ip/--node-ip`**: Filter logs by a node IP.
* **`--instance-id`**: Filter logs by an instance ID.
* **`--worker-only`**: Download logs of only the worker nodes.
* **`--head-only`**: Download logs of only the head node.
* **`--unpack/--no-unpack`**: Whether to unpack the combined-worker.log after downloading.
* **`--download-dir`**: Directory to download logs into.
* **`--ttl`**: TTL in seconds to pass to the service that generates presigned URL's (default: 4h).
* **`--parallelism`**: Number of files to download in parallel at a time.

### `anyscale logs service`[​](#anyscale-logs-service "Direct link to anyscale-logs-service")

**Usage**

`anyscale logs service [OPTIONS] [GLOB]`

Access log files of a service for a single service version.

**Options**

* **`--id`**: Provide a service ID.
* **`--version`**: Service version name or ID to get logs from. If not specified, uses the latest running version.
* **`-d/--download`**: Download logs to the current working directory, or a specified path.
* **`-t/--tail`**: Read the last N lines of logs.
* **`-ip/--node-ip`**: Filter logs by a node IP.
* **`--instance-id`**: Filter logs by an instance ID.
* **`--worker-only`**: Download logs of only the worker nodes.
* **`--head-only`**: Download logs of only the head node.
* **`--unpack/--no-unpack`**: Whether to unpack the combined-worker.log after downloading.
* **`--download-dir`**: Directory to download logs into.
* **`--ttl`**: TTL in seconds to pass to the service that generates presigned URL's (default: 4h).
* **`--parallelism`**: Number of files to download in parallel at a time.

### `anyscale logs job`[​](#anyscale-logs-job "Direct link to anyscale-logs-job")

**Usage**

`anyscale logs job [OPTIONS] [GLOB]`

Access log files of a production job. Fetches logs for all job attempts.

**Options**

* **`--id`**: Provide a production job ID.
* **`-d/--download`**: Download logs to the current working directory, or a specified path.
* **`-t/--tail`**: Read the last N lines of logs.
* **`-ip/--node-ip`**: Filter logs by a node IP.
* **`--instance-id`**: Filter logs by an instance ID.
* **`--worker-only`**: Download logs of only the worker nodes.
* **`--head-only`**: Download logs of only the head node.
* **`--unpack/--no-unpack`**: Whether to unpack the combined-worker.log after downloading.
* **`--download-dir`**: Directory to download logs into.
* **`--ttl`**: TTL in seconds to pass to the service that generates presigned URL's (default: 4h).
* **`--parallelism`**: Number of files to download in parallel at a time.

### `anyscale logs cluster`[​](#anyscale-logs-cluster "Direct link to anyscale-logs-cluster")

**Usage**

`anyscale logs cluster [OPTIONS] [GLOB]`

Access log files of a cluster.

**Options**

* **`--id`**: Provide a cluster ID.
* **`-d/--download`**: Download logs to the current working directory, or a specified path.
* **`-t/--tail`**: Read the last N lines of logs.
* **`-ip/--node-ip`**: Filter logs by a node IP.
* **`--instance-id`**: Filter logs by an instance ID.
* **`--worker-only`**: Download logs of only the worker nodes.
* **`--head-only`**: Download logs of only the head node.
* **`--unpack/--no-unpack`**: Whether to unpack the combined-worker.log after downloading.
* **`--download-dir`**: Directory to download logs into.
* **`--ttl`**: TTL in seconds to pass to the service that generates presigned URL's (default: 4h).
* **`--parallelism`**: Number of files to download in parallel at a time.
