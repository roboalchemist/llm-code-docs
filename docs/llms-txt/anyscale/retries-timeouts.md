# Source: https://docs.anyscale.com/services/retries-timeouts.md

# Manage timeouts and retries for Anyscale services

[View Markdown](/services/retries-timeouts.md)

# Manage timeouts and retries for Anyscale services

This page provides an overview of timeouts and retries as they relate to latency and backpressure with Anyscale services. Understanding the default timeout behavior for Anyscale services and configuring your Ray Serve applications and queries to gracefully handle timeouts and retries is essential for building responsive and scalable applications.

Reach out to [Anyscale support](mailto:support@anyscale.com) if you have additional questions on troubleshooting performance for Anyscale services.

## Why is it important to consider timeouts and retries for services?[​](#why-important "Direct link to Why is it important to consider timeouts and retries for services?")

While autoscaling helps to increase the size of your cluster in response to heavy query traffic, configuring timeouts and gracefully handling timeout responses help reduce transient failures and unresponsive queries.

Ray Serve doesn't drop requests by default when it's overloaded, but timing out requests and disconnecting from the client reduces the load on the service and allows it to keep up with inbound traffic. For this reason, client retries should also use exponential back-off to reduce load when the service can't respond in time.

Configuring timeouts is also helpful for identifying issues in your production applications. Instead of observing hanging behavior and latency spikes without a clear source, you see timeout errors in client and server logs associated with specific parts of your service.

## Load balancer timeouts[​](#load-balancer "Direct link to Load balancer timeouts")

Anyscale uses the default timeout thresholds for load balancers on AWS and Google Cloud. Some applications might need to exceed these thresholds for serving. Contact [Anyscale support](mailto:support@anyscale.com) for help troubleshooting or to request an increase to timeout thresholds.

The following table describes the default timeout thresholds:

| Cloud        | Description                                                                                                                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS          | Anyscale sets the default idle connect timeout for Application Load Balancer to 300 seconds. Requests that exceed this threshold with no observed response might return a `504` HTTP response code.      |
| Google Cloud | The default timeout for Google Cloud Load Balancing is 600 seconds. Requests that exceed this threshold might return a `408` HTTP response code, even if the application has started sending a response. |

## Configure client-side timeouts and retries[​](#configure-client-side-timeouts-and-retries "Direct link to Configure client-side timeouts and retries")

You should design your query client to expect transient errors and avoiding overwhelming your API endpoints.

To minimize user-facing disruptions, Anyscale recommends the following client-side configurations:

* Retries with exponential backoff.
* Query timeouts that respect application latency.

The following is a simple example of this pattern using the Python `requests` library:

```
import requests
from requests.adapters import HTTPAdapter, Retry

session = requests.Session()

retries = Retry(
    total=5,  # 5 retries total
    backoff_factor=1,  # Exponential back-off
    status_forcelist=[  # Retry on server errors
        500,
        501,
        502,
        503,
        504,
    ],
)

session.mount("http://", HTTPAdapter(max_retries=retries))

response = session.get("http://localhost:8000/", timeout=10) # Timeout after 10s
result = response.text
```

## Configure server-side request timeout for an Anyscale service[​](#configure-server-side-request-timeout-for-an-anyscale-service "Direct link to Configure server-side request timeout for an Anyscale service")

You can set a global server-side timeout for all requests to your Anyscale service. The counter for this timeout begins when the request enters a queue.

Configure this threshold using the `request_timeout_s` setting in the `http_options` of the [service config](/reference/service-api.md#serviceconfig), as in the following example:

```
name: my-service
applications:
  - import_path: main:app
http_options:
  request_timeout_s: 60
```

## Configure load shedding[​](#configure-load-shedding "Direct link to Configure load shedding")

By default, Ray Serve doesn't drop requests when overloaded and relies on timeouts for back pressure. This can cause server-side queues to build up and tail latencies to increase under load if clients misbehave.

Configure the `max_queued_requests` option in your Ray Serve deployment to drop requests when a queue exceeds a given threshold. This sends a `503` HTTP message back to the calling client. Configuring your client with retries and exponential backoff can help to relieve temporary pressure.

See the [Ray docs on load shedding](https://docs.ray.io/en/latest/serve/production-guide/best-practices.html#load-shedding).
