# Source: https://fly.io/docs/monitoring/error-codes/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Error codes and troubleshooting 

The Fly.io platform logs errors to customer log streams. Each log line contains an error code and a field containing that code. This page gives more context about the errors and how to troubleshoot them.

## [](#proxy-errors)[Proxy errors] 

The Fly proxy issues different categories of errors, identifiable by the second letter in each code, referring to: Upstream, Connection, TLS, Machine, App, Edge and Routing errors.

### [](#internal-errors)[Internal Errors] 

These errors are internal to the Fly proxy. They're not related to your application behavior.

#### [](#pp01-failed-to-set-tcp-socket-options)[PP01: Failed to set TCP socket options] 

The proxy wasn't able to set TCP socket options. This is an internal Fly.io error.

### [](#upstream-proxy-errors)[Upstream Proxy errors] 

Upstream errors occur when the proxy fails to send or complete a request to one of your upstream application machines.

#### [](#pu01-failed-http-2-handshake)[PU01: Failed HTTP/2 handshake] 

In the case that your app accepts h2c requests, `PU01` errors indicate that the HTTP/2 handshake to one of your machines failed. This error is not relevant to applications accepting only HTTP/1 connections.

#### [](#pu02-failed-to-complete-http-request-to-instance)[PU02: Failed to complete HTTP request to instance] 

An HTTP request to a machine was started, but could not be completed.

#### [](#pu03-unreachable-worker-host)[PU03: Unreachable worker host] 

The underlying host where a machine lives became unreachable. This is an internal Fly.io error unrelated to your application.

#### [](#pu04-could-not-build-http-request)[PU04: Could not build HTTP request] 

It wasn't possible to create an HTTP request, for unknown reasons.

#### [](#pc01-machine-refused-connection-on-port)[PC01: Machine refused connection on port] 

A request was sent to a specific port that isn't open on the target machine.

Is your app listening on the correct port?

Is your app listening on `0.0.0.0` or `::`? Make sure it's not listening on `127.0.0.1`. Check your app startup logs. Servers often print the address they're listening on.

#### [](#pc02-connection-refused)[PC02: Connection refused] 

A request was sent to an unspecified port that isn't open on the target machine.

Is your app listening on `0.0.0.0` or `::`? Make sure it's not listening on `127.0.0.1`. Check your app startup logs. Servers often print the address they're listening on.

#### [](#pc03-connection-reset)[PC03: Connection reset] 

This indicates a problem with your application resetting a TCP connection prematurely. Check your application logs for possible causes.

#### [](#pc04-connection-aborted)[PC04: Connection aborted] 

This indicates a problem with your application aborting a TCP connection prematurely. Check your application logs for possible causes.

#### [](#pc05-connection-timed-out)[PC05: Connection timed out] 

This indicates a problem with connections timing out to your application. Check the following to diagnose:

