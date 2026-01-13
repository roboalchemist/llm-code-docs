# Source: https://docs.datadoghq.com/tracing/guide/users-accounts.md

---
title: Setting and Querying User and Account Information in Traces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Setting and Querying User and Account
  Information in Traces
source_url: https://docs.datadoghq.com/guide/users-accounts/index.html
---

# Setting and Querying User and Account Information in Traces

## Overview{% #overview %}

Getting visibility into users and accounts in APM helps you understand which users are affected by performance issues or errors. User and account information is displayed in the [APM Investigator](https://docs.datadoghq.com/tracing/guide/latency_investigator/) and [Error Tracking issues](https://docs.datadoghq.com/error_tracking/explorer/).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/user-accounts/user-account-apm-investigator.7f21e247f84cfefaa9f72193ba55bdd1.png?auto=format"
   alt="User and account information displayed in APM Investigator showing impacted users and accounts" /%}

By tagging traces with user and account identifiers, you can:

- Track which users are impacted by backend errors or latency issues.
- Analyze performance split by user or account segments.
- Monitor user-specific behaviors across your distributed systems.

## Tag user and account information in spans{% #tag-user-and-account-information-in-spans %}

### From RUM{% #from-rum %}

If you're already collecting Real User Monitoring data, you can propagate user and account information from browser or mobile applications to your backend traces:

1. Set user and account information using the [`datadogRum.setUser()`](https://docs.datadoghq.com/real_user_monitoring/browser/advanced_configuration/#identify-user-session) and [`datadogRum.setAccount()`](https://docs.datadoghq.com/real_user_monitoring/browser/advanced_configuration/#identify-account) APIs in your browser application.

1. Enable trace propagation by configuring `allowedTracingUrls` in your RUM SDK initialization. See [Connect RUM and Traces](https://docs.datadoghq.com/real_user_monitoring/correlate_with_other_telemetry/apm/) for detailed setup instructions. Additionally, set `propagateTraceBaggage` to `true`, to automatically propagate user and account context in the [baggage](https://docs.datadoghq.com/tracing/glossary/#baggage) to backend traces alongside the trace context.

The user and account information is automatically remapped in the backend to the [`usr.id` and `account.id` standard attributes](https://docs.datadoghq.com/standard-attributes/?search=usr.id), making it consistent across all your traces. Standard attributes allow you to filter and search your trace data consistently across all your services.

### From APM SDKs{% #from-apm-sdks %}

For backend services or applications without RUM, you can tag spans directly using APM SDKs:

1. Use the [span tagging API](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/) (`set_tag`, `SetTag`, or `setTag` depending on your language) to add `usr.id` and `account.id` attributes to your spans.

1. To propagate user and account information across service boundaries, use [trace context propagation with baggage](https://docs.datadoghq.com/tracing/trace_collection/trace_context_propagation/#baggage).

**Example (Python):**

```python
from ddtrace import tracer

# Tag the span with user and account information
span = tracer.current_root_span()
span.set_tag("usr.id", "user_123")
span.set_tag("account.id", "account_456")

# Set baggage to propagate across service boundaries
span.context.set_baggage_item("user.id", "user_123")
span.context.set_baggage_item("account.id", "account_456")
```

**Note**: When propagating user and account information through baggage, this information is only tagged on [service entry spans](https://docs.datadoghq.com/glossary/#service-entry-span). This means the `usr.id` and `account.id` attributes appear on the first span of each service in your distributed trace.

## Query trace data with user and account information{% #query-trace-data-with-user-and-account-information %}

Tagging spans with user and account IDs enables powerful analysis, giving you visibility into how backend errors and latency affect end-users.

{% alert level="info" %}
Enrich your trace analysis by querying span data with attributes from [Product Analytics User and Account Profiles](https://docs.datadoghq.com/product_analytics/profiles/). To express interest in this upcoming capability, [reach out to Support](https://docs.datadoghq.com/help/).
{% /alert %}

#### Filter traces by user or account in the APM Trace Explorer{% #filter-traces-by-user-or-account-in-the-apm-trace-explorer %}

Query traces using the `usr.id` or `account.id` attributes:

- Search for all traces from a specific user or account: `@usr.id:user_123` or `@account.id:account_456`.
- Combine with other filters: `@usr.id:user_123 service:checkout status:error`.

This allows you to investigate issues affecting specific users or accounts and understand their end-to-end experience across your distributed system.

#### Identify which users or accounts are most affected by errors or latency{% #identify-which-users-or-accounts-are-most-affected-by-errors-or-latency %}

Analyze error patterns and latency issues across your user base to prioritize fixes based on business impact:

- Use [Tag Analysis](https://docs.datadoghq.com/tracing/trace_explorer/tag_analysis/) to identify which users or accounts are disproportionately affected by errors or high latency on backend services.
- [Group queries](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/#trace-groups) by `usr.id` or `account.id` to analyze error rates or latency percentiles by user or account.
- View user and account impact directly in the [APM Investigator](https://docs.datadoghq.com/tracing/guide/latency_investigator/) and [Error Tracking issues](https://docs.datadoghq.com/error_tracking/explorer/) to understand the scope of production problems.

This helps you prioritize incident response based on the number of affected users or the importance of affected accounts.

#### Create monitors and alerts based on user or account segments{% #create-monitors-and-alerts-based-on-user-or-account-segments %}

Set up [APM monitors](https://docs.datadoghq.com/monitors/types/apm/) that alert you when specific user segments experience degraded performance:

- Create error rate monitors filtered by premium account tiers: `@account.id:premium_* status:error`.
- Alert on latency spikes for critical users: `@usr.id:vip_user_* @duration:>5s`.
- Monitor SLA compliance for enterprise accounts by setting monitors on specific account IDs.

This enables proactive monitoring and ensures you can respond quickly when high-value users or accounts experience issues.

## Further reading{% #further-reading %}

- [Connect RUM and APM](https://docs.datadoghq.com/real_user_monitoring/correlate_with_other_telemetry/apm/)
- [Standard Attributes](https://docs.datadoghq.com/standard-attributes/)
- [User and Account Profiles](https://docs.datadoghq.com/product_analytics/profiles/)
