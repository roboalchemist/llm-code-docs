# Source: https://www.metabase.com/docs/latest/cloud/how-billing-works

<div>

1.  [Home](/docs/latest/)
2.  [Cloud](/docs/latest/cloud/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.57](/docs/v0.57)
-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# How Metabase billing works

When you sign up for a paid Metabase plan on our website, you can elect to pay in two ways:

-   [Monthly billing](#how-monthly-billing-works)
-   [Annual billing](#how-annual-billing-works) (10% discount)

Both billing frequencies include a flat monthly or annual payment, and bill additional [user accounts](#what-counts-as-a-user-account) each month on a prorated basis (or quarterly, if you're [paying by invoice](#how-invoicing-works-for-pro-plans)).

Companies with large number of users can talk to sales about our [Enterprise plan](/sales/), which includes more options and discounts.

## How monthly billing works

Though we bill you monthly, we calculate how much you owe each day. So, say you're on the [Starter plan](/pricing/). Your monthly bill would include:

-   \$100 flat payment for the month. This payment additionally covers the first five people who use your Metabase that month. If you have fewer than five people using your Metabase, your bill will still be \$100 that month.
-   Each additional person costs \$6, prorated for how many days their [accounts were available](#what-counts-as-a-user-account) that month. So if an account only existed for the last 10 days of your 30 day billing period, you'd only be charged for those 10 days, not for the full 30 days. Same goes if you deactivated an account before the end of the billing period, you'll only be charged for the days when the account was available for use during that billing period. Basically, you only ever pay for all accounts in your Metabase that haven't been deactivated yet.

## How annual billing works

Paying up front for a year will save you 10%. So, again let's use the [Starter plan](/pricing/) as an example. With annual billing, you will:

-   Have an annual payment of \$918. That payment additionally covers five user accounts. This flat payment is made up front; it's not billed monthly. If you have fewer than five accounts, you still pay \$918 for the year.
-   For each additional user account above those first five user accounts, you'll be billed at \$54, prorated for the year. So, for example, if you start out with just the first five accounts that are included in the initial \$918 annual payment, then decide to add another user account six months into your annual billing cycle, you'll only be charged \$27 dollars for that account, as you'll only need to pay for the remaining six months. When the annual billing cycle repeats, you'll be charged \$918 for the first five users, plus \$54 for that additional user (and any other additional users you've added in the interim).
-   If your user account number dips below the amount you've already paid for, you won't be refunded. But you'll also only be charged for additional users when the number goes above the previously paid amount.
-   Pro-rated true-ups are billed either monthly or quarterly, depending on [how you're paying](#for-annual-plans-payment-type-affects-how-often-youre-charged-for-pro-rated-true-ups). In this case, since we're on a Starter plan paying by credit card, you'll be billed for pro-rated true-ups each month.

### For annual plans, payment type affects how often you're charged for pro-rated true-ups

When paying by [invoice](#how-invoicing-works-for-pro-plans), you're charged an initial annual payment, then charged *quarterly* for pro-rated true-ups. When paying with a credit card, you're charged the initial annual payment, then charged *monthly* for pro-rated true-ups.

  Payment type                           Initial payment   Pro-rated true-up cadence
  -------------------------------------- ----------------- ---------------------------
  Credit card                            Annually          Monthly
  [Invoices](#invoicing-for-pro-plans)   Annually          Quarterly

## Annual billing payments are not refundable

The upfront annual payment, as well as each additional annual user payment and monthly/quarterly true-up payments, are non-refundable. We offer this discounted rate as way to encourage long-term investment in Metabase, which helps us hire more people, improve the product and customer experience, and support the open source project. If you're not ready to commit, no worries; stick with monthly billing.

### When you should choose annual billing

Generally, annual billing is a great deal; it's cheaper across the board. The only case where you might want to prefer monthly billing is if you anticipate downsizing the number of user accounts over the course of the next year.

## What counts as a user account?

A user account is any account which has been added to your Metabase instance (manually or via SSO) that has not been deactivated. You can view a list of user accounts in your **Admin settings** -\> **People** list. Any user account which has been [deactivated](../people-and-groups/managing#deactivating-an-account) doesn't count toward your number of user accounts. That is to say: if an account exists, but has not been deactivated, that account will count toward your bill, *even if no one signs in and uses that account*. If an account is deactivated, that account is charged for the number of days the account was available for use during that billing period, including the day it was deactivated (since it was available for use for part of the day up until it was deactivated).

## How billing works with embedding

Interactive Embedding requires viewers to sign in to your Metabase, which means they will count as users for billing purposes.

Static Embedding doesn't require viewers to sign in to your Metabase, which means they won't count as additional users for billing purposes.

## How we count active user accounts each day

Each day, we tally up the active users like so:

-   For each Metabase using a particular license token in the last 36 hours,
-   We take the maximum number of user accounts at any one time in that instance during that 36-hour period,
-   Then add those counts together across all instances with the same token.

For example, say you're running two Metabase instances, A and B, that both use the same license token. If over the last 36 hours:

-   Metabase A had a maximum of 3 user accounts
-   Metabase B had a maximum of 5 user accounts

Then the number of user accounts would total 8 for that day.

If you're on Metabase Cloud, counting active users works the same: each day we count the maximum number of user accounts at any one time over the previous 36 hours.

We refresh the user count you see in your [Metabase Store account page](https://store.metabase.com) every day. Since the refresh only happens once a day, there might be a delay between when you adjust the number of user accounts in your Metabase and when your accounts sync with your Store page.

Metabase counts each user account as unique, even if that account uses the same email for multiple Metabases. For example, if person@example.com has an account in both instance A and instance B, the total will double count person@example.com (the tallying works like `COUNT`, not `COUNT DISTINCT`).

## Invoicing for Pro plans

Metabase offers annual invoicing for Pro plans (in addition to our Enterprise plans).

### How invoicing works for Pro plans

-   After switching to billing via invoices, Metabase will send you an invoice via email for the amount due for that year, as well as payment instructions. Each year after that, you'll get an annual invoice billing you for the coming year.
-   **After receiving an invoice via email, you have 15 days to pay the invoice with ACH, wire transfer, or credit card**.
-   If you add user accounts to your plan throughout the year, Metabase will bill these true-ups on a quarterly basis, with invoices for the prorated yearly cost of the additional user accounts (see [annual billing](#how-annual-billing-works)).
-   Payment can be done via Automated Clearing House (ACH) or wire transfer.
-   You can see a list of all of your invoices and their statuses in the **Billing** tab of your Metabase Store account.
-   You can add, edit, or remove up to five Tax IDs, which Metabase will include on your invoices.
-   You'll still need to keep a valid credit card on file.
-   No, we won't use your billing portal, or fill out security or other forms. If you need white-glove treatment, our sales team will be happy to help get you set up on our [Enterprise plan](/sales/).

### Criteria for invoice eligibility

In order to be eligible for invoice billing, you need to have:

-   An account with at least one Metabase Pro subscription.
-   No failed charges within the last three months (either for monthly or annual billing).
-   Ten or more total user accounts in your Metabase, OR ten or more total user accounts across all of your Metabases (if you're running more than one Metabase).

Once you're eligible to switch to billing via invoices, you'll receive an eligibility notification. If you haven't yet gotten the notification, but you think that you meet the criteria, [contact support](mailto:help@metabase.com).

<div>

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/cloud/how-billing-works.md) ]