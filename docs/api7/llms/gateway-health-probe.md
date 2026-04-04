# Source: https://docs.api7.ai/enterprise/best-practices/gateway-health-probe.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/best-practices/gateway-health-probe.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/best-practices/gateway-health-probe.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/best-practices/gateway-health-probe.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/best-practices/gateway-health-probe.md

# Source: https://docs.api7.ai/enterprise/3.8.x/best-practices/gateway-health-probe.md

# Source: https://docs.api7.ai/enterprise/3.7.x/best-practices/gateway-health-probe.md

# Source: https://docs.api7.ai/enterprise/3.6.x/best-practices/gateway-health-probe.md

# Source: https://docs.api7.ai/enterprise/3.5.x/best-practices/gateway-health-probe.md

# Source: https://docs.api7.ai/enterprise/3.4.x/best-practices/gateway-health-probe.md

# Source: https://docs.api7.ai/enterprise/3.3.x/best-practices/gateway-health-probe.md

# Perform Gateway Health Probing

Health check probing is essential for ensuring the stability and reliability of API7 Enterprise in a production environment. When requests are routed through a load balancer (LB) before reaching the API7 Gateway, the LB can rely on health check probesâsuch as a status endpoint provided by the Gatewayâto monitor its operational state. These probes allow the LB to determine whether the Gateway instances are healthy and ready to handle incoming traffic. If an instance is deemed to be unhealthy, the LB automatically re-routes requests to healthy instances, preventing disruptions and downtime. This mechanism ensures high availability, minimizes the risk of routing requests to unresponsive nodes, and enhances the overall user experience by maintaining continuous service delivery.

This tutorial walks you through the process of enabling the health check probes and checking for Gateway liveness and readiness.

## Enable Health Check Probes[â](#enable-health-check-probes "Direct link to Enable Health Check Probes")

By default, the status probing is not enabled. To enable the check, add the following configuration to the Gateway's configuration file:

config.yaml

```
apisix:
  status:
    ip: 0.0.0.0
    port: 7085
```

â¶ Configure the listening IP to `0.0.0.0` for when the Gateway is deployed in Docker. Fall back to `127.0.0.1` if unconfigured. Adjust accordingly per your deployment.

â· Configure the listening port to `7085`.

Once enabled, the Gateway will provide `/status` and `/status/ready` endpoints for health check probing.

## Check Gateway Running Status[â](#check-gateway-running-status "Direct link to Check Gateway Running Status")

The `/status` endpoint can be used to verify whether the Gateway has successfully started and running. For example, you can send the following request to the Gateway at a regular interval:

```
curl "http://127.0.0.1:7085/status"
```

If the Gateway is healthy, you should receive `200 OK` responses. If the Gateway is not healthy, you should not receive any response and may observe connection refused.

## Check Gateway Readiness for Traffic[â](#check-gateway-readiness-for-traffic "Direct link to Check Gateway Readiness for Traffic")

The `/status/ready` endpoint can be used to verify whether the Gateway is ready to proxy traffic. For example, you can send the following request to the Gateway at a regular interval:

```
curl "http://127.0.0.1:7085/status/ready"
```

If the Gateway is ready to proxy traffic, you should receive `200 OK` responses. If not ready, you should receive `503 Service Temporarily Unavailable` responses.

The readiness is determined by the availability of the database nodes, reported by the DP Manager. The Gateway will respond with `200 OK response` if at least one database node is available. If none of the database nodes is available, the Gateway will respond with `503 Service Temporarily Unavailable`.

## Configure Readiness Probes in Kubernetes[â](#configure-readiness-probes-in-kubernetes "Direct link to Configure Readiness Probes in Kubernetes")

If you are using Kubernetes, you can leverage the readiness probe configuration to check for Gateway readiness. Update the relevant manifest file with the following section:

```
readinessProbe:
  httpGet:
    path: /status/ready
    port: 7085
  initialDelaySeconds: 5
  periodSeconds: 5
```

â¶ Set to the Gateway probing endpoint.

â· Set to the Gateway probing port.

â¸ Wait 5 seconds before performing the first probe.

â¹ Perform a probe every 5 seconds.

See [Configure Liveness, Readiness and Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) for more information.
