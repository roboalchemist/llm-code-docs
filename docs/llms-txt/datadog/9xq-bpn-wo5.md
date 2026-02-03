# Source: https://docs.datadoghq.com/security/default_rules/9xq-bpn-wo5.md

---
title: Azure App Service should have remote debugging disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure App Service should have remote
  debugging disabled
---

# Azure App Service should have remote debugging disabled
 
## Description{% #description %}

Azure App Services has 'remote debugging' **disabled** to enhance security and protect applications.

## Rationale{% #rationale %}

If [remote debugging](https://devblogs.microsoft.com/premier-developer/remote-debugging-azure-app-services/) is enabled, this can allow an attacker access to your applications. To reduce your attack surface, disable remote debugging when not actively needed.

## Remediation{% #remediation %}

### Azure CLI{% #azure-cli %}

1. Get a list of your App Services web apps by running the following in Azure Powershell:

   ```
   az webapp list \
   --query '[*].id'
   ```

1. Check the config of your web apps with the command:

   ```
   az webapp config show \
   --ids "<INSERT_ID_HERE>" \
   --query 'remoteDebuggingEnabled'
   ```

1. Disable the web app's remote debugging capability with the command:

   ```
   az webapp config set \
   --ids "<INSERT_ID_HERE>" \
   --remote-debugging-enabled false
   ```

1. Repeat steps one through three for each server that is not configured correctly.

## References{% #references %}

1. [Azure webapp config set](https://learn.microsoft.com/en-us/cli/azure/webapp/config?view=azure-cli-latest#az-webapp-config-set)
