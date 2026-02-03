# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/service-writable-filesystem.md

---
title: Avoid service with writable filesystem
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid service with writable filesystem
---

# Avoid service with writable filesystem

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/service-writable-filesystem`

**Language:** YAML

**Severity:** Warning

**Category:** Security

**CWE**: [732](https://cwe.mitre.org/data/definitions/732.html)

## Description{% #description %}

This rule advises against configuring services with a writable filesystem in Docker Compose files. Allowing a writable filesystem can increase the attack surface by enabling potential attackers or malicious processes to modify the container's file system, which could lead to unauthorized changes or persistence of malicious code.

Ensuring that services run with a read-only filesystem enhances security by preventing in-container modifications during runtime. This practice helps maintain the integrity of the container environment and reduces the risk of accidental or intentional file tampering.

To comply with this rule, explicitly set `read_only: true` for your service definitions in the Docker Compose YAML file. For example, use `read_only: true` under the service configuration to enforce a read-only root filesystem.

By adopting this approach, you improve the overall security posture of your containerized applications and make them more resilient against attacks or unintended changes.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
version: '3.3'

services:
  postgres:
    build:
      context: .
      dockerfile: Dockerfile.db
    ports:
      - 5432:5432

  redis:
    image: redis:alpine

  sqli:
    build:
      context: .
      dockerfile: Dockerfile.app
    depends_on:
      - postgres
      - redis
    ports:
      - 8080:8080
    command: |
      wait-for postgres:5432 -- python run.py
```

```yaml
version: '3.3'

services:
  postgres:
    build:
      context: .
      dockerfile: Dockerfile.db
    ports:
      - 5432:5432

  redis:
    image: redis:alpine
    read_only: false

  sqli:
    build:
      context: .
      dockerfile: Dockerfile.app
    depends_on:
      - postgres
      - redis
    ports:
      - 8080:8080
    command: |
      wait-for postgres:5432 -- python run.py
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
version: '3.3'

services:
  postgres:
    build:
      context: .
      dockerfile: Dockerfile.db
    ports:
      - 5432:5432

  redis:
    image: redis:alpine
    read_only: true

  sqli:
    build:
      context: .
      dockerfile: Dockerfile.app
    depends_on:
      - postgres
      - redis
    ports:
      - 8080:8080
    command: |
      wait-for postgres:5432 -- python run.py
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 