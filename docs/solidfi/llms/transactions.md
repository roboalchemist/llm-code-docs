# Source: https://docs.solidfi.com/general/transactions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transactions

> A guide to Transactions

A transaction records money moved into an account (credit) or out of an account (debit) on an immutable ledger. Once opened, an account can have several credit and debit transactions.

An outgoing ODFI transaction originates from a Sub Account and clears from the Master Account, creating a double entry. Each entry has a unique Transaction ID and is related to the others, leading to the transaction being reconciled.

An incoming RDFI transaction is first received in the Master Account and sub-ledged into a Sub Account, creating a double entry. Each entry has a unique Transaction ID and is related to the others, leading to the transaction being reconciled.

A transaction must be manually reconciled or reversed if it is not automatically reconciled. For more, see the [Reconciliation Guide](/accounts/reconciliation).

Depending on the payment method, each transaction will go through various statuses and finally reach the settled status. In most cases, settled is considered the terminal state, but some exceptions exist. For example, an ACH transaction can be returned after it is settled. In this case, the final status of this ACH transaction is returned. 

Each payment method has a dedicated API endpoint. For more, see the [Payments Guide](/payments/introduction).

<Frame caption="Transaction hierarchy" type="glass">
  <img src="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Transactions.svg?fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=489b745cde06dcf10dbc7b35cfb57912" data-og-width="1041" width="1041" data-og-height="680" height="680" data-path="images/Transactions.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Transactions.svg?w=280&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=f4bfb9b85faa582e26018dc505a776f6 280w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Transactions.svg?w=560&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=b2ba7edfef5c0ee18d167f53f945b4a3 560w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Transactions.svg?w=840&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=2a11b3034164c41f0bbb9c669782c2f5 840w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Transactions.svg?w=1100&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=cf5d95c1263457287a4a8bb448e40967 1100w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Transactions.svg?w=1650&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=4d076ff6093e2dffba34ff2d47a9ba82 1650w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Transactions.svg?w=2500&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=8ad14875ed15150060fa1adb827038bd 2500w" />
</Frame>
