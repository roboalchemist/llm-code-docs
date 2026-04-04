# Source: https://docs.snowflake.com/en/sql-reference/sql/show-pricing-plans.md

# SHOW PRICING PLANS

Lists visible and hidden [pricing plans](../../user-guide/collaboration/listings/pricing-plans-offers/pricing-plans-and-offers.md).

## Syntax

```sqlsyntax
SHOW PRICING PLANS [ LIKE '<pattern>' ] IN LISTING <listing>
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
:   The listing associated with the pricing plan you want shown.

## Output

The command output provides pricing plan properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `name` | The pricing plan display name. |
| `state` | Pricing plan status, one of:   *DRAFT* PUBLISHED * RETIRED |
| `display_name` | The pricing plan name visible to providers. |
| `currency` | The pricing plan currency code. |
| `pricing_model` | The pricing plan pricing model, one of:   *FLAT_FEE* USAGE_BASED |
| `usage_details` | The pricing plan usage details. |
| `base_fee` | The pricing plan base fee. |
| `billing_duration_months` | The pricing plan billing duration in months. |
| `sales_motion` | The pricing plan sales method, one of:   *SELF_SERVE* TALK_TO_SALES |
| `comment` | Comments about the pricing plan added by the provider. |
| `metadata` | The pricing plan metadata added by the provider. |
| `visibility` | The pricing plan visibility, one of:   *VISIBLE* HIDDEN |
| `contract_type` | The pricing plan contract type, one of:   *SUBSCRIPTION* LIMITED_TIME |
| `contract_duration_months` | The pricing plan duration in months. |
| `updated_on` | The date and time the pricing plan was last updated. |

## Usage notes

* You can show a pricing plan only if the listing exists and has a DRAFT or PUBLISHED status.
* You can show a pricing plan only if you use a role that has the [Global CREATE LISTING privilege](../../user-guide/data-exchange-marketplace-privileges.md).

## Examples

Show all the pricing plans with names that start with `mypricingplan` in listing `mylisting`:

```sqlexample
SHOW PRICING PLANS LIKE 'MYPRICINGPLAN%' IN LISTING 'MYLISTING';
```
