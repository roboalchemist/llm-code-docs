# Source: https://www.apollographql.com/docs/graphos/routing/observability/router-telemetry-otel/enabling-telemetry/usage-guides/debugging-client-requests.md

# Debugging Client Requests to GraphOS Router

By default, the GraphOS Router operates [without generating HTTP request logs or exporting telemetry metrics beyond what it sends to GraphOS](https://www.apollographql.com/docs/graphos/routing/observability).
This default minimizes potentially high observability costs that can result from high request volumes.
If you need more data than the default [GraphOS Insights](https://www.apollographql.com/docs/graphos/platform/insights), you can configure your router to collect and export additional telemetry.

## Using GraphOS Insights

GraphOS Studio lets you analyze data from failed requests, such as GraphQL error messages ([if enabled](https://www.apollographql.com/docs/graphos/routing/graphos-reporting#errors)) and the ID of the client making the request. You can also [segment your insights data](https://www.apollographql.com/docs/graphos/platform/insights/client-segmentation) based on the client ID.

[Learn how to ensure client IDs are included in all requests.](https://www.apollographql.com/docs/graphos/routing/observability/client-id-enforcement)

## Enabling additional telemetry

You can instrument [router telemetry](https://www.apollographql.com/docs/graphos/routing/observability/telemetry) if you need information outside of what's presented in GraphOS Studio to debug client requests.

If you want to debug client requests in your own environment, Apollo recommends first doing so in a non-production environment or using logic to debug on a per-request basis.

### Logging requests

You can conditionally include request bodies, including GraphQL operations, in your telemetry based on specific [conditions](https://www.apollographql.com/docs/graphos/reference/router/telemetry/instrumentation/conditions). Apply these conditions on a router request [event](https://www.apollographql.com/docs/graphos/reference/router/telemetry/instrumentation/events) like so:

```yaml title=router.yaml
telemetry:
  instrumentation:
    events:
      router:
        request:
          level: info
          condition: # Only log the router request if you sent `x-log-request` with the value `enabled`
            eq:
            - request_header: x-log-request
            - "enabled"
```

### Debugging router logs

By default, the router uses the `info` level for its logging. [Enabling other logging levels](https://www.apollographql.com/docs/graphos/reference/router/telemetry/log-exporters/overview) can help debug specific scenarios. Using non-`info` level configurations is only recommended for local or non-production environments.

## Rhai scripts and coprocessors

Hooking into the router service layer with either [Rhai scripts](https://www.apollographql.com/docs/graphos/routing/customization/rhai) or [coprocessors](https://www.apollographql.com/docs/graphos/routing/customization/coprocessor) gives you access to the full HTTP request before processing occurs. You can use either Rhai scripts or coprocessors to add custom logic for what to log and when.

See the Apollo Solutions ["Hello World" coprocessor](https://github.com/apollosolutions/example-coprocessor-helloworld) for an example of a coprocessor that simply logs the router's payload.

The code in this repository is experimental and has been provided for reference purposes only.

## Alternative cloud services

If you are deploying the router to a cloud service, you likely already have access to the raw HTTP logs through other services like load balancers. You should be able to find specific client request logs for a particular operation using the operation hash or trace ID. Refer to the docs for your cloud providers for more information. Popular cloud provider links are provided below.

### Amazon Web Services

* [AWS CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
* [AWS Elastic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)

### Google Cloud Platform

* [Google Cloud Observability](https://cloud.google.com/logging/docs/log-analytics)
* [Google Cloud Load Balancing](https://cloud.google.com/load-balancing/docs/l7-internal/monitoring)

### Microsoft Azure

* [Azure App Service Logging](https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs)
* [Azure Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/monitor-load-balancer)
