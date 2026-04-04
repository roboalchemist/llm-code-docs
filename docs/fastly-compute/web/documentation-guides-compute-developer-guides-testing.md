# Source: https://www.fastly.com/documentation/guides/compute/developer-guides/testing/

Title: Testing and debugging on the Compute platform | Fastly Documentation

URL Source: https://www.fastly.com/documentation/guides/compute/developer-guides/testing/

Markdown Content:

1. [Home](https://www.fastly.com/documentation/)
2. [Guides](https://www.fastly.com/documentation/guides/)
3. [Compute](https://www.fastly.com/documentation/guides/compute/)
4. [Developer guides](https://www.fastly.com/documentation/guides/compute/developer-guides/)

When building for the Compute platform, you have several options to test and debug your application:

* **Deploy to a live service**: If you need the full functionality of the Compute platform, you can deploy to a Fastly-hosted service and [monitor logs in your console](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#live-log-monitoring-in-your-console).
* **Run a local test server**: If you need to develop rapidly or work offline, you can run your application with the [local testing server](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#running-a-local-testing-server).
* **Use [Fastly Fiddle](https://fiddle.fastly.dev/)**: If you are prototyping your application or experimenting with Fastly Compute, you can use Fiddle to create ephemeral Fastly services, and write [test assertions](https://www.fastly.com/documentation/reference/tools/fiddle/testing/) against their instrumentation data.

**HINT:** Regardless of which method you use, you'll probably want to create log data from the program to provide visibility into what's going on. For information about how to log and what to log, see the usage guide to your chosen language, e.g. [using Rust](https://www.fastly.com/documentation/guides/compute/developer-guides/rust).

[](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#live-log-monitoring-in-your-console)Live log monitoring in your console
--------------------------------------------------------------------------------------------------------------------------------------------------------

During development it can be helpful to deploy your application to the Compute platform using [fastly compute deploy](https://www.fastly.com/documentation/reference/cli/compute/deploy/) and interact with it using a `*.edgecompute.app` domain (or other testing domain that you attach to the service). To make debugging easier, the [Fastly CLI](https://www.fastly.com/documentation/reference/tools/cli) also provides a [fastly log-tail](https://www.fastly.com/documentation/reference/cli/log-tail/) command that allows you to watch your service's `stdio` output from your local console.

Any output sent to `stdout` and `stderr` will be forwarded to your console, along with runtime errors encountered by the application. To see log tailing in action, add some `println!` statements to the [default starter kit for Rust](https://www.fastly.com/documentation/solutions/starters/compute-starter-kit-rust-default/):

`use fastly::http::StatusCode;use fastly::{mime, Error, Request, Response};#[fastly::main]fn main(req: Request) -> Result<Response, Error> {    // Log request path to stdout.    println!("Request received for path {}", req.get_path());    Ok(Response::from_status(StatusCode::OK)        .with_content_type(mime::TEXT_HTML_UTF_8)        .with_body("<iframe src='https://developer.fastly.com/compute-welcome' style='border:0; position: absolute; top: 0; left: 0; width: 100%; height: 100%'></iframe>\n")    )}`

Build and deploy the application with [fastly compute publish](https://www.fastly.com/documentation/reference/cli/compute/publish/), then run [fastly log-tail](https://www.fastly.com/documentation/reference/cli/log-tail/) to see log output from the live service streaming into your console:

`$ fastly log-tailINFO: Managed logging enabled on service PS1Z4isxPaoZGVKVdv0eYstdout | d81ad0e4 | Request received for path /stdout | f00dfcda | Request received for path /favicon.ico`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#constraints-and-limitations)Constraints and limitations

The following limits apply to the use of log tailing:

| Item | Limit | Scope |
| --- | --- | --- |
| Maximum STDIO ingestion rate for [log tailing](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#live-log-monitoring-in-your-console) | 20KB/s | per service |
| High watermark: when the amount of data buffered exceeds this, older data is deleted | 10MB | per service |
| Low watermark: when the high watermark is reached, data is deleted until the amount buffered is no more than this | 8MB | per service |

Other limitations apply to [logging in general](https://www.fastly.com/documentation/guides/integrations/non-fastly-services/developer-guide-logging).

[](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#using-log-endpoints)Using log endpoints
------------------------------------------------------------------------------------------------------------------------

Data sent to [named log endpoints](https://www.fastly.com/documentation/guides/integrations/non-fastly-services/developer-guide-logging) is not included in [log tailing](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#live-log-monitoring-in-your-console) output. In production, the best way to get logs out of your application is with one of our many [logging integrations](https://www.fastly.com/documentation/guides/integrations/non-fastly-services/developer-guide-logging), which support batching and high volumes as part of the Real Time Logging feature.

**HINT:** If you don't have a log destination set up, you can view your logs right here on this page by creating an [HTTP log endpoint](https://www.fastly.com/documentation/guides/integrations/non-fastly-services/developer-guide-logging#generic-log-endpoints) with the address set to the URL shown below:

Log viewer https://log-bin.fastly.dev/WXT3RHYC56

Awaiting log data...

If you wish to retain the capability to debug your service using log tailing once it is serving production traffic, it's important that you do not log on every request, since you may generate more output than can be practically streamed to your local machine (see [constraints and limitations](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#constraints-and-limitations)). Consider switching the log destination based on a simple request flag such as a cookie:

`use fastly::http::StatusCode;use fastly::{mime, Error, Request, Response};#[fastly::main]fn main(req: Request) -> Result<Response, Error> {    log_fastly::init_simple("my_endpoint_name", log::LevelFilter::Warn);    if let Some(cookie_val) = req.get_header("Cookie") {        if cookie_val.to_str().unwrap_or("").contains("key=some-secret") {            println!("This will go to stdout and be available for log tailing");        }    }    log::warn!("This will be written to the log endpoint...");    Ok(Response::from_status(StatusCode::OK)        .with_content_type(mime::TEXT_HTML_UTF_8)        .with_body("<iframe src='https://developer.fastly.com/compute-welcome' style='border:0; position: absolute; top: 0; left: 0; width: 100%; height: 100%'></iframe>\n")    )}`

[](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#running-a-local-testing-server)Running a local testing server
----------------------------------------------------------------------------------------------------------------------------------------------

With the [fastly compute serve](https://www.fastly.com/documentation/reference/cli/compute/serve/) command, you can run a local development server that behaves like the Fastly platform. Much like a Fastly [service](https://www.fastly.com/documentation/reference/glossary#term-service), the development server can be configured with backends.

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#features)Features

See the [local testing](https://www.fastly.com/documentation/reference/compute/fastly-toml/#local-server) section of the [fastly.toml reference](https://www.fastly.com/documentation/reference/compute/fastly-toml) for all of the available configuration parameters. The following compute platform features are emulated in the local development server:

| Platform features | Available in local server | Notes |
| --- | --- | --- |
| [Access control stores](https://www.fastly.com/documentation/guides/concepts/dynamic-config#access-control-stores) | ✅ |  |
| [Geolocation](https://www.fastly.com/documentation/guides/concepts/geolocation/) | ✅ | Returns data as configured in fastly.toml or default data for 127.0.0.1. |
| [Auto decompression](https://www.fastly.com/documentation/guides/concepts/compression/) | ✅ |  |
| [Dynamic compression](https://www.fastly.com/documentation/guides/concepts/compression/) | ❌ |  |
| [Environment variables](https://www.fastly.com/documentation/reference/compute/ecp-env/) | ✅ | The following are defined: `FASTLY_HOSTNAME` is always set to "localhost"; `FASTLY_TRACE_ID` is an number starting from 0 and incrementing with each incoming request. Other compute environment variables are not defined in the local server. |
| [Readthrough (HTTP) cache](https://www.fastly.com/documentation/guides/concepts/cache/#readthrough-cache) | API only | The local server does not support the readthrough cache; data passes through to the origin on every request. |
| Readthrough (HTTP) cache - [Caching controls](https://www.fastly.com/documentation/guides/concepts/cache/#controlling-cache-behavior) | ❌ | Caching controls are ineffective because the local server does not have a readthrough cache. |
| Readthrough (HTTP) cache - [Customizing cache behavior](https://www.fastly.com/documentation/guides/concepts/cache/#customizing-cache-interaction-with-the-backend) | ❌ | Setting a [before-send](https://www.fastly.com/documentation/guides/concepts/cache/#modifying-a-request-as-it-is-forwarded-to-a-backend) or [after-send](https://www.fastly.com/documentation/guides/concepts/cache/#controlling-cache-behavior-based-on-backend-response) callback may result in a `HTTP caching API is not enabled.` error. |
| [Core cache](https://www.fastly.com/documentation/guides/concepts/cache/#core-cache) | ✅ | The "replace" family of calls are not supported. |
| [Simple cache](https://www.fastly.com/documentation/guides/concepts/cache/#simple-cache) | ✅ |  |
| [Purging](https://www.fastly.com/documentation/guides/concepts/cache/purging) | ✅ | Purging is supported for the core cache. |
| [Real time logging](https://www.fastly.com/documentation/guides/integrations/non-fastly-services/developer-guide-logging/) | ✅ |  |
| [KV stores](https://www.fastly.com/documentation/guides/compute/edge-data-storage/about-edge-data-stores) | ✅ |  |
| [Config stores](https://www.fastly.com/documentation/guides/concepts/dynamic-config) | ✅ |  |
| [Secret stores](https://www.fastly.com/documentation/guides/concepts/dynamic-config) | ✅ | No local encryption supported |
| [Edge rate limiting](https://www.fastly.com/documentation/guides/concepts/rate-limiting/) | ✅ | Load testing is not supported – all requests appear as if they are the first |
| [Fanout](https://www.fastly.com/documentation/guides/concepts/real-time-messaging/fanout/) | ✅ | Details can be found in our [Local Testing](https://www.fastly.com/documentation/guides/concepts/real-time-messaging/fanout/#local-testing) docs for Fanout |
| [WebSockets passthrough](https://www.fastly.com/documentation/guides/concepts/real-time-messaging/websockets-tunnel/) | ❌ |  |
| [Dynamic backends](https://www.fastly.com/documentation/guides/integrations/non-fastly-services/developer-guide-backends/#dynamic-backends) | ✅ | Connection timing is not supported |
| [Backend Health](https://www.fastly.com/documentation/guides/concepts/healthcheck/) | ❌ | Will always return an `unknown` |
| [HTTP 103 Early Hints](https://docs.rs/fastly/latest/fastly/struct.Response.html#method.send_to_client) | ❌ | Responses with the 103 status code will be logged but not returned to clients. |

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#starting-the-server)Starting the server

Once you have defined your resources in the `fastly.toml` file, run [fastly compute serve](https://www.fastly.com/documentation/reference/cli/compute/serve/) to start the testing server:

`$ fastly compute serve✓ Initializing...✓ Verifying package manifest...✓ Verifying local rust toolchain...✓ Building package using rust toolchain...✓ Creating package archive...SUCCESS: Built rust package carpet-room (pkg/carpet-room.tar.gz)✓ Initializing...✓ Checking latest Viceroy release...✓ Checking installed Viceroy version...✓ Running local server...Jul 16 12:51:52.346  INFO checking if backend 'example_backend' is upJul 16 12:51:52.546  INFO backend 'example_backend' is upJul 16 12:51:52.546  INFO Listening on http://127.0.0.1:7676`

Open a web browser and go to [http://127.0.0.1:7676](http://127.0.0.1:7676/) to see your Compute application served by your own machine. Check the console to see both stdio and log endpoint output from your application.

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#detecting-whether-code-is-running-under-a-local-environment)Detecting whether code is running under a local environment

In the local server, the value of `FASTLY_HOSTNAME` is always "localhost", which can be used to determine that your code is executing locally rather than on the live Compute platform.

1. Rust

`let LOCAL = std::env::var("FASTLY_HOSTNAME").unwrap() == "localhost";if LOCAL {    println!("I'm testing locally");}`

### [](https://www.fastly.com/documentation/guides/compute/developer-guides/testing/#constraints-and-limitations-1)Constraints and limitations

The local server is developed and maintained in parallel to our compute platform, and while it is not intended to be a perfect replica of the Fastly platform, features are regularly added to allow testing as much of the functionality of a Compute program as possible. The [Fastly CLI](https://www.fastly.com/documentation/reference/tools/cli) will keep your local server instance up to date automatically as new features become available.

The following limitations apply to the current version of the local server:

* There is no readthrough cache, so backend responses that would ordinarily be cacheable, will not be stored.
* Data written to named log endpoints will not be routed to those endpoints but instead will be emitted to `stdout`, along with any output generated by code that prints to stdio directly.
* Requests made to the local server do not transit Fastly's routing infrastructure and as a result differ in a few ways:
  * Requests that would normally be rejected, for example for exceeding our platform limit on URL length, may instead reach your code.
  * Outbound response filters triggered by headers, such as `X-Compress-Hint`, are not available.

* Requests made from the local server to backends also differ as a result of not transiting Fastly's routing infrastructure:
  * Additional headers normally appended by Fastly such as `CDN-Loop`, `Fastly-FF` and `X-Varnish` are not added

* TLS information about the client connection is not available.
* Most [Compute environment variables](https://www.fastly.com/documentation/reference/compute/ecp-env/) are not available. The following are defined:
  * `FASTLY_HOSTNAME`: Always set to "localhost"
  * `FASTLY_TRACE_ID`: An ID starting from 0 and incrementing with each incoming request, providing each instance with its own unique ID
