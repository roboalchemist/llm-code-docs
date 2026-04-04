# Source: https://docs.solidfi.com/general/flow-of-funds.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Flow of Funds

> A guide to Flow of Funds

The flow of funds diagram visualizes money movement in and out of the Master and Sub Accounts. It is designed based on the FinTech's use case and must be approved by the partner bank.

## Outgoing Funds from a Sub Account (ODFI)

For example, there is an outgoing ACH debit of \$10 to an external bank account:

1. All outgoing transactions can only be originated from the Sub Account. In the example below, a \$10 ACH debit transaction originated from the Sub Account, and it results in a Sub Account transaction txn\_1
2. The outgoing transaction is subsequently debited from the Master Account and sent for clearing (via the partner bank). This results in a Master Account transaction txn\_2
3. txn\_2 reconciles txn\_1

<Frame caption="ODFI Flow of Funds" type="glass">
  <img src="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Outgoing-Funds.svg?fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=05a1f1e1fda9d6802d8cac2c6794eadf" data-og-width="1041" width="1041" data-og-height="680" height="680" data-path="images/Outgoing-Funds.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Outgoing-Funds.svg?w=280&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=291b6b75593ba9d03b02cb68b41e4e2e 280w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Outgoing-Funds.svg?w=560&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=46a6515a4f629f90333c0def54908699 560w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Outgoing-Funds.svg?w=840&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=f78b43876745f9413e7141217d64164b 840w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Outgoing-Funds.svg?w=1100&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=e133233e99127fa53ab4c6724236f025 1100w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Outgoing-Funds.svg?w=1650&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=86e03d5254aa839695511560ef47eaa5 1650w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Outgoing-Funds.svg?w=2500&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=ed987d8a07c02e43f571025ce6f29739 2500w" />
</Frame>

## Incoming Funds into a Sub Account (ODFI)

For example, there is an incoming ACH credit of \$10 from an external bank account:

1. All incoming transactions are first ledgered in the Master Account. \$10 is credited to the Master Account, and it results in a Master Account transaction txn\_1
2. The incoming transaction is subsequently credited to the Sub Account based on the beneficiary account number. This results in a Sub Account transaction txn\_2
3. txn\_2 reconciles txn\_1

<Frame caption="RDFI Flow of Funds" type="glass">
  <img src="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Incoming-Funds.svg?fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=37d9a359705b532f22e7e42404aa5d4e" data-og-width="1041" width="1041" data-og-height="680" height="680" data-path="images/Incoming-Funds.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Incoming-Funds.svg?w=280&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=38809a67947d7cc44457303f778160df 280w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Incoming-Funds.svg?w=560&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=156948af1a7372794dcf228bdf0c4dec 560w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Incoming-Funds.svg?w=840&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=00c72043ea5a2d217ff7a805931457aa 840w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Incoming-Funds.svg?w=1100&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=97b24bdc13937c33fe8b20112fb1b527 1100w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Incoming-Funds.svg?w=1650&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=e12108f7498e4b332369123142d60b7b 1650w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Incoming-Funds.svg?w=2500&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=324c9fcaf26934cbe7ed79df2691d1c9 2500w" />
</Frame>
