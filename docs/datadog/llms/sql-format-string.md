# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/sql-format-string.md

---
title: Avoid manually built SQL queries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid manually built SQL queries
---

# Avoid manually built SQL queries

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/sql-format-string`

**Language:** Go

**Severity:** Error

**Category:** Security

## Description{% #description %}

Queries vulnerable to SQL injection should be avoided.

Consider this code snippet:

```go
func main () {
    q := fmt.Sprintf("SELECT * FROM users where name = '%s'", username)
    rows, err := db.Query(q)
}
```

In this code snippet, the SQL query is dynamically constructed by directly injecting the `username` variable into the query string using string concatenation. This approach is dangerous because it allows an attacker to manipulate the value of `username` and potentially execute malicious SQL commands.

For example, if an attacker sets the `username` value to `'; DROP TABLE users;--`, the resulting constructed query will be:

```go
SELECT * FROM users where name = ''; DROP TABLE users;--
```

This will result in the execution of two separate SQL statements: the first statement will retrieve all user records, and the second statement will drop the entire `users` table from the database.

To avoid SQL injection vulnerabilities, it is essential to use parameterized queries or prepared statements. These techniques separate the SQL query from user-supplied input and ensure that the input is treated only as data, not as executable SQL code.

Here's an example of how the above code can be modified to use parameterized queries:

```go
func main() {
    q := "SELECT * FROM users WHERE name = ?"
    rows, err := db.Query(q, username)
}
```

By using the `?` placeholder in the SQL query and passing the `username` variable as a query parameter, the database driver takes care of properly escaping the input and preventing SQL injection attacks.

By following best practices and using parameterized queries or prepared statements, you can ensure the security and integrity of your database operations.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func (p *Profile) UnsafeQueryGetData(uid string) error {

   /* this funciton use to get data Profile from database with vulnerable query */
   DB, err = database.Connect()

   getProfileSql := fmt.Sprintf(`UPDATE users set name=%s`, uid) //here is the vulnerable query
   rows, err := DB.Query(getProfileSql)
   if err != nil {
      return err //this will return error query to clien hmmmm.
   }
   defer rows.Close()
   //var profile = Profile{}
   for rows.Next() {
      err = rows.Scan(&p.Uid, &p.Name, &p.City, &p.PhoneNumber)
      if err != nil {
         log.Printf("Row scan error: %s", err.Error())
         return err
      }
   }
   return nil
}
```

```go
func (p *Profile) UnsafeQueryGetData(uid string) error {

   /* this funciton use to get data Profile from database with vulnerable query */
   DB, err = database.Connect()

   getProfileSql := fmt.Sprintf(`SELECT p.user_id, p.full_name, p.city, p.phone_number
                        FROM Profile as p,Users as u
                        where p.user_id = u.id
                        and u.id=%s`, uid) //here is the vulnerable query
   rows, err := DB.Query(getProfileSql)
   if err != nil {
      return err //this will return error query to clien hmmmm.
   }
   defer rows.Close()
   //var profile = Profile{}
   for rows.Next() {
      err = rows.Scan(&p.Uid, &p.Name, &p.City, &p.PhoneNumber)
      if err != nil {
         log.Printf("Row scan error: %s", err.Error())
         return err
      }
   }
   return nil
}
```

```go
func main () {
    q := fmt.Sprintf("SELECT * FROM users where name = '%s'", username)
    rows, err := db.Query(q)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func foo () {
    fmt.Sprintf("Failed to update company settings: %v", err),
}
```

```go
func main () {
    q := "SELECT * FROM users where name = 'foobar'"
    rows, err := db.Query(q)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
