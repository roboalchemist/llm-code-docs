# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/pip-pin-versions.md

---
title: Always pin versions with pip
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Always pin versions with pip
---

# Always pin versions with pip

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/pip-pin-versions`

**Language:** Docker

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule emphasizes the importance of pinning versions when using pip to install Python packages in your Dockerfile. Pinning versions means specifying the exact version of the package you want to install. Without pinning, pip installs the latest version of the package, which may not be compatible with your application.

Pinning versions is crucial for maintaining the stability and reproducibility of your Docker images. Without pinning, your builds could suddenly start failing because of a new package version that introduces breaking changes. Your application could also behave differently or even fail when running in different environments, due to variations in package versions.

To avoid these issues, always specify the exact version of the package when using pip install. For example, instead of `RUN pip install django`, use `RUN pip install django==1.9`. If you have a list of packages to install, you can put them in a requirements.txt file with their versions pinned, and then install them with `RUN pip install -r requirements.txt`. This practice will ensure that you always know exactly what versions of packages are in your Docker images, and your builds will be stable and reproducible.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM busybox
RUN pip install django

RUN python3 -m pip install django

RUN python3 -m pip install django && pip install otherpackage
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM busybox
RUN pip install django==1.9

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir shepherd/src -r requirements.txt
RUN pip install --upgrade pip==22.1.2 && pip install --no-cache-dir -r requirements.txt
RUN python3 -m pip install --upgrade pip==22.1.2 && python3 -m pip install --no-cache-dir -r requirements.txt
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
