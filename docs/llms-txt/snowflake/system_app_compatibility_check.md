# Source: https://docs.snowflake.com/en/sql-reference/functions/system_app_compatibility_check.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$APP_COMPATIBILITY_CHECK

Returns the [Snowflake edition](../../user-guide/intro-editions.md) of the consumer account
where an app is installed.

> **Note:**
>
> This function can only be called by a Snowflake Native App.

## Syntax

```sqlsyntax
SYSTEM$APP_COMPATIBILITY_CHECK()
```

## Returns

Returns a VARCHAR value containing a JSON object. This object has the following
structure:

```json
{
   "ACCOUNT_EDITION": "<service_level>"
}
```

Possible values for `service_level` are:

* `STANDARD`
* `PREMIER`
* `PREMIER_PLUS_1`
* `PREMIER_PLUS_2`
* `ENTERPRISE`
* `BUSINESS_CRITICAL`
* `VPS`

## Usage notes

* Providers can use this function to determine the Snowflake edition of the account where
  the app is installed. For example, providers can call this function from the setup script
  to check for the edition during installation.

## Examples

Determine the Snowflake edition for a consumer account:

```sqlexample
SELECT SYSTEM$APP_COMPATIBILITY_CHECK();
```

```json
{
  "ACCOUNT_EDITION": "STANDARD"
}
```

This indicates that the consumer account is a Standard Edition account.
