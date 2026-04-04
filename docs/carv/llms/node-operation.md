# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/faq/node-operation.md

# Node Operation

#### **Is it feasible to host 100 verifier nodes within the CARV network?**

Yes, a node can receive up to 100 delegations.

#### **Can the user change the commission rate?**

The commission rate can only be changed once per week.

#### **Does having more node delegations increase the cost on node resources?**

No, the number of delegations to a node does not affect its performance.

#### If I delegate to someone, will I lose anything?

You need to pay portion of rewards as commission to the node operator. But right now there are bunch of 0% commission rate nodes so you can delegate to those. You lose nothing and don't need to keep anything running.

#### Getting error \`Failed to Launch Verifier, you verifier node does not have enough voting power. Please connect with a wallet with more License Keys or seek more delegations for your verifier address\`?

There is a 2000 cap for active node to make sure the contract is running efficiently. If you are getting above error that means there are already 2000 nodes active and you don't have enough delegation to join the validator set. You need to have more than the node has lowest delegation in the set to join. Prefer to delegate your license if you are getting this error or try to get more delegations.

#### Why did the rewards get reduced?

The rewards we previously displayed were the total sum of all delegations. We have now corrected the figures to show the rewards for each individual address. The updated numbers accurately reflect what is calculated by the smart contract. Moving forward, the rewards will be updated 30 minutes after midnight UTC every day.

#### How rewards are calculated?

1. Everyday there are 385850 alpha-veCARV in total. Same amount for mainnet. You can check the value here: <https://docs.carv.io/carv-protocol/verifier-node-explained/node-rewards>
2. Based on total number of license participate (delegated), rewards will be evenly distributed.
3. You can check the contract globalDailyActiveNodes to check how many license is delegated in total per day. For example day 1 has 5644 licenses in total, so day 1 each node should expect 385850 / 5644 = 68.36 alpha-veCARV.
