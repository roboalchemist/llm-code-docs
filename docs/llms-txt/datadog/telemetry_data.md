# Source: https://docs.datadoghq.com/security/sensitive_data_scanner/setup/telemetry_data.md

---
title: Telemetry Data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Sensitive Data Scanner > Setup > Telemetry Data
---

# Telemetry Data

## Overview{% #overview %}

Sensitive Data Scanner in the Cloud scans telemetry data, such as your application logs, APM events, RUM events, and events from Event Management. The data that can be scanned and redacted are:

- **Logs**: All structured and unstructured log content, including log message and attribute values
- **APM**: Span attribute values only
- **RUM**: Event attribute values only
- **Events**: Event attribute values only

Optionally, sampling rates can be set between 10% and 99% for each product. This helps manage costs when you first get started by reducing the amount of data that gets scanned for sensitive information.

For each scanning rule, one of the following actions can be applied to matched sensitive data:

- **Redact**: Replace the entire matched data with a single token that you choose, such as `[sensitive_data]`.
- **Partially redact**: Replace a specific portion of all matching values.
- **Hash**: Replace the entire matched data with a non-reversible unique identifier.
- **Mask** (available for logs only): Obfuscate all matching values. Users with the `Data Scanner Unmask` permission can de-obfuscate (unmask) and view this data in Datadog. See Mask action for more information.

**Notes**:

- When scanning sampled data, you will not be able to select actions that obfuscate the data it scans.
- Sensitive Data Scanner does not scan integer, float, and double values. If the number is in a string format, the string gets scanned.

You submit logs and events to the Datadog backend, so the data leaves your environment before it gets redacted. The logs and events are scanned and redacted in the Datadog backend during processing, so sensitive data is redacted before events are indexed and shown in the Datadog UI.

If you don't want data to leave your environment before it gets redacted, use [Observability Pipelines](https://docs.datadoghq.com/observability_pipelines/) and the [Sensitive Data Scanner processor](https://docs.datadoghq.com/observability_pipelines/processors/sensitive_data_scanner/) to scan and redact sensitive data. See [Set Up Pipelines](https://docs.datadoghq.com/observability_pipelines/configuration/set_up_pipelines/) for information on how to set up a pipeline and its components.

To use Sensitive Data Scanner in the Cloud, set up a scanning group to define what data to scan and then add scanning rules to determine what sensitive information to match within the data.

This document goes through the following:

- The permissions required to view and set up Sensitive Data Scanner.
- Adding a scanning group
- Adding scanning rules
- How to control access to logs wth sensitive data
- How to redact sensitive data in tags

## Setup{% #setup %}

### Permissions{% #permissions %}

