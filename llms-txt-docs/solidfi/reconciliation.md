# Source: https://docs.solidfi.com/accounts/reconciliation.md

# Reconciliation

> A guide to Reconciliation

Solid v2 platform has reconciliation built-in. It ensures that all three below accounts are always in sync:

* FBO
* Master Account
* Sub Accounts

<Frame caption="Reconciliation" type="glass">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/solidfi/images/Reconciliation.svg" />
</Frame>

The Solid Dashboard lets you view all non-reconciled transactions in real time, informing you of the reconciliation status. Every transaction object has a reconciliation sub-object that provides the transaction's reconciliation status. If the transaction is reconciled, the sub-object has the transaction IDs in both Master and Sub Accounts. This ensures that both Master and Sub Accounts are always in sync. [Retrieve a Transaction using the API](/v2/api-reference/transactions/retrieve-a-transaction) to view the reconciliation status.

Every incoming and outgoing transaction is ledgered in the Master Account to reflect the FBO accurately. This ensures that both Master Account and FBO are always in sync.
