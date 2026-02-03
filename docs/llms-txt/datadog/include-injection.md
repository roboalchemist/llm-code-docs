# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/include-injection.md

---
title: Prevent injection through include statements
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent injection through include statements
---

# Prevent injection through include statements

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/include-injection`

**Language:** PHP

**Severity:** Info

**Category:** Best Practices

**CWE**: [78](https://cwe.mitre.org/data/definitions/78.html)

## Description{% #description %}

This rule aims to prevent code injection vulnerabilities that arise from dynamically including files through `include`, `include_once`, `require`, or `require_once` statements. Including files based on untrusted or user-supplied input can lead to arbitrary code execution, allowing attackers to inject malicious scripts into the application.

To avoid violations of this rule, developers should avoid directly using user input in include statements without proper validation or sanitization. Instead, use predefined constants, fixed paths, or whitelist allowed file names. When dynamic paths are necessary, validate them rigorously or use safe abstractions to ensure only intended files are included.

For example, instead of `include($_GET['page']);`, use a mapping of allowed pages or sanitize the input before including: `include(__DIR__ . '/pages/' . basename($_GET['page']) . '.php');`. This approach reduces the risk of injection through include statements.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php

$val = "foo";

function foo($arg) {

    $val = $_GET["getsomevalue"];

    include($val);
}

?>
```

```php
<?php

$val = $_GET["getsomevalue"];

include($val);
include_once($val);
require($val);
require_once($val);
include(__DIR__ . $val);
?>
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php


include('something.php');

include_once('something_else.php');

require('other_stuff.php');

require_once('more_stuff.php');

require_once(CONFIG_DIR . '/mypage.php');

require_once( dirname( __FILE__ ) . '/apage.php' );

$foo = 'foo/bar.php';
require_once $foo;
?>
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 