# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/missing-helmet.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/missing-helmet.md

---
title: Express application should use Helmet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Express application should use Helmet
---

# Express application should use Helmet

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-express/missing-helmet`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [693](https://cwe.mitre.org/data/definitions/693.html)

## Description{% #description %}

Per [Express documentation](https://expressjs.com/en/advanced/best-practice-security.html#use-helmet):

[Helmet](https://helmetjs.github.io/) can help protect your app from some well-known web vulnerabilities by setting HTTP headers appropriately.

This rule will check whether you've set `app.use(helmet())` within the file that you've called `express()`

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
import express from 'express';
import helmet from 'helmet';


const MyController = express();

MyController.listen(8000);
```

```javascript
const express = require("express")

const app = express();

// no `app.use(helmet())` helmet detected in the file

app.get("/foo", (req, res) => res.send("foo"));

app.listen(8000);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
import express from 'express';
import helmet from 'helmet';



const MyController = express();
MyController.use(helmet());

MyController.listen(8000);
```

```javascript
const express = require("express")
const helmet = require("helmet")

const app = express();

app.use(json()); // helmet detected
app.use(helmet()); // helmet detected

app.get("/foo", (req, res) => res.send("foo"));

app.listen(8000);
```

```javascript
import express from "express"
import helmet from "helmet"

const app = express();

app.use(helmet()); // helmet detected

app.get("/foo", (req, res) => res.send("foo"));

app.listen(8000);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
