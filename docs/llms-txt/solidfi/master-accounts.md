# Source: https://docs.solidfi.com/accounts/master-accounts.md

# Master Accounts

> A guide to Master Accounts

The Master Account (provisioned for FinTech) mirrors FinTech's FBO  with the bank. The FBO and the Master Accounts always have the same balance and same set of credit and debit transactions.

The Master Account is provisioned for the Master Account Holder, usually the FinTech. Solid provisions the Master Account at the time of onboarding and configures it to FinTech's specific needs upon the bank's approval.

In most cases, the FinTech is provisioned with a single Master Account.

<Frame caption="Single Master Account" type="glass">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/solidfi/images/Single-Master-Account.svg" />
</Frame>

However, in some cases, depending on the use case, the provisioning process is flexible enough to accommodate the FinTech with multiple Master Accounts that mirror a single FBO at the bank.

<Frame caption="Multiple Master Accounts" type="glass">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/solidfi/images/Multiple-Master-Account.svg" />
</Frame>

Every incoming transaction that hits the FBO is first ledgered to the Master Account and then sub-ledgered to the Sub Account. The two entries of the incoming transaction (in the Master Account and Sub Accounts) are	required to reconcile the transaction.
For more, see the [Reconcilation Guide](/accounts/reconciliation).

Similarly, any transaction originating from a Sub Account is first ledged on the Sub Account and then the Master Account, eventually clearing from the FBO.

Use the [Master Account API](/v2/api-reference/master-accounts/retrieve-a-master-account) designed to provide detailed information about the Master Account.