-   Application logs may indicate the cause of a timeout
-   Ensure your app isn't overloaded by properly set its [concurrency limits](https://fly.io/docs/reference/concurrency/#main-content-start)
-   Check [application metrics](/docs/monitoring/metrics/#managed-grafana) for signs of resource exhaustion (CPU, memory, disk I/O)

#### [](#pc06-unidentified-i-o-error)[PC06: Unidentified I/O error] 

A connection to a machine experienced an unidentifiable I/O error.

#### [](#pc07-connection-retries-exhausted)[PC07: Connection retries exhausted] 

The proxy failed to connect to a machine after too many retries.

#### [](#pc08-tcp-timeout-couldnt-be-set)[PC08: TCP timeout couldn't be set] 

Failed to set the TCP timeout for an upstream connection. This is an internal Fly.io issue.

### [](#tls-errors)[TLS errors] 

TLS errors are related to the automatic TLS termination provided by Fly Proxy. These errors occur before a request is passed on to your application.

#### [](#pt01-exceeded-tls-handshake-rate-limit)[PT01: Exceeded TLS handshake rate limit] 

A specific IP range exceeded the rate limit for TLS handshake attempts.

#### [](#pt02-exceeded-rate-limit-for-sni)[PT02: Exceeded rate limit for SNI] 

TLS handshake requests to a specific SNI exceeded the rate limit.

#### [](#pt03-tls-handshake-canceled)[PT03: TLS handshake canceled] 

A TLS handshake was canceled prematurely.

#### [](#pt04-tls-handshake-failed)[PT04: TLS handshake failed] 

A TLS handshake failed.

#### [](#pt05-no-valid-tls-certificate-for-sni)[PT05: No valid TLS certificate for SNI] 

No TLS certificate was found for a specific server name, and the connection was aborted.

#### [](#pt06-no-valid-tls-certificate)[PT06: No valid TLS certificate] 

No TLS certificate was found for the connection, and the connection was aborted.

#### [](#pt07-tls-handshake-i-o-error)[PT07: TLS handshake I/O error] 

A TLS handshake failed due to an unspecified I/O error.

#### [](#pt08-tls-handshake-timed-out)[PT08: TLS handshake timed out] 

A TLS handshake timed out.

#### [](#pt09-internal-tls-error)[PT09: Internal TLS error] 

An internal TLS error occurred.

### [](#machine-related-errors)[Machine-related errors] 

This class of errors relates to how the proxy behaves when starting and stopping machines on request.

#### [](#pm01-machines-api-error)[PM01: Machines API error] 

The Machines API returned an error. If the underlying error is known, it's displayed.

#### [](#pm02-machine-wake-internal-error)[PM02: Machine wake internal error] 

An internal Fly.io error prevented a machine transitioning from a `stopped` to `started` state.

#### [](#pm03-machine-wake-timeout)[PM03: Machine wake timeout] 

The API request to transition a machine from a `stopped` to `started` state timed out.

#### [](#pm04-machine-wake-parsing-error)[PM04: Machine wake parsing error] 

A request parsing error prevented a machine transitioning from a `stopped` to `started` state.

#### [](#pm05-machine-connection-failed)[PM05: Machine connection failed] 

The proxy failed to connect to a machine. If the underlying error is known, it's displayed.

#### [](#pm06-missing-app-name)[PM06: Missing app name] 

The Machines API requires an app name to operate on an individual machine. That app name wasn't specified.

#### [](#pm07-machine-state-change-failed)[PM07: Machine state change failed] 

The proxy wasn't able to stop or start a machine. If the underlying error is known, it's displayed.

#### [](#pm08-non-startable-machine-state)[PM08: Non-startable machine state] 

A machine could not be started since due to its current non-startable state, such as `stopping` or `destroyed`. The state is displayed along with this message.

#### [](#pm09-unknown-machine-state)[PM09: Unknown machine state] 

The proxy doesn't recognize the machine's current state.

#### [](#pm10-machine-start-canceled)[PM10: Machine start canceled] 

A machine start was canceled prematurely due to an internal Fly.io problem.

#### [](#pm11-machine-recently-stopped)[PM11: Machine recently stopped] 

Machine states are broadcast to the Fly proxies in an eventually consistent manner. So, edge proxies may not have an up-to-date picture about machine states. A machine that appears as `started` to the edge proxy may actually have been recently stopped.

If the edge proxy forwards a request to a recently stopped machine, and there are other machines available to handle the request, the `PM11` error will be returned to the edge proxy. The error informs the proxy about the `stopped` state of the machine, and instructs the edge to forward the request to another machine.

If the edge proxy believes there's only one machine that can service the request, this logic is bypassed. The request is forwarded to the machine even if it was stopped recently.

The current threshold for 'recently stopped' is 5 minutes.

#### [](#pa01-replay-retry-buffer-exceeded)[PA01: Replay/retry buffer exceeded] 

To prepare for the possibility of receiving [`fly-replay` response header](https://fly.io/docs/networking/dynamic-request-routing/#the-fly-replay-response-header), or for retrying failed requests, Fly edge proxies buffer requests up to 10MB.

If a request grows larger than 10MB, buffering stops, making it impossible to replay or retry the request. When this happens, `PA01` is emitted.

#### [](#pa02-excess-fly-replay-headers)[PA02: Excess fly-replay headers] 

After a ['fly-replay' response header](https://fly.io/docs/networking/dynamic-request-routing/#the-fly-replay-response-header) replays a request, the application may respond normally, or it may issue another `fly-replay`, up to 10 times. `PA02` is emitted when `fly-replay` is returned more than 10 times.

#### [](#pa03-invalid-fly-replay)[PA03: Invalid fly-replay] 

Your app returned an invalid ['fly-replay' response](https://fly.io/docs/networking/dynamic-request-routing/#the-fly-replay-response-header).

#### [](#pa04-replay-target-app-not-found)[PA04: Replay target app not found] 

Your app returned a ['fly-replay' response header](https://fly.io/docs/networking/dynamic-request-routing/#the-fly-replay-response-header) targeting a non-existent application in the `app` parameter.

#### [](#pa05-unauthorized-replay-target-app)[PA05: Unauthorized replay target app] 

Your app returned a ['fly-replay' response header](https://fly.io/docs/networking/dynamic-request-routing/#the-fly-replay-response-header) targeting an application belonging to a different Fly.io organization. Only apps in the same organization may replay requests to each other.

### [](#edge-proxy-errors)[Edge proxy errors] 

This category of errors refers to internal Fly.io errors happening only on edge proxies.

#### [](#pe01-replay-source-app-not-found)[PE01: Replay source app not found] 

An internal error occurred while using `fly-replay` related to the source app name.

#### [](#pe02-replay-source-organization-not-found)[PE02: Replay source organization not found] 

An internal error occurred while using `fly-replay` related to the source organization.

### [](#routing-errors)[Routing errors] 

This category refers to request routing errors between proxies and applications.

#### [](#pr01-no-healthy-machines)[PR01: No healthy machines] 

No healthy machines were found to forward a request to. This error is most common in non-HTTP TCP services. The reasons could be:

**Exhausting restart retries due to boot errors**

Your app machines may all be stopped due to boot errors exhausting the number of restart retries. Check your app logs and `fly status`.

**Deployments with volumes are failing**

If your app uses volumes and your rolling deployment is failing, you might encounter this error. Check your app logs and `fly status`.

**Using the `immediate` deploy strategy**

If you use the `immediate` deploy strategy, all current machines will be replaced at once, possibly leading to downtime and some `PR01` errors.

**App concurrency limits reached**

[Concurrency limits](/docs/reference/concurrency/) set in `fly.toml` define how traffic should be balanced across machines in your app.

To diagnose, check if:

-   your app is using too much CPU, memory or disk I/O
-   your app applies its own concurrency limits
-   Connection pools to external services like databases are exhausted
-   Connections to external services from your app are slow

#### [](#pr02-machine-not-found)[PR02: Machine not found] 

The Fly proxy couldn't find a specific machine ID after the request was forwarded from an edge proxy. The VM was likely shut down between when the proxy received the request and when it got forwarded. This error is most common during [`bluegreen` deployments](https://fly.io/docs/reference/configuration/#picking-a-deployment-strategy).

#### [](#pr03-no-candidate-machines-found-after-retries)[PR03: No candidate machines found after retries] 

This error is functionally similar to `PR01`. It only applies to HTTP services however, and up to 90 retries are attempted before the proxy gives up and issues this error. This error should also display the cause of the most recent error before this one.

#### [](#pr04-no-candidate-machines-found-after-retries)[PR04: No candidate machines found after retries] 

This error is functionally similar to `PR03`, except it will not display previous errors.

#### [](#pr05-statics-retrieval-failed)[PR05: Statics retrieval failed] 

The proxy failed to retrieve a static file from the specified Tigris storage bucket.

#### [](#pl01-bypassed-connection-concurrency-limit)[PL01: Bypassed connection concurrency limit] 

[Concurrency limits](https://fly.io/docs/reference/concurrency/#main-content-start) set in `fly.toml` define how traffic should be balanced across machines in your app.

This error occurs when concurrency is measured as the number of concurrent **connections**.

To diagnose, check if:

-   your app is using too much CPU, memory or disk I/O
-   your app applies its own concurrency limits
-   Connection pools to external services like databases are exhausted
-   Connections to external services from your app are slow

#### [](#pl02-bypassed-request-concurrency-limit)[PL02: Bypassed request concurrency limit] 

This error is similar to `PL01`, but refers to concurrency measured as the number of concurrent **requests**.

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fmonitoring%2Ferror-codes.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Error+codes+and+troubleshooting%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fmonitoring%2Ferror-codes%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fmonitoring%2Ferror-codes.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Error+codes+and+troubleshooting%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/monitoring/error-codes.html.md)