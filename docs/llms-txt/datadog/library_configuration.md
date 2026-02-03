# Source: https://docs.datadoghq.com/security/application_security/policies/library_configuration.md

---
title: Library Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > App and API Protection > Policies > Library
  Configuration
---

# Library Configuration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Configuring a client IP header{% #configuring-a-client-ip-header %}

AAP automatically attempts to resolve `http.client_ip` from several well-known headers, such as `X-Forwarded-For`. If you use a custom header for this field, or want to bypass the resolution algorithm, set the `DD_TRACE_CLIENT_IP_HEADER` environment variable. If this variable is set, the library only checks the specified header for the client IP.

## Track authenticated bad actors{% #track-authenticated-bad-actors %}

Many critical attacks are performed by authenticated users who can access your most sensitive endpoints. To identify bad actors that are generating suspicious security activity, add user information to traces by instrumenting your services with the standardized user tags. You can add custom tags to your root span, or use instrumentation functions.

The Datadog Tracing Library attempts to detect user login and signup events when compatible authentication frameworks are in use, and AAP is enabled.

Read [Tracking User Activity](https://docs.datadoghq.com/security/application_security/add-user-info/) for more information on how to manually track user activity, or [see how to opt out](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=set_user#disabling-automatic-user-activity-event-tracking) of the automatic tracking.

## Exclude specific parameters from triggering detections{% #exclude-specific-parameters-from-triggering-detections %}

There may be a time when an AAP signal, or a security trace, is a false positive. For example, AAP repeatedly detects the same security trace and a signal is generated, but the signal has been reviewed and is not a threat.

You can add an entry to the passlist, which ignore events from a rule, to eliminate noisy signal patterns and focus on legitimately security traces.

To add a passlist entry, do one of the following:

- Click on a signal in [AAP Signals](https://app.datadoghq.com/security/appsec/signals) and click the **Add Entry** link next to the **Add to passlist** suggested action. This method automatically adds an entry for the targeted service.
- Navigate to [Passlist Configuration](https://app.datadoghq.com/security/configuration/asm/passlist) and manually configure a new passlist entry based on your own criteria.

**Note**: Requests (traces) that match a passlist entry are not billed.

## Data security considerations{% #data-security-considerations %}

The data that you collect with Datadog can contain sensitive information that you want to filter out, obfuscate, scrub, filter, modify, or just not collect. Additionally, the data may contain synthetic traffic that might cause your threat detection be inaccurate, or cause Datadog to not accurately indicate the security of your services.

By default, AAP collects information from security traces to help you understand why the request was flagged as suspicious. Before sending the data, AAP scans it for patterns and keywords that indicate that the data is sensitive. If the data is deemed sensitive, it is replaced with a `<redacted>` flag. This enables you to observe that although the request was suspicious, the request data was not collected because of data security concerns. User-related data, such user IDs of authenticated requests, are not part of the data being redacted.

To protect users' data, **sensitive data scanning is activated by default in AAP**. You can customize the configuration by using the following environment variables. The scanning is based on the [RE2 syntax](https://github.com/google/re2/wiki/Syntax). To customize scanning, set the value of these environment variables to a valid [RE2](https://github.com/google/re2/wiki/Syntax) pattern:

- `DD_APPSEC_OBFUSCATION_PARAMETER_KEY_REGEXP` - Pattern for scanning for keys whose values commonly contain sensitive data. If found, the values and any child nodes associated with the key are redacted.
- `DD_APPSEC_OBFUSCATION_PARAMETER_VALUE_REGEXP` - Pattern for scanning for values that could indicate sensitive data. If found, the value and all its child nodes are redacted.

{% alert level="info" %}
**For Ruby only, starting in `ddtrace` version 1.1.0**
You can also configure scanning patterns in code:

```ruby
Datadog.configure do |c|
  # ...

  # Set custom RE2 regexes
  c.appsec.obfuscator_key_regex = '...'
  c.appsec.obfuscator_value_regex = '...'
end
```

{% /alert %}

The following are examples of data that are flagged as sensitive by default:

- `pwd`, `password`, `ipassword`, `pass_phrase`
- `secret`
- `key`, `api_key`, `private_key`, `public_key`
- `token`
- `consumer_id`, `consumer_key`, `consumer_secret`
- `sign`, `signed`, `signature`
- `bearer`
- `authorization`
- `BEGIN PRIVATE KEY`
- `ssh-rsa`

See [APM Data Security](https://docs.datadoghq.com/tracing/configure_data_security/) for information about other mechanisms in the Datadog Agent and libraries that can also be used to remove sensitive data.

See [Automatic user activity event tracking modes](https://docs.datadoghq.com/security/application_security/how-it-works/add-user-info/?tab=set_user#automatic-user-activity-event-tracking-modes) for information on automatic user activity tracking modes and how to configure them. See how Datadog libraries allow you to configure auto-instrumentation by using the `DD_APPSEC_AUTO_USER_INSTRUMENTATION_MODE` environment variable with the short name for the mode: `ident|anon|disabled`.

## Configure a custom blocking page or payload{% #configure-a-custom-blocking-page-or-payload %}

The blocked requests feature JSON or HTML content. If the [`Accept` HTTP header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept) is pointing to HTML, like `text/html`, the HTML content is used. Otherwise, the JSON one is used.

Both sets of content are embedded in the Datadog Tracer library package and loaded locally. See examples of the templates for [HTML](https://github.com/DataDog/dd-trace-java/blob/master/dd-java-agent/agent-bootstrap/src/main/resources/datadog/trace/bootstrap/blocking/template.html) and [JSON](https://github.com/DataDog/dd-trace-java/blob/master/dd-java-agent/agent-bootstrap/src/main/resources/datadog/trace/bootstrap/blocking/template.json) in the Datadog Java tracer source code on GitHub.

The HTML and JSON content can both be changed using the `DD_APPSEC_HTTP_BLOCKED_TEMPLATE_HTML` and `DD_APPSEC_HTTP_BLOCKED_TEMPLATE_JSON` environment variables within your application deployment file.

Example:

```
DD_APPSEC_HTTP_BLOCKED_TEMPLATE_HTML=<path_to_file.html>
```

Alternatively, you can use the configuration entry.

For Java, add the following:

```java
dd.appsec.http.blocked.template.html = '<path_to_file.html>'
dd.appsec.http.blocked.template.json = '<path_to_file.json>'
```

For Ruby, add the following:

```ruby
# config/initializers/datadog.rb

Datadog.configure do |c|
  # To configure the text/html blocking page
  c.appsec.block.templates.html = '<path_to_file.html>'
  # To configure the application/json blocking page
  c.appsec.block.templates.json = '<path_to_file.json>'
end
```

For PHP, add the following:

```dosini
; 98-ddtrace.ini

; Customises the HTML output provided on a blocked request
datadog.appsec.http_blocked_template_html = <path_to_file.html>

; Customises the JSON output provided on a blocked request
datadog.appsec.http_blocked_template_json = <path_to_file.json>
```

For Node.js, add the following:

```javascript
require('dd-trace').init({
  appsec: {
    blockedTemplateHtml: '<path_to_file.html>',
    blockedTemplateJson: '<path_to_file.json>'
  }
})
```

{% image
   source="https://datadog-docs.imgix.net/images/security/application_security/asm-blocking-page-html.1bd71c4f21b70731d121cf245a78f60f.png?auto=format"
   alt="The page displayed as AAP blocks requests originating from blocked IPs" /%}

## Further Reading{% #further-reading %}

- [Protect against Threats with Datadog App and API Protection](https://docs.datadoghq.com/security/application_security/)
- [Out-of-the-Box App and API Protection Rules](https://docs.datadoghq.com/security/default_rules/?category=cat-application-security)
- [Adding user information to traces](https://docs.datadoghq.com/security/application_security/add-user-info/)
- [Troubleshooting AAP](https://docs.datadoghq.com/security/application_security/troubleshooting)
- [How App and API Protection Works in Datadog](https://docs.datadoghq.com/security/application_security/how-it-works/)
