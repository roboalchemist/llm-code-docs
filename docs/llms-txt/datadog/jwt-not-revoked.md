# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/jwt-not-revoked.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/jwt-not-revoked.md

---
title: Ensure an isRevoked method is used for tokens
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure an isRevoked method is used for tokens
---

# Ensure an isRevoked method is used for tokens

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-express/jwt-not-revoked`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [525](https://cwe.mitre.org/data/definitions/525.html)

## Description{% #description %}

Consider a method to revoke JWTs, especially when they contain sensitive information, to ensure they remain short-lived.

#### Learn More{% #learn-more %}

- [ExpressJWT revoking documentation](https://github.com/auth0/express-jwt#revoked-tokens)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const { expressjwt: jwt } = require("express-jwt")

app.get(
  "/protected",
  jwt({
    secret: "shhhhhhared-secret",
    algorithms: ["HS256"]
  }),
  function (req, res) {
    if (!req.auth.admin) return res.sendStatus(401);
    res.sendStatus(200);
  }
);
```

```javascript
import { expressjwt } from "express-jwt";

app.get(
  "/protected",
  expressjwt({
    secret: "shhhhhhared-secret",
    algorithms: ["HS256"],
  }),
  function (req, res) {
    if (!req.auth.admin) return res.sendStatus(401);
    res.sendStatus(200);
  }
);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const { expressjwt } = require("express-jwt")

app.get(
  "/protected",
  expressjwt({
    secret: "shhhhhhared-secret",
    algorithms: ["HS256"],
    isRevoked: isRevokedCallback,
  }),
  function (req, res) {
    if (!req.auth.admin) return res.sendStatus(401);
    res.sendStatus(200);
  }
);
```

```javascript
import { expressjwt as jwt } from "express-jwt";

app.get(
  "/protected",
  jwt({
    secret: "shhhhhhared-secret",
    algorithms: ["HS256"],
    isRevoked: isRevokedCallback,
  }),
  function (req, res) {
    if (!req.auth.admin) return res.sendStatus(401);
    res.sendStatus(200);
  }
);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
