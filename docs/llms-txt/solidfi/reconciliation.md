# Source: https://docs.solidfi.com/accounts/reconciliation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reconciliation

> A guide to Reconciliation

Solid v2 platform has reconciliation built-in. It ensures that all three below accounts are always in sync:

* FBO
* Master Account
* Sub Accounts

<Frame caption="Reconciliation" type="glass">
  <img src="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Reconciliation.svg?fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=7110025d2c32789af23728277d360afc" data-og-width="1041" width="1041" data-og-height="680" height="680" data-path="images/Reconciliation.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Reconciliation.svg?w=280&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=b785c33343c152dd23f11f203d76c5eb 280w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Reconciliation.svg?w=560&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=d971ba181bf8858c4aa8fb1ed185e567 560w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Reconciliation.svg?w=840&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=dbe4e49a8c316803e7a223eb1c285f61 840w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Reconciliation.svg?w=1100&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=69edb39bf71d458223cdef60c27f9abd 1100w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Reconciliation.svg?w=1650&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=a576ee6bd9b265d26f964a849d43bc36 1650w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Reconciliation.svg?w=2500&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=489494f4d2df855d5dc1ede5501f3da5 2500w" />
</Frame>

The Solid Dashboard lets you view all non-reconciled transactions in real time, informing you of the reconciliation status. Every transaction object has a reconciliation sub-object that provides the transaction's reconciliation status. If the transaction is reconciled, the sub-object has the transaction IDs in both Master and Sub Accounts. This ensures that both Master and Sub Accounts are always in sync. [Retrieve a Transaction using the API](/v2/api-reference/transactions/retrieve-a-transaction) to view the reconciliation status.

Every incoming and outgoing transaction is ledgered in the Master Account to reflect the FBO accurately. This ensures that both Master Account and FBO are always in sync.
