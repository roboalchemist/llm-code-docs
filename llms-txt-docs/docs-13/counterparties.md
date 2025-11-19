# Source: https://docs.solidfi.com/general/counterparties.md

# Counterparties

> A guide to Counterparties

A counterparty is a person or business that is the other party participating in a financial transaction. Before originating a transaction, the counterparty must pass the OFAC check. Other checks (as mandated by the bank per the CIP requirements) are essential in screening and verifying the counterparty before originating a transaction. 

Every transaction originating from a sub account requires a counterparty ID, which identifies the other party. FinTechs can create a counterparty using the [Create a Counterparty API](/v2/api-reference/counterparties/create-a-counterparty).

Since the end user can make multiple transactions with the same counterparty using various form factors, the counterparty object can capture information related to different form factors, such as ACH, Wire, Check, FedNow, and RTP, providing a complete transaction history with the counterparty.

For more, see the [Payments Guide](/payments/introduction).

<Frame caption="Counterparty hierarchy" type="glass">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/solidfi/images/Counterparties.svg" />
</Frame>
