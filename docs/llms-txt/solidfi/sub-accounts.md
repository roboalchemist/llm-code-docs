# Source: https://docs.solidfi.com/accounts/sub-accounts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Sub Accounts

> A guide to Sub Accounts

Sub Accounts are created under a Master Account. The total balance in all the Sub Accounts should match the Master Account balance. It's important to note that the Sub Account Holder owns the Sub Account, which means the funds in the Sub Account belong to the Sub Account Holder and are custodied at the bank.

Use the APIS to [Create a Sub Account Holder](/v2/api-reference/sub-account-holders/create-a-sub-account-holder) and then [Create a Sub Account](/v2/api-reference/sub-accounts/create-a-sub-account).

<Frame caption="Sub Accounts" type="glass">
  <img src="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Sub-Account.svg?fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=c9ba508df10ba8c78676981f3fb4337b" data-og-width="1041" width="1041" data-og-height="680" height="680" data-path="images/Sub-Account.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Sub-Account.svg?w=280&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=929528449dd592898265ba6a8a794a7d 280w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Sub-Account.svg?w=560&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=8ca0358b6953c2bcbec255baef3fd2fc 560w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Sub-Account.svg?w=840&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=0dd104fb7a110d02c5a099d103f0e4ac 840w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Sub-Account.svg?w=1100&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=d7197fd80a9a73896c9c40e4e324d33e 1100w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Sub-Account.svg?w=1650&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=210ce5b8e66d3fc384a2050490a0b8af 1650w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Sub-Account.svg?w=2500&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=78c06b847ee110b3fd50f32ef192117c 2500w" />
</Frame>

Sub Accounts can be of three types:

* Cash
* Prepaid
* Checking

Each created Sub Account comes with a unique Sub Account ID. Sub Accounts can be configured to issue an Account Number depending on the use case. Upon the bank's approval, limits and controls at the Sub Account level are configured during onboarding.

Transactions can only be originated from a Sub Account. Every outgoing transaction makes a ledger entry first in the Sub Account and then ledgered in the Master Account to keep both Master and Sub Accounts in sync.

If the Sub Account is not issued an account number, an incoming transaction has to be sub-ledgered using the [Sub-Ledger a Transaction API](/v2/api-reference/transactions/sub-ledger-a-transaction).