By default, users with the Datadog Admin role have access to view and set up scanning rules. To allow other users access, grant the `data_scanner_read` or `data_scanner_write` permissions under [Compliance](https://docs.datadoghq.com/account_management/rbac/permissions/#compliance) to a custom role. See [Access Control](https://docs.datadoghq.com/account_management/rbac/) for details on how to set up roles and permissions.

If a scanning rule uses the **mask** action (only available for logs) for matched sensitive data, users with the `data_scanner_unmask` permission can de-obfuscate and view the data in Datadog. **Note**: Datadog does not recommend using the **mask** action for credentials, unless you have a plan to respond to and rotate all leaked credentials. See Mask action for more information.

{% image
   source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/read_write_permissions.d907313061d25d09b72892bbe7cb72f8.png?auto=format"
   alt="The compliance permissions sections showing data scanner read and writer permissions" /%}

### Add a scanning group{% #add-a-scanning-group %}

A scanning group determines what data to scan. It consists of a query filter, a set of buttons to enable scanning for logs, APM, RUM, and events, and the option to set sampling rates between 10% to 99% for each product. See the [Log Search Syntax](https://docs.datadoghq.com/logs/explorer/search_syntax/) documentation to learn more about query filters.

For Terraform, see the [Datadog Sensitive Data Scanner group](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/sensitive_data_scanner_group) resource.

To set up a scanning group, perform the following steps:

1. Navigate to the [Sensitive Data Scanner](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/configuration) settings page.
1. Click **Add scanning group**. Alternatively, click the **Add** dropdown menu on the top right corner of the page and select **Add Scanning Group**.
1. Enter a query filter for the data you want to scan. At the top, click **APM Spans** to preview the filtered spans. Click **Logs** to see the filtered logs.
1. Enter a name and description for the group.
1. Click the option buttons to enable Sensitive Data Scanner for the products you want (for example, logs, APM spans, RUM events, and Datadog events).
1. Optionally set a sampling rate of 10-99% for the products you want. When you add scanning rules to a group that has sampling enabled, you will not be able to select actions that obfuscate the data it scans. To obfuscate matches, you must choose to scan all data matching your group query filter.
1. Click **Create**.

By default, a newly-created scanning group is disabled. To enable a scanning group, click the corresponding toggle on the right side.

### Add scanning rules{% #add-scanning-rules %}

A scanning rule determines what sensitive information to match within the data defined by a scanning group. You can add predefined scanning rules from Datadog's Scanning Rule Library or create your own rules using regular expression (regex) patterns. The data is scanned at ingestion time during processing. For logs, this means the scan is done before indexing and other routing decisions.

Whenever possible, use Datadog's out-of-the-box library rules. These rules are predefined rules that detect common patterns such as email addresses, credit card numbers, API keys, authorization tokens, network and device information, and more. Each rule has recommended keywords for the keyword dictionary to refine matching accuracy. You can also add your own keywords.

For Terraform, see the [Datadog Sensitive Data Scanner rule](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/sensitive_data_scanner_rule) resource.

To add scanning rules, perform the following steps:

1. Navigate to the [Sensitive Data Scanner](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/configuration) settings page.
1. Click the scanning group where you want to add the scanning rules.
1. Click **Add Scanning Rule**. Alternatively, click the **Add** dropdown menu on the top right corner of the page and select **Add Scanning Rule**.
1. Select whether you want to add a library rule or create a custom scanning rule.

{% collapsible-section #add-library-rules %}
Add library rules
The Scanning Rule Library contains predefined rules for detecting common patterns such as email addresses, credit card numbers, API keys, authorization tokens, and more.

1. Select a scanning group if you did not create this rule within a scanning group.
1. In the **Priority** dropdown menu, select the priority level for the rule based on your business needs.
1. In the **Add Library Rules** section, select the library rules you want to use.
1. In the **Action on Match** section, select if you want to scan the **Entire Event** or **Specific Attributes**. See Scan or exclude specific-attributes on how to make pattern matching more precise.
   - If you are scanning the entire event, you can optionally exclude specific attributes from getting scanned.
   - If you are scanning specific attributes, specify which attributes you want to scan.
1. For **Define actions on match**, select the action you want to take for the matched information. **Note**: Redaction, partial redaction, and hashing are all irreversible actions.
   - **Redact**: Replaces all matching values with the text you specify in the **Replacement text** field.
   - **Partially Redact**: Replaces a specified portion of all matched data. In the **Redact** section, specify the number of characters you want to redact and which part of the matched data to redact.
   - **Hash**: Replaces all matched data with a unique identifier. The UTF-8 bytes of the match is hashed with the 64-bit fingerprint of FarmHash.
   - **Mask** (available for logs only): Obfuscates all matching values. Users with the `Data Scanner Unmask` permission can de-obfuscate (unmask) and view this data. See Mask action for more information.
1. (Optional) Add tags you want to associate with events where the values match the specified regex pattern.
   - Datadog recommends using `sensitive_data` and `sensitive_data_category` tags. These tags can then be used in searches, dashboards, and monitors.
   - See Control access to logs with sensitive data for information on how to use tags to determine who can access logs containing sensitive information.
1. Click **Add Rules**.

#### Add custom keywords{% #add-custom-keywords %}

The [recommended keywords](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules/) are used by default when library rules are added. After adding library rules, you can edit each rule separately and add keywords to or remove keywords from the keyword dictionary. For example, if you are scanning for a sixteen-digit Visa credit card number, you can add keywords like `visa`, `credit`, and `card`.

1. Navigate to the [Sensitive Data Scanner](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/configuration) settings page.
1. Click the scanning group with the rule you want to edit.
1. Hover over the rule, and then click the pencil icon.
1. In the **Match Conditions** section, click **Custom Keywords**.
   - To add keywords, enter a keyword and click the plus icon to add the keyword to the list.
   - To remove keywords, click the **X** next to the keyword you want to remove.
   - You can also require that these keywords be within a specified number of characters of a match. By default, keywords must be within 30 characters before a matched value.
   - **Note**: You cannot have more than 20 keywords for a rule.
1. In the **Type or paste event data to test the rule** section, add event data to evaluate your rule and add keywords to refine match conditions.
1. Click **Update**.

#### Add suppressions{% #add-suppressions %}

1. (Optional) In the **Suppress specific match types to ignore risk-accepted data** section, you can add conditions to ignore certain matches. See Suppress specific matches to ignore risk-accepted data for more informationTo add a suppression:
   1. Click **Add New Suppression** and choose a condition:
      - **Match exactly**: For precise values such as, `info@company.org`.
      - **Start with**: For prefixes or ranges. For example: `10.0.0` for all IP ranges under `10.0.0.X`.
      - **End with**: For domains such as `@company.org`.
   1. Enter a value (for example: `@company.org`) and click the plus sign (**+**) to add it.
   1. (Optional) Enter additional suppression terms.
   1. Click **Add New Suppression** to add more suppression conditions to the same rule.

{% /collapsible-section %}

{% collapsible-section #add-custom-rule %}
Add a custom rule
You can create custom scanning rules using regex patterns to scan for sensitive data.

1. Select a scanning group if you did not create this rule within a scanning group.
1. Enter a name for the rule.
1. In the **Priority** dropdown menu, select the priority level for the rule based on your business needs.
1. (Optional) Enter a description for the rule.
1. In the **Match conditions** section, specify the regex pattern to use for matching against events in the **Regex pattern** field. Define regex patterns that are as precise as possible because generic patterns result in more false positives.Sensitive Data Scanner supports Perl Compatible Regular Expressions (PCRE), but the following patterns are not supported:
   - Backreferences and capturing sub-expressions (lookarounds)
   - Arbitrary zero-width assertions
   - Subroutine references and recursive patterns
   - Conditional patterns
   - Backtracking control verbs
   - The `\C` "single-byte" directive (which breaks UTF-8 sequences)
   - The `\R` newline match
   - The `\K` start of match reset directive
   - Callouts and embedded code
   - Atomic grouping and possessive quantifiers
1. For **Check surrounding match context for keywords to reduce noise**, add keywords to refine detection accuracy when matching regex conditions. For example, if you are scanning for a sixteen-digit Visa credit card number, you can add keywords like `visa`, `credit`, and `card`.
   - To add keywords, enter a keyword and click the plus icon to add the keyword to the list.
   - To remove keywords, click the **X** next to the keyword you want to remove.
   - You can also require that these keywords be within a specified number of characters of a match. By default, keywords must be within 30 characters before a matched value. **Note**: You cannot have more than 20 keywords for a rule.
1. (Optional) In the **Suppress specific match types to ignore risk-accepted data** section, you can add conditions to ignore certain matches. See Suppress specific matches to ignore risk-accepted data for more informationTo add a suppression:
   1. Click **Add New Suppression** and choose a condition:
      - **Match exactly**: For precise values such as, `info@company.org`.
      - **Start with**: For prefixes or ranges. For example: `10.0.0` for all IP ranges under `10.0.0.X`.
      - **End with**: For domains such as `@company.org`.
   1. Enter a value (for example: `@company.org`) and click the plus sign (**+**) to add it.
   1. (Optional) Enter additional suppression terms.
   1. Click **Add New Suppression** to add more suppression conditions to the same rule.
1. In the **Type or paste event data to test the rule** section, add event data to evaluate your rule and add keywords to refine match conditions.
1. In the **Action on Match** section, select if you want to scan the **Entire Event** or **Specific Attributes**. See Scan or exclude specific-attributes on how to make pattern matching more precise.
   - If you are scanning the entire event, you can optionally exclude specific attributes from getting scanned.
   - If you are scanning specific attributes, specify which attributes you want to scan.
1. For **Define actions on match**, select the action you want to take for the matched information. **Note**: Redaction, partial redaction, and hashing are all irreversible actions.
   - **Redact**: Replaces all matching values with the text you specify in the **Replacement text** field.
   - **Partially Redact**: Replaces a specified portion of all matched data. In the **Redact** section, specify the number of characters you want to redact and which part of the matched data to redact.
   - **Hash**: Replaces all matched data with a unique identifier. The UTF-8 bytes of the match is hashed with the 64-bit fingerprint of FarmHash.
   - **Mask** (available for logs only): Obfuscates all matching values. Users with the `Data Scanner Unmask` permission can de-obfuscate (unmask) and view this data. See Mask action for more information.
1. (Optional) Add tags you want to associate with events where the values match the specified regex pattern.
   - Datadog recommends using `sensitive_data` and `sensitive_data_category` tags. These tags can then be used in searches, dashboards, and monitors.
   - See Control access to logs with sensitive data for information on how to use tags to determine who can access logs containing sensitive information.
1. Click **Add Rule**.

{% /collapsible-section %}

**Notes**:

- Any rules that you add or update affect only data coming into Datadog after the rule was defined.
- Sensitive Data Scanner does not affect any rules you define on the Datadog Agent directly.
- After rules are added, ensure that the toggles for your scanning groups are enabled to begin scanning.
- When you add rules to a scanning group with sampling enabled, you will not be able to select the **redact**, **partially redact**, or **hash** actions. For complete obfuscation, disable sampling in your scanning group settings.

See [Investigate Sensitive Data Findings](https://docs.datadoghq.com/security/sensitive_data_scanner/guide/investigate_sensitive_data_findings/) for details on triaging sensitive data using the [Findings](https://app.datadoghq.com/sensitive-data-scanner/telemetry) page.

#### Excluded namespaces{% #excluded-namespaces %}

There are reserved keywords that the Datadog platform requires for functionality. If any of these words are in a log that is being scanned, the 30 characters after the matched word are ignored and not redacted. For example, what comes after the word `date` in a log is usually the event timestamp. If the timestamp is accidentally redacted, that would result in issues with processing the log and being able to query it later. Therefore, the behavior for excluded namespaces is to prevent unintentionally redacting important information for product functionality.

The excluded namespaces are:

{% tab title="Logs" %}

- `host`
- `hostname`
- `syslog.hostname`
- `service`
- `status`
- `env`
- `dd.trace_id`
- `trace_id`
- `trace id`
- `dd.span_id`
- `span_id`
- `span id`
- `@timestamp`
- `timestamp`
- `_timestamp`
- `Timestamp`
- `date`
- `published_date`
- `syslog.timestamp`
- `error.fingerprint`
- `x-datadog-parent-id`

{% /tab %}

{% tab title="Spans" %}

- `metrics._dd.`
- `metrics.dd.`
- `metrics._dd1.`
- `metrics.otel.trace_id`
- `metrics.otlp.`
- `metrics._sampling_priority_v1`
- `metrics._sample_rate`
- `meta._dd.`
- `meta.api.endpoint.`
- `meta.dd.`
- `meta_struct.dd.`
- `meta_struct._dd.`
- `meta_struct.api.endpoint.`
- `meta_struct.appsec.`
- `meta_struct.threat_intel.results.`
- `meta.otel.trace_id`
- `meta.otel.library.`
- `meta.otlp.`
- `trace_id`
- `span_id`
- `start`
- `timestamp`
- `end`
- `duration`
- `parent_id`
- `type`
- `resource`
- `resource_hash`
- `ingest_size_in_bytes`
- `ingestion_reason`
- `error`
- `flags`
- `status`
- `chunk_id`
- `host`
- `host_id`
- `hostname`
- `env`
- `service`
- `operation_name`
- `name`
- `version`
- `meta._dd.error_tracking`
- `meta.error.fingerprint`
- `meta.issue`

{% /tab %}

{% tab title="RUM" %}

- `application.id`
- `session.id`
- `session.initial_view.id`
- `session.last_view.id`
- `view.id`
- `action.id`
- `resource.id`
- `geo`
- `error.fingerprint`
- `error.binary_images.uuid`
- `issue`
- `_dd.trace_id`
- `_dd.span_id`
- `_dd.usage_attribution_tag_names`
- `_dd.error.unminified_frames`
- `_dd.error.threads`

{% /tab %}

#### Suppress specific matches to ignore risk-accepted data{% #suppress-specific-matches-to-ignore-risk-accepted-data %}

Use suppressions to ignore sensitive data matches you consider operationally safe (for example: internal email domains or private IP ranges).

**Notes**:

- Suppressed matches are not redacted, masked, or hashed.
- Suppressed matches are excluded from the Findings page, dashboards, alerts, and other reporting workflows.
- Suppressions are defined per rule within a scanning group.

#### Scan or exclude specific attributes{% #scan-or-exclude-specific-attributes %}

To make matches more precise, you can also do one of the following:

- Scan the entire event but exclude certain attributes from getting scanned. For example, if you are scanning for personally identifiable information (PII) like physical addresses, you might want to exclude attributes such as `ip_address`.
- Scan for specific attributes to narrow the scope of the data that is scanned. For example, if you are scanning for physical addresses, you can choose specific attributes such as `street` and `city`.

### Edit scanning rules{% #edit-scanning-rules %}

To edit scanning rules:

1. Navigate to the [Sensitive Data Scanner](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/configuration) settings page.
1. Hover over the scanning rule you want to edit and click the **Edit** (pencil) icon.
1. Make the changes you want for the rule. Depending on the type of rule you are editing, see Add library rules or Add custom rule for more information on each setup section.
1. Click **Update**.

## Control access to logs with sensitive data{% #control-access-to-logs-with-sensitive-data %}

To control who can access logs containing sensitive data, use tags added by the Sensitive Data Scanner to build queries with role-based access control (RBAC). You can restrict access to specific individuals or teams until the data ages out after the retention period. See [How to Set Up RBAC for Logs](https://docs.datadoghq.com/logs/guide/logs-rbac/) for more information.

### Mask action{% #mask-action %}

{% alert level="danger" %}
The mask action is only available for logs.
{% /alert %}

When you set up or edit a scanner rule, there is an **Action on Match** section where you can set the rule to use the **mask** action for matched sensitive data. The **mask** action obfuscates the sensitive data, but users with the `Data Scanner Unmask` permission can de-obfuscate (unmask) and view the data in Datadog.

**Notes**:

- Unmasking can only be performed on indexed logs within Datadog.
- Masked data that is accessed programmatically, such as by using the API or Terraform, or within archives, always appears obfuscated and cannot be unmasked.
- Unmasking does not work on rehydrated logs.
- Datadog does not recommend using the **mask** action for credentials, unless you have a plan to respond to and rotate all leaked credentials.

To unmask sensitive data, navigate to the [Summary page](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/summary), click on a scanning rule, and then click on a log. If you have permission to see masked data, that data has an eye icon next to it. Click the eye icon to reveal the data. You can also use the [Log Explorer](https://app.datadoghq.com/logs) to view your masked log data.

## Redact sensitive data in tags{% #redact-sensitive-data-in-tags %}

To redact sensitive data contained in tags, you must [remap](https://docs.datadoghq.com/logs/log_configuration/processors/?tab=ui#remapper) the tag to an attribute and then redact the attribute. Uncheck `Preserve source attribute` in the remapper processor so that the tag is not preserved during the remapping.

To remap the tag to an attribute:

1. Navigate to your [log pipeline](https://app.datadoghq.com/logs/pipelines).
1. Click **Add Processor**.
1. Select **Remapper** in the processor type dropdown menu.
1. Name the processor.
1. Select **Tag key(s)**.
1. Enter the tag key.
1. Enter a name for the attribute the tag key is remapped to.
1. Disable **Preserve source attribute**.
1. Click **Create**.

To redact the attribute:

1. Navigate to your [scanning group](https://app.datadoghq.com/organization-settings/sensitive-data-scanner/configuration).
1. Click **Add Scanning Rule**.
1. Check the library rules you want to use.
1. Select **Specific Attributes** for **Scan entire event or portion of it**.
1. Enter the name of the attribute you created earlier to specify that you want it scanned.
1. Select the action you want when there's a match.
1. Optionally, add tags.
1. Click **Add Rules**.

## Log rehydration{% #log-rehydration %}

When you rehydrate logs from an archive, the Sensitive Data Scanner does not re-scan those logs. Instead, Datadog restores the logs exactly as they were written to the archive.

If your archive is configured to include [Datadog tags](https://docs.datadoghq.com/logs/log_configuration/archives/?tab=awss3#datadog-tags), and your scanning rules added tags when the logs were initially ingested and processed by Sensitive Data Scanner, you can use those tags to identify which rehydrated logs previously contained sensitive data. This allows you to filter rehydrated logs using queries such as `sensitive_data:<rule_tag_name>`.

The metadata of matched sensitive data is not stored in archived logs, so sensitive data matches are not highlighted when those logs are rehydrated. The archive format contains only the original log payload and any preserved tags. It does not include the positional information that Sensitive Data Scanner uses in the Datadog UI to visually highlight detected values.

What you can do with rehydrated logs:

- If tags were included in the archive, filter for logs that previously matched scanning rules.
- Investigate historical events that contain sensitive data.

What you **cannot** do with rehydrated logs:

- View in-line highlighted sensitive data matches in the UI: The matches remain obfuscated even if mask, redact, partially redact, or hash was chosen as an action on match.
- Trigger retroactive scans: Sensitive Data Scanner does not re-scan rehydrated logs.

## Disable Sensitive Data Scanner{% #disable-sensitive-data-scanner %}

To turn off Sensitive Data Scanner entirely, set the toggle to **off** for each Scanning Group so that they are disabled.

## Further reading{% #further-reading %}

- [Learn more about out-of-the-box library rules](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/library_rules)
- [Learn more about creating custom rules](https://docs.datadoghq.com/security/sensitive_data_scanner/scanning_rules/custom_rules)
