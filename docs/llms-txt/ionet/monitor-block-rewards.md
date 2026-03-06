# Source: https://io.net/docs/guides/block-rewards/monitor-block-rewards.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Monitor Block Rewards

## Table of Contents

* [Block Rewards Tab](/guides/block-rewards/monitor-block-rewards#block-rewards-tab)
* [Block Details Table](/guides/block-rewards/monitor-block-rewards#block-details-table)
* [Block Reward Details](/guides/block-rewards/monitor-block-rewards#block-reward-details)
  * [Exceptions](/guides/block-rewards/monitor-block-rewards#exceptions)

### Block Rewards Tab

The Block Rewards tab provides a transparent view of io.net's Block Rewards and coin emissions. Users can consult this information to monitor worker nominations and their status. Users can track the performance and success rates for worker nominations and block completion. Information on coin emissions and block rewards provide transparency about io.net network’s health.

The example below shows the **Block Rewards** tab, with each section explained in detail afterward.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a4a3f9b-block_rewards.png?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=02fcc14e29107a69323d4827fb985a0f" alt="" data-og-width="2602" width="2602" data-og-height="1336" height="1336" data-path="images/docs/a4a3f9b-block_rewards.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a4a3f9b-block_rewards.png?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=1aaa5fb7e12c133030f5644cd09f54fb 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a4a3f9b-block_rewards.png?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=e46a6801f5b6fbe85402b42a2499339b 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a4a3f9b-block_rewards.png?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=ab44c1ac32bff243db7698be6fd860f9 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a4a3f9b-block_rewards.png?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=7eddfa9d32a88737be70f438e99700be 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a4a3f9b-block_rewards.png?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=72c9b82fb8dc547b7bd9de731a2ef668 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a4a3f9b-block_rewards.png?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=e3cb8026be12e606a51753caadf4fba9 2500w" />
</Frame>

The top section of the **Block Rewards** tab provides real-time data about IO Coin emissions and blocks.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fbaaa2-bwtop.png?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=f5166973a6cc8ed3c7d092b59642a62e" alt="" data-og-width="2092" width="2092" data-og-height="644" height="644" data-path="images/docs/1fbaaa2-bwtop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fbaaa2-bwtop.png?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=81795e314edb2c66de3b7f7996a30854 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fbaaa2-bwtop.png?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=d52333f81c6264501f2444cb94a8ab71 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fbaaa2-bwtop.png?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=03e8987cb3ceb593b11cdeed1e0d8ac3 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fbaaa2-bwtop.png?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=66a065df0f38d793fed41865cecf03b4 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fbaaa2-bwtop.png?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=ff30eff28f6c35a0be4eac54174c660c 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1fbaaa2-bwtop.png?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=a9b525f4a8b404eecbde13ca65618f57 2500w" />
</Frame>

| Block                         | Description                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------- |
| *Total Coins Distributed*     | The cumulative number of IO Coins distributed since inception.                                                |
| *Today’s Distributed Coins*   | Total number of IO Coins distributed for the current calendar day.                                            |
| *Total Blocks Computed*       | The cumulative number of blocks successfully added to the blockchain since inception.                         |
| *Next Block Start Time*       | The estimated time when the next block will be initiated. Blocks are added to the chain at hourly intervals.  |
| *Total Unique Workers Paid*   | The number of unique workers that earned a block reward since inception.                                      |
| *Today’s Unique Workers Paid* | The number of unique workers that earned a block reward for the current calendar day. Each day ends at UTC+0. |

### Block Details Table

The \*\*Block Details \*\*table provides a detailed overview of the blocks processed in the blockchain. The list provides a transparent and verifiable record of all blocks in the IO Coin blockchain. Users can search for specific blocks and view details, verify transactions, and trace the history and integrity of the blockchain.

The table is an important tool to monitor the blockchain's performance, transparency, and efficiency, and provides users with insight into the block creation process and the distribution of rewards.

You can download a *CSV file* for each ***Block ID*** by going to [Block Rewards](https://block-rewards.io.solutions/).

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9eda851-brbottom.png?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=d149f6713bc6b6d2af3410310f1ddc22" alt="" data-og-width="2456" width="2456" data-og-height="652" height="652" data-path="images/docs/9eda851-brbottom.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9eda851-brbottom.png?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=fc0b512249122ac31ba0c0003a722f2e 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9eda851-brbottom.png?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=5c43f5db23e950743ed31fb3f1d833cd 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9eda851-brbottom.png?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=8839195c2c5b31110a282e929a00656e 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9eda851-brbottom.png?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=815d7d70fc0d130308dcc31a0b82d76c 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9eda851-brbottom.png?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=5dee8a2b3a44f5319e15ed81a1e6c354 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/9eda851-brbottom.png?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=ecac663f53f5fdc0f09900e542ab1cec 2500w" />
</Frame>

| Column                   | Description                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Search Block ID*        | Allows you to search for specific Block IDs.                                                                                                                                                                                                                                                                                                                                                           |
| *Status*                 | The current state of each block within the io.net blockchain network.                                                                                                                                                                                                                                                                                                                                  |
| *In Progress*            | The worker has been nominated for a block reward. The block is not complete nor added to the blockchain. When the block closes, the worker is notified.                                                                                                                                                                                                                                                |
| *Completed*              | The block has been successfully validated and added to the blockchain.                                                                                                                                                                                                                                                                                                                                 |
| *Failed*                 | The attempt to create a block has failed.                                                                                                                                                                                                                                                                                                                                                              |
| *Block ID*               | A unique identifier assigned to each block within a blockchain. This assists in maintaining the chronological order and integrity of the blockchain.                                                                                                                                                                                                                                                   |
| *Processed Time*         | The exact time the block was completed in UTC.                                                                                                                                                                                                                                                                                                                                                         |
| *Total Rewards Emission* | The total distribution of rewards for a specific block.                                                                                                                                                                                                                                                                                                                                                |
| *Nominated Workers*      | Workers nominated for the hourly block reward. To be nominated, the worker must satisfy the requirements of recent *Uptime* (connection status) and *Proof of Work*. The worker is evaluated again when the block closes. If it satisfies the *Proof of TimeLock* (based on Uptime) and *Proof of Work* (PoW) requirements for the one hour period, the worker is rewarded based on their final score. |
| *Succeeded*              | The total number of workers that succeeded in meeting the criteria for a block reward of the total workers that were nominated.                                                                                                                                                                                                                                                                        |
| *Failed*                 | Number of workers that failed to earn a block reward of the total workers that were nominated.                                                                                                                                                                                                                                                                                                         |

### Block Reward Details

If you click on a specific block, you can view the details for each *IO Worker Block Reward*. This page provides a complete list of all the nominated workers for the specific block. You can filter to view by ***Completed*** (Successful) and ***Failed*** workers. You can search for your *Device ID* to check the status of your Block Reward.

<Info>
  If a block reward is in progress, you are unable to click on it until it is complete.
</Info>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/03091d7-br2.png?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=ab2cfc942040cd856a4e450ddd171cf2" alt="" data-og-width="2618" width="2618" data-og-height="2288" height="2288" data-path="images/docs/03091d7-br2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/03091d7-br2.png?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=5b6de9d5a43ac05a4ab021d25d086424 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/03091d7-br2.png?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=5fb8d4c0faac02c2acff3c29a867c10a 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/03091d7-br2.png?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e424974cdbafad400dfdcb9f6ba99b2f 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/03091d7-br2.png?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=53378facd984542cbb1da0866d259463 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/03091d7-br2.png?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=cc88e0d7bcb9557a935250654e4b4aa1 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/03091d7-br2.png?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=c3a10d2e1e025f7d352f56dec4dffbef 2500w" />
</Frame>

The example below shows an IO Worker Block Reward. It provides details on the individual worker. You can click on the ***Device ID*** to view the info related to the worker in the **Workers** tab.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/61906ca-br1.png?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=f9766fc6554d06218aa2acd66769d41e" alt="" className="mx-auto" style={{ width:"52%" }} data-og-width="802" width="802" data-og-height="1324" height="1324" data-path="images/docs/61906ca-br1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/61906ca-br1.png?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=bda21ea7be77c0575f9cfa2aa17d3da9 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/61906ca-br1.png?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=93e494b7ff2f6852cdc1b4e4fcfc1f85 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/61906ca-br1.png?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=40bf55d8a8d7aeaddb89aa07a7f3a4b5 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/61906ca-br1.png?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=c6aff2c86637cfcb499d37a8387bf03e 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/61906ca-br1.png?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=c8b3807f275ff45e1582b6a97d3c29dc 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/61906ca-br1.png?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=60595065d56fec917d4ad7838c7fd8fd 2500w" />
</Frame>

Below is the Block Reward calculation formula.

```
+(0.02 x (connectivity_tier_number" / 4.0))  
   + (2.0 x "hardware_multiplier" x "processor_quantity") ) x 100 + (0.05 x "was_hired"))x 10
```

| Block                    | Description                                                                                                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *IO Worker Block Reward* | To the right of this, you can view the **Completed** or **Failed** status. The green **Completed** status indicates success.                                                      |
| *Device ID*              | You can copy the *Device ID* or click it to view the info related to the worker in the **Workers** tab.                                                                           |
| *Connectivity Tier*      | The *Connectivity Tier* that the worker qualifies for. This is an option when a customer reserves a GPU/CPU when they deploy a cluster.                                           |
| *Processor*              | The processor type, GPU/CPU. In this example, it is a **Nvidia L4** GPU.                                                                                                          |
| *Processor Quantity*     | Number of processors available for the worker.                                                                                                                                    |
| *POTL*                   | Proof of Timelock, verifies the uptime for the worker. This can be executed against a hired worker.                                                                               |
| *POW*                    | TFLOPs Proof, tasks the worker must solve to verify the worker. To learn more about PoW, see [Proof of Work](/docs/proof-of-work). This is never executed against a hired worker. |
| *Total Score*            | The score your worker receives based on its performance as measured by **POW** and **POTL**.                                                                                      |
| *Rewarded*               | The amount of IO Coin the worker earned based on **Total Score**.                                                                                                                 |

### Exceptions

**Exempt-Hired**

If a worker was nominated for a Block Reward, but was hired by a customer during the evaluation hour, io.net exempts the worker from the *Proof of Work*. The exemption occurs so the worker can successfully complete the job for the customer.

In the example below, the **IO Worker Block Reward** is marked as **Completed**. The worker was hired by a customer so no PoW tasks were assigned. *Uptime* was tested during the hour and the worker satisfied the requirement. Since it was successful, a reward was granted.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7f01b1e-exempt-hired.png?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=784eada245f05d210c7d74c681961717" alt="" className="mx-auto" style={{ width:"50%" }} data-og-width="1026" width="1026" data-og-height="2012" height="2012" data-path="images/docs/7f01b1e-exempt-hired.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7f01b1e-exempt-hired.png?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=80d93a947fe8363e707e22a2eef500c6 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7f01b1e-exempt-hired.png?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=2faa3fa9dad5169dd9ec770aa8ceb794 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7f01b1e-exempt-hired.png?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f403b1722cb7c106a7356bed545641a1 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7f01b1e-exempt-hired.png?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=667d047a78a08fe05096fa1c7052c3a2 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7f01b1e-exempt-hired.png?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=fde37e9070d74fc3425d9c7f30d2a219 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/7f01b1e-exempt-hired.png?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ef98dc12c2c0d15ac3ceb7f8bf3edab6 2500w" />
</Frame>

**Exempt-Headnode**

Headnodes must always be available for jobs. For this reason, PoW is not executed against headnodes when nominated for Block Rewards. *Uptime* (POTL) is tested during the evaluation. In the example below, the headnode satisfied the requirement. Since it was successful, a reward was granted.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=e7efaa727650495af771dd62547e4b7e" alt="" className="mx-auto" style={{ width:"51%" }} data-og-width="802" width="802" data-og-height="1172" height="1172" data-path="images/docs/b33bbd7-ex_headnode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=687a6d259f2ac0e79a596b381bb57521 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=cb72b9020c3eabfe3ae21ffa7e0eb2b3 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=fb81d135c94dacc9df84425e5337e829 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=2b4e09c43c7c650a8d6c50e0fc3dc317 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=169255a05d9865e30ba2eba980cb5cb9 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=0b7d67a3760372b377a1a2c82ab8a14c 2500w" />
</Frame>
