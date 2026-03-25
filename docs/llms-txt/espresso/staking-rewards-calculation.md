# Source: https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/stake-table/staking-rewards-calculation.md

# Staking Rewards Calculation

Espresso uses a proof of stake consensus mechanism where validators and their delegators earn rewards for securing the network. Anyone can participate by delegating ESP tokens to a validator (minimum 1 ESP).

To be eligible for rewards, validators must:

* Have at least one delegator with non-zero stake
* Meet the minimum stake threshold: at least 1/1000th of the largest validator's stake. For example, if the largest validator has 10,000,000 ESP staked, validators need at least 10,000 ESP to be eligible.
* Be in the top 100 validators by total stake

Validators earn rewards when they propose blocks, and those rewards are shared with delegators based on their stake proportion minus the validator's commission.

Key points:

* Rewards are distributed every block to the block proposer and their delegators
* The reward rate adjusts dynamically based on network staking participation
* Delegations become active 2 epochs after being finalized on Ethereum
* Rewards do not auto compound

## Block Reward Calculation

The block reward is dynamic, meaning it changes based on how much of the total token supply is staked. Espresso adjusts rewards to maintain a healthy staking participation level. When fewer tokens are staked, rewards increase to attract more stakers. When more tokens are staked, rewards decrease to keep inflation low.

### Reward Rate Function

The reward rate R(p) depends on the staking participation ratio p = total\_stake / total\_supply:

```
        ⎧  0.03 / √(2 × 0.01)    if 0 ≤ p ≤ 0.01
R(p) =  ⎨
        ⎩  0.03 / √(2 × p)       if 0.01 < p ≤ 1
```

Annual inflation is calculated as:

```
annual inflation = p × R(p)
```

When p ≤ 1%, the formula uses a floor of 0.01, capping the maximum reward rate at 21.21%. This keeps the reward rate between 2.12% and 21.21%, and annual inflation between 0.21% and 2.12%.

The denominator √(2 × p) determines how the reward rate changes with participation. When staking participation is low, √(2 × p) is small, making the reward rate high (21.21%). High rewards attract more stakers. When staking participation is high, √(2 × p) is large, making the reward rate low (down to 2.12%). Lower rewards prevent excessive inflation and maintain token liquidity.

#### Example Reward Rates

| Stake Ratio | Reward Rate | Annual Inflation |
| ----------- | ----------- | ---------------- |
| 1.00%       | 21.21%      | 0.212%           |
| 5.00%       | 9.49%       | 0.475%           |
| 10.00%      | 6.71%       | 0.671%           |
| 25.00%      | 4.24%       | 1.06%            |
| 50.00%      | 3.00%       | 1.50%            |
| 100.00%     | 2.12%       | 2.12%            |

### Block Reward Formula

```
annual inflation = stake ratio × reward rate
block reward = (total supply × annual inflation) / blocks per year
```

Where:

* **Total supply** = initial supply + all rewards distributed so far
* **Blocks per year** = milliseconds per year / average block time in ms
* **Average block time** is measured from the previous epoch

The block reward is fixed for the entire epoch and recalculated for each new epoch.

## Reward Distribution

Validators only earn rewards when they successfully propose a block which is accepted and finalized by consensus. For each view, a leader is randomly selected from the active validator set, with selection probability proportional to stake. Over time, the number of blocks a validator proposes is proportional to their share of the total network stake.

Delegations become active 2 epochs after being finalized on Ethereum. This delay exists because the Espresso network reads the stake table from L1 and applies it with a 2-epoch lag. For example, if your delegation is finalized on Ethereum during epoch 5, your stake becomes active in epoch 7. Rewards begin in the third epoch since the first two epochs don't have the stake table from L1 available.

When a validator proposes a block, rewards are distributed as follows:

First, the portion available to delegators is calculated based on the validator's commission rate, expressed in basis points where 10,000 = 100%:

```
delegator pool = block reward × (10,000 - commission) / 10,000
```

For example, if commission is 1,000 (10%), delegators receive 90% of the block reward. Each delegator then receives a share proportional to their stake:

```
delegator reward = (delegator's stake / validator's total stake) × delegator pool
```

The validator receives everything remaining after delegator rewards:

```
validator commission = block reward - total delegator rewards
```

## Undelegating

You can undelegate some or all of your staked tokens from a validator at any time. When you undelegate, your tokens are removed from the validator's stake on L1. This change takes effect on Espresso 2 epochs after being finalized on Ethereum, the same delay as delegations.

The tokens then enter an escrow period (see [Exit Escrow Period](https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/stake-table#exit-escrow-period)). After the escrow period ends, you can claim your tokens.

You can only have one pending undelegation per validator at a time. You must claim your withdrawal before initiating another undelegation from the same validator.

## Do Rewards Compound?

**No, rewards do not automatically compound.** To compound your rewards:

1. Claim rewards to your wallet
2. Re delegate the claimed tokens to a validator
