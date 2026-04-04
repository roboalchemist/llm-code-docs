# Source: https://docs.snowflake.com/en/sql-reference/billing/partner_contract_items.md

Schema:
:   [BILLING](../billing.md)

# PARTNER_CONTRACT_ITEMS view

The PARTNER_CONTRACT_ITEMS view in the BILLING schema provides contract information for the reseller’s customers.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ORGANIZATION_NAME | VARCHAR | Name of the reseller’s organization. |
| SOLD_TO_ORGANIZATION_NAME | VARCHAR | Name of the organization of the reseller’s customer. |
| SOLD_TO_CUSTOMER_NAME | VARCHAR | Name of the reseller’s customer. |
| SOLD_TO_PO_NUMBER | VARCHAR | Purchase order number associated with the reseller’s sale to the customer. |
| SOLD_TO_CONTRACT_NUMBER | VARCHAR | Number associated with the customer’s contract with the reseller. |
| START_DATE | DATE | Start date for the customer’s contract with the reseller, or the date the CONTRACT_ITEM goes into effect. |
| END_DATE | DATE | End date of the customer’s contract with the reseller. |
| EXPIRATION_DATE | DATE | Expiration date of the customer’s contract with the reseller. |
| CONTRACT_ITEM | VARCHAR | One of capacity, additional capacity, or free usage. |
| CURRENCY | VARCHAR | Currency for the CONTRACT_ITEM. |
| AMOUNT | NUMBER(26,4) | Amount for the CONTRACT_ITEM. |
| CONTRACT_MODIFIED_DATE | DATE | Date (in UTC) the CONTRACT_ITEM was last modified. |

## Usage notes

* Latency for the view can be up to 24 hours.
