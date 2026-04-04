# Source: https://docs.datadoghq.com/security/default_rules/def-000-k0t.md

---
title: Service exposes publicly debugging endpoints
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Service exposes publicly debugging
  endpoints
---

# Service exposes publicly debugging endpoints

## Description{% #description %}

This API exposes a debug endpoint in a production environment. Frameworks sometimes expose debugging features that are helpful during development. However, those features could be abused by attackers and should be disabled before being deployed to production.

Datadog's supported framework ecosystem is continually evolving. The following list provides a sample:

- [JAVA Spring Boot's Actuators](https://docs.spring.io/spring-boot/reference/actuator/endpoints.html)
- [PHP Laravel's Telescope](https://laravel.com/docs/11.x/telescope)
- [PHP Symfony's Profiler](https://symfony.com/doc/current/profiler.html)
- [PHP Cakephp's Debugkit](https://book.cakephp.org/debugkit/4/en/index.html)

## Rationale{% #rationale %}

This finding works by identifying an endpoint responding with `200` status codes to requests to known debugging endpoints. Debugging endpoints in production can lead to security breaches by exposing sensitive data and application internals.

## Remediation{% #remediation %}

- Disable debug endpoints in production. The method varies based on the debugging tool being used; examples are provided for illustration purposes:

  - JAVA Actuators settings are set in the `application.properties` configuration file by specifying `management.endpoints.web.exposure.include=[]` (see the [documentation](https://docs.spring.io/spring-boot/appendix/application-properties/index.html) for more information). Be aware that in certain configurations, these settings can monitor and access application metrics, so it is advisable to restrict access to these endpoints.

  - In PHP frameworks, it is common to install the package as a development dependency using the `--dev` flag to prevent the feature from being added in the production release. For example: `composer require laravel/telescope --dev`.
