# Source: https://docs.solidfi.com/accounts/master-accounts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Master Accounts

> A guide to Master Accounts

The Master Account (provisioned for FinTech) mirrors FinTech's FBO  with the bank. The FBO and the Master Accounts always have the same balance and same set of credit and debit transactions.

The Master Account is provisioned for the Master Account Holder, usually the FinTech. Solid provisions the Master Account at the time of onboarding and configures it to FinTech's specific needs upon the bank's approval.

In most cases, the FinTech is provisioned with a single Master Account.

<Frame caption="Single Master Account" type="glass">
  <img src="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Single-Master-Account.svg?fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=f09dfc77809e088cd2c410ae4592b5c3" data-og-width="1041" width="1041" data-og-height="680" height="680" data-path="images/Single-Master-Account.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Single-Master-Account.svg?w=280&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=5d8948be48db012aa7c7281f9e9d3dbf 280w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Single-Master-Account.svg?w=560&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=92e88ed062f291f91a891d489f3fb46a 560w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Single-Master-Account.svg?w=840&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=8a0a2f9daf71dfff5c22ed1dc07c55cc 840w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Single-Master-Account.svg?w=1100&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=e9eeb88802f52828ecfa0f8e703ea9b5 1100w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Single-Master-Account.svg?w=1650&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=296fd6b926b6bcb8756df01a202f4676 1650w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Single-Master-Account.svg?w=2500&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=a0b89ba902a39fc612093993936556df 2500w" />
</Frame>

However, in some cases, depending on the use case, the provisioning process is flexible enough to accommodate the FinTech with multiple Master Accounts that mirror a single FBO at the bank.

<Frame caption="Multiple Master Accounts" type="glass">
  <img src="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Multiple-Master-Account.svg?fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=c58aa8ecedf22374ee82db36ee752c74" data-og-width="1041" width="1041" data-og-height="680" height="680" data-path="images/Multiple-Master-Account.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Multiple-Master-Account.svg?w=280&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=225ffb6244229ff810b46781e1844d5d 280w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Multiple-Master-Account.svg?w=560&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=a0ebcf935466ab0e91817a1801a632cd 560w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Multiple-Master-Account.svg?w=840&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=818e9a4504c1a685bca29a1067aec496 840w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Multiple-Master-Account.svg?w=1100&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=097471055d3f0dff4b5cf4ad9e3b1e89 1100w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Multiple-Master-Account.svg?w=1650&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=0f4fd433be47e0fb21e6db7c08f4b102 1650w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Multiple-Master-Account.svg?w=2500&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=fb279bdada231010548a453278e54453 2500w" />
</Frame>

Every incoming transaction that hits the FBO is first ledgered to the Master Account and then sub-ledgered to the Sub Account. The two entries of the incoming transaction (in the Master Account and Sub Accounts) are	required to reconcile the transaction.
For more, see the [Reconcilation Guide](/accounts/reconciliation).

Similarly, any transaction originating from a Sub Account is first ledged on the Sub Account and then the Master Account, eventually clearing from the FBO.

Use the [Master Account API](/v2/api-reference/master-accounts/retrieve-a-master-account) designed to provide detailed information about the Master Account.
