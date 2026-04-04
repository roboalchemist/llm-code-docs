# Source: https://docs.solidfi.com/general/counterparties.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.solidfi.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Counterparties

> A guide to Counterparties

A counterparty is a person or business that is the other party participating in a financial transaction. Before originating a transaction, the counterparty must pass the OFAC check. Other checks (as mandated by the bank per the CIP requirements) are essential in screening and verifying the counterparty before originating a transaction. 

Every transaction originating from a sub account requires a counterparty ID, which identifies the other party. FinTechs can create a counterparty using the [Create a Counterparty API](/v2/api-reference/counterparties/create-a-counterparty).

Since the end user can make multiple transactions with the same counterparty using various form factors, the counterparty object can capture information related to different form factors, such as ACH, Wire, Check, FedNow, and RTP, providing a complete transaction history with the counterparty.

For more, see the [Payments Guide](/payments/introduction).

<Frame caption="Counterparty hierarchy" type="glass">
  <img src="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Counterparties.svg?fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=df58299b1fcf9f5c6943f74f89e72fcd" data-og-width="1041" width="1041" data-og-height="680" height="680" data-path="images/Counterparties.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Counterparties.svg?w=280&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=1ef283febb50ce719ca5199e46822726 280w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Counterparties.svg?w=560&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=255d2bb1aebbb6ce5e4bfde8e21d8300 560w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Counterparties.svg?w=840&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=926b0f753447ab0222da6d2f695a91e1 840w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Counterparties.svg?w=1100&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=f69c0b995c327a7abcfc763182a09e6b 1100w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Counterparties.svg?w=1650&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=27bbf3fbec6265b99f69097b9eb3af3b 1650w, https://mintcdn.com/solidfi/QfDnCLZOrU3hxF1R/images/Counterparties.svg?w=2500&fit=max&auto=format&n=QfDnCLZOrU3hxF1R&q=85&s=ce732f86c04f3722d0fcf47cb4d3144a 2500w" />
</Frame>
