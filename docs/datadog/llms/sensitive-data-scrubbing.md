# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/sensitive-data-scrubbing.md

---
title: Dynamic Instrumentation Sensitive Data Scrubbing
description: >-
  Protect sensitive information by configuring redaction and scrubbing
  mechanisms for Dynamic Instrumentation.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Dynamic Instrumentation > Dynamic
  Instrumentation Sensitive Data Scrubbing
---

# Dynamic Instrumentation Sensitive Data Scrubbing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Datadog Dynamic Instrumentation enhances the observability and debugging capabilities of your applications by capturing variable data at arbitrary code locations in production environments. It also can craft and evaluate expressions in real-time, and integrate their outputs into log messages or add them as span tags.

While this functionality is powerful, it also presents the possibility of sensitive data leaks, both intentional and unintentional. Alongside the product's robust data capture capabilities, it also provides comprehensive measures to safeguard sensitive information.

By understanding and properly configuring these redaction mechanisms, you can use Dynamic Instrumentation with confidence and security.

## Redact based on identifiers{% #redact-based-on-identifiers %}

### Default behavior{% #default-behavior %}

Dynamic Instrumentation automatically redacts values linked to specific identifiers deemed sensitive, such as `password` and `accessToken`. See [the full list of redacted identifiers](https://github.com/DataDog/dd-trace-java/blob/master/dd-java-agent/agent-debugger/debugger-bootstrap/src/main/java/datadog/trace/bootstrap/debugger/util/Redaction.java).

### Custom identifier redaction{% #custom-identifier-redaction %}

You can further tailor redaction by specifying additional identifiers. In your application's environment (not on `datadog-agent`), set the `DD_DYNAMIC_INSTRUMENTATION_REDACTED_IDENTIFIERS` environment variable to a comma-separated list of identifiers such as `firstName,lastName,phoneNumber`.

To exclude specific identifiers from the default redaction list, set the `DD_DYNAMIC_INSTRUMENTATION_REDACTION_EXCLUDED_IDENTIFIERS` environment variable to a comma-separated list of identifiers that should not be redacted, such as `cookie,sessionid`.

Redaction applies universally, regardless of how the identifier is used in the code (as method arguments, local variables, class attributes, dictionary keys, and so on). The associated values are redacted in your infrastructure and not uploaded to Datadog.

## Redact based on specific classes or types{% #redact-based-on-specific-classes-or-types %}

Certain classes may inherently contain sensitive information (for example, a `UserCredentials` class). Again in your application's environment (not on `datadog-agent`), set the `DD_DYNAMIC_INSTRUMENTATION_REDACTED_TYPES` environment variable to a comma-separated list of sensitive types, such as `MyCompany.Authentication.UserCredential,MyCompany.BillingAddress`.

Class-based redaction:

- Redacts variables of the types listed. Their contents are not uploaded to Datadog.
- Stops probes from being set within any code location in the redacted classes.

## Redact based on variable values with Sensitive Data Scanner{% #redact-based-on-variable-values-with-sensitive-data-scanner %}

[Sensitive Data Scanner](https://docs.datadoghq.com/security/sensitive_data_scanner/) identifies and redacts sensitive information based on specific regular expressions.

### Initial setup{% #initial-setup %}

When you first access [Dynamic Instrumentation Setup](https://app.datadoghq.com/dynamic-instrumentation/setup), you can optionally set up default Sensitive Data Scanner rules for Dynamic Instrumentation. These cover common regular expressions for likely sensitive data such as email addresses or JWT tokens.

### Customizing Sensitive Data Scanner{% #customizing-sensitive-data-scanner %}

You can disable the default rules or create other rules through the [Sensitive Data Scanner](https://app.datadoghq.com/organization-settings/sensitive-data-scanner). To create a new Sensitive Data Scanner rule for Dynamic Instrumentation, set it to filter on `source:dd_debugger`.

**Note**: Datadog Sensitive Data Scanner performs its redaction *after* the information is uploaded to Datadog.

## Further reading{% #further-reading %}

- [Setting Up Dynamic Instrumentation](https://docs.datadoghq.com/dynamic_instrumentation/enabling/)
- [Sensitive Data Scanner](https://docs.datadoghq.com/security/sensitive_data_scanner/)
