# Source: https://plivo.com/docs/account/concepts/subaccounts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subaccounts

> Segment usage, isolate traffic, and manage multi-tenant architectures

Subaccounts let you create isolated environments under your main Plivo account.

***

## How Subaccounts Work

Each subaccount has:

* Unique Auth ID and Auth Token
* Separate call/message logs
* Independent webhooks

All charges deduct from the parent account balance.

***

## Use Cases

| Use Case                   | Description                                     |
| -------------------------- | ----------------------------------------------- |
| **Multi-tenant SaaS**      | Isolate each customer's traffic and logs        |
| **Reseller/White-label**   | Manage client accounts, track usage for billing |
| **Environment separation** | Separate dev, staging, production               |
| **Department tracking**    | Track usage by business unit                    |

***

## Billing

Subaccounts share the main account's credit balance:

* All charges deduct from main account
* No separate payment methods per subaccount
* Track usage per subaccount via API for client invoicing

***

## Credentials

| Account Type | Auth ID Prefix | Access                          |
| ------------ | -------------- | ------------------------------- |
| Main account | `MA`           | All resources + all subaccounts |
| Subaccount   | `SA`           | Only its own resources          |

Subaccounts cannot access main account or other subaccount resources.

***

## Phone Numbers

* Assign numbers when renting or transfer later
* Each number belongs to one account only
* Numbers transfer to main account when subaccount deleted (unless cascade=true)

***

## Related

* [Subaccount API Reference](/account/api/subaccount)
