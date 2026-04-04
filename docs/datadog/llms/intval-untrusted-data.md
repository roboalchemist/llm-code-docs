# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/intval-untrusted-data.md

---
title: Do not call intval on untrusted user data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not call intval on untrusted user data
---

# Do not call intval on untrusted user data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/intval-untrusted-data`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [95](https://cwe.mitre.org/data/definitions/95.html)

## Description{% #description %}

The `intval()` function converts a value into an integer without any validation or sanitation, potentially leading to some problematic logic bugs such as an incorrect SQL query or other forms of data manipulation.

When it receives a non-numeric value, the `intval()` function returns `0` or `1` instead of returning an error. Passing untrusted user-provided data to this function can lead to unexpected and potentially harmful results if the data includes malicious or incorrect input.

To avoid breaking this rule, always validate and sanitize user input before using it. You can use PHP's built-in functions like `isset()`, `is_numeric()`, and others to validate the input. Following these best practices will help you write more secure PHP code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
// Insecure: Directly using intval() on untrusted data from $_GET
$id = intval($_GET['id']);

$query = "SELECT * FROM users WHERE id = $id";
$result = mysqli_query($conn, $query);

// Insecure: Directly using intval() on untrusted data from $_POST
$quantity = intval($_POST['quantity']);

// Insecure: Directly using intval() on untrusted data from $_FILES
$fileSize = intval($_FILES['uploadedFile']['size']);

// Using the $fileSize variable in a condition
if ($fileSize > 1048576) { // Check if the file size is greater than 1MB
    echo "File is too large.";
} else {
    // Proceed with the file upload
}
?>
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
// Secure: Validate and sanitize user input
$id = isset($_GET['id']) && is_numeric($_GET['id']) ? intval($_GET['id']) : 0;

$stmt = $conn->prepare("SELECT * FROM users WHERE id = ?");
$stmt->bind_param("i", $id);
$stmt->execute();
$result = $stmt->get_result();

// Secure: Validate and sanitize user input
$quantity = isset($_POST['quantity']) && is_numeric($_POST['quantity']) ? intval($_POST['quantity']) : 0;

// Secure: Validate and sanitize file size
$fileSize = isset($_FILES['uploadedFile']['size']) && is_numeric($_FILES['uploadedFile']['size']) ? intval($_FILES['uploadedFile']['size']) : 0;

// Validate file size and type
$maxFileSize = 1048576; // 1MB
$allowedTypes = ['image/jpeg', 'image/png'];

if ($fileSize > 0 && $fileSize <= $maxFileSize && in_array($_FILES['uploadedFile']['type'], $allowedTypes)) {
    // Proceed with the file upload
    $uploadDir = 'uploads/';
    $uploadFile = $uploadDir . basename($_FILES['uploadedFile']['name']);

    if (move_uploaded_file($_FILES['uploadedFile']['tmp_name'], $uploadFile)) {
        echo "File uploaded successfully!";
    } else {
        echo "File upload failed.";
    }
} else {
    echo "Invalid file.";
}
?>
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
