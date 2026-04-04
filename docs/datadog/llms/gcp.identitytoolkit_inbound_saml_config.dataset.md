# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.identitytoolkit_inbound_saml_config.dataset.md

---
title: Identity Platform Inbound SAML Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Identity Platform Inbound SAML
  Configuration
---

# Identity Platform Inbound SAML Configuration

Identity Platform Inbound SAML Configuration in Google Cloud allows you to set up and manage SAML-based single sign-on for your applications. It defines how external identity providers authenticate users and how assertions are mapped to user accounts in Identity Platform. This configuration enables secure federation and centralized identity management across multiple systems.

```gdscript3
gcp.identitytoolkit_inbound_saml_config
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| enabled              | core | bool          | True if allows the user to sign in with the provider.                                                                                                                         |
| gcp_display_name     | core | string        | The config's display name set by developers.                                                                                                                                  |
| idp_config           | core | json          | The SAML IdP (Identity Provider) configuration when the project acts as the relying party.                                                                                    |
| labels               | core | array<string> |
| name                 | core | string        | The name of the InboundSamlConfig resource, for example: 'projects/my-awesome-project/inboundSamlConfigs/my-config-id'. Ignored during create requests.                       |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| sp_config            | core | json          | The SAML SP (Service Provider) configuration when the project acts as the relying party to receive and accept an authentication assertion issued by a SAML identity provider. |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
