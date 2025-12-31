# Source: https://docs.solidfi.com/accounts/sub-accounts.md

# Sub Accounts

> A guide to Sub Accounts

Sub Accounts are created under a Master Account. The total balance in all the Sub Accounts should match the Master Account balance. It's important to note that the Sub Account Holder owns the Sub Account, which means the funds in the Sub Account belong to the Sub Account Holder and are custodied at the bank.

Use the APIS to [Create a Sub Account Holder](/v2/api-reference/sub-account-holders/create-a-sub-account-holder) and then [Create a Sub Account](/v2/api-reference/sub-accounts/create-a-sub-account).

<Frame caption="Sub Accounts" type="glass">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/solidfi/images/Sub-Account.svg" />
</Frame>

Sub Accounts can be of three types:

* Cash
* Prepaid
* Checking

Each created Sub Account comes with a unique Sub Account ID. Sub Accounts can be configured to issue an Account Number depending on the use case. Upon the bank's approval, limits and controls at the Sub Account level are configured during onboarding.

Transactions can only be originated from a Sub Account. Every outgoing transaction makes a ledger entry first in the Sub Account and then ledgered in the Master Account to keep both Master and Sub Accounts in sync.

If the Sub Account is not issued an account number, an incoming transaction has to be sub-ledgered using the [Sub-Ledger a Transaction API](/v2/api-reference/transactions/sub-ledger-a-transaction).
