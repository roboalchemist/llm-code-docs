# Source: https://docs.api7.ai/enterprise/best-practices/telemetry-compression.md

# Optimize Telemetry Data Transfer

The Data Plane (DP) periodically reports its operational status and metric data to the Control Plane (CP) to enable centralized monitoring, management, and analysis. To reduce network transmission overhead, the DP enables Gzip compression by default when reporting telemetry data.

This guide explains how to configure telemetry data transfer and compression levels to optimize the balance between network bandwidth usage and CPU consumption.

## Data Transfer from DP to CP[â](#data-transfer-from-dp-to-cp "Direct link to Data Transfer from DP to CP")

The DP periodically sends telemetry metrics to the CP, including Key Performance Indicators (KPIs) such as API traffic, request latency, status codes, bandwidth, and connection counts. The metrics follow the [Prometheus format](https://docs.api7.ai/hub/prometheus.md#metrics) and provide the foundation for monitoring and alerting.

### Customize Data Transfer Configuration[â](#customize-data-transfer-configuration "Direct link to Customize Data Transfer Configuration")

By default, the DP reports telemetry data to the CP every 15 seconds. You can customize this frequency and related settings in the gateway's [configuration file](https://docs.api7.ai/enterprise/reference/configuration.md).

The following configuration lists all telemetry options with their default values:

conf/config.yaml

```
api7ee:
  telemetry:
    # -- Whether to enable telemetry data reporting to the control plane
    enable: true
    
    # -- Time interval for sending telemetry data to the control plane (seconds)
    interval: 15
    
    # -- Maximum size of metrics data sent to the control plane (bytes, default 32MB), exceeding parts will be truncated
    max_metrics_size: 33554432
    
    # -- Maximum batch size before compression (bytes, default 4MB)
    metrics_batch_size: 4194304
    
    # -- gzip compression level. -1 uses the library's default (usually 6), range 0-9; 1 is fastest, 9 is highest compression ratio
    compression_level: -1
```

### Understand Gzip Compression Levels[â](#understand-gzip-compression-levels "Direct link to Understand Gzip Compression Levels")

To reduce network transmission overhead, the DP enables Gzip compression by default when reporting telemetry data. The configurability of the compression level allows users to make a trade-off between CPU consumption and network bandwidth.

By default, Gzip compression is set to `-1`. You can customize the compression level via the `api7ee.telemetry.compression_level` parameter in the gateway's configuration file.

| Level | Description              | Characteristics                                                 |
| ----- | ------------------------ | --------------------------------------------------------------- |
| -1    | Use zlib library default | Typically level 6                                               |
| 0     | No compression           | Only packages data; no CPU consumption, largest data size.      |
| 1     | Fastest compression      | Lowest CPU consumption, lowest compression ratio.               |
| 6     | Balanced compression     | The best balance between CPU consumption and compression ratio. |
| 9     | Highest compression      | Highest compression ratio, highest CPU consumption.             |

### Disable Data Transfer[â](#disable-data-transfer "Direct link to Disable Data Transfer")

To disable telemetry data transfer, set the `api7ee.telemetry.enable` parameter to `false` in the configuration file. Be aware that disabling telemetry has the following impacts:

| Impact Category                | Details                                                                                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Loss of Observability          | The Control Plane will no longer receive performance metrics from the data plane. Monitoring dashboards and alerting systems will be ineffective. |
| Impaired Operational Decisions | Operations teams lose a key source of data for assessing service health, planning capacity, and troubleshooting issues.                           |
| Compliance Risks               | Certain industry compliance requirements for system monitoring and auditing may no longer be met.                                                 |

warning

Unless there is a special requirement (e.g., in a debugging or completely isolated environment), it is strongly recommended not to disable this feature.

## Compression Performance Testing[â](#compression-performance-testing "Direct link to Compression Performance Testing")

This section provides a complete testing workflow to validate the effects of different compression levels on data size and CPU performance in a real-world environment.

### Prerequisites[â](#prerequisites "Direct link to Prerequisites")

Before starting the test, make sure your environment is properly set up and meets the following requirements.

#### Prepare API7 Enterprise[â](#prepare-api7-enterprise "Direct link to Prepare API7 Enterprise")

Ensure the following:

* An API7 Enterprise deployment including a CP and at least one DP (gateway).
* The DP is able to report data to the CP normally.
* Permissions to modify the DP configuration file and restart the container.
* Access to the DP's logs and monitoring metrics.

#### Prepare Traffic Generation Tool[â](#prepare-traffic-generation-tool "Direct link to Prepare Traffic Generation Tool")

To generate realistic metrics data, a certain amount of request traffic needs to be sent to the DP. The following script can be used to create a large number of routes and then send requests to the DP to generate sufficient metrics data.

The example script below creates 60 services, with each service containing 60 routes, for a total of 3600 routes.

create-routes.sh

```
#!/usr/bin/env bash
set -e

############################
# 1. Pre-test Preparation
############################

# Replace with your admin API address and access token
ADMIN_API="http://127.0.0.1:7080"
ADMIN_KEY="$API7_EE_TOKEN"

############################
# 2. Create 60 services, each with 60 routes
############################

echo "==> Creating 60 services, each with 60 routes..."

for i in $(seq 1 60); do
  SERVICE_ID="demo-echo-service-${i}"
  SERVICE_PREFIX="/service-${i}"

  echo ""
  echo "==> Creating service ${i}/60: ${SERVICE_ID} (prefix: ${SERVICE_PREFIX})"

  curl -s -X PUT "${ADMIN_API}/apisix/admin/services/${SERVICE_ID}?gateway_group_id=default" \
    -H "X-API-KEY: ${ADMIN_KEY}" \
    -H "Content-Type: application/json" \
    -d "{
      \"id\": \"${SERVICE_ID}\",
      \"name\": \"${SERVICE_ID}\",
      \"desc\": \"service ${i} with 60 echo routes (prefix: ${SERVICE_PREFIX})\",
      \"upstream\": {
        \"type\": \"roundrobin\",
        \"nodes\": []
      }
    }" | jq .

  echo "   Creating 60 routes for service ${i}..."

  for j in $(seq 1 60); do
    ROUTE_ID="echo-route-service-${i}-${j}"
    URI="${SERVICE_PREFIX}/${j}/get"

    curl -s -X PUT "${ADMIN_API}/apisix/admin/routes/${ROUTE_ID}?gateway_group_id=default" \
      -H "X-API-KEY: ${ADMIN_KEY}" \
      -H "Content-Type: application/json" \
      -d "{
        \"name\": \"${ROUTE_ID}\",
        \"service_id\": \"${SERVICE_ID}\",
        \"methods\": [\"GET\"],
        \"paths\": [\"${URI}\"],
        \"plugins\": {
          \"echo\": {
            \"before_body\": \"hello from service ${i}, route ${j}\",
            \"headers\": {
              \"X-Service-Index\": \"${i}\",
              \"X-Route-Index\": \"${j}\"
            }
          }
        }
      }" > /dev/null

    echo "   â Created route ${URI}"
  done
done

############################
# 3. Completion Prompt
############################

echo ""
echo "â Done!"
echo "Created 60 services, each with 60 routes (3600 routes total)"
echo ""
echo "Test examples:"
echo "  curl http://<gateway-host>:9080/service-1/1/get"
echo "  curl http://<gateway-host>:9080/service-2/15/get"
echo "  curl http://<gateway-host>:9080/service-10/30/get"
```

### Run Compression Test[â](#run-compression-test "Direct link to Run Compression Test")

In this test, you will modify the compression levels and generate traffic to measure their impact on performance.

#### Modify Compression Level[â](#modify-compression-level "Direct link to Modify Compression Level")

Adjust the `compression_level` in the DP's [configuration file](#customize-data-transfer-configuration) to different compression levels:

config.yaml

```
api7ee:
  telemetry:
    compression_level: 1  # Example: test levels 1, 6, and 9
```

Restart the DP container (Docker) or upgrade the gateway release (Kubernetes) to apply the configuration changes. Then, generate test traffic and observe the impact on CPU usage and data size.

#### Generate Test Traffic[â](#generate-test-traffic "Direct link to Generate Test Traffic")

Generate sufficient requests to the DP to produce meaningful metrics data:

generate-traffic.sh

```
#!/usr/bin/env bash
set -e

############################
# 1. Configuration
############################

# Replace with your gateway listening address
DP_HOST="http://127.0.0.1:9080"
SERVICE_COUNT=60
ROUTES_PER_SERVICE=60
TOTAL=$((SERVICE_COUNT * ROUTES_PER_SERVICE))

############################
# 2. Test Routes
############################

echo "==> Testing ${TOTAL} echo routes (${SERVICE_COUNT} services Ã ${ROUTES_PER_SERVICE} routes each)..."

ROUTE_NUM=0
for i in $(seq 1 ${SERVICE_COUNT}); do
  echo ""
  echo "==> Testing service ${i}/${SERVICE_COUNT} (prefix: /service-${i}/)..."

  for j in $(seq 1 ${ROUTES_PER_SERVICE}); do
    ROUTE_NUM=$((ROUTE_NUM + 1))
    URL="${DP_HOST}/service-${i}/${j}/get"

    echo -n "[${ROUTE_NUM}/${TOTAL}] GET ${URL} ... "

    RESPONSE=$(curl -s -o /tmp/echo_test_service${i}_route${j}.out -w "%{http_code}" "${URL}")
  done
done

echo ""
echo "â All routes are accessible!"
```

#### Collect Test Data[â](#collect-test-data "Direct link to Collect Test Data")

For each compression level, collect the following data:

* **CPU Usage:** Continuously monitor during the traffic stress test.
* **Compressed Data Size:** Use `tcpdump` to capture the network traffic from the DP to the CP to analyze the size of the compressed data.

The following instructions assume the gateway is running in Docker. If your gateway is deployed on Kubernetes, adjust the steps accordingly.

1. Record CPU Usage (continuously monitor during the upload process):

   ```
   docker stats ${gateway-container-name}
   ```

2. Get the original data size from the DP container:

   ```
   docker exec -it ${gateway-container-name} /bin/sh

   curl "http://127.0.0.1:9091/apisix/prometheus/metrics" | wc -c
   ```

3. Use `tcpdump` to capture the network traffic from the DP to the CP to analyze the size of the compressed data:

   ```
   sudo tcpdump -i any -w /tmp/dp_to_cp_level_X.pcap host ${cp-address} and port ${cp-port}
   ```

   info

   DP and CP communicate using mTLS, which may affect the results of packet capture.

### Review Test Results[â](#review-test-results "Direct link to Review Test Results")

Example test results for different compression levels are shown in the table below:

| Measurement                       | Level 1 | Level 6 | Level 9 |
| --------------------------------- | ------- | ------- | ------- |
| Original Metrics Data Size (MB)   | 7.71    | 6.60    | 6.45    |
| Compressed Data Size (MB)         | 0.22    | 0.16    | 0.12    |
| Compression Ratio (Space Saved %) | 97.10%  | 97.54%  | 97.98%  |
| DP CPU Usage                      | 17.39%  | 21.57%  | 29.61%  |

The test results show the trade-offs of different Gzip compression levels. As the level increases from 1 to 9, the compressed data size decreases and the compression ratio improves, reducing network bandwidth usage.

However, higher compression levels also increase CPU usage on the DP. Level 6 provides a good balance, offering strong compression with moderate CPU impact, while Level 9 achieves maximum compression at the cost of significantly higher CPU consumption. Choose the compression level based on your environmentâs CPU capacity and bandwidth requirements.
