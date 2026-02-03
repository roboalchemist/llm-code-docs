# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/laravel-native-sql-injection.md

---
title: Prevent native SQL injections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent native SQL injections
---

# Prevent native SQL injections

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/laravel-native-sql-injection`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [89](https://cwe.mitre.org/data/definitions/89.html)

## Description{% #description %}

SQL injection is a code injection technique that attackers use to exploit vulnerabilities in a web application's database layer. This can lead to unauthorized access, data theft, data loss, and even loss of control over the server.

SQL injection vulnerabilities are among the most common and most harmful security flaws in web applications. These vulnerabilities can lead to severe consequences, including data breaches and unauthorized access to sensitive data.

Do not concatenate strings to form SQL queries; instead, use parameterized queries or prepared statements. Concatenating strings can lead to SQL injection if the inputs are not properly sanitized.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
class UserController extends Controller
{
  public function show($userId) {
    $query = 'SELECT * FROM users WHERE id = ' . $userId;
    $result = dbx_query($connection, $query);
    return view('user.show', ['users' => $result]);
  }

  public function display($userId) {
    $connection = db2_connect($dbName, $dbUser, $dbPass);
    $sql = 'SELECT * FROM users WHERE id = ' . $userId;
    $result = db2_exec($connection, $sql);
    return view('user.show', ['users' => $result]);
  }

  public function findByEmail($email) {
    $query = 'SELECT * FROM users WHERE email = ' . $email;
    $result = mysql_unbuffered_query($query, $connection);
    return view('user.show', ['users' => $result]);
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
class UserController extends Controller
{
  public function show($userId) {
    $result = DB::table('users')->where('id', $userId)->get();
    return view('user.show', ['users' => $result]);
  }

  public function display($userId) {
    $connection = db2_connect($dbName, $dbUser, $dbPass);
    $sql = 'SELECT * FROM users WHERE id = ?';
    $stmt = db2_prepare($connection, $sql);
    db2_bind_param($stmt, 1, "userId", DB2_PARAM_IN);
    db2_execute($stmt);
    $result = db2_fetch_assoc($stmt);
    return view('user.show', ['users' => $result]);
  }

  public function findByEmail($email) {
    $result = DB::table('users')->where('email', $email)->get();
    return view('user.show', ['users' => $result]);
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 