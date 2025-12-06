# Source: https://docs.vespa.ai/en/clients/http-best-practices.html.md

# HTTP Best Practices

 

## Always re-use connections

As connections to a JDisc container cluster are terminated at the individual container nodes, the cost of connection overhead will impact their serving capability. This is especially important for HTTPS/TLS as full TLS handshakes are expensive in terms of CPU cycles. A handshake also entails multiple network round-trips that certainly degrades request latency for new connections. A client instance should therefore re-use HTTPS connections if possible for subsequent requests.

Note that some client implementation may not re-use connections by default. For instance _Apache HttpClient (Java)_[will by default not re-use connections when configured with a client X.509 certificate](https://stackoverflow.com/a/13049131/1615280). Most programmatic clients require the response content to be fully consumed/read for a connection to be reused.

## Use multiple connections

Clients performing feed/query must use sufficient number of connections to spread the load evenly among all containers in a cluster. This is due to container clusters being served through a layer 4 load balancer (_Network Load Balancer_). Too few connections overall may result in an unbalanced workload, and some containers may not receive any traffic at all. This aspect is particular relevant for applications with large container clusters and/or few client instances.

## Be aware of server-initiated connection termination

Vespa Cloud will terminate idle connections after a timeout and active connections after a max age threshold is exceeded. The latter is performed gracefully through mechanisms in the HTTP protocol.

- _HTTP/1.1_: A `Connection: close` header is added to the response for the subsequent request received after timeout.
- _HTTP/2_: A `GOAWAY` frame with error code `NO_ERROR (0x0)` is returned for the subsequent request received after timeout. Be aware that some client implementation may not handle this scenario gracefully.

Both the idle timeout and max age threshold are aggressive to regularly rebalanced traffic. This ensures that new container nodes quickly receives traffic from existing client instances, for example when new resources are introduced by the [autoscaler](../operations/autoscaling.html).

To avoid connection termination issues, clients should either set the `Connection: close` header to explicitly close connections after each request, or configure client-side idle timeouts to **30 seconds or less**. Doing so proactively closes idle connections before the server does and helps prevent errors caused by server-initiated terminations.

## Prefer HTTP/2

We recommend _HTTP/2_ over _HTTP/1.1_. _HTTP/2_ multiplexes multiple concurrent requests over a single connection, and its binary protocol is more compact and efficient. See Vespa's documentation on [HTTP/2](../performance/http2.html) for more details.

## Be deliberate with timeouts and retries

Make sure to configure your clients with sensible timeouts and retry policies. Too low timeouts combined with aggressive retries may cause havoc on your Vespa application if latency increases due to overload.

Handle _transient failures_ and _partial failures_ through a retry strategy with backoff, for instance _capped exponential backoff_ with a random _jitter_. Consider implementing a [_circuit-breaker_](https://martinfowler.com/bliki/CircuitBreaker.html) for failures persisting over a longer time-span.

Only retry requests on _server errors_ - not on _client errors_. A client should typically not retry requests after receiving a `400 Bad Request` response, or retry a TLS connection after handshake fails with client's X.509 certificate being expired.

Be careful when handling 5xx responses, especially `503 Service Unavailable` and `504 Gateway Timeout`. These responses typically indicate an overloaded system, and blindly retrying without backoff will only worsen the situation. Clients should reduce overall throughput when receiving such responses.

The same principle applies to `429 Too Many Requests` responses from the [Document v1 API](../writing/document-v1-api-guide.html), which indicates that the client is exceeding the system's feed capacity. Clients should implement strategies such as reducing the request rate by a specific percentage, introducing exponential backoff, or pausing requests for a short duration before retrying. These adjustments help prevent further overload and allow the system to recover.

For more general advise on retries and timeouts see _Amazon Builder's Library_'s[excellent article](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) on the subject.

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [Always re-use connections](#always-re-use-connections)
- [Use multiple connections](#use-multiple-connections)
- [Be aware of server-initiated connection termination](#be-aware-of-server-initiated-connection-termination)
- [Prefer HTTP/2](#prefer-http2)
- [Be deliberate with timeouts and retries](#be-deliberate-with-timeouts-and-retries)

