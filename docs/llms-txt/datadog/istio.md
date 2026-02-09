# Source: https://docs.datadoghq.com/security/application_security/setup/kubernetes/istio.md

# Source: https://docs.datadoghq.com/security/application_security/setup/compatibility/istio.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/proxy_setup/istio.md

---
title: Instrumenting Istio
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Tracing a Proxy > Instrumenting
  Istio
---

# Instrumenting Istio

Datadog monitors every aspect of your Istio environment, so you can:

- View individual distributed traces for applications transacting over the mesh with APM (see below).
- Assess the health of Envoy and the Istio control plane with [logs](https://docs.datadoghq.com/integrations/istio/).
- Break down the performance of your service mesh with request, bandwidth, and resource consumption [metrics](https://docs.datadoghq.com/integrations/istio/).
- Map network communication between containers, pods, and services over the mesh with [Cloud Network Monitoring](https://docs.datadoghq.com/network_monitoring/performance/setup/#istio).

To learn more about monitoring your Istio environment with Datadog, [see the Istio blog](https://www.datadoghq.com/blog/istio-datadog/).

Datadog APM is available for [supported Istio releases](https://istio.io/latest/docs/releases/supported-releases/#support-status-of-istio-releases).

## Datadog Agent installation{% #datadog-agent-installation %}

1. [Install the Agent](https://docs.datadoghq.com/agent/kubernetes/)
1. [Make sure APM is enabled for your Agent](https://docs.datadoghq.com/agent/kubernetes/apm/).
1. Uncomment the `hostPort` setting so that Istio sidecars can connect to the Agent and submit traces.

## Istio configuration and installation{% #istio-configuration-and-installation %}

To enable Datadog APM, a [custom Istio installation](https://istio.io/docs/setup/install/istioctl/) is required to set two extra options when installing Istio.

- `--set values.global.proxy.tracer=datadog`
- `--set values.pilot.traceSampling=100.0`

```shell
istioctl manifest apply --set values.global.proxy.tracer=datadog --set values.pilot.traceSampling=100.0
```

Traces are generated when the namespace for the pod has sidecar injection enabled. This is done by adding the `istio-injection=enabled` label.

```shell
kubectl label namespace example-ns istio-injection=enabled
```

Traces are generated when Istio is able to determine the traffic is using an HTTP-based protocol. By default, Istio tries to automatically detect this. It can be manually configured by naming the ports in your application's deployment and service. More information can be found in Istio's documentation for [Protocol Selection](https://istio.io/docs/ops/configuration/traffic-management/protocol-selection/)

By default, the service name used when creating traces is generated from the deployment name and namespace. This can be set manually by adding an `app` label to the deployment's pod template:

```yaml
template:
  metadata:
    labels:
      app: <SERVICE_NAME>
```

For [CronJobs](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/), the `app` label should be added to the job template, as the generated name comes from the `Job` instead of the higher-level `CronJob`.

## Deployment and service{% #deployment-and-service %}

If the Agents on your cluster are running as a deployment and service instead of the default DaemonSet, then an additional option is required to specify the DNS address and port of the Agent. For a service named `datadog-agent` in the `default` namespace, that address would be `datadog-agent.default.svc.cluster.local:8126`.

- `--set values.global.tracer.datadog.address=datadog-agent.default.svc.cluster.local:8126`

If Mutual TLS is enabled for the cluster, then the Agent's deployment should disable sidecar injection, and you should add a traffic policy that disables TLS.

This annotation is added to the Agent's Deployment template.

```
  template:
    metadata:
      annotations:
        sidecar.istio.io/inject: "false"
```

For Istio v1.4.x, the traffic policy can be configured using a DestinationRule. Istio v1.5.x and higher do not need an additional traffic policy.

```
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: datadog-agent
  namespace: istio-system
spec:
  host: datadog-agent.default.svc.cluster.local
  trafficPolicy:
    tls:
      mode: DISABLE
```

Automatic Protocol Selection may determine that traffic between the sidecar and Agent is HTTP, and enable tracing. This can be disabled using [manual protocol selection](https://istio.io/docs/ops/configuration/traffic-management/protocol-selection/#manual-protocol-selection) for this specific service. The port name in the `datadog-agent` Service can be changed to `tcp-traceport`. If using Kubernetes 1.18+, `appProtocol: tcp` can be added to the port specification.

## Environment variables{% #environment-variables %}

Environment variables for Istio sidecars can be set on a per-deployment basis using the `proxy.istio.io/config` annotation. This is unique for deployments employing Istio sidecars.

```yaml
apiVersion: apps/v1
...
kind: Deployment
...
spec:
  template:
    metadata:
      annotations:
        proxy.istio.io/config: |
          proxyMetadata:
            "DD_ENV": "prod"
            "DD_SERVICE": "my-service"
            "DD_VERSION": "v1.1"
```

## Further Reading{% #further-reading %}

- [Istio website](https://istio.io/)
- [Istio documentation](https://istio.io/docs/)
- [Datadog C++ Client](https://github.com/DataDog/dd-trace-cpp)
