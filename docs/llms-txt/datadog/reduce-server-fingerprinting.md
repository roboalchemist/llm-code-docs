# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/reduce-server-fingerprinting.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/reduce-server-fingerprinting.md

---
title: Server fingerprinting misconfiguration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Server fingerprinting misconfiguration
---

# Server fingerprinting misconfiguration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-express/reduce-server-fingerprinting`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [693](https://cwe.mitre.org/data/definitions/693.html)

## Description{% #description %}

Improve your overall server security by taking the step to reduce the likelihood of server fingerprinting the software being used on the server.

By default, Express.js sends the `X-Powered-By` response header banner which can be disabled with `app.disable('X-Powered-By')`.

If you're using `helmet`, you can use either of these methods too:

- `app.use(helmet())`
- `app.use(hidePoweredBy())`
- `app.use(helmet.hidePoweredBy())`

#### Learn More{% #learn-more %}

- [Express Security Best Practices](https://expressjs.com/en/advanced/best-practice-security.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const app = express()

// express() is called but none of the following were detected afterwards
// app.disable('x-powered-by')
// app.use(hidePoweredBy())
// app.use(helmet.hidePoweredBy())
// app.use(helmet())
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const app = express()

app.use(helmet());

// rest of your config
```

```javascript
const app = express()

app.use(helmet.hidePoweredBy());

// rest of your config
```

```javascript
const app = express()

app.use(hidePoweredBy())

// rest of your config
```

```javascript
const app = express()

app.disable('x-powered-by')

// rest of your config
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 