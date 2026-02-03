# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/extract-untrusted-data.md

---
title: Do not call extract on untrusted user data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not call extract on untrusted user data
---

# Do not call extract on untrusted user data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/extract-untrusted-data`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [95](https://cwe.mitre.org/data/definitions/95.html)

## Description{% #description %}

The `extract()` function in PHP can be used to import variables into the local symbol table from an array. However, using it on untrusted data, such as user input, can lead to a variety of security vulnerabilities, including arbitrary code execution and SQL injection, making it a dangerous practice.

By using `extract()` on untrusted data, you may inadvertently create variables that overwrite important ones, or worse, you could execute harmful code that was injected by a malicious user.

To adhere to this rule, you should explicitly assign and sanitize user input rather than using `extract()`. This will ensure your code remains secure and compliant.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
// Insecure: Using extract() on untrusted data from $_GET
extract($_GET);

echo "Hello, $name!";

// Insecure: Using extract() on untrusted data from $_POST
extract($_POST);

if ($isAdmin) {
    echo "Welcome, admin!";
} else {
    echo "Welcome, user!";
}

// Insecure: Using extract() on untrusted data from $_FILES
extract($_FILES['uploadedFile']);

if (move_uploaded_file($tmp_name, "uploads/$name")) {
    echo "File uploaded successfully!";
} else {
    echo "File upload failed.";
}
?>
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
// Secure: Explicitly assign and sanitize user input
$name = htmlspecialchars($_GET['name'], ENT_QUOTES, 'UTF-8');

echo "Hello, $name!";

// Secure: Explicitly assign and validate user input
$isAdmin = isset($_POST['isAdmin']) && $_POST['isAdmin'] == '1';

if ($isAdmin) {
    echo "Welcome, admin!";
} else {
    echo "Welcome, user!";
}

// Secure: Explicitly handle file upload variables and validate
$file = $_FILES['uploadedFile'];
$uploadDir = 'uploads/';
$uploadFile = $uploadDir . basename($file['name']);

if (move_uploaded_file($file['tmp_name'], $uploadFile)) {
    echo "File uploaded successfully!";
} else {
    echo "File upload failed.";
}
?>
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 