# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Health Checks

When you add [HTTP(S) Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview), Aptible performs health checks on your App [Containers](/core-concepts/architecture/containers/overview) when deploying and throughout their lifecycle.

<Note>The Endpoint has no notion of what hostname the App expects, so it sends health check requests to your application with `containers` as the [host](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host). This is not a problem for most applications but for those that only allow the use of certain hosts, such as applications built with Django that use `ALLOWED_HOSTS`, this may result in non-200 responses. These applications will need to exempt hostname checking or add `containers` to the list of allowed hosts on `/healthcheck`.</Note>

# Health Check Modes

Health checks on Aptible can operate in two modes:

## Default Health Checks

In this mode (the default), Aptible expects your App Containers to respond to health checks with any valid HTTP response, and does not care about the status code.

## Strict Health Checks

When Strict Health Checks are enabled, Aptible expects your App Containers to respond to health checks with a `200 OK` HTTP response. Any other response will be considered a [failure](/how-to-guides/troubleshooting/common-errors-issues/http-health-check-failed).

Strict Health Checks are useful if you're doing further checking in your App to validate that it's up and running.

To enable Strict Health Checks, set the `STRICT_HEALTH_CHECKS` [Configuration](/core-concepts/apps/deploying-apps/configuration) variable on your App to the value `true`. This  setting will apply to all Endpoints associated with your App.

<Warning> Redirections are not `200 OK` responses, so be careful with e.g. SSL redirections in your App that could cause your App to respond to the health check with a redirect, such as Rails' `config.force_ssl = true`. Overall, we strongly recommend verifying your logs first to check that you are indeed returning `200 OK` on `/healthcheck` before enabling Strict Health Checks.</Warning>

# Health Check Lifecycle

Aptible performs health checks at two stages:

* [Release Health Checks](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#release-health-checks) when releasing new App [Containers](/core-concepts/architecture/containers/overview).
* [Runtime Health Checks](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#runtime-health-checks) throughout the lifecycle of your App [Containers](/core-concepts/architecture/containers/overview).

## Release Health Checks

When deploying your App, Aptible ensures that new App Containers are receiving traffic before they're registered with load balancers.

When [Strict Health Checks](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#strict-health-checks) are enabled, this request is performed on `/healthcheck`, otherwise, it is simply performed at `/`. In either case, the request is sent to the [Container Port](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview#container-port) for the Endpoint.

### Release Health Check Timeout

By default, Aptible waits for up to 3 minutes for your App to respond. If needed, you can increase that timeout by setting the `RELEASE_HEALTHCHECK_TIMEOUT` [Configuration](/core-concepts/apps/deploying-apps/configuration) variable on your App.

This variable must be set to your desired timeout in seconds. Any value from 0 to 900 (15 minutes) seconds is valid (we recommend that you avoid setting this to anything below 1 minute).

You can set this variable using the [`aptible config:set`](/reference/aptible-cli/cli-commands/cli-config-set) command:

```shell  theme={null}
aptible config:set --app "$APP_HANDLE" \
        RELEASE_HEALTHCHECK_TIMEOUT=600
```

## Runtime Health Checks

<Note>This health check is only executed if your [Service](/core-concepts/apps/deploying-apps/services) is scaled to 2 or more Containers.</Note>

When your App is live, Aptible periodically runs a health check to determine if your [Containers](/core-concepts/architecture/containers/overview) are healthy. Traffic will route to a healthy Container, except when:

* No Containers are healthy. Requests will route to **all** Containers, regardless of health status, and will still be visible in your [Endpoint Logs](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs).
* Your Service is scaled to zero. Traffic will instead route to [Brickwall](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/maintenance-page#brickwall), our error page server.

The health check is an HTTP request sent to `/healthcheck`. A healthy Container must respond with `200 OK` HTTP response if [Strict Health Checks](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#strict-health-checks) are enabled, or any status code otherwise. See [Endpoint Logs](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs) for information about how Runtime Health Checks error logs can be viewed, and [Health Checks Failed](/how-to-guides/troubleshooting/common-errors-issues/http-health-check-failed) dealing with failures.

<Note> If needed, you can identify requests to `/healthcheck` coming from Aptible: they'll have the `X-Aptible-Health-Check` header set.</Note>

### Mechanics and timing

The following are the intervals and thresholds for runtime health checks:

* **Interval**: every 20 seconds
* **Failed Check**: No response with 15 seconds from a target means a failed health check.
* **Unhealthy threshold**: 3 consecutive failed checks to mark a target unhealthy
* **Healthy threshold**: 2 consecutive successful checks to mark a target healthy

Consider the following impacts and mitigations for when containers are marked unhealthy:

* During the time it takes to confirm your container is unhealthy, requests will still be routed to this container, and you and/or you end users will be impacted if your container does not respond to those requests. When that happens and the app container is not responding, users will see the App's [Maintenance Page](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/maintenance-page).
* Horizontally scaling a service reduces the impact of a single container becoming unhealthy. For example, if your service runs on 2 containers and one fails, users may experience around one minute of a 50% error rate until traffic fully shifts away from the failing container. Scaling to 5 containers would lower this impact proportionally, resulting in an estimated 20% error rate during the same transition period.
* Using the [least-oustanding-request load balancer strategy](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview#traffic) can be beneficial in mitigating impact while a target/container is transitioning to failed status, since it's likely to have more open/stalled requests, keeping new requests routed to any other containers that are functioning normally.
