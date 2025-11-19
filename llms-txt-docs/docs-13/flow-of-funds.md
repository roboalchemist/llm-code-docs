# Source: https://docs.solidfi.com/general/flow-of-funds.md

# Flow of Funds

> A guide to Flow of Funds

The flow of funds diagram visualizes money movement in and out of the Master and Sub Accounts. It is designed based on the FinTech's use case and must be approved by the partner bank.

## Outgoing Funds from a Sub Account (ODFI)

For example, there is an outgoing ACH debit of \$10 to an external bank account:

1. All outgoing transactions can only be originated from the Sub Account. In the example below, a \$10 ACH debit transaction originated from the Sub Account, and it results in a Sub Account transaction txn\_1
2. The outgoing transaction is subsequently debited from the Master Account and sent for clearing (via the partner bank). This results in a Master Account transaction txn\_2
3. txn\_2 reconciles txn\_1

<Frame caption="ODFI Flow of Funds" type="glass">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/solidfi/images/Outgoing-Funds.svg" />
</Frame>

## Incoming Funds into a Sub Account (ODFI)

For example, there is an incoming ACH credit of \$10 from an external bank account:

1. All incoming transactions are first ledgered in the Master Account. \$10 is credited to the Master Account, and it results in a Master Account transaction txn\_1
2. The incoming transaction is subsequently credited to the Sub Account based on the beneficiary account number. This results in a Sub Account transaction txn\_2
3. txn\_2 reconciles txn\_1

<Frame caption="RDFI Flow of Funds" type="glass">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/solidfi/images/Incoming-Funds.svg" />
</Frame>
