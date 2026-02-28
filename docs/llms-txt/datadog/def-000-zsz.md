# Source: https://docs.datadoghq.com/security/default_rules/def-000-zsz.md

---
title: Verify Root Has A Primary GID 0
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Root Has A Primary GID 0
---

# Verify Root Has A Primary GID 0

## Description{% #description %}

The `root` user should have a primary group of 0.

## Rationale{% #rationale %}

To help ensure that root-owned files are not inadvertently exposed to other users.
