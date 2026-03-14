# Source: https://plivo.com/docs/number-masking/concepts/number-pools.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Number Pools with Sub-accounts

> Use sub-accounts to create dedicated number pools for different use cases

## Introduction

You can now allocate dedicated numbers for specific purposes with Plivo's enhanced support for number masking through sub-accounts. Previously, to leverage the number masking feature across various use cases—such as Customer-Delivery Agent Interaction, Customer-Support Interaction, Seller-Buyer Interaction, etc.— users were required to create multiple Plivo accounts.

This new capability eliminates the need for creating and managing multiple Plivo accounts, thereby saving you both time and effort. Here's how to make the most of Plivo's number masking feature using sub-accounts.

## Using Sub-accounts with Number Masking

Plivo customers who need dedicated numbers for multiple number masking purposes can now utilize sub-accounts. Simply assign numbers to the sub-accounts you wish to use and initiate masking sessions through the steps below. Plivo will automatically manage the virtual number allocation for these sessions.

1. Create a sub-account through the [Plivo console](https://cx.plivo.com/sub-accounts) or [API](/account/api/subaccount#create-a-subaccount).
2. Rent and link numbers to the sub-account in the [console](https://cx.plivo.com/phone-numbers) or using Plivo's [API](/numbers/phone-numbers).
3. Initiate a [number masking session](/number-masking/api/session) using the sub-account auth. You're all set!

Plivo will exclusively use the numbers associated with the sub-account for virtual number allocation in number masking.

<Frame caption="Using Sub-accounts with Number Masking">
  <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-masking/number-pools-using-sub-account-img.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=26a14f35f0c3cfca67f0c4901e7ca527" width="1024" height="513" data-path="images/number-masking/number-pools-using-sub-account-img.png" />
</Frame>

## Next Steps

* [Create a sub-account](/account/api/subaccount) - Set up sub-accounts to organize your number pools
* [Create a session](/number-masking/api/session#create-a-session) - Start a number masking session using your sub-account
