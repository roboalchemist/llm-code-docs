# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/files-permissions.md

---
title: Do not give write access to others
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not give write access to others
---

# Do not give write access to others

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/files-permissions`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [732](https://cwe.mitre.org/data/definitions/732.html)

## Description{% #description %}

Never give write access to other users.

#### Learn More{% #learn-more %}

- [Linux Privileges Escalation Guide](https://payatu.com/blog/a-guide-to-linux-privilege-escalation/)
- [CWE-732](https://cwe.mitre.org/data/definitions/732.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Main {
    public test() {
            Set<PosixFilePermission> perms = new HashSet<PosixFilePermission>();
            perms.add(PosixFilePermission.OWNER_READ);
            perms.add(PosixFilePermission.OWNER_WRITE);
            perms.add(PosixFilePermission.OWNER_EXECUTE);
            perms.add(PosixFilePermission.GROUP_READ);
            perms.add(PosixFilePermission.GROUP_EXECUTE);
            perms.add(PosixFilePermission.OTHERS_READ);
            perms.add(PosixFilePermission.OTHERS_EXECUTE);
    }
}
```

```java
class Main {
    public static void main(String[] args) {
        Files.setPosixFilePermissions("file", PosixFilePermissions.fromString("rw-rw-rw-"));
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        Files.setPosixFilePermissions("file", PosixFilePermissions.fromString("rw-rw-r--"));
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 