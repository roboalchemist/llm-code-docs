# Source: https://docs.api7.ai/enterprise/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.8.x/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.7.x/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.6.x/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.5.x/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.4.x/performance/benchmark.md

# Source: https://docs.api7.ai/enterprise/3.3.x/performance/benchmark.md

# Establish Performance Benchmark

To ensure the accuracy of API7 Gateway performance evaluation, please follow these key recommendations and steps before conducting benchmark tests.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

* **Select an Appropriate Number of Gateway Nodes**:

  <!-- -->

  1. Use a single API7 Gateway node and configure the number of `worker_processes` based on machine resources (CPU cores or vCPU cores). It is recommended to initially configure 1 `worker_processes` for baseline testing and proceed with multi-core performance testing once the [results](#performance-baseline-test-results) are confirmed.
  2. Avoid using API7 Gateway nodes with multiple smaller configurations of `worker_processes`.

* **Gradually Increase the Number of `worker_processes`**:

  <!-- -->

  1. During the initial testing, set the `worker_processes` to `1` to obtain a single-core performance baseline.
  2. After setting the single-core baseline performance, gradually increase the number of `worker_processes` to evaluate performance under multiple cores.

* **Exclude Upstream Network Interference**:
  <!-- -->
  1. Enable only the [`mocking`](https://apisix.apache.org/docs/apisix/3.2/plugins/mocking/) plugin to obtain the performance baseline of API7 Gateway. This plugin returns mock data in a specified format without forwarding requests to upstream servers.

* **Ensure Upstream Server Performance**:
  <!-- -->
  1. Closely monitor the performance of API7 Gateway and upstream servers during testing to ensure that the upstream server is not a performance bottleneck.

* **Collect Baseline Results**:

  <!-- -->

  1. Collect baseline results before testing additional scenarios. Configure 1 API7 Gateway node and enable 1 `worker_processes`;
  2. Eliminate gateway latency interference. Deploy the upstream server and API7 Gateway on the same machine and use Host networking;
  3. Ensure that the collected baseline results are largely consistent with the provided [reference results](#performance-baseline-test-results).

* **Collect and Analyze Test Results**:
  <!-- -->
  1. Collect multiple sets of test results and analyze the differences in the data using statistical methods (e.g., standard deviation) to ensure the stability and reliability of the test results.

* **Refer to [Optimization Recommendations](#optimize-api7-gateway-performance)**:
  <!-- -->
  1. After following the above recommendations and completing the tests, you can conduct benchmark tests for other scenarios based on actual needs. However, before doing so, please ensure that the collected **performance baseline test results** are largely consistent with the reference data, and carefully read the optimization suggestions provided below to make necessary adjustments to the configuration based on actual testing requirements.

### Performance Baseline Test Deployment Topology[â](#performance-baseline-test-deployment-topology "Direct link to Performance Baseline Test Deployment Topology")

![ec2 deploy](https://static.api7.ai/uploads/2024/06/25/2bp54aMM_20240625-092434.jpeg)

### Performance Baseline Test Results[â](#performance-baseline-test-results "Direct link to Performance Baseline Test Results")

While collecting the baseline test results, API7 Gateway (with 1 `worker_processes`), the NGINX upstream server, and the benchmarking tool `wrk2` were deployed on the same machine, utilizing the host network for communication.

| Test Scenarios                               | Number of Routes/Consumers | **QPS**   | **P99 (MS)** | **P95 (MS)** |
| -------------------------------------------- | -------------------------- | --------- | ------------ | ------------ |
| No plugins enabled                           | 1 route, 0 consumers       | 24,129.22 | 0.093        | 0.082        |
| No plugins enabled                           | 100 routes, 0 consumers    | 23,652.91 | 0.096        | 0.084        |
| Only enable the `limit-count`                | 1 route, 0 consumers       | 20,495.10 | 0.104        | 0.092        |
| Only enable the `limit-count`                | 100 routes, 0 consumers    | 20,462.31 | 0.104        | 0.094        |
| Only enable the `key-auth`                   | 1 route, 1 consumer        | 21,019.04 | 0.100        | 0.089        |
| Only enable the `key-auth`                   | 100 routes, 100 consumers  | 20,444.81 | 0.109        | 0.095        |
| Enable both the `key-auth` and `limit-count` | 1 route, 1 consumer        | 18,940.39 | 0.110        | 0.097        |
| Enable both the `key-auth` and `limit-count` | 100 routes, 100 consumers  | 18,193.88 | 0.110        | 0.098        |

By following the steps and recommendations outlined above, you will be able to more accurately evaluate the performance of API7 Gateway in different scenarios, providing valuable data support for subsequent optimization and deployment.

## Optimize API7 Gateway Performance[â](#optimize-api7-gateway-performance "Direct link to Optimize API7 Gateway Performance")

### Check Maximum Number of Open Files[â](#check-maximum-number-of-open-files "Direct link to Check Maximum Number of Open Files")

Check the current system's maximum number of open files overall:

```
cat /proc/sys/fs/file-nr
3984 0 3255296
```

The last number `3255296` represents the maximum number of open files. If this number is too small on your machine, you need to modify the `/etc/sysctl.conf` file to increase it.

```
# /etc/sysctl.conf
fs.file-max = 1020000
net.ipv4.ip_conntrack_max = 1020000
net.ipv4.netfilter.ip_conntrack_max = 1020000
```

The change will take effect after a reload:

```
sudo sysctl -p /etc/sysctl.conf
```

### Check the `ulimit`[â](#check-the-ulimit "Direct link to check-the-ulimit")

Each user request corresponds to a file handle, and during stress testing, a large number of requests will be generated, so you need to increase this value. Use `ulimit -n` to check, and if it is a small value (the default is `1024`), it should be modified to a million-level number, such as `1024000`.

To temporarily modify it:

```
ulimit -n 1024000
```

To permanently modify it:

```
vim /etc/security/limits.conf

# Add the following lines
* hard nofile 1024000
* soft nofile 1024000
```

### Avoiding Resource Contention[â](#avoiding-resource-contention "Direct link to Avoiding Resource Contention")

Ensure that `wrk2`, API7 Gateway, and upstream services are installed on separate machines and tested within the same host network to reduce the overhead caused by network latency.

If these resources are running on a single Kubernetes cluster, make sure the pods for the three services are scheduled on different nodes to avoid resource contention (e.g., in CPU and network), which can lead to degraded performance.

### Upstream Server Reaching Limits[â](#upstream-server-reaching-limits "Direct link to Upstream Server Reaching Limits")

Check if the upstream server is reaching its limits. During the stress test, monitor the CPU and memory usage of the upstream server to determine if it has reached its maximum capacity. If increasing the `worker_processes` count in API7 Gateway does not yield any improvement, it may be that the upstream server or other systems have reached a bottleneck.

### Disabling I/O for Access Logs[â](#disabling-io-for-access-logs "Direct link to Disabling I/O for Access Logs")

During performance benchmark testing, it is important to minimize the impact of access logs on performance, especially with high traffic scenarios involving significant log writing operations. Disabling `access_log` can alleviate the pressure on disk `I/O`.

### Cloud Provider Performance Issues[â](#cloud-provider-performance-issues "Direct link to Cloud Provider Performance Issues")

Avoid using **burstable instances** provided by cloud servers. The available CPU for such instances is variable, which can unnecessarily impact test data.

info

The mapping between vCPUs (virtual CPU) and physical CPU provided by different cloud providers in their instance types is not always **1:1**. Some instances use hyper-threading techniques, which means the actual number of physical CPU cores might be only half of the vCPU count.

To accurately understand the vCPU to physical CPU mapping for a specific instance type, it is recommended to consult the official documentation published by the cloud provider. For example, see [AWS Instance Information](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cpu-options-supported-instances-values.html).

### API7 Gateway Internal Errors[â](#api7-gateway-internal-errors "Direct link to API7 Gateway Internal Errors")

Before starting performance benchmarking, it is important to adjust the log severity level in API7 Gateway to `error` and ensure that there are no internal errors in the error logs.

### Using `c1000k` to Check Concurrent Connections[â](#using-c1000k-to-check-concurrent-connections "Direct link to using-c1000k-to-check-concurrent-connections")

Install [c1000k](https://github.com/ideawu/c1000k) to check if the test environment can meet the requirements of 1 million concurrent connections.

```
# Start the server, listening on port 7000
. /server 7000

# Run the client to simulate a stress test
. /client 127.0.0.1 7000
```

## API7 Gateway Configuration Example[â](#api7-gateway-configuration-example "Direct link to API7 Gateway Configuration Example")

config.yaml

```
nginx_config:
  error_log_level: error
  worker_processes: auto

  http:
    enable_access_log: false
```
