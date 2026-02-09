# Source: https://docs.datadoghq.com/security/application_security/setup/kubernetes/gateway-api.md

---
title: Enabling AAP for Gateway API in Kubernetes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Enabling App and API
  Protection > Set up App and API Protection on Kubernetes > Enabling AAP for
  Gateway API in Kubernetes
---

# Enabling AAP for Gateway API in Kubernetes

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="danger" %}
AAP for Gateway API is experimental. Please follow the instructions below to try it out.
{% /alert %}

## Overview{% #overview %}

The **Datadog AppSec Gateway API Request Mirror** enhances application security by leveraging the **RequestMirror** functionality in Kubernetes Gateway APIs to duplicate traffic to a Datadog App &API Protection endpoint. This enables real-time detection and analysis of potential application-level attacks, API endpoint discovery, and more, all without impacting the primary request flow.

## Prerequisites{% #prerequisites %}

- A Kubernetes cluster with [Gateway API CRDs installed](https://gateway-api.sigs.k8s.io/guides/#installing-gateway-api).
- A [controller compatible with the Gateway API RequestMirror filter](https://gateway-api.sigs.k8s.io/implementations).
- [Go](https://go.dev/doc/install) 1.23+ installed on your local machine.

## Enabling threat detection{% #enabling-threat-detection %}

### Installation{% #installation %}

1. **Deploy the Datadog Agent** in your Kubernetes cluster following the [Kubernetes installation guide](https://docs.datadoghq.com/containers/kubernetes/installation/).

1. **Configure the Datadog Agent** to [support incoming AppSec payloads](https://docs.datadoghq.com/tracing/guide/setting_up_apm_with_kubernetes_service/) using APM as transport.

1. **Deploy the AppSec Gateway API Request Mirror** in the namespace of your choice (e.g., `datadog`) along with its service:

   ```bash
   kubectl apply -f https://raw.githubusercontent.com/DataDog/dd-trace-go/refs/heads/main/contrib/k8s.io/gateway-api/cmd/request-mirror/deployment.yml
   ```

1. **Verify the deployment**:

   ```bash
   kubectl get pods -l app=request-mirror
   ```

1. **Patch your Gateway resources** to allow access to the namespace with the deployment:

   ```bash
   git clone https://github.com/DataDog/dd-trace-go.git
   cd dd-trace-go
   go run ./contrib/k8s.io/gateway-api/cmd/patch-gateways
   ```

Use the `-help` flag to see options for customizing the patching behavior.

1. **Patch your HTTPRoute resources** to redirect traffic to the service:

   ```bash
   go run ./contrib/k8s.io/gateway-api/cmd/patch-httproutes
   ```

This command adds a [RequestMirror](https://gateway-api.sigs.k8s.io/guides/http-request-mirroring/) filter to all `HTTPRoute` resources in all namespaces. Use the `-help` flag for configuration options.

**Note**: Regularly running this command ensures any newly created `HTTPRoute` resources automatically include the `RequestMirror` filter. Consider adding the resulting patch to your CI/CD pipeline where `HTTPRoute` resources are modified.

After this configuration is complete, the library collects security data from your application and sends it to the Agent. The Agent sends the data to Datadog, where [out-of-the-box detection rules](https://docs.datadoghq.com/security/default_rules/#cat-application-security) flag attacker techniques and potential misconfigurations so you can take steps to remediate.

1. To see App and API Protection threat detection in action, send known attack patterns to your application. For example, trigger the [Security Scanner Detected](https://docs.datadoghq.com/security/default_rules/security-scan-detected/) rule by running a file that contains the following curl script:

   ```
   for ((i=1;i<=250;i++)); do# Target existing service's routescurl https://your-application-url/existing-route -A dd-test-scanner-log;# Target non existing service's routescurl https://your-application-url/non-existing-route -A dd-test-scanner-log;done
```

**Note**: The `dd-test-scanner-log` value is supported in the most recent releases.

A few minutes after you enable your application and send known attack patterns to it, threat information appears in the [Application Signals Explorer](https://app.datadoghq.com/security/appsec) and vulnerability information appears in the [Vulnerabilities explorer](https://app.datadoghq.com/security/appsec/vm/).

{% video
   url="https://datadog-docs.imgix.net/images//security/application_security/appsec-getstarted-threat-and-vuln_2.mp4" /%}

## Configuration{% #configuration %}

### Environment Variables{% #environment-variables %}

The Gateway API Request Mirror deployment can be configured using the following environment variables:

| Environment Variable                 | Default Value | Description                                                                              |
| ------------------------------------ | ------------- | ---------------------------------------------------------------------------------------- |
| `DD_REQUEST_MIRROR_LISTEN_ADDR`      | `:8080`       | Address and port where the request mirror service listens for incoming mirrored requests |
| `DD_REQUEST_MIRROR_HEALTHCHECK_ADDR` | `:8081`       | Address and port where the health check endpoint is served                               |

Configure the Datadog Agent to receive traces from the integration using the following environment variables:

| Environment Variable  | Default value | Description                                    |
| --------------------- | ------------- | ---------------------------------------------- |
| `DD_AGENT_HOST`       | `localhost`   | Hostname where your Datadog Agent is running   |
| `DD_TRACE_AGENT_PORT` | `8126`        | Port of the Datadog Agent for trace collection |

### Deployment Example{% #deployment-example %}

The default deployment creates a service that listens on port 8080 for mirrored requests and exposes a health check endpoint on port 8081:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: request-mirror
  labels:
    app.kubernetes.io/component: request-mirror
    app.kubernetes.io/name: datadog
spec:
  strategy:
    type: RollingUpdate
  selector:
    matchLabels:
      app: request-mirror
  template:
    metadata:
      labels:
        app: request-mirror
    spec:
      containers:
        - name: request-mirror
          image: ghcr.io/datadog/dd-trace-go/request-mirror:latest
          ports:
            - containerPort: 8080
              name: http
          livenessProbe:
            httpGet:
              path: /
              port: 8081
          readinessProbe:
            httpGet:
              path: /
              port: 8081
          env:
            - name: DD_AGENT_HOST
              value: "datadog-agent"  # Adjust to your Agent service name
---
apiVersion: v1
kind: Service
metadata:
  name: request-mirror
spec:
  selector:
    app: request-mirror
  ports:
    - name: http
      port: 8080
      targetPort: 8080
```

## Datadog Go Tracer and Gateway API integration{% #datadog-go-tracer-and-gateway-api-integration %}

{% alert level="info" %}
The AAP Gateway API integration is built on top of the Datadog Go Tracer. It follows the same release process as the tracer, and its Docker images are tagged with the corresponding tracer version.
{% /alert %}

The Gateway API integration uses the [Datadog Go Tracer](https://github.com/DataDog/dd-trace-go) and inherits all environment variables from the tracer. You can find more information in [Configuring the Go Tracing Library](https://docs.datadoghq.com/tracing/trace_collection/library_config/go/) and [AAP Library Configuration](https://docs.datadoghq.com/security/application_security/policies/library_configuration/).

## Enabling APM tracing{% #enabling-apm-tracing %}

By default, the request mirror traces won't enable Datadog's APM product. If you want to use Application & API Protection without APM tracing functionality, this is the default behavior.

To enable APM tracing, set the environment variable `DD_APM_TRACING_ENABLED=true` in the request mirror deployment.

If you want to explicitly disable APM tracing while using App and API Protection:

1. Configure your deployment with the `DD_APM_TRACING_ENABLED=false` environment variable in addition to the `DD_APPSEC_ENABLED=true` environment variable.
1. This configuration will reduce the amount of APM data sent to Datadog to the minimum required by App and API Protection products.

For more details, see [Standalone App and API Protection](https://docs.datadoghq.com/security/application_security/setup/standalone/).

## Limitations{% #limitations %}

The Gateway API integration has the following limitations:

- It cannot access HTTP responses
- No request blocking can be applied
- Only json is supported for analysing HTTP request bodies.

For finer-grained analysis and other AAP features, consider trying other AAP integrations.

## Further Reading{% #further-reading %}

- [Gateway API integration's source code](https://github.com/DataDog/dd-trace-go/tree/main/contrib/k8s.io/gateway-api)
- [OOTB App and API Protection Rules](https://docs.datadoghq.com/security/default_rules/?category=cat-application-security)
- [Troubleshooting App and API Protection](https://docs.datadoghq.com/security/application_security/troubleshooting)
