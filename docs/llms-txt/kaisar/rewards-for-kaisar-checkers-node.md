# Source: https://docs.kaisar.io/kaisar-network/kaisar-rewards-mechanism/rewards-for-kaisar-checkers-node.md

# Rewards for Kaisar Checkers Node

Rewards are distributed to all Checkers who successfully complete tasks. The rewards are proportional to the number of tasks correctly completed by a Checker relative to the total tasks completed across the network.

### 1. Formula for Determining Checker Node Rewards

For a given Checker Node *i*, rewards are calculated per epoch (*1 Epoch = 2 weeks*) based on the following general formula:

$$
\text{Checker\_Reward} = \frac{\text{Checker\_Score} \times \text{Epoch\_Total\_Reward} \times ( 1- \text{Commission})}{\text{Total\_Score}}
$$

* **Checker\_Score**: The score of the Checker Node in a given epoch.
* **Epoch\_Total\_Reward**: The total reward allocated to all Checkers in an epoch.
* **Commission**: The reward commission rate for Delegators.
* **Total\_Score**: The cumulative score of all Checkers.

At the end of each epoch, after reward calculations, a portion of the tokens allocated to Checkers is distributed into the reward pool for supporting Delegators. The Delegator reward pool for each epoch is calculated as follows:

$$
\text{Delegator\_Total\_Reward} = \frac{\text{Checker\_Score} \times \text{Epoch\_Total\_Reward} \times \text{Commission}}{\text{Total\_Score}}
$$

For a Delegator, rewards are calculated per epoch based on the following factors:

$$
\text{Delegator\_Reward} = \frac{\text{Delegator\_Total\_Reward} \times \text{Delegator\_Stake}}{\text{Total\_Stake}}
$$

### 2.  Formula for Calculating Checker Node Points&#x20;

The score of Checker node in one epoch is calculated according to the following formula:

$$
\text{Checker\_Score} = \text{Work\_Contribution} \times \text{Checker\_Stake} \times (1 - \text{Error\_Rate)}
$$

* **Work\_Contribution**: The workload of verifications performed by the Checker, which may be the number of valid verifications completed.
* **Error\_Rate**: The error rate of the Checker (ranging from 0 to 1).
* **Checker\_Stake**: The number of NFT Licenses staked for the Node.

**Example:**

* A = 50 (50 valid verification completed)
* B = 0.9 (Checker node has a 10% error rate)
* S = 2 (2 NFT Licenses Delegators staked for Checker)

$$
\text {Checker\_Score} = 50 \times 0.9 \times 2 = 90
$$

This formula guarantees fair compensation for the Checker by accounting for workload, verification accuracy, and staking commitment.
