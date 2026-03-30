# Source: https://docs.datadoghq.com/security/application_security/setup/nginx/ingress-controller.md

---
title: Set up App and API Protection for Nginx in Kubernetes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Enabling App and API
  Protection > Enabling App and API Protection for Nginx > Set up App and API
  Protection for Nginx in Kubernetes
---

# Set up App and API Protection for Nginx in Kubernetes

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="info" %}
Your platform may be compatible with Datadog's [Single Step Instrumentation](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm), which automatically instruments your services at startup from the Datadog Agent.
{% /alert %}

# Ingress-nginx support for Datadog{% #ingress-nginx-support-for-datadog %}

[Ingress-nginx](https://github.com/kubernetes/ingress-nginx) is a [Kubernetes ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress/) that uses nginx as a reverse proxy and load balancer. In a Kubernetes cluster, external access is restricted by default for security reasons. An ingress controller uses rules to control how external traffic may reach your services.

The ingress-nginx controller is managed through [Kubernetes resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/), but customization of the underlying nginx configuration is typically limited beyond its intended use case. However, ingress-nginx allows the addition of extra nginx modules for extended functionality. To take advantage of this feature with `nginx-datadog`, we provide **init containers**.

## How to enable `nginx-datadog` in ingress-nginx?{% #how-to-enable-nginx-datadog-in-ingress-nginx %}

To integrate `nginx-datadog` with ingress-nginx, add a Datadog [init container](https://hub.docker.com/r/datadog/ingress-nginx-injection) to your pod specification and configure nginx to load the `nginx-datadog` module.

The following Helm values demonstrate how to inject the `nginx-datadog` module into an ingress-nginx controller:

```yaml
controller:
  config:
    main-snippet: "load_module /modules_mount/ngx_http_datadog_module.so;"
  opentelemetry:
    enabled: false
  extraModules:
    - name: nginx-datadog
      image:
        registry: docker.io
        image: datadog/ingress-nginx-injection
        # The tag should match the version of the ingress-nginx controller
        # For example, this will inject the Datadog module for ingress v1.10.0
        # Check <https://hub.docker.com/repository/docker/datadog/ingress-nginx-injection/tags>
        # for the list of all versions supported.
        tag: "v1.10.0"
        distroless: false
```

Check [our details examples](https://github.com/DataDog/nginx-datadog/tree/master/example/ingress-nginx) to help you set up ingress-nginx with `nginx-datadog`.

## How does it work?{% #how-does-it-work %}

Init containers are special containers that run before the main container in a Kubernetes pod. In this case, the Datadog init container is responsible for copying the `nginx-datadog` module into a shared volume that will be accessible by the main ingress-nginx container.

When the main ingrees-nginx controller starts, the nginx configuration must be updated with the `load_module` directive, allowing it to load the Datadog module seamlessly.

{% alert level="danger" %}
We provide a specific init container **for each ingress-nginx controller version**, starting with `v1.10.0`. This is crucial because **each** init container must match the underlying nginx version. To ensure compatibility, ensure the version of the Datadog init container matches your ingress-nginx version.
{% /alert %}

## Interaction with OpenTelemetry{% #interaction-with-opentelemetry %}

By default, ingress-nginx includes an OpenTelemetry (oTel) module that can be enabled using the `enable-opentelemetry: true` setting in the [ingress-nginx ConfigMap](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/#enable-opentelemetry). However, if you are using `nginx-datadog` for tracing, we recommend **disabling** OpenTelemetry to prevent duplicate tracing data from both the oTel and Datadog modules.

To disable OpenTelemetry, set `enable-opentelemetry: false`.

## Enabling AppSec{% #enabling-appsec %}

You can enable the WAF provided by AppSec to protect your applications from security threats. To do so, update your Helm values to include the AppSec configuration:

```yaml
controller:
  config:
    main-snippet: |
      load_module /modules_mount/ngx_http_datadog_module.so;
      # AppSec thread pool configuration (adjust threads and max_queue as needed)
      thread_pool waf_thread_pool threads=2 max_queue=16;
    http-snippet: |
      # Enable AppSec
      datadog_appsec_enabled on;
      datadog_waf_thread_pool_name waf_thread_pool;
  opentelemetry:
    enabled: false
  extraModules:
    - name: nginx-datadog
      image:
        registry: docker.io
        image: datadog/ingress-nginx-injection
        tag: "v1.10.0"
        distroless: false
```

**Key configuration parameters:**

- `thread_pool waf_thread_pool`: Creates a dedicated thread pool for AppSec processing. Adjust `threads` and `max_queue` based on your traffic patterns and available resources.
- `datadog_appsec_enabled on`: Enables the Application Security module for threat detection and protection. This can be omitted so that AppSec can be enabled or disabled through Remote Configuration.
- `datadog_waf_thread_pool_name waf_thread_pool`: Associates the matching requests with the configured thread pool.

Refer to the [configuration reference](https://github.com/DataDog/nginx-datadog/blob/master/doc/API.md) for more configurable options.

{% alert level="info" %}
For production environments, monitor the thread pool performance and adjust the `threads` and `max_queue` parameters based on your traffic volume and latency requirements.
{% /alert %}
