# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_purchase_attributes.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_PURCHASE_ATTRIBUTES

Identifies the behavior of a listing at runtime.

## Syntax

```sqlsyntax
SYSTEM$GET_PURCHASE_ATTRIBUTES()
```

## Arguments

None

## Returns

The function returns a value of type VARCHAR.

The returned string is in JSON format and contains the following name/value pairs:

`pricing_plan_identifier`
:   The identifier for the pricing plan associated with the listing.

`discount`
:   The pricing plan discount.

`offer_name`
:   The name of the private offer associated with the listing.

## Examples

```sqlexample
SELECT SYSTEM$GET_PURCHASE_ATTRIBUTES();
```

```output
+-----------------------------------------------------------------------------------------+
| SYSTEM$GET_PURCHASE_ATTRIBUTES()                                                        |
|-----------------------------------------------------------------------------------------|
| {"pricing_plan_identifier":"TESTPLAN","discount":10.0,"offer_name":"TESTOFFER_WELE_RO"} |
+-----------------------------------------------------------------------------------------+
```
