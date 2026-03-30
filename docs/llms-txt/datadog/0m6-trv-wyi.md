# Source: https://docs.datadoghq.com/security/default_rules/0m6-trv-wyi.md

---
title: The Azure App Service should be enabled with 'always on'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > The Azure App Service should be enabled
  with 'always on'
---

# The Azure App Service should be enabled with 'always on'

## Description{% #description %}

Azure App Services has 'always on' **enabled** for web apps.

## Rationale{% #rationale %}

Enabling 'always on' will enhance your Azure Apps web apps' availability.

## Remediation{% #remediation %}

### Azure CLI{% #azure-cli %}

1. Get a list of your App Services by running the following in Azure Powershell:

   ```powershell
       az webapp list
    --query '[*].id'

```

1. Check the config of your web apps with the command:

   ```powershell
       az webapp config show
    --ids "<INSERT_ID>"
    --query 'alwaysOn'

```

1. Enable the web app's 'always on' capability with the command:

   ```powershell
       az webapp config set
    --ids "<INSERT_ID>"
    --always-on true

```

1. Repeat steps one through three for each server that is not configured correctly.
