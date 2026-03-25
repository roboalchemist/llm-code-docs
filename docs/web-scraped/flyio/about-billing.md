# Source: https://fly.io/docs/about/billing/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Fly.io Billing 

## [](#overview)[Overview] 

Billing for Fly.io is monthly per organization. Organizations are administrative entities that enable you to add members, share app development environments, and manage billing.

New customers and all new organizations (including those created by previously existing customers) are billed monthly for resource usage. Refer to our resource [Pricing page](/docs/about/pricing/) for details.

------------------------------------------------------------------------

## [](#view-invoices)[View invoices] 

You can view and download invoices from the **Billing** section of yourÂ [dashboard](https://fly.io/dashboard/personal/billing) for each organization.

To download a past invoice, click **View** for the relevant cycle. You'll be sent to the Stripe billing portal where you'll have the option to download the invoice.

------------------------------------------------------------------------

### [](#understand-your-invoice-charges)[Understand your invoice charges] 

The prices of provisioned services are mostly fixed. If you provision Machines and leave them running all month, weâ€™ll charge you a predictable amount for that Machine.

A common reason for additional charges is extra RAM usage.

For a breakdown of charges, check out your invoice in the Billing section of the [dashboard](https://fly.io/dashboard/personal/billing).

Weâ€™re happy to discuss a refund if you do create compute resources by mistake, or if your app receives unexpected traffic due to an attack and generates a surprisingly large bill. Just send an email toÂ <billing@fly.io>.

------------------------------------------------------------------------

## [](#machine-billing)[Machine billing] 

Started Machines are billed per second that they're running (the time they spend in the `started` state), based on the price of a named CPU/RAM combination, plus the price of any additional RAM you specify.

For example, a Machine described in your dashboard as "shared-1x-cpu@1024MB" is the â€œshared-cpu-1xâ€? Machine size preset, which comes with 256MB RAM, plus additional RAM (1024MB - 256MB = 768MB). For pricing and available CPU/RAM combinations, read about [Compute pricing](/docs/about/pricing/#compute).

Stopped and suspended Machines are billed based on their root file system (rootfs) usage per second (the time they spend in the `stopped` or `suspended` state) by \$0.15 per GB per month.

For example, a Machine described in your dashboard as having 1GB of rootfs stopped for 10 days in the entire month will cost \$0.05. If you have 3 stopped Machines of 1GB rootfs each stopped for 30 days it will cost \$0.45 (\$0.15 x 3).

------------------------------------------------------------------------

## [](#gpu-billing)[GPU billing] 

GPUs are billed per second that the attached Fly Machine is running (the time they spend in the `started` state), based on the per hour cost of the GPU card. Learn more about [pricing for GPUs](/docs/about/pricing/#gpus-and-fly-machines).

You're also billed for the Fly Machine separately from the GPU.

------------------------------------------------------------------------

## [](#volume-billing)[Volume billing] 

Volume billing is pro-rated to the hour and we subtract the free allowances first for the Launch, Scale, and Enterprise plans (all of which are now discontinued for new customers). For details, see [Volume pricing](/docs/about/pricing/#persistent-storage-volumes).

If you create a volume, you will be charged for it. You're billed for volumes that aren't attached to Machines, and for volumes that are attached to Machines in any state, including stopped Machines. Volumes in `pending_destroy` state do not accrue charges.

------------------------------------------------------------------------

## [](#volume-snapshot-billing)[Volume snapshot billing] 

Volume snapshot billing is pro-rated to the hour and we subtract the free allowance first. For details, see [Volume Snapshots pricing](/docs/about/pricing/#volume-snapshots).

If you create a snapshot of a volume (either manually or through automatic daily snapshots), you will be charged for the storage space it occupies.

Snapshots are stored incrementally, so you're only charged for data that has changed since the previous snapshot for the volume.

For example, if you have a 10GB volume with 2GB of actual data and 5 daily snapshots with minimal changes between them, you might be charged for around 2.5GB of total snapshot storage rather than 50GB (5 Ã--- 10GB).

------------------------------------------------------------------------

## [](#unified-billing)[Unified Billing] 

Unified billing allows you to consolidate billing for multiple organizations under a single organization. This means you'll receive a single invoice for all organizations under unified billing. This feature is useful for managing billing for multiple organizations, such as when you have multiple teams or projects.

**Billing Organization**: The organization that is responsible for paying for the resources used by all organizations linked to it. Any organization in good standing with an attached payment method can be a Billing Organization.

**Linked Organization**: An organization that is linked to another organization for billing purposes. It otherwise functions as a normal organization.

### [](#how-unified-billing-works)[How Unified Billing Works] 

-   You'll receive a single invoice for all organizations under unified billing.
-   Billing Organization must have a payment method on file (credit card or Stripe Link).
-   Linked Organizations share credits with their Billing Organization.
-   Billing Organizations can have a max of 100 Linked Organizations.

### [](#how-to-use-unified-billing)[How to use Unified Billing] 

You can either create a new Linked Organization or link an existing one:

#### [](#new-organization)[New Organization] 

A **Linked Organization** can be created from the [new organization page](/organizations/new). When creating a new organization, you can choose an existing Organization to link it to.

#### [](#link-an-existing-organization)[Link an existing Organization] 

An existing organization can be converted to a **Linked Organization** from the organization's billing page by clicking the "Link billing to another Organization" button.

-   Only admins can link an organization to another organization.
-   We recommend saving any invoices you may need for account purposes before linking an organization.

------------------------------------------------------------------------

## [](#some-things-to-consider)[Some things to consider] 

-   Each organization has its own [private network](/docs/networking/private-networking/). Organizations are isolated from each other, which might be advantageous from a security standpoint.
-   Cross organization networking is still possible with [Flycast](/docs/networking/flycast/)
-   Detaching a Linked Organization from its Billing Organization is not possible at this time. Instead we suggest creating a new organization and moving resources there.

------------------------------------------------------------------------

## [](#payment-options)[Payment options] 

We process payments through Stripe. Monthly invoicing requires a credit card or credits.

### [](#how-we-use-credit-cards)[How we use credit cards] 

We require an active, valid credit card on file for most Fly.io accounts to do things like deploying multiple apps and deploying public images. This is primarily a means to prevent abuse and ensure that we can collect payment at the end of the month.

### [](#pre-authorization-requests)[Pre-authorization Requests] 

We may send a pre-authorization request to the issuing bank to verify a bank will authorize charges. Some credit card companies present these as real charges, which may surprise you.

A pre-auth is really just a hold on a credit card; it is not a real charge. Weâ€™ll typically pre-authorize a small amount (usually less than \$5) after signup, then cancel the authorization immediately. Banks may show the pre-auth for up to 7 days, even though we have not collected any money.

### [](#if-you-dont-have-a-credit-card)[If you don't have a credit card] 

While a credit card is the preferred payment method, if you don't have one, then you can add credits to your account. You can purchase credits from the Billing section of the [dashboard](https://fly.io/dashboard/personal/billing) in various amounts (minimum purchase \$25). Your usage cost is subtracted from the credit balance each month.

### [](#prepaid-cards)[Prepaid cards] 

You can't use a prepaid card as a default (or saved) payment method. You can, however, use a prepaid card to add credits to your account.

------------------------------------------------------------------------

## [](#delete-your-account)[Delete your account] 

To delete your Fly.io account, go to Account \> Settings \> [Delete Account](https://fly.io/user/deactivate) in your dashboard. You'll see a list of clean-up tasks that need to be done before you can delete the account, including:

-   Delete or remove yourself from organizations to avoid leaving behind inaccessible orgs. This does not include your personal organization.
-   Delete apps (or remove yourself from the associated organizations).
-   Remove certificates so that any custom domains are released.
-   Remove extensions to ensure that you don't get billed by partners when you can no longer access your account.

When you've completed the clean-up tasks, click **Delete** to permanently delete your Fly.io account.

------------------------------------------------------------------------

## [](#discontinued-legacy-plans)[Discontinued/legacy plans] 

### [](#legacy-plan-billing)[Legacy Plan billing] 

Customers who received a \$5 free trial usage credit when signing up for the \$5/mo Hobby plan will be billed monthly after that credit is used up.

Legacy plan billing, and any included usage, is pro-rated over the month. For example, if you signed up for a Scale plan on September 15th, then you'd be charged \$14.50 (half of the \$29/mo plan cost) right away and you'll have \$14.50 of usage included up to September 30th. Then you'll be charged \$29 at the start of October and have \$29/mo of usage included for that billing cycle.

### [](#free-resource-allowances-for-legacy-plan-users)[Free resource allowances for Legacy Plan users] 

Fly.io has deprecated plans as of October 7, 2024, but is still honoring them for users who purchased them prior to that date. If your plan includes [free allowances](/docs/about/pricing/#legacy-free-allowances), we subtract them off the top of your usage total. Once your usage exceeds the free allowance for any given resource, we start metering usage of that resource for billing purposes.

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fabout%2Fbilling.html.markerb)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Fly.io+Billing%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fabout%2Fbilling%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fabout%2Fbilling.html.markerb%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Fly.io+Billing%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/about/billing.html.markerb)