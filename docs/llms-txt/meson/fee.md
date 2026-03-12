# Source: https://docs.meson.fi/protocol/meson/fee.md

# Swap Fee

Using Meson to move stablecoins or ETH token cross chain might incur a small amount of fee. The fee primarily consists of two parts;

* The *service fee* is a constant 0.5% service charge (mininum $0.5 USDT/USDC/BUSD, or equivalent) levied by Meson protocol. Currently, service fee is waived for each address up to $3,000 or 3 swaps on a daily basis, whichever limit occurs first applies. *Meson Premium/Premium Plus* members are entitled to a maximum of $100,000/$500,000 or equivalent free swaps during each membership period.
* *LP fees* are levied by the Liquidity Providers (LPs) to compensate for their gas expense and cost of token conversions. Just like the first few years of the Bitcoin network, most LPs do not charge LP fees between most networks, but it might change according to network condition and market markups.

All fees are deducted on the target chain, so user will receive lesser amount of stablecoins or ETH token on the target chain. Please pay attention to the fee info in the *Swap Summary* pop-up window during the use of Meson to understand the actual fees for your cross-chain swaps. Fees illustrated in the *Comments* section are promotional rates and are therefore subject to change without notice. Meson reserved all rights on the interpretation of fees.

| Type          |       Pay to      | Amount (USD or equivalent) | Comments                                                                                                                                                                                                                              |
| ------------- | :---------------: | :------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service Fee   |   Meson Protocol  |      0.05%(min $0.5u)      | Currently waived for first 3,000 USD / 3 swaps (whichever occurs first applies) per address per day ; free for *Meson Premium/Premium Plus* up to 100,000/500,000 USD                                                                 |
| Gas & LP fees | Blockchains & LPs |        market based        | Gas fee is charged in compensation to the gas cost Meson pays on target chain and is *subject to market gas* , LP fees (up to \~1%) may also incur to compensate the cost to acquiring or unlocking liquidity on origin/target chains |

When users interact with Meson for the first time, they also need to make `approve` transactions required by the ERC20 protocol (upon first time interaction with Meson smart contracts), and therefore pay relevant gas fees.

## Service Fee

The Meson service fee is levied by Meson protocol and set to be 0.05% of the swap amount regardless of networks and token pairs.

The service fee is currently waived for all users for swaps up to daily maximum of 3,000 USD. Please note this fee waiver is temporary and is subject to change without notice.

*Meson Premium* is a membership program offering zero service-fee swaps up to 500,000 USD (Premium Plus member) during its 30-day period. Please refer to Meson Premium section for more details.

For swaps that incure service fees, Meson smart contract on the target chain will deduct the release amount by `0.05% * swap amount` or `swap amount - 0.5 USDT/USDC/BUSD` whichever is smaller, so the recipient address will receive `swap amount - 0.05% * swap amount - lp fee (if applicable)` or `swap amount - (swap amount - 0.5 USDT/USDC/BUSD) - lp fee (if applicable)` whichever is larger.

## LP Fees

LP might charge a fee to compensate their gas expenses on different networks as well as costs of token conversion. LP might adjust their accepted or preferred fee range based on network & gas conditions, market exchange rates among other factors. Currently, most LPs charge 0 fee on most swap routes and tokens.

As Meson uses LayerZero stablecoins for Aptos swaps, LP might charge a fee to compensate cost to burn LayerZero stablecoins on Aptos via LayerZero bridge. This fee is subject to the fee levied by LayerZero for use of LayerZero bridge.

LP might charge a fee to small swaps to compensate the operating cost for the use of Meson protocol. Currently, swaps below 5 USD (excluding 5 USD) will be considered small swaps and therefore see a surcharge of 0.1 USD.

Each LP predefines its fee ruleset. Upon user submission of swap, Meson app will automatically select and construct swap request with the most favorable fee offered by LPs for the swap. The LP fee is thus encoded in the swap and eventually confirmed by user's signature, and then be broadcasted and submitted for execution by the Meson smart contract. User will hence receive `swap amount - lp fee - service fee (if applicable)` on the target chain for his/her cross-chain swap.
