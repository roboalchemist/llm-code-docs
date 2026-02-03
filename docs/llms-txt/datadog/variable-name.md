# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-inclusive/variable-name.md

---
title: check variable names for wording issues
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > check variable names for wording issues
---

# check variable names for wording issues

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-inclusive/variable-name`

**Language:** Python

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Check the variable names and suggest better names.

Examples of replacement suggestions:

- `blacklist` with `denylist`
- `whitelist` with `allowlist`
- `master` with `primary`
- `slave` with `secondary`

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
# banned name, will suggest allowlist
whitelist = "foo"
names_whitelist = "bla";

names_blacklist = "bla";

addr_master_ip = "5.4.3.8";
addr_slave_ip = "1.2.3.4";
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
# not a problem with the name
snow_white = "happy"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 