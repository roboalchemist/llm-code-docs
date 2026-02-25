# Source: https://docs.datadoghq.com/security/default_rules/def-000-6cs.md

---
title: Azure App Service should have authentication enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure App Service should have
  authentication enabled
---

# Azure App Service should have authentication enabled

## Description{% #description %}

Azure App Service Authentication is a powerful feature that prevents anonymous HTTP requests from reaching your app and allows authentication before reaching app APIs. It offers customizable options for identity providers or custom authentication mechanisms. Enabling this feature ensures that all incoming HTTP requests go through the authentication process, handling user authentication, token validation, storage, and session management. Note that it should only be enabled for app services that require authentication, as it increases costs and requires additional security components.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Login to [Azure Portal](https://portal.azure.com).
1. Go to App Services
1. Click on each App
1. Under Setting section, click on Authentication / Authorization
1. Set App Service Authentication to On
1. Choose other parameters as per your requirement and click Save

**Note**: An IDP needs to be setup for the settings in step 4 to show in the console.

### From the command line{% #from-the-command-line %}

To set App Service Authentication for an existing app, run the following command:

```
az webapp auth update --resource-group <RESOURCE_GROUP_NAME> --name <APP_NAME> --enabled true
```

## References{% #references %}

1. [Authentication and authorization in Azure App Service and Azure Functions](https://docs.microsoft.com/en-us/azure/app-service/app-service-authentication-overview)
1. [Built in Roles: Website Contributor](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#website-contributor)
1. [PA-5: Automate entitlement management](https://docs.microsoft.com/en-us/azure/security/benchmarks/)
1. [GS-6: Define identity and privileged access strategy](https://docs.microsoft.com/en-us/azure/security/benchmarks/security-controls-v2-governance-strategy#gs-6-define-identity-and-privileged-access-strategy)

**Additional Information**: You're not required to use App Service for authentication and authorization. Many web frameworks are bundled with security features, and you can use them instead. If you need more flexibility than App Service provides, you can also write your own utilities. Secure authentication and authorization require deep understanding of security, including federation, encryption, JSON web tokens (JWT) management, grant types, etc.
