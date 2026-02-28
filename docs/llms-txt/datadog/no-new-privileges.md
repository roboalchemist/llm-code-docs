# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/no-new-privileges.md

---
title: Avoid privilege escalation via setuid or setgid
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid privilege escalation via setuid or setgid
---

# Avoid privilege escalation via setuid or setgid

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/no-new-privileges`

**Language:** YAML

**Severity:** Warning

**Category:** Security

**CWE**: [732](https://cwe.mitre.org/data/definitions/732.html)

## Description{% #description %}

This rule aims to prevent privilege escalation vulnerabilities in Docker Compose configurations by ensuring that the `no-new-privileges` security option is enabled. Privilege escalation occurs when a container can gain additional rights beyond its intended permissions, potentially compromising the host system or other containers.

Enabling `no-new-privileges: true` in the `security_opt` section of a service ensures that processes inside the container cannot gain new privileges via setuid or setgid binaries. This restriction helps maintain a secure environment by limiting the container's ability to perform unauthorized actions, reducing the attack surface.

To comply with this rule, ensure that your Docker images use the `no-new-privileges` directive like below.

```yaml
security_opt:
  - no-new-privileges:true
```

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
    read_only: true
    security_opt:
      - no-new-privileges: false

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
    security_opt:
      - no-new-privileges: true

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
