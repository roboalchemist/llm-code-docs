# Source: https://io.net/docs/guides/explorer/block-rewards-page.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Block Rewards

## Table of Contents

* [Block Rewards Dashboard](/guides/explorer/block-rewards-page#block-rewards-dashboard)
  * [Key Features of the Dashboard](/guides/explorer/block-rewards-page#key-features)
  * [Block Rewards Table](/guides/explorer/block-rewards-page#block-rewards-table)
* [Block Rewards View Page](/guides/explorer/block-rewards-page#view-page)
* [Base Score Calculation](/guides/explorer/block-rewards-page#base-score-calculation)
* [Exceptions & Special Cases](/guides/explorer/block-rewards-page#exceptions--special-cases)
  * [Device Eligibility Rules & Updates](/guides/explorer/block-rewards-page#device-eligibility-rules--updates)
  * [Wallet Requirement for Rewards](/guides/explorer/block-rewards-page#wallet-requirement-for-rewards)

## Block Rewards Dashboard

The Block Rewards Dashboard offers a detailed overview of the rewards earned by devices contributing computational power to the IO.net ecosystem. This page helps you track their earnings, understand reward calculations, and monitor key performance metrics. Whether you are an individual worker or managing multiple devices, the dashboard provides full transparency on reward distribution.

To view the Block Rewards tab, go to **io.net** > **IO Explorer** > **Block Rewards Tab**.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/93049e6ee17fd0d698c45a7b2a50730844d4cc982f504888dfef7ab0f2050409-Dashboard1.png?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=0656a31c85725d98cf6736f58cd51a1f" alt="" data-og-width="2367" width="2367" data-og-height="390" height="390" data-path="images/docs/93049e6ee17fd0d698c45a7b2a50730844d4cc982f504888dfef7ab0f2050409-Dashboard1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/93049e6ee17fd0d698c45a7b2a50730844d4cc982f504888dfef7ab0f2050409-Dashboard1.png?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=59e4f9abede2d8f2821641eb188866f4 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/93049e6ee17fd0d698c45a7b2a50730844d4cc982f504888dfef7ab0f2050409-Dashboard1.png?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=5cf91e7a88b19234c34917f378b0059d 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/93049e6ee17fd0d698c45a7b2a50730844d4cc982f504888dfef7ab0f2050409-Dashboard1.png?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=961adb426796395a9e97782509ca9abb 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/93049e6ee17fd0d698c45a7b2a50730844d4cc982f504888dfef7ab0f2050409-Dashboard1.png?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=ffcd6c3462a9ab56bcf3a570260efd11 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/93049e6ee17fd0d698c45a7b2a50730844d4cc982f504888dfef7ab0f2050409-Dashboard1.png?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=0af1caec6a17724b2c7b508298bc2384 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/93049e6ee17fd0d698c45a7b2a50730844d4cc982f504888dfef7ab0f2050409-Dashboard1.png?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=9438b70db00a3aff80046e47e6ead2af 2500w" />
</Frame>

**Key Features**

The Block Rewards Dashboard presents essential metrics and data points related to device earnings and overall network activity. Each feature provides critical insights into the network's devices' performance and efficiency.

* **Total Coins Distributed (In \$IO Coins):** Shows the total amount of **\$IO coins** allocated to all eligible workers since the start of the reward system.
* **Today's Coins Distributed (In \$IO Coins):** Shows the total amount of **\$IO coins** rewarded to workers within the current 24-hour period.
* **Total Blocks Computed:** Indicates the number of computational blocks successfully processed within the IO.net network.
* **Next Block Start Time:** Displays the scheduled start time for the next computational block.
* **Total Unique Workers Paid:** Represents the total number of distinct workers that have received **\$IO coin** rewards since the network began distributing payments.
* **Today's Unique Workers Paid:** Represents the total number of distinct workers that have received \$IO coin rewards since the network began distributing payments.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1e0a78ebc3e3f3144d17f20dec63bd7e85c3b6aea50b0523e4059d12a38f7771-Dashboard2.jpg?fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=17e36027f1622bd91f286bcf047f421a" alt="" data-og-width="1934" width="1934" data-og-height="369" height="369" data-path="images/docs/1e0a78ebc3e3f3144d17f20dec63bd7e85c3b6aea50b0523e4059d12a38f7771-Dashboard2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1e0a78ebc3e3f3144d17f20dec63bd7e85c3b6aea50b0523e4059d12a38f7771-Dashboard2.jpg?w=280&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=55de51e83c26229bfecf53bb81a14e66 280w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1e0a78ebc3e3f3144d17f20dec63bd7e85c3b6aea50b0523e4059d12a38f7771-Dashboard2.jpg?w=560&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=d2f72805a7c79325605085e740a42074 560w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1e0a78ebc3e3f3144d17f20dec63bd7e85c3b6aea50b0523e4059d12a38f7771-Dashboard2.jpg?w=840&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=cf0345f9524df88b9838920c8cfbc738 840w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1e0a78ebc3e3f3144d17f20dec63bd7e85c3b6aea50b0523e4059d12a38f7771-Dashboard2.jpg?w=1100&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=5ab65db1d826756a6f578a8f49ca2eb6 1100w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1e0a78ebc3e3f3144d17f20dec63bd7e85c3b6aea50b0523e4059d12a38f7771-Dashboard2.jpg?w=1650&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=32a8893ed4a60a98d39fbc12db775643 1650w, https://mintcdn.com/ionet-cca8037f/-ylztZG_lN4iZVZo/images/docs/1e0a78ebc3e3f3144d17f20dec63bd7e85c3b6aea50b0523e4059d12a38f7771-Dashboard2.jpg?w=2500&fit=max&auto=format&n=-ylztZG_lN4iZVZo&q=85&s=a5fcafdd9fc8923fd19954a49fc98e88 2500w" />
</Frame>

**Block Rewards Table**

The Block Rewards Table offers a structured breakdown of each block's reward details, allowing you to track real-time data and understand their earnings.

| Field                      | Description                                                                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Status**                 | The current state of the block. Possible statuses: **In Progress, Processing, Completed.**                                                     |
| **Block ID**               | A unique identifier assigned to each processed block.                                                                                          |
| **Processed Time**         | The exact time the block was completed and verified.                                                                                           |
| **Total Rewards Emission** | The total amount of **\$IO coins** distributed for the block.                                                                                  |
| **Nominated Workers**      | The number of devices that were nominated for Block Rewards.                                                                                   |
| **Succeeded Workers**      | The number of devices that met all requirements and successfully received rewards.                                                             |
| **Failed Workers**         | The number of devices that did not meet **Proof-of-Work (POW)** or **Proof-of-Timelock (POTL)** requirements and thus did not receive rewards. |

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9ab37d488e05875b77201c674765b11466467cb4d167026d204fbe6e6e790fd-Dashboard3.jpg?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=9552e711a5d405e07355286efd703cb7" alt="" data-og-width="1940" width="1940" data-og-height="588" height="588" data-path="images/docs/c9ab37d488e05875b77201c674765b11466467cb4d167026d204fbe6e6e790fd-Dashboard3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9ab37d488e05875b77201c674765b11466467cb4d167026d204fbe6e6e790fd-Dashboard3.jpg?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=2213e27439fcb4ad3936dbc844e95cc5 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9ab37d488e05875b77201c674765b11466467cb4d167026d204fbe6e6e790fd-Dashboard3.jpg?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=81027440288edfd366f4649bd56c2d30 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9ab37d488e05875b77201c674765b11466467cb4d167026d204fbe6e6e790fd-Dashboard3.jpg?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=c081ddfb0b4858e85a41d35104d7c9d5 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9ab37d488e05875b77201c674765b11466467cb4d167026d204fbe6e6e790fd-Dashboard3.jpg?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=7498ab8b7de83b26f4c6cbae17bbc716 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9ab37d488e05875b77201c674765b11466467cb4d167026d204fbe6e6e790fd-Dashboard3.jpg?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=b4abc639c0f0cd34597a65c7e897c6a4 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c9ab37d488e05875b77201c674765b11466467cb4d167026d204fbe6e6e790fd-Dashboard3.jpg?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=af3a1ca6337ad0689a088c908a0ca4dc 2500w" />
</Frame>

## View Page

The **Block Rewards View Page** offers a detailed breakdown of reward calculations for individual workers and devices. Each entry includes specific performance metrics and reward status updates.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/537a889949e9125f18fb5dba3006a1d8bbd1d38978c4eae374c797f05c4c0303-Dashboard4.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=4312e950e229ca814b09e49bf7f60dd0" alt="" data-og-width="1938" width="1938" data-og-height="699" height="699" data-path="images/docs/537a889949e9125f18fb5dba3006a1d8bbd1d38978c4eae374c797f05c4c0303-Dashboard4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/537a889949e9125f18fb5dba3006a1d8bbd1d38978c4eae374c797f05c4c0303-Dashboard4.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e2a77abb5df3b30e8be5051349c2e3ff 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/537a889949e9125f18fb5dba3006a1d8bbd1d38978c4eae374c797f05c4c0303-Dashboard4.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=f4b255405881b95037421d8ba808899b 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/537a889949e9125f18fb5dba3006a1d8bbd1d38978c4eae374c797f05c4c0303-Dashboard4.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=93e586f2c2b85e4a047219e6dce87c52 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/537a889949e9125f18fb5dba3006a1d8bbd1d38978c4eae374c797f05c4c0303-Dashboard4.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=859c359b3d3dc48dd7646612dde33ccd 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/537a889949e9125f18fb5dba3006a1d8bbd1d38978c4eae374c797f05c4c0303-Dashboard4.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=1d2ccadf69da4c0e038dd872aaf52931 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/537a889949e9125f18fb5dba3006a1d8bbd1d38978c4eae374c797f05c4c0303-Dashboard4.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=9a9d6ec37bb54da2215cf2c556912924 2500w" />
</Frame>

### Key Metrics

| Field                        | Description                                                                                                                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Block Reward**             | Displays the reward status of a device. Status can be **Completed** (successful reward) or **Failed** (if the device does not meet **Proof-of-Work (POW)** and **Proof-of-Timelock (POTL)** requirements). |
| **Block ID**                 | A unique identifier assigned to each block in the blockchain.                                                                                                                                              |
| **Connectivity Tier**        | The assigned connectivity level of the worker. Customers select this when reserving a GPU/CPU.                                                                                                             |
| **Processor**                | The type of processor used (e.g., Nvidia L4 GPU).                                                                                                                                                          |
| **Processor Quantity**       | The number of processors allocated to the worker.                                                                                                                                                          |
| **POW (zkTFLOPs Proof)**     | A computational task verifying the worker's performance. Not executed against hired workers. ([Learn more](/guides/workers/proof-of-work))                                                                 |
| **POTL (Proof of Timelock)** | Ensures the worker remains active for a set duration. May be executed against hired workers.                                                                                                               |
| **Device Base Score**        | A score based on hardware quality, quantity, and connectivity tier. Used to determine earnings.                                                                                                            |
| **Device Normalized Score**  | Represents potential earnings, ensuring fairness across the network. Adjusted based on total emissions and device performance.                                                                             |
| **Rewarded Amount**          | Displays the IO Coin earned based on total device score.                                                                                                                                                   |

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0cb663c27871259fa1ac6f43021f38bad8eb71fcacc3f02b6f38d59e96f94c21-Dashboard5.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=129a1d2e11cedb24af850970c544ad1a" alt="" className="mx-auto" style={{ width:"54%" }} data-og-width="635" width="635" data-og-height="1077" height="1077" data-path="images/docs/0cb663c27871259fa1ac6f43021f38bad8eb71fcacc3f02b6f38d59e96f94c21-Dashboard5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0cb663c27871259fa1ac6f43021f38bad8eb71fcacc3f02b6f38d59e96f94c21-Dashboard5.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=753d138a90b06ef59d3590b4cba26573 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0cb663c27871259fa1ac6f43021f38bad8eb71fcacc3f02b6f38d59e96f94c21-Dashboard5.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=dbfe856c287f85fd9dc885752c60b722 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0cb663c27871259fa1ac6f43021f38bad8eb71fcacc3f02b6f38d59e96f94c21-Dashboard5.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=75fa4b0bba30bb8487222754a191e601 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0cb663c27871259fa1ac6f43021f38bad8eb71fcacc3f02b6f38d59e96f94c21-Dashboard5.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=4ec898e4a35571cb808c7322557d4159 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0cb663c27871259fa1ac6f43021f38bad8eb71fcacc3f02b6f38d59e96f94c21-Dashboard5.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=a0de01ebcb52eb5dc0d7bc13bcccbbaf 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0cb663c27871259fa1ac6f43021f38bad8eb71fcacc3f02b6f38d59e96f94c21-Dashboard5.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=802c4884942db88111f71e6332b9f105 2500w" />
</Frame>

## Base Score Calculation

The Device Base Score is determined using the following formula:

```
+(0.02 _ (connectivity_tier_number / 4.0))  
+ (2.0 _ hardware_multiplier _ processor_quantity)) _ 100 + (0.05 _ was_hired)) _ 10
```

*⚠ This formula is subject to change by the IOG Foundation to optimize incentives within the IO.net ecosystem.*

**Example calculation:**

* A GPU device with a base score of 8150
* Total network GPU score: 115M
* Normalized Score: (8150/115M) /\* 8M = 569

### Exceptions & Special Cases

**Headnode Exemptions**

Head nodes must stay online to support jobs. Therefore, **Proof of Work (POW)** is not executed against them, but **Proof of Timelock (POTL)** is needed. If the head node meets the uptime requirements, it will receive rewards.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=e7efaa727650495af771dd62547e4b7e" alt="" className="mx-auto" style={{ width:"49%" }} data-og-width="802" width="802" data-og-height="1172" height="1172" data-path="images/docs/b33bbd7-ex_headnode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=687a6d259f2ac0e79a596b381bb57521 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=cb72b9020c3eabfe3ae21ffa7e0eb2b3 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=fb81d135c94dacc9df84425e5337e829 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=2b4e09c43c7c650a8d6c50e0fc3dc317 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=169255a05d9865e30ba2eba980cb5cb9 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/b33bbd7-ex_headnode.png?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=0b7d67a3760372b377a1a2c82ab8a14c 2500w" />
</Frame>

**Device Eligibility Rules & Updates**

To maintain fairness and align with evolving infrastructure needs, the following rules apply:

##### Minimum Uptime Requirements:

* Devices must meet a **minimum uptime (e.g., 3-5 hours)** to be eligible for Block Rewards.
* After **Ignition Reward S3**, additional cooldown periods may be enforced.

##### Ineligible Devices:

* **M3 devices** should have at least 16GB RAM for optimal performance.

**Wallet Requirement for Rewards**

* A valid SOL address is required to calculate Block Rewards.
* Automated payouts are not yet enabled, so you should consider using a self-custodial wallet.

***
