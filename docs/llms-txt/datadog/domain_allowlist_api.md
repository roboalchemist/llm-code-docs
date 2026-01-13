# Source: https://docs.datadoghq.com/account_management/org_settings/domain_allowlist_api.md

---
title: Domain Allowlist API
description: >-
  How to use the API to configure domain allowlist settings to restrict email
  domains that can receive Datadog notifications for monitor and scheduled
  reports.
breadcrumbs: Docs > Account Management > Domain Allowlist API
source_url: https://docs.datadoghq.com/org_settings/domain_allowlist_api/index.html
---

# Domain Allowlist API

{% callout %}
##### Get Started with Domain Allowlist

Domain Allowlist is available for customers with Enterprise plans. If you're interested in this feature, contact Datadog support to request access.

[Request Access](https://docs.datadoghq.com/help/)
{% /callout %}

[Domain Allowlist](https://docs.datadoghq.com/account_management/org_settings/domain_allowlist) enables you to restrict the email domains to which notifications can be sent.

This document describes how to access and configure Domain Allowlist through the API. To use the UI instead, see [Domain Allowlist](https://docs.datadoghq.com/account_management/org_settings/domain_allowlist).

## Get Domain Allowlist{% #get-domain-allowlist %}

Return the Domain Allowlist and its enabled or disabled state.

GET [https://api.datadoghq.com/api/v2/domain_allowlist](https://api.datadoghq.com/api/v2/domain_allowlist)

### Request{% #request %}

#### Example{% #example %}

```bash
curl -X GET "https://api.datadoghq.com/api/v2/domain_allowlist" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
```

### Response{% #response %}

{% tab title="200" %}
OK

#### Model{% #model %}

| Field                   | Type     | Description                                                                                  |
| ----------------------- | -------- | -------------------------------------------------------------------------------------------- |
| data                    | object   | Domain Allowlist email data                                                                  |
| data.type               | enum     | Domain Allowlist type. Allowed enum values: `domain_allowlist`. Default: `domain_allowlist`. |
| data.attributes         | object   | Attributes of Domain Allowlist                                                               |
| data.attributes.enabled | Boolean  | If `true`, Domain Allowlist is enabled                                                       |
| data.attributes.domains | [string] | List of domains in Domain Allowlist                                                          |

{% /tab %}

{% tab title="403" %}
Forbidden

#### Model{% #model %}

| Field               | Type     | Description    |
| ------------------- | -------- | -------------- |
| errors [*required*] | [string] | List of errors |

{% /tab %}

{% tab title="404" %}
Not Found

#### Model{% #model %}

| Field               | Type     | Description    |
| ------------------- | -------- | -------------- |
| errors [*required*] | [string] | List of errors |

{% /tab %}

{% tab title="429" %}
Too many requests

#### Model{% #model %}

| Field               | Type     | Description    |
| ------------------- | -------- | -------------- |
| errors [*required*] | [string] | List of errors |

{% /tab %}

#### Example{% #example-1 %}

```js
{
  "data": {
    "type": "domain_allowlist",
    "attributes": {
      "enabled": true,
      "domains": [
        "@aol.com",
        "@yahoo.com",
        "@gmail.com"
      ]
    }
  }
}
```

## Modify Domain Allowlist{% #modify-domain-allowlist %}

Enable/disable Domain Allowlist and rewrite the entire allowlist with a given list of email domains.

PATCH [https://api.datadoghq.com/api/v2/domain_allowlist](https://api.datadoghq.com/api/v2/domain_allowlist)

### Request{% #request-1 %}

#### Example{% #example-2 %}

```bash
curl -X PATCH "https://api.datadog.com/api/v2/domain_allowlist" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF

{
  "data": {
    "type": "domain_allowlist",
    "attributes": {
      "enabled": true,
      "domains": [
        "@datadoghq.com",
        "@yahoo.com",
        "@gmail.com"
      ]
    }
  }
}

EOF
```

### Response{% #response-1 %}

{% tab title="200" %}
OK

#### Model{% #model %}

| Field                   | Type     | Description                                                                                  |
| ----------------------- | -------- | -------------------------------------------------------------------------------------------- |
| data                    | object   | Domain Allowlist email data                                                                  |
| data.type               | enum     | Domain Allowlist type. Allowed enum values: `domain_allowlist`. Default: `domain_allowlist`. |
| data.attributes         | object   | Attributes of Domain Allowlist                                                               |
| data.attributes.enabled | Boolean  | If `true`, Domain Allowlist is enabled                                                       |
| data.attributes.domains | [string] | List of domains in Domain Allowlist                                                          |

{% /tab %}

{% tab title="403" %}
Forbidden

#### Model{% #model %}

| Field               | Type     | Description    |
| ------------------- | -------- | -------------- |
| errors [*required*] | [string] | List of errors |

{% /tab %}

{% tab title="404" %}
Not Found

#### Model{% #model %}

| Field               | Type     | Description    |
| ------------------- | -------- | -------------- |
| errors [*required*] | [string] | List of errors |

{% /tab %}

{% tab title="429" %}
Too many requests

#### Model{% #model %}

| Field               | Type     | Description    |
| ------------------- | -------- | -------------- |
| errors [*required*] | [string] | List of errors |

{% /tab %}

#### Example{% #example-3 %}

```js
{
  "data": {
    "type": "domain_allowlist",
    "attributes": {
      "enabled": true,
      "domains": [
        "@datadoghq.com",
        "@yahoo.com",
        "@gmail.com"
      ]
    }
  }
}
```

## Further Reading{% #further-reading %}

- [Domain Allowlist](https://app.datadoghq.com/organization-settings/domain-allowlist)
- [Domain Allowlist UI](https://docs.datadoghq.com/account_management/org_settings/domain_allowlist)
