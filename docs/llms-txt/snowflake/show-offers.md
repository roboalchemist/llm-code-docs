# Source: https://docs.snowflake.com/en/sql-reference/sql/show-offers.md

# SHOW OFFERS

Provides information about all [offers](../../user-guide/collaboration/listings/pricing-plans-offers/pricing-plans-and-offers.md) added to a listing.

## Syntax

```sqlsyntax
SHOW OFFERS [ LIKE '<pattern>' ] IN LISTING <listing>
```

## Parameters

`LIKE 'pattern'`
:   Optionally filters the command output by object name. The filter uses case-insensitive pattern matching, with support for SQL
    wildcard characters (`%` and `_`).

    For example, the following patterns return the same results:

    `... LIKE '%testing%' ...`

    `... LIKE '%TESTING%' ...`

    . Default: No value (no filtering is applied to the output).

`IN LISTING listing`
:   The listing associated with the offer you want shown.

## Output

The command output provides offer properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `name` | The offer name. |
| `state` | Offer status, one of:   *DRAFT* PUBLISHED * WITHDRAWN |
| `state_updated_on` | The date and time the offer state was last updated. |
| `access_start_date_preference` | The preferred date for consumer listing access, one of:   *OFFER_ACCEPTED_DATE* SPECIFIC_DATE |
| `comment` | Comments about the offer added by the provider. |
| `contract_value` | The total contract value. |
| `contract_type` | The contract type, one of:   *SUBSCRIPTION* LIMITED_TIME * PAY_AS_YOU_GO |
| `contract_duration_months` | The contract duration in months. |
| `invoice_start_date_preference` | The preferred invoicing start date, one of:   *OFFER_ACCEPTED_DATE* SPECIFIC_DATE * FIRST_DAY_NEXT_MONTH |
| `invoice_start_time` | The date and time invoicing started. |
| `is_default` | Specifies a default offer is included with the pricing plan, one of:   *TRUE* FALSE (default) |
| `display_name` | The offer name visible to consumers. |
| `expiration_time` | The date and time the offer expires. |
| `payment_terms` | Additional pricing plan parameters, one of:   *PAYMENT_TYPE* INSTALLMENT_SCHEDULE * ALLOWED_PAYMENT_METHODS |
| `pricing_plan_name` | The pricing plan associated with the offer. |
| `access_end_time` | The date and time consumers lose access to the listing. |
| `access_start_time` | The date and time consumers can access the listing. |
| `discount` | The offer discount. |
| `target_consumer` | The consumer the offer targets. |
| `terms_of_service` | The terms of service associated with the offer. |
| `additional_information` | Additional information about the offer. |
| `updated_on` | The date the offer was last updated. |

## Access control requirements

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE LISTING | Account | Only the ACCOUNTADMIN role has this privilege by default. The privilege can be granted to additional roles as needed. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Examples

Show all the offers with names that start with `myoffer` in `mylisting`:

```sqlexample
SHOW OFFERS LIKE 'MYOFFER%' IN LISTING MYLISTING;
```
