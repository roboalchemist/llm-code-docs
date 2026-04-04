# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/multiple-cmd.md

---
title: Do not use multiple CMD
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use multiple CMD
---

# Do not use multiple CMD

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/multiple-cmd`

**Language:** Docker

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The Dockerfile CMD instruction provides defaults for an executing container. These can include an executable, or they can omit the executable, in which case you must specify an ENTRYPOINT instruction. However, if you use multiple CMD instructions in a Dockerfile, only the last CMD instruction takes effect.

Using multiple CMD instructions in a Dockerfile can lead to confusion and unexpected behavior when the Docker image is run (only the last CMD instruction is executed). This can potentially lead to parts of your application not running as expected or not running at all.

To avoid this, ensure that you only use one CMD instruction in your Dockerfile. If you have multiple commands that need to be run, consider using a script to encapsulate these commands and then call this script in your CMD instruction. For example, instead of having `CMD run_server1` and `CMD run_server2`, you could have a script called `run_servers.sh` that contains the commands `run_server1` and `run_server2`, and then your Dockerfile would contain `CMD ./run_servers.sh`. This way, all your commands are run as expected.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM awesomeimage
CMD run_server1
CMD run_server2
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM awesomeimage
CMD run_server
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost/ || exit 1
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
