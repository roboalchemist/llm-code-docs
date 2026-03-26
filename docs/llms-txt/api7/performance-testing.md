# Source: https://docs.api7.ai/enterprise/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.8.x/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.7.x/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.6.x/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.5.x/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.4.x/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.3.x/performance/performance-testing.md

# Source: https://docs.api7.ai/apisix/production/performance/performance-testing.md

# Source: https://docs.api7.ai/enterprise/3.3.x/performance/performance-testing.md

# Source: https://docs.api7.ai/apisix/production/performance/performance-testing.md

# Performance Testing Benchmarks

This document will explain the testing environments, methodologies, and results, to help you evaluate how APISIX performs under various load conditions and how to conduct performance testing yourself.

In addition to referring to the [performance testing benchmarks](#performance-benchmarking-results), you can also conduct your own performance tests with the setup in the [performance benchmark repository](https://github.com/api7/api7-gateway-performance-benchmark). This repository documents in detail all the resource deployment configurations used for testing as well as the specific configuration information for each test scenario. Through this repository, you can conduct performance benchmark tests on your own deployment of APISIX following the provided guidelines. Before starting the tests, please ensure that the [performance baselines](https://docs.api7.ai/enterprise/performance/benchmark.md) you are getting are roughly consistent with the test results.

## Methodologies[â](#methodologies "Direct link to Methodologies")

* **Environment**: Kubernetes.

* **Test Scenarios**:

  <!-- -->

  1. Only enable the [`mocking`](https://apisix.apache.org/docs/apisix/3.2/plugins/mocking) plugin to obtain the baseline performance value of APISIX. This plugin returns mock data in a specified format, and requests are **not forwarded** to upstream servers;
  2. No plugins enabled;
  3. Only enable the [`limit-count`](https://docs.api7.ai/hub/limit-count.md) rate limiting plugin;
  4. Only enable the [`key-auth`](https://docs.api7.ai/hub/key-auth.md) authentication plugin;
  5. Enable both the `key-auth` and `limit-count` plugins;

* **Routes and Consumers**:

  <!-- -->

  1. Single route and a single consumer;
  2. 100 routes and 100 consumers;

* **Sample size**: Test Data Collection: Each test case is run 5 times, with each run lasting 2 minutes. The reported results are the average of the 5 test runs.

## Performance Benchmarking Results[â](#performance-benchmarking-results "Direct link to Performance Benchmarking Results")

* AWS EKS

| Test Scenarios                               | Number of Routes/Consumers | Forward to Upstream | **QPS**    | **P99 (MS)** | **P95 (MS)** |
| -------------------------------------------- | -------------------------- | ------------------- | ---------- | ------------ | ------------ |
| Only enable the `mocking`                    | 1 route, 0 consumers       | False               | 310,392.07 | 1.16         | 1.08         |
| No plugins enabled                           | 1 route, 0 consumers       | True                | 167,019.37 | 2.30         | 2.16         |
| No plugins enabled                           | 100 routes, 0 consumers    | True                | 162,753.17 | 2.31         | 2.16         |
| Only enable the `limit-count`                | 1 route, 0 consumers       | True                | 145,370.10 | 2.43         | 2.24         |
| Only enable the `limit-count`                | 100 routes, 0 consumers    | True                | 143,108.40 | 2.45         | 2.25         |
| Only enable the `key-auth`                   | 1 route, 1 consumer        | True                | 147,869.49 | 2.41         | 2.22         |
| Only enable the `key-auth`                   | 100 routes, 100 consumers  | True                | 145,070.93 | 2.43         | 2.25         |
| Enable both the `key-auth` and `limit-count` | 1 route, 1 consumer        | True                | 136,725.47 | 2.43         | 2.26         |
| Enable both the `key-auth` and `limit-count` | 100 routes, 100 consumers  | True                | 133,782.95 | 2.48         | 2.30         |

## Test Environment[â](#test-environment "Direct link to Test Environment")

This performance test was conducted in the AWS EKS environment. When building the test environment, it is essential to ensure that APISIX, NGINX Upstream, and the performance testing tool [`wrk2`](https://github.com/giltene/wrk2) are deployed on separate nodes, all using `c5.4xlarge` EC2 instances. This configuration ensures a reasonable allocation of resources and avoids resource contention issues.

During stress testing, it is recommended to use the `top` command or other system monitoring tools to monitor the process resource utilization of APISIX and NGINX Upstream servers in real-time. This ensures that each test reaches the performance bottleneck of APISIX, resulting in accurate and reliable performance test results.

Here is an overview of the main components involved in this test and their specifications:

| Name                       | Details                       |
| -------------------------- | ----------------------------- |
| Node                       | Amazon Linux 2 (AL2\_x86\_64) |
| Kubernetes                 | 1.29                          |
| APISIX                     | 3.9                           |
| Upstream Service           | nginx/1.25.4                  |
| Performance Benchmark Tool | wrk2                          |

## Deployment Topology[â](#deployment-topology "Direct link to Deployment Topology")

![K8s deploy](https://static.api7.ai/uploads/2024/06/28/BNqw0uzp_20240628-183402.jpeg)

## Test Configuration[â](#test-configuration "Direct link to Test Configuration")

For this test, the number of `worker_processes` was adjusted to match the available virtual core count (i.e. 16 vCPUs) on the node running APISIX. No further modifications were made to the system configuration.

## Additional Information[â](#additional-information "Direct link to Additional Information")

The following resources are part of API7 Enterprise documentation, but the guidelines and best practices are equally applicable to APISIX.

* [Establish Performance Benchmark](https://docs.api7.ai/enterprise/performance/benchmark.md): Find out how to optimize the performance of APISIX.
* [Guide for Performance Testing of APISIX on AWS EKS](https://docs.api7.ai/enterprise/performance/aws-eks.md): View detailed steps and guidelines on how to establish performance benchmark on AWS EKS.
