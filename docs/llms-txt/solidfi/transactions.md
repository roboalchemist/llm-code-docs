# Source: https://docs.solidfi.com/general/transactions.md

# Transactions

> A guide to Transactions

A transaction records money moved into an account (credit) or out of an account (debit) on an immutable ledger. Once opened, an account can have several credit and debit transactions.

An outgoing ODFI transaction originates from a Sub Account and clears from the Master Account, creating a double entry. Each entry has a unique Transaction ID and is related to the others, leading to the transaction being reconciled.

An incoming RDFI transaction is first received in the Master Account and sub-ledged into a Sub Account, creating a double entry. Each entry has a unique Transaction ID and is related to the others, leading to the transaction being reconciled.

A transaction must be manually reconciled or reversed if it is not automatically reconciled. For more, see the [Reconciliation Guide](/accounts/reconciliation).

Depending on the payment method, each transaction will go through various statuses and finally reach the settled status. In most cases, settled is considered the terminal state, but some exceptions exist. For example, an ACH transaction can be returned after it is settled. In this case, the final status of this ACH transaction is returned. 

Each payment method has a dedicated API endpoint. For more, see the [Payments Guide](/payments/introduction).

<Frame caption="Transaction hierarchy" type="glass">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/solidfi/images/Transactions.svg" />
</Frame>
