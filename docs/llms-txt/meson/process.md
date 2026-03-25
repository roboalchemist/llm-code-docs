# Source: https://docs.meson.fi/protocol/meson/process.md

# Swap Process

On each chain, in order to ensure the convenience of users, Meson will directly use the widely accepted tokens on the chain. For each Meson-backed token on each chain, the Meson smart contract will provide a liquidity pool to provide swap services for that token.

### Preparation Stage

LPs who want to provide swap services can call the [`deposit`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Pools/MesonPools.sol#L22) method of Meson and inject tokens that are willing to participate in the cross-chain swap into the Meson contract.

### Swap Stage

1. **Swap request:** The user (U) constructs a swap request off-chain which specifies the swap amount, the initial chain (X), the target chain (Y) and token type, as well as other necessary information. To publish the swap request, the user needs to sign it which authorizes the Meson contract to lock the swap amount + swap fee for matching LP. The signed swap will be broadcasted to the LP network through [Meson relayer](https://docs.meson.fi/protocol/system-design/relayer) and wait for an LP to match. Since this process does not require actual on-chain transactions, users do not need to pay any gas fees (for ERC20 tokens, users need to `approve` in advance and gas fees still need to be paid for this step). The signature for a swap request will be checked by Meson's smart contract ([source](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/utils/MesonHelpers.sol#L145)) for the next step to proceed.
2. **Post and bond a swap:** LP needs to validate the swap request after receiving it. For a valid swap request, an LP can post the swap by calling the [`postSwap`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Swap/MesonSwap.sol#L36) method of Meson on the initial chain X and bond it to himself. Meson contract will check the signature, transfer user's swap amount + fee, and lock them for a certain time (tentatively set to 1-2 hours). During this period, the swap will be bonded to the LP for subsequent steps. At the same time, at most one LP can complete the bonding.
3. **Lock the swap:** For an LP successfully bonded to a swap, he needs to call the [`lock`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Pools/MesonPools.sol#L79) method of Meson on the target chain Y to lock the swap funds (step 5) (tentatively 20 minutes) to ensure that the user can get paid;
4. **Release signature:** After the user validates the transactions in step 2 & 3, it is necessary to construct a signature for releasing funds within the lock period, specify the recipient address, and broadcast to inform the LP. This operation also does not require users to pay gas fees. The signature will also be checked by Meson's smart contract ([source](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/utils/MesonHelpers.sol#L187)) for the next two steps to proceed.
5. **Release fund:** After the user's release signature is made public, anyone (including the user himself) can call the [`release`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Pools/MesonPools.sol#L127) method of the Meson contract on the target chain Y. When this transaction is executed, the validity of the signature will be checked. The funds locked in step 3 will be paid to the recipient designated by the user;
6. **Receive initial funds:** Finally, the LP uses the same release signature to call the [`executeSwap`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Swap/MesonSwap.sol#L112) method of the Meson contract on the initial chain X to obtain the funds (including swap fees) deposited by the user initially. LPs can choose to withdraw this part of funds or transfer them to his liquidity pool on chain X.

![Flow of a Cross-chain Swap on Meson](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-4e00e5b8ec3a06fd65431077f9814d72cf1b3e9f%2FMeson-swap-flow.png?alt=media)

In steps 1 and 4, the use of relayer service is not mandatory. Users can also post swap requests or release signatures directly on-chain. However, this requires the user to invoke the on-chain contract and pay the gas fee. The actual process is as follows

* Posting a swap request: The user should call the `postSwap` contract method directly without LP information on the initial chain. Once processed, the LP can call the [`bondSwap`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Swap/MesonSwap.sol#L69) method to bond the swap. The consequence of the prior two is the same as an LP executing `postSwap`.
* Release the swap: The user should call the `release` contract method directly on the target chain. The LP can then see the release signature from that transaction and subsequently call the `executeSwap` method on the initial chain.

Please refer to the following diagram for the sequential process of swap.

### Rebalance Stage

After an LP provides swaps for a period of time, the distribution of his funds on different chains may be different from the initial state. If LP provides swaps in both directions of X → Y and Y → X, the overlapping parts can cancel each other so the funds that LP needs to rebalance are lower than the actual total swap amount.

When the LP rebalances the distribution of its fund pools, he can withdraw some funds from the pool by calling the [`withdraw`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Pools/MesonPools.sol#L60) method, and use the existing cross-chain solutions (cross-chain bridges, centralized exchanges, etc.) for asset movement. The time requirement for this process is relatively low, and LPs can accumulate a certain amount of funds before rebalancing. Therefore, the ratio of cross-chain fees to the swap amount would become much lower.
