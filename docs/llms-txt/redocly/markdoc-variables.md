# Source: https://redocly.com/docs/realm/customization/markdoc-variables.md

# Markdoc variables

Markdoc variables allow you to access dynamic data in your Markdoc content.
This reference documents the available variables and their usage.

## Available variables

| Variable | Description |
|  --- | --- |
| `$rbac.teams` | Array of RBAC teams the user belongs to |
| `$user.email` | User's email address |
| `$user.authCookie` | User's authentication cookie |
| `$user.{claim}` | Other user claims from the Identity Provider (IdP) |
| `$idpAccessToken` | User's access token |
| `$lang` | Current page locale ID from the config or `default_locale` if i18n is not configured |
| `$frontmatter.{property}` | Access properties defined in the page's front matter |
| `$env.{name}` | Access environment variables |


## Usage examples

### Display the user email

Use variables within your Markdoc content:


```md
Welcome, {% default($user.email, "Redocker") %}!
```

Result:

> Welcome, !


### Dump the RBAC details

Dump the `$rbac` contents to troubleshoot RBAC issues:


```md
{% $rbac %}
```

Result:



## Data structure examples

### $rbac


```json
{
  "teams": [
    "sample",
    "authenticated"
  ]
}
```

### $user

The structure of `$user` depends on your Identity Provider (IdP). Here's an example:


```json
{
  "at_hash": "0194_mIut36l1RvlemrfUA",
  "aud": ["41e74d64-6b6b-44b5-8779-28df7aa3cce6"],
  "auth_time": 1747025292,
  "email": "smile@example.com",
  "exp": 1747032494,
  "firstName": "Smile",
  "https://redocly.com/auth/aud": [
    "redocly"
  ],
  "https://redocly.com/sso/teams": [
    "sample",
    "authenticated"
  ],
  "iat": 1747025293,
  "id": "usr_00h4e3haae4mtb50gtn497n93d",
  "iss": "https://auth.cloud.redocly.com/oidc",
  "jti": "74a7518b-e05e-417f-9931-94b523237212",
  "lastName": "Example",
  "loginSource": "sso",
  "providerId": "idp_01h4dygdnk9veyr4wzkkf9824m",
  "rat": 1747025291,
  "sessionId": "a6bbb5cb-4fc5-40e1-901a-9d104264f708",
  "sid": "a6bbb5cb-4fc5-40e1-901a-9d104264f708",
  "sub": "idp_01h4dygdnk9veyr4wzkkf9978m__smile@example.com",
  "idpId": "oidc",
  "teams": [
    "sample",
    "authenticated"
  ],
  "name": "smile@example.com",
  "authCookie": "[auth cookie value]"
}
```

### $idpAccessToken


```md
"ory_at_CcByTgsW7q......"
```

### $lang


```md
"default_locale"
```

### $frontmatter

Access properties defined in the front matter of the current page:


```md example.md
---
title: Getting Started
description: Learn how to use our product
author: Redocly Team
---

# {% $frontmatter.title %}

By {% $frontmatter.author %}
```

### $env

Access [environment variables](/docs/realm/reunite/project/env-variables) that have been exposed to the Markdoc renderer.

Usage example: `{% $env.PUBLIC_REDOCLY_BRANCH_NAME %}`