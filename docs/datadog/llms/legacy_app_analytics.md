# Source: https://docs.datadoghq.com/tracing/legacy_app_analytics.md

---
title: App Analytics
description: >-
  Documentation for deprecated App Analytics features with configuration
  information for legacy setups and migration guidance to new ingestion
  controls.
breadcrumbs: Docs > APM > App Analytics
---

# App Analytics

{% alert level="warning" %}
This page describes deprecated features with configuration information relevant to legacy App Analytics, useful for troubleshooting or modifying some old setups. To have full control over your traces, use [ingestion controls and retention filters](https://docs.datadoghq.com/tracing/trace_pipeline) instead.
{% /alert %}

## Migrate to the new configuration options{% #migrate-to-the-new-configuration-options %}

Navigate to the [ingestion control page](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/) to see services with legacy configurations. These are flagged with a `Legacy Setup` status.

To migrate to the new configuration options, remove all legacy App Analytics configuration options from the services flagged with `Legacy Setup`. Then, implement the Datadog Agent and tracing libraries' [sampling mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/) to send traces.

## App Analytics setup{% #app-analytics-setup %}

App Analytics configuration options are located in the Tracing Libraries and in the Datadog Agent. In the libraries, analytics spans from your services are generated either automatically or manually.

### In Tracing Libraries{% #in-tracing-libraries %}

#### Automatic configuration{% #automatic-configuration %}

{% tab title="Java" %}
App Analytics is available starting in version 0.25.0 of the Java tracing client. It can be enabled globally for all **web server** integrations with one configuration parameter in the Tracing client:

- System Property: `-Ddd.trace.analytics.enabled=true`
- Environment Variable: `DD_TRACE_ANALYTICS_ENABLED=true`

{% /tab %}

{% tab title="Python" %}
App Analytics is available starting in version 0.19.0 of the Python tracing client. This configuration is only available for ddtrace versions 3.x or older. Enable App Analytics globally for all **web** integrations with one configuration parameter in the Tracing Client:

- Tracer Configuration: `ddtrace.config.analytics_enabled = True`
- Environment Variable: `DD_TRACE_ANALYTICS_ENABLED=true`

{% /tab %}

{% tab title="Ruby" %}
App Analytics is available starting in version 0.19.0 of the Ruby tracing client, and can be enabled for all **web** integrations with a global flag.

To do so, set either `DD_TRACE_ANALYTICS_ENABLED=true` in your environment, or configure with:

```ruby
Datadog.configure { |c| c.tracing.analytics.enabled = true }
```

- `true` enables analytics for all web frameworks.
- `false` or `nil` disables analytics, except for integrations that explicitly enable it. (Default)

{% /tab %}

{% tab title="Go" %}
App Analytics is available starting in version 1.11.0 of the Go tracing client, and can be enabled globally for all **web** integrations using:

- the [`WithAnalytics`](https://pkg.go.dev/github.com/DataDog/dd-trace-go/v2/ddtrace/tracer#WithAnalytics) ([v1 documentation](https://pkg.go.dev/gopkg.in/DataDog/dd-trace-go.v1/ddtrace/tracer#WithAnalytics)) tracer start option, for example:

  ```go
  tracer.Start(tracer.WithAnalytics(true))
  ```

- starting in version 1.26.0 using environment variable: `DD_TRACE_ANALYTICS_ENABLED=true`

{% /tab %}

{% tab title="Node.js" %}
App Analytics is available starting in version 0.10.0 of the Node.js tracing client, and can be enabled globally for all web integrations with one configuration parameter in the tracing client:

```javascript
tracer.init({
  analytics: true
})
```

You can also use the following configuration parameter:

- Environment Variable: `DD_TRACE_ANALYTICS_ENABLED=true`

{% /tab %}

{% tab title=".NET" %}
App Analytics is available starting in version 1.1.0 of the .NET tracing client, and can be enabled globally for all **web** integrations with one configuration parameter in the Tracing Client:

- Environment Variable or AppSetting: `DD_TRACE_ANALYTICS_ENABLED=true`

This setting can also be set in code:

```csharp
Tracer.Instance.Settings.AnalyticsEnabled = true;
```

{% /tab %}

{% tab title="PHP" %}
App Analytics is available starting in version 0.17.0 of the PHP tracing client, and can be enabled globally for all **web** integrations with one configuration parameter in the Tracing Client:

- Environment Variable: `DD_TRACE_ANALYTICS_ENABLED=true`

{% /tab %}

{% tab title="C++" %}
App Analytics is available starting in version 1.0.0 of the C++ tracing client, and can be enabled globally for all service entry spans by setting the environment variable: `DD_TRACE_ANALYTICS_ENABLED` to `true`. **Note**: This setting can also be set in the code directly:

```csharp
datadog::opentracing::TracerOptions tracer_options;
  tracer_options.agent_host = "dd-agent";
  tracer_options.service = "<SERVICE_NAME>";
  tracer_options.analytics_rate = 1.0;
  auto tracer = datadog::opentracing::makeTracer(tracer_options);
```

{% /tab %}

{% tab title="NGINX" %}
To enable App Analytics for Nginx:

1. Set the environment variable: `DD_TRACE_ANALYTICS_ENABLED` to `true`.

1. Add `env DD_TRACE_ANALYTICS_ENABLED;` at the top of your `nginx.conf` file.

{% /tab %}

#### Configure additional services (optional){% #configure-additional-services-optional %}

##### Configure by integration{% #configure-by-integration %}

{% tab title="Java" %}
In addition to setting globally, you can enable or disable App Analytics for individual integrations using the following setting:

- System Property: `-Ddd.<integration>.analytics.enabled=true`
- Environment Variable: `DD_<INTEGRATION>_ANALYTICS_ENABLED=true`

Use this in addition to the global configuration for any integrations that submit custom services. For example, for JMS spans which comes in as a custom service, you can set the following to enable all JMS Tracing in App Analytics:

- System Property: `-Ddd.jms.analytics.enabled=true`
- Environment Variable: `DD_JMS_ANALYTICS_ENABLED=true`

Integration names can be found on the [integrations table](https://docs.datadoghq.com/tracing/compatibility_requirements/java/#compatibility).
{% /tab %}

{% tab title="Python" %}
In addition to setting globally, you can enable or disable App Analytics for individual integrations using the following setting:

- Tracer Configuration: `ddtrace.config.<INTEGRATION>.analytics_enabled = True`
- Environment Variable: `DD_<INTEGRATION>_ANALYTICS_ENABLED=true`

Use this in addition to the global configuration for any integrations that submit custom services. For example, for Boto spans which comes in as a custom service, set the following to enable all Boto Tracing in App Analytics:

- Tracer Configuration: `ddtrace.config.boto.analytics_enabled = True`
- Environment Variable: `DD_BOTO_ANALYTICS_ENABLED=true`

**Note**: Several integrations require non-standard configuration due to the integration-specific implementation of the tracer. Consult the library documentation on [App Analytics](https://ddtrace.readthedocs.io/en/stable/advanced_usage.html#trace_search_analytics) for details.
{% /tab %}

{% tab title="Ruby" %}
App Analytics can be enabled for specific integrations.

To do so, set either `DD_<INTEGRATION>_ANALYTICS_ENABLED=true` in your environment, or configure with:

```ruby
Datadog.configure { |c| c.tracing.instrument :integration, analytics_enabled: true }
```

Where `integration` is the name of the integration. See the [list of available integrations](https://docs.datadoghq.com/tracing/setup/ruby/#library-compatibility) for options.

- `true` enables analytics for this integration, regardless of the global setting.
- `false` disables analytics for this integration, regardless of the global setting.
- `nil` defers to global setting for analytics.

{% /tab %}

{% tab title="Go" %}
**Note**: This documentation uses v2 of the Go tracer, which Datadog recommends for all users. If you are using v1, see the [migration guide](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/migration) to upgrade to v2.

In addition to the global setting, you can enable or disable App Analytics individually for each integration. As an example, for configuring the standard library's `net/http` package, you could do:

```go
package main

import (
    httptrace "github.com/DataDog/dd-trace-go/contrib/net/http/v2"
    "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
)

func main() {
    tracer.Start()
    defer tracer.Stop()

    mux := httptrace.NewServeMux(httptrace.WithAnalytics(true))
    // ...
}
```

{% /tab %}

{% tab title="Node.js" %}
In addition to setting globally, you can enable or disable App Analytics for individual integrations.

For example, to enable App Analytics for `express`:

```js
tracer.use('express', {
  analytics: true
})
```

Integration names can be found on the [integrations table](https://docs.datadoghq.com/tracing/setup/nodejs/#integrations).
{% /tab %}

{% tab title=".NET" %}
In addition to setting globally, you can enable or disable App Analytics for individual integrations.

- Environment Variable or AppSetting: `DD_<INTEGRATION>_ANALYTICS_ENABLED=true`

Or in code:

```csharp
Tracer.Instance.Settings.Integrations["<INTEGRATION>"].AnalyticsEnabled = true;
```

For example, to enable App Analytics for ASP.NET MVC:

- Environment Variable or AppSetting: `DD_ASPNETMVC_ANALYTICS_ENABLED=true`

Or in code:

```csharp
Tracer.Instance.Settings.Integrations["AspNetMvc"].AnalyticsEnabled = true;
```

Integration names can be found on the [integrations table](https://docs.datadoghq.com/tracing/setup/dotnet/#integrations). **Note:** On Linux, the names of environment variables are case-sensitive.
{% /tab %}

{% tab title="PHP" %}
In addition to setting globally, you can enable or disable App Analytics for individual integrations using the following setting:

- Environment Variable: `DD_<INTEGRATION>_ANALYTICS_ENABLED=true`

Use this in addition to the global configuration for any integrations that submit custom services. For example, for Symfony spans which comes in as a custom service, you can set the following to enable all Symfony Tracing in App Analytics:

- Environment Variable: `DD_SYMFONY_ANALYTICS_ENABLED=true`

Integration names can be found on the [integrations table](https://docs.datadoghq.com/tracing/setup/php/#integration-names).
{% /tab %}

#### Database services{% #database-services %}

{% tab title="Java" %}
Database tracing is not captured by App Analytics by default and you must enable collection manually for each integration. For example:

- System Property: `-Ddd.jdbc.analytics.enabled=true`
- Environment Variable: `DD_JDBC_ANALYTICS_ENABLED=true`

{% /tab %}

{% tab title="Python" %}
Database tracing is not captured by App Analytics by default and you must enable collection manually for each integration. For example:

- Tracer Configuration: `ddtrace.config.psycopg.analytics_enabled = True`
- Environment Variable: `DD_PSYCOPG_ANALYTICS_ENABLED=true`

{% /tab %}

{% tab title="Ruby" %}
Database tracing is not captured by App Analytics by default and you must enable collection manually for each integration. For example:

```ruby
Datadog.configure { |c| c.tracing.instrument :mongo, analytics_enabled: true }
```

{% /tab %}

{% tab title="Go" %}
Database tracing is not captured by App Analytics by default. Enable collection manually for each integration, for example:

```go
// Register the database driver with Analytics enabled.
sqltrace.Register("mysql", &mysql.MySQLDriver{}, sqltrace.WithAnalytics(true))
```

{% /tab %}

{% tab title="Node.js" %}
Database tracing is not captured by App Analytics by default and you must enable collection manually for each integration. For example:

```javascript
tracer.use('mysql', {
  analytics: true
})
```

{% /tab %}

{% tab title=".NET" %}
Database tracing is not captured by App Analytics by default and you must enable collection manually for each integration. For example, to enable App Analytics for ADO.NET:

- Environment Variable or AppSetting: `DD_AdoNet_ANALYTICS_ENABLED=true`

Or in code:

```csharp
Tracer.Instance.Settings.Integrations["AdoNet"].AnalyticsEnabled = true;
```

Integration names can be found on the [integrations table](https://docs.datadoghq.com/tracing/setup/dotnet/#integrations). **Note:** On Linux, the names of environment variables are case-sensitive.
{% /tab %}

{% tab title="PHP" %}
Database tracing is not captured by App Analytics by default. You can enable or disable App Analytics for individual integrations using the following setting:

- Environment Variable: `DD_<INTEGRATION>_ANALYTICS_ENABLED=true`

Use this in addition to the global configuration for any integrations that submit custom services. For example, for `mysqli`:

- Environment Variable: `DD_MYSQLI_ANALYTICS_ENABLED=true`

Integration names can be found on the [integrations table](https://docs.datadoghq.com/tracing/setup/php/#integrations).
{% /tab %}

##### Custom instrumentation{% #custom-instrumentation %}

{% tab title="Java" %}
Applications with custom instrumentation can enable App Analytics by setting the `ANALYTICS_SAMPLE_RATE` tag on a span:

```java
import datadog.trace.api.DDTags;
import datadog.trace.api.Trace;
import io.opentracing.Tracer;
import io.opentracing.util.GlobalTracer;

class MyClass {
  @Trace
  void myMethod() {
    final Span span = GlobalTracer.get().activeSpan();
    // Span provided by @Trace annotation.
    if (span != null) {
      span.setTag(DDTags.SERVICE, "<SERVICE_NAME>");
      span.setTag(DDTags.ANALYTICS_SAMPLE_RATE, 1.0);
    }
  }
}
```

**Note:** App analytics for [dd.trace.methods](https://docs.datadoghq.com/tracing/custom_instrumentation/java/#dd-trace-methods) or [trace annotations](https://docs.datadoghq.com/tracing/custom_instrumentation/java/#trace-annotations) spans can be enabled by setting `-Ddd.trace-annotation.analytics.enabled=true`.
{% /tab %}

{% tab title="Python" %}
Applications with custom instrumentation can enable App Analytics by setting the `ddtrace.constants.ANALYTICS_SAMPLE_RATE_KEY` tag on a span:

```python
from ddtrace import tracer
from ddtrace.constants import ANALYTICS_SAMPLE_RATE_KEY

@tracer.wrap()
def my_method():
    span = tracer.current_span()
    span.set_tag(ANALYTICS_SAMPLE_RATE_KEY, True)
```

{% /tab %}

{% tab title="Ruby" %}
Applications with custom instrumentation can enable App Analytics by setting the `Analytics::TAG_ENABLED` tag on a span:

```ruby
Datadog::Tracing.trace('my.task') do |span|
  # Set the analytics sample rate to 1.0
  span.set_tag(Datadog::Tracing::Metadata::Ext::Analytics::TAG_ENABLED, true)
end
```

{% /tab %}

{% tab title="Go" %}
For custom instrumentation, a special tag has been added to enable App Analytics on a span, as can be seen below:

```go
span.SetTag(ext.AnalyticsEvent, true)
```

This marks the span as a App Analytics event.
{% /tab %}

{% tab title="Node.js" %}
Applications with custom instrumentation can enable App Analytics by setting the `ANALYTICS` tag on a span:

```javascript
const { ANALYTICS } = require('dd-trace/ext/tags')

span.setTag(ANALYTICS, true)
```

{% /tab %}

{% tab title=".NET" %}
Applications with custom instrumentation can enable App Analytics by setting the `Tags.Analytics` tag on a span:

```csharp
using Datadog.Trace;

using(var scope = Tracer.Instance.StartActive("web.request"))
{
    // enable Analytics on this span
    scope.span.SetTag(Tags.Analytics, "true");
}
```

{% /tab %}

{% tab title="PHP" %}
Applications with custom instrumentation can enable App Analytics by setting the `ANALYTICS_KEY` tag on a span:

```php
<?php
  // ... your existing span that you want to enable for App Analytics
  $span->setTag(Tag::ANALYTICS_KEY, true);
?>
```

{% /tab %}

{% tab title="C++" %}
Applications with custom instrumentation can enable App Analytics by setting the `analytics_event` tag on a span:

```cpp
...
#include <datadog/tags.h>
...
auto tracer = ...
auto span = tracer->StartSpan("operation_name");
// A boolean value of true enables App Analytics for the span,
// with a sample rate of 1.0.
span->SetTag(datadog::tags::analytics_event, true);
// A double value between 0.0 and 1.0 enables App Analytics
// and sets the sample rate to the provided value.
span->SetTag(datadog::tags::analytics_event, 0.5);
```

{% /tab %}

### In the Datadog Agent{% #in-the-datadog-agent %}

{% alert level="warning" %}
This section describes deprecated features with configuration information relevant to legacy App Analytics.
{% /alert %}

To configure a rate of spans to analyze by service, setup the following in the `datadog.yaml` file:

```
apm_config:
  analyzed_rate_by_service:
    service_A: 1
    service_B: 0.2
    service_C: 0.05
```

To configure a rate of spans to analyze by service and operation name, setup the following in the `datadog.yaml` file:

```
apm_config:
  analyzed_spans:
    service_A|operation_name_X: 1
    service_A|operation_name_Y: 0.25
    service_B|operation_name_Z: 0.01
```

## Troubleshooting: Maximum events per second limit{% #troubleshooting-maximum-events-per-second-limit %}

If you encounter the following error message in your Agent logs, your applications are emitting more than the default 200 trace events per second allowed by APM.

```
Max events per second reached (current=300.00/s, max=200.00/s). Some events are now being dropped (sample rate=0.54). Consider adjusting event sampling rates.
```

To increase the APM rate limit for the Agent, configure the `max_events_per_second` attribute within the Agent's configuration file (underneath the `apm_config:` section). For containerized deployments (for example, Docker or Kubernetes), use the `DD_APM_MAX_EPS` environment variable.

**Note**: Increasing the APM rate limit could result in increased costs for App Analytics.
