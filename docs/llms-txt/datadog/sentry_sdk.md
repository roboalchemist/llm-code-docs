# Source: https://docs.datadoghq.com/error_tracking/guides/sentry_sdk.md

---
title: Sentry SDK
description: >-
  Start using Datadog Error Tracking today without changing your existing setup
  with the Sentry SDK
breadcrumbs: Docs > Error Tracking > Error Tracking Guides > Sentry SDK
---

# Sentry SDK

{% alert level="danger" %}
Using the Sentry SDK with Error Tracking helps you migrate to Datadog. However, to get the most out of Error Tracking, it is recommended to use the Datadog SDKs. See [Frontend Error Tracking](https://docs.datadoghq.com/error_tracking/frontend) and [Backend Error Tracking](https://docs.datadoghq.com/error_tracking/backend).
{% /alert %}

## Overview{% #overview %}

You can use [Sentry SDKs](https://docs.sentry.io/) to send your events to Datadog, so you can start using Error Tracking on existing applications that are instrumented using Sentry SDKs.

Setting up the Sentry SDK with Datadog requires a minimal code change to point the SDK to a Datadog Data Source Name (DSN).

[Events](https://develop.sentry.dev/sdk/data-model/envelope-items/#event) and non-error events (messages) appear in Datadog as logs in the [log explorer](https://app.datadoghq.com/logs). Other item types (traces, attachments, sessions, etc.) are not supported.

## Supported SDKs{% #supported-sdks %}

The following Sentry SDKs are verified to work with Error Tracking:

| Platform   | Tested version                                |
| ---------- | --------------------------------------------- |
| JavaScript | `@sentry/node@9.13.0``@sentry/browser@9.13.0` |
| Python     | `sentry-sdk==2.26.1`                          |
| Java       | `io.sentry:sentry:8.6.0`                      |
| .NET       | `Sentry 5.5.1`                                |
| Go         | `sentry-go v0.32.0`                           |
| Ruby       | `sentry-ruby 5.23.0`                          |

## Setup{% #setup %}

### Prerequisites{% #prerequisites %}

Sentry SDK events are sent into Datadog as logs. You must have [Error Tracking for Logs](https://app.datadoghq.com/error-tracking/settings) enabled for errors to show up in Error Tracking.

**Note:** By default, enabling Error Tracking for Logs enables Error Tracking on **all** of your logs. You can use [rules](https://docs.datadoghq.com/error_tracking/manage_data_collection#rules) to configure Error Tracking for Logs to **only** collect errors from the Sentry SDK. To do this, create a rule for logs with scope `source:sentry-sdk`, and create an exclusion rule for all other logs.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/sentry-sdk-rules.42b5d6a5b209ab642d0907ea66084559.png?auto=format"
   alt="Error Tracking rules including only Logs from the Sentry SDK" /%}

### Service configuration{% #service-configuration %}

To configure the Sentry SDK to send events into Datadog:

1. Configure a Datadog Data Source Name (DSN). Follow the [in-app instructions](https://app.datadoghq.com/error-tracking/settings/setup/sentry) to generate your unique DSN.
1. Set a `service` tag on all events. This is used to separate errors and is shown in the Datadog UI:

{% tab title="JavaScript" %}

```javascript
  Sentry.init({
      dsn: 'https://<TOKEN>@sentry-intake.<DD_SITE>/1',
      initialScope: {
          tags: {
              service: 'my-app'
          }
      }
  });
  
```

{% /tab %}

{% tab title="Python" %}

```python
  sentry_sdk.init(
      dsn="https://<TOKEN>@sentry-intake.<DD_SITE>/1",
  )
  sentry_sdk.set_tag("service", "my-app")
  
```

{% /tab %}

{% tab title="Java" %}

```java
  Sentry.init(options -> {
      options.setDsn("https://<TOKEN>@sentry-intake.<DD_SITE>/1");
  });
  Sentry.configureScope(scope -> {
      scope.setTag("service", "my-app");
  });
  
```

{% /tab %}

{% tab title="C#" %}

```csharp
  SentrySdk.Init(options =>
  {
      options.Dsn = "https://<TOKEN>@sentry-intake.<DD_SITE>/1";
      options.SetBeforeSend((sentryEvent, hint) => {
          sentryEvent.SetTag("service", "my-app");
          return sentryEvent;
      });
  });
  
```

{% /tab %}

{% tab title="Go" %}

```go
  sentry.Init(sentry.ClientOptions{
      Dsn: "https://<TOKEN>@sentry-intake.<DD_SITE>/1",
  })
  sentry.ConfigureScope(func(scope *sentry.Scope) {
      scope.SetTag("service", "my-app");
  })
  
```

{% /tab %}

{% tab title="Ruby" %}

```ruby
  Sentry.init do |config|
      config.dsn = https://<TOKEN>@sentry-intake.<DD_SITE>/1'
  end
  Sentry.set_tags('service': 'my-app')
  
```

{% /tab %}

### Upload JavaScript source maps{% #upload-javascript-source-maps %}

If your frontend JavaScript source code is minified, you can upload source maps to Datadog to deobfuscate stack traces in Error Tracking. See [Upload JavaScript Source Maps](https://docs.datadoghq.com/real_user_monitoring/guide/upload-javascript-source-maps).

The `version` on source maps is matched with the `release` [configured](https://docs.sentry.io/product/releases/setup/) on the Sentry SDK.

### Source code integration{% #source-code-integration %}

[Datadog Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/) allows you to connect your telemetry with your Git repositories. It works with Sentry SDKs by configuring telemetry tags:

{% tab title="JavaScript" %}

```javascript
Sentry.setTag("git.commit.sha", "<commitSha>");
Sentry.setTag("git.repository_url", "<git-provider.example/me/my-repo>");
```

{% /tab %}

{% tab title="Python" %}

```python
sentry_sdk.set_tag("git.commit.sha", "<commitSha>")
sentry_sdk.set_tag("git.repository_url", "<git-provider.example/me/my-repo>")
```

{% /tab %}

{% tab title="Java" %}

```java
Sentry.configureScope(scope -> {
    scope.setTag("git.commit.sha", "<commitSha>");
    scope.setTag("git.repository_url", "<git-provider.example/me/my-repo>");
});
```

{% /tab %}

{% tab title="C#" %}

```csharp
SentrySdk.ConfigureScope(scope =>
{
    scope.SetTag("git.commit.sha", "<commitSha>");
    scope.SetTag("git.repository_url", "<git-provider.example/me/my-repo>");
});
```

{% /tab %}

{% tab title="Go" %}

```go
sentry.ConfigureScope(func(scope *sentry.Scope) {
    scope.SetTag("git.commit.sha", "<commitSha>");
    scope.SetTag("git.repository_url", "<git-provider.example/me/my-repo>");
})
```

{% /tab %}

{% tab title="Ruby" %}

```ruby
Sentry.set_tags('git.commit.sha', '<commitSha>')
Sentry.set_tags('git.repository_url', '<git-provider.example/me/my-repo>')
```

{% /tab %}

## Migrate to the recommended setup{% #migrate-to-the-recommended-setup %}

To get the most out of Error Tracking, Datadog recommends migrating to the Datadog SDK and/or Agent-based setups. See [Backend Error Tracking](https://docs.datadoghq.com/error_tracking/backend) and [Frontend Error Tracking](https://docs.datadoghq.com/error_tracking/frontend) for more information.

The Sentry SDK setup can be used simultaneously with the recommended setup. Errors may be reported twice.

## Send events to both Sentry and Datadog{% #send-events-to-both-sentry-and-datadog %}

Events can be sent to both Sentry (or any other Sentry-compatible backend) and Datadog. This allows you to start using Datadog while also keeping your current solution. There are a couple of ways to achieve this:

- Using the Sentry SDK
- Using Sentry Mirror

### Using the Sentry SDK{% #using-the-sentry-sdk %}

You can configure Sentry SDKs to send events to multiple DSNs at once. On most Sentry SDKs, you can override the default transport to achieve this.

{% tab title="JavaScript" %}

```javascript
// Change to import from "@sentry/react", "@sentry/nextjs", etc. as needed
import * as Sentry from "@sentry/browser";
import { makeFetchTransport } from "@sentry/browser"; // import { makeNodeTransport } from "@sentry/node" for Node.js
import { makeMultiplexedTransport } from "@sentry/core";

const sentryDsn = '<SENTRY_DSN>';
const datadogDsn = '<DATADOG_DSN>';

Sentry.init({
  dsn: sentryDsn,
  transport: makeMultiplexedTransport(makeFetchTransport, () => [sentryDsn, datadogDsn]),
  // ...
});
Sentry.setTag('service', 'my-app');
```

{% /tab %}

{% tab title="Python" %}

1. Copy the following function into your code:

```python
from sentry_sdk.transport import Transport, make_transport
def make_multi_transport(dsns):
    class MultiTransport(Transport):
        def __init__(self, options):
            super().__init__(options)
            self.transports = [
                make_transport({**options, "dsn": dsn, "transport": None}) for dsn in dsns
            ]
        def capture_envelope(self, *args, **kwargs):
            for transport in self.transports:
                transport.capture_envelope(*args, **kwargs)
        def flush(self, *args, **kwargs):
            for transport in self.transports:
                transport.flush(*args, **kwargs)
        def kill(self):
            for transport in self.transports:
                transport.kill()
        def record_lost_event(self, *args, **kwargs):
            for transport in self.transports:
                transport.record_lost_event(*args, **kwargs)
    return MultiTransport
```
Use as follows:
```python
_SENTRY_DSN = "<SENTRY_DSN>"
_DATADOG_DSN = "<DATADOG_DSN>"
sentry_sdk.init(
    dsn=_SENTRY_DSN,
    transport=make_multi_transport([_SENTRY_DSN, _DATADOG_DSN]),
    # ...
)
sentry_sdk.set_tag("service", "my-app")
```

{% /tab %}

{% tab title="Java" %}

1. Copy the following class into your code. Make sure to define it in the **io.sentry** package.

```java
package io.sentry;

public record MultiTransportFactory(List<String> dsns) implements ITransportFactory {
  @Override
  public ITransport create(final SentryOptions options, final RequestDetails requestDetails) {
    final var transports = dsns.stream()
        .map(dsn -> {
          var requestOptions = new SentryOptions();
          requestOptions.setDsn(dsn);
          requestOptions.setSentryClientName(options.getSentryClientName());
          return new AsyncHttpTransportFactory().
              create(options, new RequestDetailsResolver(requestOptions).resolve());
        })
        .toList();
    return new ITransport() {
      @Override
      public void send(SentryEnvelope envelope, Hint hint) throws IOException {
        for (ITransport transport : transports) {
          transport.send(envelope, hint);
        }
      }

      @Override
      public boolean isHealthy() {
        return transports.stream().allMatch(ITransport::isHealthy);
      }

      @Override
      public void flush(long timeoutMillis) {
        transports.forEach(transport -> transport.flush(timeoutMillis));
      }

      @Override
      public RateLimiter getRateLimiter() {
        return null;
      }

      @Override
      public void close(boolean isRestarting) throws IOException {
        for (ITransport transport : transports) {
          transport.close(isRestarting);
        }
      }

      @Override
      public void close() throws IOException {
        for (ITransport transport : transports) {
          transport.close();
        }
      }
    };
  }
}
```
Use as follows:
```java
final var sentryDsn = "<SENTRY_DSN>"
final var datadogDsn = "<DATADOG_DSN>"

Sentry.init(options -> {
  options.setDsn(sentryDsn);
  options.setTransportFactory(new MultiTransportFactory(List.of(sentryDsn, datadogDsn)));
});
Sentry.setTag("service", "my-app");
```

{% /tab %}

{% tab title="Go" %}

1. Copy the following snippet into your code:

```go
type MultiTransport struct {
	dsns       []string
	transports []*sentry.HTTPTransport
}

func NewMultiTransport(dsns []string) *MultiTransport {
	transports := make([]*sentry.HTTPTransport, len(dsns))
	for i := range dsns {
		transports[i] = sentry.NewHTTPTransport()
	}
	return &MultiTransport{
		dsns:       dsns,
		transports: transports,
	}
}

func (mt *MultiTransport) Configure(options sentry.ClientOptions) {
	for i := range mt.dsns {
		options.Dsn = mt.dsns[i]
		if options.EnableTracing {
			// Replicating the default behavior:
			// https://github.com/getsentry/sentry-go/blob/v0.32.0/client.go#L358
			mt.transports[i].BufferSize = 1000
		}
		mt.transports[i].Configure(options)
	}
}

func (mt *MultiTransport) Flush(timeout time.Duration) bool {
	allDone := true
	for _, t := range mt.transports {
		if ok := t.Flush(timeout); !ok {
			allDone = false
		}
	}
	return allDone
}

func (mt *MultiTransport) SendEvent(event *sentry.Event) {
	for _, t := range mt.transports {
		t.SendEvent(event)
	}
}

func (mt *MultiTransport) Close() {
	for _, t := range mt.transports {
		t.Close()
	}
}
```
Use as follows:
```go
sentryDSN := "<SENTRY_DSN>"
datadogDSN := "<DATADOG_DSN>"

err := sentry.Init(sentry.ClientOptions{
	Dsn: sentryDSN,
	Transport: NewMultiTransport([]string{sentryDSN, datadogDSN}),
})
// ...
sentry.ConfigureScope(func(scope *sentry.Scope) {
	scope.SetTag("service", "my-app")
})
```

{% /tab %}

### Using Sentry Mirror{% #using-sentry-mirror %}

[Sentry Mirror](https://github.com/getsentry/sentry-mirror) is a proxy that replicates traffic to multiple DSNs. You run in it your own environment, and point your applications to Sentry Mirror's inbound DSN.

Sentry Mirror is configured using a YAML file:

```yaml
ip: 0.0.0.0
port: 3000
keys:
  - inbound: http://1234567890abcdef1234567890abcdef@my-domain.example/123
    outbound:
      - <SENTRY_DSN>
      - <DATADOG_DSN>
```



## Further Reading{% #further-reading %}

- [Manage Data Collection](https://docs.datadoghq.com/error_tracking/manage_data_collection)
