# Source: https://docs.datadoghq.com/developers/authorization.md

---
title: Authorization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Developers > Authorization
---

# Authorization

## Overview{% #overview %}

Datadog uses the [OAuth 2.0 (OAuth2) Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749) to allow users to securely authorize third-party applications' access to restricted Datadog resources on behalf of the user. The access that applications have is determined by [scopes](https://docs.datadoghq.com/api/latest/scopes/), which enable users to grant explicit consent for a specific set of granular permissions requested by the application.

## Clients and credentials{% #clients-and-credentials %}

An OAuth2 client is the component of an application that enables users to authorize the application access to Datadog resources on the user's behalf. OAuth2 defines two types of clients: public and [confidential](https://datatracker.ietf.org/doc/html/rfc6749#section-3.2.1).

{% dl %}

{% dt %}
Public Clients
{% /dt %}

{% dd %}
Typically used for browser-based applications and are not capable of storing confidential information.
{% /dd %}

{% /dl %}

{% dl %}

{% dt %}
Confidential Clients
{% /dt %}

{% dd %}
Capable of storing sensitive data and requires an additional `client_secret` to make authorization requests. OAuth clients for integrations are confidential clients.
{% /dd %}

{% /dl %}

When you create an OAuth client, a set of client credentials is issued in the form of a client ID, and optionally, a client secret for confidential clients.

{% dl %}

{% dt %}
Client ID
{% /dt %}

{% dd %}
Used to identify your client when making requests to the authorization and token endpoints.
{% /dd %}

{% dt %}
Client Secret
{% /dt %}

{% dd %}
If issued, used to authenticate the client when making requests to the authorization endpoints. Immediately copy and store the client secret securely as it is a confidential password exposed only once upon client creation.
{% /dd %}

{% /dl %}

## Further Reading{% #further-reading %}

- [Authorize your Datadog integrations with OAuth](https://www.datadoghq.com/blog/oauth/)
- [Implement OAuth for your API-based integration](https://docs.datadoghq.com/developers/integrations/api_integration)
- [Learn more about OAuth2 in Datadog](https://docs.datadoghq.com/developers/authorization/oauth2_in_datadog/)
- [OAuth2 Authorization Endpoints Reference](https://docs.datadoghq.com/developers/authorization/oauth2_endpoints)
