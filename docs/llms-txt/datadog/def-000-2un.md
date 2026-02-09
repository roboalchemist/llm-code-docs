# Source: https://docs.datadoghq.com/security/default_rules/def-000-2un.md

---
title: Ensure No Daemons are Unconfined by SELinux
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure No Daemons are Unconfined by
  SELinux
---

# Ensure No Daemons are Unconfined by SELinux
 
## Description{% #description %}

Daemons for which the SELinux policy does not contain rules will inherit the context of the parent process. Because daemons are launched during startup and descend from the `init` process, they inherit the `unconfined_service_t` context.

To check for unconfined daemons, run the following command:

```
$ sudo ps -eZ | grep "unconfined_service_t"
```

It should produce no output in a well-configured system.

## Rationale{% #rationale %}

Daemons which run with the `unconfined_service_t` context may cause AVC denials, or allow privileges that the daemon does not require.

## Warning{% #warning %}

Automatic remediation of this control is not available. Remediation can be achieved by amending SELinux policy or stopping the unconfined daemons as outlined above.
