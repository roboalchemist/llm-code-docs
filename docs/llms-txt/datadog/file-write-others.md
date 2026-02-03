# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/file-write-others.md

---
title: do not let all users write permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not let all users write permissions
---

# do not let all users write permissions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/file-write-others`

**Language:** Python

**Severity:** Warning

**Category:** Security

**CWE**: [280](https://cwe.mitre.org/data/definitions/280.html)

## Description{% #description %}

Make sure that programs do not let write permissions for all users. When using `os.chmod`, the user should never use `S_IWOTH` that gives the permission to all users to write the file on the filesystem.

Instead, this permission should be removed, and proper control access should be configured.

See the following related CWE:

- [CWE-275](https://cwe.mitre.org/data/definitions/275.html) category - Permission Issues
- [CWE-280](https://cwe.mitre.org/data/definitions/280.html) - Improper Handling of Insufficient Permissions or Privileges

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import stat

path = "/path/to/file"
os.chmod(path, stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import stat

path = "/path/to/file"
os.chmod(path, stat.S_IROTH | stat.S_IXOTH)  # no write by others
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 