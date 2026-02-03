# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/application-unavailable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Application is Currently Unavailable

> 📘 If you have a [Custom Maintenance Page](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/maintenance-page#custom-maintenance-page) then you will see your maintenance page instead of *Application is currently unavailable*.

## Cause and Resolution

This page will be served by Aptible if your App fails to respond to a web request. There are several reasons why this might happen, each with different steps for resolution:

For further details about each specific occurrence, see [Endpoint Logs](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs).

## The Service for your HTTP(S) Endpoint is scaled to zero

If there are no [Containers](/core-concepts/architecture/containers/overview) running for the [Service](/core-concepts/apps/deploying-apps/services) associated with your [HTTP(S) Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview), this error page will be served. You will need to add at least one Container to your Service in order to serve requests.

## Your Containers are closing the connection without responding

Containers that have unexpectedly restarted will drop all requests that were running and will not respond to new requests until they have recovered. There are two reasons a Container would restart unexpectedly:

* Your Container exceeded the [Memory Limit](/core-concepts/scaling/memory-limits) for your Service. You can tell if your Container has been restarted after exceeding its Memory Limit by looking for the message `container exceeded its memory allocation` in your [Logs](/core-concepts/observability/logs/overview). If your Container exceeded its Memory Limit, consider [Scaling](/core-concepts/scaling/overview) your Service.

* Your Container exited unexpectedly for some reason other than a deploy, restart, or exceeding its Memory Limit. This is typically caused by a bug in your App or one of its dependencies. If your Container unexpectedly exits, you will see `container has exited` in your logs. Your logs may also have additional information that can help you determine why your container unexpectedly exited.

## Your App is taking longer than the Endpoint Timeout to serve requests

Clients will be served this error page if your App takes longer than the [Endpoint Timeout](/core-concepts/apps/connecting-to-apps/app-endpoints/overview#timeouts) to respond to their request. Your [Logs](/core-concepts/observability/logs/overview) may contain request logs that can help you identify specific requests that are exceeding the Endpoint Timeout. If it's acceptable for some of your requests take longer than your current Endpoint Timeout to process, you can increase the Endpoint Timeout by setting the `IDLE_TIMEOUT` [Configuration](/core-concepts/apps/deploying-apps/configuration) variable.

Hitting or exceeding resource limits may cause your App to respond to requests more slowly. Reviewing metrics from your Apps, either on the Aptible dashboard or from your [Metric Drains](/core-concepts/observability/metrics/metrics-drains/overview), can help you identify if you are hitting any resource bottlenecks. If you find that you are hitting or exceeding any resource limits, consider [Scaling](/core-concepts/scaling/overview) your App.

You should also consider deploying [Application Performance Monitoring](/how-to-guides/observability-guides/setup-application-performance-monitoring) for additional insight into why your application is responding slowly.

If you see the Aptible error page that says "This application crashed" consistently every time you [release](/core-concepts/apps/deploying-apps/releases/overview) your App (via Git push, `aptible deploy`, `aptible restart`, etc.), it's possible your App is responding to Aptible's [Release Health Checks](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#release-health-checks), made via `GET /`, before the App is ready to serve other requests. Aptible's zero-downtime deployment process assumes that if your App responds to `GET /`, it is ready to respond successfully to other requests. If that assumption is not true, then your App cannot benefit from our zero-downtime approach, and you will see downtime accompanied by the Aptible error page after each release.

This situation can happen, for example, if your App runs a background process on startup, like precompiling static assets or loading a large data set, and blocks any requests (other than `GET /`) until this process is complete.

The best solution to this problem is to identify whatever background process is blocking requests and reconfigure your App to ensure this happens either (a) in your Dockerfile build or (b) in a startup script **before** your web server starts. Alternatively, you may consider enabling [Strict Health Checks](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks#strict-health-checks)] for your App, using a custom healthcheck request endpoint that only returns 200 when your App is actually ready to serve requests.

> 📘 Your [Endpoint Logs](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs) will contain a specific error message for each of the above problems. You can identify the cause of each by referencing [Endpoint Common Errors](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/endpoint-logs#common-errors).
