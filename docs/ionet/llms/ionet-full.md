# Ionet Documentation

Source: https://io.net/docs/llms-full.txt

---

# Overview
Source: https://io.net/docs/guides/announcements/announcements

Stay up to date with the latest updates, migrations, and important news from io.net.

This section provides key information on platform upgrades, new features, and essential changes that impact suppliers and users.

<Update label="Ocotober 1, 2025">
  ### Service Update: Bare Metal (Self Serve) Moving Forward

  Bare Metal on Demand will no longer be available starting Wednesday,  October 1, 2025.

  * If you need Bare Metal, please contact our sales team at [business@io.net](mailto:business@io.net) for managed services.
  * For self-service compute, check out our latest option: [Virtual Machines on Demand](/guides/clouds/deploy-vm-on-demand).
</Update>

<Update label="May 2025">
  ### Important: Action Required for Expired Refresh Tokens

  Some suppliers using older refresh tokens (generated before our switch to non-expiring tokens) may experience token expiration after 365 days — causing worker downtime and authentication errors.

  For full details and steps to resolve the issue, please refer to the [Action Required for Expired Refresh Tokens](/guides/announcements/important-action-required-for-expired-refresh-tokens)
</Update>

<Update label="April 2025" description>
  ### Supplier Migration to M4 Series – Upgrade Now!

  Suppliers on io.net can now seamlessly upgrade their existing inventory of M2 Pro, M2 Max, and M2 Ultra devices to the cutting-edge M4 series. This transition offers enhanced performance, improved efficiency, and ensures continued eligibility for earnings on the io.net platform.

  For full details on the migration process, please refer to the [Supplier Migration Guide: Upgrading to M4 Series Devices](/guides/announcements/supplier-migration-guide-upgrading-to-m4-series-devices)
</Update>


# Action Required for Expired Refresh Tokens
Source: https://io.net/docs/guides/announcements/important-action-required-for-expired-refresh-tokens

May 2025

We’ve identified that some suppliers who generated their refresh tokens before we switched to non-expiring tokens may encounter token expiration after 365 days. This can lead to worker downtime and authentication errors such as:

<CodeGroup>
  ```json json theme={null}
  {"error":"invalid_grant", "error_description":"Unknown or invalid refresh token."}
  ```
</CodeGroup>

**Error:** *Authentication failed. Your token might be invalid or expired. Please re-generate one and try again. Use `--no_cache=true` flag to re-authenticate.*

To resolve this, please follow these steps to generate a new **non-expiring** refresh token and restart your worker:

**Step 1:** Run the `io.net worker` CLI binary with the `--no_cache=true` flag to initiate token regeneration.

**Step 2:** Provide any required details to the CLI. Once successful, your worker will launch using the refreshed token.

<Info>
  After completing the initial interactive authentication, you’ll see a new --token value. You can reuse this token to update other devices silently.
</Info>

Thank you for your continued support of io.net. The io.net Team


# Supplier Migration Guide: Upgrading to M4 Series Devices
Source: https://io.net/docs/guides/announcements/supplier-migration-guide-upgrading-to-m4-series-devices

April 2025

Suppliers on io.net can now seamlessly upgrade their existing inventory of **M2 Pro, M2 Max, and M2 Ultra** devices to the cutting-edge **M4 series.** This transition ensures enhanced performance, improved efficiency, and continued eligibility for earnings on the io.net platform.

<Warning>
  **Important Pre-Migration Requirement**:

  Before initiating the migration, ensure your current M2 worker has been actively earning Block Rewards for at least the last 3 continuous hours (i.e., passing PoW tests and contributing work).

  If this condition is not met, the new M4 device will be automatically blocked during the migration process.
</Warning>

### Important Migration Dates:

* **Migration Start:** UTC 09:00 AM on April 3rd, 2025
* **End of Support for M2 Devices:** UTC 23:59:59 on April 21st, 2025
* **Migration Window Closes:** UTC 23:59:59 on April 21st, 2025

<Info>
  Only currently connected devices with full stake are eligible for migration.
</Info>

### M4 Series Device Options

| Device | Earning Multiplier | Ray Cluster Pricing | Staking Requirement |
| ------ | ------------------ | ------------------- | ------------------- |
| M4     | 0.5x               | \$0.10/hour         | \$IO 200            |
| M4 Pro | 0.75x              | \$0.13/hour         | \$IO 200            |
| M4 Max | 1x                 | \$0.15/hour         | \$IO 200            |

### Migration Process:

##### Step 1: Disconnect Your M2 Device

Before migrating, ensure your **M2 Pro, M2 Max, or M2 Ultra** device is **disconnected** from the io.net network.

##### Step 2: Execute the Migration Command

Once your M2 device is disconnected, run the following command on your new **M4, M4 Pro, or M4** Max device:

<CodeGroup>
  ```curl curl theme={null}
  ./io_net_launch_binary_mac --device_id={same device id} --user_id={same user_id} 
  --operating_system="macOS" --usegpus=false --device_name="{same device name}"
  ```
</CodeGroup>

##### Step 3: Ensure Proper Configuration

Your new **M4 series** device should be **correctly configured** with a **stable internet connection** to avoid loss of **Block Rewards** during migration.

### Benefits of Migration:

When migrating to the M4 series, your new device will:

* **Retain** **the same device\_id**
* **Retain the same \$IO staked** (M2 Pro/Max staking requirements match M4/M4 Pro/M4 Max)
* **For M2 Ultra migrations**: The excess 50 \$IO (beyond the minimum staking requirement) will be withdrawable without a cooldown period after approximately 24-48 hours post-migration./*/*

### Additional Update:

This migration ensures suppliers remain operational on io.net while benefiting from the **next-generation M4 series devices**. We appreciate your continued support as we drive decentralized computing forward.

**Thank you for your continued partnership and support as we move towards a more innovative future together.**

If you have any questions, please contact io.net support. The io.net Team


# Architectural Layers
Source: https://io.net/docs/guides/architecture/io-architecture

The IO Portal architecture is a multi-layered, cohesive structure that provides a seamless, secure, and efficient user experience. Each layer has a distinct role, working in tandem to ensure the system's optimal performance. The architecture is built upon modern technologies, ensuring scalability, reliability, and robustness.

<Frame>
  <img alt="" />
</Frame>

### User Interface

This layer is the visual gateway for users. It comprises the ***Public website***, ***Customers area***, and ***GPU providers area (Workers)***. The design is intuitive and user-centric, ensuring easy navigation and interaction.

> Tech Stack: ReactJS, Tailwind, web3.js, zustand.

### Security Layer

A pivotal layer ensuring the system's integrity and safety. It encompasses a **Firewall** for network protection, an **Authentication Service** for user validation, and a **Logging Service** for tracking activities.

> Tech Stack: Firewall (pfSense, iptables), Authentication (OAuth, JWT), Logging Service (ELK Stack, Graylog).

### API Layer

Serving as the communication bridge, this layer has multiple facets: ******Public API for the website, Private APIs for Workers/GPU Providers and Customers, andInternal APIs******  for Cluster Management, Analytics, and Monitoring/Reporting.

> Tech Stack: FastAPI, Python, GraphQL, RESTful services, gunicorn, solana.

### Backend Layer

The powerhouse of the system. It manages Providers (Workers), Cluster/GPU operations, Customer interactions, Fault Monitoring, Analytics, Billing/Usage Monitoring, and Autoscaling.

> Tech Stack: FastAPI, Python, Node.js, Flask, solana, IO-SDK (a fork of Ray 2.3.0), Pandas.

### Database Layer

The data repository of the system. It uses **Main storage** for structured data and **Caching** for temporary and frequently accessed data.

> Tech Stack: Postgres (Main storage), Redis (Caching).

### Message Broker/Task Layer

This layer orchestrates asynchronous communications and task management, ensuring smooth data flow and efficient task execution.

> Tech Stack: RabbitMQ (Message Broker), Celery (Task Management).

### Infrastructure Layer

The foundational layer. It houses the **GPU Pool** with hardware from our verified partners. Orchestration tools manage deployments, while Execution/ML Tasks handle computations and machine learning operations. Additionally, it provides ***Data Storage solutions***. GPU performance is monitored using Nvidia-smi or NVIDIA DCGM.

> Tech Stack:
>
> * GPU/CPU Pool
> * Orchestration: Kubernetes, Prefect, Apache Airflow
> * Execution/ML Tasks: Ray, Ludwig, Pytorch, Keras, TensorFlow, Pandas
> * Data Storage: Amazon S3, Hadoop HDFS
> * Containerization: Docker
> * Monitoring: Grafana, Datadog, Prometheus, NVIDIA DCGM

### IO-SDK: The Powerhouse Behind io.net

IO-SDK is our specialized fork of Ray, a core technology driving io.net's capabilities. Embracing Ray's native parallelism, IO-SDK effortlessly parallelizes Python functions, enabling dynamic task execution. Its in-memory storage ensures rapid data sharing between tasks, eliminating serialization delays. The dynamic auto-scaling feature means IO-SDK can quickly adapt to computational demands. Moreover, it is not just limited to Python; the language versatility and integration capabilities with leading ML frameworks like PyTorch and TensorFlow make it a robust and flexible choice. Whether on a single machine or a vast cloud platform, IO-SDK ensures io.net's scalability and performance.

> Together, these layers, powered by the mentioned tech stacks, form a robust and scalable architecture for the io.net Portal, ensuring it meets the demands of modern users.


# IO Network
Source: https://io.net/docs/guides/architecture/io-network

This article explores the concepts of mesh VPN networks and how we leverage their benefits to improve performance and reliability in the io.net protocol.

**IO Network** is a cutting-edge networking backend that utilizes a secured mesh VPN to allow ultra-low latency communication between the antMiners nodes or 'workers'.

<Frame>
  <img alt="" />
</Frame>

### Understanding Mesh VPN Networks

A *Mesh VPN network* is a type of virtual private network (VPN) that connects nodes in a non-hierarchical, decentralized manner. Unlike traditional hub-and-spoke VPN architectures, which rely on a central concentrator or gateway, mesh VPN networks allow each node to connect directly to every other node in the network. This structure ensures data packets can travel along multiple paths, increasing redundancy, fault tolerance, and better load distribution.

<Frame>
  <img alt="" />
</Frame>

<Frame>
  <img alt="" />
</Frame>

#### Advantages of *Mesh VPN networks*:

1. **Robust**: Mesh networks are resilient to individual node failures, as there are multiple paths for data to travel. This redundancy ensures that the network remains operational when one or more nodes experience issues.
2. **Scalability**: Adding new nodes to a mesh network does not significantly impact the overall network performance, making it easy to expand the network as needed.
3. **Low Latency**: By connecting nodes directly, mesh networks reduce the number of *hops* needed for data to travel between nodes. This reduction in latency enhances the performance of real-time applications and distributed computing.
4. **Optimized Load Distribution**: Mesh networks distribute traffic more evenly across nodes, preventing bottlenecks and ensuring optimal performance.

### Implementation of the *io.net Network*

We built an io.net network that creates an efficient, resilient, and scalable networking backend. By adopting mesh networking principles, io.net delivers the following benefits to its users:

1. **Enhanced Performance**: io.net's mesh network architecture minimizes latency by allowing data to travel along the most efficient paths, optimizing application performance and user experience.
2. **Improved Resilience**: The decentralized nature of io.net's mesh network ensures that it remains operational even when individual nodes fail. This resilience translates to increased reliability and uptime for users.
3. **Seamless Scalability**: io.net's mesh network can easily grow to accommodate more nodes as the user base expands, ensuring consistent performance and adaptability.
4. **Distributed Computing**: By allowing direct connections between nodes, io.net's mesh network facilitates efficient distributed computing, which enables resource sharing and collaborative processing across the network.

### Decentralized Architecture and Privacy

The decentralized nature of mesh VPN networks contributes to their security and privacy. Some notable aspects include:

1. **No Single Points of Failure**: The absence of a central concentrator or gateway in mesh VPN networks eliminates the risk of a single point of failure, ensuring that the network remains operational even if individual nodes are compromised or experience issues.
2. **Anonymity**: Since data travels along multiple paths within the mesh network, it becomes more difficult for an attacker to trace the origin or destination of the data, enhancing privacy for users.
3. **Traffic Obfuscation**: Mesh VPN networks can employ techniques like packet padding and timing obfuscation to make it harder for eavesdroppers to analyze traffic patterns and identify specific users or data streams.

### Network Access Control and Monitoring

Next for io.net Network includes:

1. **Access Control Lists (ACLs)**: Nodes must define and enforce ACLs to restrict communication between specific nodes or groups of nodes, ensuring that sensitive data is only accessible to authorized parties and only available during the time they are hired for a specific cluster.
2. **Regular Auditing and Logging**: To maintain security and compliance, the io.net mesh VPN must be configured to allow us to perform regular audits and maintain logs of network activities, enabling administrators to identify and address potential vulnerabilities or breaches.


# IO Tunnels
Source: https://io.net/docs/guides/architecture/io-tunnels

Reverse tunnels technology provides a way to bypass firewall and NAT restrictions, enabling secure access to remote resources. This article discusses the concept of reverse tunnels, how they work, and how io.net uses them to simplify engineer access to AntMiners Clusters.

<Frame>
  <img alt="" />
</Frame>

### Understanding Reverse Tunnels

A *Reverse tunnel* is a method to establish a secure connection from a client to a remote server by opening an inbound connection on the server side. This is the opposite of a conventional forward tunnel, where a client opens a connection to the server. By using reverse tunnels, engineers can access remote resources behind NAT routers and firewalls without the need for complex network configurations.

### How Reverse Tunnels Work

1. The remote server (IO Worker) initiates a connection to the client (engineer's machine) through an intermediate server (io.net server).
2. The io.net server listens for incoming connections from both the client and the remote server. Once the connection is established, data can be exchanged between the client and the remote server through the tunnel as if they were directly connected.

The io.net network employs reverse tunnels to simplify access to io.net miners for engineers.

The process involves:

1. The IO Worker establishes a connection to the io.net server, creating a reverse tunnel.
2. The engineer's machine connects to the io.net server as an intermediary.
3. The io.net server routes traffic between the engineer's machine and the IO Worker through the reverse tunnel. Engineers can securely access and manage IO Workers without the need for complex network configurations or dealing with firewalls and NAT restrictions.

### Benefits of Reverse Tunnels

1. **Simplified Access**: Engineers can easily access IO Workers without worrying about network restrictions, port forwarding, or VPNs.
2. **Enhanced Security**: Reverse tunnels provide a secure communication channel, ensuring data privacy and integrity.
3. **Scalability**: io.net can manage multiple IO Workers simultaneously, allowing engineers to work efficiently.
4. **Flexibility**: Reverse tunnels work across various platforms, ensuring compatibility with different operating systems and environments.


# Overview
Source: https://io.net/docs/guides/block-rewards/block-rewards



## Table of Contents

* [What Are Block Rewards](/guides/block-rewards/block-rewards#what-are-block-rewards)
* [Block Rewards Allocation](/guides/block-rewards/block-rewards#block-rewards-allocation)
* [Block Reward Nomination Requirements](/guides/block-rewards/block-rewards#block-reward-nomination-requirements)
* [Block Rewards Nomination Checklist](/guides/block-rewards/block-rewards#block-rewards-nomination-checklist)
* [Wallets](/guides/block-rewards/block-rewards#wallets)

### What Are Block Rewards?

Block rewards are payments made to suppliers who provide their GPUs or CPUs to our network. This incentivizes supply-side network growth. These rewards are accrued hourly in ***\$IO***, following a predefined emission schedule. Rewards are potentially subject to slashing before distribution.

### Block Rewards Allocation

Block Rewards are credited to Suppliers on an hourly basis for making their GPU or CPU available on the *IOG Network*, thereby incentivizing supply-side network growth. This payout is in **IO Coin** and follows a predetermined emission schedule. The current allocation of block rewards from each hourly emission is:

* 95% to GPUs
* 5% to CPUs

The ratio of rewards may be adjusted in the future to manage network growth.

To learn more, see [IO Coin](https://internet-of-gpus.readme.io/docs/what-is-io-coin).

### Initial Block Reward

**The first Block Reward was created on June 25th 2024 12:00 UTC.**

We will calculate and publish the initial block rewards, and block rewards use a claim mechanism that is similar to the *Ignition Program*. The first 7 days of block rewards were claimable together with *Ignition Reward Season 3*. Block Rewards for June 25th - June 30th will also be claimable.

<Info>
  IO Device Level staking/Minimum staking is now required for Block Rewards. To learn more about staking, see [IO Staking](/docs/io-staking).
</Info>

*IOG Foundation* provides emission rewards to incentivize the correct growth of the IO ecosystem. To better align with *Ignition Reward Season 3*, the *IOG Foundation* has not requested io.net to cap the amount of devices eligible for block rewards. In the future, the *IOG Foundation* will monitor the reward distribution and may potentially cap the amount of devices eligible for the top percentage of nodes. A device cap is used to increase the alignment of the network's structure.

### Block Reward Nomination Requirements

The requirements below must be met to be nominated for a Block Reward:

* Device *Uptime* must be green for the past **5 hours**.
* The minimum stake for the device must be met. To learn more about staking, see [IO Staking](/guides/staking/io-staking).
* The account holder for the device must have a valid Solana wallet.
* The device’s status is **NOT** terminated or unsupported.
* The device’s hardware multiplier is greater than **0**.
* The device’s connectivity tier is greater than **0**.

<Info>
  When a block is about to close, we test your device for *Uptime* and *PoW* again.
</Info>

### Block Rewards Nomination Checklist

Click the caret on the right side of the status row (**Eligible** in the example) to open the **Block Rewards Nomination Checklist**. Each step of the verification status is displayed, with a green or red check that indicates success or failure. The checklist displays the **current status** of the device's eligibility for a block reward. In the example case below, if a new block was opening, this device would be eligible.

The **Block Rewards Nomination Checklist** is designed to offer total transparency into the Block Reward nomination process.

<Frame>
  <img alt="" />
</Frame>

**Device Limitations**

* M3 devices with 8GB memory can be configured by users for higher memory. The minimum configuration should be 16GB of memory.
* As of July, 5th, we removed Block Reward eligibility for Threadrippers. This is due to reports that malicious actors tried to inject Ryzen Threadripper devices into Block Rewards. We will reevaluate this and restore this option in the future.

### Wallets

Wallets with *Exchange Deposit Addresses* (Custodial wallets) are not supported. To collect Block Rewards, worker earnings, or seasonal events, connect a *Web3 wallet* (Self-Custodial wallet) in your ***Account Settings***. Exchange Deposit Addresses are not supported because airdrop claims require a smart contract interaction.

<Warning>
  We do not support Exchange Deposit Addresses (Custodial wallets) for Block Rewards. If you connect a wallet with an Exchange Deposit Address to your account in ***Account Settings***, you will not be able to claim Block Rewards, seasonal events, nor worker earnings. If this is the case, please change it to a Self-Custodial wallet as soon as possible.
</Warning>


# Monitor Block Rewards
Source: https://io.net/docs/guides/block-rewards/monitor-block-rewards



## Table of Contents

* [Block Rewards Tab](/guides/block-rewards/monitor-block-rewards#block-rewards-tab)
* [Block Details Table](/guides/block-rewards/monitor-block-rewards#block-details-table)
* [Block Reward Details](/guides/block-rewards/monitor-block-rewards#block-reward-details)
  * [Exceptions](/guides/block-rewards/monitor-block-rewards#exceptions)

### Block Rewards Tab

The Block Rewards tab provides a transparent view of io.net's Block Rewards and coin emissions. Users can consult this information to monitor worker nominations and their status. Users can track the performance and success rates for worker nominations and block completion. Information on coin emissions and block rewards provide transparency about io.net network’s health.

The example below shows the **Block Rewards** tab, with each section explained in detail afterward.

<Frame>
  <img alt="" />
</Frame>

The top section of the **Block Rewards** tab provides real-time data about IO Coin emissions and blocks.

<Frame>
  <img alt="" />
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
  <img alt="" />
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
  <img alt="" />
</Frame>

The example below shows an IO Worker Block Reward. It provides details on the individual worker. You can click on the ***Device ID*** to view the info related to the worker in the **Workers** tab.

<Frame>
  <img alt="" />
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
  <img alt="" />
</Frame>

**Exempt-Headnode**

Headnodes must always be available for jobs. For this reason, PoW is not executed against headnodes when nominated for Block Rewards. *Uptime* (POTL) is tested during the evaluation. In the example below, the headnode satisfied the requirement. Since it was successful, a reward was granted.

<Frame>
  <img alt="" />
</Frame>


# Device Block Reward Multiplier
Source: https://io.net/docs/guides/block-rewards/proposed-device-block-reward-multiplier

A detailed comparison of 2025 block reward multipliers by device type, with upcoming staking-related adjustments.

The io.net block reward system uses performance-based multipliers to fairly distribute rewards across a wide variety of hardware types. These multipliers are designed to reflect the relative utility, compute performance, and cost-efficiency of each device, ensuring the most effective hardware for AI workloads is appropriately incentivized.

## Network Expansion and Updated Reward Structure

On **June 4, 2025 at 3 PM UTC**, io.net significantly expanded its network with the addition of over **800 NVIDIA H200 GPUs**. This is the largest single onboarding of enterprise-grade hardware in our history and is part of our commitment to scaling infrastructure for enterprise AI workloads like training and inference.

To ensure fair distribution of rewards as the network grows, the block reward system has been updated to reflect the following changes:

* Updated device multipliers
* New reward pool categories
* Temporary staking grace period

## Reward Pool Categories

| Pool Type                  | Description                                                                    |
| -------------------------- | ------------------------------------------------------------------------------ |
| 🔴 **No longer supported** | Low-tier or outdated devices. Multiplier set to 0. **No longer earn rewards.** |
| 🟡 **Community Pool**      | Consumer and mid-range devices. **Earn 5% of block rewards.**                  |
| 🟢 **Enterprise Pool**     | High-performance processors. **Earn 95% of block rewards.**                    |

## Device Earning Multiplier Comparison

#### 🔴 No longer supported

| Processor           | Current Multiplier | New Multiplier | Notes                                    |
| ------------------- | ------------------ | -------------- | ---------------------------------------- |
| M2 Max              | 1                  | 0              | Already dropped                          |
| M2 Pro              | 0.75               | 0              | Already dropped                          |
| M2 Ultra            | 1.25               | 0              | Already dropped                          |
| A10                 | 0.75               | 0              | Dropped due to lack of demand and supply |
| A10G                | 0.75               | 0              | Dropped due to lack of demand and supply |
| A16                 | 1                  | 0              | Dropped due to lack of demand and supply |
| A40                 | 2                  | 0              | Dropped due to lack of demand and supply |
| GeForce GTX 1080 Ti | 0.25               | 0              | Dropped due to lack of demand            |
| GeForce GTX 2080 Ti | 0.25               | 0              | Dropped due to lack of demand            |
| GeForce GTX 3050    | 0.25               | 0              | Dropped due to lack of demand            |
| GeForce GTX 3050 Ti | 0.25               | 0              | Dropped due to lack of demand            |

#### 🟡 Community Pool

| Processor                   | Current Multiplier | New Multiplier | Notes                                                |
| --------------------------- | ------------------ | -------------- | ---------------------------------------------------- |
| M3                          | 0.5                | 1              | TFLOP-based adjustment with bonus for unified memory |
| M3 Pro                      | 0.75               | 1.25           | TFLOP-based adjustment with bonus for unified memory |
| M3 Max                      | 1                  | 1.5            | TFLOP-based adjustment with bonus for unified memory |
| M4                          | 0.5                | 1              | TFLOP-based adjustment with bonus for unified memory |
| M4 Pro                      | 0.75               | 1.25           | TFLOP-based adjustment with bonus for unified memory |
| M4 Max                      | 1                  | 1.5            | TFLOP-based adjustment with bonus for unified memory |
| GeForce RTX 3060            | 0.25               | 0.75           | TFLOP-based adjustment                               |
| GeForce RTX 3060 Ti         | 0.25               | 0.75           | TFLOP-based adjustment                               |
| GeForce RTX 3070            | 0.25               | 1              | TFLOP-based adjustment                               |
| GeForce RTX 3070 Ti         | 0.25               | 1              | TFLOP-based adjustment                               |
| GeForce RTX 3080            | 0.25               | 1.5            | TFLOP-based adjustment                               |
| GeForce RTX 3080 Ti         | 0.25               | 1.75           | TFLOP-based adjustment                               |
| GeForce RTX 3090            | 0.5                | 1.75           | TFLOP-based adjustment                               |
| GeForce RTX 3090 Ti         | 0.5                | 2              | TFLOP-based adjustment                               |
| GeForce RTX 4060            | 0.25               | 1              | TFLOP-based adjustment                               |
| GeForce RTX 4060 Ti         | 0.25               | 1              | TFLOP-based adjustment                               |
| GeForce RTX 4070            | 0.25               | 1.5            | TFLOP-based adjustment                               |
| GeForce RTX 4070 Ti         | 0.25               | 2.5            | TFLOP-based adjustment                               |
| GeForce RTX 4080            | 0.5                | 2.75           | TFLOP-based adjustment                               |
| L4                          | 0.75               | 0.25           | TFLOP-based adjustment                               |
| RTX 4000                    | 0.4                | 0.75           | TFLOP-based adjustment                               |
| RTX 4000 SFF Ada Generation | 0.5                | 1              | TFLOP-based adjustment                               |
| RTX 5000                    | 0.25               | 1.5            | TFLOP-based adjustment                               |
| RTX 5000 Ada Generation     | 1.5                | 3              | TFLOP-based adjustment                               |
| RTX 6000 Ada Generation     | 2.5                | 4.5            | TFLOP-based adjustment                               |
| RTX A4000                   | 0.4                | 1.5            | TFLOP-based adjustment                               |
| RTX A5000                   | 0.75               | 1.5            | TFLOP-based adjustment                               |
| RTX A6000                   | 1.5                | 2              | TFLOP-based adjustment                               |
| Tesla T4                    | 0.4                | 0.5            | TFLOP-based adjustment                               |
| Tesla V100-PCIE-16GB        | 0.5                | 0.75           | TFLOP-based adjustment                               |
| Tesla V100-PCIE-32GB        | 0.75               | 0.75           | TFLOP-based adjustment                               |
| Tesla V100-SXM2-16GB        | 0.5                | 0.75           | TFLOP-based adjustment                               |
| Tesla V100-SXM2-32GB        | 0.75               | 0.75           | TFLOP-based adjustment                               |
| Tesla V100S-PCIE-32GB       | 0.75               | 0.75           | TFLOP-based adjustment                               |

#### 🟢 Enterprise Pool

| Processor          | Current Multiplier | New Multiplier | Notes                        |
| ------------------ | ------------------ | -------------- | ---------------------------- |
| L40S               | 2.25               | 3              | High-demand based adjustment |
| A100 80GB PCIe     | 5                  | 5              | No change                    |
| A100-PCIE-40GB     | 2                  | 2              | No change                    |
| A100-SXM4-80GB     | 5                  | 5              | No change                    |
| GeForce RTX 4090   | 0.75               | 1.25           | High-demand based adjustment |
| GeForce RTX 4090 D | 0.75               | 1.25           | High-demand based adjustment |
| H100 80GB HBM3     | 10                 | 10             | No change                    |
| H100 PCIe          | 10                 | 10             | No change                    |
| H100 80G PCIe      | 10                 | 10             | No change                    |
| B200               | 30                 | 30             | No change                    |
| H200               | 15                 | 12             | High-demand based adjustment |

## Overview of Staking Requirements

<Warning>
  **Important changes to Staking Requirements coming July 1, 2025**

  Until **July 1, 2025**, staking requirements will continue to be calculated using the current earning multiplier.
</Warning>

To qualify for block rewards, each device must meet a minimum staking threshold calculated as follows:

* **Base Stake** **per processor**: 200 \$IO
* **Earning Multiplier**: Varies by device performance
* **Number of processors**: Total processors in the device

<Info>
  Minimum Stake = Base Stake × max(1, Earning Multiplier) × Number of processors
</Info>

Starting **July 1, 2025**, staking requirements may increase for some devices, as a new calculation logic will take effect.

For example:

* A device with **8** H100 **GPUs**, each having an earning **multiplier of 10** - Minimum Stake calculation: **200 × 10 × 8 = 16,000 \$IO**
* A device with **4** RTX 4070 **GPUs**, each having an earning **multiplier of 0.25** - Minimum Stake calculation: 200 × max(1, 0.5) × 4 = **200 × 1 × 4 = 800 \$IO**

<Info>
  Even if the earning multiplier is less than 1, the multiplier used in the calculation defaults to 1 to ensure a minimum stake of 200 \$IO per processor.
</Info>

### Upcoming Adjustments

With the integration of new H200 GPUs and the introduction of a ***Community Hardware Pool***, the following changes are anticipated:

* **Updated Multipliers:** Devices will have their earning multipliers recalibrated based on performance metrics.
* **Adjusted Staking Requirements:** As multipliers change, the corresponding staking requirements will also adjust.
* **Grace Period**: A one-month grace period will be provided before new staking requirements are enforced.

<Warning>
  **Higher multiplier** ≠ **always higher rewards.** \
  Actual rewards depend on several factors - including the number of eligible devices in a block, pool allocation (e.g., Community vs. Enterprise), and your device’s multiplier.
</Warning>

For more detailed information on staking requirements and calculations, refer to the [IO Staking Documentation](/guides/staking/io-staking).


# Confidential Compute Attestation
Source: https://io.net/docs/guides/clouds/confidential-compute-attestation-overview

Learn what confidential compute attestation is and how it can be utilized to verify secure workloads on io.net Cloud. Explore Trusted Execution Environments (TEE), GPU verification, and hardware-based security for sensitive compute.

## Overview

[io.net](http://io.net) provisioned *Confidential Compute VMs* are equipped with NVIDIA H200 GPUs featuring hardware-based confidential computing capabilities. This guide shows you how to verify that your GPUs are genuine NVIDIA hardware with confidential computing features properly enabled.

### Key Takeaways

* Understand why GPU verification is essential for confidential computing.
* Learn how to confirm GPU authenticity using cryptographic attestation.
* Follow clear, step-by-step instructions to run verification on your VM.

### Prerequisites

* SSH access to your Confidential Compute VM
* Python 3.7 or later (pre-installed on your VM)
* Basic command line understanding
* 5 minutes to perform the initial set up

## Why does GPU verification matter?

### Trust, but Verify

When running sensitive workloads on **Confidential Computing (CC)** infrastructure, it is not enough to rely on a provider’s assurances. You need **cryptographic proof** that the hardware is authentic, correctly configured, and operating in a secure state.

GPU attestation provides independent verification that:

* **The GPUs are genuine NVIDIA hardware** - not counterfeit, emulated, or misrepresented.
* **Firmware is intact and unmodified** - ensuring no tampering with GPU software or drivers.
* **Confidential computing features are enabled** - confirming that CC mode is active and functioning properly.
* **Hardware measurements match expected “golden” values** - validating that the GPU’s state aligns with NVIDIA’s reference integrity manifests.

### Security and Compliance

GPU attestation is a foundational security mechanism for confidential computing environments. It helps ensure:

* **Zero-trust architecture** - trust no component by default, verify every claim cryptographically.
* **Regulatory and compliance adherence** - meet requirements that mandate hardware verification.
* **Data protection** - guarantee that sensitive workloads run only on validated, trustworthy hardware.
* **Clear auditability** - produce cryptographic evidence for stakeholders, security teams, and auditors.

### How It Works

Attestation relies on **cryptographic proofs** that cannot be falsified, forged or altered. The verification process follows a clear chain of checks:

```
Your VM → Collect GPU Evidence → Verify Certificates
                                → Check Measurements
                                → Validate Signatures
                                → Result: Verified or Check Failed
```

**What gets verified:**

During attestation, the following elements are validated:

* **A four-level GPU certificate chain**, traced back to the NVIDIA Root Certificate Authority.
* **Certificate revocation status**, checked via OCSP to ensure no certificates have been revoked.
* **Driver firmware measurements**, consisting of 64 SHA-384 cryptographic hashes.
* **VBIOS firmware measurements**, consisting of 64 SHA-384 cryptographic hashes.
* **Digital signatures on all attestation evidence**, ensuring integrity and authenticity.

## What is GPU Attestation?

### Cryptographic Proof of Authenticity

GPU attestation is a cryptographic verification process rooted in **hardware-based trust**. It provides verifiable proof that a GPU is authentic, securely configured, and operating in a trusted state. Specifically, it validates four core properties:

<Tabs>
  <Tab title="1. Hardware Authenticity">
    Every NVIDIA GPU that supports Confidential Computing includes:

    * A **unique hardware identity** permanently embedded in silicon during manufacturing.
    * A **certificate chain** signed by NVIDIA’s Root Certificate Authority.
    * **Cryptographic keys** stored in tamper-resistant hardware.

    **What this proves:**\
    The GPU is genuine NVIDIA hardware, produced by NVIDIA, and not counterfeit or emulated.
  </Tab>

  <Tab title="2. Firmware Integrity">
    During attestation, the system:

    * Measures all GPU firmware using **SHA-384 cryptographic hashes.**
    * Compares measurements against NVIDIA’s **Reference Integrity Manifests (RIMs)**.
    * Verifies the **digital signatures** on the RIM files.

    **What this proves:**\
    The GPU firmware has not been modified, tampered with, or compromised.
  </Tab>

  <Tab title="3. Configuration State">
    The verification process confirms that:

    * **Confidential Computing (CC)** is enabled.
    * **Protected PCIe (PPCIE)** is correctly configured.
    * The GPU is operating in the **expected secure state**.

    <Note>
      In this context, **CC** refers to the general concept of **Confidential Compute**, where the GPU operates in a secure, protected environment. This is different from **CC mode** (also referred to as `CC State`), which is a specific configuration within the GPU.

      `CC State` cannot be enabled at the same time as **PPCIe**, the two modes are mutually exclusive.

      `CC State` specifically refers to scenarios where a single GPU (or multiple GPUs that are **NOT** NVLink-connected) is passed through directly to a virtual machine.
    </Note>

    **What this proves:**\
    Confidential Computing features are actively enabled and functioning, not merely claimed.

    <Accordion title="Further Reading on CC and PPCIe">
      **How CC and Protected PCIe (PPCIe) Work Together**

      GPU confidentiality is controlled through **two independent mechanisms**:

      * **CC (Confidential Compute / CC State)**
      * **PPCIe (Protected PCIe)**

      These settings determine *how* and *which* GPUs operate in confidential mode. Each GPU can have CC and PPCIe enabled or disabled independently, but only certain combinations are valid.

      * **CC = OFF, PPCIe = OFF**\
        No confidential computing is enabled.
      * **CC = ON, PPCIe = OFF**\
        Only a subset of GPUs is confidential. This mode is **NOT compatible with NVLink-connected GPUs**.
      * **CC = OFF, PPCIe = ON**\
        The **entire GPU set in the server, including NVLink connected GPUs**, operate in confidential mode.

        <Note>
          *This is the configuration used in our recommended setup.*
        </Note>
      * **CC = ON, PPCIe = ON**\
        This is an invalid configuration. The virtual machine will either fail to boot or the CUDA drivers will not load.
    </Accordion>
  </Tab>

  <Tab title="4. Freshness">
    Attestation uses a **nonce** (a cryptographic challenge) to:

    * Prevent replay attacks.
    * Ensure the evidence is current, not reused or pre-recorded.
    * Confirm that measurements reflect the GPU’s **current state**.

    **What this proves:**\
    The attestation is happening in real time on this specific GPU.
  </Tab>
</Tabs>

### Official NVIDIA Technology

**GPU attestation is performed using NVIDIA’s official tooling:**

* **Package:** `nv-attestation-sdk` (official NVIDIA Python SDK)
* **Source:** PyPI (Python Package Index)
* **Version:** 2.6.3 (as of December 2025)
* **License:** Apache 2.0
* **Repository:** [https://github.com/NVIDIA/nvtrust](https://github.com/NVIDIA/nvtrust)

This is **not a third-party tool**. It is NVIDIA’s production-ready attestation framework, used by enterprise customers worldwide.

### Standards-Based Approach

NVIDIA GPU attestation is built on widely adopted industry standards:

* **SPDM (Security Protocol and Data Model):** Version 1.1 for device authentication.
* **X.509 PKI:** Standard public key infrastructure for certificates.
* **OCSP:** Online Certificate Status Protocol for revocation checks.
* **TCG standards:** Trusted Computing Group measurement and attestation specifications.

## Quick Reference

**One-time setup (approximately 2–3 minutes):**

```bash theme={null}
mkdir -p ~/gpu-verification && cd ~/gpu-verification
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install nv-attestation-sdk
# Create the verify_gpu.py script (refer to Step 5 of the GPU Attestation and Verification Guide)
```

**Run verification (approximately 30 seconds):**

```bash theme={null}
cd ~/gpu-verification
source venv/bin/activate
python3 verify_gpu.py
```

**Successful verification output:**

```
✅ VERIFICATION SUCCESSFUL
This system has X genuine NVIDIA GPU(s)
with Confidential Computing features enabled and operational.
```

For a more comprehensive guide for verifying your Confidential Compute VM, refer to the [GPU Attestation and Verification Guide](/guides/clouds/confidential-compute-attestation-guide).

### Key Points

* **Official NVIDIA tooling** - uses the NVIDIA-provided `nv-attestation-sdk`.
* **Cryptographic assurance** - verification cannot be forged or bypassed.
* **Comprehensive validation** - certificates, firmware measurements, and signatures are all verified.
* **Fast execution** - completes in approximately 30 seconds after initial setup.
* **Self-contained operation** - runs entirely within the virtual machine without external accounts.

### Next Steps

1. Complete the one-time setup.
2. Run GPU verification on the virtual machine.
3. Integrate verification into the security or deployment workflow.
4. Perform verification before processing sensitive workloads.
5. Contact support if verification fails.

## FAQs

<AccordionGroup>
  <Accordion title="How often should verification be performed?" icon="comment-question">
    **Recommended frequency:**

    * **Daily:** Before processing sensitive or regulated workloads.
    * **After system changes:** Following any reboot, update, or migration.
    * **Initial provisioning:** When the virtual machine is first received.
    * **Compliance requirements:** As dictated by organizational security policies.

    **Why regular verification is important:**

    * Detects firmware tampering or unauthorized modification.
    * Confirms that *Confidential Computing* features remain enabled after updates.
    * Provides a verifiable audit trail for compliance and governance.
  </Accordion>

  <Accordion title="Can verification be automated?" icon="comment-question">
    **Yes.** Verification can be integrated into startup or pre-workload scripts.

    ```bash theme={null}
    #!/bin/bash
    # Example: Run verification before starting an application

    cd ~/gpu-verification
    source venv/bin/activate
    python3 verify_gpu.py

    if [ $? -eq 0 ]; then
        echo "✅ Verification passed. Starting workload."
        # Insert application startup commands here
    else
        echo "❌ Verification failed. Aborting startup."
        exit 1
    fi
    ```
  </Accordion>

  <Accordion title="Does verification impact GPU performance?" icon="comment-question">
    **No.** Verification:

    * Runs independently of GPU compute workloads.
    * Typically completes within 30–60 seconds.
    * Does not interfere with running applications.
    * Can be executed while GPUs are performing other tasks.
  </Accordion>

  <Accordion title="What should I do if verification fails?" icon="comment-question">
    **Immediate steps to follow:**

    1. Retry the verification once, as failures may be caused by transient network issues.
    2. Review system logs using `journalctl -xe`.
    3. Confirm that the NVIDIA driver is installed and functioning using `nvidia-smi`.
    4. Contact support and provide complete error messages and output.

    <Warning>
      Sensitive or confidential data should not be processed until verification succeeds.
    </Warning>
  </Accordion>

  <Accordion title="Is this the same verification NVIDIA uses?" icon="comment-question">
    **Yes.** This verification process uses:

    * The official NVIDIA Python SDK (`nv-attestation-sdk`).
    * The same verification logic used by NVIDIA enterprise customers.
    * Reference Integrity Manifests and certificate chains served directly by NVIDIA.
    * Industry-standard cryptographic validation mechanisms.

    This is not a third-party tool. It is NVIDIA’s official, production-grade attestation solution.
  </Accordion>

  <Accordion title="What exactly is verified?" icon="comment-question">
    The verification process validates the following components:

    **Hardware**

    * The GPU is genuine NVIDIA hardware, verified through a certificate chain to the NVIDIA Root Certificate Authority.
    * The hardware identity matches the issued certificates.
    * Certificates have not been revoked, as verified through OCSP.

    **Firmware**

    * Driver firmware measurements (64 SHA-384 cryptographic hashes).
    * VBIOS firmware measurements (64 SHA-384 cryptographic hashes).
    * Measurements match NVIDIA’s reference “golden” RIM values.
    * All firmware and measurement signatures are cryptographically valid.

    **Configuration**

    * Confidential Computing mode is enabled.
    * Protected PCIe (PPCIE) is correctly configured.
    * The GPU ready state is operational.
  </Accordion>

  <Accordion title="Can verification results be falsified?" icon="comment-question">
    **No.** Verification is based on strong cryptographic guarantees, including:

    * A **hardware root of trust**, with cryptographic keys embedded in tamper-resistant silicon.
    * **Certificate chains** signed by NVIDIA’s Root Certificate Authority, protected by NVIDIA’s private keys.
    * **Cryptographic signatures** that cannot be forged without NVIDIA’s private keys.
    * **Fresh nonces** that prevent replay of previously captured attestation results.

    Even if the operating system is fully compromised, an attacker cannot:

    * Forge NVIDIA’s digital signatures.
    * Create certificates that successfully validate against the NVIDIA Root CA.
    * Modify firmware measurements without detection.
    * Bypass the hardware root of trust.
  </Accordion>

  <Accordion title="What does verification not prove?" icon="comment-question">
    GPU attestation verifies GPU authenticity and configuration, but it DOES NOT validate:

    * Hypervisor security or configuration.
    * Host operating system security.
    * Network isolation between virtual machines.
    * Physical datacenter security.
    * Guest operating system security within the VM.

    **For comprehensive protection:**\
    GPU attestation should be used as part of a defense-in-depth security strategy.
  </Accordion>

  <Accordion title="How do I verify the verification tool itself?" icon="comment-question">
    The verification tooling can be independently validated through the following means:

    1. **Official NVIDIA package distribution:** Published on PyPI

       ```bash theme={null}
       pip show nv-attestation-sdk
       # Displays: nv-attestation-sdk 2.6.3
       ```
    2. **Open-source implementation:** Publicly available for review

       Repository: [https://github.com/NVIDIA/nvtrust](https://github.com/NVIDIA/nvtrust)
    3. **Package signing:** Signed and distributed by NVIDIA

       ```bash theme={null}
       pip show --verbose nv-attestation-sdk
       ```
    4. **Checksum verification:** Validate package integrity

       ```bash theme={null}
       pip hash nv-attestation-sdk
       ```
  </Accordion>

  <Accordion title="Why does the CC State show as OFF when I check my onboarded node?" icon="comment-question">
    This is expected for nodes with **NVLink-connected GPUs**. CC State is only used when individual GPUs (or non-NVLink GPUs) are passed into a VM. Because NVLink-connected GPUs must be passed through **as a complete set**, CC State remains `OFF`.

    For these nodes, confidentiality is provided through **Protected PCIe**, not `CC State`. You can confirm this by checking:

    * `Multi-GPU Mode: Protected PCIe` → GPUs are running in confidential mode.
    * `CPU CC Capabilities: INTEL TDX` → CPU is running in confidential mode.
  </Accordion>
</AccordionGroup>


# Confidential Compute
Source: https://io.net/docs/guides/clouds/confidential-compute-overview

Run secure AI workloads with Intel TDX encryption on io.cloud. Protect data in use on H100, H200, and B200 GPUs at up to 90% lower cost.

## Overview

**Confidential Compute VMs** on [io.net](http://io.net) provides hardware-based encryption that protects your AI data, model weights, and computations from unauthorized access, including cloud operators, administrators, or malicious actors.

Unlike traditional cloud environments that only encrypt data at rest and in transit, **Confidential Compute** maintains end-to-end encryption even in memory while your workloads are running.

This capability is powered by **Intel Trust Domain Extensions (TDX)** on **5th** and **6th** **generation** **Intel Xeon processors**, combined with [io.net](http://io.net)’s decentralized GPU network.

## **What Is Confidential Computing?**

**Confidential Computing** is a hardware-based security model that ensures your data stays encrypted even while being processed.

Using **Trusted Execution Environments (TEEs)**, it creates isolated regions of memory where code and data remain protected from all external access, including the host OS, hypervisor, and cloud administrators.

### **Key Technology**

* **Intel Trust Domain Extensions (TDX):** Provides per-VM encryption and isolation for workloads.
* **Trusted Execution Environments:** Secure enclaves ensure no unauthorized party can read memory contents.
* **Hardware Attestation:** Verifies the integrity of BIOS, firmware, and kernel before execution.

[io.net](http://io.net) delivers the same enterprise-grade protection as *Azure* and *Google Cloud* Confidential VMs, at a fraction of the cost, with bare-metal GPU performance and no centralized dependency.

## Why It Matters

When training or running AI models on traditional hyperscalers, your data sits unencrypted in memory where it can be exposed through:

* Insider threats or compromised infrastructure operators
* Cyberattacks targeting shared cloud environments
* Government subpoenas or data access requests

These risks endanger:

* Proprietary model architectures
* Customer PII, health records, and financial data
* Sensitive inference requests revealing business logic

## **Key Benefits**

* **Protect Intellectual Property:** Encrypt training data, model weights, and architectures during AI model development.
* **Enable Secure Collaboration:** Support multi-party or federated learning while keeping datasets isolated and private.
* **Ensure Regulatory Compliance:** Meet HIPAA, GDPR, and financial data requirements with full auditability.
* **Secure Inference at Scale:** Protect live prompts, responses, and intermediate model states.
* **Reduce Costs:** Run on a decentralized GPU infrastructure, **up to 90% cheaper** than hyperscalers.

## **Getting Started**

Confidential Compute is available upon request through [io.net](http://io.net)’s managed services, supporting machines from H100 up to B200.

To begin using **Confidential Compute** on [io.net](http://io.net):

1. **Request Access:** Submit a provisioning request by emailing `business@io.net` . Mention your preferred GPU type (H100, H200, or B200) and provide basic project details.

   <Note>
     Our specialists will reach out to understand your needs and assist with configuring the machines to your specifications.
   </Note>
2. **Deploy a Confidential VM:** Once set up, deploy your Confidential VM using the web console or API.
3. **Verify Attestation:** Before running sensitive workloads, verify your instance’s attestation report to confirm the integrity of its BIOS, firmware, and TDX configuration. This ensures your VM is operating in a trusted, secure state.
4. **Integrate Seamlessly:** Run workloads on **Ubuntu 24.04 (LTS)** with **built-in Intel TDX support**. Existing MLOps pipelines run without modification. You can migrate existing workflows directly to [io.net](http://io.net) without changing your training or deployment code.
5. **Run Secure Workloads:** Connect to your instance and deploy your AI training or inference workloads as usual. All computations, model weights, and data remain encrypted in memory throughout processing, maintaining full performance and GPU acceleration.

<Note>
  Performance impact is minimal and with full GPU capabilities preserved. This validates secure AI pipelines on cost-effective infrastructure.
</Note>

## **Compliance and Use Cases**

**Confidential Compute** supports secure operations across regulated and high-risk industries:

* **Healthcare:** Train on PHI and diagnostic data securely.
* **Finance:** Protect trading models and risk analytics pipelines.
* **Legal:** Safeguard sensitive inference workloads and document data.
* **Defense and Government:** Maintain sovereignty over AI models and datasets.

Additionally, all workloads comply with:

* **HIPAA** (Health Insurance Portability and Accountability Act)
* **GDPR** (General Data Protection Regulation)
* **PCI DSS** (Payment Card Industry Data Security Standard)


# Data Science Specification
Source: https://io.net/docs/guides/clouds/data-science-image-full-specification



This document provides the full specification of the Data Science Image used in IO.NET cloud deployments. It includes the operating system, core dependencies, and package lists for both the Conda `rapids-25.6.0` environment and the base Python environment.

## Base Information

* **OS**: Ubuntu 24.04.1 LTS (Noble Numbat)
* **CUDA**: 12.1
* **RAPIDS**: 25.6.0
* **Python**: 3.12
* **Conda**: 25.7.0

## Package Lists

The image comes with a preconfigured Conda environment (`rapids-25.6.0`) as well as a base Python environment.\
To see the full package versions installed, run the following commands inside the image:

### Conda environment (`rapids-25.6.0`)

```bash theme={null}
conda run -n rapids-25.6.0 pip3 list
```

### Base Python environment

```
pip3 list
```

> 📘 \*\*Note: \*\*The package lists may change over time as the image is updated.
>
> Users should always re-run the commands above to get the most up-to-date package versions.


# Bare Metal (Self Serve) Moving Forward
Source: https://io.net/docs/guides/clouds/deploy-bare-metal-cluster

Bare Metal clusters give you direct access to hardware for maximum performance, low latency, high efficiency, and full control over configuration.

<Danger>
  ### Service Update: Bare Metal (Self Serve) Moving Forward

  Bare Metal on Demand will no longer be available starting Wednesday,  October 1, 2025.

  If you need Bare Metal, please contact our sales team at [business@io.net](mailto:business@io.net) for managed services.
</Danger>

The Bare Metal Automated Solution provides fast, self-service access to dedicated hardware resources, all of which eliminate delays from custom contracts and manual setup. This solution is ideal for high-performance workloads such as AI model training, making predictions (inferencing), and other compute-heavy tasks. Through an automated deployment flow, you can select and provision devices in minutes, while our real-time dashboard offers visibility into usage, performance metrics, and costs to optimize your deployments.

<iframe title="Deploying a Bare Metal Cluster on IO Cloud" />

<Info>
  Bare Metal On Demand clusters do not provide `sudo` or `root` access. Certain system-level operations requiring elevated privileges will not be possible. Please ensure your workloads and deployment requirements can operate within this restriction.
</Info>

### To deploy a Bare Metal On Demand Cluster:

1. From IO Cloud, next to **Bare Metal**, click **Request**.

   <Frame>
     <img alt="" />
   </Frame>
2. Select a location.

   <Frame>
     <img alt="" />
   </Frame>
3. Select your Connectivity Tier.

   <Frame>
     <img alt="" />
   </Frame>
4. Select your processor.

   <Frame>
     <img alt="" />
   </Frame>
5. Before submitting your request, you can view a summary of all details of your bare metal solution, including the duration and pricing.

<Frame>
  <img alt="" />
</Frame>

### Bare Metal Dashboard

Our real-time dashboard provides the following insights to help you track and optimize your deployments:

|                     |                                                                                                                  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Device Inventory    | View active, idle, and available devices in your cluster.                                                        |
| Performance Metrics | Track CPU, memory, and GPU utilization for each device, enabling real-time monitoring and adjustments.           |
| Usage Tracking      | View historical and current device usage data to understand and optimize resource allocation.                    |
| Pricing Information | Real-time cost breakdowns help you manage budget and understand the impact of each device on your overall spend. |
| Revenue Insights    | For multi-tenancy or resale scenarios, monitor revenue generated by specific devices and clusters.               |

<Info>
  At the end of your rental period, we securely wipe and restore each Bare Metal device to its original state. We adhere to strict data security protocols to prevent unauthorized access and maintain compliance with industry standards throughout the device lifecycle.
</Info>


# Deploy CaaS
Source: https://io.net/docs/guides/clouds/deploy-containers

Flexible & High-Performance Containers built for rapid deployment and scalable AI workloads

[io.net](http://io.net) offers a simple and powerful interface for deploying containers using high-performance infrastructure. Whether you are running inference, training models, or hosting APIs, the Containers system gives you flexibility and speed.

This guide will help you deploy using IO Cloud API keys on our CaaS clusters. For detailed API usage, refer to our [API Reference](/reference/get-started-with-caas-api).

<Note>
  Support for *AWS ECR* private images is not available at this time for **CaaS**.
</Note>

<iframe title="Start Using IO Cloud: Your First Steps Explained" />

## Deploy Container

Click the **Deploy Container** button to launch a wizard that guides you through the deployment process.

<Frame>
  <img alt={true} />
</Frame>

## Container Deployment Wizard

### Step 1: Basic Deployment Settings

Configure your container:

* **Container Image** *(required)* Example: `myorg/myimage:latest`
* **Image Type**
  * Public Image
  * Private Image
* **Start Command** Enter the start command in JSON array format, example:

  <CodeGroup>
    ```json json theme={null}
    ["python3","-m","vllm.entrypoints.openai.api_server","--model"]
    ```
  </CodeGroup>
* **Traffic Port** *(required)* Default: `8000`
* **Environment Variables** Click **Add Variable** to define key-value pairs. Options:
  * Normal Variable
  * Private Variable You can add or remove variables as needed.

Once all required fields are completed, click **Next Step**.

<Frame>
  <img alt="" />
</Frame>

<Accordion title="Using Environment Variables in Entrypoints" icon="warning">
  To avoid deployment failures:

  * Always define environment variables in the `env_variables` section.
  * Do not substitute variables directly in the `entrypoint` or `args`.
  * When referencing variables in the entrypoint, **escape**`$`**as**   `$$`.

  Example:

  ```json theme={null}
  "entrypoint": [
    "sh", "-c", "echo 'Variable value: $${TEST_VAR}' && sleep 3600"
  ],
  "env_variables": {
    "TEST_VAR": "This is a test"
  }
  ```

  * **Correct:** `$${TEST_VAR}` prints the variable value inside the container.
  * **Incorrect:** `$TEST_VAR` may cause deployment failure.
  * Always use `env_variables` for variable management.

  <Note>
    For advanced users: There is a known issue where Terraform variable interpolation (`$`) may conflict with service-layer substitution. Escaping with `$$` resolves this issue.
  </Note>
</Accordion>

### Step 2: Select Your Cluster Processor + Location

Choose the hardware and region for your deployment:

* **Available GPUs** Search by GPU model and view:
  * GPU Model
  * GPUs per Container
* **Location Selection** After selecting a GPU, you'll see a list of locations showing:
  * Region (e.g. Canada, Germany)
  * Available containers per location

Once both **GPU** and **location** are selected, proceed to the **next step**.

<Frame>
  <img alt="" />
</Frame>

### Step 3: Summary

On the Summary page, the choices you made in the process are displayed. You must select the number of Containers and the duration of time that you will use them.

1. In the **No. of Containers** field, select the number of Containers in the dropdown. 2 Containers will increase the cost.
2. In the **Enter Duration** field, select the length of time: Hourly, Daily, or Weekly. To the right, you can increase the quantity.
3. Review all the details of your cluster, including the **Total Cost**.
4. Click **Deploy Cluster**.

<Frame>
  <img alt="" />
</Frame>

### View Cluster

After payment is processed you can view your cluster loading.

<Frame>
  <img alt="" />
</Frame>

Click **Return to Clusters** after your cluster is successfully deployed. The screenshot below is a detail page of your cluster.

<Frame>
  <img alt="" />
</Frame>

> 🚧 Troubleshooting Container Issues
>
> If your container is not running, you do not need to delete the whole cluster. Instead, open the deployment settings, adjust any incorrect details (for example, the image name or registry credentials), and redeploy.
>
> This way, you avoid the minimum 1-hour charge for deleting and recreating a cluster.
>
> <img alt="Containers9 Jp" />


# Deploy Ray Cluster
Source: https://io.net/docs/guides/clouds/deploy-ray-cluster

This document explains how to deploy a Ray cluster by leveraging compute power in io.net's DePIN network.

## Payments

IO Cloud customers can load their io.net account prior to deploying clusters, or they can pay at the end of the deploy process. The main two ways to pay for clusters is using Solana and credit cards. To use Solana, you must set up a wallet. This can be done when you register your account or later in **Account Settings**.

To learn more about the types of payments we offer and step-by-step guides, see [IO Cloud Payments](/guides/payment/io-cloud-payments).

<iframe title="Deploy Ray Cluster on IO Cloud" />

## Configure Cluster

### 1. Create Cluster

Select Ray from the Cluster menu.

<Frame>
  <img alt="" />
</Frame>

### 2. Select Cluster Type

Select the cluster type that meets the scope of your project.

* **General** - This option works well for prototyping or general E2E workloads.
* **Inference** - Choose if you require production-ready clusters for low-latency inference and heavy workloads.
* **Train** - Choose if you require production-ready clusters for machine learning models, training, and fine-tuning.

<Frame>
  <img alt="" />
</Frame>

### 3. Rename Cluster

Click the pencil icon to the right of the name to rename your cluster. In the screenshot below, the icon is highlighted in the blue box. Provide a unique name for your cluster.

<Frame>
  <img alt="" />
</Frame>

Click **Next Step**.

### 4. Security Compliance

Select the level and type of security for your cluster.

* **E2E Encrypted** - A method of secure communication that prevents bad actors from accessing data while it's transferred. It restricts data access to the sender and recipient. All data traffic between GPUs is encrypted.
* **SOC2/HIPAA** - (Coming Soon) A framework for managing and securing data related to technology and cloud computing services. All data traffic between GPUs is encrypted.

<Frame>
  <img alt="" />
</Frame>

Click **Next Step**.

### 5. Location

To select a location for our GPUs, enter a country name in the Search field or browse the country list (screenshot below is truncated). You can select multiple locations. Residents of countries with strict data residency can use this option to meet those requirements.

<Info>
  One reason to select a specific location is to reduce latency. If you're located in USA and select USA for location, then your clients can get results more quickly if, for example, your GPUs are inferencing.
</Info>

<Frame>
  <img alt="" />
</Frame>

Click **Next Step**.

### 6. Connectivity Tiers

Select the connectivity speed for your project.

* **Ultra High Speed** - Download 1600 MB/s / 1200 MB/s Upload
* **High Speed** - Download 800 MB/s / 600 MB/s Upload
* **Medium** - Download 400 MB/s / 300 MB/s Upload
* **Low Speed** - Download 100 MB/s / 10 MB/s Upload

<Frame>
  <img alt="" />
</Frame>

Click **Next Step**.

### 7. Select GPUs

Select the type of computing your project requires, **GPU** or **CPU**.

* If you select GPU, also select NVIDIA and browse for the model that satisfies your requirements.
* If you select CPU, you can choose between Apple of AMD CPUs.

<Frame>
  <img alt="" />
</Frame>

Click **Next Step**.

### 8. Cluster Base Image

Ray is the only selection for now. We will release additional cluster base images soon such as:

* IOG
* Ludwig
* Pytorch FSDP
* Unreal Engine 5
* Unity Streaming

<Frame>
  <img alt="" />
</Frame>

Click **Next Step**.

### 9. Master Configuration

All clusters include a preconfigured master node. These nodes are selected by io.net from reliable and security compliant data centers.

<Frame>
  <img alt="" />
</Frame>

Click **Next Step**.

### 10. Summary

On the Summary page, the choices you made in the process are displayed. You must select the number of GPUs and the duration of time that you will use them.

1. In the **Enter GPUs Quantity** field, select the number of GPUs in the dropdown. 2 GPUs will increase the cost.
2. In the **Enter Duration** field, select the length of time: Hourly, Daily, or Weekly. To the right, you can increase the quantity.
3. Review all the details of your cluster, including the **Total Cost**.
4. Click **Deploy Cluster**.

<Frame>
  <img alt="" />
</Frame>

### View Cluster

After payment is processed you can view your cluster loading.

<Frame>
  <img alt="" />
</Frame>

Click **Return to Clusters** after your cluster is successfully deployed. The screenshot below is a detail page of your cluster.

<Frame>
  <img alt="" />
</Frame>


# Deploy VM on Demand
Source: https://io.net/docs/guides/clouds/deploy-vm-on-demand

Instantly deploy GPU accelerated virtual machines designed for AI and ML workloads. Configure, launch, and manage your compute VMs. CPUs are included with every instance.

**VM on Demand** provides a seamless way to deploy fully equipped virtual machines optimized for AI and machine learning workflows. Designed for data scientists, researchers, and builders, it enables you to launch high-performance GPU or CPU-powered environments with a few simple clicks.

You can scale resources as your workloads grow, monitor performance, and manage deployments, all through an intuitive interface. Whether you are training deep learning models, running data pipelines, or testing ML prototypes, **VM on Demand** delivers a fast, reliable, and frictionless compute experience.

## Quick Start:

1. Click **Deploy Virtual Machine** on the **Home** tab.
2. Choose your **Processor**.
3. Configure your **Virtual Machine**.
4. Monitor your deployment details in the sidebar.
5. Once the minimum requirements are met, review and deploy your cluster.
6. Start using your **Virtual Machine**.
7. View and manage your virtual machines in the **Virtual Machine** tab.

## Deploying Clusters

### 1. Getting Started

To begin, click the **Deploy** button in the **Virtual Machine** row on the **Home** tab of the io.net Cloud platform.

<Frame>
  <img alt="IO Cloud VM Deploy Home Tab Pn" />
</Frame>

You can also open the **Virtual Machine** tab directly and select **Deploy Virtual Machine** to start a new deployment.

<Frame>
  <img alt="IO Cloud VM Deploy VM Pn" />
</Frame>

### 2. Select your Virtual Machine Processor

Choose a processor based on your requirements. Each card displays its specifications, including:

* *Device Availability*
* *Price*
* *VRAM per card*
* *Storage*
* *Supplier*
* *Location*

<Frame>
  <img alt="IO Cloud VM Choose Cluster Pn" />
</Frame>

To view detailed technical information, click **More details**. This will display additional specifications such as interconnect technology, NVLink support, memory, and the number of virtual CPUs (vCPUs).

You can refine your selection using the **Search GPU Model** field or by applying filters. Click **Filter** to filter by:

* *GPU Family*
* *Region*
* *Supplier*
* *GPU Memory*
* *CPU Cores*
* *Device Memory*
* *Storage*

You can apply these filters individually or in combination.

<Frame>
  <img alt="IO Cloud VM Filters Pn" />
</Frame>

After selecting your Virtual Machine Processor, click **Next Step** to continue.

### 3. Configure Environment and SSH Keys

Set up your environment and link SSH Keys for secure access. You can choose between two image types:

<Note>
  Partner-provided clusters include a preloaded image that cannot be changed.

  To choose a specific image, select a processor supplied by **io.net**.
</Note>

<Tabs>
  <Tab title="General Purpose Image">
    The **General Purpose Image** provides a clean, flexible foundation for building any type of compute environment.

    ***Specifications:***

    * **OS:** Ubuntu 24.04 (64-bit)
    * **Size:** 3.5 GB (uncompressed)
    * **Includes:** CUDA Toolkit and drivers
    * **Ideal for:** Users who prefer to fully customize their development environment and software stack.

    <Frame>
      <img alt="IO Cloud VM General Purpose Image Pn" />
    </Frame>
  </Tab>

  <Tab title="Data Science Image">
    The **Data Science Image** provides a ready-to-use environment for machine learning, artificial intelligence, and data analytics workloads. It comes fully configured with GPU acceleration and essential data science tools, allowing you to begin experimentation and model development immediately without additional setup.

    ***Specifications:***

    * **OS:** Ubuntu 24.04.2 LTS
    * **Includes:**
      * Python 3.12
      * Conda 25.7.0
      * CUDA 12.1
      * RAPIDS 25.6.0
    * **Ideal for:**
      * Building and training deep learning or machine learning models using GPU acceleration.
      * Analyzing and processing large datasets with GPU-accelerated data frames.
      * Running distributed computing tasks with frameworks such as **Ray**.
      * Developing, visualizing, and testing AI workflows directly from **Jupyter Notebooks**.

    [View full image specification →](/guides/clouds/data-science-image-full-specification)

    <Frame>
      <img alt="IO Cloud VM Data Science Image Pn" />
    </Frame>
  </Tab>
</Tabs>

#### 4. Add your SSH Key

Choose one of the following methods to access your VM securely:

<Note>
  Partner-supplied clusters only support **Manual SSH key input**. You must add your SSH key by entering a key name and pasting your public key directly.

  To use the **Fetch from GitHub** feature, select an **io.net-supplied processor**. This allows you to retrieve your public SSH key automatically by entering your *GitHub ID*, simplifying setup and secure access.
</Note>

<Frame>
  <img alt="IO Cloud VM SSH Options Pn" />
</Frame>

<Tabs>
  <Tab title="Manual Input">
    Use this option to add your SSH key directly.

    1. Enter a **Key Name** to identify the key.
    2. Paste your **public SSH key** into the field provided.

    You can repeat these steps to add multiple SSH keys if several users or systems require access. Each key you add will be authorized for SSH connections to your deployed VM.

    This method is especially useful if you manage SSH keys locally or use multiple machines. It also ensures that you can explicitly control which public keys are linked to your cluster.

    <Tip>
      Make sure that you paste only the public portion of your SSH key. Private keys should never be uploaded or shared.
    </Tip>

    <img alt="Containers7 Jp" title="Containers7 Jp" />
  </Tab>

  <Tab title="Fetch from GitHub">
    If your public SSH keys are already associated with your GitHub account, you can retrieve them automatically using the Fetch from GitHub feature.

    1. Select the **Fetch SSH key from GitHub** option in the Type of *SSH key* field.
    2. Enter your **GitHub ID**, or multiple **GitHub IDs** separated with commas, in the field provided.
    3. The system will automatically retrieve and apply your public SSH keys from your GitHub profile.

    This option is a fast and convenient way to authenticate without copying or pasting keys manually. It is especially useful if you frequently rotate keys or work across multiple environments, since your GitHub account always stores the latest authorized keys.

    <Tip>
      You can view or manage your SSH keys in your GitHub account by navigating to **Settings > SSH and GPG keys**.
    </Tip>
  </Tab>
</Tabs>

### 5. Customize your Virtual Machine (Optional)

In this step, you can personalize your deployment by assigning a **name** and configuring **network services**.

<Frame>
  <img alt="IO Cloud VM Customize Pn" />
</Frame>

**Cluster Name**

You can assign a unique name to your cluster to help identify and manage it easily.

Enter your preferred name in the **Your Cluster Name** field. This name will appear throughout your dashboard and logs, making it simpler to distinguish between different clusters or projects.

**Network Services**

Network services allow you to expose specific ports on your virtual machine that are necessary for your applications or workflows. These ports enable external access to services running inside your virtual machine, such as APIs, web applications, or databases.

By defining network services during setup, you ensure that your required tools and applications are reachable while keeping all other ports securely closed by default. This approach provides flexibility for your workloads without compromising security.

You can configure multiple network services depending on your use case.

<Note>
  Partner-supplied clusters expose all ports. However, the following ports are occupied by default:

  * ***Port 22 - SSH Access***
  * ***Port 53 - System DNS***
  * ***Port 5555 - NVIDIA Host Engine***
  * ***Port 9100 - Node Exporter: Metrics***
  * ***Port 9400 - DCGM Exporter: GPU Metrics***
  * ***Port 12345  and 12346 - Grafana Agent***
</Note>

To expose additional ports or services, follow these steps:

1. Click **Add Network Service**
2. Provide the required details:
   * *Service Name*
   * *Port Number*
   * *Protocol* (TCP or UDP)
   * *Whitelisted IPs* (IPv4 subnet)
3. Click the **+** button to add each IP to your whitelist.

<Warning>
  Network services and port configurations cannot be changed after virtual machine deployment. Ensure that all required ports are defined before deployment, and expose them in your Docker command inside the VM.
</Warning>

<Accordion title="Port Exposure on io.net">
  When deploying containers, you must expose ports in two locations:

  1. **Inside the VM (Docker):**

  Specify ports when running your container.

  ```bash theme={null}
  docker run -d -p 8082:8082 your-image-name
  ```

  2. **io.net Network or Frontend Configuration:**

  After deployment, the platform assigns external ports that map to your container ports.\
  These external ports are used to access your services.

  <Note>
    Docker port exposure inside the VM does not automatically propagate to the external network. Both configurations are required for external accessibility.
  </Note>
</Accordion>

### 6. Review and Deploy

A sidebar on the right displays all your deployment details, including:

* *Machine Type*
* *Processor*
* *Cost*
* *GPUs per VM*
* *Location*
* *Duration type (Hourly, Daily, Weekly, Monthly)*
* *Duration*

After confirming that all details are correct and the minimum requirements are met, click **Pay & Deploy**.

<Frame>
  <img alt="IO Cloud VM Deployment and Summary" />
</Frame>

A payment window will appear where you can complete the transaction using **IO Credits**, **Credit or Debit Cards**, **USDC**, or **IO Coin**.

<Frame>
  <img alt="IO Cloud VM Payment Pn" />
</Frame>

Once payment is confirmed, your cluster deployment will begin automatically.

## Viewing Virtual Machines

After deployment, you can view your virtual machines.

Navigate to the **Virtual Machines** tab to monitor performance or launch additional VMs.

The **Virtual Machines Dashboard** allows you to filter clusters by their current status. Click on a specific VM to open its details page.

Each **Detail** page shows you:

* Real-time resource usage information
* SSH connection details
* Billing and usage insights

### Connecting to your Virtual Machine

1. Locate the *SSH Access* field on your cluster page and copy the provided command.

<img alt="Containers9 Jp" />

2. Open your **Terminal** and paste the command, then press **Enter**.
3. When prompted to confirm the connection, type **yes** and press **Enter**.
4. Once connected, you will see the welcome message and gain access to your VM through the SSH terminal.


# IO Cloud Overview
Source: https://io.net/docs/guides/clouds/io-cloud

Harness the power of io.net’s decentralized network through IO Cloud, your gateway to high-performance GPUs and CPUs for Web3 initiatives.

<Frame>
  <img alt="CLOUD Pn" />
</Frame>

## Your Web3 Gateway to Efficiency

### Ease of Use

At IO Cloud, we prioritize an effortless user experience. Our dashboards provide real-time insights, enabling informed decision-making with minimal delay. Cluster creation is streamlined, granting immediate access to high-performance GPUs, so you can begin working without unnecessary complexity. Developed using ReactJS and Tailwind, the portal offers a clean, modern interface designed to facilitate an efficient and intuitive workflow.

### Real-time Performance

In the dynamic landscape of Web3, time is of the essence. IO Cloud is engineered for real-time interactions, with our specialized Python API layer delivering immediate updates and data synchronization, ensuring you stay fully informed at every step.

### Customizability

IO Cloud is designed to adapt to your specific requirements. With a wide range of customization options, you can configure your environment to optimize efficiency. From tailored dashboards to custom configurations, every aspect is adjustable to streamline your operations and maintain focus on critical tasks.

### Security

Security is an integral part of IO Cloud’s architecture. Rather than being an afterthought, robust security measures are embedded at every level. Multiple layers of protection—including a strong firewall, granular access controls, and a modular design—ensure that your data and workflows remain secure from potential threats.

##### The IO Cloud is designed with the modern user, emphasizing real-time interactions, robust security, complete user control, and ease of use.

**IO Cloud:** The future of Web3, simplified.


# Train a PyTorch Model on Fashion MNIST: Jupyter Notebook
Source: https://io.net/docs/guides/clouds/jupyter-notebook

This document describes how to run a job on your cluster that distributes the training workload across multiple workers using Ray's distributed computing capabilities. This allows for parallelizing the training process and potentially reducing the overall training time. In the instructions below, we run Train a PyTorch Model on Fashion MNIST job using Jupyter Notebook.

For more information about Jupyter Notebook, see their [documentation](https://docs.jupyter.org/en/latest/).

<iframe title="Easy Model Training with Ray Cluster  on IO Cloud" />

## Table of Contents

* [Steps to run a test job in Jupyter Notebook](https://docs.io.net/docs/jupyter-notebook#steps-to-run-a-test-job-in-jupyter-notebook)
* [Congratulations on Successfully Training Your First Model](https://docs.io.net/docs/jupyter-notebook#congratulations-on-successfully-training-your-first-model)
* [Troubleshooting Model Training](https://docs.io.net/docs/jupyter-notebook#troubleshooting-model-training)

## Steps to run a test job in Jupyter Notebook:

1. After your cluster deployment is complete, go to **View Cluster**.

   <Frame>
     <img alt="" />
   </Frame>
2. On the cluster detail page, copy the **IDE Password** and click **Jupyter Notebook**.

   <Frame>
     <img alt="" />
   </Frame>
3. Enter your **IDE Password** you copied in the **Jupyter** password field.

   <Frame>
     <img alt="" />
   </Frame>
4. Click **File** to create a new Python Notebook.

   <Frame>
     <img alt="" />
   </Frame>
5. In the **New** dropdown, select **Notebook**. It launches a new tab.

   <Frame>
     <img alt="" />
   </Frame>
6. A new notebook will open in a new browser tab with a prompt to select a kernel. Choose **Python 3** for this example, then click **Select**.

   <Frame>
     <img alt="" />
   </Frame>
7. Enter the code sample below into a cell and click **Run**.

   <CodeGroup>
     ```python Python theme={null}
     import os
     from typing import Dict

     import torch
     from filelock import FileLock
     from torch import nn
     from torch.utils.data import DataLoader
     from torchvision import datasets, transforms
     from torchvision.transforms import Normalize, ToTensor
     from tqdm import tqdm

     import ray.train
     from ray.train import ScalingConfig
     from ray.train.torch import TorchTrainer

     def get_dataloaders(batch_size):
         transform = transforms.Compose([ToTensor(), Normalize((0.5,), (0.5,))])

         with FileLock(os.path.expanduser("~/data.lock")):
             training_data = datasets.FashionMNIST(
                 root="~/data",
                 train=True,
                 download=True,
                 transform=transform,
             )

             test_data = datasets.FashionMNIST(
                 root="~/data",
                 train=False,
                 download=True,
                 transform=transform,
             )

         train_dataloader = DataLoader(training_data, batch_size=batch_size, shuffle=True)
         test_dataloader = DataLoader(test_data, batch_size=batch_size)

         return train_dataloader, test_dataloader

     class NeuralNetwork(nn.Module):
         def __init__(self):
             super(NeuralNetwork, self).__init__()
             self.flatten = nn.Flatten()
             self.linear_relu_stack = nn.Sequential(
                 nn.Linear(28 * 28, 512),
                 nn.ReLU(),
                 nn.Dropout(0.25),
                 nn.Linear(512, 512),
                 nn.ReLU(),
                 nn.Dropout(0.25),
                 nn.Linear(512, 10),
                 nn.ReLU(),
             )

         def forward(self, x):
             x = self.flatten(x)
             logits = self.linear_relu_stack(x)
             return logits

     def train_func_per_worker(config: Dict):
         lr = config["lr"]
         epochs = config["epochs"]
         batch_size = config["batch_size_per_worker"]

         train_dataloader, test_dataloader = get_dataloaders(batch_size=batch_size)

         train_dataloader = ray.train.torch.prepare_data_loader(train_dataloader)
         test_dataloader = ray.train.torch.prepare_data_loader(test_dataloader)

         model = NeuralNetwork()

         model = ray.train.torch.prepare_model(model)

         loss_fn = nn.CrossEntropyLoss()
         optimizer = torch.optim.SGD(model.parameters(), lr=lr, momentum=0.9)

         # Model training loop
         for epoch in range(epochs):
             if ray.train.get_context().get_world_size() > 1:
                 train_dataloader.sampler.set_epoch(epoch)

             model.train()
             for X, y in tqdm(train_dataloader, desc=f"Train Epoch {epoch}"):
                 pred = model(X)
                 loss = loss_fn(pred, y)

                 optimizer.zero_grad()
                 loss.backward()
                 optimizer.step()

             model.eval()
             test_loss, num_correct, num_total = 0, 0, 0
             with torch.no_grad():
                 for X, y in tqdm(test_dataloader, desc=f"Test Epoch {epoch}"):
                     pred = model(X)
                     loss = loss_fn(pred, y)

                     test_loss += loss.item()
                     num_total += y.shape[0]
                     num_correct += (pred.argmax(1) == y).sum().item()

             test_loss /= len(test_dataloader)
             accuracy = num_correct / num_total

             ray.train.report(metrics={"loss": test_loss, "accuracy": accuracy})

     def train_fashion_mnist(num_workers=2, use_gpu=False):
         global_batch_size = 32

         train_config = {
             "lr": 1e-3,
             "epochs": 10,
             "batch_size_per_worker": global_batch_size // num_workers,
         }

         # Configure computation resources
         scaling_config = ScalingConfig(num_workers=num_workers, use_gpu=use_gpu)

         # Initialize a Ray TorchTrainer
         trainer = TorchTrainer(
             train_loop_per_worker=train_func_per_worker,
             train_loop_config=train_config,
             scaling_config=scaling_config,
         )

         result = trainer.fit()
         print(f"Training result: {result}")
     ```
   </CodeGroup>

   <Frame>
     <img alt="" />
   </Frame>
8. Enter the **Python command** below in a new cell to run the training model script. Then click **Run**.

   <CodeGroup>
     ```python python theme={null}
     train_fashion_mnist(num_workers=2, use_gpu=True)
     ```
   </CodeGroup>

   <Info>
     Note, by default, 2 CPUs and a GPU are set for this command. Make sure that your hardware has enough CPU and GPU available, increase or reduce the allocation if needed.
   </Info>

   <Frame>
     <img alt="" />
   </Frame>
9. If you scroll to the bottom of the output, you will see the training result.

   <CodeGroup>
     ```python python theme={null}
     Training result: Result(
       metrics={'loss': 0.3572742183404133, 'accuracy': 0.8728},
       path='/home/ray/ray_results/TorchTrainer_2024-05-17_18-55-55/TorchTrainer_c3725_00000_0_2024-05-17_18-55-55',
       filesystem='local',
       checkpoint=None
     )
     ```
   </CodeGroup>

## Congratulations on Successfully Training Your First Model

You can now track your model's progress using the **Ray Dashboard.** The dashboard provides detailed insights into your cluster, including **cluster utilization, status, autoscaler activity, resource states**, and more.

1. Return to your cluster. On the cluster detail page, copy the **IDE Password** and click **Ray Dashboard**.

   <Frame>
     <img alt="" />
   </Frame>
2. In the password field, enter your password. Click **View All Jobs**. Here, you can see that your job is running.

   <Frame>
     <img alt="" />
   </Frame>
3. You can also check this in io.net by going to **Clusters** > **select your cluster** > click an **IO Worker** > **Jobs**.

<Frame>
  <img alt="" />
</Frame>

## Troubleshooting Model Training

1. If you see an error after running the example code that matches the one below:

   <CodeGroup>
     ```python python theme={null}
     2025-05-15 01:39:02,503	INFO util.py:154 -- Outdated packages:
       ipywidgets==7.7.2 found, needs ipywidgets>=8
     Run `pip install -U ipywidgets`, then restart the notebook server for rich notebook output.
     2025-05-15 01:39:03,181	INFO util.py:154 -- Outdated packages:
       ipywidgets==7.7.2 found, needs ipywidgets>=8
     Run `pip install -U ipywidgets`, then restart the notebook server for rich notebook output.
     2025-05-15 01:39:03,219	INFO util.py:154 -- Outdated packages:
       ipywidgets==7.7.2 found, needs ipywidgets>=8
     Run `pip install -U ipywidgets`, then restart the notebook server for rich notebook output.
     ```
   </CodeGroup>
2. Copy the update command for outdated packages, paste it into a new cell, and click the Run button to install the updates:

   <CodeGroup>
     ```python python theme={null}
     pip install -U ipywidgets
     ```
   </CodeGroup>
3. In the toolbar, click **Kernel** and select **Restart the kernel** from the dropdown. This updates the packages.

   <Frame>
     <img alt="" />
   </Frame>
4. Then paste the command again and run it to execute the script.


# Exposing Applications to the Internet
Source: https://io.net/docs/guides/clouds/kubernetes/exposing-to-the-internet

Learn how to expose applications to the internet on io.net Kubernetes clusters using ingress controllers, with guidance on DNS automation and SSL certificate management.

This guide provides a comprehensive overview of how to expose applications to the internet on **io.net** *Kubernetes Clusters* using an ingress controller. It details two supported deployment approaches, outlines their respective advantages and trade-offs, and explains how DNS can be automated with *ExternalDNS*. The guide also covers SSL certificate management using cert-manager to support secure application delivery.

## Prerequisites

* `kubectl` access to your io.net Kubernetes Cluster.
* `Helm 3.x` installed.
* Domain ownership and DNS management access.
* Basic understanding of Kubernetes concepts (Pods, Services, Ingress).
* For *ExternalDNS*: API credentials for your DNS provider.

## Selecting your Method

This table outlines the key factors to consider when choosing between **Deployment + Service IPs** and **DaemonSet**.

| Key Factor            | Deployment + Service IPs        | DaemonSet                      |
| --------------------- | ------------------------------- | ------------------------------ |
| **Setup Complexity**  | Medium                          | Simple                         |
| **Scalability**       | High, supports flexible scaling | Limited, one pod per node      |
| **High Availability** | Requires manual IP management   | Built-in with multiple nodes   |
| **Resource Usage**    | Configurable                    | Fixed per node                 |
| **Best For**          | Large-scale applications        | Simple deployments, edge cases |

<Tabs>
  <Tab title="Option 1">
    ## Option 1: Ingress Controller as a Deployment with Service IPs

    The ingress controller is deployed as a scalable Kubernetes deployment and exposed via a LoadBalancer Service with manually assigned external IP addresses.

    Incoming traffic is automatically load-balanced across ingress pods. This approach is fully compatible with ExternalDNS.

    ### Flow overview:

    ```
    [ Client ]
       |
       v
    Connects to node public IPs (set as externalIPs on LoadBalancer service)
       |
       v
    Traffic → balanced across ingress controller pods
       |
       v
    Ingress controller routes to applications
    ```

    ### How it works:

    * ***Service Type***: `LoadBalancer` (required for ExternalDNS compatibility).
    * ***External IPs***: Manually assigned and mapped to the nodes where ingress pods are scheduled.
    * ***DNS Management***: ExternalDNS monitors the LoadBalancer Service and automatically creates DNS records that point to the configured external IPs.

    | Pros                                                 | Cons                                            |
    | :--------------------------------------------------- | :---------------------------------------------- |
    | Automatic load balancing across ingress controllers. | Node failures impact the assigned public IPs.   |
    | No host port conflicts.                              | Public IPs must be managed manually.            |
    | Ingress controllers can scale flexibly.              | No automatic failover without additional tools. |
    | Cleaner setup for most applications.                 |                                                 |

    ### Step-by-Step Setup:

    <Steps>
      <Step title="Install NGINX Ingress Controller as a Deployment">
        <Warning>
          The *Pod Security Admission* plugin is enabled by default in all [io.net](http://io.net) Kubernetes clusters to enforce *Pod Security Standards* and enhance baseline cluster security.

          You may override *Pod Security Admission* settings at the namespace level when necessary. This can be useful for workloads such as ingress controllers or monitoring solutions that require less restrictive security policies.

          However, the recommended approach is to adapt your applications to run securely by configuring an appropriate `podSecurityContext`.
        </Warning>

        ```bash theme={null}
        kubectl create namespace ingress-nginx
        kubectl label namespace ingress-nginx pod-security.kubernetes.io/enforce=privileged

        helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
        helm repo update
        helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx \
          --namespace ingress-nginx \
          --set controller.kind=Deployment \
          --set controller.replicaCount=3 \
          --set controller.resources.requests.cpu=100m \
          --set controller.resources.requests.memory=128Mi \
          --set controller.service.enabled=true \
          --set controller.service.type=LoadBalancer \
          --set controller.publishService.enabled=false \
          --set-string controller.nodeSelector.worker-node=true
        ```

        <Note>
          The ingress controller is configured to deploy only on worker nodes with the `worker-node=true` label.
        </Note>

        <Info>
          **Optional:** add *Tolerations* if your worker nodes have taints:

          `--set 'controller.tolerations[0].operator=Exists'`
        </Info>

        <Info>
          **Optional:** add *Pod Anti-Affinity* to ensure pod replicas are scheduled on different nodes (only if you have sufficient worker nodes):

          `--set 'controller.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[0].labelSelector.matchLabels.app\.kubernetes\.io/name=ingress-nginx'`

          `--set 'controller.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[0].topologyKey=kubernetes.io/hostname'`
        </Info>
      </Step>

      <Step title="Assign Public IPs to Ingress Nodes">
        Edit the Service configuration so that Public IPs are assigned only from nodes where ingress pods are running.

        ```bash theme={null}
        kubectl patch svc ingress-nginx-controller -n ingress-nginx --type=merge -p "{
          \"spec\": {
            \"externalIPs\": [
              $(kubectl get pods -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx -o jsonpath='{.items[*].spec.nodeName}' \
                | tr ' ' '\n' | sort -u | while read node; do \
                  kubectl get node "$node" -o jsonpath='{.status.addresses[?(@.type=="ExternalIP")].address}'; \
                  echo; \
                done | tr '\n' ',' | sed 's/,$//' | sed 's/\([^,]*\)/"\1"/g')
            ]
          }
        }"
        ```

        <Note>
          This command identifies the nodes currently running ingress controller pods and assigns their external IP addresses to the LoadBalancer Service. This allows ExternalDNS to correctly detect the service endpoints and manage the corresponding DNS records.
        </Note>
      </Step>

      <Step title="Update DNS Records">
        Point your domain to the Service’s `EXTERNAL-IP` values shown by `kubectl get svc -n ingress-nginx`, or follow the [*ExternalDNS Guide*](/guides/clouds/kubernetes/externaldns-guide).
      </Step>

      <Step title="Deploy Applications with Ingress">
        Deploy your applications and configure ingress resources to handle routing to the appropriate services.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Option 2">
    ## Option 2: Ingress Controller as a DaemonSet

    Run the ingress controller on every cluster node, where it listens directly on ports 80 and 443 of each node’s public IP. Your domain can be configured to point to multiple node IPs for traffic ingress.

    ### Flow overview:

    ```
    [ Client ]
       |
       v
    DNS round robin → node public IPs
       |
       +--> Node A: ingress controller (listens 80/443) → routes to applications
       +--> Node B: ingress controller (listens 80/443) → routes to applications
       +--> Node C: ingress controller (listens 80/443) → routes to applications
    ```

    ### How it works:

    * ***Workload Type:*** DaemonSet (one ingress controller pod per node).
    * ***Traffic Exposure:*** The ingress controller listens directly on ports **80/443** of each node’s public IP.
    * ***DNS Management:*** DNS records are configured to point directly to the public IPs of all nodes running the ingress controller (for example, using DNS round-robin).

    | Pros                                                                                 | Cons                                                                             |
    | :----------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
    | Simple and straightforward to set up.                                                | Relies on DNS round robin when no external load balancer is used.                |
    | Every node can accept traffic directly.                                              | DNS records may continue to point to unavailable nodes until they are refreshed. |
    | High availability through multiple node public IPs.                                  | Ports 80/443 are reserved on every node.                                         |
    | Can combine with an external load balancer for a more advanced traffic distribution. | Scaling is limited to one ingress pod per node.                                  |

    ### Step-by-Step Setup:

    <Steps>
      <Step title="Install NGINX Ingress Controller as a DaemonSet">
        <Warning>
          The *Pod Security Admission* plugin is enabled by default in all [io.net](http://io.net) Kubernetes clusters to enforce *Pod Security Standards* and enhance baseline cluster security.

          You may override *Pod Security Admission* settings at the namespace level when necessary. This can be useful for workloads such as ingress controllers or monitoring solutions that require less restrictive security policies.

          However, the recommended approach is to adapt your applications to run securely by configuring an appropriate `podSecurityContext`.
        </Warning>

        ```bash theme={null}
        kubectl create namespace ingress-nginx
        kubectl label namespace ingress-nginx pod-security.kubernetes.io/enforce=privileged

        helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
        helm repo update
        helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx \
          --namespace ingress-nginx \
          --set controller.kind=DaemonSet \
          --set controller.hostNetwork=true \
          --set controller.publishService.enabled=false \
          --set controller.dnsPolicy=ClusterFirstWithHostNet \
          --set controller.resources.requests.cpu=100m \
          --set controller.resources.requests.memory=128Mi \
          --set controller.service.enabled=true \
          --set controller.service.type=ClusterIP \
          --set controller.service.clusterIP=None \
          --set controller.admissionWebhooks.enabled=false \
          --set-string controller.nodeSelector.worker-node=true
        ```

        <Warning>
          Using `hostNetwork=true` reserves ports 80/443 on every node. Use `nodeSelector` and `tolerations` if you only want ingress on specific nodes.

          `--set 'controller.tolerations[0].operator=Exists'`

          `--set 'controller.nodeSelector.node-role\.kubernetes\.io/hostname='`
        </Warning>
      </Step>

      <Step title="Configure DNS for Node IPs">
        Point your domain to the public IPs of all nodes running the ingress controller, or follow the [*ExternalDNS Guide*](/guides/clouds/kubernetes/externaldns-guide).
      </Step>

      <Step title="Deploy Applications with Ingress">
        Deploy your applications and define Ingress resources to route incoming traffic to the appropriate services.
      </Step>
    </Steps>
  </Tab>
</Tabs>

## SSL/TLS Certificate Management

When exposing applications to the internet through a Kubernetes ingress controller, SSL/TLS certificates are required to securely terminate HTTPS traffic. `cert-manager` automates the issuance and renewal of certificates from **Let’s Encrypt**, integrating directly with Kubernetes Ingress resources to provide end-to-end HTTPS without manual certificate management.

In the setup below, `cert-manager` is installed in the cluster and configured to use a **DNS-01 challenge**, which is well suited for internet-facing applications, wildcard domains, and environments where ingress traffic reaches services through public IPs.

The following examples show how to install `cert-manager` and configure it with **Cloudflare** as the DNS provider.

Read more: [https://cert-manager.io/docs/configuration/acme/dns01/cloudflare/](https://cert-manager.io/docs/configuration/acme/dns01/cloudflare/)

### `cert-manager` with *Let's Encrypt* (Recommended)

```bash theme={null}
kubectl create namespace cert-manager
kubectl label namespace cert-manager pod-security.kubernetes.io/enforce=privileged

# Install cert-manager
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm upgrade --install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --set installCRDs=true

### Example for Cloudflare - https://cert-manager.io/docs/configuration/acme/dns01/cloudflare/

cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: cloudflare-api-key-secret
  namespace: cert-manager
type: Opaque
stringData:
  api-key: ${CLOUDFLARE_API_KEY}
---
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    email: ${cloudflare_email}
    server: https://acme-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      name: letsencrypt-dns01-private-key
    solvers:
    - dns01:
        cloudflare:
          email: ${cloudflare_email}
          apiKeySecretRef:
            name: cloudflare-api-key-secret
            key: api-key
EOF
```

### Example for Cloudflare with API Token (Recommended)

<Expandable title="Example">
  ```bash theme={null}
  cat <<EOF | kubectl apply -f -
  apiVersion: v1
  kind: Secret
  metadata:
    name: cloudflare-api-token-secret
    namespace: cert-manager
  type: Opaque
  stringData:
    api-token: ${CLOUDFLARE_API_TOKEN}
  ---
  apiVersion: cert-manager.io/v1
  kind: ClusterIssuer
  metadata:
    name: letsencrypt-prod
  spec:
    acme:
      email: ${YOUR_EMAIL}
      server: https://acme-v02.api.letsencrypt.org/directory
      privateKeySecretRef:
        name: letsencrypt-dns01-private-key
      solvers:
      - dns01:
          cloudflare:
            apiTokenSecretRef:
              name: cloudflare-api-token-secret
              key: api-token
  EOF
  ```
</Expandable>

### Example for Cloudflare with API Key

<Expandable title="Example">
  ```bash theme={null}
  cat <<EOF | kubectl apply -f -
  apiVersion: v1
  kind: Secret
  metadata:
    name: cloudflare-api-key-secret
    namespace: cert-manager
  type: Opaque
  stringData:
    api-key: ${CLOUDFLARE_API_KEY}
  ---
  apiVersion: cert-manager.io/v1
  kind: ClusterIssuer
  metadata:
    name: letsencrypt-prod
  spec:
    acme:
      email: ${CLOUDFLARE_EMAIL}
      server: https://acme-v02.api.letsencrypt.org/directory
      privateKeySecretRef:
        name: letsencrypt-dns01-private-key
      solvers:
      - dns01:
          cloudflare:
            email: ${CLOUDFLARE_EMAIL}
            apiKeySecretRef:
              name: cloudflare-api-key-secret
              key: api-key
  EOF
  ```

  ##
</Expandable>

<Tip>
  For an end-to-end HTTPS application example, refer to [Quick Start: Hello World with HTTPS](/guides/clouds/kubernetes/quick-start).
</Tip>

## Troubleshooting

### Health Checks

<AccordionGroup>
  <Accordion title="Check Ingress Controller Status" icon="circle-check">
    ```bash theme={null}
    kubectl get pods -n ingress-nginx
    kubectl logs -f deployment/nginx-ingress-ingress-nginx-controller -n ingress-nginx
    ```
  </Accordion>

  <Accordion title="Check Ingress Resources" icon="circle-check">
    ```bash theme={null}
    kubectl get ingress --all-namespaces
    kubectl describe ingress hello-ingress -n hello


    ```
  </Accordion>
</AccordionGroup>

### Common Issues and Solutions

<AccordionGroup>
  <Accordion title="DNS Not Resolving" icon="circle-exclamation">
    ```bash theme={null}
    # Check DNS propagation
    nslookup app.example.com
    dig app.example.com

    # Check ExternalDNS logs
    kubectl logs -f deployment/external-dns -n external-dns
    ```
  </Accordion>

  <Accordion title="SSL Certificate Issues" icon="circle-exclamation">
    ```bash theme={null}
    # Check certificate status
    kubectl get certificates --all-namespaces
    kubectl describe certificate hello-tls -n hello

    # Check cert-manager logs
    kubectl logs -f deployment/cert-manager -n cert-manager
    ```
  </Accordion>

  <Accordion title="Application Not Accessible" icon="circle-exclamation">
    ```bash theme={null}
    # Check ingress configuration
    kubectl describe ingress hello-ingress -n hello

    # Test backend service directly
    kubectl port-forward svc/hello-world 8080:80 -n hello
    # Then test: curl localhost:8080

    # Check ingress controller logs
    kubectl logs -f deployment/nginx-ingress-ingress-nginx-controller -n ingress-nginx
    ```
  </Accordion>

  <Accordion title="High Resource Usage" icon="circle-exclamation">
    ```bash theme={null}
    # Check resource usage
    kubectl top pods -n ingress-nginx
    kubectl describe pod <ingress-controller-pod> -n ingress-nginx

    # Adjust resource limits
    helm upgrade nginx-ingress ingress-nginx/ingress-nginx \
      --namespace ingress-nginx \
      --set controller.resources.limits.cpu=2000m \
      --set controller.resources.limits.memory=1Gi
    ```
  </Accordion>

  <Accordion title="Debug Commands" icon="circle-exclamation">
    ```bash theme={null}
    # Get all ingress-related resources
    kubectl get all,ingress,certificates -n ingress-nginx
    kubectl get all,ingress,certificates -n your-app-namespace

    # Test connectivity
    kubectl run test-pod --image=busybox --rm -it -- sh
    # Inside pod: wget -O- http://your-service.namespace.svc.cluster.local
    ```
  </Accordion>
</AccordionGroup>


# ExternalDNS Deployment Guide
Source: https://io.net/docs/guides/clouds/kubernetes/externaldns-guide

Learn how to deploy ExternalDNS to automate DNS record management for Kubernetes ingress controllers, including Deployment-based and DaemonSet-based ingress setups.

*ExternalDNS* automatically manages DNS records for applications exposed through your ingress controller. Configuration depends on whether the ingress controller is deployed as a [Deployment (Option 1)](https://io.net/docs/guides/clouds/kubernetes/exposing-to-the-internet#option-1) or a [DaemonSet (Option 2)](https://io.net/docs/guides/clouds/kubernetes/exposing-to-the-internet#option-2).

**Popular DNS providers:** Cloudflare, Route 53, Google Cloud DNS, DigitalOcean, Vultr, etc.

<Steps>
  <Step title="Deploy ExternalDNS">
    Choose one of the following examples based on your DNS provide:

    **Example for Cloudflare with API Token (Recommended)**

    <Note>
      API tokens are more secure than API keys as they can be scoped to specific zones and permissions.
    </Note>

    <Expandable title="Example">
      ```bash theme={null}
      kubectl create namespace external-dns
      kubectl create secret generic cloudflare-api-token -n external-dns --from-literal=apiToken=YOUR_API_TOKEN

      helm repo add external-dns https://kubernetes-sigs.github.io/external-dns/
      helm repo update

      helm upgrade --install external-dns external-dns/external-dns \
        --namespace external-dns \
        --set txtOwnerId=mycluster \
        --set provider.name=cloudflare \
        --set 'env[0].name=CF_API_TOKEN' \
        --set 'env[0].valueFrom.secretKeyRef.name=cloudflare-api-token' \
        --set 'env[0].valueFrom.secretKeyRef.key=apiToken'
      ```
    </Expandable>

    **Example for Cloudflare with API Key**

    Reference: [https://kubernetes-sigs.github.io/external-dns/latest/docs/tutorials/cloudflare/](https://kubernetes-sigs.github.io/external-dns/latest/docs/tutorials/cloudflare/)

    <Expandable title="Example">
      ```bash theme={null}
      kubectl create namespace external-dns
      kubectl create secret generic cloudflare-api-key -n external-dns --from-literal=apiKey=YOUR_API_KEY --from-literal=email=YOUR_CLOUDFLARE_EMAIL

      helm repo add external-dns https://kubernetes-sigs.github.io/external-dns/
      helm repo update

      helm upgrade --install external-dns external-dns/external-dns \
        --namespace external-dns \
        --set txtOwnerId=mycluster \
        --set provider.name=cloudflare \
        --set 'env[0].name=CF_API_KEY' \
        --set 'env[0].valueFrom.secretKeyRef.name=cloudflare-api-key' \
        --set 'env[0].valueFrom.secretKeyRef.key=apiKey' \
        --set 'env[1].name=CF_API_EMAIL' \
        --set 'env[1].valueFrom.secretKeyRef.name=cloudflare-api-key' \
        --set 'env[1].valueFrom.secretKeyRef.key=email'
      ```
    </Expandable>

    <Note>
      By default, *ExternalDNS* runs with the `upsert-only` policy, which allows it to create and update DNS records but not delete them. To enable record deletion, change the policy to `sync`.

      `--set policy=sync`
    </Note>
  </Step>

  <Step title="Annotate the Ingress Controller Service">
    The annotations you need depend on which ingress controller option you chose.

    **Option 1 (Deployment with the LoadBalancer Service)**

    ```bash theme={null}
    kubectl annotate svc ingress-nginx-controller \
      -n ingress-nginx \
      external-dns.alpha.kubernetes.io/hostname="*.example.com"
    ```

    * Wildcard domains simplify DNS management for multiple applications.
    * Eliminates the need to annotate each Ingress resource individually.
    * DNS records are automatically updated when the Service’s `externalIPs` change.
    * ExternalDNS monitors the LoadBalancer Service and creates DNS **A** records that point to the configured `externalIPs`.

    **Option 2 (DaemonSet with hostNetwork)**

    ```bash theme={null}
    kubectl annotate svc ingress-nginx-controller \
      -n ingress-nginx \
      external-dns.alpha.kubernetes.io/hostname="*.example.com" \
      external-dns.alpha.kubernetes.io/endpoints-type=NodeExternalIP
    ```

    * The `endpoints-type=NodeExternalIP` annotation instructs *ExternalDNS* to use the external IPs of nodes where the DaemonSet pods are running.
    * This results in DNS **A** records pointing to the external IPs of all worker nodes.
    * DNS records are automatically updated as nodes are added to, or removed from, the cluster.
  </Step>
</Steps>

<Tip>
  For an end-to-end HTTPS application example, refer to [Quick Start: Hello World with HTTPS](/guides/clouds/kubernetes/quick-start).
</Tip>


# Optimizations
Source: https://io.net/docs/guides/clouds/kubernetes/optimizations

Explore Kubernetes optimizations on io.net Cloud, including Kubernetes control plane design, minimal GPU cluster sizing, and master node scheduling best practices.

This section explains several infrastructure design decisions and provides guidance on how to optimize your Kubernetes cluster for performance and reliability.

## Control Plane Architecture

By default, a Kubernetes cluster is provisioned with **three CPU-only master (control plane) nodes** running in a **separate cloud environment** from your worker nodes.

### Why this design was chosen?

This architecture enables two key benefits:

* **Minimum cluster size of one GPU VM:** You can create a functional Kubernetes cluster with just a single GPU Virtual Machine, avoiding the cost of running multiple GPU nodes purely for control plane redundancy.
* **Improved fault tolerance without extra GPU cost:** Running three dedicated CPU-only master nodes provides higher availability for the control plane without requiring two or more expensive GPU VMs per cluster.

## Untainted Master Nodes

By default, **master nodes are not tainted**. This means Kubernetes may schedule your workloads (pods) onto master nodes in the control plane cloud.

### Why master nodes are not tainted by default

* Reduce cluster creation time
* Allow clusters to become usable immediately without additional configuration.

## Avoid Running Pods on Master Nodes

Running application pods on master nodes can lead to several issues, such as:

* **Risk to control plane stability:** Application workloads may interfere with critical Kubernetes components responsible for scheduling, networking, and cluster orchestration.
* **Increased latency:** Because master nodes run in a separate cloud, communication between services may experience higher latency when one service runs on a master node and another runs on a worker node.

## Recommended Optimisation - Taint Master Nodes

To prevent pods from being scheduled on master nodes, apply a taint to all control plane nodes.

Run the following command:

```bash theme={null}
kubectl taint nodes -l node-role.kubernetes.io/control-plane node-role.kubernetes.io/control-plane=:NoSchedule
```

### What this does

* Prevents application pods from being scheduled on master nodes.
* Ensures master nodes are reserved exclusively for control plane workloads.
* Improves performance isolation and overall cluster reliability.


# Quick Start: Hello World with HTTPS
Source: https://io.net/docs/guides/clouds/kubernetes/quick-start

Deploy a Kubernetes Hello World application with HTTPS using Ingress, ExternalDNS, and cert-manager, and expose it securely to the internet step by step.

This walkthrough demonstrates how to deploy a simple application and expose it securely to the internet using Kubernetes Ingress. It brings together the components such as, [Ingress routing](/guides/clouds/kubernetes/exposing-to-the-internet), [ExternalDNS for DNS management](/guides/clouds/kubernetes/externaldns-guide), and [cert-manager for automated TLS certificates](https://io.net/docs/guides/clouds/kubernetes/exposing-to-the-internet#ssl%2Ftls-certificate-management), to deliver a working **HTTPS-enabled** application from start to finish.

<Steps>
  <Step title="Deploy the Application">
    ```bash theme={null}
    kubectl create namespace hello
    kubectl run hello-world \
      --image=k8s.gcr.io/echoserver:1.10 \
      --port=8080 \
      -n hello
    ```
  </Step>

  <Step title="Expose the Application with a Service">
    ```bash theme={null}
    kubectl expose pod hello-world \
      --type=ClusterIP \
      --port=80 \
      --target-port=8080 \
      -n hello
    ```
  </Step>

  <Step title="Create an Ingress Resource with HTTPS">
    ```yaml theme={null}
    cat <<EOF | kubectl apply -f -
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: hello-ingress
      namespace: hello
      annotations:
        cert-manager.io/cluster-issuer: "letsencrypt-prod"
        nginx.ingress.kubernetes.io/ssl-redirect: "true"
    spec:
      ingressClassName: nginx
      tls:
      - hosts:
        - app.example.com
        secretName: hello-tls
      rules:
      - host: app.example.com
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: hello-world
                port:
                  number: 80
    EOF
    ```
  </Step>

  <Step title="Test the Application">
    * ExternalDNS automatically manages DNS records when the ingress controller Service is annotated, though synchronization may take a few minutes.
    * Verify that your domain points to the ingress controller’s public IP address(es).
    * Open `https://app.example.com/` in a browser to confirm the application is reachable and displaying “Hello World”.
  </Step>
</Steps>

For additional examples, troubleshooting guidance, or clarification on any topics covered in this guide, refer to the resources below:

* [Exposing Applications to the Internet](/guides/clouds/kubernetes/exposing-to-the-internet)
* [ExternalDNS Deployment Guide](/guides/clouds/kubernetes/externaldns-guide)
* [Optimizations](/guides/clouds/kubernetes/optimizations)


# Monitor & Manage Clusters
Source: https://io.net/docs/guides/clouds/monitor-manage-clusters

Manage Clusters offers a comprehensive interface for configuring and monitoring GPU and CPU clusters, enabling users to optimize resource allocation and performance. With advanced management tools, users can efficiently deploy workloads, scale resources, and gain real-time insights into cluster health and utilization.

To access the dashboard, log into [io.net](http://io.net) and select **Manager Clusters**.

## View Your Cluster

To see all the details about your cluster, click on it in the **Cluster** tab.  The screenshot below highlights what you can expect to see in a hired, active cluster.

<Frame>
  <img alt="" />
</Frame>

#### Clusters Tab

The **Clusters** tab provides a quick overview of all your clusters, both active and inactive.

#### Sort Clusters

Use the sorting options to find the cluster you're looking for easily. Sort by status (**Running, Completed, Failed, Destroyed**) or search by keyword.

<img alt="Monitor2 Pn" title="Monitor2 Pn" />

## Cluster Management Actions

These actions can be done if a cluster is currently running.

#### Terminate Cluster

Click **Terminate Cluster** in the bottom right to end your session.

<img alt="Monitor3 Pn" title="Monitor3 Pn" />

#### Extend Cluster

To keep your cluster active for longer, simply click **Extend Cluster**. You'll be charged the same amount as your original transaction.

<img alt="Monitor4 Pn" title="Monitor4 Pn" />

## Actions

A completed cluster provides the option to archive the cluster.  Click **Archive** in the bottom right to archive this cluster.

**Run Jobs and Monitor Your Cluster**

Ready to start working on your cluster? You can run your jobs using either Visual Studio or Jupyter Notebook. The Ray Dashboard lets you manage and monitor everything, including your cluster and running jobs.

On your cluster's details page, grab the **IDE Password**, and then click on **Jupyter Notebook**, **Visual Studio**, or the **Ray Dashboard** to get started

<Frame>
  <img alt="" />
</Frame>

To access your application, enter the **IDE Password**.

<Warning>
  Once your cluster's time expires, you'll lose access to the IDEs and the Ray Dashboard.
</Warning>

#### Archive a Cluster

Once a cluster is complete, you can archive it. Click **Archive** at the bottom right to archive a cluster.

> 🚧 You can’t renew a cluster after it’s completed.

## Cluster Information

Click on a cluster in the **Cluster** tab to view the details associated with the cluster. In the screenshot below, a completed cluster has been selected.

<Frame>
  <img alt="" />
</Frame>

## Monitor the following on the right:

| Action                     | Description                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Compute Hours**          | Shows how long a single instance has been running and consuming resources. Includes “Served” and “Remaining” times. |
| **Funds Used or Refunded** | The amount you've spent or had refunded for cluster operations.                                                     |
| **Connectivity Tier**      | Your chosen level of connectivity for the cluster (download / upload speeds).                                       |
| **Security Compliance**    | The selected security setting (e.g. end-to-end encryption).                                                         |
| **Locations**              | Geographic location(s) where your GPUs are located.                                                                 |

<Frame>
  <img alt="" />
</Frame>

## Monitor the following on the left:

| Action           | Definition                                                                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **All Workers**  | Allows you to filter the view by selecting different groups of workers. This option is currently set to show all workers in the cluster.                                                                           |
| **\[#] Workers** | Indicates that the dashboard currently shows four workers in the cluster that are active or relevant to the task being monitored. The panel below labels these workers as "IO Worker 1," "IO Worker 2," and so on. |
| **\[#] GPUs**    | Shows that there are 4 GPUs (Graphics Processing Units) in use across the cluster. Each worker seems to have one GPU assigned to it, as indicated by the details in each worker's panel.                           |
| **Search**       | The search bar allows you to quickly find specific workers, GPUs, or tasks by searching based on keywords, worker names, device IDs, or other identifiers.                                                         |

## Detailed information for each worker

| Feature                              | Description                                                                                                                                                             |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Decentralized Network                | IO Cloud uses a network of computers (called "IO workers") to create powerful GPU clusters. This means you're not relying on a single company for your computing power. |
| Self-healing                         | If one part of the cluster has issues, the others automatically take over, keeping your projects running smoothly.                                                      |
| Easy to Use                          | You can easily run your AI projects using Python code, just like on any other cloud platform.                                                                           |
| Built on Industry-leading Technology | IO Cloud is powered by the same technology used by OpenAI to train its powerful AI models, such as GPT-3 and GPT-4.                                                     |

<Frame>
  <img alt="" />
</Frame>

## Selecting a worker shows you the following

| Feature                         | Description                                                                                                                                                                                                                                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Worker Name and Status          | Indicates the worker's status, such as **Completed**, **Running**, **Pending**, or **Failed**. A green dot signifies successful completion.                                                                                                                                                         |
| Device ID                       | The unique identifier for the specific GPU device in the worker node.                                                                                                                                                                                                                               |
| GPU Information                 | **GeForce RTX 3060 Ti** (GPU type): Each worker is equipped with an NVIDIA GeForce RTX 3060 Ti GPU. **x1**: Number of GPUs utilized (in this case, one unit). **Uptime in Cluster**: Displays uptime, showing that the worker has been fully operational without downtime for the monitored period. |
| Activity Consistency Status Bar | A visual representation of the worker’s uptime, consisting of 10 white squares filled in to indicate 100% uptime.                                                                                                                                                                                   |

<img alt="Monitor9 Pn" title="Monitor9 Pn" />


# Overview
Source: https://io.net/docs/guides/clouds/run-jobs-on-clusters

IO Cloud users can run jobs on their clusters using Visual Studio Code and Jupyter Notebook.

Machine learning (ML) has revolutionized various fields by enabling data-driven decision-making and automating complex tasks. As ML models become more sophisticated, the computational power required to train and deploy these models increases significantly. Running machine learning jobs on clusters, which consist of interconnected computers working together, has become a critical approach to meet these demands. This document provides an overview of the benefits, setup, and best practices for running machine learning jobs on clusters, ensuring efficient and scalable ML workflows.

### Benefits of Running ML Jobs on Clusters

1. **Enhanced Computational Power** Clusters aggregate the computational resources of multiple machines, providing the necessary power to handle large-scale ML tasks. This enables the training of complex models on vast datasets that would be infeasible on a single machine.
2. **Scalability** Clusters offer the ability to scale resources up or down based on the needs of the ML job. This flexibility allows for efficient resource management and cost optimization, ensuring that resources are allocated appropriately for different stages of the ML workflow.
3. **Parallel Processing** By distributing tasks across multiple nodes in a cluster, ML jobs can be executed in parallel, significantly reducing the time required for training and inference. This parallelism is crucial for handling the iterative and computationally intensive nature of ML algorithms.
4. **Fault Tolerance and Reliability** Clusters are designed with fault tolerance in mind. In the event of hardware failure or other issues, the workload can be redistributed among other nodes, minimizing downtime and ensuring the reliability of ML job execution.


# Overview
Source: https://io.net/docs/guides/clouds/start-using-io-cloud

Discover the simple steps for creating, configuring, deploying, and managing clusters, giving you complete control over your computing power.

## Introduction

IO Cloud enables the deployment and management of on-demand, decentralized GPU clusters, giving users access to powerful GPU resources without significant hardware investments or the complexity of managing infrastructure. IO Cloud democratizes GPU access by leveraging a decentralized model, providing machine learning engineers and developers with the same seamless experience as traditional cloud providers.

The platform utilizes a distributed network of nodes, IO workers, to offer flexible, scalable compute resources. IO Cloud clusters are self-healing, fully meshed GPU systems that ensure high availability and fault tolerance. With IO Cloud, you can tap into a decentralized network of GPUs and CPUs capable of running Python-based machine learning workloads. It is ideal for AI projects requiring distributed compute. The platform is natively built on the Ray framework, the same distributed computing technology used by OpenAI to train models like GPT-3 and GPT-4 across hundreds of thousands of servers.

<iframe title="Start Using IO Cloud: Your First Steps Explained" />

## IO Clouds Integration Flow

The diagram below provides a high-level overview of how users integrate with IO Cloud - from choosing a compute resource to launching AI workloads. It illustrates the end-to-end flow across key components, including cluster selection, container deployment, and runtime execution.

<Frame>
  <img alt="" />
</Frame>

## Create Account

To create an account, go to [cloud.io.net](https://cloud.io.net/cloud/home) using Google, Apple ID, GitHub, Hugging Face, X, Worldcoin, or simply with a one-time password by clicking the "Login with Email" button.

<img alt="Newlogin1 Jp" />

#### Payments

IO Cloud simplifies the process of paying for GPU clusters by offering two convenient payment methods:

* **Solana:** This cryptocurrency option enables fast, secure transactions. You can configure a Solana wallet either during account creation or through your Account Settings. Once configured, you can fund your wallet or proceed with payment for your GPU cluster.
* **Credit Cards:** We accept all major credit cards, providing a straightforward payment solution.

To learn more about payment options, visit our [IO Cloud Payments](https://io.net/docs/guides/payment/io-cloud-payments) page.

#### App Guide

The home page offers the following options:

| Action                         | Definition                                                  |
| ------------------------------ | ----------------------------------------------------------- |
| Deploy a Cluster               | Create a new cluster for your workloads.                    |
| Browse the GPU Marketplace     | Explore and select GPUs for your clusters.                  |
| Add Funds to Your Balance      | Top up your account for cluster usage.                      |
| View and Monitor Your Clusters | Track the status and performance of your existing clusters. |

## Clusters

io.net offers three distinct cluster types to power your AI projects:

<Frame>
  <img alt="" />
</Frame>

### Ray Cluster

Designed to run distributed applications efficiently across multiple nodes.

* **Powered by the Ray framework:** A widely-used open-source framework for building and managing distributed applications.
* **Universal API:** Delivers a consistent interface for creating and managing distributed applications across various hardware configurations.
* **Scalable Infrastructure:** Comprises multiple interconnected nodes collaborating to execute tasks and manage resources efficiently.

To view detailed instructions on Ray clusters, see [Deploy Ray Cluster](/guides/clouds/deploy-ray-cluster).

### VM on Demand

Provision dedicated bare-metal machines instantly, giving you complete control over the hardware for performance-critical workloads.

* **Direct Hardware Access:** Run workloads directly on physical machines with no virtualization layer.
* **Maximum Performance:** Eliminate virtualization overhead for speed, isolation, and reliability.
* **Flexible Setup:** Select your preferred processor and location, then deploy in minutes.

To view detailed instructions, see [Deploy VM on Demand Cluster](/guides/clouds/deploy-vm-on-demand).

### Container-as-a-Service (CaaS)

Allows you to configure and deploy containers on powerful GPU-backed infrastructure through a simple, guided interface.

* **Step-by-Step Wizard:** Set image, command, ports, environment variables, and more.
* **Cluster & Location Choice:** Select from available GPUs and regions that meet your needs.
* **Scalable & Fast:** Built for AI and compute-heavy workloads with rapid setup.

To view detailed instructions, see [Deploy Container](/guides/clouds/deploy-containers).

### Bare Metal on Demand

Gives you full access to physical hardware without any virtualization layer — ideal for low-level control and maximum performance.

* \*\*Direct-to-Hardware Access: \*\*Run workloads directly on machines for optimal speed and isolation.
* \*\*No Virtualization Overhead: \*\*Perfect for users with specialized or custom environments.
* \*\*Custom Configuration: \*\*Choose your processor and location, then deploy instantly.

To view detailed instructions, see [Deploy Bare Metal Instance](/guides/clouds/deploy-bare-metal-cluster).

## Clusters Tabs

The Cluster tabs provide a central hub for managing your deployed clusters. Each tab displays a list of clusters, categorized by type, with details such as:

* **Name:** The unique identifier for the cluster.
* **Accelerator (GPU):** The type of GPU used in the cluster.
* **Status:** The current state of the cluster (e.g., running, stopped, pending).
* **Remaining Compute Hours:** The remaining time on your cluster's billing cycle.

<Frame>
  <img alt="" />
</Frame>

From here, you can perform actions like:

* **Rename:** Change the name of a cluster.
* **Extend:** Increase the duration of your cluster's billing cycle.
* **Terminate:** Stop and delete a cluster.

Each cluster tab also provides quick access to essential management tools:

* **Visual Studio:** An integrated code editing and debugging development environment.
* **Jupyter Notebook:** An interactive environment for data analysis and visualization.
* **Ray Dash:** A dashboard for monitoring and managing distributed applications.

For a detailed explanation of monitoring and managing your clusters, see [Monitor and Manage Clusters](/guides/clouds/monitor-manage-clusters).

<Frame>
  <img alt="" />
</Frame>


# Coin Restrictions
Source: https://io.net/docs/guides/coin/coin-restrictions



## Token Allocation and Restrictions

### Investors

Tokens allocated to investors are restricted for three years. Transfer restrictions are lifted in 24 equal tranches, starting at the end of the 13th month and continuing monthly until the 36th month following the Initial Distribution Date.

### Employees & Core Members

Tokens allocated to employees of io.net Inc. are restricted for four years. Transfer restrictions are lifted in 36 equal tranches, starting at the end of the 13th month and continuing monthly until the 48th month following the Initial Distribution Date.


# Overview
Source: https://io.net/docs/guides/coin/io-coin

What is IO Coin ($IO)?

IO Coin (\$IO) is the native cryptocurrency of the IOG Network, powering its ecosystem and facilitating seamless interactions between key participants. These participants include:

### GPU Renters (Users):

Machine Learning Engineers, developers, and individual consumers who use \$IO to rent GPU computing power for tasks like deploying GPU clusters, running cloud gaming instances, or building applications such as Unreal Engine 5 pixel streaming. Users can also leverage \$IO for serverless AI model inferences via platforms like BC8.ai and other apps hosted on io.net.

### GPU Owners (Suppliers):

Independent data centers, crypto mining farms, and professional miners supply underutilized GPU computing power to the network. They earn \$IO tokens by providing this compute power.

### \$IO Coin Holders (Community):

Supporters who stake \$IO to secure the network, earn rewards and align incentives across the ecosystem for sustainable growth and adoption.

These roles are flexible—anyone can participate in multiple capacities (e.g., a GPU owner can also be an \$IO holder and a GPU renter).

***

### Universal Payment System

The IOG Network’s payment system revolves around \$IO. While users can pay in fiat (e.g., USD), USDC, or other supported cryptocurrencies, all payments are ultimately converted to \$IO behind the scenes. This approach reduces friction in transactions and avoids traditional issues like escrow and delayed billing, while maintaining strong demand for \$IO.

#### User Payments:

* Customers can pay in USDC or fiat for GPU services.
* Suppliers receive compensation in \$IO, creating demand for the token.

#### Supplier Options:

* Suppliers can opt to receive payments in native \$IO or convert earnings into USDC, based on their preference.

***

### Fee Structure: Incentivizing \$IO Use

The network’s fee model encourages the use of \$IO for transactions while charging minimal fees for critical operations like staking and rewards.

#### User Fees:

* Payments in USDC: 2% facilitation fee.
* Payments in \$IO: No fee.

#### Supplier Fees:

* Rewards earned through network emissions: No fee.

* Compute job earnings:

  * Payments in USDC: 2% fee.
  * Payments in \$IO: No fee.

This fee structure ensures that \$IO remains the most cost-effective way to transact on the network.

***

### Network Security and Collateralization

\$IO is integral to securing and maintaining the network’s integrity. Two primary mechanisms achieve this:

#### Node Collateral Requirements:

A minimum amount of \$IO must be staked to operate a node and earn idle rewards.

#### Staking for Rewards:

Additional \$IO can be staked up to a maximum limit per node, allowing holders to earn rewards while contributing to the network’s security and reliability.

These mechanisms incentivize active participation and align interests across the network.

***

### Why \$IO Matters

\$IO is more than just a transactional token—it’s the backbone of the IOG Network, driving economic activity and ensuring network health. Its design creates a dynamic, interconnected ecosystem that benefits Renters, Suppliers, and Holders alike.

By reducing payment friction, offering a flexible fee structure, and integrating network security features, \$IO builds a sustainable framework for growth and innovation.

***

### Call to Action

Explore the IOG Network and see how \$IO can power your GPU-driven projects or help you monetize unused resources. Whether you’re an AI developer, a data center owner, or a blockchain enthusiast, \$IO offers a unified, efficient, and scalable solution.

### Join the IOG Network today and experience the future of decentralized computing!


# IO Coin Allocation
Source: https://io.net/docs/guides/coin/io-coin-allocation



### Initial \$IO Allocation

The genesis supply of \$IO is set at 500,000,000 tokens, distributed across five categories:

* Seed Investors
* Series A Investors
* Core Contributors
* Research & Development
* Ecosystem and Community

Over the next 20 years, this supply will grow to 800,000,000 \$IO through emissions designed to incentivize network growth and adoption.

***

### Unlocks and Rewards

The initial 500 million tokens are subject to specific unlock schedules outlined below. In addition, the circulating supply increases as rewards are issued. Rewards are unlocked upon receipt and immediately added to the circulating supply.

#### Key Definitions:

* Circulating Supply: The amount of \$IO available in general circulation without on-chain transfer restrictions.
* Locked Supply: The portion of \$IO that is unvested and unavailable for circulation.
* Available Supply: The sum of circulating supply and issued (but locked) tokens. Rewards not yet issued are excluded from this figure.
* Max Supply: The total number of \$IO tokens that will exist after all emissions have been completed.

A breakdown of these supply categories and schedules is provided in the chart below:

<Frame>
  <img alt="" />
</Frame>

***

### Pro Forma Allocation

As the IOG Network emits rewards over time, the proportional share held by early backers and Core Contributors will gradually decrease. Consequently, the Community’s allocation will expand, reaching approximately 50% of the total supply once all rewards have been distributed.

<img alt="" />

<img alt="" />


# IO Tokenomics
Source: https://io.net/docs/guides/coin/io-tokenomics

Tokenomics defines the structure and mechanics of a token, covering aspects like distribution, supply-demand dynamics, utility, incentives, governance, and value capture. This document provides transparency into the tokenomics of io.net.

## Key Principles

### Fixed Maximum Supply:

The total supply of \$IO is capped at 800 million coins.

* 500 million \$IO will be distributed at launch.
* The remaining 300 million \$IO will be emitted as hourly rewards to Suppliers and their Stakers over time.

### Hourly Rewards:

Rewards are distributed hourly to Suppliers and their Stakers over 20 years following a disinflationary model:

* Starts at 8% annual inflation in year 1.
* Decreases by 1.02% monthly (/\~12% per year) until the cap of 800 million \$IO is reached.

Charts detail the emission rates, annual inflation, and the distribution of emitted vs. remaining coins.

<Frame>
  <img alt="" />
</Frame>

**Figure 1. Emission rate as a function of total emissions pool.**

<Frame>
  <img alt="" />
</Frame>

**Figure 2 Year Inflation Rate**

<Frame>
  <img alt="" />
</Frame>

**Figure 3: Coins already emitted by year versus remaining Coins to be emitted.**

### Burn Mechanism:

\$IO employs a programmatic coin burn system:

* Revenues from the IOG Network are used to purchase and burn \$IO.
* The burn amount is adjusted dynamically based on \$IO's price, reducing supply and creating deflationary pressure.

***

## Revenue Streams and Fee Structure

io.net generates revenue through fees charged to both Users (Renters) and Suppliers:

**GPU Renter Fees**

* Reservation Fee:
  * 0.25% of the total compute reservation cost is added to the Renter's cost.

* Payment Fee:

  * 2% fee for payments made in 100% USDC.
  * No fees for payments made in 100% \$IO.

**GPU Supplier Fees**

* Reservation Fee:
  * 0.25% fee on the total reservation cost, charged to the Supplier upon payment for compute.

* Payment Fee:

  * 2% fee for payments in 100% USDC.
  * No fees for payments in 100% \$IO.

***

## Summary of Tokenomics Features

* **Fixed Supply:** Capped at 800 million \$IO.
* **Hourly Rewards:** Emitted to Suppliers and Stakers over 20 years with decreasing inflation.
* **Burn Mechanism:** Reduces supply via programmatic burns funded by network revenue.

These mechanisms ensure a balanced and sustainable ecosystem for \$IO.


# Monthly Token Emission Schedule
Source: https://io.net/docs/guides/coin/ionet-monthly-token-emission-schedule

io.net proposes transitioning from an hourly to a monthly disinflation schedule while maintaining the original objective of emitting 300 million IO tokens over 20 years. This streamlined approach simplifies calculations and management while adhering to the same disinflationary principles.

io.net will release 300 million tokens over 20 years in addition to the 500 million tokens available at launch. The proposed emission schedule simplifies the frequency of disinflation from hourly to monthly while achieving the same total supply target of 800 million tokens.

* Initial Supply at Launch: 500,000,000 tokens
* Total Additional Emissions: 300,000,000 tokens over 20 years
* Final Cap: 800,000,000 tokens
* Disinflation Frequency: Monthly
* Starting Inflation Rate: 8% per year (0.667% per month)
* Disinflation Factor: /\~0.989849199 per month
* Disinflation periods: 240 (20 years × 12 months)

The monthly emission schedule follows a disinflationary curve, meaning that the inflation rate decreases over time. It starts at 8% annually and gradually reduces each month until it reaches near-zero inflation at the end of 20 years.

### Monthly Emission Schedule

The table below demonstrates the first 12 months of emissions under the proposed schedule:

| Month          | Total Supply   | Inflation Rate (%) | Tokens Emitted |
| -------------- | -------------- | ------------------ | -------------- |
| July 2024      | 500,000,000.00 | 0.667              | 3,333,333      |
| August 2024    | 503,335,000.00 | 0.660              | 3,299,497      |
| September 2024 | 506,658,165.73 | 0.654              | 3,266,003      |
| October 2024   | 509,969,316.47 | 0.647              | 3,232,850      |
| November 2024  | 513,268,276.00 | 0.640              | 3,200,033      |
| December 2024  | 516,554,872.59 | 0.634              | 3,167,549      |
| January 2025   | 519,828,938.94 | 0.627              | 3,135,395      |
| February 2025  | 523,090,312.18 | 0.621              | 3,103,568      |
| March 2025     | 526,338,833.81 | 0.615              | 3,072,063      |
| April 2025     | 529,574,349.69 | 0.608              | 3,040,879      |
| May 2025       | 532,796,709.99 | 0.602              | 3,010,011      |
| June 2025      | 536,005,769.19 | 0.596              | 2,979,456      |

### Visual Representation

Below is a chart illustrating the total supply growth and token emissions for the first 12 months:

<Frame>
  <img alt="" />
</Frame>

### Formula for Emissions Calculation

The formula for calculating emissions under the proposed monthly schedule is as follows:

**Emissions\_T = Total Supply\_T-1 × Inflation Rate\_T**

Where:

* Inflation Rate\_T = Inflation Rate\_T-1 × (1 - Disinflation Factor)
* Disinflation Factor ≈ 0.010150801 (or 1.01508%)

#### Initial Inflation Rate

Initial Monthly Inflation Rate = Annual Inflation Rate ÷ Months Per Year Initial Monthly Inflation Rate = 8% ÷ 12 = 0.667%

### Detailed Calculations: First Three Months

**Month 1 (July 2024):**

The first month’s emissions are based on the initial supply of 500,000,000 tokens and an inflation rate of 0.667%.

Emissions\_1 = 500,000,000 × 0.667% Emissions\_1 = 3,333,333.33 tokens

At the end of Month 1:

* Total Supply: 500,000,000 + 3,333,333.33 = 503,333,333.33

**Month 2 (August 2024):**

The disinflation factor reduces the inflation rate for Month 2:

Inflation Rate\_2 = 0.667% × (1 - 0.010150801) Inflation Rate\_2 ≈ 0.660%

The emissions for Month 2 are:

Emissions\_2 = 503,333,333.33 × 0.660% Emissions\_2 ≈ 3,299,497.40 tokens

At the end of Month 2:

* Total Supply: 503,333,333.33 + 3,299,497.40 = 506,632,830.73

**Month 3 (September 2024):**

The inflation rate for Month 3 is further reduced:

Inflation Rate\_3 = 0.660% × (1 - 0.010150801) Inflation Rate\_3 ≈ 0.654%

The emissions for Month 3 are:

Emissions\_3 = 506,632,830.73 × 0.654% Emissions\_3 ≈ 3,266,003.20 tokens

At the end of Month 3:

* Total Supply: 506,632,830.73 + 3,266,003.20 = 509,898,833.93

### Conclusion

The proposed monthly schedule achieves the same emission goal of 300 million tokens over 20 years but simplifies management and calculations compared to the current hourly schedule. By transitioning to monthly emissions:

1. Simplification: Reduces emission frequency from 175,319 hourly epochs to 240 monthly epochs.
2. Accuracy: Maintains the same cumulative disinflation effect over 20 years.
3. Ease of Implementation: Aligns better with monthly financial and operational reporting cycles.


# Confidential Chat
Source: https://io.net/docs/guides/confidential-inference/confidential-chat

io.net provides a web-based confidential chat interface where you can interact with AI models securely, with full privacy guarantees and verifiable attestation.

## Getting Started

### Step 1: Select a Secure Model

1. Navigate to [ai.io.net/ai/models](https://ai.io.net/ai/models)
2. Look for models with the **SECURE AI** badge
3. Click on a secure model to start a confidential chat session

<img alt="Image" />

### Step 2: Start Chatting Privately

Once you select a secure model, you enter a private chat session with the following guarantees:

* **Messages are never saved** - your conversation is not stored on any server
* **No observation** - io.net staff cannot see your prompts or responses
* **Session-only context** - only the current chat is passed to the LLM for context
* **End-to-end verification** - every response is cryptographically signed

## Privacy Guarantees

| Feature           | Description                                                       |
| ----------------- | ----------------------------------------------------------------- |
| Zero storage      | Messages exist only in your browser and the TEE during processing |
| No logging        | Conversation content is never written to logs                     |
| Session isolation | Each chat session is independent and ephemeral                    |
| Signed responses  | Every AI response includes a cryptographic signature              |

## Verifying Attestation and Signatures

Every message in a confidential chat can be verified. Click the **Secure AI** label under any AI response to open the verification panel.

<img alt="Image" />

### Attestation Report

The verification panel displays the full attestation report, proving:

* The response came from a genuine NVIDIA GPU running in TEE mode
* The specific hardware configuration and firmware version
* The container image hash (`image_digest`) running inside the secure enclave - compare with the expected digest from the [latest official release](https://github.com/ionet-official/attestation-agent/releases) to confirm the container hasn't been tampered with

### Message Signatures

For each AI response, you can view:

| Field               | Description                                           |
| ------------------- | ----------------------------------------------------- |
| **Signed Text**     | The exact content that was signed                     |
| **Signature**       | The cryptographic signature proving authenticity      |
| **Signing Address** | The public key that signed (matches attestation)      |
| **Algorithm**       | The signing algorithm used (e.g., ecdsa)              |
| **Image digest**    | SHA256 hash of the container image running in the TEE |

This allows you to independently verify that:

1. The response was generated by the attested hardware
2. The content was not modified after generation
3. The signing key matches the attestation report

## Best Practices

### For Maximum Privacy

* **Start fresh sessions** for sensitive topics
* **Verify signatures** for critical responses
* **Check attestation** to confirm hardware authenticity
* **Clear your browser** after sensitive sessions

### Understanding Session Context

Since messages are not saved:

* The AI only has context from the current session
* New chat starts a new session with no history
* You cannot retrieve previous confidential conversations

This is by design - true privacy means no persistent storage.

## What's Next

* [Quick Start API](./quick-start) - For developers building integrations
* [Verification Guide](./verification-guide) - Deep dive into verifying attestation and signatures


# Overview
Source: https://io.net/docs/guides/confidential-inference/overview

io.net's Confidential Inference enables verifiable AI inference where you can cryptographically prove that your prompts were processed securely on trusted hardware, without storing any of your data.

## Don't Trust, Verify

Traditional AI APIs require you to trust that the provider handles your data securely. With confidential compute, you can **verify** these guarantees cryptographically:

* **Hardware attestation** proves your request ran on genuine, secure GPU hardware
* **Response signatures** prove the output came from the attested machine
* **Nonce verification** proves the attestation is fresh, not replayed

## How It Works

1. **Request attestation** with a unique nonce you generate
2. **io.net routes** your request to a confidential compute-enabled GPU machine
3. **GPU TEE** generates a hardware attestation report with a signing key
4. [**Verify**](./guides/confidential-inference/verification-guide) the attestation report proves the machine is genuine and secure
5. [**Run inference**](./guides/confidential-inference/quick-start) - responses are signed with the attested key
6. **Verify signatures** to prove responses came from the attested machine

## Key Components

### Trusted Execution Environment (TEE)

The GPU runs inside a Trusted Execution Environment that provides:

* **Memory isolation** - your data is encrypted in memory and inaccessible to the host
* **Code integrity** - only authorized code can run inside the TEE
* **Hardware attestation** - the GPU can prove its identity and configuration

### Attestation Agent (Open Source)

The attestation agent running on GPU machines is fully open source. You can audit the code that generates attestation reports and signs responses:

**Repository:** [https://github.com/ionet-official/cc-attestation-agent-api](https://github.com/ionet-official/cc-attestation-agent-api)

This transparency allows you to:

* Verify what code is running inside the TEE
* Understand exactly what is being attested
* Build confidence in the verification process

### Attestation Reports

When you request attestation, you receive:

| Field             | Description                                                          |
| ----------------- | -------------------------------------------------------------------- |
| `gpu`             | NVIDIA GPU attestation report proving the GPU identity and TEE state |
| `cpu`             | CPU attestation report (when available) for additional verification  |
| `image_digest`    | SHA256 hash of the container image running in the TEE                |
| `signing_address` | Public key the machine will use to sign inference responses          |
| `nonce`           | Your nonce echoed back, proving freshness                            |

### Response Signatures

Every inference response includes cryptographic signatures in the response headers:

| Header            | Description                                         |
| ----------------- | --------------------------------------------------- |
| `text`            | The content that was signed                         |
| `signature`       | Cryptographic signature of the text                 |
| `signing_address` | Public key that signed (matches attestation report) |
| `signing_algo`    | Algorithm used for signing                          |

## What You Can Prove

| Check                                 | What It Proves                                                           |
| ------------------------------------- | ------------------------------------------------------------------------ |
| GPU attestation report is valid       | Response came from genuine NVIDIA GPU in TEE mode                        |
| `image_digest` matches release        | Running container hasn't been tampered with                              |
| `signing_address` matches attestation | Responses are signed by the attested machine                             |
| Signature verifies                    | Response was not tampered with in transit and signed on attested machine |
| Nonce matches your request            | Attestation is fresh, not replayed                                       |

## Privacy Guarantees

Confidential compute operates in **Zero Data Retention (ZDR) mode**:

* Your prompts and responses are **never stored**
* Only token counts are recorded for billing
* No logs of conversation content exist

## What's Next

* [Quick Start API](./quick-start) - For developers building integrations
* [Confidential Chat](./confidential-chat) - Use the web interface for private conversations
* [Verification Guide](./verification-guide) - Deep dive into verifying attestation and signatures


# Quick Start API
Source: https://io.net/docs/guides/confidential-inference/quick-start

This guide walks you through running your first verifiable AI inference with io.net's Confidential Compute.

## Prerequisites

* io.net API key ([get one here](https://cloud.io.net))
* `curl` or Python 3.7+

## Step 1: Find Models with Attestation Support

First, list available models and filter for those supporting attestation:

### curl

```bash theme={null}
curl -s https://api.intelligence.io.net/v1/models \
  -H "Authorization: Bearer $IO_API_KEY" | \
  jq '.data[] | select(.supports_attestation == true) | {name, model_id}'
```

### Python

```python theme={null}
import requests

response = requests.get(
    "https://api.intelligence.io.net/v1/models",
    headers={"Authorization": f"Bearer {IO_API_KEY}"}
)

models = response.json()["data"]
attestation_models = [m for m in models if m.get("supports_attestation")]

for model in attestation_models:
    print(f"{model['name']}: {model['model_id']}")
```

Note the `model_id` (UUID) for a model you want to use.

## Step 2: Get Attestation Report

Before running inference, request an attestation report to verify the GPU machine. Generate a unique nonce (random string) for freshness verification.

### curl

```bash theme={null}
# Generate a random nonce
NONCE=$(openssl rand -hex 16)

# Request attestation report
curl -X POST https://api.intelligence.io.net/v1/private/attestation \
  -H "Authorization: Bearer $IO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model_id": "YOUR_MODEL_UUID_HERE",
    "nonce": "'$NONCE'"
  }'
```

### Python

```python theme={null}
import secrets
import requests

# Generate a random nonce
nonce = secrets.token_hex(16)

response = requests.post(
    "https://api.intelligence.io.net/v1/private/attestation",
    headers={
        "Authorization": f"Bearer {IO_API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model_id": "YOUR_MODEL_UUID_HERE",
        "nonce": nonce
    }
)

attestation = response.json()
# Nonce is padded to 64 hex characters - verify prefix matches
print(f"Nonce verified: {attestation['nonce'].startswith(nonce)}")
print(f"Signing address: {attestation['signing_address']}")
```

### Example Response

```json theme={null}
{
  "nonce": "87ebbef3ceb69d2d6d7edc1b05c42ad900000000000000000000000000000000",
  "gpu": {
    "nonce": "87ebbef3ceb69d2d6d7edc1b05c42ad900000000000000000000000000000000",
    "arch": "HOPPER",
    "evidence_list": [
      {
        "evidence": "<base64-encoded attestation evidence>",
        "certificate": "<base64-encoded certificate chain>"
      }
    ],
    "claims_version": "3.0"
  },
  "cpu": {
    "quote": "<hex-encoded CPU attestation quote>"
  },
  "signing_address": "0xf52373547CAa0EeCB0fcD34042D7518E79aA80cC",
  "image_digest": "sha256:cf47db862b96b243e077a80ee51afa2c007604bf3c648232d42144947e56c339"
}
```

**`Save the signing_address`** - you'll use it to verify response signatures.

**`Verify the image_digest`** - compare with the expected digest published in the [latest official release](https://github.com/ionet-official/cc-attestation-agent-api/releases) to confirm the running container hasn't been tampered with.

## Step 3: Run Confidential Inference

Now run inference using the confidential completions endpoint. The request format is OpenAI-compatible.

### curl

```bash theme={null}
curl -X POST https://api.intelligence.io.net/v1/private/completions \
  -H "Authorization: Bearer $IO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "messages": [
      {"role": "user", "content": "What is confidential computing?"}
    ],
    "max_tokens": 5000
  }' \
  -i  # Include response headers
```

### Python

```python theme={null}
response = requests.post(
    "https://api.intelligence.io.net/v1/private/completions",
    headers={
        "Authorization": f"Bearer {IO_API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "meta-llama/Llama-3.3-70B-Instruct",
        "messages": [
            {"role": "user", "content": "What is confidential computing?"}
        ],
        "max_tokens": 5000
    }
)

# Get the response body
completion = response.json()
print(completion["choices"][0]["message"]["content"])

# Get signature headers for verification
signature_headers = {
    "text": response.headers.get("text"),
    "signature": response.headers.get("signature"),
    "signing_address": response.headers.get("signing_address"),
    "signing_algo": response.headers.get("signing_algo"),
    "image_digest": response.headers.get("image_digest"),
}
```

### Response Headers

The response includes signature headers for verification:

```
text: <signed content>
signature: <cryptographic signature>
signing_address: 0x1234...abcd
signing_algo: ecdsa
image_digest: sha256:...c00
```

## Step 4: Verify the Response Signature

Verify that the response came from the attested machine by checking the signature.

### Python (with eth\_account)

```python theme={null}
from eth_account.messages import encode_defunct
from eth_account import Account

def verify_response(signature_headers, expected_signing_address):
    """Verify the response signature matches the attested machine."""

    text = signature_headers["text"]
    signature = signature_headers["signature"]
    signing_address = signature_headers["signing_address"]

    # Verify signing address matches attestation
    if signing_address.lower() != expected_signing_address.lower():
        raise ValueError("Signing address does not match attestation!")

    # Verify signature
    message = encode_defunct(text=text)
    recovered_address = Account.recover_message(message, signature=signature)

    if recovered_address.lower() != signing_address.lower():
        raise ValueError("Signature verification failed!")

    return True

# Verify using the signing_address from Step 2
signing_address_from_attestation = attestation["signing_address"]
verify_response(signature_headers, signing_address_from_attestation)
print("Response verified!")
```

## Complete Example

Here's a complete Python script that performs verified confidential inference:

```python theme={null}
import secrets
import requests
from eth_account.messages import encode_defunct
from eth_account import Account

IO_API_KEY = "your-api-key"
BASE_URL = "https://api.intelligence.io.net/v1"
PRIVATE_URL = "https://api.intelligence.io.net/v1/private"

def get_attestation_models():
    """Get models that support attestation."""
    response = requests.get(
        f"{BASE_URL}/models",
        headers={"Authorization": f"Bearer {IO_API_KEY}"}
    )
    models = response.json()["data"]
    return [m for m in models if m.get("supports_attestation")]

def get_attestation(model_id: str, nonce: str):
    """Get attestation report for a model."""
    response = requests.post(
        f"{PRIVATE_URL}/attestation",
        headers={
            "Authorization": f"Bearer {IO_API_KEY}",
            "Content-Type": "application/json"
        },
        json={"model_id": model_id, "nonce": nonce}
    )
    response.raise_for_status()
    return response.json()

def confidential_completion(model: str, messages: list):
    """Run confidential inference and return response with headers."""
    response = requests.post(
        f"{PRIVATE_URL}/completions",
        headers={
            "Authorization": f"Bearer {IO_API_KEY}",
            "Content-Type": "application/json"
        },
        json={"model": model, "messages": messages}
    )
    response.raise_for_status()

    return {
        "body": response.json(),
        "signature_headers": {
            "text": response.headers.get("text"),
            "signature": response.headers.get("signature"),
            "signing_address": response.headers.get("signing_address"),
            "signing_algo": response.headers.get("signing_algo"),
			"image_digest": response.headers.get("image_digest"),
        }
    }

def verify_signature(text: str, signature: str, expected_address: str):
    """Verify response signature."""
    message = encode_defunct(text=text)
    recovered = Account.recover_message(message, signature=signature)
    return recovered.lower() == expected_address.lower()

# Main flow
if __name__ == "__main__":
    # 1. Find an attestation-enabled model
    models = get_attestation_models()
    model = models[0]
    print(f"Using model: {model['name']}")

    # 2. Get attestation with fresh nonce
    nonce = secrets.token_hex(16)
    attestation = get_attestation(model["model_id"], nonce)

    # Verify nonce freshness (nonce is padded to 64 hex chars)
    assert attestation["nonce"].startswith(nonce), "Nonce mismatch!"
    signing_address = attestation["signing_address"]
    print(f"Attestation verified, signing address: {signing_address}")

    # 3. Run confidential inference
    result = confidential_completion(
        model=model["name"],
        messages=[{"role": "user", "content": "Hello, explain TEE in one sentence."}]
    )

    # 4. Verify response signature
    headers = result["signature_headers"]
    assert headers["signing_address"].lower() == signing_address.lower(), \
        "Signing address mismatch!"

    assert verify_signature(
        headers["text"],
        headers["signature"],
        signing_address
    ), "Signature verification failed!"

    print("Response verified!")
    print(result["body"]["choices"][0]["message"]["content"])
```

## What's Next

* [Confidential Chat](./confidential-chat) - Use the web interface for private conversations
* [Verification Guide](./verification-guide) - Deep dive into verifying attestation and signatures


# Verification Guide
Source: https://io.net/docs/guides/confidential-inference/verification-guide

This guide explains how to verify that your AI inference ran on genuine trusted hardware and that responses haven't been tampered with.

## Verification Checklist

| Check                     | What It Proves                                | How to Verify                                        |
| ------------------------- | --------------------------------------------- | ---------------------------------------------------- |
| Nonce matches             | Attestation is fresh, not replayed            | Compare returned nonce with your generated nonce     |
| GPU report is valid       | Machine has genuine NVIDIA GPU in TEE mode    | Verify report against NVIDIA's root certificates     |
| CPU report is valid       | Machine's CPU is in confidential compute mode | Verify report against AMD/Intel attestation services |
| `image_digest` matches    | Running container hasn't been tampered with   | Compare with expected digest from official release   |
| `signing_address` matches | Responses come from attested machine          | Compare header with attestation report               |
| Signature verifies        | Response wasn't modified in transit           | Cryptographic signature verification                 |

## Understanding the Attestation Report

### Nonce Verification

The nonce prevents replay attacks. Always:

1. Generate a **unique, random nonce** for each attestation request
2. Verify the returned nonce **starts with** what you sent (it gets padded to 64 hex characters)
3. Never reuse nonces

```python theme={null}
import secrets

# Generate fresh nonce
nonce = secrets.token_hex(16)  # 32 character hex string

# After receiving attestation - nonce is padded with zeros to 64 chars
# e.g., "87ebbef3ceb69d2d6d7edc1b05c42ad900000000000000000000000000000000"
assert attestation["nonce"].startswith(nonce), "Nonce mismatch - possible replay attack!"
```

### GPU Attestation Report

The `gpu` field contains NVIDIA's hardware attestation:

```json theme={null}
{
  "gpu": {
    "nonce": "87ebbef3ceb69d2d6d7edc1b05c42ad900000000000000000000000000000000",
    "arch": "HOPPER",
    "evidence_list": [
      {
        "evidence": "<base64-encoded attestation evidence>",
        "certificate": "<base64-encoded certificate chain to NVIDIA root>"
      }
    ],
    "claims_version": "3.0"
  }
}
```

This proves:

* The GPU is a genuine NVIDIA device (architecture identified, e.g., "HOPPER")
* The GPU is running in Confidential Computing mode
* The GPU's firmware and configuration are in a known-good state
* Multiple GPUs may have multiple evidence entries in `evidence_list`

**Verification:**

Use NVIDIA's attestation API to verify the GPU evidence list:

* [NVIDIA Multi-GPU Attestation API](https://docs.api.nvidia.com/attestation/reference/attestmultigpu)
* Submit the `evidence_list` from the attestation response
* The API validates the certificate chain and returns verification status

### CPU Attestation Report

The `cpu` field (when present) contains CPU-level attestation:

```json theme={null}
{
  "cpu": {
    "quote": "<hex-encoded CPU attestation quote>"
  }
}
```

This proves:

* The CPU is running in a Trusted Execution Environment (AMD SEV-SNP or Intel TDX)
* The VM's memory is encrypted and isolated from the host

**Verification:**

Use the proof verifier to verify the CPU attestation quote:

* [t16z Proof Verifier](https://proof.t16z.com/)
* Submit the `cpu.quote` from the attestation response
* The verifier validates the quote against Intel TDX attestation

### Image Digest

The `image_digest` field contains the SHA256 hash of the container image running in the TEE:

```json theme={null}
{
  "image_digest": "sha256:cf47db862b96b243e077a80ee51afa2c007604bf3c648232d42144947e56c339"
}
```

This allows you to verify that the expected code is running inside the TEE.

**Verification:** Compare the `image_digest` with the expected digest published in the [latest official release](https://github.com/ionet-official/attestation-agent/releases). If the digests match, you can be confident the running container hasn't been tampered with.

### Signing Address

The `signing_address` is the Ethereum-style public address the attested machine will use to sign inference responses:

```json theme={null}
{
  "signing_address": "0xf52373547CAa0EeCB0fcD34042D7518E79aA80cC"
}
```

This key is generated inside the TEE and its binding to the attestation report proves that:

* Only the attested machine holds the private key
* Responses signed with this key came from the attested hardware

## Verifying Response Signatures

Every confidential inference response includes signature headers:

| Header            | Description                                               |
| ----------------- | --------------------------------------------------------- |
| `text`            | The content that was signed (typically the response body) |
| `signature`       | Cryptographic signature over `text`                       |
| `signing_address` | Public key that created the signature                     |
| `signing_algo`    | Signing algorithm (e.g., ecdsa)                           |
| `image_digest`    | SHA256 hash of the container image running in the TEE     |

### Verification Steps

1. **Verify signing address matches attestation**

```python theme={null}
assert response_headers["signing_address"].lower() == \
       attestation["signing_address"].lower(), \
       "Signing address mismatch!"
```

2. **Verify the cryptographic signature**

For `ecdsa` signatures (Ethereum-style):

```python theme={null}
from eth_account.messages import encode_defunct
from eth_account import Account

def verify_ecdsa_signature(text: str, signature: str, expected_address: str) -> bool:
    """Verify an Ethereum-style signature."""
    message = encode_defunct(text=text)
    recovered_address = Account.recover_message(message, signature=signature)
    return recovered_address.lower() == expected_address.lower()

# Verify
is_valid = verify_ecdsa_signature(
    text=response_headers["text"],
    signature=response_headers["signature"],
    expected_address=attestation["signing_address"]
)

if not is_valid:
    raise SecurityError("Response signature verification failed!")
```

3. **Verify content integrity**

Ensure the signed `text` matches the response you received:

```python theme={null}
import json

# For non-streaming responses, verify the signed text matches the response
response_body = response.json()
signed_text = response_headers["text"]

# The exact format of signed_text depends on implementation
# Typically it's the JSON response body or a hash of it
```

## Complete Verification Flow

```python theme={null}
import secrets
import requests
from eth_account.messages import encode_defunct
from eth_account import Account

class ConfidentialClient:
    def __init__(self, api_key: str, base_url: str = "https://api.intelligence.io.net/v1/private"):
        self.api_key = api_key
        self.base_url = base_url
        self.attestation = None
        self.nonce = None

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def attest(self, model_id: str) -> dict:
        """Get and verify attestation for a model."""
        # Generate fresh nonce
        self.nonce = secrets.token_hex(16)

        response = requests.post(
            f"{self.base_url}/attestation",
            headers=self._headers(),
            json={"model_id": model_id, "nonce": self.nonce}
        )
        response.raise_for_status()
        self.attestation = response.json()

        # Verify nonce freshness (nonce is padded to 64 hex chars)
        if not self.attestation["nonce"].startswith(self.nonce):
            raise SecurityError("Nonce mismatch - possible replay attack!")

        # TODO: Verify GPU/CPU attestation reports against root certificates
        # This requires NVIDIA/AMD attestation verification libraries

        return self.attestation

    def complete(self, model: str, messages: list, **kwargs) -> dict:
        """Run verified confidential inference."""
        if not self.attestation:
            raise ValueError("Must call attest() before complete()")

        response = requests.post(
            f"{self.base_url}/completions",
            headers=self._headers(),
            json={"model": model, "messages": messages, **kwargs}
        )
        response.raise_for_status()

        # Extract signature headers
        sig_headers = {
            "text": response.headers.get("text"),
            "signature": response.headers.get("signature"),
            "signing_address": response.headers.get("signing_address"),
            "signing_algo": response.headers.get("signing_algo")
        }

        # Verify signing address matches attestation
        if sig_headers["signing_address"].lower() != \
           self.attestation["signing_address"].lower():
            raise SecurityError("Signing address doesn't match attestation!")

        # Verify signature
        if not self._verify_signature(sig_headers):
            raise SecurityError("Response signature verification failed!")

        return response.json()

    def _verify_signature(self, headers: dict) -> bool:
        """Verify response signature."""
        if headers["signing_algo"] == "ecdsa":
            message = encode_defunct(text=headers["text"])
            recovered = Account.recover_message(
                message,
                signature=headers["signature"]
            )
            return recovered.lower() == headers["signing_address"].lower()
        else:
            raise ValueError(f"Unknown signing algorithm: {headers['signing_algo']}")

class SecurityError(Exception):
    pass

# Usage
client = ConfidentialClient(api_key="your-key")
client.attest(model_id="model-uuid-here")
response = client.complete(
    model="meta-llama/Llama-3.3-70B-Instruct",
    messages=[{"role": "user", "content": "Hello"}]
)
```

## Security Guarantees Summary

| Verification           | Threat Mitigated                                                    |
| ---------------------- | ------------------------------------------------------------------- |
| Nonce verification     | Replay attacks - attacker cannot reuse old attestation reports      |
| GPU attestation        | Fake hardware - proves response came from genuine NVIDIA GPU in TEE |
| CPU attestation        | Host compromise - proves VM memory is encrypted and isolated        |
| Image digest match     | Code tampering - proves container hasn't been modified              |
| Signing address match  | Man-in-the-middle - proves response came from attested machine      |
| Signature verification | Tampering - proves response wasn't modified in transit              |

## Troubleshooting

### Nonce Mismatch

**Symptom:** Returned nonce doesn't start with the one you sent.

**Cause:** Possible replay attack, caching issue, or request routing error.

**Note:** The returned nonce is padded with zeros to 64 hex characters. For example, if you send `87ebbef3ceb69d2d6d7edc1b05c42ad9`, you'll receive `87ebbef3ceb69d2d6d7edc1b05c42ad900000000000000000000000000000000`.

**Solution:** Use `startswith()` for comparison instead of exact match. Generate a new nonce and retry if verification fails. If persistent, contact support.

### Signature Verification Fails

**Symptom:** Cryptographic signature doesn't verify.

**Possible Causes:**

* Response was modified in transit
* Encoding mismatch in signed text
* Wrong signing algorithm used for verification

**Solution:**

1. Ensure you're using the correct signing algorithm from the header
2. Verify the `text` header encoding matches what you're verifying
3. Check for any proxy or middleware that might modify responses

### Signing Address Mismatch

**Symptom:** Response `signing_address` doesn't match attestation.

**Possible Causes:**

* Attestation expired and machine rotated keys
* Request was routed to a different machine

**Solution:** Re-request attestation before inference. Attestation should be refreshed periodically.

## What's Next

* [Quick Start API](./quick-start) - For developers building integrations
* [Confidential Chat](./confidential-chat) - Use the web interface for private conversations


# Block Rewards
Source: https://io.net/docs/guides/explorer/block-rewards-page



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
  <img alt="" />
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
  <img alt="" />
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
  <img alt="" />
</Frame>

## View Page

The **Block Rewards View Page** offers a detailed breakdown of reward calculations for individual workers and devices. Each entry includes specific performance metrics and reward status updates.

<Frame>
  <img alt="" />
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
  <img alt="" />
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
  <img alt="" />
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


# Clusters
Source: https://io.net/docs/guides/explorer/clusters-page

The Clusters tab provides a public overview of all deployed clusters within the network, along with real-time metrics on active bookings. This feature helps users assess the current status of computational resources and understand the demand for decentralized compute power.

#### Key Metrics Displayed:

* **Total Compute Hours Served** (cumulative processing time delivered by the network)

<Frame>
  <img alt="" />
</Frame>

### Daily Compute Hours

The Daily Compute Hours chart shows how many compute hours were contributed to the network each day.

* Hover on any bar to view the **exact number of compute hours** for that specific day.
* Monitor **daily trends in supply and usage** of GPU/CPU resources across the network.
* This visualization helps track fluctuations in **compute availability and demand** over time.

<Frame>
  <img alt="" />
</Frame>

### List of Clusters

The Clusters Table provides a transparent, real-time view of all deployed clusters and their associated compute bookings.

**The table includes:**

* **Cluster Status** (active, idle, or under maintenance)
* **Cluster ID** (unique identifier for each cluster)
* **Remaining Compute Hours** (available processing capacity)
* **Device Types & Quantities** (hardware resources within each cluster)

This page enables users to **monitor compute resource availability**, track network performance, and optimize cluster utilization in real time.

<Frame>
  <img alt="" />
</Frame>


# Home
Source: https://io.net/docs/guides/explorer/homepage

The Home page serves as a central hub, providing users with a comprehensive overview of our services, real-time insights into resource availability, and key metrics on network performance.

Information that can be viewed in the Home page include:

**Ready-to-Use Devices Secured with \$IO Staking:** Each device in the network is pre-configured and secured by a stake in \$IO, proportional to its computational capacity. This ensures security, reliability, and efficient resource allocation.

**Total Cluster Readiness & Fully Collateralized GPUs/CPUs:** This section displays the number of available GPUs and CPUs in the network, including both hired and idle devices. Only Cluster-Ready Devices - those that have successfully passed Proof of Work and are ready for deployment - are included.

<Frame>
  <img alt="" />
</Frame>

## Supply Insights & Geographic Distribution

The Homepage Dashboard provides real-time data on active hardware across the network, helping users assess resource availability and optimize their computational needs.

The block "**Supply Insights & Geo Distribution**" displays:

* Selected country/region
* Total number of available GPUs/CPUs and currently hired devices
* A breakdown of devices by type and availabilitye

<Frame>
  <img alt="" />
</Frame>

## Trending Devices

The Trending Devices table showcases the latest high-performance GPUs and CPUs optimized for AI model training and inference. Users can filter devices by brand, technology, and connectivity tiers to find the most suitable hardware for their needs.

The table includes:

* **Device** (Model & Specifications)
* **Quantity** (Available Units)
* **Price** (Cost per Usage)
* **Managed Service Option** (Contact button for top-tier devices))

<Frame>
  <img alt="" />
</Frame>


# Inferences
Source: https://io.net/docs/guides/explorer/inferences-page

The Inferences tab provides a public overview of all transactions conducted within the network, along with real-time metrics for these transactions.

### Key Metrics Displayed:

* **Total Inference Count** (cumulative number of inferences processed)
* **Total On-Chain Transactions** (total recorded transactions on the blockchain)
* **Today's Inference Count** (number of inferences processed within the last 24 hours)
* **Today's On-Chain Transactions** (transactions recorded on-chain today)

<Frame>
  <img alt="" />
</Frame>

### List of Inferences

The Inferences Table offers a transparent, real-time view of transactions conducted on the network.

**The table includes:**

* **Transaction Status** (successful, pending, or failed)
* **Link to View Transaction Details**
* **Date** (when the inference was processed)
* **Time** (specific timestamp of execution)
* **Computed By** (identification of the computing resource used)

<Frame>
  <img alt="" />
</Frame>

### Inference Details Page

Clicking on a transaction opens a **detailed view** with the following information:

* **Inference ID** (unique identifier for the transaction)
* **Status** (completed, pending, or failed)
* **Date** (when the inference was executed)
* **Computation Time** (duration in minutes/seconds)
* **Inference Micro Transaction URL** (on-chain transaction record)
* **Requested By App URL** (source application that initiated the request)

This page provides **full transparency** into how inferences are processed within the network, enabling users to track transaction history and ensure accuracy in AI computations.

<Frame>
  <img alt="" />
</Frame>


# Overview
Source: https://io.net/docs/guides/explorer/io-explorer

Real-time open statistics about our service operations without personal data.

<Frame>
  <img alt="EXPLORER Pn" />
</Frame>

The purpose of IO Explorer is to provide users with a comprehensive view of our network, offering detailed statistics and insights into every aspect of our GPU Cloud. Similar to Solscan or a blockchain explorer for blockchain transactions, IO Explorer offers transparency to our GPU-powered operations.

Its primary goal is to empower users to easily monitor, analyze, and understand the io.net network by providing complete visibility into activities, key statistics, data points, and Rewards transactions.

IO Explorer democratizes access to our cloud data by offering transparent real-time metrics on cluster bookings, deployments, and network devices, all while ensuring that sensitive information remains hidden and securely protected.


# Network Map
Source: https://io.net/docs/guides/explorer/network-map-page

The Network Map simplifies understanding by displaying the distribution of GPUs/CPUs across various countries along with their quantities. The proximity of Workers impacts both cost and speed, with closer Workers offering faster and more cost-effective task handling.

<Frame>
  <img alt="" />
</Frame>

You can click on any map point to access Workers in that country, where you'll find details such as:

* Device types and their quantities
* Current statuses
* Activity trends over time
* Detailed information on specific Workers

<Frame>
  <img alt="" />
</Frame>


# Staking Dashboard
Source: https://io.net/docs/guides/explorer/staking-dashboard

The Staking Dashboard is your central hub for real-time statistics and trends about staking activity on the io.net platform. Crafted for clarity and efficiency, it offers a comprehensive overview of essential staking metrics to keep you updated.

To access the Staking Dashboard, go to **io.net** > **IO Explorer** > **Staking Dashboard**.

<Frame>
  <img alt="" />
</Frame>

## Staking Tab

### Key Features

* **Net Staked Amount (TVL in \$IO):** Displays the total value locked in staking, representing active stakes in \$IO coins.
* **Net Staked Amount (TVL in USD):** Displays the total value locked in staking, representing active stakes in USD.
* **Monthly Staked Amount**: Shows the total amount staked within the current month.
* **GPU/CPU With Full Stake:** Lists devices that meet the complete staking requirements.

<img alt="Stakingtab2 Jp" />

* **Auto-refresh:** All data updates automatically every 10 minutes, but you can get the latest information instantly by clicking the **Refresh Data** button. You can also click the **See it On Chain** button to view it directly on Solscan for real-time data.

### Staking Graphs and Visualizations

The Staking Dashboard includes several key metrics and graphs to help monitor staking performance over time:

* **Net Staked Amount (\$IO)** – Represents active and currently staked funds (*Total Value Locked in \$IO*).
* **Monthly Staked Amount (\$IO)** –  Reflects the total amount staked within the current month.

<img alt="Stakingtab3 Jp" />

These visuals make it easy to monitor changes, spot trends, and gain actionable insights into staking performance.


# Overview
Source: https://io.net/docs/guides/explorer/tne-on-chain

Introducing TNE On Chain — io.net’s next-generation transaction system built on Solana blockchain.

**TNE On Chain** marks a major milestone in io.net’s evolution, introducing a fully transparent and verifiable transaction system on the Solana blockchain. This upgrade brings every booking, payment, and \$IO repurchase on-chain — making io.net one of the first AI compute networks to offer complete financial transparency and security for its users and suppliers.

By recording all financial activity on-chain, TNE introduces an immutable ledger of interactions between customers, suppliers, and io.net’s treasury. This system not only enforces accountability, but also improves automation, strengthens trust, and aligns the platform with Web3-native infrastructure.

## Why On-Chain?

Moving transactions to the Solana blockchain ensures:

* **Transparency** — Every payment, refund, or repurchase can be independently verified.
* **Security** — Funds are held in escrow using smart contracts, reducing risk.
* **Efficiency** — Automated payments and settlements minimize delays and errors.
* **Decentralization** — All financial flows are publicly auditable and blockchain-native.
* **Ecosystem Support** — A portion of every transaction goes toward repurchasing \$IO on the open market, supporting liquidity and value for token holders.

<Info>
  Total Network Earnings and Daily Network Earnings reflect estimated values based on compute provided, not actual payments or finalized settlements.
</Info>

<Note>
  Clusters initiated in **USDC** can have remaining balances settled in **IO Coin** or **USD**, enabling flexible multi-currency transactions.
</Note>

## How It Works

The **Transactions** tab gives you full visibility into the financial activity happening across the io.net network. This section of **IO** **Explorer** is designed to highlight revenue trends, individual transaction details, and the overall performance of the platform in real time..

<Frame>
  <img alt="" />
</Frame>

From this dashboard, you can view:

### Total Network Earnings

This block provides a comprehensive overview of all revenue generated across the network. It includes:

* **Total Earnings Graph:** A line graph displaying estimated cumulative revenue over time.
* **Daily Change (%):** A quick view of the day-over-day percentage change in revenue, giving users an immediate sense of growth or fluctuation.
* **Detailed Revenue Graph:** A more granular visualization that breaks down network earnings into smaller time intervals or sources for deeper analysis.

<Frame>
  <img alt="" />
</Frame>

<Note>
  All compute workloads are **denominated and recorded in IO Coin terms**, even when the initial cluster payment was made in another currency.
</Note>

### Daily Earnings Trends

This section highlights how earnings change over time, using a **Bar Chart by Day** to show daily revenue. It helps you spot trends, seasonal patterns, and the effects of key events or cluster deployments.

<Note>
  Within **TNE metadata**, all transaction values are **displayed in USDC** for clarity and consistency.
</Note>

<Frame>
  <img alt="" />
</Frame>

### Transaction List

This section provides a transparent view of all on-chain activities happening within the network. You can track key transaction types - such as bookings, payments, refunds, and \$IO repurchases — with full visibility into each action’s status, amount, and associated cluster. Each transaction includes a direct link for verification on Solana Scan.:

<Frame>
  <img alt="" />
</Frame>

<Note>
  When **no \$IO repurchase** is recorded, it indicates that the client **paid directly in IO Coin**.
</Note>

<Info>
  **Quick Steps for Users**

  * [Connect your Solana](/docs/solana)-compatible wallet (e.g., Phantom, Solflare) to seamlessly track your earnings and transactions on-chain.
  * Use the **Explorer’s** **Transactions** tab to view detailed, real-time payment and payout information.
</Info>

## What’s Next

**TNE On Chain** is just the beginning. Future updates will expand the Explorer with deeper analytics, customer leaderboards, and more detailed tracking of earnings and transaction costs — giving users better tools to understand and optimize their experience on io.net.


# Smart Contract Events
Source: https://io.net/docs/guides/explorer/tne-smart-contracts

Learn how smart contracts manage booking, payments, extensions, compute tracking, refunds, and earnings within the IO Network. This guide explains each on-chain event, from creating a cluster to final IO Coin settlement, ensuring full transparency and auditability.

When you interact with the IO Network, whether by creating, extending, or completing a compute cluster, every action is managed transparently through smart contracts. These contracts handle payments, track usage, and settle completed compute work in **IO Coin**, which powers the **Total Network Earnings (TNE)**.

<Note>
  The **Total Network Earnings (TNE)** metric represents the total compute-based activity and payments within the IO Network. It is not a distribution of financial returns.
</Note>

This section walks you through the full process, from booking a cluster to the point where the network records its earnings.

***

## **1. Creating a Cluster (Book Product)**

When you create a cluster on the IO Network, your booking is recorded on-chain. This booking defines the main details of your compute session, including hardware type (CPU or GPU), quantity, duration, and payment currency (USDC or IO Coin).

At this stage, your compute agreement with the network is established. The cluster is reserved and ready, but payment can be completed in stages if needed.

```json theme={null}
book_product(
  customer_id: <uuid>,
  cluster_id: <uuid>,
  currency: USDC | IOCOIN,
  hardware_type: 'CPU' | 'GPU',
  hardware_quantity: int,
  total_cost: u64,
  compute_minutes_hired: int,
  compute_minutes_worked: int,
  worked_amount: int,
  paid: u64
)
```

***

## **2. Paying for a Cluster (Payment)**

Once your cluster is created, you can start making payments toward it.

Each payment updates the total paid amount and the cluster status. If the total amount paid has not yet covered the full cost, the cluster is marked as **partially paid**. Once it is fully paid, the status changes to **paid**.

```json theme={null}
pay(
  transaction_id: <uuid>,
  cluster_id: <uuid>,
  amount: u64  # in cluster currency
)

paid_amount = paid_amount + amount
payment_status = if paid_amount >= total_amount then "paid" else "partially_paid"
```

***

## **3. Extending a Cluster (Extension)**

If you want to keep your cluster running for longer than originally planned, you can extend it. When you do this, both the total compute time and the total cost increase proportionally. The extension is added to your existing contract, allowing your cluster to continue operating without interruption.

```json theme={null}
extend(
  cluster_id: <uuid>,
  extended_minutes: int,
  extended_amount: u64
)

compute_minutes_hired = compute_minutes_hired + extended_minutes
total_cost = total_cost + extended_amount
```

***

## **4. Tracking Compute Work**

Once your cluster begins running, the network automatically tracks the compute time that is used.

Every 24 hours, or when the hired duration ends, whichever happens first, the smart contract records the total compute delivered. For longer jobs, the system records progress every 24 hours to make verification simple and consistent.

**Examples:**

* A 3-hour cluster is logged once after 3 hours.
* A 48-hour cluster is logged twice, once every 24 hours.

All compute work is recorded in **IO Coin**, even when you pay in another currency. This ensures that TNE calculations remain consistent in the network’s native token.

```json theme={null}
worked(
  cluster_id: <uuid>,
  compute_minutes: int,
  amount: u64  # always in IO Coin
)

compute_minutes_served = compute_minutes_served + compute_minutes
worked_amount = worked_amount + amount
```

***

## **5. Refunds (if Applicable)**

If a cluster terminates early, the protocol automatically calculates a refund for unused compute time at the original booking rate, excluding the first non-refundable hour and applicable network fees. Refunds are issued in the same currency used for payment.

```json theme={null}
refund(
  transaction_id: <uuid>,
  cluster_id: <uuid>,
  amount: u64  # in cluster currency
)

refund = refund + amount
```

***

## **6. Repurchases**

For clusters paid in USDC, the protocol automatically converts the equivalent compute value into IO Coin via on-chain logic only. No off-chain exchange, custody, or third-party conversion is involved.

```json theme={null}
repurchase(
  cluster_id: <uuid>,
  amount_in: u64,   # USDC
  amount_out: u64   # IO Coin
)
```

***

## **7. Earnings**

After your compute work is verified and any conversions are complete, the earned IO Coin is transferred from escrow to the **IO Treasury wallet**.

```json theme={null}
earn(
  transaction_id: <uuid>,
  cluster_id: <uuid>,
  amount: u64  # always in IO Coin
)

settled_amount = settled_amount + amount
send amount to treasury from escrow
```

Each completed cluster, extension, and repurchase follows this process, creating a transparent and verifiable record of the network’s total compute activity.

***

## **Putting It All Together**

Here is the full lifecycle of a cluster in the IO Network:

1. **Booking** – You reserve compute resources.
2. **Payment** – You fund your session, fully or partially.
3. **Extension** – You can add more time if needed.
4. **Compute Work** – The network tracks and records your compute activity.
5. **Refund (if applicable)** – Unused time is refunded.
6. **Repurchase** – USDC payments are converted into IO Coin.
7. **Earnings** – IO Coin from completed work is transferred to the treasury.


# Workers
Source: https://io.net/docs/guides/explorer/workers-page

The Workers tab provides a public overview of all devices connected to the network, along with real-time metrics on active hires. This allows users to gain valuable insights into the current network status and the demand for computing power.

**Key Metrics Displayed:**

* **Total GPUs** (hired and idle)
* **Total CPUs** (hired and idle)

<Frame>
  <img alt="" />
</Frame>

### Available Inventory

The Workers tab also highlights **available inventory**, which includes both active and passive GPU and CPU processors. You can click on a specific processor to view detailed statistics about its usage and performance.

<Frame>
  <img alt="" />
</Frame>

## Workers List

The Workers List provides a transparent, real-time view of all connected devices, along with their current operational status and hire activity.

**The table includes:**

* **Worker Status** (active, idle, or under maintenance)
* **Link to View Worker Details** (for in-depth metrics)
* **Hire Status** (availability for compute tasks)
* **Uptime Duration** (how long the worker has been active)
* **Device Types & Quantities** (detailed breakdown within each cluster)

<Frame>
  <img alt="" />
</Frame>

## Worker Details

Users can access a detailed view of each **Device** by selecting it from the **Workers List**. The details for each device includes full specifications, utilization metrics, and a breakdown of worker performance.

### Device Overview Includes:

At the top of the Device Overview, users can view:

* **Block Rewards Nomination Eligibility Status**
  * Default view shows only pass/fail status for each category.
  * Users can expand the section to see detailed criteria for Block Rewards Nominations.
* **Uptime Graph for the Last 30 Days**
  * Easily track whether the device has experienced downtime or remained continuously active.

<Frame>
  <img alt="" />
</Frame>

### Main Metrics Displayed:

On the right-hand side of the page, users can find key performance indicators for the selected device:

* **Uptime Percentage** (availability over time)
* **Traffic Transmitted** (data usage and throughput)
* **Connectivity Tier** (network performance classification)
* **Security Compliance** (status of security protocols)
* **Location** (geographic placement of the device)

**Running Services:**

* **IO Version Control Status** (software version management)
* **IO Monitor Status** (device health monitoring)
* **Ray.io Status** (distributed computing framework status)

This **Device Overview** enables users to efficiently track, manage, and assess decentralized compute resources in real-time.

<Frame>
  <img alt="" />
</Frame>

**Block Rewards:**

The **Block Rewards** tab provides detailed information about all of the Block Rewards associated with a specific device, this includes:

| Block              | Description                                                                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Block Reward       | To the right of Block Reward, you see the status. In this instance, it's **Completed**. If the device fails to satisfy the POW and POTL requirements, **Failed** will appear.        |
| Block ID           | A unique identifier assigned to each block within a blockchain.                                                                                                                      |
| Connectivity Tier  | The Connectivity Tier that the worker qualifies for. This is an option when a customer reserves a GPU/CPU when they deploy a cluster.                                                |
| Processor          | The processor type, GPU/CPU. In this example, it's a Nvidia L4 GPU.                                                                                                                  |
| Processor Quantity | Number of processors available for the worker.                                                                                                                                       |
| POTL               | (Proof of Timelock) - Verifies the uptime for the worker. This can be executed against a hired worker.                                                                               |
| POW                | (zkTFLOPs Proof) Tasks the worker must solve to verify the worker. To learn more about POW, see [Proof of Work](/docs/proof-of-work). This is never executed against a hired worker. |
| Device Base Score  | This score is based on hardware quantity, hardware multiplier, and the connectivity tier.                                                                                            |

See below for the base score calculation:

```
+ (0.02 x (connectivity_tier_number" / 4.0))  
  + (2.0 x "hardware_multiplier" x "processor_quantity") ) x 100 + (0.05 x "was_hired")) x 10
```

The formula above is subject to future change by the IOG foundation. For example, a significant increase for the weight of hired status in the overall base score calculation. This would incentivize practical and usable GPU device growth within the IO ecosystem.

**Device Normalized Score**- This score represents potential earnings for the device, which is based on the available coin emissions for the block and the scores of all eligible devices.

The calculation is designed to ensure that the total GPU Normalized Score is 8M, and Total CPU Normalized Score is 2M. **Device Normalised Score** is calculated as **Device Base Score** / **Total Base Score** of **Device Type** / **Normalized Score** allocation.

For example, if a GPU Device Base Score is 8150, the total GPU device score at that hour across the entire network is 115M, then the GPU Device Normalized Score is 569. (8150/115Mx8M).

**Rewarded**- The amount of IO Coin the worker earned based on **Total Score**.

<Frame>
  <img alt="" />
</Frame>


# FAQ
Source: https://io.net/docs/guides/faq

Straightforward answers to general queries.

<AccordionGroup>
  <Accordion title="Q: What is io.net's mission, and what are you working towards?">
    io.net is a decentralized GPU network designed to give unlimited computing power to ML applications. We make computing more scalable, accessible, and efficient. Our mission is to unlock fair access to computing power by assembling 1 million + GPUs from independent data centers, crypto miners, and crypto projects such as Filecoin or Render.
  </Accordion>

  <Accordion title="Q: How big is the GPU shortage? How is io.net solving it?">
    The major cloud providers currently have around 10-15 exaFLOPS of GPU compute capacity available. However, given the surging volume of AI/ML model training and inferencing workloads, the potential demand for GPU compute in the cloud could be as high as 20-25 exaFLOPS.

    This suggests the current shortage in cloud GPU capacity is likely in the range of 5-10 exaFLOPS. In the near future, cloud GPU capacity must expand 2- 3 times current levels in order to meet user demand.

    There is a long lead time to increase GPU supply which suggests that this problem won't be resolved any time soon.

    io.net is solving this by accessing underutilized GPU sources outside of the cloud such as:

    * Independent data centers: There are thousands of independent data centers in the US alone, and their average utilization rate is only 12% - 18%.
    * Crypto miners: Miners have suffered significant losses with Ethereum’s switch to Proof-of-Stake. They can repurpose GPUs in our DePin network.
    * Consumer GPUs: Consumer GPUs account for 90% of the total supply yet the majority of these resources are latent in consumer households and small cloud farms.

    When combined, it is estimated these sources can provide an additional 200 exaFLOPs of GPU capacity.
  </Accordion>

  <Accordion title="Q: How is io.net different from AWS?">
    io.net offers a fundamentally different approach to cloud computing. We leverage a distributed and decentralized model that provides increased control and flexibility for users. io.net's services don't involve complicated permission models and it's cost efficient. The combination of all these factors sets io.net in its own league of Decentralized providers.
  </Accordion>

  <Accordion title="Q: How & why is io.net cheaper and faster than other providers like AWS?">
    io.net is significantly more affordable and faster than current cloud solutions. By leveraging underutilized sources, such as independent data centers, crypto miners, and consumer GPUs, we offer compute for up to 90% less than traditional cloud providers.

    We are significantly faster than the competition because creating distributed clusters through traditional cloud providers is a time-consuming process. Companies like AWS often ask for detailed KYC information, require long-term contracts, and often have waitlists for the most desired hardware. It can often take two weeks to obtain GPU compute from cloud providers.

    io.net doesn't impose these restrictions which allows users to access GPU supply and deploy clusters in less than 90 seconds. Ultimately, the combination of speed and cost allows io.net to be 10x to 20x more efficient than traditional cloud providers.
  </Accordion>

  <Accordion title="Q: What is a DePIN and how does io.net fit?">
    DePIN, or Decentralized Physical Infrastructure Networks, leverages blockchains, IoT, and the greater Web3 ecosystem to create, operate and maintain real-world physical infrastructure. These networks use token incentives to coordinate, reward, and safeguard members of the network. io.net is the first and only GPU DePIN. We are optimized for machine learning but are also ideal for all GPU use cases.
  </Accordion>

  <Accordion title="Q: What type of GPUs does io.net offer?">
    We offer a wide range of:

    * GPUs, including NVIDIA RTX series, and AMD Ryzen series.
    * CPUs, including Intel, AMD, and the Apple M3/M4 Chip with its unparalleled neural engine.

    Please refer to (pricing page) to see the full list of supported GPUs. Contact our support team if your hardware is not listed.

    Our minimum requirements are:

    * +12 GB of RAM
    * +500 GB Free Disk Space
    * Internet Speed : Download +500 MBs and +250 Mbps Upload with /\< 30ms ping

    Test your internet from here: [https://www.speedtest.net](https://www.speedtest.net)
  </Accordion>

  <Accordion title="Q: Why is io.net needed for machine learning?">
    io.net is natively built on top of ray.io, a machine-learning framework for distributed computing. This is the same framework used by open.ai to train GPT3 over 300k CPUs and 20k GPU. You can use io.net to distribute your AI and Python applications for reinforcement learning to deep learning, to tuning, and model serving - across an extensive grid of GPUs.

    We are set to support all the frameworks that ML engineers use for workload distribution, including Anyscale, Pytorch FSDP, TensorFlow, and Predibase.
  </Accordion>

  <Accordion title="Q: Who are your target customers?">
    Anyone looking to create or operate an ML model or AI app is a potential customer. Due to the explosion of “no-code tools” like Predibase and model creation platforms like Hugging Face, this will eventually be a massive market.
  </Accordion>

  <Accordion title="Q: How do we manage availability and allocation to users across your global network of GPUs?">
    io.net connects a global network of clients to a global network of suppliers. We deploy our container on each worker machine, facilitating the io.net Virtual Network's integration and monitoring of all device availability across the network. Our algorithm intelligently groups resources, matching the selections made by the engineer and glues them into a cluster, all within 90 seconds. Our networking solution has been thoroughly tested and found reliable.
  </Accordion>

  <Accordion title="Q: What is the connectivity requirement for suppliers?">
    * We are offering clients different tiers of connectivity, from low to ultra high. While our absolute minimum connectivity requirement is 250 Mbps, we strongly encourage suppliers to support at least 1 Gbps download and upload speeds to remain attractive to demand-side customers.
    * We expect data traffic to average 5GB / hour.
  </Accordion>

  <Accordion title="Q: Can I customize cluster creation?">
    Clients can create their cluster with unmatched flexibility through a set of selections and options: cluster type by use case, sustainability (e.g., “Green GPUs” powered by 100% clean energy), geographic location, security compliance level (SOC2, HIPAA, end-to-end encryption), connectivity tier, and cluster purpose (currently Ray App, but more options available soon). Our out-of-the-box configuration requires no additional setup by our clients to deploy the cluster.
  </Accordion>

  <Accordion title="Q: Explain the pricing model? Do pricing tiers differ based on GPU model / performance?">
    Prices are automatically determined based on supply and demand; GPU specs, such as internet speed, GPU make and model, security / compliance certifications, etc., will also affect pricing. For example, enterprise-grade GPUs with SOC2 compliance and >2 Gbps cost more than consumer-grade GPUs without SOC2 compliance and slower connectivity.
  </Accordion>

  <Accordion title="Q: What's the maximum amount of GPUs allowed in a single cluster?">
    The only limitation for your cluster size is the total available supply of GPUs.
  </Accordion>

  <Accordion title="Q: How long does it take to create a cluster of GPUs?">
    It takes less than 90 seconds to create a cluster on io.net.
  </Accordion>

  <Accordion title="Q: Is it possible to adjust the number of GPUs in my cluster as my requirements change?">
    Yes it is possible to adjust the number of GPUs either with Auto Scaling or by manually adding nodes to your cluster.
  </Accordion>

  <Accordion title="Q: What is the minimum and maximum duration for GPU cluster rentals?">
    There is a one hour minimum for clusters. You can rent GPUs for as long as you need them, there is no time limit.
  </Accordion>

  <Accordion title="Q: Does the docker container launch with --privileged flag?">
    No, the Docker container does not launch with the --privileged flag.
  </Accordion>

  <Accordion title="Q: Why do we mount the Docker socket while starting the containers?">
    The platform manages the device states and usage through the orchestration of docker containers. You must mount the docker socket to manage docker containers on the worker node. This is mandatory for the platform and there are currently no plans or alternatives to remove this.
  </Accordion>

  <Accordion title="Q: Isn't mounting docker socket and --privileged flag the same?">
    While the --privileged flag gives broad system access to a container, mounting the Docker socket gives the container control over Docker on the host.
  </Accordion>

  <Accordion title="Q: Why do you use docker containers?">
    Our platform enables clustering GPU compute and provides the end user of the platform with a production ready environment for distributed training. The custom docker images contain all the required drivers and environments. All the required libraries are installed, enabling efficient utilization of GPU and CPU resources that are required for distributed training.

    For suppliers, reproducing our environment is challenging and can result in irregularities based on the worker platform (linux, windows). Docker helps to stabilize this issue. Distributed training can only function if the environment is replicated on all nodes.
  </Accordion>

  <Accordion title="Q: Do you have proof of compute / verification, what kind of proof do you use ?">
    **Current Industry Protocol**

    It's primarily accomplished with validators that randomly replicate compute jobs on the network and verify that it matches the results provided by participants. Secondly, with a rewards punishment system that ensures that participants are not providing false results since the compute is done off chain. Thirdly, through proof of learning which is an anti-cheat mechanism based on logs provided by user that detail their compute process and some other steps.

    This proof of compute isn't mature and hasn't proven itself as its efficacy remains theoretical. In proof-of-work systems, due to the sequential nature of computations, validating work at a specific point requires completing all previous work up to that point. There are many other obstacles and challenges associated with this model.

    **io.net Protocol**

    io.net leverages the existing model, taking advantage of its benefits and enhancing its strengths with our improvements. Our compute service operates on an hourly basis, allowing users to book clusters for specific periods of time. Since our service is time based rather than compute based, we simply need to prove that the GPU's compute power is completely available when it's rented.

    This is achieved with io.net's innovative concept of Proof: **Proof of Time-Lock**. This provides proof that the GPUs were not accessed by any other services or threads that would diminish compute power during the time it was rented. We can prove that from the start of the rental period (T1) until the end (T2), the GPU is 100% committed to the AI/ML jobs running on the device. This proof consists of multiple steps that benchmarks:

    * Consumption
    * Monitoring containers
    * Eliminating foreign processes
    * A punishment and rewards system to ensure that all workers are compliant

    All this is accomplished with io.net's revolutionary AI, which learns at a granular level with each cluster booking to ensure fairness and maintain a trusted environment throughout the entire process.
  </Accordion>

  <Accordion title="Q: How do you mitigate latency issues?">
    * io.net's flexible system features our algorithm that intelligently groups resources and matches their Connectivity Speed, Geolocations, and Hardware Specs to eliminate bottlenecks and reduce latency.
    * Our distribution technology on Ray and Mesh networks ensures that data travels along multiple paths which increases redundancy, fault tolerance, while improved load distribution minimizes latency.
    * When VPNs are used to increase security it often results in increased latency. In order to offer robust security with minimal latency, we employ a kernel-level VPN that uses one of the most secure mesh VPN protocols, ensuring high security without compromising network performance.
    * The majority of our GPU supply is hosted by Tier 3 - 4 data centers and advanced mining facilities. Quality infrastructure results in low latency. Our reports indicate that over 40% of our supply has internet speeds surpassing those of Lambda Labs Cloud.
  </Accordion>

  <Accordion title="Q: How do you parallelize? / How are you connecting all the GPUs together?">
    **Distribution and decentralization**: We leverage Ray with specialized libraries for data streaming, training, fine-tuning, hyperparameter tuning. When our technology is combined with Mesh VPN, it results in a streamlined process for developing and deploying large-scale AI models across a vast network of GPUs.
  </Accordion>

  <Accordion title="Q: How do you ensure data privacy and security?">
    Our **IO** agent eliminates risks by detecting and blocking unauthorized containers from running on a hired GPU. When a node is hired, data between worker nodes is encrypted within the Docker file system. Network traffic is on a mesh VPN, providing maximum security. **We also prioritize suppliers with SOC2 compliance** and continue to stress the importance of SOC2 compliance with our suppliers.
  </Accordion>
</AccordionGroup>


# Overview
Source: https://io.net/docs/guides/getting-started

Powered by Solana

<Frame>
  <img alt="" />
</Frame>

## IO Coin

To learn more about IO Coin, see the [Internet of GPUs Foundation](https://docs.iog.net/docs/what-is-io-coin) docs.

### What Is io.Net?

io.net has built an enterprise-grade decentralized computing network that allows machine learning engineers to access distributed cloud clusters at a small fraction of the cost of comparable centralized services.

We believe that compute is this generation's "digital oil," powering a never before seen technological industrial revolution. Our vision is to build IO to be the currency of compute, powering an ecosystem of products and services that enable access to compute as a resource and as an asset.

Modern machine learning models frequently leverage parallel and distributed computing. It is crucial to harness the power of multiple cores across several systems to optimize performance or scale to larger datasets and models. Training and inference processes are not just simple tasks running on a single device but often involve a coordinated network of GPUs that work in synergy.

However traditional cloud service providers have 2.5x less capacity than the estimated demand in the market from AI/ML companies, making access to distributed computing resources presents several challenges. Some of the most prominent are:

* **Limited Availability:** It can often take weeks to get access to hardware using cloud services like AWS, GCP or Azure, and popular GPU models are often unavailable.
* **Poor Choice**: Users have little choice regarding GPU hardware, location, security level, latency and other options.
* **High Costs**: Getting good GPUs is extremely expensive, and projects can easily spend hundreds of thousands of dollars monthly on training and inferencing.

io.net solves this problem by aggregating GPUs from underutilized sources such as independent data centers, crypto miners, and other hardware networks like Filecoin, Render and others. These resources are combined within a Decentralized Physical Infrastructure Network (DePIN), giving engineers access to massive amounts of on-demand computing power in a system that is accessible, customizable, cost-efficient and easy to implement.

With io.net, teams can scale their workloads across a network of GPUs with minimal adjustments. The system handles orchestration, scheduling, fault tolerance, and scaling and supports a variety of tasks such as preprocessing, distributed training, hyperparameter tuning, reinforcement learning, and model serving. It is designed to serve general-purpose computation for Python workloads, with an emphasis on serving AI/ML workloads.

## io.net offering is purpose-built for four core functions:

* **Batch Inference and Model Serving**: Performing inference on incoming batches of data can be parallelized by exporting the architecture and weights of a trained model to the shared object-store. io.net allows machine learning teams to build out inference and model-serving workflows across a distributed network of GPUs.
* **Parallel Training:** CPU/GPU memory limitations and sequential processing workflows present a massive bottleneck when training models on a single device. io.net leverages distributed computing libraries to orchestrate and batch-train jobs such that they can be parallelized across many distributed devices using data and model parallelism.
* **Parallel hyperparameter tuning**: Hyperparameter tuning experiments are inherently parallel, and io.net leverages distributed computing libraries with advanced Hyperparam tuning for checkpointing the best result, optimizing scheduling, and specifying search patterns simply.
* **Reinforcement learning**: io.net uses an open-source reinforcement learning library, which supports production-level, highly distributed RL workloads alongside a simple set of APIs.

It all started at the Solana Hackathon, Feb 2023 and the Solana Austin Hacker House.

<Frame>
  <img alt="" />
</Frame>


# Glossary
Source: https://io.net/docs/guides/glossary



### IO Ecosystem

* **IO Coin** Connecting all the Web3 money that’s flowing into the GPU to power io.net. A blockchain-based cryptocurrency and platform designed to foster a decentralized ecosystem for applications and services. Operating on its own blockchain, IO Coin employs a hybrid consensus mechanism merging Proof of Work (PoW) and Proof of Stake (PoS) to ensure security and energy efficiency. With support for decentralized applications (dApps), including features like smart contracts and token issuance, IO Coin enables diverse functionalities. It integrates privacy-enhancing features like ZeroCoin and Ring Signatures, providing anonymity. Its versatility extends to applications in peer-to-peer transactions, remittances, and decentralized finance (DeFi).
* **IO Worker** IO Worker is a component of the IO.NET ecosystem that enables users to rent out their computing devices like GPUs and CPUs to those needing computational power. By leasing their device's processing capabilities, users earn rewards for tasks like artificial intelligence computations or rendering. This setup fosters decentralized computing and resource sharing, fostering collaboration and mutual benefit among users on the IO.NET platform.
* **IO Explorer** IO Explorer is a multifunctional tool within the IO.NET ecosystem designed for users to explore and navigate various aspects of the platform. It serves as a dashboard where users can monitor compute jobs, access performance metrics, and explore available resources within the IO.NET network. Additionally, IO Explorer provides insights into others' activities, offering a comprehensive view of the platform's functionalities and user engagements.
* **IO Cloud** IO Cloud is a component of the IO.NET ecosystem that provides cloud computing services to users. It enables users to deploy and manage virtual machines, containers, and other cloud resources on-demand. IO Cloud offers scalability, flexibility, and accessibility, allowing users to harness the power of cloud computing for various applications and workloads. IO Cloud simplifies the process of managing cloud infrastructure and empowers users to focus on their core tasks without worrying about underlying infrastructure complexities.

### Basic Terms

* **Client** Customers who hire GPU/CPU compute power.
* **Binary** A binary is a file that contains executable instructions in a format that a computer can directly execute. It represents a software application in a form that the computer's processor can understand and run.
* **Worker** Are the nodes in the cluster that execute the tasks assigned by the master node. They process data, perform computations, and contribute to the overall workload of the system.
* **Solscan** Solscan is a Solana block explorer (blockchain explorer) that enables investors to view transactions, explore wallets, find important data, and better understand other key metrics of the Solana ecosystem.
* **Solana** Solana is a high-performance blockchain platform designed for decentralized applications (dApps) and cryptocurrency transactions. It aims to provide fast and scalable solutions for developers, with the ability to process thousands of transactions per second. Solana uses a unique consensus mechanism called Proof of History (PoH) combined with Proof of Stake (PoS) to achieve high throughput and low latency. The platform also offers low transaction fees and supports smart contracts, making it suitable for a wide range of applications in finance, gaming, and decentralized finance (DeFi).
* **Aptos** Aptos is a blockchain platform designed for high scalability, security, and efficiency in decentralized applications (DApps). It aims to provide fast transaction speeds and strong security through a novel consensus mechanism and advanced cryptography. Aptos supports smart contracts, enabling developers to build various DApps, and emphasizes a user-friendly experience and robust developer tools.
* **Computing** Computing refers to the process of performing calculations, such as addition, multiplication, or more complex mathematical functions. This term is closely associated with computers, which are designed to perform computations rapidly and efficiently.
* **Compute Hours** Compute hours are the measurable hours or, time that your process is loaded and executing. Compute hours are one of the two main metrics that are used to determine costs.
* **Cluster Processor** CPU/GPU unit designed to handle parallel computing workloads within a cloud-based cluster. These processors are used for tasks that can be parallelized across multiple cores or nodes within a cluster, such as data analytics, scientific simulations, machine learning training, and other high-performance computing (HPC) workloads.
* **Connectivity Tier** It's a speed or bandwidth of internet connectivity provided by an internet service provider (ISP) or telecommunications company. It represents the rate at which data can be transmitted over a network connection, typically measured in megabits per second (Mbps) or gigabits per second (Gbps).
* **Blockchain Prover** A computational entity that confirms that information is accurate without revealing its underlying data. Provers create "proofs" that can be easily verified by a verifier. Traditionally provers generates proofs via Proof of Work (PoW), and some migrated to Proof of Stake (PoS), some are now generating Zero Knowledge Proofs.
* **Containerized Workload** An application or software workload that has been packaged into a containerized format. Containers are a lightweight, portable, and self-contained unit of software that includes all the necessary dependencies, libraries, and configuration files needed to run the application.
* **DePIN** Decentralized Physical Infrastructure Networks, leverages blockchains, IoT and the greater Web3 ecosystem to create, operate and maintain real-world physical infrastructure. These networks leverage token incentives to coordinate, reward and safeguard members of the network.
* **Node** Node AI is a platform that connects you with GPU and artificial intelligence resources in a decentralized way. It uses blockchain technology to ensure security and transparency, enabling users to engage in a range of activities securely.
* **Decentralized Applications** Decentralized applications (dApps), are software programs that run on a blockchain or peer-to-peer (P2P) network of computers instead of on a single computer. Rather than operating under the control of a single authority, dApps are spread across the network to be collectively controlled by its users.
* **Script FIle** A script file is a file that contains a sequence of commands or instructions written in a scripting language. Scripting languages, such as Bash, Python, PowerShell, and JavaScript, allow you to automate tasks, execute programs, and perform various operations on a computer or within a software environment.
* **Proof-of-Work (PoW)** The Proof-of-Work (PoW) consensus algorithm was brought to fruition with the inception of Bitcoin in 2009. It serves as the mechanism for validating transactions and generating new blocks within a blockchain. This process involves specialized devices, computers, or graphics cards performing complex calculations. In PoW, the discovery or creation of a new block is achieved through solving a cryptographic puzzle, a task known as mining. Miners invest significant computational power and energy in attempting to solve these puzzles, which forms the foundation of the term 'Proof-of-Work'.
* **Job** Job refers to a specific task allocated to a GPU cluster for execution, such as machine learning training or data analysis. It involves parameters and instructions for efficient execution.
* **Random Access Memory (RAM)** RAM is a type of computer memory that allows data to be accessed and read in any order, making it faster than storage devices like hard drives. It temporarily holds data and instructions that are actively being used or processed by the CPU (Central Processing Unit). RAM is volatile memory, meaning it loses its contents when the power is turned off.
* **SXM** SXM is a high-performance connection standard that allows GPUs to be directly mounted onto a motherboard without the need for PCIe (Peripheral Component Interconnect Express) slots.
* **BIOS** The BIOS (Basic Input/Output System) is built-in software on your computer's motherboard that starts up your computer and ensures all hardware works together properly. It also lets you change basic settings through an easy-to-navigate menu.
* **UEFI** Unified Extensible Firmware Interface (**UEFI**) is modern software that starts up your computer and helps it run smoothly. It's like an upgraded version of BIOS, with a more user-friendly interface, faster startup times, and better support for large hard drives. It also provides more advanced security features to protect your system from threats.
* **WSL 2** Windows Subsystem for Linux 2 (WSL 2) is a feature in Windows that lets you run a full Linux system on your computer without needing to set up a separate machine or use complex software. It provides a seamless way to use Linux tools and applications alongside your regular Windows programs, making it easier for developers and tech enthusiasts to work with both systems at the same time.

### Device Type

* **Central Processing Unit (CPU)** CPU stands for Central Processing Unit. It is the primary component of a computer responsible for executing instructions and performing calculations required to run software programs and operating systems.
* **Graphics Processing Unit (GPU)** Graphics Processing Unit, is a special computer chip that helps make images and videos appear on your screen faster. It's like a supercharged engine for handling visual tasks, such as gaming, watching videos, and designing graphics. They accelerate the computational tasks involved in training and running machine learning models.

### Clusters

**Cluster** A group of interconnected computers or servers that work together to perform tasks or provide services. Clustering allows multiple machines to function as a single system, enabling improved performance, scalability, and reliability. Here are some key characteristics and types of clusters.

* **Ray Cluster** A cluster of machines managed by the Ray framework. Ray is an open-source framework for building and running distributed applications. It provides a simple, universal API for building distributed applications efficiently. Typically consists of multiple machines (**nodes**) connected together to form a distributed computing environment. These machines work together to execute tasks and manage resources efficiently.
* **Mega-Ray** The supply offers a cutting-edge global networking infrastructure on a diverse selection of enterprise-grade GPU models, all of which meet the highest standards of security compliance. However, this comes at a premium cost.
* **Kubernetes (AKA k8s)** Open-source platform designed to automate the deployment, scaling, and management of containerized applications. Provides a framework for automating the management of containerized workloads and services, allowing organizations to abstract away the underlying infrastructure and focus on developing and deploying their applications.

### Base Image

A base image is the core starting point for creating containers or virtual machines, containing essential components and dependencies needed to run applications or systems.

* **Ray App** Ray is an open-source distributed computing framework primarily used for scaling Python applications across clusters. Ray provides a set of libraries for building distributed applications, including machine learning training, hyperparameter tuning, reinforcement learning, and more.
* **Pytorch FSDP** PyTorch FSDP stands for PyTorch Fully Sharded Data Parallelism. It's a distributed training technique designed to efficiently train large deep learning models across multiple GPUs or even across multiple machines. FSDP achieves this by sharding (splitting) the model parameters and activations across multiple devices, allowing for parallel computation during training.
* **Ludwig** Ludwig is an open-source, declarative deep learning model building framework developed by Uber AI Labs. It aims to provide a simple and flexible way to train and test deep learning models without requiring extensive knowledge of machine learning or deep learning frameworks. Ludwig enables users to build and deploy deep learning models for a variety of tasks, including natural language processing (NLP), computer vision, time series forecasting, and more.
* **IO Native App** A specialized software development kit provided by IO.NET, based on a fork of Ray, designed to streamline model development, training, and deployment within the ecosystem. It supports the parallelization of Python functions, dynamic task execution, and effortless scalability, empowering developers to build and scale their AI applications seamlessly on the network.
* **Unreal Engine 5** Unreal Engine 5 (UE5) is a powerful and popular real-time 3D creation platform primarily used for developing video games, architectural visualizations, virtual reality (VR) experiences, and more. Machine learning algorithms for computer vision can be used to enhance augmented reality (AR) or mixed reality (MR) experiences created with Unreal Engine 5. For example, object recognition and tracking algorithms can enable more realistic interactions between virtual and real-world objects in AR applications.
* **Unity Streaming** Unity Render Streaming is a technology that brings Unity's powerful rendering capabilities to web browsers, allowing users to experience high-quality graphics directly in their browser without additional software installations.

### Cluster Type

* **General** Best for prototyping or general end-to-end (E2E) Workloads. Virtual Machine (VM) clusters are often straightforward to set up and configure, making them suitable for prototyping. Virtual machines can be quickly provisioned and customized to match specific requirements, enabling developers to experiment with different configurations and environments.
* **Train** For production-ready clusters for machine learning model training and fine-tuning, **Train** clusters with specialised machine learning orchestration tools are often preferred. This Cluster provides a scalable, reliable, and flexible infrastructure for deploying and managing containerized applications, while machine learning orchestration tools offer features tailored to the unique requirements of training and deploying machine learning models.
* **Inference** By deploying **Inference** services on the cluster with efficient resource management, auto-scaling capabilities, hardware acceleration, and robust monitoring, it's possible to build a production-ready infrastructure capable of handling low-latency inference and heavy workloads at scale.
* **Inference** Refers to the process of using a trained model to make predictions, decisions, or classifications based on new, unseen data. In other words, it's the application of a machine learning model to real-world data to derive insights or take action.
* **NV Link** NVLink is a high-speed communication interface developed by NVIDIA for connecting GPUs (Graphics Processing Units) together. It enables direct communication between GPUs, allowing them to work together more efficiently by sharing data at extremely high speeds. NVLink is designed to enhance performance in tasks that require parallel processing, such as deep learning, scientific simulations, and high-performance computing.
* **Green GPUs** Green computing is the practice of maximizing energy efficiency and minimizing environmental impact in the ways computer chips, systems and software are designed and used.

### Additional Software

* **CUDA** The NVIDIA CUDA Toolkit provides a development environment for creating high-performance, GPU-accelerated applications. With it, you can develop, optimize, and deploy your applications on GPU-accelerated embedded systems, desktop workstations, enterprise data centers, cloud-based platforms, and supercomputers. The toolkit includes GPU-accelerated libraries, debugging and optimization tools, a C/C++ compiler, and a runtime library.
* **Docker** Docker is a platform that allows developers to develop, ship, and run applications in containers. Containers are lightweight, portable, and self-sufficient units that contain everything needed to run an application, including the code, runtime, system tools, libraries, and settings. Docker provides a way to package and distribute applications along with their dependencies, making it easier to deploy and manage software across different environments.
* **Fabric Manager** It's a software tool developed by NVIDIA that manages the hardware resources and interconnects in NVIDIA GPUs, particularly those using NVLink and SXM architectures. It is essential for ensuring that the high-speed interconnects between GPUs are functioning correctly, which is crucial for applications requiring intense computational power and fast data transfer between GPUs.
* **Terminal** A terminal is a text-based interface in a computer system used for entering commands and interacting with the operating system or applications. It provides a way to navigate the file system, run programs, manage processes, and perform various tasks using command-line instructions. Terminals are commonly used in Unix-based systems like Linux and macOS, where users can access a terminal window to enter commands directly.
* **NVIDIA driver** A NVIDIA driver is a software component that allows your computer's operating system to communicate and interact with NVIDIA graphics processing units (GPUs). It acts as a bridge between the hardware and the operating system, facilitating the proper functioning and optimization of NVIDIA GPUs for tasks like graphics rendering, gaming, AI processing, and more.
* **Hiveon OS** Hiveon OS is an operating system specifically designed for cryptocurrency mining. It is optimized to maximize mining efficiency and profitability by providing features such as easy setup, remote monitoring and management, mining software integration, and performance optimization for various mining rigs.
* **Rosetta 2** Rosetta 2 is a special software for Apple computers with M1 chips that lets them run apps designed for older Intel-based Macs. It works behind the scenes to translate the app's instructions so they can work on the new hardware, allowing you to use your favorite apps even if they haven't been updated for the new chips.

### Security Compliance

* **E2E Encrypted** It’s a method of secure communication where the data is encrypted on the sender's device, remains encrypted while it's transmitted over a network, and is only decrypted on the recipient's device.
* **SOC2/HIPAA** SOC 2 and HIPAA are compliance frameworks that address different aspects of data security and privacy. SOC 2 focuses on assessing the controls implemented by service organizations to protect customer data, while HIPAA sets standards for protecting sensitive personal information.

### Monitoring Services

* **Ray.io** Ray is an open-source unified compute framework that makes it easy to scale AI and Python workloads — from reinforcement learning to deep learning to tuning, and model serving.
* **IO Version Control** IO Version Control refers to a specific version or release of components within the IO.NET platform, including IO Cloud, IO Worker, or IO SDK. Each version includes updates, bug fixes, and enhancements aimed at improving performance, security, and overall user experience.
* **IO Monitor** IO Monitor is a tool within the IO.NET ecosystem that enables users to oversee the performance, status, and metrics of their computing resources. This includes monitoring real-time data on GPU utilization, computing efficiency, and possibly financial aspects related to usage and earnings from contributing computing power to the network.

### Supplier

* **FileCoin** Is designed specifically for decentralized storage. It's a decentralized storage network that enables users to store and retrieve data in a decentralized manner. Users who have excess storage capacity can become storage providers on the Filecoin network. They can offer their storage space to store files for others. (Kind of what we do with GPUs).
* **Render Network** The Render Network is a blockchain and crypto-enabled platform where users can contribute their unused GPU power to assist in rendering motion graphics and visual effects for projects. In exchange for their contributions, users receive Render tokens (RNDR), the native utility token of the network.
* **IO Network** IO Network is a sophisticated networking backend that employs a secured mesh VPN to enable ultra-low latency communication among the IO.NET Miner nodes, also known as "workers."


# Overview
Source: https://io.net/docs/guides/id/io-id

IO ID is your central hub for managing all io.net products and services. Learn how to view your usage, credits, and clusters, compare intelligence plans, and get started with the io.net ecosystem from one unified dashboard.

<Frame>
  <img alt="ID Pn" />
</Frame>

## What is IO ID?

**IO ID** is your central hub for managing everything related to the [**io.net**](http://io.net) ecosystem.

Originally designed to help you track your earnings, expenses, and cryptocurrency withdrawals, IO ID has evolved into a complete platform dashboard where you can view, manage, and explore all your [io.net](http://io.net) products in one place.

Through IO ID, you can:

* Get a quick overview of your [io.net](http://io.net) activity and usage.
* Manage and monitor your deployed clusters.
* Compare and manage your IO Intelligence plans.
* Review your usage, billing, and credit history.
* Access and configure your personal settings and acknowledgements.

When you open **IO ID**, the **Overview tab** will be displayed by default. This section helps you understand your current setup and guides you through getting started with [io.net](http://io.net).

## **Overview Tab**

The **Overview tab** gives you a quick start into the [io.net](http://io.net) ecosystem. It provides onboarding guidance, usage summaries, and key information about your account, all in one place.

### **Getting Started Tasks**

Here, you will find a list of tasks that help you set up and begin using [io.net](http://io.net) products efficiently. Completing these tasks ensures that you can make full use of the available features.

### **IO Intelligence Plan Usage**

This section shows an overview of your current IO Intelligence plan, including how much of your plan has been used and a breakdown of usage per model. It helps you monitor your resource consumption and understand which models contribute most to your plan usage.

### **IO Credits and Usage**

You can view your total IO Credits, remaining balance, and recent transactions.\
The credit usage section includes a clear transaction table that lists your credit activities in an easy-to-read format, so you can quickly identify how your credits are being earned and spent.

## **io.cloud Tab**

The **io.cloud tab** provides a simplified view of the **IO Cloud platform**, allowing you to manage your clusters without leaving IO ID. It gives you a convenient way to check your active clusters and deploy new ones.

### **Deploy a Cluster**

You can deploy a new compute cluster by clicking the **Deploy Cluster** button. This will take you to the [**IO Cloud platform**](https://cloud.io.net/cloud/home), where you can go through all the configuration steps required to complete your deployment.

### **Cluster Management Table**

This table lists all your deployed clusters along with important details such as cluster name, cluster type, status, device type, and hours served.\
You can use filters and sorting options to easily find specific clusters or review deployment information.

## **io.intelligence Tab**

The **io.intelligence tab** allows you to view and compare all available **IO Intelligence plans** to help you find the one that best suits your needs.

### **Plan Comparison**

You can explore and compare IO Intelligence plans by reviewing their respective limits, pricing, and key features.\
For more detailed information about these plans, you can refer to the [**IO Intelligence Payments help page**](https://io.net/docs/guides/payment/io-intelligence-payments).

### **Usage Overview**

This section provides details about your plan usage, including the percentage of your quota used, when your usage will reset, and how your consumption is distributed across different models.\
It helps you monitor your plan’s performance and manage your resources effectively.

## **Usage and Billing Tab**

The **Usage and Billing tab** provides an overview of your account’s financial and resource activity. It allows you to monitor how your credits are being used, review your transaction history, and view your earnings and balances across [io.net](http://io.net) platforms. This section helps you stay informed about your usage and maintain transparency over all your activity.

For more detailed information, you can visit the [**IO ID Usage and Billing Guide**](https://io.net/docs/guides/id/usage-and-billing), which provides an in-depth explanation of every field and feature available in this tab.

## **Settings**

The **Settings** tab allows you to:

1. Change profile picture.
2. Change your account details such as your *Full Name* and *Timezone*.
3. Connect *New Wallets* for future payments.
4. Delete your account. To do so, contact [technical support](mailto:support@io.net) from your registered email account and request account deletion.

   <Warning>
     This operation is final, your account cannot be restored once it is deleted.
   </Warning>

## **User Acknowledgment**

This page contains the terms and conditions for all [io.net](http://io.net) users and is periodically updated as our services evolve. However, you can always revisit this page for the comprehensive overview of our services from a legal perspective.

## **Fees**

Certain transactions may include small fees depending on the payment method you choose.

### Fiat Payments

All payments made in fiat currency are subject to a **3% payment provider fee**.\
This applies to all fiat-based transactions, including when you purchase cloud compute or **IO Credits**.\
The fee covers payment processing and transaction facilitation by third-party providers.

### Cryptocurrency Payments

Payments made using cryptocurrencies, such as **\$IO Coin** or **USDC**, **do not incur any fees**.\
You can use these methods to complete transactions or buy IO Credits without additional charges.

<Info>
  Feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, do not hesitate to open a support ticket.
</Info>


# Managing your Wallets
Source: https://io.net/docs/guides/id/managing-your-wallets-in-io-id

All suppliers must add at least three to their IO ID account to remain eligible.

You can associate up to **10 Solana wallets** with your account. One wallet will be designated as the **Primary Wallet**, and will serve as the default for all transactions, **except Block Rewards Distribution.**

Ensure that your account meets this requirement to continue participating in the reward program.

For detailed steps on adding and managing wallets, refer to the instructions below:

## Adding a Wallet for Crypto Payments

If you plan on using crypto, you must add a wallet to your account. **Credit card users do not need to complete this step.**

### Connecting a Solana Wallet

To learn how to create your own Solana wallet, check out this [short guide](/guides/workers/solana). When you create your account, you are encouraged to add a wallet. You can skip this step and add your wallet later, in the **Settings** tab of **IO ID**.

Follow the steps below to add a wallet to your account:

1. Click on your icon in the upper right and select **Account Settings**.

   <Frame>
     <img alt="" />
   </Frame>
2. In Account Settings, find the **Solana Wallet Address** block and click the **Add Wallet** button.

   <Frame>
     <img alt="" />
   </Frame>
3. In the appearing popup, enter your new **Solana wallet address**
4. Click **Connect** to add the new address.

<Frame>
  <img alt="" />
</Frame>

5. As a result, your wallet will be successfully connected to the IO ecosystem.

### Connect a Single Aptos Wallet

To learn how to create your own Aptos wallet, check out this [short guide](/guides/workers/aptos-wallet). When you create your account, you are promoted to add a wallet. You can also skip the step and add your wallet in **Account Settings**.

1. Click on your icon in the upper right and select **Account Settings**.

   <Frame>
     <img alt="" />
   </Frame>
2. In the **Aptos Wallet** section, click **Add Wallet.**

   <Frame>
     <img alt="" />
   </Frame>
3. Enter your wallet address in the **Connect New Aptos Wallet** field and click **Connect**.

<Frame>
  <img alt="" />
</Frame>

## Adding Multiple Wallets

The **multi-wallet feature** allows you to add up to **10 Solana wallets** to your io.net account, providing flexibility in managing **rewards, payments, and assets.**

This is particularly useful if one of your wallets becomes **inaccessible, lost, or compromised**, ensuring your ability to receive your rewards. Additionally, you can distribute rewards across different wallets for better **organization and security.**

You can add up to 10 wallets to your account by following these steps:

1. Underneath your first wallet address, find and click the \*\*Add New Solana Wallet Address \*\*link.

   <Frame>
     <img alt="" />
   </Frame>
2. In the popup, enter your other **Solana wallet address**.
3. Click **Connect** to add the new additional address.

   <Frame>
     <img alt="" />
   </Frame>
4. Your new wallet will be successfully added to the IO ecosystem.

   <Frame>
     <img alt="" />
   </Frame>

## Setting your Primary Wallet

By default, your first wallet becomes the primary wallet. However, if you add more than one wallet, you can set another wallet as your primary. The primary wallet will be used for **Block Rewards** and payment transactions.

To change your primary wallet, hover your mouse over the desired wallet address and click on the blue star beneath the field. The selected wallet will then become your primary wallet.

<Frame>
  <img alt="" />
</Frame>

## Removing a Wallet

You can remove any of your wallet addresses at any time by following these steps:

1. Hover over the wallet address you want to remove.
2. A red**Trash**  icon will appear. Click on it to remove the selected wallet.

   <Frame>
     <img alt="" />
   </Frame>
3. A pop-up will then appear to double-check your action to ensure you want to remove the wallet.

   <Frame>
     <img alt="" />
   </Frame>

<Warning>
  If you remove your wallet from the IO ecosystem, you will no longer receive block rewards, payments, or any other rewards associated with that wallet. Make sure you remove wallets only when necessary.
</Warning>

<Frame>
  <img alt="" />
</Frame>


# Usage and Billing
Source: https://io.net/docs/guides/id/usage-and-billing

Review your usage, transaction history, earnings and billing details. Get full visibility into your IO Credits, block-reward earnings, withdrawals, and platform spend in one place.”

<Frame>
  <img alt="IO Credits Nav Bar" />
</Frame>

On the top navigation bar, click the **Usage & Billing** button.

This page allows you to:

* View your *Credit Usage* and your credit *Transactions*.
* *Buy* IO Credits or *Withdraw* IO Credits.
* View *Lifetime Block Reward* earnings for your workers.
* View *Block Rewards Already Claimed* for your workers.
* View *Worker Earnings* and claim your earnings.
* View your current *Cloud \$IO Balance*.

<Frame>
  <img alt="IO Credits Your Credits" />
</Frame>

<Frame>
  <img alt="IOID Usage Billing Overview Pn" />
</Frame>

#### List of Transactions

This page allows you to view a **Transactions** list. You can filter the transactions by date within any allowed period and by the transaction types such as:

* *Reloaded*
* *Earnings*
* *Refunded*
* *Withdrawals*
* *Promo Credits*

Additionally, you can filter transactions by *Platforms* within the IO system, such as:

* ***IO Worker***
* ***IO Cloud***

When you click on a specific transaction, it will open a page with its detailed information.

<Frame>
  <img alt="IOID Usage Billing Transactions List Jpe" />
</Frame>

#### Detailed Transaction View

The **Transaction Details** page shows:

* *Transaction Amount*
* *Type of Transaction*
* *Platform Used*
* *Status*
* *Date/Time*
* *Transaction ID*

<Frame>
  <img alt="IOID Usage Billing Transaction Detail Jpe" />
</Frame>


# Company Origins
Source: https://io.net/docs/guides/inception

The origins of io.net.

Prior to June 2022, io.net was exclusively devoted to the development of institutional-grade quantitative trading systems for both the United States stock market and the cryptocurrency market. Our primary challenge was constructing the infrastructure necessary to accommodate our complex needs, which included a robust backend trading system with significant computational power.

Our trading strategies, bordering on high-frequency trading (HFT), necessitated real-time monitoring of the tick data of over 1,000 stocks and 150 cryptocurrencies. HFT is a method of trading that uses powerful computer programs to transact a large number of orders in fractions of a second. It uses complex algorithms to analyze multiple markets and execute orders based on market conditions. Furthermore, our system had to dynamically backtest and adjust algorithm parameters for each asset in real-time, while also being optimized to facilitate trading for more than 30,000 individual clients across ETrade.com, Alpaca.markets, and Binance.com, maintaining a latency below 200 milliseconds from market events to system reaction on client account for order execution.

Achieving such an infrastructure would typically require a dedicated team of MLOps and DevOps professionals. However, our discovery of Ray.io, an open-source library used by OpenAI to distribute GPT-3/4 training across over 300,000 CPUs and GPUs ( source ) revolutionized our approach and streamlined our infrastructure management. and increased our speed to build this backend from +6 months to less than 60 days .

After integrating Ray into our backend and preparing to deploy the application on a cluster of GPU & CPU workers to handle our substantial compute power, we faced the wall of price for running such system due to overpriced GPU on-demand cloud providers.

For instance, an NVIDIA A100 card was priced at over \$80 USD/day per card. We needed more than 50 of these cards to run on average 25 days/month, amounting to \$80 x 50 card x 25 day = 100K USD/month.

This posed a serious challenge for us as also for other self-funded startups in the AI/ML industry.

Even with such high prices, compute requirements for AI apps have been doubling every 3 months, 10x every 18 months

<Frame>
  <img alt="" />
</Frame>

<Frame>
  <img alt="Ark Invest Big ideas 2022 Page 22" />
</Frame>

Distributed applications have been around for over five decades, starting with the emergence of computer networks like ARPANET. Over the years, developers have utilized distributed systems to scale applications and services, including large-scale simulations, web serving, and big data processing.

Nonetheless, distributed applications have generally been the exception rather than the rule. Even today, most undergraduate students complete only a handful of projects involving distributed applications, if any. This landscape is quickly changing as distributed applications are on track to become the norm. Two primary trends drive this transformation: the end of Moore's Law and the skyrocketing computational demands of new machine learning applications. Consequently, a rapidly widening gap between application demands and single-node performance is leaving us no choice but to distribute these applications.

### Moore's Law is Dead

For the past 40 years, Moore's Law has driven the unprecedented growth of the computer industry. According to this law, processor performance doubles every 18 months. However, performance growth has slowed to a meagre 10-20% over the same period. Although Moore's Law may have ended, the demand for increased computing power has increased. In response, computer architects have shifted their focus to developing domain-specific processors that prioritize performance over generality.

### Domain-Specific Hardware is Not Enough

As the name suggests, domain-specific processors are optimized for specific workloads, sacrificing generality for performance. Deep learning is a prime example of such a workload, revolutionizing various application domains, including financial services, industrial control, medical diagnosis, manufacturing, system optimization, etc.

Companies have raced to create specialized processors, like Nvidia's GPUs and Google's TPUs, to support deep learning workloads. While accelerators such as GPUs and TPUs increase computational power, they only extend Moore's Law further into the future, rather than fundamentally increasing the rate of improvement.

The Triple Whammy of Deep Learning Application Demand: Machine learning applications' demands are growing at an astonishing pace. Here are three key workloads as examples:

### Training

According to a renowned OpenAI blog post, the computation required to achieve state-of-the-art machine learning results has roughly doubled every 3.4 months since 2012. This equates to an increase of almost 40x every 18 months, which is 20x more than Moore's Law! Thus, even without the end of Moore's Law, it would fall significantly short of meeting the demands of these applications.

This explosive growth isn't exclusive to niche machine-learning applications like AlphaGo. Similar trends are evident in mainstream applications like computer vision and natural language processing. For example, comparing the computational resources required by the seq2seq model from 2014 to a pretraining approach on tens of billions of sentence pairs from 2019 reveals a ratio of over 5,000x. This corresponds to an annual increase of 5.5x. These figures overshadow Moore's Law, which suggests an increase of only 1.6x per year.

### Tuning

The situation is further exacerbated by the fact that models are not trained just once. The quality of a model often depends on various hyperparameters, such as the number of layers, hidden units, and batch size. To find the best model, developers must search through different hyperparameter settings. This process, called hyperparameter tuning, can be resource-intensive.

For instance, RoBERTa, a robust technique for pretraining NLP models, uses at least 17 hyperparameters. Assuming a minimal two values per hyperparameter, the search space consists of over 130K configurations. Even partially exploring this space requires vast computational resources. Another example of a hyperparameter tuning task is neural architecture search, which automates the design of artificial neural networks by testing different architectures and selecting the best-performing one. Researchers report that designing even a simple neural network can take hundreds of thousands of GPU computing days. Simulations

While deep neural network models can typically leverage advances in specialized hardware, not all ML algorithms can. In particular, reinforcement learning algorithms involve numerous simulations. Due to their complex logic, these simulations are best executed on general-purpose CPUs (with GPUs only used for rendering), meaning they don't benefit from recent advances in hardware accelerators. For example, in a recent blog post, OpenAI reported using 128,000 CPU cores and just 256 GPUs (i.e., 500x more CPUs than GPUs) to train a model capable of defeating amateurs at Dota 2.

While Dota 2 is just a game, we're witnessing a surge in the use of simulations for decision-making applications, with startups like Pathmind, Prowler, and Hash.ai emerging in this area. As simulators strive for increasingly accurate environmental modelling, their complexity rises, adding another multiplicative factor to the computational complexity of reinforcement learning.

### Why we need distributed computing for AI

Big data and AI are rapidly transforming our world. While technological revolutions bring risks, we see immense potential for this revolution to enhance our lives in ways we couldn't have imagined just a decade ago. However, to realize this promise, we must overcome the massive challenges posed by the rapidly growing gap between application demands and our hardware capabilities. To bridge this gap, distributing applications appears to be the only viable solution. This necessitates new software tools, frameworks, and curricula to train and enable developers to build such applications, marking the beginning of a thrilling new era in computing.

At io.net, we develop innovative tools and distributed systems like Ray to guide application developers into this new era.

## References:

* \[1] Avg market price: [https://www.paperspace.com/pricing](https://www.paperspace.com/pricing)
* \[2] [https://arxiv.org/pdf/2202.05924.pdf](https://arxiv.org/pdf/2202.05924.pdf)
* \[3] [https://businessolution.org/gpt-3-statistics/](https://businessolution.org/gpt-3-statistics/)
* \[4] [https://research.ark-invest.com/hubfs/1\_Download\_Files\_ARK-Invest/White\_Papers/ARK\_BigIdeas2022.pdf?hsCtaTracking=217bbc93-a71a-4c2b-9959-0842b6fe301c%7C2653a4d0-af35-42f0-853a-c5f90f002abb](https://research.ark-invest.com/hubfs/1_Download_Files_ARK-Invest/White_Papers/ARK_BigIdeas2022.pdf?hsCtaTracking=217bbc93-a71a-4c2b-9959-0842b6fe301c%7C2653a4d0-af35-42f0-853a-c5f90f002abb)


# Agentic Workflow Editor
Source: https://io.net/docs/guides/intelligence/agentic-workflow

Build, connect, and execute powerful AI workflows using a visual, no-code interface. From simple task chains to full-blown multi-agent orchestration - without writing a single line of code.

## What is Agentic Workflow?

**Agentic Workflow Editor** is a visual builder that lets you create and manage AI workflows composed of models, agents, tools, and task logic — like a modular intelligence engine.

Instead of scripting interactions between various models or APIs, you can drag components onto a canvas, configure them, connect them visually, and run the flow to see the outcome — all from your browser.

### Who is this for?

* **AI Engineers & Researchers** – Quickly prototype multi-agent systems
* **Data Scientists & Analysts** – Automate complex logic chains without coding
* **Product / Ops Teams** – Connect AI models to business logic visually
* **Consultants & Agencies** – Package workflows as reusable templates

## Getting Started

To begin using the Agentic Workflow Editor :

1. **Go to your io.net Dashboard.**
2. Navigate to the [**Agentic Workflow Editor**](https://id.io.net/ai/agentic-workflow-editor) under **IO Intelligence** section.

<Frame>
  <img alt="" />
</Frame>

3. Create a new workflow and start interacting with AI models.

### Interface Overview

| Section           | Description                                             |
| ----------------- | ------------------------------------------------------- |
| **Left Sidebar**  | Workflows list: folders, create new flow, rename/delete |
| **Center Editor** | Visual flow builder: drag & drop components             |
| **Right Sidebar** | Settings for selected components                        |
| **Bottom Panel**  | Flow Outcome result: logs and execution steps           |

## Import your flow before starting:

* Click **Import From YAML** button when you just created new flow in the center of the flow editor

  <Frame>
    <img alt="" />
  </Frame>
* Upload `.yaml` file (max 1MB)
* Click **Generate Flow**

  <Frame>
    <img alt="" />
  </Frame>

## How the flow working

To design an effective agentic workflow, we recommend the following order:

### 1. Create an Agent

Start by adding an Agent component to represent your core logic and behavior. In the right sidebar, configure: `Agent Name`, `Instructions` (what it should do), `Swarm Name `(for group coordination if applicable)

<Frame>
  <img alt="" />
</Frame>

<Warning>
  First, insert an Agent component. Then connect it to a Model, followed by Tasks or Tools.
</Warning>

### 2. Pick an AI Model

Attach an AI Model to the Agent by clicking into the component and choosing from the available models in the right sidebar. This defines the core reasoning engine your agent will use.

1. Click **Add Component** → Select **AI Model**
2. Select the Component block → use right sidebar to:

   * Search and select an AI model
   * Click **Save**

   <Frame>
     <img alt="" />
   </Frame>
3. The block updates with the model name

### 3. Define Tasks

Add Task components for specific steps your Agent will perform. Configure each task with: `Task ID`, `Name`, `Text`, `Client Mode (on/off)`

<Frame>
  <img alt="" />
</Frame>

### 4. Connect Tools

Use Tool components to integrate external capabilities — such as RAG search, cryptocurrency data, or web search. Tools allow **Agents** or **Tasks** to interact with these systems.

To use a Tool:

* Add the **Tool** component to your flow.
* Select one from the built-in list — no manual configuration is required.

| Tool Name                    | Description                                                             |
| ---------------------------- | ----------------------------------------------------------------------- |
| `r2r.list documents`         | Lists documents with pagination.                                        |
| `r2r.rag search`             | Performs a Retrieval-Augmented Generation (RAG) search.                 |
| `listing coins`              | Retrieves a paginated list of active cryptocurrencies.                  |
| `get coin info`              | Returns coin metadata like logo, description, links, and documentation. |
| `get coin quotes`            | Provides real-time price quotes for cryptocurrencies.                   |
| `get coin quotes historical` | Returns historical price quotes.                                        |
| `search the web`             | Performs a web search. Requires `text` input.                           |
| `search the web async`       | Performs a web search asynchronously. Requires `text` input.            |

<Info>
  Note: When connecting components, remember — arrow always points from Agent or Task → Tool. Tools never initiate.
</Info>

<Frame>
  <img alt="" />
</Frame>

### 5. Add Stages (Optional)

Add Stage components to organize your workflow into sequential or parallel stages, each with defined objectives and context. Configure each Stage with: `Type`, `Objective`, `Result Type`, `Context`

<Frame>
  <img alt="" />
</Frame>

### 6. Connect Everything

In the Agentic Workflow Editor, components are connected to define how data and logic flow between them.

* **Agents** and **Tasks** are active components — they **initiate** actions.
* **Tools** and **Models** are passive — they are **called** by Agents or Tasks.

#### Valid Connection Examples:

* Agent → Tool
* Agent → Model
* Task → Tool

#### Invalid:

* Tool → Agent
* Tool → Task

<Info>
  Tools don’t initiate logic — they return results when triggered by another component.
</Info>

**To create a connection:** Drag from the top-right circle of one block to another. This sets execution order and data flow

<Frame>
  <img alt="" />
</Frame>

**To remove a connection**: Hover over the connecting line, then click the cross icon to remove it.

<Frame>
  <img alt="" />
</Frame>

### 7. Run and Review

Hit Run to execute your flow and see step-by-step output in the Flow Outcome panel.

* **Successful** real-time execution steps in **Flow Outcome**

  <Frame>
    <img alt="" />
  </Frame>
* **Errors** (e.g., logic issues or invalid config) will be displayed clearly

  <Frame>
    <img alt="" />
  </Frame>

### 8. Reposition or Delete

* Drag components freely to organize your flow
* **To delete a component:** Select the block in the editor, then click the **trash icon** in the right sidebar

  <Frame>
    <img alt="" />
  </Frame>

## Saving, Exporting

* Your work is **autosaved**, no need to click Save (see timestamp near Run).
* Click **⋮** three dots (top-right) to :

  * **Download as .yaml** your Flow
  * **Delete flow** from your account

  <Frame>
    <img alt="" />
  </Frame>

## Left Sidebar: Workflows

The left sidebar helps you organize and manage your workflows efficiently. Here's how it works:

* **Search Bar** Quickly find any existing workflow by typing its name.
* **Add New Flow** Use the “+ Flow” button to start a new workflow inside the selected folder.
* **Flow List** Displays all your existing workflows, grouped by folders. Each flow entry shows the number of components inside it, e.g. (2).
* **Flow Actions** (Hover Options) When you hover over a flow in the list, additional options appear:

  * **Edit** – Open the flow in the editor.
  * **Rename** – Update the flow name.
  * **Delete** – Permanently remove the flow (confirmation required).

  <Frame>
    <img alt="" />
  </Frame>

You can also collapse the left sidebar to maximize the workspace. Click the collapse arrow icon to hide or show the sidebar.

## Canvas Tools

* Zoom In / Out using **+ / -** buttons
* Use **Lock icon** to freeze layout
* Use **Fit to View** to focus on working area
* Collapse **Left / Bottom Panels** for full-screen editing

<Frame>
  <img alt="" />
</Frame>

## What Happens Under the Hood?

Each flow is executed as an agentic graph:

* Components are orchestrated via context-passing protocol
* Execution supports branching, parallelism, and tool chaining
* Flow outcome shows step-by-step logs, results, and failures

<Info>
  Note: execution is managed by IO’s internal orchestration engine, ensuring retry logic, state management, and observability.
</Info>

## Tips

* Start with an Agent → Connect an AI Model → Add Tasks and Tools
* Keep blocks modular and reusable
* Use Flow Outcome to debug before scaling
* YAML export lets you version-control or share flows

## Shortcuts & Extras

| Action          | How                                                        |
| --------------- | ---------------------------------------------------------- |
| Upload Flow     | Click **Import From YAML**, select `.yaml`, click Generate |
| Delete Flow     | Click `⋮`, choose **Delete Flow** (confirmation popup)     |
| Export Flow     | Click `⋮`, choose **Download YAML**                        |
| Collapse Panels | Click arrows on **Left** or **Bottom** bars                |
| Fit View        | Use **Zoom to Fit** icon                                   |


# API Keys and Secrets
Source: https://io.net/docs/guides/intelligence/api-keys-and-secrets

Learn how to create and manage API keys and secrets for use across io.net Intelligence, including models, agents, and integrations.

The *API Keys and Secrets* tab within IO Intelligence provides a unified interface for managing both API keys and authentication secrets used across the platform. These credentials enable secure access to IO Intelligence APIs, whether interacting with models, agent endpoints, or third-party service integrations.

<Frame>
  <img alt="IO Intel API Key Secrets Nav Bar" />
</Frame>

## Overview

IO Intelligence APIs provide programmatic access to powerful AI models and agents. Before making API requests, credentials must be configured correctly to authenticate calls. This section explains how to create, manage, and use both **API Keys** and **Secrets** in IO Intelligence.

## API Keys

### What are API Keys?

API keys are authentication credentials that allow applications to securely interact with IO Intelligence APIs. They are required when accessing model inference endpoints, agent workflows, or other programmatic services.

### Creating API Keys

Use the following steps to create a new API key within the *API Keys and Secrets* tab.

<Note>
  The API key will only be displayed once. Store it securely, as it cannot be shown again.
</Note>

<Steps>
  <Step title="Navigate to the API Keys and Secrets tab" />

  <Step title="Click Create New API Key" />

  <Step title="Fill in the New API Key Form" />

  <Step title="Confirm and Save" />
</Steps>

### Managing API Keys

In the API Keys and Secrets tab, you can manage your API keys to control access to IO Intelligence APIs and maintain secure usage over time.

* **Search:** Use the search bar to quickly locate existing API keys by name, which is especially useful when managing multiple keys.
* **Edit:** Update an API key’s name or permissions to reflect changes in how the key is used, such as limiting access or aligning it with a specific workflow.
* **Revoke:** Revoke API keys that are no longer needed to immediately disable further use and reduce security risk.
* **Expiration:** Configure or review expiration settings so API keys are automatically invalidated after a defined period.

## Secrets

### What are Secrets?

Secrets are credentials or tokens required by certain agents or integrations, especially when interacting with third-party services, for example, GitHub, Jira, Linear, or other external APIs. These secrets enable authenticated access on your behalf and must be configured securely.

### Creating Secrets

There are two ways to create a new secret, through the API Keys and Secrets tab or from within an Agent's configuration.

<Tabs>
  <Tab title="API Keys and Secrets Tab">
    To create a ***Secret*** from the API Keys and Secrets Tab, follow these steps:

    <Steps>
      <Step title="Open the API Keys and Secrets tab" />

      <Step title="Click the Add Secret button" />

      <Step title="Enter your Secret Details">
        <Tip>
          For agent-specific instructions on obtaining required secrets, open the *Secrets Management* tab in the *Agent Details* view and follow the steps outlined for that agent.
        </Tip>
      </Step>

      <Step title="Save your Secret">
        Secrets created here are stored securely and will be available for use across agents.
      </Step>
    </Steps>
  </Tab>

  <Tab title="Agent Details View">
    If you want to configure your secret while viewing an agent, it can be created or selected directly from the *Agent Details* view by completing the steps below:

    <Steps>
      <Step title="Navigate to the Secrets Management tab" />

      <Step title="Select an Existing Secret or Select 'Add New Secret'">
        Select a secret that has already been configured in the API Keys and Secrets tab, or choose **Add New Secret**. When adding a new secret, provide a *Secret Name* and *Secret Value* in the fields provided.
      </Step>

      <Step title="Click Save">
        Secrets created here are automatically stored and will also be available in the *API Keys and Secrets* tab.
      </Step>
    </Steps>
  </Tab>
</Tabs>

### Managing Secrets

The *API Keys and Secrets* tab provides a centralized view of all secrets created within [io.net](http://io.net) Intelligence. From here, existing secrets can be reviewed and deleted when they are no longer in use. Deleting a secret immediately removes it and prevents it from being used by any agent or integration.

## Using API Keys and Secrets

API keys must be included in the **Authorization** header of all requests to IO Intelligence APIs.

For example:

```shellscript theme={null}
curl -X GET “https://api.intelligence.io.solutions/api/v1/models” \
  -H “Authorization: Bearer $IOINTELLIGENCE_API_KEY”
```

<Note>
  Replace `$IOINTELLIGENCE_API_KEY` with your actual API key.
</Note>

For agents requiring third-party integrations, secrets must be configured before those features can be used or tested. Once a secret is set, the agent will use it to authenticate with the external service.

## FAQs

<AccordionGroup>
  <Accordion title="How do I secure my API Key?" icon="comment-question">
    Some best practices and tips:

    * Do not share your API key publicly.
    * Use environment variables to store API keys securely.
    * Rotate your API keys periodically.
  </Accordion>

  <Accordion title="What is the difference between an API key and a secret?" icon="comment-question">
    API keys authenticate requests to io.net Intelligence APIs, while secrets authenticate access to third-party services or integrations required by certain agents.
  </Accordion>

  <Accordion title="What do I do if a secret is compromised?" icon="comment-question">
    Revoke or rotate the secret immediately from the *API Keys and Secrets* tab.
  </Accordion>

  <Accordion title="What are the rate limits for the APIs?" icon="comment-question">
    The IO Intelligence API offers different **quotas**, depending on your [io.net](http://io.net) Intelligence Payment Plan. Refer to  [IO Intelligence Payment](/guides/payment/io-intelligence-payments)  for more information.
  </Accordion>
</AccordionGroup>


# Exploring AI Agents
Source: https://io.net/docs/guides/intelligence/exploring-ai-agents

Learn about AI Agents on io.net and how to use, configure, and deploy them to build autonomous AI systems.

Agents on [io.net](http://io.net) are packaged, executable components that encapsulate task logic, tool interactions, and external integrations. This section documents the agents provided by [io.net](http://io.net), including core agents and agents that integrate with third-party services such as *GitHub*, *Linear*, and other external tools. It describes how to deploy agents programmatically or via `curl`, configure runtime parameters, and manage secrets required for authenticated access to external APIs. These capabilities support repeatable, secure operation of AI agents within automated workflows.

## Getting Started

<Steps>
  <Step title="Navigate to the Agents tab">
    Open [io.net Intelligence](https://ai.io.net/) and navigate to the Agents tab in the navigation bar.

    <Frame>
      <img alt="Agents Tab in the Navigation Bar" />
    </Frame>
  </Step>

  <Step title="Select an Agent">
    Browse the list of available agents, or use the search bar to quickly locate a specific agent, then click on your chosen agent to view its details.

    <Frame>
      <img alt="Agents Selection and Search Bar" />
    </Frame>
  </Step>
</Steps>

## **Deploying and Configuring Agents**

When an agent is selected, the *Agent Details* view provides everything needed to evaluate, install, and configure your chosen agent.

### Agent Details and Installation

The *Agent Details* view displays information about your selected agent, along with installation options. Agents can be installed using either Python (via `pip`) or `cURL`, depending on your preferred workflow.

If you do not already have an existing API key, the *Agent Details* view provides an option to generate and inject a new API key directly into the provided `pip` or `curl` installation commands, allowing installation to proceed without leaving the page.

<Frame>
  <img alt="IO Intel Agents Inject API Key" />
</Frame>

### Trying an Agent before Installation

Before installing, an agent can be tested directly from the interface. Click the **Try Agent** button and it opens the *Playground* where you can be provide input for the agent.

After clicking the **Run Agent** button, the **Result** tab displays the agent’s output, making it possible to quickly validate behavior and responses before deployment.

<Frame>
  <img alt="IO Intel Agents Playground" />
</Frame>

### Configuring Secrets

Agents that integrate with third-party applications require secrets for authenticated access, for example, GitHub, Linear, Jira and many more.

To configure secrets, navigate to the **Secret Management** tab within the *Agent Details* view.

<Frame>
  <img alt="IO Intel Agents Secret Management" />
</Frame>

On this tab:

* Clicking the **Manage Secrets** button redirects you to the *API Keys and Secrets* page.
* On the *API Keys and Secrets* page, a new secret can be added here by clicking **Add Secret** and providing the following details:
  * *Secret Name*
  * *Secret Value*
  * *Associated Agent*

Alternatively, secrets can be created or selected directly within the **Secret Management** section of the *Agent Details* view:

* An existing secret can be selected from the list.
* A new secret can be created by entering a secret name and value.
* Secrets created here are automatically saved and will also appear in the *API Keys and Secrets* page.

Once the required secrets are configured, the agent is fully set up and ready to be interacted with.


# Exploring AI Models
Source: https://io.net/docs/guides/intelligence/exploring-ai-models

The AI Models section provides access to a wide range of pre-trained and custom models. These models combine instructions, additional knowledge, and specialized skills for various tasks.

To get started, navigate to the [Models](https://id.io.net/ai/models) tab.

<Frame>
  <img alt="Models Nav Bar Pn" />
</Frame>

### What you can do on the Models Dashboard:

* Browse the list of models with their context lenghts and prices.

### Popular AI Models

| Model Name                                                                                                                    | Developer   | Description                                                                                                                                                                                                                                                                                                              |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [deepseek-ai/DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528)                                           | Deepseek    | Enhanced model with improved reasoning, inference, and algorithmic post-training optimizations; designed for high-accuracy tasks.                                                                                                                                                                                        |
| [meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8) | Meta AI     | Multimodal instruction-tuned model leveraging a mixture-of-experts (MoE) architecture for top-tier performance in both text and image understanding.                                                                                                                                                                     |
| [gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b)                                                                    | Open AI     | Open-weight 117B parameter Mixture-of-Experts model supporting 128k context, advanced reasoning via chain-of-thought, optimized for real-world tool use, coding, and efficient local or cloud deployment.                                                                                                                |
| [Intel/Qwen3-Coder-480B-A35B-Instruct-int4-mixed-ar](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct)              | Qwen        | High-capacity, instruction-tuned code generation model optimized with INT4 mixed-precision for fast inference, designed for complex programming tasks on Intel hardware.                                                                                                                                                 |
| [Qwen3-Next-80B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)                                        | Qwen        | High-capacity model optimized for instruction following and knowledge-intensive tasks.                                                                                                                                                                                                                                   |
| [gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b)                                                                      | Open AI     | Open-source GPT-style model suitable for text generation and general-purpose tasks.                                                                                                                                                                                                                                      |
| [Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507)                                    | Qwen        | Powerful 235B-parameter language model optimized for deep reasoning, planning, and complex multi-step tasks.                                                                                                                                                                                                             |
| [Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)                                     | Mistral AI  | Instruction-tuned model focusing on efficient reasoning and NLP tasks.                                                                                                                                                                                                                                                   |
| [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/unsloth/Llama-3.3-70B-Instruct)                                    | Meta AI     | Large-scale transformer model fine-tuned for instruction-following, aligning responses with human preferences.                                                                                                                                                                                                           |
| [mistralai/Mistral-Large-Instruct-2411](https://huggingface.co/mistralai/Mistral-Large-Instruct-2411)                         | Mistral AI  | Large instruction-tuned model offering strong general-purpose reasoning, summarization, and assistant-style responses.                                                                                                                                                                                                   |
| [Qwen/Qwen2.5-VL-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct)                                           | Qwen        | Powerful vision-language model trained to follow multimodal instructions, suitable for image understanding, captioning, and reasoning.                                                                                                                                                                                   |
| [meta-llama/Llama-3.2-90B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct)                   | Meta AI     | Vision-language model with instruction tuning, capable of image analysis, visual Q\&A, and multimodal dialogue generation.                                                                                                                                                                                               |
| [BAAI/bge-multilingual-gemma2](https://huggingface.co/BAAI/bge-multilingual-gemma2)                                           | BAAI        | Multilingual embedding model optimized for semantic search and retrieval tasks across diverse languages.                                                                                                                                                                                                                 |
| [**zai-org/GLM-4.6**](https://huggingface.co/zai-org/GLM-4.6)                                                                 | Z.AI        | Advanced large-language model that expands context capacity to 200K tokens and significantly enhances coding, reasoning, and agentic capabilities. It excels in real-world coding tools, delivering more natural, human-aligned outputs.                                                                                 |
| [zai-org/GLM-4.7](https://huggingface.co/zai-org/GLM-4.7)                                                                     | Z.AI        | Advanced large-language model that retains a 200K-token context window and elevates coding, reasoning, and agentic capabilities with enhanced multi-step execution and consistency. It introduces sophisticated thinking modes like *Preserved Thinking* and *Turn-level Thinking*.                                      |
| [**moonshotai/Kimi-K2-Instruct-0905**](https://huggingface.co/moonshotai/Kimi-K2-Instruct-0905)                               | Moonshot AI | A state-of-the-art mixture-of-experts (MoE) language model, featuring 32 billion activated parameters and a total of 1 trillion parameters. It delivers exceptional reasoning, coding, and content-generation performance.                                                                                               |
| [moonshotai/Kimi-K2-Thinking](https://huggingface.co/moonshotai/Kimi-K2-Thinking)                                             | Moonshot AI | A high-performance open-source thinking model built for step-by-step thinking and dynamic tool use. It achieves state-of-the-art results on benchmarks such as Humanity’s Last Exam (HLE) and BrowseComp by dramatically scaling multi-step reasoning depth maintaining stable tool-use across 200–300 sequential calls. |
| [deepseek-ai/DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2)                                                 | Deepseek    | A LLM model that combines breakthrough efficiency with exceptional reasoning and tool-use performance. Powered by Sparse Attention and scalable RL post-training, it delivers premium long-context quality at reduced cost. Reports place it in the GPT-5 class with gold-medal wins in the 2025 IMO and IOI.            |

For a full list of models, visit the [AI Models section](https://id.io.net/ai/models) in your dashboard.

## Testing an AI Model

Before using any of our AI models in your project, you can perform real-time testing directly from the dashboard. This allows you to evaluate the model’s performance and ensure it meets your requirements.

### How to Test an AI Model

1. **Select a Model:**
   * Navigate to the **Models** tab.
   * Select the model you want to test by clicking on it.
2. **Start Testing:**
   * On the AI model chat page, type your question or input into the centered text field.
   * Press your **Enter** key or the **arrow icon** to submit your query.

     <Frame>
       <img alt="Models Model Chat Pn" />
     </Frame>

     <Note>
       Your **Daily Credits usage** is shown above the request field. To view detailed model-specific usage information, visit the [**IO Intelligence Payments**](/guides/payment/io-intelligence-payments) page.
     </Note>
3. **Interact with the Model:**
   * The AI model will respond, starting a conversation. You can continue testing by asking additional questions or providing more input.
   * Compare different models to find the one that best suits your needs.

### Managing Chats

* **View Previous Chats:**
  * On the left, you can manage your previously created chats with different AI models.
  * Click on any chat to dive deeper into the conversation.
* **Create or Remove Chats:**
  * Create a new chat by clicking the **+** button next to the model name.
  * Remove a chat by clicking the three-dot menu and selecting **Delete**. Remove unnecessary chats to keep your workspace organized.

    <Frame>
      <img alt="Models Remove Chat Pn" />
    </Frame>

### Switching Between Models

* Next to the **+** button is a dropdown menu showing the currently selected model.
* Click the dropdown menu to select a different AI model and begin a new conversation with it.

  <Frame>
    <img alt="Models Switch Models Pn" />
  </Frame>


# Sub-API Keys
Source: https://io.net/docs/guides/intelligence/sub-api-keys

Issue scoped API keys to teams, services, or partners — each with independent model restrictions and credit limits that roll up to your account balance.

Sub-API keys allow an account holder (the *admin*) to issue multiple child API keys, each independently controlled. Each sub-key can be restricted to specific models, given a spending cap per billing cycle, and revoked at any time — without touching the admin key or other sub-keys.

## Overview

When you create a sub-key:

* It inherits your account's credit pool — there is no separate balance to fund.
* You optionally cap how much of that pool any single sub-key can consume per billing period.
* You optionally restrict which models the sub-key can call.
* The sub-key's usage feeds back into your account's overall billing.

This is useful for:

* **Teams** — give each team or project its own key with a monthly budget.
* **Partners / customers** — provide programmatic API access with hard credit limits so a single integration can never exhaust your entire balance.
* **Services** — isolate microservices with model allow-lists so they can only call the models they need.

## Authentication

All sub-key management endpoints use your **admin API key** in the `x-api-key` header. Sub-keys themselves authenticate inference calls (chat completions, embeddings, etc.) using the same header — they are recognized automatically by the API.

```bash theme={null}
# Admin operations (create, list, update, revoke)
-H "x-api-key: $ADMIN_API_KEY"

# Inference calls using a sub-key
-H "x-api-key: $SUB_API_KEY"
```

<Note>
  Sub-keys cannot create further sub-keys. Only an admin key can manage the key hierarchy.
</Note>

## Creating a Sub-API Key

<Steps>
  <Step title="Call the create endpoint with your admin key">
    ```bash theme={null}
    curl -X POST "https://api.intelligence.io.solutions/v1/api-keys/sub-keys" \
      -H "x-api-key: $ADMIN_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "description": "Partner integration – Acme Corp",
        "allowed_models": ["meta-llama/Llama-3.3-70B-Instruct"],
        "credit_limit": 10.0,
        "credit_refresh_cycle": "monthly",
        "key_prefix": "acme"
      }'
    ```
  </Step>

  <Step title="Store the returned key value securely">
    The response includes a `value` field with the full key string (e.g. `acme-v2-eyJhbGci...`). This is shown **only once**. Copy it to a secret manager immediately — it cannot be retrieved again.

    ```json theme={null}
    {
      "status": "succeeded",
      "data": {
        "key_id": "71775d2e-fbcc-4ef4-aa30-8aaeb82062c0",
        "value": "acme-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
        "display": "acme-v2-eyJh...c0eQ",
        "description": "Partner integration – Acme Corp",
        "allowed_models": ["meta-llama/Llama-3.3-70B-Instruct"],
        "credit_limit": 10.0,
        "credit_refresh_cycle": "monthly",
        "expires_at": "2026-08-20T00:00:00"
      }
    }
    ```
  </Step>

  <Step title="Distribute the sub-key to its intended user or service">
    The recipient uses the sub-key exactly like a regular API key — just pass it in the `x-api-key` header for inference calls.
  </Step>
</Steps>

## Request Parameters

| Field                  | Type                 | Required | Description                                                                                                            |
| ---------------------- | -------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| `description`          | string               | Yes      | Human-readable label for the key.                                                                                      |
| `allowed_models`       | string\[]            | No       | List of model IDs this key may call. Omit to allow all models.                                                         |
| `credit_limit`         | number               | No       | Maximum credits per refresh cycle. Omit for no per-key cap.                                                            |
| `credit_refresh_cycle` | string               | No       | When the usage counter resets: `"8h"`, `"daily"`, `"weekly"`, `"monthly"` (default).                                   |
| `expires_at`           | datetime / `"never"` | No       | Key expiry. Defaults to 180 days from creation.                                                                        |
| `key_prefix`           | string               | No       | 2–8 char lowercase slug prepended to the key (e.g. `"acme"` → `acme-v2-...`). Defaults to the standard `io-v2` prefix. |

## Model Restrictions

When `allowed_models` is set, any request to a model not in the list is rejected with **403 Forbidden**, even if the admin key has access to that model.

The `GET /v1/models` endpoint, when called with a sub-key, returns only the models in the sub-key's allow-list — so integrations can discover their permitted set without any extra configuration.

To remove all restrictions on an existing sub-key, pass an empty array:

```bash theme={null}
curl -X PATCH "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/{key_id}" \
  -H "x-api-key: $ADMIN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"allowed_models": []}'
```

## Credit Limits

### How limits are enforced

Credit limits are evaluated once per billing cycle by the settlement pipeline (which runs every \~60 seconds). When a sub-key's accumulated spend in the current period exceeds its `credit_limit`, the key is automatically blocked and inference calls return **429 Too Many Requests**.

The block clears automatically when the cycle resets (`credit_refresh_cycle`), or immediately when you raise the limit via `PATCH`.

### Blocking and unblocking

<AccordionGroup>
  <Accordion title="A sub-key is returning 429 — how do I unblock it?">
    The key has exceeded its `credit_limit` for the current period. You have two options:

    **Raise the limit immediately:**

    ```bash theme={null}
    curl -X PATCH "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/{key_id}" \
      -H "x-api-key: $ADMIN_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"credit_limit": 50.0}'
    ```

    **Wait for the next cycle reset** — the key unblocks automatically when `credit_refresh_cycle` rolls over.
  </Accordion>

  <Accordion title="How do I check how much a sub-key has spent?">
    Use the admin endpoint to inspect a specific key:

    ```bash theme={null}
    curl "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/{key_id}/usage" \
      -H "x-api-key: $ADMIN_API_KEY"
    ```

    Or let the sub-key check itself:

    ```bash theme={null}
    curl "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/me/usage" \
      -H "x-api-key: $SUB_API_KEY"
    ```
  </Accordion>

  <Accordion title="What happens to my account balance when a sub-key is blocked?">
    The block applies only to that specific sub-key. Your admin key and all other sub-keys continue operating normally. The admin's overall account balance is not affected by per-key limits.
  </Accordion>
</AccordionGroup>

## Credit Refresh Cycles

The `credit_refresh_cycle` determines when a sub-key's `credit_used` counter resets to zero, allowing spending up to `credit_limit` again.

| Cycle     | Resets at                                                    |
| --------- | ------------------------------------------------------------ |
| `8h`      | Every 8 hours aligned to midnight UTC (00:00, 08:00, 16:00). |
| `daily`   | Midnight UTC each day.                                       |
| `weekly`  | Monday 00:00 UTC.                                            |
| `monthly` | The 1st of each month at 00:00 UTC.                          |

## Custom Key Prefix

By default, sub-keys follow the standard `io-v2-` format. You can supply a custom `key_prefix` to make keys visually identifiable:

```json theme={null}
{ "key_prefix": "acme" }
```

Produces: `acme-v2-eyJhbGci...`

**Prefix rules:**

* 2–8 characters, lowercase letters, digits, and internal hyphens only.
* Cannot start with `io` (reserved for platform keys).
* Cannot contain version markers like `-v2`.

The prefix does not change any functionality — it is purely cosmetic for organizational clarity.

## Managing Sub-Keys

### Listing keys

```bash theme={null}
curl "https://api.intelligence.io.solutions/v1/api-keys/sub-keys" \
  -H "x-api-key: $ADMIN_API_KEY"
```

Returns all active sub-keys with their current `credit_used` for the active billing period.

### Updating a key

All fields on a sub-key can be updated at any time. Only the fields you include in the `PATCH` body are changed:

```bash theme={null}
curl -X PATCH "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/{key_id}" \
  -H "x-api-key: $ADMIN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Updated label",
    "credit_limit": 25.0,
    "credit_refresh_cycle": "weekly"
  }'
```

### Revoking a key

```bash theme={null}
curl -X DELETE "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/{key_id}" \
  -H "x-api-key: $ADMIN_API_KEY"
```

Revocation is immediate and permanent. Any subsequent inference call with the revoked key returns **401 Unauthorized**.

## Viewing Usage

### All sub-keys (admin)

```bash theme={null}
curl "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/usage" \
  -H "x-api-key: $ADMIN_API_KEY"
```

Returns a per-key breakdown of token consumption and credit cost, grouped by model, for today and all time — plus aggregate totals across all sub-keys.

### Single sub-key (admin)

```bash theme={null}
curl "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/{key_id}/usage" \
  -H "x-api-key: $ADMIN_API_KEY"
```

### Self-service (sub-key holder)

```bash theme={null}
curl "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/me/usage" \
  -H "x-api-key: $SUB_API_KEY"
```

## FAQs

<AccordionGroup>
  <Accordion title="Do sub-keys have their own credit balance?" icon="comment-question">
    No. Sub-keys draw from the admin's account balance. The `credit_limit` is a spending cap per cycle, not a separate balance. All usage by sub-keys is deducted from the same pool as the admin's own usage.
  </Accordion>

  <Accordion title="Can a sub-key call any model endpoint?" icon="comment-question">
    Only the models listed in `allowed_models`. If no list is configured, the sub-key can call any model available to the admin account. The `/v1/models` endpoint filters its response to only show the permitted models when called with a sub-key.
  </Accordion>

  <Accordion title="What happens when the cycle resets?" icon="comment-question">
    The sub-key's `credit_used` counter is reset to zero at the start of each new period. If the key was blocked due to exceeding its limit, it is automatically unblocked.
  </Accordion>

  <Accordion title="How quickly does blocking take effect after the limit is exceeded?" icon="comment-question">
    The billing settlement pipeline runs approximately every 60 seconds. Once a sub-key's accumulated spend exceeds its `credit_limit`, the block is applied within the next pipeline run.
  </Accordion>

  <Accordion title="Can I have sub-keys without a credit limit?" icon="comment-question">
    Yes. Omit `credit_limit` (or set it to `null`) when creating or updating a sub-key. The key will only be limited by the admin's overall account balance.
  </Accordion>

  <Accordion title="Is the key prefix stored anywhere?" icon="comment-question">
    No. The prefix is encoded in the key string itself. The display value (e.g. `acme-v2-eyJh...c0eQ`) shows the prefix so you can identify it, but it is not stored separately in the database.
  </Accordion>
</AccordionGroup>


# Training as a Service (TaaS)
Source: https://io.net/docs/guides/intelligence/training-as-a-service

Customize and fine-tune models to fit your needs - no need to train from scratch.

<Info>
  Note: This feature is currently in Beta. We are actively refining the experience and would love to hear your feedback.
</Info>

With IO Intelligence’s [Training as a Service (TaaS)](https://ai.io.net/ai/training), you can fine-tune powerful pre-trained models using your own data—achieving tailored performance without the complexity of training from scratch.

Built for builders, researchers, developers, and businesses, TaaS gives you greater control over how your AI learns and adapts. With support for advanced techniques such as PPO, DPO, and reward modeling, you can move beyond traditional fine-tuning and experiment at the cutting edge of machine learning.

<iframe title="Training as a Service with IO Intelligence" />

## Getting Started

To begin training your model:

* **Go to your** io.net Dashboard.
* Navigate to [**Training**](https://ai.io.net/ai/training) under the **IO Intelligence** section.

  <Frame>
    <img alt="" />
  </Frame>
* Click the **Start Training** button to launch the setup form.

  <Frame>
    <img alt="" />
  </Frame>

<Info>
  io.net does not support training models from scratch. All training is done via fine-tuning or customization of existing models.
</Info>

## Build Your Training Workflow

The *Training Model* form is designed to guide you through the setup process, step by step.

### 1. Select a Training Method

Pick how your model should learn. You can choose from a variety of advanced methods:

* **Supervised Fine-Tuning**: Teach your model using labeled datasets for task-specific learning.
* **Reward Modeling:** Train your model to assign scores to generated responses.
* **Proximal Policy Optimization (PPO):** Use reinforcement learning with reward feedback.
* **Direct Preference Optimization (DPO):** Optimize the model directly using ranked preferences.
* **Controlled Tuning Optimization** *(Experimental):* Apply KL-regularized tuning for fine-grained control.

<Frame>
  <img alt="" />
</Frame>

### 2. Select a Base Model

You can select a **pre-integrated** model from our library or bring your own model from **Hugging Face**.

<Tabs>
  <Tab title="Option A - Use a Preloaded Model">
    Choose from our library of 561 open-source base models in the dropdown list, for example, LLaMA, Mistral, Falcon, GPT-Neo, and many more.

    <Frame>
      <img alt="TaaS Choose Preloaded Model" />
    </Frame>
  </Tab>

  <Tab title="Option B - Link a Hugging Face Model">
    You can bring your own model from **Hugging Face** by following these steps:

    1. Paste your Hugging Face model repository link in the field.
    2. Click the **Test** button.
    3. If the connection is successful, you will see: “*Successfully tested.*”
    4. If the repository is **private** or **invalid**, a prompt will request your *Hugging Face Token* with the message: "*The repository is private or does not exist. Provide an HF Token".* For additional guidance, see [**How to get your Hugging Face Token**](https://huggingface.co/docs/hub/en/security-tokens).

    <Frame>
      <img alt="TaaS Select Model - Import from Hugging Face Link" />
    </Frame>
  </Tab>
</Tabs>

### 3. Select a Dataset

Choose training data from a **curated list** or bring your own custom dataset.

<Tabs>
  <Tab title="Option A - Use a Built-in Dataset">
    Select a dataset from our list using the dropdown menu.

    <Frame>
      <img alt="TaaS Select Dataset - Base Dataset" />
    </Frame>
  </Tab>

  <Tab title="Option B - Link a Custom Dataset">
    Set up your dataset by completing the configuration fields.

    <Frame>
      <img alt="TaaS Select Dataset - Custom Dataset" />
    </Frame>

    <Tip>
      Refer to the documentation link provided on top of the ***Configuration*** section for more details.
    </Tip>
  </Tab>
</Tabs>

### 4. Choose a Training Style

Depending on your goal, you can select between **Simple Creating** and **Advanced Creating** when training a model.

<Tabs>
  <Tab title="Option A - Simple Creating">
    Uses default settings for a quick and straightforward setup. Best if you want to get started fast without managing technical details.

    <Frame>
      <img alt="Taa S Simple Training Style Pn" />
    </Frame>
  </Tab>

  <Tab title="Option B - Advanced Creating">
    Offers full flexibility and control. Select this option if your goal is to customize every aspect of how your model learns, from hyperparameters to optimization strategies.

    <Note>
      For further technical documentation on each advanced configuration, refer to [Llama Factory](https://llamafactory.readthedocs.io/en/latest/).
    </Note>

    <Frame>
      <img alt="Taa S Select Training Style Temp Pn" />
    </Frame>
  </Tab>
</Tabs>

### 5. Start Training

After setting up the details of your model, click **Start Training** to begin.

## Training Dashboard

The following sections can be viewed in the ***Training Dashboard***.

#### Your Current Plan

At the top of the page, you can view your current plan details. To increase your training runs or access faster processing, click the **Upgrade** button.

<Frame>
  <img alt="" />
</Frame>

#### Your Training Jobs

Below your plan, there is a **Training Jobs** table where you can view and manage all your model training requests. Each row shows key details such as, *Job ID*, *Base Model*, *Type*, *Status*, and *Run Time.*

Click on any job to open the detailed view and see how it is progressing.

<Frame>
  <img alt="Your Training Jobs table" />
</Frame>

## Job Details

Click on a job from the dashboard to open its ***Job Details***. This provides everything you need to track and manage your model training in real time.

At the top of the page are the following buttons and indicators:

* **Download Model** – Available once the job is complete, to download the final model.
* **Abort Training** – Manually stop the job if necessary.
* **Time Remaining** – Displays how much time is left for training to finish.
* **Time Passed** – Shows how long the job has been running.

<Frame>
  <img alt="" />
</Frame>

### Training Metrics (Charts)

Track your model’s learning performance in real time.

* **Loss Chart** – Shows how training loss decreases over time.

This visual tool allows you to understand if your model is learning effectively - or if it needs adjustments.

<Frame>
  <img alt="" />
</Frame>

### Training Details

A summary of the key information for the training job is provided as follows:

* **Status** – Created, Deploying, Deploy Failed, Training Failed, Training, or Completed.
* **Date Created**
* **Model Name**
* **Training Method**
* **Base Model Used**
* **Dataset Used**
* **User Tag** - Custom label or identifier.
* **End Date** - If completed or aborted.

<Frame>
  <img alt="" />
</Frame>

### Training Logs

***Training Logs*** provide visibility into what occurs behind the scenes during the model training process. They contain a detailed list of steps, events, and status updates throughout the job’s lifecycle, making them especially useful for debugging, monitoring, or maintaining transparency.

Click the **Download Logs** button to save them locally for review or record-keeping.

<Frame>
  <img alt="" />
</Frame>


# Chat
Source: https://io.net/docs/guides/intelligence/unified-chat

One Chat. Every Tool — Powered by IO Cloud

**Unified Chat** enables your AI to **read**, **watch**, **listen**, and **create** across multiple content types in real time. After you upload files or connect data sources, the system extracts key information, integrates it with contextual knowledge, and generates **accurate**, **well-supported responses** to your queries. It can also **generate** images and videos, and perform live web searches to enhance the quality and relevance of its answers.

Unlike a standard chatbot, **Unified Chat** is built on **Retrieval-Augmented Generation (RAG)**. This approach connects answers directly to your own data, ensuring responses are **relevant, verifiable, and transparent**.

## How it works

**Unified Chat** uses **Retrieval-Augmented Generation (RAG)** — a method that pairs a language model with a retrieval system. Instead of relying only on pre-trained knowledge, the model retrieves and incorporates **the most relevant information** from your files and connected sources in real time.

This design is particularly useful in **enterprise, research, and developer workflows**, where **accuracy, explainability, and traceability** are essential.

<Note>
  Unified Chat replaces the previous **Retrieval Engine**. All existing features are preserved, with additional capabilities such as **multimedia support** and improved contextual understanding.
</Note>

## Getting Started

To begin using **Unified Chat**:

1. Go to your **io.net Dashboard**.
2. Navigate to [**Chat**](https://ai.io.net/ai/re) within **IO Intelligence**.

   <Frame>
     <img alt="Unified Chat1 Jp" />
   </Frame>
3. Upload your content and start chatting.

## Key Features

1. **Upload & Manage Files**

   * Click **Upload Files** or drag and drop files into the left-hand panel.
   * Supported formats include **.pdf, .docx, .png, .jpg, .mp4, .html**, and more.
   * Maximum file size per upload: **100MB**.

     <Frame>
       <img alt="Unified Chat" />
     </Frame>

   **Best practices:**

   * Use clear, descriptive file names and structured content for better results.
   * Avoid scanned or low-quality documents whenever possible.

   **To delete a file:**

   1. Hover over the file name.
   2. Click the **three-dot menu (⋮)**.
   3. Select **Delete**.

      <Frame>
        <img alt="Unified Chat5 Jp" />
      </Frame>
2. **Chat with Unified Chat**
   * Type your question or command in the chat box at the bottom of the page.
   * Use the microphone icon to record voice input (if preferred).

     <Frame>
       <img alt="Unified Chat Audio Recording2 Pn" />
     </Frame>

     <Frame>
       <img alt="Unified Chat Audio Recording Pn" />
     </Frame>
   * Each interaction **consumes tokens**.
   * You can also **attach additional files or images** and enable **web search** to provide more context for better answers.

     <Frame>
       <img alt="Unified Chat Attach Images Enable Web Search Pn" />
     </Frame>
3. **Generate Creative Outputs**

* Unified Chat can generate **creative outputs** such as **images, short videos, or anime clips** directly from your prompt.

  <Frame>
    <img alt="Unified Chat Creative Outputs Pn" />
  </Frame>
* Choose the desired output type before sending your prompt, or simply describe what you want in the chat.

**Short video example:**

<img alt="Unified Chatvideo Gi" title="Unified Chatvideo Gi" />

**Anime clip example:**

<img alt="Unified Chatanime Gi" title="Unified Chatanime Gi" />

## Communicating with Unified Chat

After uploading your documents, you can interact with **Unified Chat** to explore, analyze, and retrieve information.

### How to Ask Questions

1. Enter your question or prompt in the **chat field**.
2. **Unified Chat** will search your content and generate an **accurate, well-grounded response**.

### What Each Response Includes

* **Clear, concise answer** — directly addressing your query.
* **Reasoning breakdown** — explaining how the system reached the conclusion.
* **Tools or agents used** — showing any additional AI functions applied.
* **References to source files** — linking to your uploaded or connected content for traceability.

  <Frame>
    <img alt="Unified Chat Example Pi Pn" />
  </Frame>

### Example Use Cases

* Research paper analysis
* Enterprise document summarization
* Legal document Q\&A
* Media file transcription and interpretation
* Knowledge management for teams

## IO Credits and Token Management

Each chat interaction consumes tokens, which are **automatically refreshed daily**. If you reach the daily token limit of your plan and need additional usage, you can purchase **IO Credits** to continue without interruption:

<Note>
  When your daily quota limit is reached, the system will automatically switch to consuming your available **IO Credits** for continued usage — this applies across all subscription tiers.
</Note>

1. Click **Buy IO Credits** or **Upgrade to Professional** to continue when you run out of **Daily Credits**.
2. Complete your purchase to gain access to:
   * **Unlimited responses and storage** — continue conversations without restrictions.
   * **Advanced AI insights and automation** — unlock enhanced features and capabilities.
   * **Dedicated account management** — receive personalized support when needed.


# Sign Up or Log In to io.net
Source: https://io.net/docs/guides/loginsignup



## Create Account

If you haven't created an account yet, registration on [id.io.net](https://id.io.net) is currently available through  **Google**,  **Apple ID**, **Github**, **Huggingface**, **X (Twitter)**, **Worldcoin** or **email address**.

<img alt="Newlogin1 Jp" title="Newlogin1 Jp" />

### To get started

Choose your preferred method - Google, Apple ID, Github, Huggingface, X or Worldcoin and click the “**Sign Up**” button.

If you choose to sign up using your **email address**, you’ll go through a simple OTP (one-time passcode) verification process instead of creating a password:

1. Enter your email and click **Continue**.

   <img alt="Newlogin2 Jp" title="Newlogin2 Jp" />
2. A **one-time passcode (OTP)** will be sent to your email inbox.

   <img alt="Newlogin3 Jp" title="Newlogin3 Jp" />
3. Open the email from **io.net** with the subject “*Login to io.net*”, copy the large numeric code provided in the email.

   <Frame>
     <img alt="" />
   </Frame>
4. Return to the io.net website, **paste the code into the verification field**, and click **Verify Code**.

   <img alt="Newlogin5 Jp" title="Newlogin5 Jp" />

This method allows you to log in securely without needing to remember a password.

### If the email doesn't arrive:

* Check your **Spam** or **Junk** folder.
* Refresh your inbox after a few seconds.
* If still not received, wait **30 seconds** and click **Resend Code** to get a new OTP.

Once verified, your account will be created and you’ll be logged in automatically, ready to explore io.net’s services.


# Card Payment FAQs
Source: https://io.net/docs/guides/payment/card-payments-faqs

This page answers common questions about using Stripe (Fiat payments) and Credits when purchasing compute or IO Credits.

This page answers common questions about using Card (Fiat) payments when purchasing compute or IO Credits.

## General Payment Logic

**Users can pay for compute in two ways:**

* **IO Credits** — internal platform credits.
* **Fiat via Stripe** — credit/debit cards payment methods.

**Minimum amounts:**

* Purchasing IO Credits — **\$1.00**
* Paying directly with Fiat — **\$0.50**

## FAQ

### Q. Can I use Fiat (Stripe) to pay for compute?

Yes. You can now pay for compute directly using Fiat through Stripe. Minimum amount: **\$0.50**

If the cluster cost is **lower than the \$0.50 minimum card payment**, Stripe will still charge \$0.50, and **the remaining balance is automatically added to your IO Credits**.

<img alt="Stripe 1 Jp" title="Stripe 1 Jp" />

Stripe will show line items such as:

* `Cluster Cost`
* `Payment Provider Fee`

<img alt="Stripe 1 2 Jp" title="Stripe 1 2 Jp" />

### Q. Can I use Fiat to purchase IO Credits?

Yes. You can purchase IO Credits using either Crypto (USDC) or Fiat (Stripe). The minimum amount is **\$1.00**.

Stripe payment page will show line items:

* `IO Credits Cost`
* `Payment Provider Fee`

<img alt="Stripe 2 2 Jp" title="Stripe 2 2 Jp" />

After successful payment, credits are added to the user’s IO Credits balance.

### Q. What happens if I already have enough credits?

If your existing IO Credits balance is enough to cover the compute cost then **Fiat (card) payments are disabled**

The following message will appear: `You have sufficient credits to purchase compute. Please proceed to use them.` This ensures credits are used first before showing any Fiat options.

<img alt="Stripe 3 Jp" title="Stripe 3 Jp" />

### Q. Can I extend my compute using Fiat?

Yes. You can extend your compute using Fiat (Stripe). It works the same as initial compute purchase. Minimum fiat amount: **\$0.50**

<img alt="Stripe 4 Jp" title="Stripe 4 Jp" />

Any leftover amount (after cluster cost + provider fee) is **automatically added to IO Credits.**

<img alt="Stripe 4 2 Jp" title="Stripe 4 2 Jp" />

### Q. How are fees displayed during payment?

When paying through Stripe, you will see:

* **IO Credits Cost / Compute Cost**
* **Payment Provider Fee**
* **Total Amount**

This breakdown makes the payment fully transparent.

### Q. Can I pay with my local currency?

Yes. If your local currency is supported by Stripe, you should be able to pay using it.

Stripe will automatically handle currency conversion to USD during checkout.

The final amount charged may vary slightly based on exchange rates and your bank’s conversion fees.

### Q. Why am I purchasing credits when I pay by card?

Even when you pay directly by card (Fiat), the system works by first adding the equivalent amount as **IO Credits** to your account and then using those credits to pay for your compute clusters.

This happens automatically in the background, so you might see a small remaining balance added as credits if the cluster cost is less than the minimum card payment amount.


# Deploy Cluster and Pay
Source: https://io.net/docs/guides/payment/deploy-cluster-and-pay



### Deploy Cluster and Pay with \$IO Coin

If you don't have any funds in your account, you can still deploy a cluster and pay for it at the end of the process. In this example, we pay with **\$IO Coin**.

#### 1. Pay

1. Complete the steps to deploy a cluster, and on the final Summary step, select “Pay with \$IO Coin”. Please note that if you choose \$IO coins as payment for the cluster, the **conversion rate updates every minute** based on the exchange rate.

   <Frame>
     <img alt="" />
   </Frame>

   If you are satisfied with the current rate, click **Deploy Cluster** at the bottom of the Summary step.

   <Frame>
     <img alt="" />
   </Frame>
2. At the end of the deploy process, click **Click to pay button.** Please note that if payment isn't completed **within 20 minutes**, the cluster creation session will end, and the **cluster will be destroyed**. You'll then be redirected to the previous step to confirm the details and create the cluster again.

   <Frame>
     <img alt="" />
   </Frame>
3. In the **Payment Currency** dialog, you select **IO Coin** (via Sphere Pay). After selecting your payment method, click **Confirm Method**.

   <Frame>
     <img alt="" />
   </Frame>
4. On the **Set Amount** dialog, you can select **Custom** and enter any amount, or select the values to the right: **20, 100, 200, or 400** and click **Confirm Amount** and you are redirected to Spherepay to complete the transaction.

<Frame>
  <img alt="" />
</Frame>

#### 2. Select Payment Method - \$IO Coin

1. You are redirected to Spherepay to complete the transaction.
2. To connect your wallet, you can click **Select Wallet** or **Connect Wallet**.
3. When the wallet will be connected **Click Pay** with **\$IO Coin**

<Frame>
  <img alt="" />
</Frame>

#### 3. Connect Wallet

1. If you have a wallet, Spherepay may detect it. Scroll to browse and **select your wallet** if undetected. (Image below is a truncated list).

   <Frame>
     <img alt="" />
   </Frame>
2. Click **Connect**.

   <Frame>
     <img alt="" />
   </Frame>
3. After you complete the transaction, wait until your cluster is **successfully deployed.**

   <Frame>
     <img alt="" />
   </Frame>
4. Click **View Cluster** to view the details of your deployed cluster.

### Deploy Cluster and Pay with USDC Crypto

If you don't have any funds in your account, you can still deploy a cluster and pay for it at the end of the process. In this example, we pay with **USDC crypto**.

<Info>
  Users can no longer use their Cloud USDC Balance to deploy clusters. Even if your account shows a positive Cloud USDC Balance, you must make a separate direct payment via USDC crypto for each cluster deployment.
</Info>

#### 1. Pay

1. Complete the steps to deploy a cluster, and on the final Summary step, select **Pay with USDC**.

   <Frame>
     <img alt="" />
   </Frame>

   Check the cost in USD and click **Deploy Cluster**.

   <Frame>
     <img alt="" />
   </Frame>
2. At the end of the deploy process, click **Click to pay** button. Please note that if payment isn't completed **within 20 minutes**, the cluster creation session will end, and the **cluster will be destroyed**. You'll then be redirected to the previous step to confirm the details and create the cluster again.

   <Frame>
     <img alt="" />
   </Frame>
3. In the **Payment Currency** dialog, you select **USDC** (via Sphere Pay). After selecting your payment method, click **Confirm Method**.

   <Frame>
     <img alt="" />
   </Frame>
4. On the **Set Amount** dialog, you can select Custom and enter any amount, or select the values to the right: **20, 100, 200, or 400** and click **Confirm Amount** and you are redirected to Spherepay to complete the transaction.

   <Frame>
     <img alt="" />
   </Frame>

#### 2. Select Payment Method - USDC Token

1. You are redirected to **Spherepay** to complete the transaction.
2. To connect your wallet, you can click **Select Wallet** or **Connect Wallet.**
3. When the wallet will be connected **Click Pay** with **USDC**

<Frame>
  <img alt="" />
</Frame>

#### 3. Connect Wallet

1. If you have a wallet, Spherepay may detect it. Scroll to browse and **select your wallet** if undetected. (Image below is a truncated list).

   <Frame>
     <img alt="" />
   </Frame>
2. Click **Connect**.

   <Frame>
     <img alt="" />
   </Frame>
3. After you complete the transaction, wait until your cluster is **successfully deployed**.

   <Frame>
     <img alt="" />
   </Frame>
4. Click **View Cluster** to view the details of your deployed cluster.

### Deploy Cluster and Pay with Fiat

If you don't have any funds in your account, you can still deploy a cluster and pay for it at the end of the process. In this example, we pay with a credit card.

1. Complete the steps to deploy a cluster, and on the final Summary step, select **Pay with USDC**.

   <Frame>
     <img alt="" />
   </Frame>

   Check the cost in USD and click **Deploy Cluster**.

   <Frame>
     <img alt="" />
   </Frame>
2. At the end of the deploy process, click **Click to pay** button. Please note that if payment isn't completed **within 20 minutes**, the cluster creation session will end, and the **cluster will be destroye**d. You'll then be redirected to the previous step to confirm the details and create the cluster again.

   <Frame>
     <img alt="" />
   </Frame>
3. In the **Payment Currency** dialog, you select **USD** (Credit/Debit card). After selecting your payment method, click **Confirm Method**.

   <Frame>
     <img alt="" />
   </Frame>
4. On the **Set Amount** dialog, you can select Custom and enter any amount, or select the values to the right: **20, 100, 200, or 400** and click **Confirm Amount** and you are redirected to **Stripe** to complete the transaction.

   <Frame>
     <img alt="" />
   </Frame>
5. Select **Card** in the Payment method section. Enter your credit card information and click Pay.

   <Frame>
     <img alt="" />
   </Frame>
6. After your payment is processed, a confirmation appears.

   <Frame>
     <img alt="" />
   </Frame>
7. Return to the tab with your cluster. Payment Verified is checked and the cluster is in the **deployment process**. Click **View Cluster** to view the details of your deployed cluster.

   <Frame>
     <img alt="" />
   </Frame>


# Extending your Cluster and Pay
Source: https://io.net/docs/guides/payment/extending-your-cluster-and-pay



## Table of Contents

* [Extending Your Cluster and Paying with \$IO Coin](/guides/payment/extending-your-cluster-and-pay#extending-your-cluster-and-paying-with-io-coin)
* [Etending Your Cluster and Paying with USDC](/guides/payment/extending-your-cluster-and-pay#extending-your-cluster-and-paying-with-usdc)

### Extending Your Cluster and Paying with \$IO Coin

To expand your cluster, you need to click **Expand Cluster** in the active cluster

<Frame>
  <img alt="" />
</Frame>

A window will appear where you can choose the duration in **hours, days, or weeks.** Set your renewal preferences, check the **\$IO coins rate** (updated every minute), and click **Extend** if you're satisfied.

<Frame>
  <img alt="" />
</Frame>

If you don't have enough funds to expand the cluster, an additional pop-up will appear after clicking "**Expand**" to let you add more **\$IO coins**.

<Frame>
  <img alt="" />
</Frame>

### Extending Your Cluster and Paying with USDC

To expand your cluster, you need to click **Expand Cluster** in the active cluster

<Frame>
  <img alt="" />
</Frame>

A window will appear where you can select the duration in **hours, days, or weeks**. Set your renewal preferences, check the total cost, and click **Extend** if everything looks good.

<Frame>
  <img alt="" />
</Frame>

If you don't have enough funds to expand the cluster, an additional pop-up will appear after clicking **Expand** to let you add more funds in USDC.

<Frame>
  <img alt="" />
</Frame>


# Overview
Source: https://io.net/docs/guides/payment/io-cloud-payments

This document describes how to add crypto wallets and pay using the wallet or with credit cards.

io.net offers IO Cloud users different payment methods. Users may also pay at different points in the cluster deployment process.

## Table of Contents

* [Fees](/guides/payment/io-cloud-payments#fees)
* [Add Wallet for Crypto](/guides/payment/io-cloud-payments#adding-a-wallet-for-crypto-payments)
* [Manage funds page](/guides/payment/io-cloud-payments#manage-funds-page)
* [Deploy Cluster and Pay with \$IO Coin, USDC Crypto or Fiat](/guides/payment/deploy-cluster-and-pay)
* [Extending Your Cluster and Pay with \$IO Coin or USDC Crypto](/guides/payment/extending-your-cluster-and-pay)

### Fees

There are fees associated with reserving GPU & CPU and for payments made in USDC.

* Payments made in USDC are subject to **2% facilitation fee**.
* The IOG Network charges users a **0.25% reservation fee** on the total cost to reserve the compute. This is added to the Renter’s cost when reserving. There are fees associated with reserving GPU & CPU and for payments made in \$IO Coin.
* Payments made in \$IO Coin **incur no fees**.
* The IOG Network charges users a **0.25% reservation fee** on the total cost to reserve the compute. This is added to the Renter’s cost when reserving. To learn more, see [IO Coin.](https://internet-of-gpus.readme.io/docs/what-is-io-coin).

All suppliers must add at least three **(3) self-custodial Solana wallets** to their IO ID account to remain eligible for **Block Rewards**. This requirement is effective as of **23:59:59 UTC on April 30, 2025.**

You can associate up to **10 Solana wallets** with your account. One wallet will be designated as the **Primary Wallet**, which will serve as the default for all transactions **except Block Rewards Distribution.**

Please ensure your account meets this requirement to continue participating in the reward program.

For detailed steps on adding and managing wallets, please refer to the instructions below:

## Adding a Wallet for Crypto Payments

If you plan to pay using crypto, you must add a wallet to your account. **Credit card users don't need to complete this step.**

### Connect a Single Solana Wallet

To learn how to create your own Solana wallet, check out this [short guide](/guides/workers/solana). When you create your account, you are promoted to add a wallet. You can also skip the step and add your wallet in **Account Settings**.

Follow the steps below to add a wallet to your account:

1. Click on your icon in the upper right and select **Account Settings**.

   <Frame>
     <img alt="" />
   </Frame>
2. In Account Settings, find the **Solana Wallet Address** block and click the **Add Wallet** button.

   <Frame>
     <img alt="" />
   </Frame>
3. In the appearing popup, enter your new **Solana wallet address**
4. Click **Connect** to add the new address.

<Frame>
  <img alt="" />
</Frame>

5. As a result, your wallet will be successfully connected to the IO ecosystem.

### Connect a Single Aptos Wallet

To learn how to create your own Aptos wallet, check out this [short guide](/guides/workers/aptos-wallet). When you create your account, you are promoted to add a wallet. You can also skip the step and add your wallet in **Account Settings**.

1. Click on your icon in the upper right and select **Account Settings**.

   <Frame>
     <img alt="" />
   </Frame>
2. In the **Aptos Wallet** section, click **Add Wallet.**

   <Frame>
     <img alt="" />
   </Frame>
3. Enter your wallet address in the **Connect New Aptos Wallet** field and click **Connect**.

<Frame>
  <img alt="" />
</Frame>

## Adding Multiple Wallets

The **multi-wallet feature** allows you to add up to **10 Solana wallets** to your IO.net account, providing flexibility in managing **rewards, payments, and assets.**

This is particularly useful if one of your wallets becomes **inaccessible, lost, or compromised**, ensuring you still receive your rewards. Additionally, you can distribute rewards across different wallets for better **organization and security.**

You can add up to 10 wallets to your account. Here’s how to add additional wallets:

1. Underneath your first wallet address, find and click the **Add New Solana Wallet Address link**.

   <Frame>
     <img alt="" />
   </Frame>
2. In the appearing popup, enter your new **Solana wallet address** just like you did for your first wallet.
3. Click **Connect** to add the new additional address.

   <Frame>
     <img alt="" />
   </Frame>
4. Your new wallet will be successfully added to the IO ecosystem.

   <Frame>
     <img alt="" />
   </Frame>

## Primary Wallet Address

By default, your first wallet becomes the primary one. However, if you add more than one wallet, you can set another wallet as the primary. The primary wallet will be used for Block Rewards and payment transactions instead of the old address.

To change your primary wallet, hover your mouse over the desired wallet address and click on the blue star beneath the field. The selected wallet will then become the primary one.

<Frame>
  <img alt="" />
</Frame>

## Removing a Wallet

You can remove any of your wallet addresses at any time. Here’s how:

1. Hover over the wallet address you want to remove.
2. A **red Trash** icon will appear. Click on it to remove the selected wallet.

   <Frame>
     <img alt="" />
   </Frame>
3. A pop-up will appear to double-check your action to ensure you want to remove the wallet.

   <Frame>
     <img alt="" />
   </Frame>

<Warning>
  If you remove your wallet from the IO ecosystem, you will no longer receive block rewards, payments, or any other rewards associated with that wallet. Please be sure to remove wallets only when necessary.
</Warning>

<Frame>
  <img alt="" />
</Frame>

### Manage funds page

In the upper-right corner of the screen, click **Manage Funds**.

<Frame>
  <img alt="" />
</Frame>

This will open the **Manage Funds** page, where you can:

* View your lifetime Block Rewards earnings for your Workers.
* View the Block rewards already claimed for your Workers.
* View your current Cloud balance in USDC.
* View your current Cloud balance in \$IO Coin.
* See your **Worker Earnings** and Claim rewards.

<Frame>
  <img alt="" />
</Frame>

**List of Transactions**

This section also includes a **List of Transactions.** You can filter transactions by date within any allowed period and by categories such as:

* Reloaded
* Earnings
* Refunded
* Withdrawal
* Promo Credit

Additionally, you can filter transactions by sections in the IO system, such as:

* Worker
* Cloud

Clicking on a specific transaction will open a page with detailed information about it.

<Frame>
  <img alt="" />
</Frame>

**View a specific transaction**

The detailed transaction page shows:

* Amount and type of currency received
* Transaction type
* Platform used
* Status
* Date
* Transaction ID


# IO Credits
Source: https://io.net/docs/guides/payment/io-credits

Simplify your io.net Cloud payments with IO Credits, a prepaid USD-equivalent credit system you can use across compute products.

## What are IO Credits?

**IO Credits** are prepaid credits you can use to pay for compute deployments on io.net Cloud, including Ray Clusters, VMs, Kubernetes, and Baremetal. **Each IO Credit is equivalent to 1 USD**, this allows pricing to be simple and consistent.

## Why IO Credits?

* Pay once to use anytime.
* Can be used across [io.net](http://io.net) Cloud products.
* Faster checkout process during deployments.
* Refunds and incentives automatically appear as credits.
* API support is available for fully automated workflows.

## Quick Start

1. On the *Navigation Bar*, click **Buy IO Credits** and A pop-up window will appear.

   <Frame>
     <img alt="IO Credits Nav Bar" />
   </Frame>

   <Frame>
     <img alt="IO Credits Buy Pop Up" />
   </Frame>
2. Enter the amount of credits you want to purchase.
3. Choose a payment method: **USDC** or **USD (Credit/Debit Card)**.
4. If **USDC** is selected, you will be redirected to **Spherepay** to complete the transaction.
5. If **USD (Credit/Debit Card)** is selected, you will be redirected to **Stripe** to complete the transaction.
6. Once payment is confirmed, the purchased IO Credits will be added to your account.
7. Use IO Credits to deploy compute or inference workloads.
8. View your balance, track usage, and manage withdrawals in **Usage & Billing**.

### Refunds as Credits

If a deployment ends early or is cancelled, any unused funds are returned as IO Credits. You will be notified via the **Notification Center**.

## Using IO Credits

### Compute Products

During the checkout process, several payment options are available.\
Select **IO Credits** to view the required amount and your current credit balance.

<Info>
  1 IO Credit = 1 USD
</Info>

If sufficient credits are available, the **Pay & Deploy** button becomes active, allowing you to proceed with deployment.

### Use via API

Deployment endpoints accept the parameter `payment_method: "credits"`.\
If the available balance is low, the system may provide fallback options such as:

* `GET /credits/check?amount=XX` – Checks if sufficient credits are available for a specific amount.
* **Pending Payment** state – Indicates that payment confirmation is required.
* **Small negative credit allowance** (for example, up to -\$10) – Allows limited temporary usage.
* **Five-minute grace window** – Prompts you to top up before deployment fails.
* **Failure to deploy** – Occurs if credits are not replenished within the grace period.

## Managing IO Credits

### Viewing Credit Balance

To view your IO Credit balance:

1. Navigate to **Usage & Billing** from the top navigation bar.
2. In this page you can:
   * View your **Total IO Credits** displayed as a single balance (in USD).
   * View your **Credits Usage** and **Transactions**.
   * Request a **Withdrawal** (available for purchased credits only).

### Request Withdrawal

You may submit a manual request to withdraw available **purchased credits** from your balance.

Withdrawals are available only to users who have **paid for credits**. Once submitted, withdrawal requests are reviewed by the IO Finance team and typically **processed within three to seven business days**.

<Frame>
  <img alt="IO Credits Withdrawal Pop Up" />
</Frame>

#### Viewing Transactions

The **Transactions** section provides visibility into how your IO Credits have been **added, used, or refunded**. It allows you to track spending, reconcile deployments, and understand your current balance.

You will find transaction entries for the following categories:

* **Credit Inflow** – Credits that you have purchased or that have been issued to your account by the IO team.
* **Usage Deductions** – Credits spent on compute deployments, inference runs, or other billable operations.
* **Refunds** – Credits returned from early terminations, failed deployments, or unused services.

Each transaction record includes the following details:

* **Type** of transaction
* **Amount** added or deducted
* **Date and time** of the transaction
* **Transaction ID**

Use this log to **audit your activity**, **track usage patterns**, or **troubleshoot billing inquiries**.

<Frame>
  <img alt="" />
</Frame>

## Credit Usage via API and Tracking

Credits are tied to your IO ID and can be used across all io.net Cloud products. When using io.net APIs, you can specify the payment method as `credits` to automatically deduct from your balance.

## FAQs

<AccordionGroup>
  <Accordion title="What happens if I don’t have enough IO Credits?" icon="comment-question">
    You will be prompted to top up or use another payment method. Your deployment will pause temporarily and may fail if not resolved in time.
  </Accordion>

  <Accordion title="Can I convert credits back to USDC?" icon="comment-question">
    Only **purchased** credits may be withdrawn, after a manual review by the finance team.
  </Accordion>

  <Accordion title="Do IO Credits expire?" icon="comment-question">
    Yes. All **purchased** IO Credits expire **twelve (12) months from the date of purchase**.
  </Accordion>

  <Accordion title="What happens when my IO Credits expire?" icon="comment-question">
    Once IO Credits expire, any unused balance will **have no remaining value** and **cannot be withdrawn, refunded, or reinstated**.
  </Accordion>

  <Accordion title="Does this expiration policy apply to all IO Credits?" icon="comment-question">
    No. The **12-month expiration** applies **only to non-promotional credits**, which are credits that were **purchased or paid for by users**.

    Promotional credits (for example, credits granted by the IO team for trials, rewards, or campaigns) may have **different expiration timelines or conditions**, which will be **clearly stated** when they are issued.
  </Accordion>

  <Accordion title="Can I extend or renew my IO Credit expiration date?" icon="comment-question">
    No. Once IO Credits have expired, they **cannot be reactivated** or extended. To continue using IO, you can purchase new credits at any time.
  </Accordion>
</AccordionGroup>


# Overview
Source: https://io.net/docs/guides/payment/io-intelligence-payments

Overview of io.net’s AI access plans and model rates.

At **io.net**, we believe AI access should be **simple, transparent, and scalable**. Whether you are experimenting with ideas, running daily creative workflows, or deploying large-scale automation.

Our platform connects every capability, this includes **text, images, code, data, and voice**, all in one workspace.

You can start free, upgrade as your usage grows, and scale on demand without worrying about token tracking or hidden fees.

Each plan provides access to the same advanced models and tools. Usage is measured in credits, which refresh automatically. **Pay-as-you-go (PAYG)** is available when you exceed your daily credits quota.

* **Standard (default):** Explore and learn with free, light daily access. **Pay-as-you-go (PAYG)** pricing is applied for usage beyond the daily limit.
* **Professional:** Includes \$15 in monthly usage credits, refreshed daily to provide steady, predictable access for light coding projects and applications.
* **Developer:** Includes \$150 in monthly usage credits, refreshed every 8 hours to support continuous development and production workloads.

## Plan Overview

Each plan includes a **fixed daily or hourly allowance** that refreshes automatically, so you can focus on your work instead of tracking tokens or costs.

| Plan           | Usage                               | Refresh cycle                            | Ideal for                              |
| -------------- | ----------------------------------- | ---------------------------------------- | -------------------------------------- |
| *Standard*     | Continuous access with **PAYG**.    | No refreshes, pay only for what you use. | Teams that need flexible scaling.      |
| *Professional* | **\$15** in monthly usage credits.  | Once every 24 hours.                     | Coding projects or light applications. |
| *Developer*    | **\$150** in monthly usage credits. | Every 8 hours (3 x per day).             | Builders, teams, and automations.      |

## How Usage Works

* **Professional** plans refresh once every 24 hours for predictable, worry-free access.
* **Developer** plans refresh every 8 hours, designed for continuous work or API usage.
* If you hit your allowance, your access will pause until the next refresh, unless you have **IO Credits**.
* **IO Credits (Pay-As-You-Go)** allow instant continuation beyond limits, charging per request through your connected payment method.

## More on Pay-As-You-Go

* Billed directly to your **IO Credits** balance.
* Includes the same tools and models as subscription plans.
* The **Developer** plan offers roughly a 10% discount compared to **PAYG** for consistent high-volume users.
* **PAYG** stops when your plan refreshes.
* Enables precise accounting of model-level usage and costs.

<Note>
  To verify the latest model pricing, use the **GET /models** API endpoint. The response includes detailed pricing information for each available model. The fields `"input_token_price"` and `"output_token_price"` represent the respective costs per token for input and output usage. For implementation details and the full endpoint specification, refer to: [**GET /models API Documentation**](/reference/ai-models/get-models-list)**.**
</Note>

## FAQs

<Accordion title="What do I do when I hit my daily limit?" icon="comment-question">
  You can buy **IO Credits** or wait for your daily limit to refresh.\
  If you already have credits, they will automatically cover additional usage with no interruptions.
</Accordion>

<Accordion title="How does the limit work across different models?" icon="comment-question">
  ***IO Intelligence*** uses a **shared credit pool system**.\
  Credits can be spent on any model, with each consuming credits at a different rate depending on the complexity.
</Accordion>

<Accordion title="Does my daily limit include both Chat and API calls?" icon="comment-question">
  Yes. **Chat**  interactions count toward your API quota and contribute to your daily limit.
</Accordion>


# Overview
Source: https://io.net/docs/guides/staking/3rd-party-staking

In the world of decentralized networks, staking is a crucial way to secure blockchain systems and reward participants. Collaborative Staking (Co-Staking) takes this idea further by allowing third parties to participate in staking on devices they don't own, earning a share of the block rewards. This makes staking more accessible and encourages a more inclusive and cooperative network.

On our platform, **Co-Staking** allows users to contribute to staking on someone else’s device. This creates a partnership where both the device owner and the co-staker benefit. However, it’s important to remember that if a device doesn't meet the platform’s requirements, it could be penalized (a process called **slashing**), which may reduce both rewards and the original staked amount.

This guide will walk you through how to find staking opportunities, manage your co-staked devices, and track your rewards. Whether you're experienced with staking or just getting started, we’ll provide the tools and knowledge you need to navigate the Co-Staking system with confidence.

<Info>
  To ensure that more users can benefit from co-staking offers, we have set a claim cap of up to two offers per IO account.
</Info>

## FAQs

We've compiled answers to frequently asked questions about co-staking on io.net, including troubleshooting tips and guidelines to help users navigate the platform.

#### Getting Started with Co-Staking

<AccordionGroup>
  <Accordion title="Q: Why is the 'Create Co-Staking Offer' button greyed out for my device?">
    If you're a device owner and the **"Create Co-Staking Offer"** button is greyed out, it likely means your device hasn’t met the minimum self-staking requirement. io.net requires you to stake a certain amount of **\$IO tokens** on the device before inviting co-stakers. In most cases, you must stake **at least 50%** of the total required amount before creating an offer.

    Ensure that:

    * Your device is fully set up and active on the network.
    * You have met the minimum staking requirement.

    Co-staking is only available for operational devices.
  </Accordion>

  <Accordion title="Q. Can a person co-stake on multiple devices?">
    **Yes**, co-stakers can participate in multiple devices simultaneously. However, you can **only claim offers from two devices at any given time**. This ensures fair distribution and prevents one person from monopolizing multiple co-staking opportunities.
  </Accordion>

  <Accordion title="Q. Can I co-stake on my own device?">
    **No**, device owners **cannot co-stake on their own devices**. This rule is in place to prevent users from bypassing staking requirements, such as the **minimum self-staking threshold**. Co-staking is designed to foster collaboration between independent parties.

    <Info>
      Unstaking involves a 7-day waiting period followed by a 14-day cooldown period. Funds cannot be used during the cooldown, and rewards are paused during this time.
    </Info>
  </Accordion>
</AccordionGroup>

#### Co-Staking Terms & Rules

<AccordionGroup>
  <Accordion title="Q. How many co-stakers can a device have?">
    Each device can have **only one co-staker per offer.** Co-staking agreements follow a **one-to-one structure**:

    * **1 device owner → 1 co-staker**

    If a device owner needs more than one co-staker, they must create multiple offers or reduce their own stake. **Co-stakers can participate in up to two devices at the same time.**
  </Accordion>

  <Accordion title="Q. Are the identities of co-stakers or device owners visible?">
    No, identities are **anonymized** within the marketplace. While users can view **device specifications and staking terms**, personal details of device owners or co-stakers are not disclosed.

    However, **wallet addresses are visible on the blockchain**, but they do not directly reveal the identity of the parties involved.
  </Accordion>

  <Accordion title="Q. Can I change the terms of a co-staking agreement after it has been accepted?">
    **No**, once a co-staking offer is accepted, its terms are **locked in via a smart contract**. You **cannot modify** the stake amount, reward split, or other conditions after activation.

    If changes are needed, you must:

    1. **Cancel or close** the existing offer.
    2. **Create a new** offer with the updated terms.
  </Accordion>
</AccordionGroup>

#### Withdrawing & Unstaking

<Accordion title="Q. How do I unstake and withdraw funds from co-staking?">
  To withdraw your staked funds:

  1. Click "**Unstake**" - this initiates a **7-day waiting period** where your tokens stop earning rewards.
  2. After the waiting period, your stake enters a **14-day cooldown period**.
  3. Once the cooldown ends, your tokens will be available for withdrawal.
</Accordion>

#### Risks & Performance Considerations

<AccordionGroup>
  <Accordion title="Q. What if the device I co-staked on performs poorly or goes offline?">
    io.net has a **slashing mechanism** that penalizes underperforming devices. If a device frequently goes offline or fails to meet performance requirements, **both the device owner's and co-staker's stake may be slashed**.

    <Info>
      Slashing means forfeiting part of the staked amount as a penalty.
    </Info>

    To minimize risk, always **select reliable devices** before co-staking.
  </Accordion>

  <Accordion title="Q. How does co-staking compare to traditional staking?">
    Unlike traditional staking, where tokens are delegated to validators, **co-staking on io.net directly stakes tokens onto a specific device.**

    Key differences:

    * Co-stakers share the risk of slashing.
    * Rewards and conditions are set in a **smart contract.**
    * It promotes a **collaborative staking model** rather than simple delegation.
  </Accordion>
</AccordionGroup>

#### Troubleshooting & Support

<Accordion title="Q. What should I do if I experience an issue not covered in the FAQs?">
  If you encounter a problem, such as:

  * A **transaction error**
  * A **device not appearing in the marketplace**
  * **Co-staking issues**

  Try the following:

  * Ensure you’re using the **official io.net platform**.
  * Verify that your **wallet is properly connected**.
  * **Clear your browser cache** or try a **different browser**.

  If the issue persists, reach out to **io.net support** through:

  * [Support ticket system](https://support.io.net/en/support/home)
  * [Discord community](https://discord.com/invite/ionetofficial)

  When [contacting support](https://support.io.net/en/support/home), provide key details like your **wallet address** and **device ID** for faster assistance.
</Accordion>


# Co-staking
Source: https://io.net/docs/guides/staking/co-staking

Co-staking allows third parties to stake on devices and share block rewards. As a co-staker, you contribute to an existing staking offer and receive a share of the block rewards based on the agreed-upon percentage.

## Table of Contents

* [The Staking Marketplace](/guides/staking/co-staking#the-staking-marketplace)
* [Co-stake to a Device](/guides/staking/co-staking#costake-to-a-device)

Co-staking allows third parties to stake on devices and share block rewards.

<Danger>
  Devices failing to meet IO.net criteria may result in slashing, affecting rewards and principal.
</Danger>

## The Staking Marketplace

To explore staking opportunities, go to **IO Staking** > **Co-staking Marketplace**. The marketplace provides all the information you need to make informed decisions.

<Frame>
  <img alt="" />
</Frame>

The marketplace includes filters for:

* **Device Model:** GPU or CPU type.
* **Device ID:** Search by device ID.
* **Requested Amount:** Amount of \$IO requested by the device owner.
* **Reliability**: Indicates device dependability.
* **Offered Reward Percentage:** Block reward percentage shared with co-stakers.

The screenshot below provides an example of Co-Staking offers.

<Frame>
  <img alt="" />
</Frame>

## Co-stake to a Device

<Info>
  To ensure that more users can benefit from co-staking offers, we have set a claim cap of up to two offers per IO account.
</Info>

To co-stake a device:

1. Click the **Co-stake** button next to the device to view a summary of the offer.

   <Frame>
     <img alt="" />
   </Frame>
2. If you agree with the terms, click **Stake**

   <Frame>
     <img alt="" />
   </Frame>
3. Approve the transaction in your wallet app (**e.g., Phantom**). The interface may vary depending on your wallet..

   <Frame>
     <img alt="" />
   </Frame>
4. The status will first show **Sending** and then change to **Approved**.

   <Frame>
     <img alt="" />
   </Frame>

To see your co-staked device, go to the **Third-Party Co-Staking Devices** tab.


# Create a Co-staking Offer
Source: https://io.net/docs/guides/staking/create-a-co-staking-offer

Co-Staking operates as a smart contract on the blockchain, allowing device owners to invite co-stakers to contribute to their stake in exchange for a share of block rewards.

## Table of Contents

* [Create a Co-staking Offer](/guides/staking/create-a-co-staking-offer#create-a-co-staking-offer)
* [Offer Status](/guides/staking/create-a-co-staking-offer#offer-status)
* [Check Co-Staked Devices](/guides/staking/create-a-co-staking-offer#check-co-staked-devices)

### Create a Co-staking Offer

**Prerequisite**

Before creating a Co-Staking offer, ensure that your device meets the **minimum staking requirement**. If the requirement is not met, the option to create a Co-Staking offer will be disabled (grayed out).

**Steps to Create a Co-Staking Offer**

1. In the **Staking Actions** column, click the three dots next to your device and select **Create Co-Staking Offer.**

   <Frame>
     <img alt="" />
   </Frame>
2. Set the amount of IO you’re requesting from a potential co-staker using the slider on the **Co-Staker Contribution** page. *The maximum co-stake is 50% of the total stake.*

   <Frame>
     <img alt="" />
   </Frame>
3. On the **Block Reward Sharing** page, define the reward percentage for the co-staker using the slider. In the screenshot below, the co-staker will receive 74% of the block reward. Below the slider, we provide the estimated block reward per block for your co-staker based on the previous 7-day average.

   <Frame>
     <img alt="" />
   </Frame>
4. Review your choices on the **Summary** page and click **Create a Co-Staking Offer**.

   <Frame>
     <img alt="" />
   </Frame>
5. A unique offer link will be generated. Share this link with your collaborators.

   <Frame>
     <img alt="" />
   </Frame>
6. To see your device, return to the Staking section and find your device listed under the **Co-Staking Devices** tab.

   <Frame>
     <img alt="" />
   </Frame>

### Offer Status

Track your Co-Staking offer in the **Co-Staking** Devices tab. Statuses include:

* **Sufficient State (Wait Period):** The co-staker has unstaked, and their contribution is in the 7-day **Wait Period**. The stake still counts toward the device’s minimum staking requirement but does not earn block rewards.
* **Sufficient State (Waiting for Co-Staker):** The owner has staked the device and is awaiting a co-staker.
* **In Cooldown:** The unstaking process has completed the wait period and is now in a **14-day cooldown**, where funds remain locked.
* **Co-Staker Withdrawn:** The co-staker has successfully withdrawn their funds after completing the unstaking process.
* **Co-Staker Unstaked (In Wait Period):** The co-staker has initiated unstaking, and their funds are in the **7-day wait period.**
* **Offer Closed:** The offer has been closed by the owner or due to other circumstances and is no longer available in the marketplace.
* **Insufficient Stake (Waiting for Co-Staker):** The device does not meet the minimum stake requirement and is waiting for a co-staker to fulfill it.

<Frame>
  <img alt="" />
</Frame>

### Managing Co-Staked Devices

1. To view and manage your co-staked devices, click **Co-Staked Devices** tab.

   <Frame>
     <img alt="" />
   </Frame>
2. To view offers, click the ellipsis next to the device and choose **Co-Staking Details**.

   <Frame>
     <img alt="" />
   </Frame>
3. The Check Offer modal shows you the parameters of the **Co-Staked Device**.

   <Frame>
     <img alt="" />
   </Frame>


# Overview
Source: https://io.net/docs/guides/staking/device-owner-staking



Staking **\$IO tokens** is a key step in participating in the IO.net decentralized ecosystem. It helps secure the network, validate computational tasks, and earn rewards. Whether you're staking on your own or teaming up with others through **co-staking**, this guide will walk you through everything —from connecting your wallet to managing your stakes and maximizing your rewards.

## Table of Contents

* [Solo Staked Devices](/guides/staking/solo-staked-devices)
* [Protecting your Stake](/guides/staking/protecting-your-stake)
* [Create a Co-staking Offer](/guides/staking/create-a-co-staking-offer)
* [Deleting, Unstaking & Withdrawing](/guides/staking/unstaking-deleting-withdrawing)
* [FAQs](/guides/staking/device-owner-staking#faqs)

### FAQs

#### General Co-Staking Questions

<AccordionGroup>
  <Accordion title="Q: Can a person co-stake on multiple devices?">
    Yes.
  </Accordion>

  <Accordion title="Q: Is there a limitation?">
    As the device owner, you can not co-stake with your own devices.
  </Accordion>

  <Accordion title="Q: What is the maximum number of co-staking offers I can claim?">
    To ensure that more users can benefit from co-staking offers, we have set a claim cap of up to **two offers per IO account.**
  </Accordion>
</AccordionGroup>

#### Identity & Anonymity

<AccordionGroup>
  <Accordion title="Q: Are there any identifiable details of a co-staker or device owner?">
    No, the marketplace deliberately anonymizes this information for privacy. However, wallet details remain public on the blockchain.
  </Accordion>

  <Accordion title="Q: What if a co-staker and device owner want to adjust contributions?">
    If the co-staking offer is still not being taken up, the device owner can simply cancel the offer and create a new one. Otherwise, they must unstake and wait for the cooldown period to pass before creating a new one.
  </Accordion>
</AccordionGroup>

#### Staking Structure & Financial Impact

<AccordionGroup>
  <Accordion title="Q: Can multiple co-stakers contribute to a single offer?">
    No. Only one co-staker is allowed per offer.
  </Accordion>

  <Accordion title="Q: If a primary worker is suspected of fraud or gets slashed, what happens financially to the co-staker?">
    If BR (Block Rewards) are slashed, co-stakers are also impacted.
  </Accordion>

  <Accordion title="Q: What happens to the co-staked \$IO when the device owner terminates the device?">
    The device will immediately stop earning Block Rewards for both the supplier and co-staker as the device no longer meets the requirement for earning Block Rewards. Staked \$IO will not be automatically unstaked and will need to be manually unstaked and go through the applicable Wait Period and/or Cooldown period.
  </Accordion>
</AccordionGroup>


# Device Reliability Score
Source: https://io.net/docs/guides/staking/device-reliability-score

The Device Reliability Score is a key metric that helps both worker providers and co-stakers assess the reliability and trustworthiness of a device in the staking network. It reflects how consistently the device performs and whether it meets io.net’s technical and uptime requirements.

## For Worker Providers:

Your **Device Reliability Score** directly impacts your ability to attract co-stakers. A higher score indicates a more reliable device, making it more appealing for co-stakers who want to ensure their contributions are secure and productive.

#### How to Boost Your Device Reliability Score:

1. **Maintain Consistent Uptime:** Devices that experience frequent downtime or technical issues are penalized. Ensure your device is always running and connected to the network as much as possible.
2. **Meet Staking Requirements:** Consistently meet the minimum staking requirements to avoid slashing or penalties. Slashing or unstaking for failure to meet requirements directly impacts your score.
3. **Device Performance:** Devices with higher computational power (e.g., newer GPUs, faster CPUs) tend to have a better reliability score. Optimize your hardware for better performance.
4. **Network Stability**: Ensure that your internet connection is stable and fast. Devices that frequently disconnect or experience network instability will receive a lower reliability score.
5. **Monitor & Optimize Regularly**: Regularly check your device’s performance metrics and optimize it as necessary, whether that’s upgrading hardware or troubleshooting any recurring issues.

## For Co-Stakers:

As a **co-staker**, the **Device Reliability Score** allows you to evaluate the likelihood that your contribution will remain stable and continue to earn rewards without disruptions. Devices with higher scores are less likely to face slashing penalties or fail to meet staking requirements.

#### How to Use the Reliability Score:

1. **Filter by Reliability:** In the **Co-Staking Marketplace**, you can filter offers based on the **Device Reliability Score**. This helps you sort and prioritize staking offers that come from more reliable devices.

   <Frame>
     <img alt="" />
   </Frame>
2. **Evaluate the Risk:** A device with a **low reliability score** might be riskier for your investment. Be sure to assess whether the offered reward percentage justifies the risk.

   <Frame>
     <img alt="" />
   </Frame>
3. **Understand the Impact on Rewards:** A lower reliability score may increase the risk of slashing or other penalties, meaning you could lose part of your staked funds. Devices with high reliability are less likely to experience slashing.

## How the Reliability Score is Calculated:

The **Device Reliability Score** is determined based on several factors, including:

* **Device Uptime:** Percentage of time the device is online and active.
* **Performance Metrics**: Hardware capabilities and performance consistency.
* **Network Stability**: Frequency of disconnections or network failures.
* **Slashing Events**: Past penalties for failing to meet staking requirements.
* **Historical Compliance**: Whether the device owner consistently meets the staking thresholds.

A **higher score** indicates a better-performing, more reliable device, making it more attractive for both workers to stake on and co-stakers to contribute funds.

## Key Benefits for Both Worker Providers and Co-Stakers:

* **For Worker Providers:** Higher reliability scores help attract more co-stakers, increasing the likelihood of filling staking offers.
* **For Co-Stakers:** By sorting devices based on reliability, you can reduce the risk of staking your funds on a device prone to penalties, disconnections, or performance issues.


# Unstake and Withdraw $IO
Source: https://io.net/docs/guides/staking/how-to-unstake

This document explains how to unstake & withdraw $IO.

## Table of Contents

* [How to Unstake \$IO](/guides/staking/how-to-unstake#how-to-unstake-io)
* [Withdraw \$IO After Cooling Period](/guides/staking/how-to-unstake#withdraw-io-after-cooling-period)

### How to Unstake \$IO

You can unstake at any time. An Unstake option is available for every device you stake. Once you unstake, you are subject to a 14-day cooldown period before the stake can be withdrawn. If a stake is in cooldown period, it does't meet the staking requirement for Block Rewards.

Follow the instructions below to unstake \$IO:

1. Go to io.net > **IO Worker** > **Staking** tab.
2. Locate the stake that you want to unstake. Click **Unstake** under the **Action** column.

<Frame>
  <img alt="" />
</Frame>

3. A pop-up window appears, informing you that the entire amount must be unstaked & that it no longer counts toward the Minimum Required Stake for Block Rewards. Click the **Unstake** button.

<Info>
  Staking rewards are not automatically compounded.
</Info>

<Frame>
  <img alt="" />
</Frame>

4. After you **Unstake**, a timer appears next to the worker, counting down the 14-day cooldown period. You can't withdraw your funds until this period of time elapses.

<Frame>
  <img alt="" />
</Frame>

### Withdraw \$IO After Cooling Period

To withdraw funds after the cooldown period, go to the **Staking** tab and click the **Withdraw** button.

<img alt="" />

<img alt="" />

You can only withdraw funds to the wallet used for the initial stake. If you attempt to withdraw to a different wallet, you will receive a warning message. To stake with a new wallet, please unstake and withdraw your funds first.

<Frame>
  <img alt="" />
</Frame>

If you use the same wallet, you're prompted to withdraw funds to it. When you click the **Withdraw** button, your wallet extension will open to **Confirm** the transaction.

<Frame>
  <img alt="" />
</Frame>


# Overview
Source: https://io.net/docs/guides/staking/io-staking

At IO.net, we're committed to building a robust, secure, and decentralized platform for GPU and CPU supply and demand. Our staking program is designed to align incentives, ensure network integrity, and reward active participants in our ecosystem.

<Frame>
  <img alt="STAKING Pn" />
</Frame>

<Info>
  The content of this doc is subject to change depending on successful contract auditing.
</Info>

### Why Staking?

Staking is a crucial component of our network security and efficiency. Requiring suppliers to stake \$IO allows us to:

* Encourage long-term commitment to our platform.
* Create an incentive for good behavior.
* Establish a mechanism to discourage and penalize malicious actions.

### How It Works

**Staking Requirements**

To participate in our network and receive block rewards, GPU and CPU suppliers must stake a specific amount of \$IO. The exact staking amount required is determined on the supplier's capacity and their contribution to the network.

The staking requirement is displayed in the UI. The formula for the total is explained below.

1. Base requirement (minimum stake per card) X = \$IO 200.
2. If the multiplier per GPU on the device is less or equal to 1, the per GPU stake is 1 /\* X. The minimum staking remains \$IO 200.
3. If the multiplier per GPU on the device is greater than 1, then the multiplier value is represented by M. The per GPU stake on this device is M /\* X. (Device Earning Multiplier /\* Minimum Stake)
4. If there are multiple (N) GPUs on the device, the total device stake value is M /\* N /\* X.

```
minimum_stake_required = base_requirement_per_card * max(1, earning_multiplier)
```

**Examples**

1. If there are eight (8) H100 GPUs (earning multiplier=10) on device A. The minimum staking requirement value is `$IO 200`. Then the amount required to stake on device A is 8 \* 10 \* 200 = 16,000 `$IO`.
2. If there are four (4) 4070s GPUs (earning multiplier=0.25) on device B. The minimum staking requirement value is `$IO 200`. Then the amount required to stake on device BCD is 4 /\* 1/\* 200 = 800 `$IO`.

**Rewards**

Each supplier’s device will have a dedicated smart contract where the `$IO` stake is secured. Block Reward Eligibility is determined on a per-device basis. In Phase I, Block Rewards are accrued to the [Solana wallet address ](/guides/workers/solana)associated with your account and are distributed through periodic reward claims. This ensures a fair and transparent distribution of rewards to all qualifying participants.

**Unstaking Process**

When a supplier decides to unstake their `$IO`, a 14-day cooldown period is initiated. Once unstaked, `$IO` in a cooldown period is no longer counted toward minimum staking requirement for Block Rewards. This period helps maintain network stability and prevents potential manipulation.

The action of unstaking is irreversible. You can not restake to your device until the cooldown period ends. You must withdraw the coins after the cooldown period to stake to the same device again.

<Info>
  When you unstake and withdraw your IO Coins, always use the wallet used in the initial stake.
</Info>

**Security**

To protect our network and users, we implemented a slashing mechanism. Staked `$IO` and accrued block rewards can be subject to slashing. If a supplier engages in malicious behavior, such as spoofing or compromising data, a portion of their staked \$IO tokens may be slashed (i.e., deducted from their stake). Also, if your device is providing inadequate service, it is subject to slashing.

Slashed `$IO` is subject to a one month reconsideration process. If you notice your device stake is slashed, you can open up a support ticket. IO support will present technical evidence that proves why the device was identified for spoofing or other malicious behavior. Device owners can appeal this decision. If the device owner doesn't appeal the decision or the appeal is lost, the slashed `$IO` will be burned.

### **Get Started**

To participate in the staking program, ensure you have the required amount of `$IO` and follow our simple staking process in the IO.net platform.

<Info>
  In Phase I, only device owners can stake to their own devices. We plan to add features for non-node operators to also stake \$IO and earn rewards in Phase II.
</Info>

We're excited to launch this staking program and look forward to growing our network together. For more detailed information or assistance, please refer to our comprehensive documentation or contact our support team. Join us in shaping the future of decentralised computing with IO.net.

#### Staking Release Stages

1. **Phase**: Staking is currently **available for workers only**.
2. **Phase**: Staking for **non-workers is coming soon.**

For more details on earning multipliers, Block Rewards, and the minimum staking requirements, please refer to our public documentation: [Proposed calibration in earning multiplier and the simulated impact on Block Rewards](/guides/block-rewards/proposed-device-block-reward-multiplier).


# Protecting your Stake
Source: https://io.net/docs/guides/staking/protecting-your-stake

How to Ensure Strengthened Security for Your Stake

When participating in \$IO staking, it’s crucial to only interact with the official and correct smart contract. This contract governs the staking process, ensuring your funds are safely managed in line with the platform's operations. To protect yourself from potential risks, always verify the contract address before making any transactions. Here’s how you can safeguard your funds and ensure the legitimacy of your transactions.

<Danger>
  We will never DM you in Discord or any other platform outside our official channels with alternative wallet addresses.
</Danger>

Be cautious of scammers who may ask you to transfer funds to alternative addresses. If you receive any unsolicited messages asking you to send crypto to another wallet or join a staking offer outside of official channels, **do not engage**. Scammers often impersonate our team, and many users have fallen victim to these attacks, resulting in lost funds. Protect your assets by following the steps outlined below.

## Official \$IO Staking Contract Address

To ensure you're interacting with the [correct contract](https://solscan.io/account/3RRz3bZ7Khr3Cw2i7JURpKuUPT3G9QFV7fNVPmhSsF2i), always verify the address in our official documentation.

```
https://solscan.io/account/3RRz3bZ7Khr3Cw2i7JURpKuUPT3G9QFV7fNVPmhSsF2i 
```

## Security Practices to Protect Your Stake:

* **Access URLs Directly:** Always type **io.net** directly into your browser and bookmark the site. This protects against phishing sites that could trick you into entering personal details on fraudulent websites.
* **Verify Smart Contracts:** Before interacting with any smart contract, use trusted tools like **Solscan** to confirm the contract address matches the one provided in our official documentation. This step helps ensure your interactions are with legitimate addresses only.
* **Watch Out for Phishing:** Be cautious of links from unverified sources, unsolicited crypto offers, or direct messages, especially on platforms like Discord, social media, or community forums. Scammers often impersonate official channels and offer fake staking opportunities or ask you to send funds to alternative wallet addresses.
* **Use Secure Wallets:** For added security, use **hardware wallets** to store your funds. These provide an extra layer of protection against hacks. Never share your **private keys** or **seed phrases** with anyone, and always store them securely.

## Why this matters:

Interacting with **incorrect or malicious contracts** could result in the **loss of your funds** or the compromise of your sensitive information. Always verify every detail and follow the security measures listed above before making any transactions or interacting with smart contracts.

## Verify Official Contract Addresses

To ensure the security of your transactions with the \$IO ecosystem, always double-check the following contract addresses:

* **`$IO` Token Contract**: The official smart contract for the `$IO` token.
* **`$IO` Staking Contract**: The official contract for staking your `$IO` tokens.
* **`$IO` Safety Module**: The contract for the \$IO Safety Module, which provides additional security features for your stake.

You can verify these addresses using:

* **Official documentation** or the **io.net** website.
* **Blockchain explorers** like **Solscan**.
* **Community announcements** or official support channels.


# Solo Staked Devices
Source: https://io.net/docs/guides/staking/solo-staked-devices

This section outlines how to individually stake IO and manage your stake effectively. For general information, refer to .

## Staking Tab

To view the Staking tab, go to io.net > **IO Worker** > **Staking**. The Staking tab displays:

* **Total Wallet Balance:** Available balance in \$IO.
* **Total Active Stake**: Amount actively staked.
* **Total in Cooldown**: Funds in the unstaking process.
* **Rewards from the Latest Block**: Your latest block rewards in \$IO.

<Frame>
  <img alt="" />
</Frame>

## How to Stake

#### Connect Your Crypto Wallet

To stake on IO, you need to connect your crypto wallet.

1. Go to io.net > **IO Worker** > **Staking** tab.
2. Follow the steps in [Rewards and Wallets](/guides/workers/rewards-wallets) to connect your wallet.

<Info>
  Staking above the minimum required stake does not increase block rewards.
</Info>

#### Stake \$IO

Once you’ve connected your wallet, you can stake \$IO to your device. After you connect your device to our network, you must stake to the device.

To view your devices that have no stake or only a stake from the device owner, click the **Solo Staked Devices** tab. The screenshot below shows a **list of devices**, indicating whether they have no stake, or just the owner’s stake.

<Frame>
  <img alt="" />
</Frame>

<Info>
  Before making a co-staking offer, a full stake must be created for your device.
</Info>

#### Stake your tokens

1. Locate your device and click **Stake** in the **Staking Actions** column.

   <Frame>
     <img alt="" />
   </Frame>
2. In the pop-up window, enter the required **\$IO amount** to stake your device, then click **Stake**. Any subsequent solo staking attempts on the same worker must use the wallet that was initially used for the device’s stake.

<Frame>
  <img alt="" />
</Frame>

## 14-Day Cooldown Period

The **14-day cooldown period** is important when unstaking your funds. Here's how it works:

* You can **unstake** at any time, but there is a **14-day cooldown period** before the funds can be fully withdrawn.
* **Funds in cooldown** are **not counted toward staking requirements.**
* During the cooldown, your funds remain locked and cannot be withdrawn until the process is complete.

<Danger>
  During the cooldown period, your funds do not contribute to staking rewards. You will only be able to access your funds after the 14-day period ends.
</Danger>


# How to Stake
Source: https://io.net/docs/guides/staking/staking

This document describes how to stake with $IO. Staking is a crucial component of our network security and efficiency. For general information about staking, see .

## Table of Contents

* [Staking Tab](/guides/staking/staking#staking-tab)
* [How to Stake](/guides/staking/staking#how-to-stake)
  * [Connect Crypto Wallet](/guides/staking/staking#connect-crypto-wallet)
  * [Stake \$IO](/guides/staking/staking#stake-io)
* [Smart Contract Address](/guides/staking/staking#smart-contract-address)

## Staking Tab

To view the **Staking** tab, go to io.net > **IO Worker** > **Staking**. This tab displays information about your staking earnings:

* Total Wallet Balance in \$IO
* Total Active Stake in \$IO
* Total in Cooldown in \$IO
* Rewards from the Latest Block in \$IO

<Frame>
  <img alt="" />
</Frame>

<Info>
  Staking rewards are not automatically compounded. The unstaking process takes fourteen days to complete. \$IO in the unstaking process (cooldown) does NOT count towards staking requirement.
</Info>

## How to Stake

#### Connect Crypto Wallet

To stake on IO, you need to connect your crypto wallet.

<Info>
  If you stake more than the minimum required stake, you don’t earn extra block rewards.
</Info>

1. In io.net, go to **IO Worker** > **Staking** tab.
2. Click **Connect Crypto Wallet** on the right side on the **Staking** page.

   <Frame>
     <img alt="" />
   </Frame>
3. Select your crypto wallet in the pop-up window. Please note that this wallet can be different from the wallet you have associated with your account. For example, see [Solana Wallet](/docs/solana) to learn more.

   <Frame>
     <img alt="" />
   </Frame>
4. The **Phantom** wallet prompts you to connect with IO. Click **Connect** to proceed.

   <Frame>
     <img alt="" />
   </Frame>

   After the wallet is connected, your Wallet ID is displayed on the right side of the **Staking** page. This indicates a **successful connection.**

   <Frame>
     <img alt="" />
   </Frame>

#### Stake \$IO

Now that your crypto wallet is connected, you are ready to stake \$IO..

1. Locate the worker you want to stake to and click the **Stake** button under **Staking Actions** in the **Manage Your Stake & Devices** table.

<Frame>
  <img alt="" />
</Frame>

2. In the pop-up window, enter the required amount of `$IO` for your hardware, and confirm by clicking the **Stake** button. Remember that you can always add to your `$IO` stake later, but you must use the same wallet that you originally used to stake on that device.

<Frame>
  <img alt="" />
</Frame>

<Info>
  You can unstake at any time, and an Unstake option will be available for each device you’ve staked. Bear in mind that once you unstake, you will need to wait for a 14-day cooldown period before the stake can be withdrawn. Stake in cooldown does not count towards the staking requirement for devices to receive Block Rewards.
</Info>

## Smart Contract Address

This smart contract address is a unique identifier where the \$IO staking contract is deployed:

```
https://solscan.io/account/8tvkkogztREitU38YBxZDmirRiarcm5vNaCV2P2pFArz 
```

#### Security

Solscan allows you to explore and view data stored on the Solana blockchain. You can use this to verify the smart contract address you are interacting with against the official address provided in our documentation. This ensures you are engaging with the legitimate contract.

You can also review the total amount of \$IO staked on the blockchain. You can confirm the staked amounts and verify that info matches your expectations.

Read the suggestions below to enhance the security of your stake:

* Manually enter io.net into your URL to stake and bookmark it. Don't search for io.net to avoid imposter websites. Sites such as [GoDaddy](https://www.godaddy.com/whois) offer domain lookups. Most imposter sites are active for a very short period of time.
* Do not click on links from unverified sources. Beware of strangers approaching you on social media about crypto opportunities.
* Be aware of phishing websites and fake contracts that attempt to mimic our staking platform. If something seems suspicious, verify the information with our resources or contact our support team.
* Always use a secure wallet and consider hardware wallets for added security. Be cautious of any prompts that ask for your private keys or seed phrases. We won't ask for this information.


# Unstake Your Co-stake & Withdrawing
Source: https://io.net/docs/guides/staking/unstake-your-co-stake



## Unstaking

You can cancel a stake at any time. If a co-staker unstakes first, an additional **7-day wait period** is added to the **14-day cooldown**, making the stake unavailable for **21 days**.

#### Partial Unstaking of Overflow (Solo Stakers)

Solo stakers can also partially unstake their excess (overflow) amount without deactivating the worker.

* **Overflow** is calculated as: `(Your Stake + Co-stake) – Minimum Stake Requirement`

* You can withdraw this overflow at any time by:

  * Using the **Withdraw Overflow** button (if visible), or
  * Selecting **Unstake** and entering an amount equal to or less than the overflow.

<Warning>
  If you enter more than the overflow amount, the system will treat it as a full unstake and deactivate the device.
</Warning>

#### Important Notes

* Unstaking may be **blocked** if:

  * The device is currently **rented in a cluster**
  * The offer is **open** and unstaking would reduce the total stake below the required minimum

There is **no penalty** or impact on the device status when withdrawing only the overflow amount.

#### How to Unstake your Co-Staking Devices:

1. Go to the **Manage Your Stake & Devices** section and find your device.

2. Click the three dots next to the device and select **Unstake** from the dropdown menu.

   <Frame>
     <img alt="" />
   </Frame>

3. Confirm by clicking **Unstake**.

   <Frame>
     <img alt="" />
   </Frame>

## Withdrawing

You can withdraw your funds only after completing the **14-day cooldown** period.

**To Withdraw for Your Co-Staking Device:**

1. Go to the **My Co-Staking Devices** tab and locate your device.

2. Click the three dots next to the device and select **Withdraw** from the dropdown menu.

   <Frame>
     <img alt="" />
   </Frame>

3. Confirm by clicking the **Withdraw**.

   <Frame>
     <img alt="" />
   </Frame>


# Deleting, Unstaking & Withdrawing
Source: https://io.net/docs/guides/staking/unstaking-deleting-withdrawing

Co-Staking operates as a smart contract on the blockchain, allowing device owners to invite co-stakers to contribute to their stake in exchange for a share of block rewards.

## Table of Contents

* [Deleting a Co-Staking Offer](/guides/staking/unstaking-deleting-withdrawing#deleting-a-co-staking-offer)
* [Unstaking](/guides/staking/unstaking-deleting-withdrawing#unstaking)
* [Withdrawing Overflow](/guides/staking/unstaking-deleting-withdrawing#withdrawing-overflow)

### Deleting a Co-Staking Offer

* If you unstake part of your contribution while co-staked, you are **not** subject to a cooldown period.
* If a co-staker cancels their stake, you have **7 days** to cover the remaining portion or create a new co-staking offer.
* During this **7-day period**, your device continues fulfilling staking requirements for block reward eligibility.

<Info>
  Your device must still meet all other criteria.
</Info>

**Steps to Delete a Co-Staking Offer**:

1. Go to the **Manage Your Stake & Devices** block, where all your staking devices are listed, and click the three dots next to the desired device.

2. Select **Delete a Co-Staking Offer** from the dropdown list.

   <Frame>
     <img alt="" />
   </Frame>

3. In the pop-up, confirm by clicking the **Retract My Co-Staking Offer** button to complete the process.

   <Frame>
     <img alt="" />
   </Frame>

**If you unstake first:**

* If your stake remains above the minimum requirement, there is no impact.
* If your stake **falls below the requirement**, the system automatically unstakes for the co-staker. In this case, all funds enter the **14-day cooldown period**.

### Unstaking

You can cancel a stake at any time.

* **Unstaking takes 14 days.**
* You must **unstake the entire amount**, which stops counting toward the **Minimum Required Stake** immediately.
* You **cannot** restake until the process is complete.
* Unstaking **is not available** for devices in **hired status.**

**How to Unstake Your Device:**

1. Go to the **Manage Your Stake & Devices** block, where all your staking devices are listed, and click the three dots next to the desired device.

2. Select **Unstake** from the dropdown list.

   <Frame>
     <img alt="" />
   </Frame>

3. In the pop-up, confirm by clicking the **Unstake** button to complete the process.

   <Frame>
     <img alt="" />
   </Frame>

   <Info>
     If an unfilled co-staking offer exists for the selected device, retract your offer before unstaking.
   </Info>

### Withdrawing Overflow

Overflow refers to funds exceeding your initial stake that can be withdrawn separately, while your original stake remains locked until the unstaking process is complete.

**How to Withdraw Overflow:**

1. Go to the **Manage Your Stake & Devices** section and select the **Co-Staked Devices** tab.

2. Find your device, click the ellipsis, and select **Withdraw Overflow** from the dropdown menu.

   <Frame>
     <img alt="" />
   </Frame>

3. To confirm, click **Withdraw Overflow**. You can only withdraw overflow funds, not the main staked amount.

   <Frame>
     <img alt="" />
   </Frame>

<Info>
  You can only withdraw overflow funds, not the main staked amount.
</Info>


# View Co-Staking Device
Source: https://io.net/docs/guides/staking/view-co-staking-device



## View Co-Staking Device

Go to **IO Staking** > **My Co-Staking Devices** to see your devices listed with Co-Staking.

<Frame>
  <img alt="" />
</Frame>

Select the desired device in the **Manage Your-Staking Devices** block and click **Co-Staking Details** in the Action column.

<Frame>
  <img alt="" />
</Frame>

This shows you the parameters of the **Co-Staked Offer Device.**

<Frame>
  <img alt="" />
</Frame>

## View Block Rewards Earned through Co-Staking

To view your co-staked devices and earnings, go to  **IO Staking**> **My Co-Staking Devices** > **Block Rewards tab.**

<Frame>
  <img alt="" />
</Frame>

A graph showing your block reward earnings will appear, with options to filter by daily or monthly views.

<Frame>
  <img alt="" />
</Frame>


# Additional Guides
Source: https://io.net/docs/guides/workers/additional-guides



### Ports

Expose the ports below to ensure platform stability for Linux:

* TCP: 443, 25061, 5432, 80
* UDP: 80, 443, 41641, 3478

Ensure that these ports are open and accessible to enable smooth operation of the platform.

### How can I verify that program has started successfully?

* When running the following command on Terminal, **you should always have 2 Docker containers running**:
  <CodeGroup>
    ```Text Terminal Command theme={null}
     docker ps
    ```
  </CodeGroup>

* If there are no containers or only one container running after running the docker run **-d ... command** from the website:

  * Stop the platform using the command provided in the guide above.
  * Restart the platform using the command from the website again.

### reset\_drivers\_and\_docker.sh :

Create a new file called `reset_drivers_and_docker.sh`, and copy paste the code snippet below:


# Aptos Wallet
Source: https://io.net/docs/guides/workers/aptos-wallet

This document discusses Aptos and provides instructions on how to create a Aptos Wallet.

## What is a Aptos Wallet?

An <Tooltip>Aptos</Tooltip> Wallet is a digital wallet designed for securely storing and managing Aptos tokens, sending and receiving transactions, and interacting with decentralized applications (DApps) on the Aptos blockchain. It offers features such as private key management, encryption, and a user-friendly interface for monitoring balances and transaction history. Additionally, it integrates with various blockchain services and platforms, and can be available as mobile apps, browser extensions, or hardware wallets.

## How to Create a Aptos Wallet

You can create any Aptos (APT) wallet from the official list here: [Aptos Ecosystem](https://aptosfoundation.org/ecosystem/projects/wallets).

For this example, we will use a popular option - Petra, and demonstrate how to configure and use the wallet:

**1. Go to** [Petra Wallet.](https://petra.app/)

1. Select the browser to install Petra on. In this example, we use Chrome.
2. Click **Add to browser**.

<Frame>
  <img alt="" />
</Frame>

**2. Add to Chrome**

After you click **Add to browser**, you're redirect to the extension download page.

Click **Add to Chrome** to add the extension to Chrome.

<Frame>
  <img alt="" />
</Frame>

**3. Open the Petra extension**

1. Click **Create New Wallet**.
2. Create a password for your wallet.
3. Click **Continue**.

<Info>
  If you forget your password you will need to restore your wallet using your seed words, provided in the next step. Also, if you clear the browser cache, you cannot login using a password. You must restore wallet again using the seed word.
</Info>

<Frame>
  <img alt="" />
</Frame>

**4. Store the Recovery Phrase**

1. In the **Secret Recovery Phrase** page, copy and store your 12 word Secret Recovery phrase. You can save them on password managers like **Keepass**.
2. Click **Continue**.

<Frame>
  <img alt="" />
</Frame>

<Warning>
  Failure to save your Secret Recovery Phrase can result in an inability to access your account. You may lose access to your coins.
</Warning>

**5. Copy the APT Address**

After you click **Continue**, the wallet generates a new APT address. This is the address used to receive coins.

To copy your APT address:

1. Click on Aptos wallet extension.
2. Click **Receive**.
3. At the top of the extension, click **Copy** icon to copy deposit address.

<Frame>
  <img alt="" />
</Frame>

**6. Go to your IO ID account to set your new APT wallet address.**

Follow the steps below to set your APT wallet address.

1. Log in to your io.net account.
2. Go to your **IO ID** profile.
3. In the **Account Settings tab** (it's there by default), find the **Aptos Wallet** address field.
4. Click **Change Wallet** button
5. Enter your new **Aptos** wallet address.
6. Click **Connect** to add the new address.

<Frame>
  <img alt="" />
</Frame>


# Bare Metal On-Demand Supplier Process
Source: https://io.net/docs/guides/workers/bare-metal-on-demand-supplier-process

As a supplier of bare metal on-demand devices, you provide critical hardware that powers high-performance computing tasks for consumers. This guide outlines the steps to register your devices, comply with network standards, and securely reset hardware after bookings, ensuring seamless participation and maximum rewards.

### Register Your Device

1. Install the latest version of the IO.NET Binary.
2. Use the following command to launch the binary: `/io_net_launch_binary_linux --device_id=DEVICE_ID --user_id=USER_ID --operating_system="Linux" --usegpus=true --device_name=DEVICE_NAME --worker_mode=baremetal --worker_ip=HOST_IP --worker_port=HOST_PORT` Replace **DEVICE\_ID** and **USER\_ID** with your specific identifiers.

### When Your Device is Hired

* Once your device is hired as a Bare Metal device:
  * **Exemption**: It is exempt from Proof of Work and Proof of Time Lock requirements, allowing you to earn block rewards even under the consumer’s control.

### Post-Booking Requirements

* **Wipe the Device**:
  * You have 24 hours to wipe the device and reinstall the binary after the booking period ends. Failure to do so will result in the cessation of block rewards for the device.

* **Reinstallation Steps**:

  * Reinstall the IO.NET Binary.

  * Inform our Customer Support (CS) team by following these steps:

    * Sign in or create an account at the [Support Portal](https://support.io.net/en/support/signup).

    * Submit a support ticket with the following:

      * **Issue Type**: “IO Worker”
      * **Subject**: “Recycled the device(s)”
      * **Device ID(s)**: List all recycled device IDs.
      * **Description**: Add “Recycled the device(s)” under the explanation field.

    * Submit the form.

### Recommended Cleanup Steps

| Action                               | Steps                                                                                                                                                                                                                                      |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Terminate Active Processes**       | **Purpose:** Ensure no data is in use or locked.<br /> **Actions:** Shut down applications, databases, and services. Stop all background tasks.<br /> **Verification:** Confirm no active processes remain using tools like `ps` or `top`. |
| **Unmount and Securely Wipe Drives** | **Purpose:** Ensure no residual data is recoverable.<br /> **Actions:** Unmount filesystems using `umount`. Securely delete data using tools like `shred`, `dd`, or `wipe`. For SSDs, use the manufacturer's secure erase utility.         |
| **Reset RAID Configuration**         | **Purpose:** Clear RAID metadata.<br /> **Actions:** Delete RAID arrays using `mdadm` or vendor utilities.                                                                                                                                 |
| **Update Firmware**                  | **Purpose:** Remove malicious firmware or backdoors.<br /> **Actions:** Update server firmware (BIOS/UEFI, BMC/iDRAC/iLO).<br /> **Verification:** Confirm firmware updates are applied.                                                   |
| **Reset Configuration**              | **Purpose:** Restore server to factory defaults.<br /> **Actions:** Reset BIOS/UEFI and IPMI/iDRAC/iLO configurations, including passwords and network settings.                                                                           |
| **Document the Cleaning Process**    | **Purpose:** Maintain an audit trail.<br /> **Actions:** Record the commands and tools used. Attach logs for verification.                                                                                                                 |
| **Verify Clean State**               | **Purpose:** Ensure no residual data or configurations.<br /> **Actions:** Boot into a live environment (e.g., Ubuntu Live USB). Check that drives are unpartitioned and firmware is reset.                                                |
| **Reinstall Base OS**                | **Purpose:** Prepare the server for the next customer.<br /> **Actions:** Reinstall the requested base OS or leave it unformatted per customer requirements.                                                                               |


# Connectivity Displays Incorrectly
Source: https://io.net/docs/guides/workers/connectivity-tier-not-displaying-correctly

To troubleshoot connectivity tier issues, users can test network speeds via a sample Docker container. Here's how:

1. Pull the Python 3.9 Slim container:

   ```
   docker pull python:3.9-slim
   ```
2. Run the container:

   ```
   docker run -it --name speedtest-container python:3.9-slim /bin/bash
   ```
3. Install the speedtest tool:

   ```
   pip install speedtest-cli
   ```
4. Test the network speed:

   ```
   speedtest-cli
   ```

<Frame>
  <img alt="" />
</Frame>

We recommend running similar speed tests periodically within your containers to monitor connectivity performance. You can also guide users on how to perform these tests at regular intervals or during specific instances for troubleshooting.


# CUDA Toolkit
Source: https://io.net/docs/guides/workers/cuda-toolkit-optional

A step by step process for Downloading the CUDA Toolkit.

### What is CUDA?

The CUDA Toolkit is like a toolbox for programmers who want to make their software run faster using NVIDIA graphics cards. It has everything they need, like tools and instructions, to write code that takes advantage of the graphics card's power for tasks like math calculations, simulations, and artificial intelligence. Here are a few steps to install the CUDA Toolkit:

### 1. Go to [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) Download Page

Choose either the Windows or Linux operating system to access additional settings.

<Frame>
  <img alt="" />
</Frame>

### 2. Provide Additional Information

For Windows, you need to choose your architecture, which is usually x86\_64 for 64-bit systems.

<Frame>
  <img alt="" />
</Frame>

### 3. Download the Recommended Cuda Executable File

Downloading the Local Installer file may take some time. Please be patient. After downloading the file, run the installer.

<Frame>
  <img alt="" />
</Frame>

### 4. Open the .exe File and Proceed With the Installation Process

It includes steps such as agreeing to the terms and selecting installation options.

<Frame>
  <img alt="" />
</Frame>

### 5. Fixing CUDA Toolkit Installation Errors

Installation errors while installing CUDA Toolkit are common issues encountered by many users.

<Frame>
  <img alt="" />
</Frame>

Follow these steps to resolve the error:

1. When reinstalling the CUDA Toolkit, opt for **Custom (Advanced)** installation.

   <Frame>
     <img alt="" />
   </Frame>
2. After selecting the custom installation option, expand the **CUDA** section and uncheck the option for **Nsight Compute** to exclude it from the installation. This step ensures that only the necessary components are installed, reducing the likelihood of errors.

   <Frame>
     <img alt="" />
   </Frame>
3. Proceed with the installation process.

### 6. Verify the Installation Process

<Frame>
  <img alt="" />
</Frame>

After the installation, open Windows Terminal and enter the following command:

<CodeGroup>
  ```Text Terminal Command theme={null}
  nvcc --version
  ```
</CodeGroup>

You should receive a similar response:

```
nvcc: NVIDIA (R) Cuda compiler driver  
Copyright (c) 2005-2022 NVIDIA Corporation  
Built on Wed_Sep_21_10:41:10_Pacific_Daylight_Time_2022  
Cuda compilation tools, release 11.8, V11.8.89  
Build cuda_11.8.r11.8/compiler.31833905_0
```

### That’s It. You Have the Cuda Toolkit Installed and Ready

Now that CUDA Toolkit has been successfully installed and is running, you can proceed with [setting up the Worker](/docs/install-on-windows)

<Info>
  Feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>


# Overview
Source: https://io.net/docs/guides/workers/device-onboarding

This document provides instructions about how to create an account, device onboarding basics, block rewards, staking, and statuses to assist in you in the onboarding process.

### Table of Contents

* [Create Account](/guides/workers/device-onboarding#create-account)
* [Requirements](/guides/workers/device-onboarding#requirements)
* [Set Up a New Worker](/guides/workers/device-onboarding#set-up-a-new-worker)
* [App Guide](/guides/workers/device-onboarding#app-guide)
  * [Workers Homepage](/guides/workers/device-onboarding#workers-homepage)
  * [Device Status](/guides/workers/device-onboarding#device-status)
  * [Readiness](/guides/workers/device-onboarding#readiness)
  * [Transition Between States](/guides/workers/device-onboarding#transition-between-states)
* [Troubleshoot](/guides/workers/device-onboarding#troubleshoot)

### Create Account

To create an account, go to [worker.io.net](https://worker.io.net/). Currently, you can sign up using Google, Apple ID, X, or Worldcoin. Choose your preferred option, click **Sign Up**, and you're all set to join us.

**Go to**[worker.io.net](https://worker.io.net)

<Frame>
  <img alt="" />
</Frame>

### Requirements

Devices that meet the [minimum system requirements](#minimum-system-requirements) are eligible for job assignments. All devices must pass our [Proof of Work](/guides/workers/proof-of-work) verification through the Worker to be hired by clusters.

To view a list of the current supported devices, see [Supported Devices](/guides/workers/supported-devices).

<Info>
  After your onboard your device for the first time, there is a 12 hour waiting period until it's eligible to be hired as a worker. Your device is only subject to the waiting period after its initial onboarding.
</Info>

#### Minimum System Requirements

* 12 GB RAM
* 256 GB SSD
* Windows: NVIDIA GeForce RTX 30xx and above series / MacOS: Apple M3, M4.
* Internet Speed (please use [speedtest.net](https://www.speedtest.net/) or a similar service to check your speed) To qualify for the airdrop, the minimum requirement is 100Mb/s download and 75Mb/s upload. However, for a higher chance of being hired, the recommended minimum requirements are:
  * Download: Above 500 Mb/s
  * Upload: Above 250 Mb/s
  * Ping: Below 30ms

<Info>
  For better performance, we recommend a download/upload speed of 200–500 Mbps and 16GB of RAM to avoid crashes.
</Info>

#### Staking

Your must stake to your device to make it eligible for block rewards and to be hired for jobs. For more information about staking, see our [Staking](/guides/staking/io-staking) documentation.

### Set Up a New Worker

We have detailed guides available to help you set up your worker on various operating systems such as:

* [MacOS](/guides/workers/install-on-macos)
* [Windows](/guides/workers/install-on-windows)
* [Ubuntu](/guides/workers/install-on-ubuntu)
* [HiveOS](/guides/workers/install-on-hiveos)

These guides are tailored to provide step-by-step instructions, ensuring a smooth setup process for your new worker. Whether you're using MacOS, Windows or Ubuntu, you'll find comprehensive guidance to join get your worker up and running efficiently.

## App Guide

### Workers Homepage

This screen provides users with real-time access to general information about all their calculations. Users can easily see who is connected to the network, currently active, or experiencing errors. Additionally, they can perform actions like renaming and deleting devices.

For users managing a large number of devices, features like search and sorting by criteria such as Status, Brand, Technology, Connectivity Tier, and Security Compliance are invaluable.

This page allows you to monitor workers and track data such as:

* **Status**
* **Device ID-** The unique identifier for your device. Click the ID to view the Device Detail page.
* **Readiness**- This value provides insights into your device's readiness for Block Reward eligibility.
* **Up For**
* **Chip/GPUs**

<Frame>
  <img alt="" />
</Frame>

### Device Status

**Device Status** is displayed at the top of the table.

<Frame>
  <img alt="" />
</Frame>

| Status                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🟢 **up/running**         | Running status is indicative that everything installed correctly and everything is in normal operations. No issues.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 🟢 **Idle**               | Idle status is indicative that everything installed correctly and everything is in normal operations but it has not been hired by someone yet. It is awaiting work. No issues.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 🟡 **Paused**             | Paused status is indicative that the client has manually suspended or disabled the node. They can resume it themselves.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 🔴 **Down**               | Down status is indicative that a worker is down and needs to re-run the commands.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 🔴 **Failed**             | Failed status is indicative of a connection/outage problem or the device is offline. The device is not communicating and is unavailable or experiencing another form of outage such as:<br /><br />• **Error during startup**: There may have been errors during the startup of your worker that prevented it from launching successfully.<br />• **Resource issues**: It's possible that there aren't enough resources available for your worker to start, such as allocated memory, CPU time, or other resources.<br />• **Network failure**: Network issues can prevent the establishment of connection with the platform or other services, leading to startup failures. |
| 🟠 **Blocked**            | Blocked status is indicative that we detected GPU utilization that was not authorized by our internal checks. It's important that GPU availability is dedicated 100% to the task being volunteered for the health of the DePin.<br /><br />Blocked status occurs in a few different flavors, but mainly these:<br />• **Excessive GPU Utilization**: Playing games, Graphic intensive utilization, etc. (You'll need to pause it before you start usage)<br />• **Mining Detection**: FYI - Our team has implemented an update to detect mining devices and instances with high GPU usage, resulting in an automatic ban.                                                    |
| 🟣 **Unsupported device** | Unsupported status is indicative that your worker or its current configuration is not supported into the IO.NET platform at this moment. This could be due to incompatibility with the required software version, operating system, or hardware components. The list of supported devices can be checked [here](/docs/supported-devices).                                                                                                                                                                                                                                                                                                                                    |
| 🟣 **Inactive**           | Inactive status is indicative that your worker has been inactive for more than 5 days. This may have been caused by pausing a worker and forgetting about it, an outage, or a technical / communication issue.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Readiness

The **Readiness** column differs from **Status**. This value provides insights into your device's readiness for Block Reward eligibility. The screenshot below shows the Readiness column in the **Device Status** table.

<Frame>
  <img alt="" />
</Frame>

If the status is **Cluster Ready,** then your device is eligible to be hired and/or for a Block Reward. The four possible Readiness statuses are:

| Status                     | Description                                                                                                                                                                                                                                                                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cluster Ready**          | Device meets PoW requirements and passed several Cluster Formation verifications.                                                                                                                                                                                                                                                                  |
| **Hired**                  | Device is currently hired by a cluster.                                                                                                                                                                                                                                                                                                            |
| **Pending**                | The device has joined the network and is currently undergoing both the PoW and Cluster Readiness test. This process can take up to 12 hours of cumulative uptime after onboarding, but may complete sooner if your device passes our tests early. If your device remains in a Pending state after more than 12 hours of uptime, please contact us. |
| **Not Block Reward Ready** | Device doesn't meet the criteria for block reward eligibility, mainly Cluster Formation verifications.                                                                                                                                                                                                                                             |

**Not Block Reward Ready** offers one of three tooltips in the UI to provide troubleshooting tips.

* **Please check your device's computational capacity**- Your device's computational capacity is below the required threshold.
* **Please check your device setup and computational capacity**- Your device setup might not be configured correctly and its computational capacity is below the required threshold. Please refer to the worker setup guide.
* **Please check your device setup**- Your device setup might not be configured correctly. Please refer to the worker setup guide.

#### Transition Between States

The transition from **Pending** to **Cluster Ready**state can take up to 12 hours. During this time, we form clusters with newly joined devices (Pending) and verify them as **Cluster Ready** once they successfully pass the cluster formation process.

If the device fails to join the cluster multiple times, it's labeled as **Not Block Reward Ready**. To verify if a device has successfully passed cluster formation is to check its job page, which indicates the record of past cluster formations.

### Troubleshoot

1. Verify that the device is operated using io.net official binaries and official docker images.
2. Verify that the device has the right network setup (beyond basic internet speed test capability) where the device can properly interact with the remote head node or peer workers.


# Device Utilization Threshold
Source: https://io.net/docs/guides/workers/device-utilization-threshold

Devices available for hire on io.net should remain idle and not perform any computationally intensive tasks. We are updating device requirements to ensure that your processor utilization rates do not exceed the thresholds specified in the tables below.

<Danger>
  Starting November 4th, 2024 00:00:00 UTC, any devices that fail to adhere to the maximum utilization requirement will be considered non-compliant. Workers that fail to comply can be blocked and are subject to slashed Block Rewards.
</Danger>

### Processors

| Supported Processor         | Max CPU Utilization Threshold | Max GPU Utilization Threshold |
| --------------------------- | ----------------------------- | ----------------------------- |
| A10                         | 30%                           | 5%                            |
| A100 80GB PCIe              | 30%                           | 5%                            |
| A100-PCIE-40GB              | 30%                           | 5%                            |
| A100-SXM4-80GB              | 30%                           | 5%                            |
| A10G                        | 30%                           | 5%                            |
| A16                         | 30%                           | 5%                            |
| A40                         | 30%                           | 5%                            |
| GeForce GTX 1080 Ti         | 30%                           | 20%                           |
| GeForce RTX 2080 Ti         | 30%                           | 20%                           |
| GeForce RTX 3050            | 30%                           | 20%                           |
| GeForce RTX 3060            | 30%                           | 20%                           |
| GeForce RTX 3060 Ti         | 30%                           | 20%                           |
| GeForce RTX 3070            | 30%                           | 20%                           |
| GeForce RTX 3070 Ti         | 30%                           | 20%                           |
| GeForce RTX 3080            | 30%                           | 20%                           |
| GeForce RTX 3080 Ti         | 30%                           | 20%                           |
| GeForce RTX 3090            | 30%                           | 20%                           |
| GeForce RTX 3090 Ti         | 30%                           | 20%                           |
| GeForce RTX 4060            | 30%                           | 20%                           |
| GeForce RTX 4060 Ti         | 30%                           | 20%                           |
| GeForce RTX 4070            | 30%                           | 20%                           |
| GeForce RTX 4070 Ti         | 30%                           | 20%                           |
| GeForce RTX 4080            | 30%                           | 20%                           |
| GeForce RTX 4090            | 30%                           | 5%                            |
| GeForce RTX 4090 D          | 30%                           | 5%                            |
| GeForce RTX 5090            | 30%                           | 5%                            |
| H100 80GB HBM3              | 30%                           | 5%                            |
| H100 PCIe                   | 30%                           | 5%                            |
| H200                        | 30%                           | 5%                            |
| L4                          | 30%                           | 5%                            |
| L40                         | 30%                           | 5%                            |
| RTX 4000                    | 30%                           | 20%                           |
| RTX 4000 SFF Ada Generation | 30%                           | 20%                           |
| RTX 5000                    | 30%                           | 20%                           |
| RTX 5000 Ada Generation     | 30%                           | 5%                            |
| RTX 6000 Ada Generation     | 30%                           | 5%                            |
| RTX A4000                   | 30%                           | 20%                           |
| RTX A5000                   | 30%                           | 20%                           |
| RTX A6000                   | 30%                           | 5%                            |
| Tesla T4                    | 30%                           | 5%                            |
| Tesla V100-PCIE-16GB        | 30%                           | 5%                            |
| Tesla V100-PCIE-32GB        | 30%                           | 5%                            |
| Tesla V100-SXM2-16GB        | 30%                           | 5%                            |
| Tesla V100-SXM2-32GB        | 30%                           | 5%                            |
| Tesla V100S-PCIE-32GB       | 30%                           | 5%                            |
| M3                          | 30%                           | N/A                           |
| M3 Max                      | 30%                           | N/A                           |
| M3 Pro                      | 30%                           | N/A                           |
| M4                          | 30%                           | N/A                           |
| M4 Max                      | 30%                           | N/A                           |
| M4 Pro                      | 30%                           | N/A                           |


# Docker Not Installed or Running
Source: https://io.net/docs/guides/workers/docker-not-installed-or-running

This issue can occur if Docker is not installed or if the user is not added to the Docker group. Here's how to troubleshoot:

1. **Check if Docker is installed.** Run the following command:

   ```
   docker info
   ```

   Sample output:

   ```
   Client:
    Context: default
    Debug mode: false
    Servers:
     default:
       Host: localhost
       Engine:
         Version: 20.10.14
         API version: 1.44
         Go version: go1.17.15
         Git commit: 8668127
         Built: Thu Apr 1 06:02:55 2021
         OS/Arch: linux/amd64
         Experimental: false
       Kernel: 5.15.0-52-generic
       Operating System: Ubuntu 22.04.1 LTS
       Total Memory: 31.8GiB
       CPUs: 8
   ```

   If you see this output, **Docker is installed,** but the user may not be added to the Docker group.

2. **Check if the user is in the Docker group.** Run the following command:

   ```
   grep -i docker /etc/group
   ```

   Sample output:

   ```
   docker:x:999:root,$USER1,$USER2,etc
   ```

   Verify if your username is listed. If not, add the user to the Docker group:

3. **Add user to the Docker group:**

   ```
   sudo usermod -aG docker $USER
   ```

   Example:

   ```
   sudo usermod -aG docker Michael
   ```

4. **Verify the user is added.** Re-run the group check:

   ```
   grep -i docker /etc/group
   ```

   The output should now include your username, e.g.:

   ```
   docker:x:999:root,michael
   ```

5. **Reboot the server:**
   ```
   sudo reboot
   ```

6. Once logged back in, **restart Docker**:
   ```
   sudo systemctl restart docker
   ```

7. If no output is shown when running **docker info**, suggest downloading and [installing Docker properly](/guides/workers/install-on-ubuntu).


# Earnings & Rewards
Source: https://io.net/docs/guides/workers/earnings-rewards

The Earnings & Rewards tab provides transparency and granular insights into your earnings and the jobs your devices have served.

### Earnings and Rewards Tab

To access the Earnings and Rewards tab, go to IO Worker and click the **Earnings & Rewards** tab in the upper-left corner.

<Frame>
  <img alt="" />
</Frame>

### Rewards and Jobs

* Earnings from Block Rewards in \$IO coins
* Earnings from Jobs in \$IO coins
* Total time your workers were active.
* Number of jobs processed by your workers.

<Frame>
  <img alt="" />
</Frame>

### Daily Block Rewards

The graph displays your daily earnings in \$IO coins from Block Rewards. Below the graph, you can see:

* Total Blocks Earned
* Total Blocks Failed

<Frame>
  <img alt="" />
</Frame>

### Daily Earnings

In the top-right corner of the chart, you can **switch to the Earnings chart.** This graph displays your daily earnings in \$IO coins from common jobs performed by your workers. Below the graph, you can find:

* Total Compute Hours Served
* Earned vs. Slashed
* Total Compute Jobs

<Frame>
  <img alt="" />
</Frame>

### Clusters

The list shows the clusters your workers are part of and provides detailed earnings information, including:

* Earnings in \$IO coins
* Projected Max Earnings
* Total Slashed

Click on a specific cluster to view its details. You can also search by Cluster ID to find information for that cluster.

<Frame>
  <img alt="" />
</Frame>

### Job Payments

**Important**: If the job is completed within a day, **payment is made immediately**. For jobs that last multiple days, **payment is made at the end of each day**. A few points:

* If your Worker participated in a job and remained available throughout, it **will receive payment**.
* If the Worker was **unavailable** during the cluster process, it **will not receive payment for the whole time**.
* If the Worker **stops within the first hour** of connection, **no payment will be made for that time**.

You can search for a transaction by entering the Job ID number and filter transactions by date within any permitted period. Clicking on a specific transaction will open a page with detailed information about it.

<Frame>
  <img alt="" />
</Frame>

### View Transactions

The transaction page shows: Amount and type of currency received

* Transaction type
* Platform used
* Status
* Date
* Transaction ID

<Frame>
  <img alt="" />
</Frame>


# MacOS: Install Docker
Source: https://io.net/docs/guides/workers/install-docker-on-macos

A step-by-step guide for installing Docker on MacOS-based machines.

<iframe title="Docker Guide for MacOS" />

### What is Docker?

Let's take a quick look at what Docker is? Imagine Docker as a magic box where you put your software and everything it needs to run. This box can be easily carried to any computer, and when you open it, your software works just the way you packed it, without needing anything extra from that computer. Here are a few steps to install Docker:

### 1. Download Docker

Go to the [Docker website](https://www.docker.com/products/docker-desktop/) and click on "**Download for Mac - Apple Chip.**"

Downloading the Docker file may take some time. Please be patient.

<Frame>
  <img alt="" />
</Frame>

### 2. Open the docker.dmg File and Drag It Into the Applications Folder

<Frame>
  <img alt="" />
</Frame>

### 3. Start the Docker Installation From the Applications Folder

We recommend using the recommended settings during the installation wizard.

<Frame>
  <img alt="" />
</Frame>

### 4. Open  Terminal Through Launchpad

Click the Launchpad icon in the Dock, type Terminal in the search field, then click Terminal

<Frame>
  <img alt="" />
</Frame>

### 5. Verify the Installation in Terminal

<Frame>
  <img alt="" />
</Frame>

Copy and paste the following line into Terminal.

<CodeGroup>
  ```Text Terminal Command theme={null}
  docker --version
  ```
</CodeGroup>

The result will be the current version of Docker.

```
Docker version 24.0.6, build ed223bc
```

### Expanding Virtual Disk Limit

1. Click **Settings**.
2. Go to **Resources** on the left nav.

   <Frame>
     <img alt={true} />
   </Frame>
3. Check the amount of space shown under **Virtual disk limit**. **Note:** Docker does not natively assign all of your disk space.

   <Frame>
     <img alt="" />
   </Frame>
4. Drag the slider to your desired virtual disk limit amount.
5. Click **Apply & restart**.

### Congratulations on Successfully Setting up Docker

Now that Docker has been successfully installed and is running, you can proceed with [setting up the Worker](/guides/workers/install-on-macos).

<Info>
  Feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>


# Windows: Install Docker
Source: https://io.net/docs/guides/workers/install-docker-on-windows

A step-by-step guide for installing Docker on Windows-based machines

<iframe title="Docker Guide for Windows" />

### What is Docker?

Let's take a quick look at what **Docker** is? Imagine Docker as a magic box where you put your software and everything it needs to run. This box can be easily carried to any computer, and when you open it, your software works just the way you packed it, without needing anything extra from that computer. Here are a few steps to install Docker:

<Danger>
  **Network Capability Issue on Docker Desktop for Windows**

  We are currently investigating a network performance issue with Docker Desktop on Windows. This might be due to Docker's overhead, and we are exploring potential fixes.

  **Recommendation**: \
  If you experience this issue, we recommend switching to Linux as a temporary workaround.

  Thank you for your understanding and patience.
</Danger>

### First, verify that Virtualization is Enabled on your Computer.

To verify if virtualization is enabled, open **Task Manager** by pressing Ctrl+Alt+Del. Select "**Performance**" and then click on the "**CPU**" tab to view the information in the bottom right corner, as shown in the image below:

<Frame>
  <img alt="" />
</Frame>

<Warning>
  If it's not enabled, follow these steps:
</Warning>

1. To enable virtualization technology in your BIOS or UEFI settings, you need to access your computer's BIOS or UEFI configuration menu during the boot process. The specific steps can vary depending on your computer's manufacturer and model, but here are the general steps to enable virtualization.
2. Install WSL 2 by opening the PowerShell as an Administrator. To do this, search for "PowerShell" in the Start menu, right-click on "Windows PowerShell," and select "Run as administrator."
3. Run the following command to enable the WSL feature in **Windows 10/11** in Terminal:

   <CodeGroup>
     ```Text Terminal Command theme={null}
     dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
     ```
   </CodeGroup>
4. Then **Enable** the Virtual Machine Platform Feature while still in the same PowerShell window by running the following command:

   <CodeGroup>
     ```Text Terminal Command theme={null}
     dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
     ```
   </CodeGroup>
5. Then set WSL 2 as the Default Version (you might be required to restart your machine sometimes):

   <CodeGroup>
     ```Text Terminal Command theme={null}
     wsl --set-default-version 2
     ```
   </CodeGroup>

### 1. Download Docker

Go to the [Docker website](https://www.docker.com/products/docker-desktop/) and click on "**Download for Windows**." Downloading the Docker file may take some time. Please be patient.

<Frame>
  <img alt="" />
</Frame>

### 2. Run the Installation Process

The installation starts when you open the file. Follow the prompts. When the installation process is completed, you need to **restart your computer.** Just click the "**Close and Restart**" button on the last step of the Docker wizard:

<Frame>
  <img alt="" />
</Frame>

After rebooting, open Docker and use the recommended settings from the installation wizard:

<Frame>
  <img alt="" />
</Frame>

### 3. Configure WSL2  to Integrate with Docker Settings

Open the Docker settings. In the Resources section, choose <Tooltip>WSL 2</Tooltip> Integration and check the box for <Tooltip>WSL 2</Tooltip> to integrate.

<Frame>
  <img alt="" />
</Frame>

### 4. Open Terminal Through Start Menu

Click the Start Menu icon in the Popup Menu, type Terminal in the search field, then click Terminal

<Frame>
  <img alt="" />
</Frame>

### 5. Verify the Installation in Terminal

<Frame>
  <img alt="" />
</Frame>

Copy and paste the following line into Terminal.

<CodeGroup>
  ```Text Terminal Command theme={null}
  docker --version
  ```
</CodeGroup>

The result will be the current version of Docker.

```
Docker version 24.0.6, build ed223bc
```

### Congratulations on Successfully Setting up Docker

Now that Docker has been successfully installed and is running, you can proceed with [setting up the Worker](/guides/workers/install-on-windows).

<Info>
  If you encounter issues with Docker, please refer to our [Troubleshooting Docker guide](/guides/workers/troubleshoot-docker). If the problem persists or if you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>


# Install Nvidia Drivers
Source: https://io.net/docs/guides/workers/install-nvidia-drivers-on-windows

A step-by-step guide for installing Nvidia Drivers on Windows-based machines.

### What are Nvidia Drivers?

NVIDIA drivers are software packages that allow your computer's operating system to communicate effectively with NVIDIA graphics cards. These drivers ensure that your GPU can perform optimally, providing support for various features such as graphical rendering, video playback, and gaming performance. Keeping your NVIDIA drivers up to date is important for maintaining system stability, compatibility with new software, and obtaining the best performance from your graphics card.

### 1. Open Windows Terminal From the Start Menu

Click the Start Menu icon in the popup Menu, type Terminal in the search field, then click **Terminal**.

<Frame>
  <img alt="" />
</Frame>

### 2. Verify That the Correct Drivers Are Installed

<Frame>
  <img alt="" />
</Frame>

To check that you have the correct drivers, open a command line on your Windows PC (Windows key + R, type cmd) and type into it the following.

<CodeGroup>
  ```Text Terminal Command theme={null}
  nvidia-smi
  ```
</CodeGroup>

If you encounter the following error message:

```
C://Users>nvidia-smi  
'nvidia-smi' is not recognized as an internal or external command,  
operable program or batch file.
```

It means that you do not have NVIDIA drivers installed. To install them, follow the steps below:

### 3. Go to [Nvidia Driver](https://www.nvidia.com/download/index.aspx) Download Page

Choose your GPU's name, then click on search.

<Frame>
  <img alt="" />
</Frame>

### 4. Download the Driver Installation File

Click the **Download** button for the NVIDIA driver that matches your GPU and Windows version.

<Info>
  Driver Version 552.44 is currently the most stable & tested driver.
</Info>

<Frame>
  <img alt="" />
</Frame>

### 5. Open the .Exe File and Proceed With the Installation Process

Once the download is complete, start the installation, select the first option and click on "Agree and Continue."

<Frame>
  <img alt="" />
</Frame>

### 6. Reboot your computer

After the installation is complete, it's essential to reboot your computer. Restart your machine to ensure that the new NVIDIA driver is fully integrated into your system.

### 7. Verify the Installation Process

<Frame>
  <img alt="" />
</Frame>

After your computer reboots, open Windows Terminal from the Start Menu and enter the following command:

<CodeGroup>
  ```Text Terminal Command theme={null}
  nvidia-smi
  ```
</CodeGroup>

You should see this outcome:

```
+ — — — — — — — — — — — — — — — — — — — — — — — — + — — — — — — — — — —  +
| GPU  Name         TCC/WDDM                      | Bus-Id        Disp.A |
| Fan  Temp  Perf   Pwr:Usage/Cap                 |         Memory-Usage |
|                                                 |                      |
+ = = = = = = = = = = = = = = = = = = = = = = = = + = = = = = = = = = =  +
| 0   NVIDIA GeForce GTX 1070 Ti       WDDM       |     00000000:01:00.0 |
| 0%  53C    P8                  13W / 180W       |     503МіВ / 8192MiB |
|                                                 |                      |
+ — — — — — — — — — — — — — — — — — — — — — — — — + — — — — — — — — — —  +
| 0   NVIDIA GeForce GTX 1070 Ti       WDDM       | 00000000:02:00.0 0ff |
| 0%  49C    P8                  10W / 180W       |       OMiB / 8192MiB |
|                                                 |                      |
+ — — — — — — — — — — — — — — — — — — — — — — — — + — — — — — — — — — —  +
```

### That’s It. You Have the Nvidia Drivers Installed and Ready.

Now that CUDA Toolkit has been successfully installed and is running, you can proceed with [setting up the Worker](/guides/workers/install-on-windows).

<Info>
  Feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>


# HiveOS: Install Worker
Source: https://io.net/docs/guides/workers/install-on-hiveos

A step-by-step process for running io.net on HiveOS:

### What is HiveOS?

HiveOS is an operating system designed specifically for mining cryptocurrencies. It is optimized for mining efficiency, stability, and ease of use, offering features such as remote monitoring, management of mining rigs, and support for a variety of mining hardware. HiveOS is popular among cryptocurrency miners for its user-friendly interface, robust performance, and support for a wide range of mining algorithms and coins..

### 1. [Download the HiveOS](https://hiveon.com/install/) Version from the Hiveon Website

<Frame>
  <img alt="" />
</Frame>

### 2. Burn the HiveOS image into the hard drive of the machine you want to rent using [Etcher.io](https://etcher.balena.io/)

<Frame>
  <img alt="" />
</Frame>

### 3. Add a new worker in HiveOS

<Frame>
  <img alt="" />
</Frame>

In this step, what you are required to do is:

* Click on the plus icon on the toolbar and select **Add Worker** option.
* Enter the required information for the new worker, such as the worker name, rig type, and other details as needed.
* Save or confirm the changes to add the new worker to your account..

### 4. In the settings, enter the Rig ID and password in the rig

<Frame>
  <img alt="" />
</Frame>

### 5. Open the console from the toolbar

<Frame>
  <img alt="" />
</Frame>

Click on the Console icon in the toolbar to open the command line interface

### 6. Enter commands into the command line

**Command Line** is a tool on your computer that lets you type in commands to tell the computer what to do. Instead of clicking on things with a mouse, you write instructions, and the computer follows them. It's like talking directly to your computer using text.

<Frame>
  <img alt="" />
</Frame>

Enter the following commands in a row into the command line:

```
sudo apt-get update -y
```

```
sudo apt-get install -y gnupg1
```

```
cd ~
```

```
wget https://raw.githubusercontent.com/ionet-official/io-net-official-setup-script/main/ionet-setup.sh
```

```
chmod +x ionet-setup.sh
```

```
./ionet-setup.sh
```

```
sudo reboot
```

To check if all your graphics cards are connected, enter this additional command:

```
nvidia-smi
```

<Warning>
  When using SXM or NV Link, ensure that Fabric Manager is [installed correctly](https://docs.nvidia.com/datacenter/tesla/pdf/fabric-manager-user-guide.pdf) and enabled. This will prevent initialization issues and ensure that all GPUs are functioning properly, thereby avoiding PoW verification failures.
</Warning>

### 7. Execute the Docker command provided on the 'Connect New Device' page in your dashboard.

<Frame>
  <img alt="" />
</Frame>

### 8. Check both IO-worker-monitor and IO-worker-vc are running

```
docker ps
```

Wait for the device to indicate "Running" on the device page.

<Warning>
  If only one container appears, run the command "docker ps" again.
</Warning>

### Congratulations on successfully setting up your first Worker.

Now that your Worker has been successfully created and is running, you can track its status on the Workers page.

<Info>
  If you're having trouble installing Worker, please refer to our \[Worker troubleshooting guide]/guides/workers/troubleshoot-worker-general). If the issue persists or you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>


# Overview
Source: https://io.net/docs/guides/workers/install-on-macos

A step-by-step guide for setting up the environment for io.net on Mac OS-based machines

<iframe title="IO Worker Guide for MacOS" />

### Before Starting, Check Your Mac Processor

We currently only support **Apple chip** processors (M3, M4). All currently supported processor and video card models can be [found here](/guides/workers/supported-devices).

To check your Mac processor:

1. On your Mac, click the Apple icon in the top-left corner of the menu bar.
2. Select the **About This Mac** option.
3. If you see **Apple M3** (or higher) in the **Chip** line, it means you’re using a Mac with an Apple Silicon CPU.

<Frame>
  <img alt="" />
</Frame>

### Go to [cloud.io.net](https://worker.io.net/worker/devices)

If you have not yet created an account, you can sign up on [io.net](http://io.net) using Google, Apple ID, GitHub, Hugging Face, X, Worldcoin, or simply with a one-time password by clicking the "Login with Email" button.

<img alt="Newlogin1 Jp" />

### 1. From IO Elements Navigate to Worker Section

IO Elements serves as your new control panel for navigating the service efficiently. Click on **IO Worker** to delve deeper into its functionalities and features.

<Frame>
  <img alt="" />
</Frame>

### 2. Use "Connect New Worker" Button to Open the Wizard

If Workers have not yet been added, you can use the central button. If the screen is full of information, find the same button in the upper right corner

<Frame>
  <img alt="" />
</Frame>

### 3. Name Your Device

Click the "**Pencil**" icon to open the popup for editing the device name.

Please add a unique name for your device. An ideal format would be something like this: **My-Test-Device** 

<Frame>
  <img alt="" />
</Frame>

### 4. Select MacOS Operating System “OS”

Choose the Operating System “OS” of your device from **MacOS**, Windows or Ubuntu.

<Frame>
  <img alt="" />
</Frame>

### 5. Prerequisites for Mac

Download and install Docker Desktop for MacOS by [following the link](/docs/install-docker-on-macos).

<Info>
  It has been confirmed that some users limit the amount of system resources that IO Worker can access when performing compute verifications. Many users do not set the proper amount of device level resources available for the Docker engine. Many have used default settings or restricted the Worker’s RAM access to 8GB or lower. This would significantly impact the device capability in passing PoW. This is mostly common among Mac devices.
</Info>

<Check>
  To install Docker on MacOS computers, refer to the "[Installing Docker on MacOS](/docs/install-docker-on-macos)" instructions.
</Check>

### 6. Download and Launch IO Binary

**IO Binary** is a compiled executable file used to perform computational tasks and manage system operations. It is crucial for the smooth operation of the platform as it handles essential functions directly related to the performance and reliability of the computational resources.

<Warning>
  Do not modify or run code directly in io.net’s docker containers. This may disqualify your device from earning block rewards or being hired. If you have suggestions or ideas for custom code in our Docker containers, contact customer support to suggest them.
</Warning>

Follow the steps below to download and launch the IO binary:

1. Open the Terminal through **Launchpad**

   **Terminal** is a tool on your computer that lets you type in commands to tell the computer what to do. Instead of clicking on things with a mouse, you write instructions, and the computer follows them. It's like talking directly to your computer using text.

   Click the **Launchpad** icon in the Dock, start typing "**Terminal**" in the search field, then click the **Terminal** icon:

   <Frame>
     <img alt="" />
   </Frame>
2. Download the IO Binary for MacOS using the following link in the Terminal:

   ```
   curl -L https://github.com/ionet-official/io_launch_binaries/raw/main/io_net_launch_binary_mac -o io_net_launch_binary_mac
   ```
3. Grant permissions to the new IO Binary with this command:

   ```
   chmod +x io_net_launch_binary_mac
   ```

   <Frame>
     <img alt="" />
   </Frame>
4. Copy generated the IO Binary address provided in the wizard and past it into Terminal to run further:

   ```
   ./io_net_launch_binary_mac
   ```

   <Info>
     To disable sleep mode for a device, pass the --disable\_sleep\_mode=true argument at the end of the command line.

     ```
     ./io_net_launch_binary_mac --disable_sleep_mode=true
     ```

     You can find more additional arguments to use with the IO Binary command [here](https://github.com/ionet-official/io_launch_binaries?tab=readme-ov-file#usage).
   </Info>

   <Frame>
     <img alt="" />
   </Frame>

### 7. Authorize Your New Device

The IO Binary may prompt you to authorize your new device.

<Info>
  Remember, you have 3+ minutes to complete the authorization of the device. If you miss it, rerun the code again.
</Info>

You can do this in two ways:

1. **Copy the Link from the Terminal**:

   <Frame>
     <img alt="" />
   </Frame>

   Paste it into your browser and confirm the action. After confirmation, the system will prompt you to log in.

   <Frame>
     <img alt="" />
   </Frame>
2. **Copy the Code from the Terminal**:

   <Frame>
     <img alt="" />
   </Frame>

   Enter this code on the page [https://auth0.io.solutions/activate](https://auth0.io.solutions/activate) to authorize the device. You will be prompted to log in.

   <Frame>
     <img alt="" />
   </Frame>

<Info>
  **Onboard Multiple Devices by Bypassing Interactive Authentication**

  To onboard a new device, use the following command with the **--token** flag:

  <Frame>
    <img alt="" />
  </Frame>

  ```
  ./io_net_launch_binary_mac --token your-token-value
  ```

  This will allow you to bypass the interactive authentication process.
</Info>

### 8. Remove previously installed Docker containers

<Tooltip>IO Binary</Tooltip> will ask you questions related to previously installed Docker Containers. To continue the installation of <Tooltip>IO Worker</Tooltip>, you must agree to remove all old containers and proceed by typing: **Yes**

<Frame>
  <img alt="" />
</Frame>

### 9. Wait for Worker Connection to Complete

IO Binary will install all additional containers and images for your Docker. The process may take some time to complete as it installs additional packages for Docker. Please allow the installation process to finish.

<Frame>
  <img alt="" />
</Frame>

Afterward, return to the browser to complete the installation.

You may need to wait for up to 10 minutes while the device checks and connects to the IO Ecosystem. If it doesn't connect, contact customer support by logging into your [IO.Net account](https://worker.io.net).

<Frame>
  ![](https://files.readme.io/7059edf-Step13.gif)
</Frame>

<Warning>
  Please disable power-saving mode when running your devices on IO Net. Power-saving mode can impair device performance, potentially leading to failure in PoW or being classified as not providing adequate computing power.
</Warning>

### Congratulations on Successfully Setting up Your First Worker.

Now that your Worker has been successfully created and is running, you can track its status on the Workers page.

<Frame>
  <img alt="" />
</Frame>

<Info>
  If you're having trouble installing the Worker, please refer to our [MacOS Worker troubleshooting guide](/guides/workers/troubleshoot-macos-worker) or the [general Worker troubleshooting guide](/guides/workers/troubleshoot-worker-general). If the issue persists or you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>

<Warning>
  Be aware that you will be installing a 20GB size container. This contains all the packages needed to serve AI/ML apps. Everything happens inside the container, nothing within the container can access your filesystem
</Warning>


# Overview
Source: https://io.net/docs/guides/workers/install-on-ubuntu

A step-by-step guide for setting up the environment for io.net on Ubuntu-based machines.

<iframe title="IO Worker Guide for Linux" />

### Before Starting

##### 1. Open the Ubuntu Terminal through the Start Menu.

**Terminal** is a tool on your computer that lets you type in commands to tell the computer what to do. Instead of clicking on things with a mouse, you write instructions, and the computer follows them. It's like talking directly to your computer using text.

Click the **Start Menu** icon, start typing "**Terminal**" in the search field, then click the **Terminal** icon:

<Frame>
  <img alt="" />
</Frame>

##### 2. Verify Your Ubuntu Version

For Linux users, ensure that your system is running Ubuntu 20.04 or later. You can check your Ubuntu version by executing the following command in the terminal.

<Info>
  We recommend that you use Ubuntu 22.04 LTS.
</Info>

```
lsb_release -a
```

<Frame>
  <img alt="" />
</Frame>

##### 3. CPU Requirement for Linux

We currently support AMD & Intel processors. You can find all supported processor and video card models [found here](/guides/workers/supported-devices).

To check your processor type, use the following command in the terminal:

```
lscpu
```

<Frame>
  <img alt="" />
</Frame>

### Go to [cloud.io.net](https://cloud.io.net)

If you have not yet created an account, you can sign up on [io.net](http://io.net) using Google, Apple ID, GitHub, Hugging Face, X, Worldcoin, or simply with a one-time password by clicking the "Login with Email" button.

<img alt="Newlogin1 Jp" />

### 1. From IO Elements Navigate to IO Worker

IO Elements serves as your new control panel for navigating the service efficiently. Click on **IO Worker** to delve deeper into its functionalities and features.

<Frame>
  <img alt="" />
</Frame>

### 2. Use "Connect New Worker" Button to Open the Wizard

If Workers have not yet been added, you can use the central button. If the screen is full of information, find the same button in the upper right corner.

<Frame>
  <img alt="" />
</Frame>

### 3. Name Your Device

Click the "**Pencil**" icon to open the popup for editing the device name.

Please add a unique name for your device. An ideal format would be something like this: **My-Test-Device** .

<Frame>
  <img alt="" />
</Frame>

### Select Ubuntu Operating System

Choose the Operating System of your device from MacOS, Windows or **Ubuntu**.

<Frame>
  <img alt="" />
</Frame>

### 5. Select Device Type

You should choose the device type based on your task. A video card is better suited for AI tasks, while a processor is more suitable for graphic rendering.

<Tooltip>GPU</Tooltip> - This is the part of your computer or laptop that handles graphics - the video card. It's usually from Nvidea or Radeon. You can find a full list of video cards that io.net is compatible with [here](/guides/workers/supported-devices).

<Tooltip>CPU</Tooltip> - This forms the core of every smart device in our world, including your computer or laptop. Now, alongside Intel and AMD processors, Apple's processors have also joined the lineup. You can find a comprehensive list of processors compatible with io.net [here](/guides/workers/supported-devices).

<Frame>
  <img alt="" />
</Frame>

You can also verify whether your GPU or CPU is included in the list of devices supported by our service on the wizard page.

<Warning>
  If you select a GPU Worker and your device doesn't have GPU the setup will fail.
</Warning>

### 6. Prerequisites for Ubuntu - One-Time Setup for Hardware

Before proceeding, ensure you have the necessary tools installed on your Ubuntu system (**skip if Docker and NVIDIA driver are already installed and configured**).

<Info>
  Do not install and use beta drivers for Linux.
</Info>

If not, to install IO.Net Setup, follow these steps:

<Frame>
  <img alt="" />
</Frame>

1. Install the desktop IO.NET Setup Script using the installation command in the Terminal:

   ```
   curl -L https://github.com/ionet-official/io-net-official-setup-script/raw/main/ionet-setup.sh -o ionet-setup.sh
   ```

   <Warning>
     ```
     sudo apt install curl 
     ```
   </Warning>
2. Grant permissions to the new IO.NET Setup Script with this command:

   ```
   chmod +x ionet-setup.sh && ./ionet-setup.sh
   ```
3. **For systems equipped with GPUs**, wait for the system to restart. Once it has restarted, run the setup again using the command provided earlier.

<Warning>
  When using SXM or NV Link, ensure that Fabric Manager is [installed correctly](https://docs.nvidia.com/datacenter/tesla/pdf/fabric-manager-user-guide.pdf) and enabled. This will prevent initialization issues and ensure that all GPUs are functioning properly, thereby avoiding PoW verification failures.
</Warning>

<Frame>
  <img alt="" />
</Frame>

### 7. Download and Launch IO Binary

**IO Binary** is a compiled executable file used to perform computational tasks and manage system operations. It is crucial for the smooth operation of the platform as it handles essential functions directly related to the performance and reliability of the computational resources.

<Warning>
  Do not modify or run code directly in io.net’s docker containers. This may disqualify your device from earning block rewards or being hired. If you have suggestions or ideas for custom code in our Docker containers, contact customer support to suggest them.
</Warning>

In this step, follow these instructions in the Terminal:

<Frame>
  <img alt="" />
</Frame>

1. Download the IO Binary for Ubuntu using the following link:

   ```
   curl -L https://github.com/ionet-official/io_launch_binaries/raw/main/io_net_launch_binary_linux -o io_net_launch_binary_linux
   ```
2. Grant permissions to the new IO Binary with this command:

   ```
   chmod +x io_net_launch_binary_linux
   ```

   <Frame>
     <img alt="" />
   </Frame>
3. Copy generated the IO Binary address provided in the wizard and past it into Terminal to run further:

   ```
   ./io_net_launch_binary_linux
   ```

   <Info>
     If you want to disable sleep mode for a device, you can pass the --disable\_sleep\_mode=true argument at the end of the command line.

     ```
     ./io_net_launch_binary_linux --disable_sleep_mode=true
     ```

     You can find more additional arguments to use with the IO Binary command [here](https://github.com/ionet-official/io_launch_binaries?tab=readme-ov-file#usage).
   </Info>

   <Frame>
     <img alt="" />
   </Frame>

### 8. Authorize Your New Device

The IO Binary may prompt you to authorize your new device.

<Info>
  Remember, you have 3 minutes to complete the authorization of the device. If you miss it, you will need to rerun the code again.
</Info>

You can do this in two ways:

1. **Copy the Link from the Terminal**:

   <Frame>
     <img alt="" />
   </Frame>

   Paste it into your browser and confirm the action. After confirmation, the system will prompt you to log in.

   <Frame>
     <img alt="" />
   </Frame>
2. **Copy the Code from the Terminal**:

   <Frame>
     <img alt="" />
   </Frame>

   Enter this code on the page [https://auth0.io.solutions/activate](https://auth0.io.solutions/activate) to authorize the device. After it, the system will prompt you to log in.

   <Frame>
     <img alt="" />
   </Frame>

<Info>
  **Onboarding Multiple Devices by Bypassing Interactive Authentication**

  To onboard a new device, use the following command with the **--token** flag:

  <Frame>
    <img alt="" />
  </Frame>

  ```
  ./io_net_launch_binary_linux --token your-token-value
  ```

  This will allow you to bypass the interactive authentication process.
</Info>

### 9. Remove previously installed Docker containers

<Tooltip>IO Binary</Tooltip> will ask you questions related to previously installed Docker Containers. To continue the installation of <Tooltip>IO Worker</Tooltip>, you must agree to remove all old containers and proceed by typing: **Yes**

<Frame>
  <img alt="" />
</Frame>

### 10. Waiting for Worker Connection to Complete

IO Binary will install all additional containers and images for your Docker. The process may take some time to complete as it installs additional packages for Docker. Please allow the installation process to finish.

<Frame>
  <img alt="" />
</Frame>

Afterward, return to the browser to complete the installation.

You may need to wait for up to 10 minutes while the device checks and connects to the IO ecosystem. If it doesn't connect, reach out to our Support ticket by logging into your [IO.Net account](https://worker.io.net).

<Frame>
  <img alt="" />
</Frame>

<Warning>
  Please disable power-saving mode when running your devices on IO Net. Power-saving mode can impair device performance, potentially leading to failure in PoW or being classified as not providing adequate computing power.
</Warning>

### Congratulations on Successfully Setting up Your First Worker.

Now that your Worker has been successfully created and is running, you can track its status on the Workers page.

<Frame>
  <img alt="" />
</Frame>

<Info>
  If you're having trouble installing Worker, please refer to our [Worker troubleshooting guide](/guides/workers/troubleshoot-worker-general). If the issue persists or you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket
</Info>

<Warning>
  Be aware that you will be installing a 20GB size container. This contains all the packages needed to serve AI/ML apps. Everything happens inside the container, nothing within the container can access your filesystem.
</Warning>


# Overview
Source: https://io.net/docs/guides/workers/install-on-windows

A step-by-step guide for setting up the environment for io.net on Windows-based machines.

<iframe title="IO Worker Guide for Windows" />

### Go to

[cloud.io.net](https://cloud.io.net)

If you have not yet created an account, you can sign up on [io.net](http://io.net) using Google, Apple ID, GitHub, Hugging Face, X, Worldcoin, or simply with a one-time password by clicking the "Login with Email" button.

<img alt="Newlogin1 Jp" />

### 1. From IO Elements Go to IO Worker

IO Elements serves as your new control panel for navigating the service efficiently. Click on **IO Worker** to delve deeper into its functionalities and features.

<Frame>
  <img alt="" />
</Frame>

### 2. Click "Connect New Worker" to Open the Wizard

If Workers have not been added, click Connect New Worker. If the screen is full of information, find the same button in the upper right corner.

<Frame>
  <img alt="" />
</Frame>

### 3. Name Your Device

Click the "**Pencil**" icon to open the popup for editing the device name.   

Please add a unique name for your device. We suggest a format such as: **My-Test-Device** .

<Frame>
  <img alt="" />
</Frame>

### 4. Select Windows Operating System

Choose the Operating System of your device from MacOS, **Windows** or Ubuntu.

<Frame>
  <img alt="" />
</Frame>

### 5. Select Device Type

You should choose the device type based on your task. A video card is better suited for AI tasks, while a processor is more suitable for graphic rendering.

<Tooltip>GPU</Tooltip> - This is the part of your computer or laptop that handles graphics - the video card. It's usually from Nvidea or Radeon. You can find a full list of video cards that io.net is compatible with [here](/guides/workers/supported-devices).

<Tooltip>CPU</Tooltip> - This forms the core of every smart device in our world, including your computer or laptop. Now, alongside Intel and AMD processors, Apple's processors have also joined the lineup. You can find a comprehensive list of processors compatible with io.net [here](/guides/workers/supported-devices).

<Frame>
  <img alt="" />
</Frame>

You can also verify whether your GPU or CPU is included in the list of devices supported by our service on the wizard page.

<Warning>
  If you choose <Tooltip>GPU</Tooltip> .Worker and your device doesn't have GPU the setup will fail
</Warning>

### 6. Prerequisites for Windows

Follow the steps below to complete the prerequisites:

<Frame>
  <img alt="" />
</Frame>

1. Download and Install Desktop <Tooltip>Docker</Tooltip>. You can find comprehensive instructions on how to install Docker for Windows in this [concise guide](/guides/workers/install-docker-on-windows).
2. Then Download and Setup <Tooltip>CUDA</Tooltip>. Please refer to the instructions on how to do this by [following the link](/guides/workers/cuda-toolkit-optional).
3. Afterward (if needed or if not done yet), you'll need to install or update the correct <Tooltip>NVIDIA driver</Tooltip> for your video card. You can find instructions on how to do this [here](/guides/workers/install-nvidia-drivers-on-windows) .

<Warning>
  When using SXM or NV Link, ensure that Fabric Manager is installed correctly and enabled. This will prevent initialization issues and ensure that all <Tooltip>GPU</Tooltip>s are functioning properly, thereby avoiding PoW verification failures.
</Warning>

### 7. Download and Launch IO Binary

**IO Binary** is a compiled executable file used to perform computational tasks and manage system operations. It is crucial for the operation of the platform as it handles essential functions directly related to the performance and reliability of computational resources.

<Warning>
  Do not modify or run code directly in io.net’s docker containers. This may disqualify your device from earning block rewards or being hired. If you have suggestions or ideas for custom code in our Docker containers, contact customer support to suggest them.
</Warning>

In this step, what you are required to do is:

1. **Download the Executable File:** Copy the URL below, open your browser, and paste it. The browser downloads the executable file to your computer. **It's recommended to download the IO Binary again, as we often update versions for improvements.**

   ```
   https://github.com/ionet-official/io_launch_binaries/raw/main/io_net_launch_binary_windows.exe
   ```

   <Frame>
     <img alt="" />
   </Frame>
2. **Open IO Binary file into Terminal**

   **Terminal** is a tool on your computer that allows you enter commands to tell the computer what to do. Instead of clicking on elements with a mouse, you write instructions, and the computer follows them. It's like talking directly to your computer using text.

   * Click the **Start Menu** icon, then find and select the **Terminal** app from the popup menu.

     <Frame>
       <img alt="" />
     </Frame>
   * In the **Terminal**, navigate to the **Downloads** folder by typing the command to go to the folder with the IO Binary.

     ```
     cd Downloads
     ```
   * Next, copy the command from your new worker page to launch the IO Binary.

     <Frame>
       <img alt="" />
     </Frame>

     Then paste it into the terminal and press Enter to run it.

   <Frame>
     <img alt="" />
   </Frame>

### 8. Authorize Your New Device

The <Tooltip>IO Binary</Tooltip> may prompt you to authorize your new device.

<Info>
  Remember, you have about 3 minutes to complete the authorization of the device. If you miss it, you will need to rerun the code again.
</Info>

You can do this in two ways:

1. **Copy the Link from the Terminal**:

   <Frame>
     <img alt="" />
   </Frame>

   Paste it into your browser and confirm the action. After confirmation, the system will prompt you to log in.

   <Frame>
     <img alt="" />
   </Frame>
2. **Copy the Code from the Terminal**:

   <Frame>
     <img alt="" />
   </Frame>

   Enter this code on the page [https://auth0.io.solutions/activate](https://auth0.io.solutions/activate) to authorize the device. After it, the system will prompt you to log in.

   <Frame>
     <img alt="" />
   </Frame>

<Info>
  **Onboard Multiple Devices by Bypassing Interactive Authentication**

  After you authenticate once, you can bypass the interactive auth process when you join additional devices. To do this, run the binary with an additional argument, the **--token** flag, followed by the token value.

  In the Command Prompt, copy your token and pass the --token flag, followed by the token and run the binary.

  <Frame>
    <img alt="" />
  </Frame>

  ```
  io_net_launch_binary_windows.exe --token your-token-value
  ```

  Tokens are valid for 12 months.
</Info>

### 9. Remove Previously Installed Docker Containers

<Tooltip>IO Binary</Tooltip> will ask you questions related to previously installed Docker Containers. To continue the installation of <Tooltip>IO Worker</Tooltip>, you must agree to remove all old containers and proceed by typing: **Yes**

<Frame>
  <img alt="" />
</Frame>

### 11. Wait for Worker Connection to Complete

The IO Binary will installs all additional containers and images for your Docker. The process may take some time to complete as it installs additional packages for Docker. Please allow the installation process to finish.

<Frame>
  <img alt="" />
</Frame>

Afterward, return to the browser to complete the installation.

You may need to wait for up to 10 minutes while the device checks and connects to the IO Ecosystem. If it doesn't connect, reach out to our Support ticket by logging into your [IO.Net account](https://worker.io.net).

<Frame>
  <img alt="" />
</Frame>

<Warning>
  Please disable power-saving mode when running your devices on IO Net. Power-saving mode can impair device performance, potentially leading to failure in PoW or being classified as not providing adequate computing power.
</Warning>

### Congratulations on Successfully Setting up Your First Worker.

Now that your Worker has been successfully created and is running, you can track its status on the Workers page.

<Frame>
  <img alt="" />
</Frame>

<Info>
  If you're having trouble installing the Worker, please refer to our [Windows Worker troubleshooting guide](/guides/workers/troubleshoot-windows-worker) or the [general Worker troubleshooting guide](/guides/workers/troubleshoot-worker-general). If the issue persists or you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>

<Warning>
  Be aware that you will be installing a 20GB size container. This contains all the packages needed to serve AI/ML apps. Everything happens inside the container, nothing within the container can access your filesystem.
</Warning>


# Intro
Source: https://io.net/docs/guides/workers/intro



### What is IO Worker?

IO Worker is like having a virtual rental manager for your device. It's a simple web app that lets you lend your computing power to those tackling AI tasks, making it easier for everyone to access the resources they need.

Thanks to our decentralized setup and smart resource management, you can earn more by renting out your GPU/CPU than you would with traditional cloud services. It's a win-win situation where you support others while boosting your own earnings.

With io.net, you're not just renting out hardware; you're part of a community that values collaboration and efficiency. Whether you're a business looking to optimize resources or an individual keen on making extra profits, io.net has got you covered.

### Key Features

* **Decentralized Compute Power:** IO Workers enable access to a distributed network of GPUs and CPUs, providing the computational resources users need.
* **Cost-Efficiency:** By leveraging IO Workers, users can benefit from cost-effective compute resources. The decentralized nature of the network optimizes costs, reduces latency, and provides scalable compute capabilities.
* **Scalability:** IO Workers offer flexibility, allowing users to scale their computational resources based on demand. This ensures efficient handling of varying workloads.
* **Real-Time Monitoring:** Users can monitor the performance of IO Workers in real-time, tracking metrics such as uptime, resource utilization, and job completion rates for efficient management and optimization.
* **Secure Resource Sharing:** IO Workers facilitate secure resource sharing among network participants. Users maintain control over access and usage while sharing their compute resources securely.
* **Global Accessibility:** IO Workers provide global accessibility, allowing users from different regions and industries to access and utilize decentralized compute power seamlessly.

### IO Worker Integration Flow

The diagram below illustrates the general integration process of an IO Worker into the IO.NET ecosystem — from setting up required components to successfully connecting your device to the network. It provides a clear overview of the key steps involved in configuration and deployment.

<Frame>
  <img alt="" />
</Frame>

### Create Account

To create an account, go to [worker.io.net](https://worker.io.net/). Currently, you can sign up using Google, Apple ID, X, or Worldcoin. Choose your preferred option, click **Sign Up**, and you're all set to join us.

#### Go to [worker.io.net](https://worker.io.net)

<Frame>
  <img alt="" />
</Frame>

<Info>
  Feel free to [check our knowledge](https://support.io.net/en/support/home) base for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>


# Overview
Source: https://io.net/docs/guides/workers/io-worker



<Frame>
  <img alt="WORKER Pn" />
</Frame>

## IO Worker Development Principles

We recognize the pivotal role IO Worker and Suppliers are providing required computing power play in our ecosystem. As such, our IO Worker portal is meticulously crafted to cater to the unique needs of our suppliers, emphasizing real-time updates, stringent security, streamlined operations, and user-friendly interfaces.

### I. Full Financial Control

Real-time Earnings Overview. We are staunch advocates for complete financial transparency. Through our portal, suppliers gain real-time access to their earnings and financial metrics. Leveraging the capabilities of ReactJS and a Fast API backend layer, we guarantee that the financial data displayed remains current, empowering suppliers to make decisions grounded in the latest figures. No more delays or uncertainties – you witness your earnings in real-time. Our Billing/Usage Monitoring layer ensures meticulous oversight.

### II. Ease of Management

Simplified GPU Integration. Time is of the essence, and we recognize its value. That's precisely why we've simplified the GPU addition process on our platform. Suppliers are spared the hassle of navigating intricate setups or configurations. Add your GPU, and our system seamlessly integrates the rest with our advanced tech stack. This approach allows suppliers to concentrate on their core competencies while we manage the technical orchestration.

We employ state-of-the-art orchestration tools, including Kubernetes, Prefect, and Apache Airflow, to ensure a swift and reliable deployment process.

### III. Efficient Resource Use

Optimized GPU Utilization. In the GPU supply landscape, unutilized resources represent lost potential. Our platform is meticulously crafted to optimize the use of GPUs supplied by our partners. Through smart task allocation and workload management, facilitated by our Fault Monitoring/Reporting/Analytics layers, we ensure GPUs are neither overwhelmed nor underutilized. This strategy enhances profitability and guarantees a consistent revenue flow for our suppliers.

### IV. Real-time Monitoring

Stay Informed. Miners have the capability to monitor their GPU usage in real time on our platform, ensuring unparalleled transparency and clarity. Our platform offers a holistic view, from intricate GPU performance metrics to detailed earnings breakdowns. This comprehensive overview empowers miners to closely track their returns and guarantees that their hardware is utilized to its fullest potential. To further enhance this, our Analytics Layer provides deeper insights and trends.

### V. Security & Stability

Protected Assets. The GPUs that miners rent out are invaluable assets. Recognizing this, our platform is reinforced with stringent security protocols to safeguard the hardware and the associated earnings. Stability is a cornerstone of our service. We are committed to ensuring that the GPU renting process remains seamless, marked by consistent uptime and unwavering performance. Our Fault Monitoring Layer actively oversees and ensures system health to bolster this commitment.


# Manage, Monitor, & FAQs
Source: https://io.net/docs/guides/workers/manage-and-monitor



### Worker Details

The **Device View** page provides a comprehensive overview of the device's details. io.net presents real-time data on transmitted traffic, connection status, and uptime history.

Users can monitor the status of all active services on the device and activate additional ones by purchasing io.coins. By default, these services are automatically linked to the worker:

* IO Version Control
* IO Monitor
* Ray.io

Equally important is the device's current/past tasks and its complete notification history, conveniently accessible through the corresponding tabs after 'Services' tab.

The worker detail page displays the following information:

* List of Jobs and status
* Uptime Graph
* Type of GPU/CPU
* Uptime Percentage
* Remaining Compute Hours
* Daily block Rewards Earnings
* Connectivity Tier
* Notifications

<Frame>
  <img alt="" />
</Frame>

### FAQs

<AccordionGroup>
  <Accordion title="Q: My graphics card is sufficient, but my internet or RAM is not enough. Can I still receive airdrop rewards?">
    Yes, you can still receive rewards by running your Worker properly, although not as much as those who meet all the requirements and get jobs.
  </Accordion>

  <Accordion title="Q: I have followed all the steps correctly, but my Worker is not visible on the website. What should I do?">
    If you've [completed all the steps](/docs/install-on-macos) in the guide and your Worker is still not visible, you can create a ticket in the #support-tickets channel on the [Discord](https://discord.gg/ionetofficial) server for assistance.
  </Accordion>

  <Accordion title="Q: Should I keep my computer on 24/7?">
    For maximum airdrop rewards and system stability, it's recommended to keep your computer running continuously. You can "pause" the system in emergencies, but extended periods of downtime may result in suspension.
  </Accordion>

  <Accordion title="Q: Can I participate using a VPS?">
    It is not recommended due to both the cost and potential issues it may cause.
  </Accordion>

  <Accordion title="Q: My Worker status shows 'Idle' - is this a problem?">
    No, "Idle" status means your Worker is not currently receiving jobs. There's no issue with your system in this state.
  </Accordion>
</AccordionGroup>

<Info>
  If you're seeking answers to other technical questions related to Worker, please refer to the [Troubleshoots Worker page](/guides/workers/troubleshoot-worker-general).
</Info>


# Optimize PCIe Lane Configuration
Source: https://io.net/docs/guides/workers/optimize-pcie-lane-configuration

When onboarding new devices into the IO.NET network, it’s essential to review the hardware installed and ensure that it is fully capable of performing as expected. We recommend verifying that your hardware supports the required PCIe (Peripheral Component Interconnect Express) lanes. PCIe lanes are the fundamental building blocks of a PCIe connection, enabling communication between a device and the CPU.

## Locate PCIe Lanes for Your CPU

To ensure optimal performance and stability, it’s recommended that your device's CPU be capable of providing the number of PCIe lanes required for the hardware installed. The number of PCIe lanes required varies depending on the number of PCIe hardware components installed on your motherboard.

### Locate The Number of PCIe Lanes for Your CPU

* For Intel CPUs, search Intel Ark for your CPU model and look for “Max # of PCI Express Lanes” (here’s an example for the Intel Core i9 14900k, which provides 20x PCIe lanes).
* For AMD CPUs, search AMD’s Processor Specifications site for your model to find PCI Express versions.

| Device Type               | PCIe Lane Requirements                                                                                                                                                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GPUs**                  | • Consumer-grade GPUs (ex: NVIDIA 30-series, 40-series) → **8 PCIe lanes por GPU**, usar slot **x8** <br /> • Enterprise-grade GPUs (ex: NVIDIA H100, A100) → **16 PCIe lanes por GPU**, usar slot **x16**                 |
| **SATA SSDs & NVMe SSDs** | • SATA SSDs → **2 PCIe lanes por device** <br /> • NVMe SSDs → **4–8 PCIe lanes por device**, depende da geração (Gen4, Gen5) e do limite da placa-mãe                                                                     |
| **Other Devices**         | • Network Adapters (1Gbps, 10Gbps) → **4–8 PCIe lanes** <br /> • Sound cards → **4–8 PCIe lanes** <br /> • Storage expansion cards & HBAs → **8–16 PCIe lanes** (ex: placas para múltiplos NVMe SSDs ou configuração JBOD) |

<Info>
  Note: We strongly recommend removing all PCI devices that are not a GPU, Storage Device, or Network Adapter from your system. These devices won’t be used, and they will reduce the number of PCIe lanes available for other critical components.
</Info>

### Configure PCIe Lane Width

To ensure that each of your GPUs performs optimally, we strongly recommend configuring the PCIe Lane Width for each GPU to match the number of PCIe lanes required and avoid mixing lane widths.

Configuring PCIe Lane Width varies by motherboard manufacturer. Consult your motherboard manufacturer's manual for detailed guidance.

### PCIe Lane Width Configuration Example

Using 4x NVIDIA RTX 4090s, each of which requires 8x PCIe lanes (for a total of 32 PCIe lanes), each GPU should be configured to use an x8 PCI Lane Width in the motherboard BIOS. This will ensure that each of the 4090s can perform as expected.

<Info>
  Note: We recommend all GPUs installed on your device use the same PCI Lane Width. In the example above, each of the 4090s should be set to use an x8 PCI Lane Width (as they are consumer GPUs). If your motherboard cannot match PCI Lane Widths for each GPU installed, we recommend reducing the number of GPUs installed on the device to ensure optimal performance.
</Info>

### PCIe Riser Cables

Riser Cables (GPU Risers) insert directly into PCIe slots on the motherboard and allow you to install more GPUs on your device than possible due to the size of modern GPUs and the limited space available on modern motherboards.

If using Riser Cables, ensure they are labeled as x8 or x16 (depending on your GPU model). Avoid risers that split PCIe lanes (bifurcate) into x1, x2, or x4 slots, as these cannot deliver the required performance and may reduce system stability.


# Proof of Work
Source: https://io.net/docs/guides/workers/proof-of-work

io.net is committed to providing a reliable and trustworthy platform for distributed CPU/GPU resources. A key challenge in a decentralized network is to ensure that the computational resources offered by suppliers are genuine and perform as intended. We actively verify the authenticity and reliability of the network by implementing an hourly Proof-of-Work (PoW) verification process.

### What is Proof-of-Work?

Proof-of-Work is a cryptographic puzzle that requires significant computational resources to solve. It’s easy to verify the authenticity of a GPU/CPU after they successfully solve the puzzle. Our PoW algorithm leverages an industry-standard approach to verify computational resources, similar to the approaches used in cryptocurrencies such as Ethereum, prior to its Proof-of-Stake upgrade, and Bitcoin.

### Why Is This Necessary?

1. **Authenticity Verification**: PoW verifies that suppliers provide real and functional CPU/GPU resources rather than simulated or virtual environments.
2. **Performance Validation**: By requiring devices to solve complex puzzles, we can verify that they perform at the level claimed by the supplier.
3. **Fraud Prevention**: This mechanism makes it difficult and economically unfeasible for malicious actors to fake or overstate their computational capacity.
4. **Quality Assurance**: Regular PoW checks help maintain the overall quality and reliability of the io.net network.
5. **Fair Resource Allocation**: By verifying the authenticity and performance of resources, we ensure fair pricing and allocation for users hiring computational power.

Our hourly PoW process runs in the background, causing minimal disruption to normal operations while continuously ensuring the integrity of our network. Suppliers can expect some load on their devices normally for no more than 15 mins per hour to complete the hourly Proof-of-Work authentication process.

<Info>
  When you onboard your device into the io.net network, the device’s full capacity should be available to potential customers. If your device's computational capacity is compromised when connected to our platform, it might disqualify you from rewards and being hired. Please note that we expect resources including VRAM to be fully available while your device is made available on io.net.
</Info>

### The PoW Process

There are three parts in this process:

* **Binary Checker API:** This is a tool that helps us solve the puzzle. It checks if a solution meets the puzzle's requirements.
* **Challenges API**: These are the puzzles themselves. It involves finding a number that fits a specific pattern, such as having a certain number of zeros at the beginning.
* **Results Submission API**: Once we find a solution, we submit it to the system to check if it's correct.

Here's how it works in simple steps:

1. The **Binary Checker** receives a puzzle and attempts to find a solution (called a nonce) that fits the puzzle's pattern.
2. The system verifies that the device has the reported amount of VRAM to prevent devices with similar hash rates from misrepresenting their capacity.
3. When a solution is found, it sends it to the system for verification.
4. The system verifies that the solution matches the puzzle's requirements. For example, containing a specific number of zeros at the beginning.
5. If the solution matches the requirements, the system records this as a successful solution. The device has passed PoW challenge.

We have a monitoring system that regularly checks for new puzzles, finds solutions, and submits them for verification.

### Is My Device Verified?

There are two visible aspects of Proof of Work (PoW) in our system:

1. Users can directly see on their device page whether their device is **Verified** or **Not Verified**:

   Verified devices are indicated by a blue icon located underneath the name of your device:

   <Frame>
     <img alt="" />
   </Frame>

   Devices that are awaiting verification have a gray mark:

   <Frame>
     <img alt="" />
   </Frame>

   Verification Failed have a red label:

   <Frame>
     <img alt="" />
   </Frame>

### What Happens if Proof-of-Work Fails?

If Proof-of-Work fails on your device, you may find your device tagged **Verification Failed** and/or **Not Block Reward Ready.**

<Frame>
  <img alt="" />
</Frame>

You can use our [`Proof-of-Work logs`](https://pow-logs.io.solutions/) to troubleshoot any potential issues by searching for your device ID to view any errors that occurred during the hourly Proof-of-Work challenges. Please download logs corresponding to where PoW failure took please and either use grep if you are familiar with command line tools (recommended) or use Microsoft Excel to search for your device ID.

**Common errors you might encounter in the PoW log include:**

* If you find an **empty list passed** error: This is often caused by a CUDA memory allocation error. Your device might be occupied by some other jobs, Please check and stop using the device for other purposes when it's available on the IO platform.
* If you find a **wrong answer** error: Your device failed the PoW test. You may want to delete all containers, download the latest launcher, and restart the onboarding process following our documentation.
* If you find a **timeout** error: Due to the inherent indeterminacy of PoW, there is a slight chance that your device might fail a PoW test even if it's correctly configured. Mostly likely, if you repeat the setup process, it will pass PoW.

**Common issue that can cause errors:**

* If you run your devices on deprecated drivers or CUDA versions (in case of Nvidia Graphics cards).
* If you have more than 3 GPUs in your setup, we recommend running your device on Linux because there are intermittent issues with multi-card setups on Windows platforms. PoW tests have a high probability of failing in this instance.

If you use Linux, you can run a self-check binary to troubleshoot your devices. A successful self-check does not guarantee that your device will pass PoW; however, your device is highly unlikely to pass PoW if self-check returns any errors. This binary also works on Windows WSL2: [https://github.com/ionet-official/io-net-official-setup-script/releases/](https://github.com/ionet-official/io-net-official-setup-script/releases/).

<Info>
  Encountering problems? Feel free to open a support ticket by logging into [your IO.Net account](https://worker.io.net) and submitting a ticket.
</Info>


# Quick Start Guide
Source: https://io.net/docs/guides/workers/quick-start-guide

Get started with IO Worker by following simple steps to create an account, connect your device, and begin earning by sharing your compute power.

### 1. Create an Account

Sign up to IO Worker using one of the following options: Google, Apple ID, X, or Worldcoin. Create your [account here](https://worker.io.net/worker/devices).

### 2. Requirements

Before installing IO Worker, make sure your system meets the following requirements:

* **Hardware Requirements**: Review the minimum hardware specifications in the [IO Device Onboarding Guide](/guides/workers/device-onboarding#requirements)
* **Supported Devices**: Ensure your device is compatible. [Check the list of supported devices here](/guides/workers/supported-devices).

Ensure your device is updated to the latest version of its operating system for the best performance and security.

### 2. Install IO Worker

Choose your system and follow the appropriate installation guide:

* MacOS: [Install Worker](/guides/workers/install-on-macos)
* Windows: [Install Worker](/guides/workers/install-on-windows) | [Install Nvidia Drivers](/guides/workers/install-nvidia-drivers-on-windows)
* Linux (Ubuntu): [Install Worker](/guides/workers/install-on-ubuntu) | [Bare Metal On-Demand Process](/guides/workers/bare-metal-on-demand-supplier-process)
* HiveOS: [Install Worker](/guides/workers/install-on-hiveos)

### 3. Configure Your Device

* Optimize Performance:
  * [Device Utilization Threshold](/guides/workers/device-utilization-threshold)
  * [Optimize PCIe Lane Configuration](/guides/workers/optimize-pcie-lane-configuration)

### 4. Start Earning

* [Proof of Work](/guides/workers/proof-of-work): IO Worker enables you to contribute your computing power to Proof of Work tasks, helping to secure decentralized networks and earn rewards.
* Understand how rewards work: [Earnings & Rewards](/guides/workers/earnings-rewards).
* Set up a wallet:
  * [Solana Wallet](/guides/workers/solana)
  * [Aptos Wallet](/guides/workers/aptos-wallet)

### 5. Manage and Monitor

* Use the [dashboard to track](/guides/manage-and-monitor):
  * Device uptime
  * Resource utilization
  * Job completion rates
* Explore FAQs for common issues: [Manage, Monitor, & FAQs](/guides/manage-and-monitor#faqs).

### 6. Troubleshooting

For system-specific troubleshooting, refer to:

* MacOS: [Troubleshoot Worker](/guides/workers/troubleshoot-macos-worker) | [Troubleshoot Docker](/guides/workers/troubleshoot-docker-for-macs)
* Windows: [Troubleshoot Worker](/guides/workers/troubleshoot-windows-worker) | [Troubleshoot Docker](/guides/workers/troubleshoot-docker-for-windows)
* Linux: [General Worker Troubleshooting](/guides/workers/troubleshoot-worker-general) | [Troubleshoot Docker](/guides/workers/troubleshoot-docker-for-linux)
* HiveOS: [General Worker Troubleshooting](/guides/workers/troubleshoot-worker-general)


# Overview
Source: https://io.net/docs/guides/workers/rewards-wallets

This document explains the financial aspects of supplying compute power to the IO network.

### Rewards and Fees

All worker earnings are paid in IO Coin. IO Coin reduces friction in our payment system, bypassing the use of escrow, past-pay billing etc. At the same time, we balance this by creating a structural demand for \$IO in the actual payment process. Every transaction in io.net creates \$IO demand because Customers pay in USDC, but Suppliers are compensated with \$IO tokens.

To learn more, see [IO Coin](https://internet-of-gpus.readme.io/docs/what-is-io-coin).

#### Supplier Rewards & Fees

* Block Rewards incur no fees.
* All worker earnings incur a 0.25% fee.

Additionally, the Proof of Work (PoW) [mechanism underpinning our ecosystem](/guides/workers/proof-of-work) ensures that each transaction contributes to the network's security and integrity, further incentivizing the use of \$IO tokens within the platform.

### Add Wallet to Account

To ensure future cryptocurrency withdrawals, you must link your wallet to your account. You can find instructions on how to get it here, using the [Phantom](/guides/workers/solana) wallet as an example. You can connect a [Solana](/guides/workers/solana) or [Aptos](/guides/workers/aptos-wallet) wallet to your account.

Follow the steps below to add a wallet to your account:

1. Click on your icon in the upper right and select **Account Settings.**

   <Frame>
     <img alt="" />
   </Frame>
2. In the **Solana Wallet** section, click **Add Wallet**.

### Withdraw Funds from Your Account

1. Create a crypto wallet, such as [Phantom](/guides/workers/solana), or use an existing wallet.
2. In the upper-right of the screen, click USDC.

   <Frame>
     <img alt="" />
   </Frame>
3. On the Claim Rewards dialog, choose Custom to enter a specific amount or select the values to the right: 5, 20, 50, or 100.
4. Click the **Confirm Amount** button.
5. A dialog launches that indicates the payment is being processed, followed by a Success confirmation. You can also track the transaction on Soloscan immediately by clicking on the **See on Soloscan** link.

### Earnings and Rewards Tab

The **Earnings & Rewards** tabs enable you to view and manage your earnings for various compute jobs.

In the upper-left, select the **Earnings & Rewards** tab.

<Frame>
  <img alt="" />
</Frame>

On this page, you can monitor your earnings and track data such as:

* Total Compute Hours Served
* Claimable Earnings
* Total Compute Jobs Served
* Earnings graphs by month
* Compute Jobs categorized by tasks

### Block Rewards

Block Rewards are payments made to suppliers who provide their GPUs or CPUs to the our network. This incentivizes supply-side network growth. These rewards are distributed hourly in \$IO, following a predefined emission schedule.

The Block Rewards tab in IO Explore provides a transparent view of io.net's Block Rewards and coin emissions. Users can consult this information to monitor worker nominations and their status. Users can track the performance and success rates for worker nominations and block completion. Information on coin emissions and block rewards provides transparency about io.net network’s health.

For more information, see [Block Rewards](/guides/block-rewards/block-rewards).

### Staking

At IO.net, we're committed to building a robust, secure, and decentralized platform for GPU and CPU supply and demand sides. Our staking program is designed to align incentives, ensure network integrity, and reward active participants in our ecosystem.

Staking is a crucial component of our network security and efficiency. Requiring suppliers to stake \$IO allows us to:

* Encourage long-term commitment to our platform.
* Create an incentive for good behavior.
* Establish a mechanism to discourage and penalize malicious actions.

To learn more about Staking, see [IO Staking](/guides/staking/io-staking).


# Solana Wallet
Source: https://io.net/docs/guides/workers/solana

This document discusses Solana and provides instructions on how to create a Solana Wallet.

<iframe title="Solana Wallet Installation Guide" />

## What is a Solana Wallet?

A Solana wallet is a digital wallet used to store, manage, and interact with Solana (SOL) tokens and other assets on the Solana blockchain. It allows users to securely send, receive, and store their SOL tokens, as well as participate in decentralized finance (DeFi) activities such as staking, lending, and trading on decentralized exchanges (DEXs). Solana wallets come in various forms, including web wallets, mobile wallets, desktop wallets, and hardware wallets, each offering different levels of security and convenience for managing SOL tokens and engaging with the Solana ecosystem.

## How to Create a Solana Wallet

IO.NET is a DeFi project on Solana that pools GPU/CPU resources for artificial intelligence (AI) and machine learning (ML) companies. It uses Solana's blockchain for transparent proof-of-compute, making all jobs and transactions visible on-chain. You can create any Solana (SOL) wallet from the official list here: [Solana Ecosystem](https://solana.com/en/ecosystem/explore?categories=wallet).

For this example, we will use a popular option - Phantom, and demonstrate how to configure and use the wallet:

#### 1. Go to [Phantom Wallet.](https://phantom.app/)

1. Select the browser to install Phantom on. In this example, we use Chrome.
2. Click **Download**.

<Frame>
  <img alt="" />
</Frame>

#### 2. Add to Chrome

After you click **Download**, you're redirect to the extension download page.

Click **Add to Chrome** to add the extension to Chrome.

<Frame>
  <img alt="" />
</Frame>

#### 3. Open the Phantom extension

1. Click **Create a new wallet**.
2. Create a password for your wallet.
3. Click **Continue**.

<Info>
  If you forget your password you will need to restore your wallet using your seed words, provided in the next step. Also, if you clear the browser cache, you cannot login using a password. You must restore wallet again using the seed word.
</Info>

<Frame>
  <img alt="" />
</Frame>

#### 4. Store the Recovery Phrase

1. In the **Secret Recovery Phrase** page, copy and store your 24 word Secret Recovery phrase. You can save them on password managers like Keepass.
2. Click **Continue**.

<Frame>
  <img alt="" />
</Frame>

<Warning>
  Failure to save your Secret Recovery Phrase can result in an inability to access your account. You may lose access to your coins.
</Warning>

#### 5. Copy the SOL Address

After you click **Continue**, the wallet generates a new SOL address. This is the address used to receive coins.

To copy your SOL address:

1. Click on Solana wallet.
2. Click **Receive**.
3. Click Copy button to copy deposit address.

<Frame>
  <img alt="" />
</Frame>

#### 6. Go to your IO ID account to set your new SOL wallet address.

Follow the steps below to set your SOL wallet address.

1. Log in to your io.net account.
2. Go to your **Account Settings** via dropdown menu (in the top-right corner).
3. In **Account Settings**, find the **Solana Wallet Address** block and click the **Add Wallet** button.
4. In the appearing popup, enter your new **Solana wallet** address.
5. Click **Connect** to add the new address.

<Frame>
  <img alt="" />
</Frame>


# Stop & Restart the Platform
Source: https://io.net/docs/guides/workers/stop-restart-the-platform



### Stop the Platform

Run the command below in Terminal to stop and remove all containers for Linux.

<CodeGroup>
  ```Text Terminal Command theme={null}
  sudo docker stop $(sudo docker ps -a -q); sudo docker rm $(sudo docker ps -q)
  ```
</CodeGroup>

### Restart the Platform

* Reboot your computer or server.
* After you reboot the device, restart the platform.
* Rerun the same command provided on the website during the initial setup. It resembles `docker run -d`.

<Danger>
  Verify that you're not running two instances of io-worker-vc.
</Danger>

Run the command below to verify that you're running a single instance of io-worker-vc.

<CodeGroup>
  ```Text Terminal Command theme={null}
  docker ps
  ```
</CodeGroup>

If there are 2 containers running the same image io-worker-vc , the platform fails. The output resembles the sample below:

```
~$ docker ps
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS         PORTS     NAMES
87b1b066bdfa   ionetcontainers/io-worker-monitor   "tail -f /dev/null"      3 seconds ago    Up 2 seconds             agitated_hawking
7033c1b8feba   ionetcontainers/io-worker-vc        "sudo -E /srp/invoke…"   8 seconds ago    Up 8 seconds             friendly_ritchie
67f699e12c2e   ionetcontainers/io-worker-vc        "sudo -E /srp/invoke…"   10 seconds ago   Up 8 seconds             sleepy_feynman
```

#### How to fix this?

Run the stop all docker containers (check troubleshooting guide) and run the (docker run -d ...) command from website only ONCE to run the platform normally.


# Supported Devices
Source: https://io.net/docs/guides/workers/supported-devices

A list of supported device by device type

## Support Processors

#### Below is the list of supported Processors on the IO Network.

| Manufacturer | Processor                   |
| ------------ | --------------------------- |
| Apple        | M3                          |
| Apple        | M3 Pro                      |
| Apple        | M3 Max                      |
| Apple        | M4                          |
| Apple        | M4 Pro                      |
| Apple        | M4 Max                      |
| NVIDIA       | GeForce RTX 3060            |
| NVIDIA       | GeForce RTX 3060 Ti         |
| NVIDIA       | GeForce RTX 3070            |
| NVIDIA       | GeForce RTX 3070 Ti         |
| NVIDIA       | GeForce RTX 3080            |
| NVIDIA       | GeForce RTX 3080 Ti         |
| NVIDIA       | GeForce RTX 3090            |
| NVIDIA       | GeForce RTX 3090 Ti         |
| NVIDIA       | GeForce RTX 4060            |
| NVIDIA       | GeForce RTX 4060 Ti         |
| NVIDIA       | GeForce RTX 4070            |
| NVIDIA       | GeForce RTX 4070 Ti         |
| NVIDIA       | GeForce RTX 4080            |
| NVIDIA       | GeForce RTX 5090            |
| NVIDIA       | L4                          |
| NVIDIA       | RTX 4000                    |
| NVIDIA       | RTX 4000 SFF Ada Generation |
| NVIDIA       | RTX 5000                    |
| NVIDIA       | RTX 5000 Ada Generation     |
| NVIDIA       | RTX 6000 Ada Generation     |
| NVIDIA       | RTX A4000                   |
| NVIDIA       | RTX A5000                   |
| NVIDIA       | RTX A6000                   |
| NVIDIA       | Tesla T4                    |
| NVIDIA       | Tesla V100-PCIE-16GB        |
| NVIDIA       | Tesla V100-PCIE-32GB        |
| NVIDIA       | Tesla V100-SXM2-16GB        |
| NVIDIA       | Tesla V100-SXM2-32GB        |
| NVIDIA       | Tesla V100S-PCIE-32GB       |
| NVIDIA       | L40S                        |
| NVIDIA       | A100 80GB PCIe              |
| NVIDIA       | A100-PCIE-40GB              |
| NVIDIA       | A100-SXM4-80GB              |
| NVIDIA       | GeForce RTX 4090            |
| NVIDIA       | GeForce RTX 4090 D          |
| NVIDIA       | H100 80GB HBM3              |
| NVIDIA       | H100 PCIe                   |
| NVIDIA       | H100 80G PCIe               |
| NVIDIA       | B200                        |
| NVIDIA       | H200                        |

<Info>
  We actively expand our network and support new models from different manufacturers.
</Info>


# Overview
Source: https://io.net/docs/guides/workers/troubleshoot-docker-for-linux

See the following articles to troubleshoot Linus for Docker:

* [Docker Not Installed or Running](/guides/workers/docker-not-installed-or-running)
* [Worker Disconnects When Containers Are Running](/guides/workers/worker-disconnects-when-containers-are-running)
* [Connectivity Displays Incorrectly](/guides/workers/connectivity-tier-not-displaying-correctly)
* [Waiting for IO Containers to Start](/guides/workers/waiting-for-io-containers-to-start)
* [Stop & Restart the Platform](/guides/workers/stop-restart-the-platform)
* [Additional Guides](/guides/workers/additional-guides)


# MacOs: Troubleshoot Docker
Source: https://io.net/docs/guides/workers/troubleshoot-docker-for-macs



### Incompatible CPU detected Error

To resolve this issue, ensure you download and install the appropriate Docker version. For macOS, Docker provides two options: "**Apple Chip**" and "**Intel Chip**."

<Frame>
  <img alt="" />
</Frame>

First, you need to remove the previous version for the **Intel chip**. Click on the **Bug** icon to open Docker Settings, then click **Uninstall**.

<Frame>
  <img alt="" />
</Frame>

After that, visit the Docker website and download and install the version designed for the "**Apple Chip**." Downloading the Docker file may take some time, so please be patient..

<Frame>
  <img alt="" />
</Frame>

### Waiting for IO Containers to Start

Ensure the "**Use containerd for storing and pulling images**" option is **disabled** in Docker's General Settings.

<Frame>
  <img alt="" />
</Frame>

Containerd may interfere with Docker’s default image management, **so it’s recommended to turn it off**.

## Worker Disconnecting Despite Containers Running

If your Worker disconnects even when the containers are up, try the following checks:

1. Ensure resources aren't limited. Make sure Docker's "**Resource Saver**" feature is **disabled** in the **Resources tab** of **Docker Settings**.

   <Frame>
     <img alt="" />
   </Frame>
2. Check Docker Resource Allocation. Ensure Docker is allocated the minimum required **CPU**, **RAM**, and **disk space**. System requirements are as follows:
   * **Memory**: At least 512MB of free RAM (2GB is recommended)
   * **Disk**: Adequate storage to run the Docker containers you intend to use
   * **GPU**: You can check the currently supported [GPUs](/guides/workers/supported-devices).

## Connectivity Tier Not Displaying Correctly

To troubleshoot connectivity tier issues, users can test network speeds via a sample Docker container. Here's how:

1. Pull the Python 3.9 Slim container:

   ```
   docker pull python:3.9-slim
   ```
2. Run the container:

   ```
   docker run -it --name speedtest-container python:3.9-slim /bin/bash
   ```
3. Install the speedtest tool:

   ```
   pip install speedtest-cli
   ```
4. Test the network speed:

   ```
   speedtest-cli
   ```

<Frame>
  <img alt="" />
</Frame>

We recommend running similar speed tests periodically within your containers to monitor connectivity performance. You can also guide users on how to perform these tests at regular intervals or during specific instances for troubleshooting.


# Windows: Troubleshoot Docker
Source: https://io.net/docs/guides/workers/troubleshoot-docker-for-windows



### Windows Uptime

Follow the instructions below if you experience inconsistent uptime on Windows.

<Info>
  To ensure that the DHCP lease time on the router is set to a duration exceeding 24 hours, access the group policy editor within the Windows operating system. Proceed by enabling the specified settings in the following sequence:
</Info>

1. Open the group policy editor and go to **Computer Configuration**.
2. In Computer Configuration, find the **Administrative Templates** section.
3. Under **Administrative Templates**, go to **System**.
4. In the **System** menu, choose **Power Management**.
5. Access the **Sleep Settings** subsection within **Power Management**.
6. Activate both **Allow network connectivity during connected-standby (on battery)** and **Allow network connectivity during connected-standby (plugged in)** options.

Adjust the settings above to meet your requirements.

### Fixing the "Docker Desktop - Unexpected WSL error" in Windows

This error occurs when you haven't updated to the latest version of WSL or haven't enabled the Hyper-V feature. Follow these steps:

<Frame>
  <img alt="" />
</Frame>

1. **Check and Update WSL Version**: First, ensure that you’re running the latest version of WSL. You can check your current WSL version by opening a command prompt and typing:

   ```
   wsl --version
   ```

   If you find that you’re not on WSL 2, you can set the default version to 2 by executing:

   ```
   wsl --set-default-version 2
   ```
2. **Enable Hyper-V Feature**: Hyper-V is a virtualization technology tool that needs to be enabled in Windows. To check if Hyper-V is enabled, you can use the Windows Features dialog via Search:

   <Frame>
     <img alt="" />
   </Frame>

   In the **Windows Features** dialog, scroll down and check **Windows Hypervisor Platform**, then click OK.:

   <Frame>
     <img alt="" />
   </Frame>

   After installing **Windows Hypervisor Platform**, the problem should disappear.

### Stop the Docker with all Containers and Images

Run the command below in Terminal to stop the platform and remove all containers for Windows.

<CodeGroup>
  ```Text Terminal Command theme={null}
  # Stop all running containers
  docker stop $(docker ps -aq)

  # Remove all containers
  docker rm $(docker ps -aq)

  # Remove all images
  docker rmi $(docker images -aq)
  ```
</CodeGroup>

### Restart the Platform

* Reboot your computer or server.
* After the device reboots, restart the platform by entering this command into the Terminal:

  ```
  ./io_net_launch_binary_windows.exe 
  ```

### Additional Guides

#### Ports

Expose the ports below to ensure platform stability for Windows:

* TCP: 443, 25061, 5432, 80
* UDP: 80, 443, 41641, 3478

Ensure that these ports are open and accessible to enable smooth operation of the platform.

#### How can I verify that program has started successfully?

* When running the following command on Terminal, **you should always have 2 Docker containers running**:

  <CodeGroup>
    ```Text Terminal Command theme={null}
     docker ps
    ```
  </CodeGroup>
* If there are no containers or only one container running after running the docker run **-d ... command** from the website:
  * Stop the platform using the command provided in the guide above.
  * Restart the platform using the command from the website again.

### Waiting for IO Containers to Start

Ensure the "**Use containerd for storing and pulling images**" option is **disabled** in Docker's General Settings.

<Frame>
  <img alt="" />
</Frame>

Containerd may interfere with Docker’s default image management, **so it’s recommended to turn it off**.

## Worker Disconnecting Despite Containers Running

If your Worker disconnects even when the containers are up, try the following checks:

1. Ensure resources aren't limited. Make sure Docker's "**Resource Saver**" feature is **disabled** in the **Resources tab** of **Docker Settings**.

   <Frame>
     <img alt="" />
   </Frame>
2. Check Docker Resource Allocation. Ensure Docker is allocated the minimum required **CPU**, **RAM**, and **disk space**. System requirements are as follows:
   * **Memory**: At least 512MB of free RAM (2GB is recommended)
   * **Disk**: Adequate storage to run the Docker containers you intend to use
   * **CPU/GPU**: You can check the currently supported [CPUs/GPUs](/guides/workers/supported-devices).
3. Verify Power Supply to GPU(s). Ensure the GPU(s) are receiving adequate power for stable operation.

## Connectivity Tier Not Displaying Correctly

To troubleshoot connectivity tier issues, users can test network speeds via a sample Docker container. Here's how:

1. Pull the Python 3.9 Slim container:

   ```
   docker pull python:3.9-slim
   ```
2. Run the container:

   ```
   docker run -it --name speedtest-container python:3.9-slim /bin/bash
   ```
3. Install the speedtest tool:

   ```
   pip install speedtest-cli
   ```
4. Test the network speed:

   ```
   speedtest-cli
   ```

<Frame>
  <img alt="" />
</Frame>

We recommend running similar speed tests periodically within your containers to monitor connectivity performance. You can also guide users on how to perform these tests at regular intervals or during specific instances for troubleshooting.


# MacOS: Troubleshoot Worker
Source: https://io.net/docs/guides/workers/troubleshoot-macos-worker

Here we've compiled essential use cases for working with Workers.

### Bad CPU Type in Executable Error

If you come across an error message like "**bad CPU type in executable**," it's likely because you are trying to run software intended for an Intel processor on an Apple Silicon device. To resolve this issue, you'll need to install <Tooltip>Rosetta 2</Tooltip>, which enables support for Intel processors to operate within <Tooltip>Docker</Tooltip> on Apple Silicon devices.

<Frame>
  <img alt="" />
</Frame>

To check if Rosetta is installed and active, enter the following command in the Terminal and press Enter:

```
/usr/sbin/sysctl sysctl.proc_translated
```

If the output is **sysctl.proc\_translated: 1**, Rosetta is installed and active on your system. If the output is either **sysctl.proc\_translated: 0** or there is **no output**, Rosetta is not installed or not active.

If Rosetta 2 is not installed, use this command to install it:

```
softwareupdate --install-rosetta --agree-to-license
```

Once Rosetta 2 installation is complete, rerun the execution command:

```
./io_net_launch_binary_mac
```

### Common Issue: Container CPU Dropping to 0

A common issue that many users encounter is the CPU of the container dropping to 0.

This problem is often due to missing necessary software components. You need to install[Rosetta](/guides/workers/install-on-macos#7-download-and-launch-io-binary). Detailed instructions on how to install these software components can be found in this section above.

If you still encounter this issue after installing all the necessary software components, try deleting the containers and images, then **re-run** the worker command and wait. You may need to repeat this process 3 or 4 times until they function normally. If the issue persists after these steps, it may indicate a system-level error.

<Frame>
  <img alt="" />
</Frame>

<Info>
  For general questions about the Worker, no matter the operating system, check [here](/guides/workers/troubleshoot-worker-general)
</Info>

<Info>
  Feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>


# Windows: Troubleshoot Worker
Source: https://io.net/docs/guides/workers/troubleshoot-windows-worker

Here we've compiled essential use cases for working with Workers.

### How to Resolve Unsupported GPU Issues?

If a user's supported GPU is listed as unsupported on the website, they should verify their NVIDIA driver configuration. Often, when a Docker container running **nvidia-smi** fails, the backend receives this information and marks the GPU as unsupported.

To check the configuration, running the following command should provide the correct output:

```
docker run --gpus all nvidia/cuda:11.0.3-base-ubuntu18.04 nvidia-smi
```

### Regulate RAM Usage

<Frame>
  <img alt="" />
</Frame>

Create a file called **.wslconfig** to restrict the resources used by **WSL2** (Windows Subsystem for Linux). Follow the steps below to create it:

* **Open File Explorer** and navigate to your user's home directory (usually **`C:/Users/<Username>`**).
* **Create a new text file** in your home directory and name it **.wslconfig**.
* **Edit the .wslconfig File:** Right-click on the newly created **.wslconfig** file and open it with a text editor such as Notepad.
* **Add the following configuration parameters** to limit memory (set values according to your preference):

  ```
  [wsl2]  
  memory=4GB # Limits the VM memory in WSL between 2 and 4 GB  
  processors=2 # Limits the number of processors to 2  
  swap=8GB # Sets the swap size to 8 GB
  ```
* **Save the file and restart your computer**. If the worker does not connect automatically, you may [need to install it again](/guides/workers/troubleshoot-worker-general#how-can-i-pause-or-reset-a-worker-if-it-has-disconnection-issues).

### Computer Time Synchronization Issue

Make sure your computer's time is synchronized with the server. If it's not, the IO binary won't work properly. Click the **Start Menu** and open the **Settings** app.

<Frame>
  <img alt="" />
</Frame>

Next, in the **Settings** app, go to **Time & Language** and select **Date & Time**. Then, under **Additional settings,** click the **Sync now** button to synchronize your computer's time with the server.

<Frame>
  <img alt="" />
</Frame>

### Common Issue: Container CPU Dropping to 0

A common issue that many users encounter is the CPU of the container dropping to 0.

This problem is often due to missing necessary software components. For instance, on Windows, you need to ensure [CUDA](/guides/workers/cuda-toolkit-optional) and [WSL2](/guides/workers/install-docker-on-windows#3-configure-wsl2-to-integrate-with-docker-settings) are installed.

If you still encounter this issue after installing all the necessary software components, try deleting the containers and images, then **re-run** the worker command and wait. You may need to repeat this process 3 or 4 times until they function normally. If the issue persists after these steps, it may indicate a system-level error.

<Frame>
  <img alt="" />
</Frame>

<Info>
  For general questions about the Worker, no matter the operating system, check [here](https://docs.io.net/docs/troubleshoot-worker-general)
</Info>

<Info>
  Feel free to [check our knowledge base](/guides/workers/troubleshoot-worker-general) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>


# General Worker Troubleshooting
Source: https://io.net/docs/guides/workers/troubleshoot-worker-general

Here we've compiled essential use cases for working with Workers.

### How to Resolve Unsupported GPU Issues on Windows and Linux?

If a user's supported GPU is listed as unsupported on the website, they should verify their NVIDIA driver configuration. Often, when a Docker container running **nvidia-smi** fails, the backend receives this information and marks the GPU as unsupported.

To check the configuration, running the following command should provide the correct output:

```
docker run --gpus all nvidia/cuda:11.0.3-base-ubuntu18.04 nvidia-smi
```

### If I received a "device code authorization returned: Bad Request" error?

If this error is displayed following authorization:

```
Error: device code authorization returned: Bad Request
Error: Error authenticating: provided token has expired or invalid. Please re-authenticate using --no_cache=true flag.
```

This error might be caused by an issue with network connections. Visit [https://auth0.io.solutions/activate](https://auth0.io.solutions/activate). If the page does not open, it means **Auth0** is not reachable for you.

### How can I pause or reset a Worker if it has disconnection issues?

If your worker has been disconnected, here are a few steps to fix it:

1. Go to your running **Worker Page** and click on **Pause** for the Worker (located at the top-right corner).
2. **Optionally**, restart the device as needed.
3. After restarting the device, open your Worker page at IO.NET and copy the command from the **Re-Run docker command** block on the **Worker Page**, then run it Terminal.

   <Frame>
     <img alt="" />
   </Frame>
4. If prompted, authorize the device using IO.ID. Remember, you have about 3 minutes to complete the authorization.

   <Frame>
     <img alt="" />
   </Frame>
5. Confirm the removal of all previous containers in Docker.

   <Frame>
     <img alt="" />
   </Frame>
6. Wait for up to 10 minutes to see the progress. Your worker is now ready to use again.

<Frame>
  <img alt="" />
</Frame>

### How can suppliers change their accounts in IO Worker?

To change accounts, suppliers should include the **--no\_cache=true** flag in the binary run command. This triggers a re-authentication process. Simply add **--no\_cache=true** at the end of your main request when connecting the device with the new login.

<CodeGroup>
  ```Text MacOs theme={null}
  ./launch_binary_mac --disable_sleep_mode=true --no_cache=true
  ```

  ```Text Windows theme={null}
  ./io_net_launch_binary_windows.exe --disable_sleep_mode=true --no_cache=true
  ```

  ```Text Linux theme={null}
  ./io_net_launch_binary_linux --disable_sleep_mode=true --no_cache=true
  ```
</CodeGroup>

<Info>
  After one successful sign-in, the token will be saved in memory.
</Info>

<Frame>
  <img alt="" />
</Frame>

### How can you run an existing worker UUID in the new authentication and authorization system?

As of May 2024, we have transitioned to a new authentication and authorization system. Follow these steps to run your existing worker UUID again.

#### 1. Run the Command to Connect the Device

Open the Terminal on your system by navigating to the Start menu and using the search function. The process is similar regardless of your operating system.

<Frame>
  <img alt="" />
</Frame>

Then run the command in the Terminal. For Windows, start by downloading and running the executable file.

* Download the binary for your operating system running command. [**For Windows you need to download the executable file. You can see how it's done here**](/docs/install-on-windows#7-download-and-launch-io-binary)

  <CodeGroup>
    ```Text MacOS theme={null}
    curl -L https://github.com/ionet-official/io_launch_binaries/blob/main/io_net_launch_binary_mac -o io_net_launch_binary_mac
    ```

    ```Text Windows theme={null}
    https://github.com/ionet-official/io_launch_binaries/raw/main/io_net_launch_binary_windows.exe
    ```

    ```Text Linux theme={null}
    curl -L https://github.com/ionet-official/io_launch_binaries/blob/main/io_net_launch_binary_linux -o io_net_launch_binary_linux
    ```
  </CodeGroup>
* Use the following command to grant permissions to the new binary:

  <CodeGroup>
    ```Text MacOS theme={null}
    chmod +x io_net_launch_binary_mac
    ```

    ```Text Linux theme={null}
    chmod +x io_net_launch_binary_linux
    ```
  </CodeGroup>
* Launch the binary to connect your device to the platform.

  <CodeGroup>
    ```Text MacOS theme={null}
    ./io_net_launch_binary_mac --no_warnings=true 
    ```

    ```Text Windows theme={null}
    ./io_net_launch_binary_windows.exe --no_warnings=true 
    ```

    ```Text Linux theme={null}
    ./io_net_launch_binary_linux --no_warnings=true 
    ```
  </CodeGroup>

<Frame>
  <img alt="" />
</Frame>

#### 2: To authorize the device with [IO.ID](http://io.id/), follow one of the options below and verify your IO.ID account:

<Info>
  Remember, you will have about 1-2 minutes to complete the authorization of the device. If it expires, run the code again.
</Info>

You can do this in two ways: **Copy the Link from the Terminal**: Paste it into your browser and confirm the action.

<Frame>
  <img alt="" />
</Frame>

After confirmation, the system will prompt you to log in.

<Frame>
  <img alt="" />
</Frame>

#### 3. Save the Token

The information below is found in the CLI. Keep this token accessible.

<Frame>
  <img alt="" />
</Frame>

#### 4. For all other machines use the saved token

This does not require manual reauthentication and can be used for all your worker nodes.

<Frame>
  <img alt="" />
</Frame>

### Why Do Containers Disappear from Docker?

If the container disappears from docker, then your worker was likely blocked. If this happens, you must recreate the worker from scratch.

<Frame>
  <img alt="" />
</Frame>

### Why Is My Worker Blocked?

Blocked status is indicative that our system detected GPU utilization that was not authorized by our internal checks. It's important that GPU availability is dedicated 100% to the task being volunteered for the health of the <Tooltip>DePIN</Tooltip>.

Blocked status can occur for a few different reasons, primarily:

* **Excessive GPU Utilization:** Activities such as playing games or using graphics-intensive applications. (You'll need to pause these activities before you start usage.)
* **Mining Detection:** Our team has implemented an update to detect mining devices and instances with high GPU usage, resulting in an automatic ban.
* **Device and Hardware Switching:** Our team has implemented a mechanism for blocking device if they were verified and later a different device with a different hardware was detected. If you need to use a new hardware, please create a new device

<Frame>
  <img alt="" />
</Frame>

### Why Does My Worker Have an Unsupported Status?

This occurs when your GPU/CPU is not listed among the supported devices on the IO Network. You can check the list of supported devices [here](/docs/supported-devices).

<Frame>
  <img alt="" />
</Frame>

### Why Does My Worker Disappear from My Dashboard?

This issue can stem from a few main causes:

1. **Unsuccessful Connection**: You didn't successfully connect the new worker. Here's an example of a successful worker connection:

   <Frame>
     <img alt="" />
   </Frame>
2. **Unsupported Hardware**: If you successfully connected a new worker but the GPU/CPU you're using is not supported, you won't see your worker on the dashboard. You can check the list of supported devices [here](/docs/supported-devices).
3. **User Interface Issues**: If your worker was running normally and suddenly disappears from the dashboard, it could be due to a problem with the user interface (UI). In such cases, try refreshing the website. If the worker still doesn't appear, please try again later or [create a ticket](https://worker.io.net) for our support team to assist you.

### Creating Multiple Workers from the Same Device

Users may inadvertently create a new worker each time the previous one fails instead of re-running the existing worker. To address this issue, you need to **Terminate the old workers** and learn how to restart Docker to continue running the existing worker. Follow the instructions [here](/docs/troubleshoot-worker-general#how-can-i-pause-or-reset-a-worker-if-it-has-disconnection-issues).

<Frame>
  <img alt="" />
</Frame>

### Device Readiness Status

Your device status needs to be either **Cluster Ready** or **Hired** to be nominated for Block Rewards and be eligible for hiring. You can verify device status either on the device detail page or on the **Workers** tab in **IO Explore**. For more information, see the [Get Started - IO Worker](/docs/intro) doc.

The four possible **Readiness** statuses are:

| Status                     | Description                                                                                                                                                                                                                                                                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cluster Ready**          | Device meets PoW requirements and passed several Cluster Formation verifications.                                                                                                                                                                                                                                                                  |
| **Hired**                  | Device is currently hired by a cluster.                                                                                                                                                                                                                                                                                                            |
| **Pending**                | The device has joined the network and is currently undergoing both the PoW and Cluster Readiness test. This process can take up to 12 hours of cumulative uptime after onboarding, but may complete sooner if your device passes our tests early. If your device remains in a Pending state after more than 12 hours of uptime, please contact us. |
| **Not Block Reward Ready** | Device doesn't meet the criteria for block reward eligibility, mainly Cluster Formation verifications.                                                                                                                                                                                                                                             |

**Not Block Reward Ready** offers one of three tooltips in the UI to provide troubleshooting tips.

* **Please check your device's computational capacity**- Your device's computational capacity is below the required threshold.
* **Please check your device setup and computational capacity**- Your device setup might not be configured correctly and its computational capacity is below the required threshold. Please refer to the worker setup guide.
* **Please check your device setup**- Your device setup might not be configured correctly. Please refer to the worker setup guide.

<Info>
  Feel free to [check our knowledge](https://support.io.net/en/support/home) base for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>


# Ubuntu: Install Docker
Source: https://io.net/docs/guides/workers/ubuntu-install-docker

A step-by-step guide for installing Docker on Linux-based machines

<iframe title="Docker Guide for Linux" />

### What is Docker?

Let's take a quick look at what **Docker** is? Imagine Docker as a magic box where you put your software and everything it needs to run. This box can be easily carried to any computer, and when you open it, your software works just the way you packed it, without needing anything extra from that computer. Here are a few steps to install Docker:

### Before installing Docker, please check if it is already installed

Run the following command to verify if Docker is not installed:

```
docker compose version
```

If you see the following error, you can proceed with this guide:

```
Command 'docker' not found, but can be installed with:
sudo snap install docker         # version 24.0.5, or
sudo apt  install podman-docker  # version 3.4.4+ds1-1ubuntu1.22.04.2
sudo apt  install docker.io      # version 24.0.7-0ubuntu2~22.04.1
See 'snap info docker' for additional versions.
```

<Frame>
  <img alt="" />
</Frame>

### 1. Download Docker

Go to the [Docker website](https://www.docker.com/products/docker-desktop/) and click on "**Download for Linux**." You will be redirected to a page with supported Linux platforms.

<Frame>
  <img alt="" />
</Frame>

### 2. Download the appropriate version for your system

Select the appropriate version for your system, such as Ubuntu, and click on the link in the **"Supported platforms"** section of the page. Downloading the Docker file may take some time. Please be patient.

<Frame>
  <img alt="" />
</Frame>

### 3.Open the Ubuntu Terminal

through the Start Menu

**Terminal** is a tool on your computer that lets you type in commands to tell the computer what to do. Instead of clicking on things with a mouse, you write instructions, and the computer follows them. It's like talking directly to your computer using text.

Click the **Start Menu** icon, start typing "**Terminal**" in the search field, then click the **Terminal** icon:

<Frame>
  <img alt="" />
</Frame>

### 4. Copy and run the first command

Return to the Docker page and copy the first command from the "Install Docker Desktop" section:

```
sudo apt-get update
```

<Frame>
  <img alt="" />
</Frame>

Paste the command into the Terminal and press Enter. After that, you will be prompted to enter your password for confirmation. Type your password (note that it will not be visible while typing) and press Enter again.

<Frame>
  <img alt="" />
</Frame>

### 5. Check the .deb package

In the Terminal, you need to check the name of the downloaded file. First, navigate to the "Downloads" folder by typing this command:

```
cd Downloads/
```

Then, enter the following command to see the list of files in the "Downloads" folder:

```
ls
```

<Frame>
  <img alt="" />
</Frame>

### 6. Copy the installation command

Return to the Docker installation page and copy the second command from the "Install Docker Desktop" section:

```
 sudo apt-get install ./docker-desktop-amd64.deb
```

<Warning>
  Make sure to replace the package name with the correct one from the Terminal (based on what you saw in the previous step).
</Warning>

<Frame>
  <img alt="" />
</Frame>

Paste the command into the **Terminal** and press Enter. After that, you will be prompted to enter your password for confirmation. Type your password (note that it will not be visible while typing) and press Enter again.

<Danger>
  If you encounter an error related to the absence of Docker CE-CLI during the installation, you can follow this detailed guide: [How to Install Docker CE on Ubuntu](https://www.rosehosting.com/blog/how-to-install-docker-ce-on-ubuntu-22-04).

  After completing the steps, you can continue installing Docker Desktop from where you left off.
</Danger>

During the installation process, you will be asked to confirm if Docker can use some space on your computer. Type **Yes** to complete the installation successfully..

<Frame>
  <img alt="" />
</Frame>

<Warning>
  You must restart your device after installing Docker Desktop; otherwise, the system may not allow you to use it properly, even if Docker appears to be running.
</Warning>

### 7. Run the Docker Desktop

Return to the Docker installation page and copy the command from the "Launch Docker Desktop" section:

<Frame>
  <img alt="" />
</Frame>

Paste the command into the Terminal and press Enter. If there are no issues with the installation, Docker should be running.

<Frame>
  <img alt="" />
</Frame>

### 7. Verify that Docker Desktop is Successfully Installed

Copy and paste the following line into Terminal.

<CodeGroup>
  ```Text Terminal Command theme={null}
  sudo systemctl status docker
  ```
</CodeGroup>

<Frame>
  <img alt="" />
</Frame>

The result will be the current version of running Docker.

```
● docker.service  - Docker Application Container Engine
          Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
          Active: active (running) since Thu 2023-02-09 03:02:24 CST; 10s ago
     TriggeredBy: ● docker.socket
            Docs: https://docs.docker.com
        Main PID: 2361 (dockerd)
           Tasks: 9
          Memory: 26.2M
             CPU: 780ms
          CGroup: /system.slice/docker.service
                 └─2361 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock 
```

### 8. Verify Docker Installation with GPU

Confirmation Command:

* To confirm that your setup is working correctly, run:

  <CodeGroup>
    ```Text Terminal Command theme={null}
    docker run --gpus all nvidia/cuda:11.0.3-base-ubuntu18.04 nvidia-smi
    ```
  </CodeGroup>
* The output should resemble the information displayed by `nvidia-smi`.
* This command verifies that Docker is correctly utilizing your GPU.

### Congratulations on Successfully Setting up Docker

Now that Docker has been successfully installed and is running, you can proceed with [setting up the Worker](/guides/workers/install-on-ubuntu).

### Troubleshoot Docker Installation

Use the Reset Script (end of page):

* If the confirmation command fails, use the reset\_drivers\_and\_docker script:

  <CodeGroup>
    ```Text Terminal Command theme={null}
    chmod +x reset_drivers_and_docker.sh  
    ./reset_drivers_and_docker.sh
    ```
  </CodeGroup>
* After running the script, restart your device.
* Rerun the setup from the website. After an automatic restart, rerun the setup to complete the installation.
* If the confirmation command continues to fail, seek assistance on the community support channel.

<Info>
  If you encounter issues with Docker, please refer to our [Troubleshooting Docker guide](/guides/workers/troubleshoot-docker). If the problem persists or if you need further assistance, feel free to [check our knowledge base](https://support.io.net/en/support/home) for answers, and if you still need help, don’t hesitate to open a support ticket!
</Info>


# Waiting for IO Containers to Start
Source: https://io.net/docs/guides/workers/waiting-for-io-containers-to-start

On Linux the above issue can be due to several reasons:

1. **Nvidia-container-toolkit.** Ensure the Nvidia-container-toolkit is installed and properly configured.
2. **Docker Daemon.** Check if Docker Daemon is running.
3. **GPU Configuration.** Docker needs to be configured with the Nvidia runtime to use the GPU inside a container. This can be fixed by installing and configuring the Nvidia-container-toolkit.

#### Debugging:

1. **Test GPU with Docker:** Run the following command to check if Docker can access the GPU:

   ```
   docker run --gpus all nvidia/cuda:11.0.3-base-ubuntu18.04 nvidia-smi
   ```

   If **nvidia-smi** output is visible, Docker can use the GPU inside the container. If not, try restarting Docker Daemon:

   ```
   sudo systemctl restart docker
   ```

   Else there might be some error similar to the following:

   <Frame>
     <img alt="" />
   </Frame>
2. **Error Debugging:** If errors related to **nvidia-container-toolkit** are shown, it may not be installed or configured correctly.

#### Commands to Check Nvidia-container-toolkit Installation:

1. Check if Nvidia-container-toolkit is installed:

   ```
   nvidia-container-runtime --version
   dpkg -l | grep nvidia-container-toolkit
   ```
2. If it's installed but not configured properly, follow one of the two methods below:

#### Method 1: Configure daemon.json:

1. Open the daemon.json file:

   ```
   sudo nano /etc/docker/daemon.json
   ```
2. Paste the following:

   ```
   {
      "runtimes": {
        "nvidia": {
          "path": "nvidia-container-runtime",
          "runtimeArgs": []
        }
      },
      "default-runtime": "nvidia"
   }
   ```
3. Save and exit, then reboot the server:

   ```
   sudo reboot
   ```
4. After reboot, restart Docker:

   ```
   sudo systemctl restart docker
   ```

#### Method 2: Configure Nvidia-ctk Directly:

Run the following commands:

```
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

#### If Nvidia-container-toolkit is Not Installed:

1. Install Nvidia-container-toolkit:

   ```
   curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg && /
   curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | /
   sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | /
   sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
   ```
2. Enable experimental features:

   ```
   sudo sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list
   ```
3. Update and install the toolkit:

   ```
   sudo apt-get update
   sudo apt-get install -y nvidia-container-toolkit
   sudo nvidia-ctk runtime configure --runtime=docker
   sudo systemctl restart docker
   ```

#### Verify Nvidia-container-toolkit:

1. Check if the toolkit is in the **\$PATH**:

   ```
   /usr/bin/nvidia-ctk --version
   echo $PATH
   ```
2. Verify the runtime is configured:

   ```
   docker info | grep -i runtime
   ```

   Sample output:

   <Frame>
     <img alt="" />
   </Frame>

#### Final GPU Test:

Run the following command to test if Docker can use the GPU:

```
docker run --gpus all nvidia/cuda:11.0.3-base-ubuntu18.04 nvidia-smi
```


# Worker Disconnects When Containers Are Running
Source: https://io.net/docs/guides/workers/worker-disconnects-when-containers-are-running

If your Worker disconnects even when the containers are up, try the following checks:

1. Ensure resources aren't limited. Make sure Docker's "**Resource Saver**" feature is **disabled** in the **Resources tab** of **Docker Settings**.

   <Frame>
     <img alt="" />
   </Frame>

2. Check Docker Resource Allocation. Ensure Docker is allocated the minimum required **CPU**, **RAM**, and **disk space**. System requirements are as follows:

   * **Memory**: At least 512MB of free RAM (2GB is recommended)
   * **Disk**: Adequate storage to run the Docker containers you intend to use
   * **CPU/GPU**: You can check the currently supported [CPUs/GPUs](/guides/workers/supported-devices).

3. Verify Power Supply to GPU(s). Ensure the GPU(s) are receiving adequate power for stable operation.


# Agents List
Source: https://io.net/docs/reference/ai-agents/get-agents-list

openapi/ai-agents/get-agents-list.json get /api/v1/agents
Get a list of all the available agents.

<Warning>
  **Beta Notice:** This project is in rapid development and may not be stable for production use.
</Warning>


# Getting Started with AI Agents API
Source: https://io.net/docs/reference/ai-agents/getting-started-with-api-agents



<Warning>
  Beta Notice: This project is in rapid development and may not be stable for production use.
</Warning>

***AI Agents*** in **IO Intelligence** are specialized assistants designed to handle a variety of tasks, from reasoning and summarization to sentiment analysis and translation. These agents leverage advanced AI capabilities to automate complex workflows, enhance decision-making, and streamline information processing.

Each ***AI Agent*** is tailored for a specific function — whether it is extracting key information, classifying data, moderating content, or translating languages. By integrating these agents into your applications, you can harness powerful AI-driven automation with ease.

### Important Note on Usage Limits

Each model within **IO Intelligence** has its own value and credit consumption rate based on its complexity, capability, and computational cost.

For **plan subscribers** (*Basic*, *Professional*, or higher tiers), all model interactions draw from a **shared usage pool**. This means you can use any model available under your plan, and your total usage will count toward a single shared credit allowance — rather than having separate limits for each model.

This shared system provides maximum flexibility, allowing you to switch between models seamlessly while staying within your daily or hourly quota.

This limit is designed to ensure fair and balanced usage for all users. If you anticipate needing a higher request limit, please consider optimizing your implementation or reach out to us for assistance.

For further details on **usage limits, full breakdown of rates, and how IO Credits are billed**, refer to the [**IO Intelligence Payments**](/guides/payment/io-intelligence-payments) page.

## Introduction

You can interact with the API using HTTP requests from any programming language or by using the official Python.

To install the official Python library, run the following command:

```
pip install iointel
```

### Example: Using the AI Agents API in Python

The following is an example of how you can use the `iointel Python` library to interact with the *IO Intelligence APIs*:

<CodeGroup>
  ```python Python theme={null}
  from iointel import (
      Agent,
      Workflow
  )

  import os
  import asyncio

  api_key = os.environ["OPENAI_API_KEY"]  # Replace with your actual IO.net API key

  text = """In the rapidly evolving landscape of artificial intelligence, the ability to condense vast amounts of information into concise and meaningful summaries is crucial. From research papers and business reports to legal documents and news articles, professionals across industries rely on summarization to extract key insights efficiently. Traditional summarization techniques often struggle with maintaining coherence and contextual relevance. However, advanced AI models now leverage natural language understanding to identify core ideas, eliminate redundancy, and generate human-like summaries. As organizations continue to deal with an ever-growing influx of data, the demand for intelligent summarization tools will only increase. Whether enhancing productivity, improving decision-making, or streamlining workflows, AI-powered summarization is set to become an indispensable asset in the digital age."""

  agent = Agent(
      name="Summarize Agent",
      instructions="You are an assistant specialized in summarization.",
      model="meta-llama/Llama-3.3-70B-Instruct",
      api_key=api_key,
      base_url="https://api.intelligence.io.solutions/api/v1"
  )

  workflow = Workflow(objective=text, client_mode=False)

  async def run_workflow():
      results = (await workflow.summarize_text(max_words=50,agents=[agent]).run_tasks())["results"]
      return results

  results = asyncio.run(run_workflow())
  print(results)
  ```
</CodeGroup>

This snippet demonstrates how to configure the client, send a chat completion request using the `Llama-3.3-70B-Instruct` agent, and retrieve a response.

<Warning>
  `run_tasks()` is now asynchronous. All usage must be wrapped inside an async function. Use asyncio.run() to execute it.
</Warning>

## Authentication

### API Keys

*IO Intelligence APIs* authenticate requests using **API keys**. You can generate API keys from the [API Keys tab](https://ai.io.net/ai/api-keys) under **IO Intelligence**.

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service on your backend server.
</Warning>

Include the API key in an `Authorization` HTTP header for all API requests:

```
Authorization: Bearer \$IOINTELLIGENCE_API_KEY
```

### Example: List Available Agents

The following is an example `curl` command to list all agents available in **IO Intelligence**:

<CodeGroup>
  ```curl curl theme={null}
  curl https://api.intelligence.io.solutions/api/v1/agents /
    -H "Authorization: Bearer \$IOINTELLIGENCE_API_KEY" 
  ```
</CodeGroup>

<Frame>
  <img alt="" />
</Frame>

This request should return a response as follows:

<CodeGroup>
  ```json json theme={null}
  {
    "agents": {
      "reasoning_agent": {
        "name": "Reasoning Agent",
        "description": "A logic-driven problem solver that breaks down complex scenarios into clear, step-by-step conclusions. Whether evaluating arguments, making inferences, or troubleshooting issues, this agent excels at structured thinking and insightful analysis.",
        "persona": null,
        "metadata": {
          "image_url": null,
          "tags": [
            "text"
          ]
        }
      },
      "summary_agent": {
        ...
      },
      "sentiment_analysis_agent": {
       ...
      },
      ...
    }
  }
  ```
</CodeGroup>

With these steps, you have successfully made your first request to the ***IO Intelligence Agents API***.

For further details on **Agents, Workflows, and API Endpoints**, check out the [IO Intelligence Agent Framework](/guides/intelligence/agent-framework).


# Delete a Secret
Source: https://io.net/docs/reference/ai-agents/secret-management-delete

openapi/ai-agents/secret-management-delete.json delete /api/v1/secrets/{secret_id}
Deletes an existing secret and its associated configuration.

This endpoint allows you to permanently remove a registered secret from storage, revoking access for any tool previously authorized to use it. Once deleted, the secret and its associations cannot be recovered.

<Note>
  The API supports multiple authentication mechanisms, but only **one** needs to be provided per request. You may authenticate using **any** of the following headers, a browser-issued JWT `token`, an `Authorization` header, or an `x-api-key` header (io.net API key).
</Note>


# Get Secret Details
Source: https://io.net/docs/reference/ai-agents/secret-management-get

openapi/ai-agents/secret-management-get.json get /api/v1/secrets/{secret_id}
Retrieves details for a specific secret.

This endpoint allows you to access detailed information about a registered secret, including its associated tool, argument, and configuration details. The actual secret value is never returned in the response for security reasons.

<Note>
  The API supports multiple authentication mechanisms, but only **one** needs to be provided per request. You may authenticate using **any** of the following headers, a browser-issued JWT `token`, an `Authorization` header, or an `x-api-key` header (io.net API key).
</Note>

<Note>
  The `display` field returned in the response provides a partially masked representation of the secret value. It shows only the first and last few characters, ensuring that at least part of the value remains hidden. Complete visibility is only possible for very short secrets (typically 4 characters or fewer).
</Note>

<Tip>
  When retrieving secrets, wildcard patterns can be used to simplify configuration. For example, instead of specifying each *Linear* subtool individually (such as `agno__linear__get_user_details`, `agno__linear__get_issue_details`, and others), a single wildcard pattern like `agno__linear__*` can be used to apply the secret across all related Linear tools.
</Tip>


# Update Secret Details
Source: https://io.net/docs/reference/ai-agents/secret-management-patch

openapi/ai-agents/secret-management-patch.json patch /api/v1/secrets/{secret_id}
Updates an existing secret or its associated metadata.Updates an existing secret or its associated metadata.

This endpoint allows you to modify one or more properties of a previously registered secret, such as its value, linked tool, or default configuration. Only the fields provided in the request body will be updated, and omitted fields will remain unchanged.

<Note>
  The API supports multiple authentication mechanisms, but only **one** needs to be provided per request. You may authenticate using **any** of the following headers, a browser-issued JWT `token`, an `Authorization` header, or an `x-api-key` header (io.net API key).
</Note>

<Note>
  The system imposes an overall implementation-specific limit on the total size of stored secrets. If a request attempts to store a secret, or a combination of secrets, that exceeds this limit, the API will return an **HTTP 413 (Payload Too Large)** error.
</Note>

<Tip>
  When updating secrets, wildcard patterns can be used. For example, instead of specifying each *Linear* subtool individually (such as `agno__linear__get_user_details`, `agno__linear__get_issue_details`, and others), a single wildcard pattern like `agno__linear__*` can be used to apply the secret across all related Linear tools.
</Tip>

### Request body parameters:

`secret_name` – A user-defined identifier for the secret. This value is used to reference and manage the secret in subsequent operations.

`secret_value` – The confidential value associated with the secret. This value is securely stored and made available to the designated tool when access is authorized.

`tool_name` – The name of the single tool that is granted access to this secret. This field accepts only one tool identifier, not an array or list.

`tool_arg` – The specific argument of the tool that this secret applies to.

`is_default_for_tool` – A boolean flag specifying whether this secret should be automatically applied when the associated tool does not receive a value for the argument. This field is optional when using secrets in workflow YAML configurations, but required when defining secrets for built-in agents.


# Create a Secret
Source: https://io.net/docs/reference/ai-agents/secret-management-post

openapi/ai-agents/secret-management-post.json post /api/v1/secrets/
Creates or registers a new secret for use with specific tools or workflows.

This endpoint allows you to securely store a secret, associate it with a specific tool and argument, and optionally configure it as a default value when the tool is used without explicit input.

<Note>
  The API supports multiple authentication mechanisms, but only **one** needs to be provided per request. You may authenticate using **any** of the following headers, a browser-issued JWT `token`, an `Authorization` header, or an `x-api-key` header (io.net API key).
</Note>

<Warning>
  Once a secret is created, the value provided in the `secret_value` parameter cannot be retrieved or viewed again through the API. Only metadata about the secret such as its identifier, associated tool, and configuration can be viewed.
</Warning>

<Note>
  The system imposes an overall implementation-specific limit on the total size of stored secrets. If a request attempts to store a secret, or a combination of secrets, that exceeds this limit, the API will return an **HTTP 413 (Payload Too Large)** error.
</Note>

<Tip>
  When registering secrets, wildcard patterns can be used. For example, instead of specifying each *Linear* subtool individually (such as `agno__linear__get_user_details`, `agno__linear__get_issue_details`, and others), a single wildcard pattern like `agno__linear__*` can be used to apply the secret across all related Linear tools.
</Tip>

### Request body parameters:

`secret_name` – A user-defined identifier for the secret. This value is used to reference and manage the secret in subsequent operations.

`secret_value` – The confidential value associated with the secret. This value is securely stored and made available to the designated tool when access is authorized.

`tool_name` – The name of the single tool that is granted access to this secret. This field accepts only one tool identifier, not an array or list.

`tool_arg` – The specific argument of the tool that this secret applies to.

`is_default_for_tool` – A boolean flag specifying whether this secret should be automatically applied when the associated tool does not receive a value for the argument. This field is optional when using secrets in workflow YAML configurations, but required when defining secrets for built-in agents.


# Workflows Run
Source: https://io.net/docs/reference/ai-agents/workflows-run

openapi/ai-agents/workflows-run.json post /api/v1/workflows/run
Enables users to execute AI-driven workflows by submitting text inputs to one or more AI agents.

<Warning>
  **Beta Notice:** This project is in rapid development and may not be stable for production use.
</Warning>

The **Workflows Run API** allows users to execute AI-powered workflows by submitting text input and specifying one or more AI agents to process the data. This API is designed for automation, decision-making, and data analysis tasks using multiple AI capabilities.


# Workflows Schema
Source: https://io.net/docs/reference/ai-agents/workflows-schema

openapi/ai-agents/workflows-schema.json get /api/v1/workflows/schema
Get a list of default workflows.

<Warning>
  **Beta Notice:** This project is in rapid development and may not be stable for production use.
</Warning>


# Create Chat Completion
Source: https://io.net/docs/reference/ai-models/create-chat-completion

openapi/ai-models/create-chat-completion.json post /api/v1/chat/completions
Creates a model response for a given chat conversation.

<Note>
  Parameter support can differ depending on the model used to generate the response, particularly for newer reasoning models. Parameters that are only supported for reasoning models are noted below. For the current state of unsupported parameters in reasoning models, refer to the reasoning guide.
</Note>


# Create Embeddings
Source: https://io.net/docs/reference/ai-models/create-embedding

openapi/ai-models/create-embedding.json post /api/v1/embeddings
Computes an embedding vector that encodes the input text.



# Embedding Models List
Source: https://io.net/docs/reference/ai-models/get-embedding-models-list

openapi/ai-models/get-embedding-models-list.json get /api/v1/embedding-models
Retrieves a list of available models for the Embeddings API.



# Models List
Source: https://io.net/docs/reference/ai-models/get-models-list

openapi/ai-models/get-models-list.json get /api/v1/models
Retrieves a list of available models for the Chat Completions API.



# Getting Started with AI Models API
Source: https://io.net/docs/reference/ai-models/get-started-with-io-intelligence-api



<iframe title="Get Started with the IO Intelligence API" />

### Important Note on Usage Limits

Each model within **IO Intelligence** has its own value and credit consumption rate based on its complexity, capability, and computational cost.

For **plan subscribers** (*Basic*, *Professional*, or higher tiers), all model interactions draw from a **shared usage pool**. This means you can use any model available under your plan, and your total usage will count toward a single shared credit allowance — rather than having separate limits for each model.

This shared system provides maximum flexibility, allowing you to switch between models seamlessly while staying within your daily or hourly quota.

This limit is designed to ensure fair and balanced usage for all users. If you anticipate needing a higher request limit, please consider optimizing your implementation or reach out to us for assistance.

For further details on **usage limits, full breakdown of rates, and how IO Credits are billed**, refer to the [**IO Intelligence Payments**](/guides/payment/io-intelligence-payments) page.

## Introduction

You can interact with the API using HTTP requests from any programming language or by using the official Python and Node.js libraries.

To install the official Python library, run the following command:

```
pip install openai
```

To install the official Node.js library, run this command in your Node.js project directory:

```
npm install openai
```

### Example: Using the IO Intelligence API with Python

Here’s an example of how you can use the `openai Python` library to interact with the IO Intelligence API:

<CodeGroup>
  ```python openai Python theme={null}
  import openai

  client = openai.OpenAI(
      api_key="$IOINTELLIGENCE_API_KEY",
      base_url="https://api.intelligence.io.solutions/api/v1/",
  )

  response = client.chat.completions.create(
      model="meta-llama/Llama-3.3-70B-Instruct",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Hi, I am doing a project using IO Intelligence."},
      ],
      temperature=0.7,
      stream=False,
      max_completion_tokens=50
  )

  print(response.choices[0].message.content)
  ```
</CodeGroup>

This snippet demonstrates how to configure the client, send a chat completion request using the `Llama-3.3-70B-Instruct` model, and retrieve a response.

## Authentication

### API keys

IO Intelligence APIs authenticate requests using API keys. You can [generate API keys from your user](https://ai.io.net/ai/api-keys) account:

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service on your backend server.
</Warning>

Include the API key in an `Authorization` HTTP header for all API requests:

```
Authorization: Bearer \$IOINTELLIGENCE_API_KEY
```

### Example: List Available Models

Here's an example `curl` command to list all models available in IO Intelligence:

<CodeGroup>
  ```curl curl theme={null}
  curl https://api.intelligence.io.solutions/api/v1/models /
    -H "Authorization: Bearer \$IOINTELLIGENCE_API_KEY" 
  ```
</CodeGroup>

<Frame>
  <img alt="" />
</Frame>

An example response is as follows:

<CodeGroup>
  ```json json theme={null}
  {
    "object": "list",
    "data": [
      {
        "id": "meta-llama/Llama-3.3-70B-Instruct",
        "object": "model",
        "created": 1736168795,
        "owned_by": "io-intelligence",
        "root": null,
        "parent": null,
        "max_model_len": null,
        "permission": [
          {
            "id": "modelperm-30ac078e67ab456a9279d53cf83155bb",
            "object": "model_permission",
            "created": 1736755239,
            "allow_create_engine": false,
            "allow_sampling": true,
            "allow_logprobs": true,
            "allow_search_indices": false,
            "allow_view": true,
            "allow_fine_tuning": false,
            "organization": "*",
            "group": null,
            "is_blocking": false
          }
        ]
      },
      ...
    ]
  }
  ```
</CodeGroup>

## Making requests

The example below demonstrates how to make a request to the Chat Completions endpoint using `curl`. To test the API, replace `$IOINTELLIGENCE_API_KEY` with your actual API key and modify the input values as shown.

<CodeGroup>
  ```curl curl theme={null}
  curl https://api.intelligence.io.solutions/api/v1/chat/completions /
    -H "Content-Type: application/json" /
    -H "Authorization: Bearer \$IOINTELLIGENCE_API_KEY" /
    -d '{
       "model": "meta-llama/Llama-3.3-70B-Instruct",
       "messages": [{"role": "user", "content": "Say this is a test!"}],
       "reasoning_content": true,
       "temperature": 0.7
     }'
  ```
</CodeGroup>

<Frame>
  <img alt="" />
</Frame>

This example queries the `meta-llama/Llama-3.3-70B-Instruct` model to generate a chat completion for the input: "*Say this is a test!*".

### Example Response

The API should return a response as follows:

<CodeGroup>
  ```json json theme={null}
  {
    "id": "01945ea6-1d9f-9d46-efbc-2608dcc78169",
    "object": "chat.completion",
    "created": 1736754732,
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "This is a test!"
        },
        "logprobs": null,
        "finish_reason": "stop",
        "stop_reason": null
      }
    ],
    "usage": {
      "prompt_tokens": 12,
      "total_tokens": 18,
      "completion_tokens": 6,
      "prompt_tokens_details": null
    },
    "prompt_logprobs": null
  }
  ```
</CodeGroup>

### Key Details in the Response

* **finish\_reason**: Indicates why the generation stopped (e.g., "stop").
* **choices**: Contains the generated response(s). Adjust the n parameter to generate multiple response choices.


# Uploading Images
Source: https://io.net/docs/reference/ai-models/uploading-images

The io.net Intelligence API supports image inputs for vision-enabled AI models. This allows users to send images as part of their API requests, enabling advanced multimodal AI capabilities.

**Supported Models for Image Processing**

| Model Name                                 | Capabilities                                                   |
| ------------------------------------------ | -------------------------------------------------------------- |
| *meta-llama/Llama-3.2-90B-Vision-Instruct* | Multi-modal vision model supporting image understanding.       |
| *Qwen/Qwen2-VL-7B-Instruct*                | Supports both text and image-based inputs for AI interactions. |

### Sending an Image via API Request

The API allows **two methods** to send an image:

1. **Passing an Image URL** (recommended for publicly hosted images)
2. **Sending a Base64 Encoded Image** (for local images)

<CodeGroup>
  ```python Passing a URL theme={null}
  import requests

  url = "https://api.intelligence.io.solutions/api/v1/chat/completions"

  headers = {
      "Authorization": "Bearer \$IOINTELLIGENCE_API_KEY",
      "Content-Type": "application/json"
  }

  data = {
      "model": "meta-llama/Llama-3.2-90B-Vision-Instruct", 
      "messages": [
          {"role": "system", "content": "You are an AI assistant."},
          {"role": "user", "content": [
              {"type": "text", "text": "What is in this image?"},
              {"type": "image_url", "image_url": {"url": "https://your-image-url.com/image.jpg"}}
          ]}
      ]
  }

  response = requests.post(url, json=data, headers=headers)
  print(response.json())
  ```

  ```python Passing a Base64 encoded image theme={null}
  import requests
  import base64

  url = "https://api.intelligence.io.solutions/api/v1/chat/completions"

  headers = {
      "Authorization": "Bearer \$IOINTELLIGENCE_API_KEY",
      "Content-Type": "application/json"
  }

  image_url = "path_to_your_image.jpg"

  image_response = requests.get(image_url)
  if image_response.status_code == 200:
      image_data = image_response.content  # Get raw image bytes
  else:
      print("Error: Unable to download image")
      exit()

  base64_image = base64.b64encode(image_data).decode("utf-8")

  data = {
      "model": "meta-llama/Llama-3.2-90B-Vision-Instruct", 
      "messages": [
          {"role": "system", "content": "You are an AI assistant."},
          {"role": "user", "content": [
              {"type": "text", "text": "What is in this image?"},
              {"type": "image", "image": base64_image} 
          ]}
      ]
  }

  response = requests.post(url, json=data, headers=headers)

  try:
      print(response.json())  # Parse JSON response
  except requests.exceptions.JSONDecodeError:
      print("Error: Unable to parse response. Raw response:", response.text)
  ```
</CodeGroup>

<Info>
  The image URL must be publicly accessible. Private or authentication-required URLs will not work.
</Info>

### Image Input Requirements

To ensure successful processing, images must meet the following requirements:

| Requirement           | Details                                          |
| --------------------- | ------------------------------------------------ |
| *Format*              | JPEG, PNG, WEBP, or GIF (static)                 |
| *Max File Size*       | 20MB                                             |
| *Resolution*          | At least 512x512 pixels (recommended)            |
| *Max Dimensions*      | 4096×4096 pixels                                 |
| *Accessibility*       | If using a URL, ensure it is publicly accessible |
| *Multi-Image Support* | Up to 10 images per request                      |

**Best Practices for Image Uploads**

* **Optimize File Size**: While the maximum limit is 20MB, smaller files (1-5MB) ensure faster processing.
* **Use Clear Images**: Avoid blurry or low-resolution images for better AI analysis.
* **Ensure Public URLs**: If passing a URL, test it in a browser to confirm that it is accessible.

### Expected API Response

Upon successful submission, the API will return a structured response with AI-generated insights based on the image.

**Example Response:**

<CodeGroup>
  ```json json theme={null}
  {
      "id": "chatcmpl-abc123",
      "object": "chat.completion",
      "created": 1710456789,
      "model": "meta-llama/Llama-3.2-90B-Vision-Instruct",
      "choices": [
          {
              "index": 0,
              "message": {
                  "role": "assistant",
                  "content": "This is an image of a cat sitting on a table."
              },
              "finish_reason": "stop"
          }
      ],
      "usage": {
          "prompt_tokens": 120,
          "completion_tokens": 20,
          "total_tokens": 140
      }
  }
  ```
</CodeGroup>

### Common Issues & Troubleshooting

| Issue                                                  | Possible Cause                      | Solution                                                  |
| ------------------------------------------------------ | ----------------------------------- | --------------------------------------------------------- |
| *"An image? I'm in text format, so I can't see it..."* | Model does not support image input. | Ensure you are using one of the supported vision models.  |
| *"Invalid image format"*                               | Image not encoded properly.         | Convert image to base64 before sending.                   |
| *"Unauthorized"*                                       | API key is missing or incorrect.    | Check that your API key is valid and correctly formatted. |


# Check available replicas per location
Source: https://io.net/docs/reference/caas/available-replicas

openapi/caas/available-replicas.json get /enterprise/v1/io-cloud/caas/available-replicas
Returns the number of deployable replicas in each location based on selected hardware type and GPU count per container, useful for matching supply to workload needs.

By leveraging this endpoint, it's possible to discover the current supply on the platform that fits workload requirements and use this data during the deployment process.


# Check maximum GPUs per container
Source: https://io.net/docs/reference/caas/check-maximum-gpus-per-container

openapi/caas/check-maximum-gpus-per-container.json get /enterprise/v1/io-cloud/caas/hardware/max-gpus-per-container
Returns the maximum number of GPUs available per hardware type across all locations, helping to determine deployment limits by hardware.

By leveraging this endpoint, it's possible to discover the current supply on the platform that fits workload requirements and use this data during the deployment process.


# Container Job Details
Source: https://io.net/docs/reference/caas/container-job-details

openapi/caas/container-job-details.json get /enterprise/v1/io-cloud/caas/deployment/{deployment_id}/containers-jobs/{container_id}
Inspect job-level details of a specific container within a deployment.



# Container Logs
Source: https://io.net/docs/reference/caas/container-logs

openapi/caas/container-logs.json get /enterprise/v1/io-cloud/caas/deployment/{deployment_id}/log/{container_id}
Access real-time or historical logs for a specific container in a deployment.

## Fetching Container Logs via API

* The logs endpoint always **produces a chunked response** - it’s a **stream**.
* Specifically, it uses **Server-Sent Events (SSE)** for streaming logs.
* **Do not** use r`esponse.json();` consume the logs line-by-line.
* Currently, the **API spec is incomplete**:
  * `offset` and `stream type` query parameters are missing.
  * Public API specs need a full review to match Swagger; other fields may be missing.

### Python Example

```python theme={null}
import requests

# Replace with your Deployment and Log IDs
deployment_id = "Deployment ID"
log_id = "Log ID"

url = "https://api.io.solutions/enterprise/v1/io-cloud/caas/deployment/{deployment_id}/log/{log_id}"
headers = {
    "X-API-KEY": "YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Use stream=True to handle the response incrementally
with requests.get(url, headers=headers, stream=True) as r:
    r.raise_for_status()
    for line in r.iter_lines():
        if line:
            print(line.decode("utf-8"))
```

### Notes

* Treat all responses as **streams**, not JSON.
* Each line corresponds to a log entry (stdout/stderr), as seen in the UI.
* SSE allows for real-time log consumption for monitoring/debugging.


# Deploy a Container
Source: https://io.net/docs/reference/caas/deploy-a-container

openapi/caas/deploy-a-container.json post /enterprise/v1/io-cloud/caas/deploy
This endpoint is used to deploy a CaaS cluster on IO.NET infrastructure. The container must expose an HTTP server on a single port, and it must run within a single node.

## **Important Constraints:**

* **Only HTTP server containers are supported.**
* **Only a single traffic port is allowed.**
* **Each container must use a minimum of 1 GPU, with no maximum GPU limit.**
  * Multi-node GPU configurations are not supported at this time.


# Destroy Container
Source: https://io.net/docs/reference/caas/destroy-container

openapi/caas/destroy-container.json delete /enterprise/v1/io-cloud/caas/deployment/{deployment_id}
Shut down a deployment and release associated resources.



# Extend Deployment Duration
Source: https://io.net/docs/reference/caas/extend-deployment-duration

openapi/caas/extend-deployment-duration.json post /enterprise/v1/io-cloud/caas/deployment/{deployment_id}/extend
Increase the runtime of an existing deployment without redeploying.



# Get All Deployments
Source: https://io.net/docs/reference/caas/get-all-deployments

openapi/caas/get-all-deployments.json get /enterprise/v1/io-cloud/caas/deployments
View a list of all your active and past deployments.



# Get Deployment Details
Source: https://io.net/docs/reference/caas/get-deployment-details

openapi/caas/get-deployment-details.json get /enterprise/v1/io-cloud/caas/deployment/{deployment_id}
Retrieve detailed information about a specific deployment.



# Getting Started with CaaS API
Source: https://io.net/docs/reference/caas/get-started-with-caas-api

The CaaS API lets you programmatically deploy and manage high-performance containerized workloads on io.net’s decentralized GPU network.

<iframe title="Get Started with CaaS API" />

## Generate an API key

You can obtain an API key for IO Cloud in two ways:

1. Via the web interface
2. By using a two-step process (first generate a JWT token, then request the API key using cURL).

### Option 1: Generate an API Key via Web Interface

IO Clouds APIs authenticate requests using API keys. You can [generate API keys from your user](https://ai.io.net/ai/api-keys) account. **Note: When generating an API key, make sure to specify the associated IO Cloud project.**

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service on your backend server.
</Warning>

### Option 2: Generate an API Key Using a JWT Token

#### Step 1. Get a JWT Token

IO's API is built around [RESTful](https://en.wikipedia.org/wiki/REST) principles. You can use IO's APIs to gain insights into different elements of our network.

To use IO's APIs, you must supply a JWT token in the header of your request. Follow the instructions below to generate a token:

1. Go to **io.net** > **IO ID** > **io.cloud** tab.
2. In the UI, right-click and select **Inspect**.
3. In the Inspect tool, click **Network**.
4. Refresh the **io.cloud** page.
5. In the list of elements, click **Devices**.
6. Scroll down to the **Request Headers** section.
7. Copy and store the **Token**.

<Info>
  This token is valid for 21 days.
</Info>

<Frame>
  <img alt="" />
</Frame>

#### Step 2. Generate an API Key via `cURL`

Use the **JWT token** to request your API key:

<CodeGroup>
  ```curl curl theme={null}
  curl -X POST 'https://api.io.solutions/v1/api-keys/' /
    -H 'accept: application/json' /
    -H 'token: $JWT_TOKEN' /
    -H 'Content-Type: application/json' /
    -d '{
      "description": "API Key Name",
      "expires_at": "2025-07-17T19:54:36.418Z",
      "project": "io-cloud",
      "scopes": ["all"]
  }'
  ```
</CodeGroup>

Use the returned key with the `X-API-KEY` header in your requests.

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service on your backend server.
</Warning>

<Frame>
  <img alt="" />
</Frame>

## Making requests

<Danger>
  Accessing APIs requires IO Credits. Please make sure to request IO credits before using any API endpoints. Contact support or visit the [IO Credits](/guides/payment/io-credits) page for more information.
</Danger>

Include the API key in an `Authorization` HTTP header for all API requests:

```
Authorization: X-API-KEY \$IOCLOUD_API_KEY
```

Replace `$IOCLOUD_API_KEY` with your actual **API key.**

### Example: Check Available Replicas per Location

Here is an example `cURL` command to check available replicas per location in IO Cloud:

<CodeGroup>
  ```curl curl theme={null}
  curl https://api.io.solutions/enterprise/v1/io-cloud/caas/available-replicas?hardware_id={hardawer_id}&hardware_qty={hardware_qty} /
    -H "X-API-KEY: \$IOCLOUD_API_KEY" 
  ```
</CodeGroup>

<Frame>
  <img alt="" />
</Frame>

This request should return a response as follows:

<CodeGroup>
  ```json json theme={null}
  {
    "data": [
      {
        "id": 0,
        "iso2": "string",
        "name": "string",
        "available_replicas": 0
      }
    ]
  }
  ```
</CodeGroup>


# List Deployment Containers
Source: https://io.net/docs/reference/caas/list-deployment-containers

openapi/caas/list-deployment-containers.json get /enterprise/v1/io-cloud/caas/deployment/{deployment_id}/containers
Get information about all containers running within a specific deployment.



# Deployment Price Check
Source: https://io.net/docs/reference/caas/price-estimation

openapi/caas/price-estimation.json get /enterprise/v1/io-cloud/caas/price
Calculates the estimated deployment cost based on selected location, hardware, GPU count, duration, and number of replicas. Returns a detailed price breakdown.

**Once** `location_id` **and** `hardware_id`**are known, you can estimate the deployment cost based on the desired configuration.**

As a result, a detailed price breakdown will be returned.\
**This step is optional.**


# Update Deployment Configuration
Source: https://io.net/docs/reference/caas/update-deployment-configuration

openapi/caas/update-deployment-configuration.json patch /enterprise/v1/io-cloud/caas/deployment/{deployment_id}
Modify runtime container settings such as environment variables or entrypoints.

<Warning>
  Note: Hardware parameters (like hardware\_id, location\_id, and replica\_count) cannot be changed.
</Warning>

<Note>Note: Although earlier examples may use a `container_config` wrapper, the current API expects all configuration fields at the top level of the request body. Including a `container_config` key will result in a "`extra_forbidden`" error.</Note>


# Block Rewards Summary
Source: https://io.net/docs/reference/io-explorer/block-rewards-summary

openapi/io-explorer/block-rewards-summary.json get /v1/io-blocks/devices/{device_id}/block-rewards-summary/{from_date}/{to_date}
The Block Rewards Summary endpoint returns insight on the block rewards associated with a specific device. This includes, but is not limited to, successful rewards, failed and missed rewards, and an earnings summary - given a specific date range. 



# Device Details for a Block
Source: https://io.net/docs/reference/io-explorer/device-details-for-a-block

openapi/io-explorer/device-details-for-a-block.json get /v1/io-blocks/blocks/{block_id}/workers/{device_id}
The Deice Details for a Block endpoint returns granular information about a device in the context of a specific block reward. It offers details about Block Reward challenges, the outcome, and details about the device.



# Device Summary
Source: https://io.net/docs/reference/io-explorer/device-summary

openapi/io-explorer/device-summary.json get /v1/io-explorer/devices/{device_id}/summary
The Device Summary endpoint provides detailed information on a specific device. This allows you to view the device's status, aspects of connectivity, compute hours served, earnings and more.



# Device Details
Source: https://io.net/docs/reference/io-explorer/get-device-details

openapi/io-explorer/get-device-details.json get /v1/io-explorer/devices/{device_id}/details
The Device Details endpoint provides comprehensive insights into a specific device, including its status, connectivity, job activity, rewards earned, hire rate, and other key performance metrics.



# Getting Started with IO Explorer API
Source: https://io.net/docs/reference/io-explorer/getting-started-with-your-api

Use IO Explorer APIs to gain insight into the different elements of our network.

<iframe title="Get Started with the IO Explorer API" />

### Authentication

To use io.net APIs, you must supply a *JWT token* in the header of your request.

Follow the instructions below to generate a token:

1. Go to io.net > **Get Started** > **IO Explore** > and the **Workers** tab.
2. In the **UI**, right-click and select **Inspect**.
3. In the **Inspect** tool, click **Network**.
4. Refresh the **Workers** page.
5. In the list of elements, click **Devices**.
6. Scroll down to the **Request Headers** section.
7. Copy and store the token.

<Info>
  The token is valid for 21 days.
</Info>

<Frame>
  <img alt="" />
</Frame>

### Make an API Call

You can use **cURL** to make API requests. Make sure you replace the following variables:

* `{device_id}`: Your actual **Device ID**, which you can copy from the *Device View* page.

  <Frame>
    <img alt="" />
  </Frame>
* `{your_token}` : The **Token** you previously copied using the **Inspect Tool**.

```bash theme={null}
curl X GET "https://api.io.solutions/v1/io-explorer/devices/{device_id}/details"
    -H "Token: {your_token}"
```

### Rate Limits

The base io.net API rate limit is as follows:

* 150 reqs / 10 second (umbrella Rate Limit on IO Explorer)
* **Summary:** 100 / 5 minutes
* **Details:** 100 / 5 minutes
* **Search:** 80 / 1 minute


# Device Object Reference
Source: https://io.net/docs/reference/io-explorer/objects

Defines the structure, attributes, and metrics of a Device within the IO Network. Includes details on hardware specs, network performance, compliance, and job history used for monitoring and rewards calculation.

### Device Object

The **Device Object** represents a compute node within the IO Network, typically a machine or worker running one or more GPUs. It provides the foundational schema for describing devices that contribute compute power to the distributed network.

Each device entry captures details about its hardware, performance metrics, network characteristics, geographic location, and SOC 2 compliance. This object also tracks job-level details such as compute minutes, uptime, and earnings, this allows for transparent performance analytics, availability tracking, and compensation calculation.

***

## Structure Overview

A **Device** includes:

* **Identification** – Unique ID, hardware name, and quantity
* **Performance Metrics** – Uptime, speed, and availability stats
* **Geographic Info** – Location name, ISO code, and country icon
* **Compliance** – SOC 2 certification flag
* **Job History** – Records of compute jobs, earnings, and status

***

## Core Attributes

<ParamField type="string">
  The unique identifier for your device.
</ParamField>

<ParamField type="string">
  The name of the hardware model used in the device, such as 'RTX A6000'.
</ParamField>

<ParamField type="integer">
  The number of hardware components (GPUs) in the device.
</ParamField>

<ParamField type="string">
  The performance tier assigned to the device based on its network speed.
</ParamField>

***

## Performance Metrics

<ParamField type="integer">
  The percentage of time the device was unavailable.
</ParamField>

<ParamField type="integer">
  The average download speed, measured in megabits per second (Mbps).
</ParamField>

<ParamField type="integer">
  The average upload speed, measured in megabits per second (Mbps).
</ParamField>

<ParamField type="object">
  A breakdown of downtime occurrences by date.

  <Expandable title="properties">
    <ParamField type="string">
      Date of downtime in `YYYY-MM-DD` format.
    </ParamField>

    <ParamField type="array">
      Each entry represents a day's downtime data.

      <Expandable title="properties">
        <ParamField type="number">
          Total downtime duration in seconds.
        </ParamField>

        <ParamField type="string">
          Human-readable note summarizing downtime (e.g., “down for 0 days and 3 hours and 23 minutes”).
        </ParamField>

        **Example**

        ```json theme={null}
        {
          "2023-09-11": {
            "downtime": 281.508,
            "note": "down for 0 days and 0 hours and 4 minutes"
          },
          "2023-09-12": {
            "downtime": 12193.385,
            "note": "down for 0 days and 3 hours and 23 minutes"
          }
        }
        ```
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

***

## Location & Branding

<ParamField type="string">
  The country ISO code (e.g., `CA` for Canada).
</ParamField>

<ParamField type="string">
  The name of the country or region where the device is located.
</ParamField>

<ParamField type="string">
  The URL of the location icon.
</ParamField>

<ParamField type="string">
  The web address of the device’s associated brand icon.
</ParamField>

***

## Compliance & Status

<ParamField type="boolean">
  Indicates whether the device meets SOC 2 (System and Organization Controls 2) compliance standards.
</ParamField>

<ParamField type="string">
  The current status of the device or job running on it.
</ParamField>

***

## Job History

<ParamField type="array">
  An array of job entries representing each compute job executed on this device.

  <Expandable title="properties">
    <ParamField type="integer">
      Total minutes a customer hired the device.
    </ParamField>

    <ParamField type="integer">
      Total minutes the device was active during the job.
    </ParamField>

    <ParamField type="integer">
      Total \$IO earnings for this job.
    </ParamField>

    <ParamField type="integer">
      Earnings deducted (slashed) for downtime or failed performance.
    </ParamField>

    <ParamField type="integer">
      The full payment rate if the device achieved 100% uptime.
    </ParamField>

    <ParamField type="integer">
      Percentage of uptime during the job.
    </ParamField>

    <ParamField type="datetime string">
      UTC timestamp when the job started.
    </ParamField>

    <ParamField type="datetime string">
      UTC timestamp when the job ended.
    </ParamField>

    <ParamField type="string">
      Job status (e.g., `pending`, `running`, `completed`).
    </ParamField>

    <ParamField type="string">
      Cluster ID associated with the job.
    </ParamField>

    **Example**

    ```json theme={null}
    {
      "jobs": [
        {
          "compute_minutes_hired": 300,
          "compute_minutes_served": 0,
          "earned": 0,
          "end_time": "2023-09-12 00:00:00",
          "for": "e242cd76-9e65-4de1-b3ec-1cb8b002b38d",
          "slashed": 0,
          "start_time": "2023-09-12 00:00:00",
          "status": "pending",
          "total_hire_rate": 10.8,
          "uptime_percent": 100
        }
      ]
    }
    ```
  </Expandable>
</ParamField>


# PoW Summary
Source: https://io.net/docs/reference/io-explorer/pow-summary

openapi/io-explorer/pow-summary.json get /v1/io-explorer/devices/{device_id}/pow-summary
This PoW Summary endpoint returns information about the Proof of Work challenges for a device.



# Overview
Source: https://io.net/docs/reference/rag/chunks

The R2R Chunks API defines how processed document segments, called chunks, are created, managed, and searched. It provides endpoints for semantic retrieval, knowledge graph extraction, and metadata-driven filtering to power advanced AI and RAG workflows.

A **Chunk** in R2R represents a processed segment of content derived from a parent **Document**. Chunks are the **core unit of retrieval** within the system, serving as the foundation for **semantic search**, **knowledge graph construction**, and **Retrieval-Augmented Generation (RAG)** workflows.

Each chunk includes the following components:

* **Text content** — the extracted or generated portion of the source document.
* **Metadata** — contextual information such as source, timestamp, or author.
* **Optional vector embeddings** — numerical representations used for similarity search and reasoning.

Chunks are automatically generated during document ingestion and are optimized for:

* Semantic search and retrieval
* Knowledge graph relationship extraction
* Vector similarity comparison
* Metadata-based filtering and organization

## API Endpoints

| Method | Endpoint                                              | Description                                    |
| ------ | ----------------------------------------------------- | ---------------------------------------------- |
| GET    | [/chunks](/reference/rag/chunks/list-chunks)          | List chunks with pagination and filtering.     |
| POST   | [/chunks/search](/reference/rag/chunks/search-chunks) | Perform semantic search with advanced filters. |
| GET    | [/chunks/](/reference/rag/chunks/get-chunk-by-id)     | Retrieve a chunk by its ID.                    |
| POST   | [/chunks/](/reference/rag/chunks/update-chunk)        | Update chunk content or metadata.              |
| DELETE | [/chunks/](/reference/rag/chunks/delete-chunk)        | Delete a specific chunk.                       |


# Delete Chunk
Source: https://io.net/docs/reference/rag/chunks/delete-chunk

openapi/rag-chunks/delete-chunk.json delete /api/r2r/v3/chunks/{id}
Delete a specific chunk by ID.

Delete a specific chunk by ID. This permanently removes the chunk and its associated vector embeddings. The parent document remains unchanged. Users can only delete chunks they own unless they are superusers.


# Retrieve Chunk
Source: https://io.net/docs/reference/rag/chunks/get-chunk-by-id

openapi/rag-chunks/get-chunk-by-id.json get /api/r2r/v3/chunks/{id}
Get a specific chunk by its ID.

Returns the chunk’s content, metadata, and associated document/collection information. Users can only retrieve chunks they own or have access to through collections.


# List Chunks
Source: https://io.net/docs/reference/rag/chunks/list-chunks

openapi/rag-chunks/list-chunks.json get /api/r2r/v3/chunks
List chunks with pagination support.

Returns a paginated list of chunks that the user has access to. Results can be filtered and sorted based on various parameters. Vector embeddings are only included if specifically requested. Regular users can only list chunks they own or have access to through collections. Superusers can list all chunks in the system.


# Search Chunks
Source: https://io.net/docs/reference/rag/chunks/search-chunks

openapi/rag-chunks/search-chunks.json post /api/r2r/v3/chunks/search
Perform a semantic search query over all stored chunks.

This endpoint allows for complex filtering of search results using PostgreSQL-based queries. Filters can be applied to various fields such as document\_id, and internal metadata values.

Allowed operators include `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`, `ilike`, `in`, and `nin`.


# Update Chunk
Source: https://io.net/docs/reference/rag/chunks/update-chunk

openapi/rag-chunks/update-chunk.json post /api/r2r/v3/chunks/{id}
Update an existing chunk’s content and/or metadata.

The chunk’s vectors will be automatically recomputed based on the new content. Users can only update chunks they own unless they are superusers.


# Overview
Source: https://io.net/docs/reference/rag/collections

The R2R Collections API enables structured organization, sharing, and access control for documents and their related chunks. It provides endpoints to create, manage, and collaborate on collections, supporting team workflows, permission management, and intelligent content organization.

A **Collection** in R2R is a **logical grouping mechanism** that organizes and manages access to documents and their associated chunks. Collections serve as the **core organizational unit** for content management, access control, and collaboration across users and teams.

They provide a structured way to categorize documents, enforce permissions, and enable seamless sharing and processing of related data within the R2R ecosystem.

### Key Capabilities

Collections in R2R enable:

* **Organizational structure** for managing documents.
* **Access control and permission management** for secure data governance.
* **Group-based content sharing** across teams or users.
* **Document categorization** for better organization and retrieval.
* **User collaboration** for joint access and workflow execution.

## API Endpoints

| Method | Endpoint                                                                                | Description                                                                        |
| ------ | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| POST   | [/collections](/reference/rag/collections/create-a-new-collection)                      | Create a new collection.                                                           |
| GET    | [/collections](/reference/rag/collections/list-collections)                             | List collections with pagination and filtering.                                    |
| GET    | [/collections/](/reference/rag/collections/get-collection-by-id)                        | Retrieve details of a specific collection.                                         |
| POST   | [/collections/](/reference/rag/collections/update-collection)                           | Update an existing collection.                                                     |
| DELETE | [/collections/](/reference/rag/collections/delete-collection)                           | Delete a specific collection.                                                      |
| GET    | [/collections//documents](/reference/rag/collections/list-documents-in-collection)      | List documents within a collection.                                                |
| POST   | [/collections//documents/](/reference/rag/collections/add-document-to-collection)       | Add a document to a collection.                                                    |
| DELETE | [/collections//documents/](/reference/rag/collections/remove-document-from-collection)  | Remove a document from a collection.                                               |
| POST   | [/collections//extract](/reference/rag/collections/trigger-extraction-for-a-collection) | Extract entities and relationships from all unprocessed documents in a collection. |
| GET    | [/collections//users](/reference/rag/collections/list-users-in-a-collection)            | List users who have access to a collection.                                        |
| POST   | [/collections//users/](/reference/rag/collections/add-user-to-collection)               | Grant a user access to a collection.                                               |
| DELETE | [/collections//users/](/reference/rag/collections/remove-user-from-collection)          | Remove a user's access to a collection.                                            |
| GET    | [/collections/name/](/reference/rag/collections/get-collection-by-name)                 | Retrieve a collection by its name.                                                 |


# Add document to collection
Source: https://io.net/docs/reference/rag/collections/add-document-to-collection

openapi/rag-collections/add-document-to-collection.json post /api/r2r/v3/collections/{id}/documents/{document_id}
Add a document to a collection.



# Add user to collection
Source: https://io.net/docs/reference/rag/collections/add-user-to-collection

openapi/rag-collections/add-user-to-collection.json post /api/r2r/v3/collections/{id}/users/{user_id}
This endpoint grants a user access to a specific collection.

The authenticated user must have admin permissions for the collection to add new users.


# Create a new collection
Source: https://io.net/docs/reference/rag/collections/create-a-new-collection

openapi/rag-collections/create-a-new-collection.json post /api/r2r/v3/collections
Create a new collection and automatically add the creating user to it.

This endpoint allows authenticated users to create a new collection with a specified name and optional description. The user creating the collection is automatically added as a member.


# Delete Collection
Source: https://io.net/docs/reference/rag/collections/delete-collection

openapi/rag-collections/delete-collection.json delete /api/r2r/v3/collections/{id}
Delete an existing collection.

This endpoint allows deletion of a collection identified by its UUID. The user must have appropriate permissions to delete the collection. Deleting a collection removes all associations but does not delete the documents within it.


# Get collection details
Source: https://io.net/docs/reference/rag/collections/get-collection-by-id

openapi/rag-collections/get-collection-by-id.json get /api/r2r/v3/collections/{id}
Get details of a specific collection.

This endpoint retrieves detailed information about a single collection identified by its UUID. The user must have access to the collection to view its details.


# Get collection by name
Source: https://io.net/docs/reference/rag/collections/get-collection-by-name

openapi/rag-collections/get-collection-by-name.json get /api/r2r/v3/collections/name/{collection_name}
Retrieve a collection by its (owner_id, name) combination.

The authenticated user can only fetch collections they own, or, if superuser, from anyone.


# List collections
Source: https://io.net/docs/reference/rag/collections/list-collections

openapi/rag-collections/list-collections.json get /api/r2r/v3/collections
Returns a paginated list of collections the authenticated user has access to.

Results can be filtered by providing specific collection IDs. Regular users will only see collections they own or have access to. Superusers can see all collections. The collections are returned in order of last modification, with most recent first.


# List documents in collection
Source: https://io.net/docs/reference/rag/collections/list-documents-in-collection

openapi/rag-collections/list-documents-in-collection.json get /api/r2r/v3/collections/{id}/documents
Get all documents in a collection with pagination and sorting options.

This endpoint retrieves a paginated list of documents associated with a specific collection. It supports sorting options to customize the order of returned documents.


# List users in collection
Source: https://io.net/docs/reference/rag/collections/list-users-in-a-collection

openapi/rag-collections/list-users-in-a-collection.json get /api/r2r/v3/collections/{id}/users
Get all users in a collection with pagination and sorting options.

This endpoint retrieves a paginated list of users who have access to a specific collection. It supports sorting options to customize the order of returned users.


# Remove document from collection
Source: https://io.net/docs/reference/rag/collections/remove-document-from-collection

openapi/rag-collections/remove-document-from-collection.json delete /api/r2r/v3/collections/{id}/documents/{document_id}
This endpoint removes the association between a document and a collection.

It does not delete the document itself. The user must have permissions to modify the collection.


# Remove user from collection
Source: https://io.net/docs/reference/rag/collections/remove-user-from-collection

openapi/rag-collections/remove-user-from-collection.json delete /api/r2r/v3/collections/{id}/users/{user_id}
This endpoint revokes a user's access to a specific collection.

The authenticated user must have admin permissions for the collection to remove users.


# Extract entities and relationships
Source: https://io.net/docs/reference/rag/collections/trigger-extraction-for-a-collection

openapi/rag-collections/trigger-extraction-for-a-collection.json post /api/r2r/v3/collections/{id}/extract
Extracts entities and relationships from a document.

The entities and relationships extraction process involves:

1. Parsing documents into semantic chunks
2. Extracting entities and relationships using LLMs


# Update Collection
Source: https://io.net/docs/reference/rag/collections/update-collection

openapi/rag-collections/update-collection.json post /api/r2r/v3/collections/{id}
Update an existing collection's configuration.

This endpoint allows updating the name and description of an existing collection. The user must have appropriate permissions to modify the collection.


# Overview
Source: https://io.net/docs/reference/rag/conversations

The R2R Conversations API enables threaded, context-aware exchanges between users or AI agents. It offers endpoints to create, manage, and update conversations and messages, supporting branching dialogue, metadata attachment, and message history tracking.

A **Conversation** in R2R represents a **threaded exchange of messages** that can **branch into multiple paths**, allowing for dynamic, structured dialogue management. Conversations help maintain **context**, preserve **message history**, and support **branching discussions** for more flexible interactions across users, agents, or systems.

They form the foundation for managing dialogue flows and conversational AI interactions within R2R.

### Key Capabilities

Conversations in R2R provide:

* **Threaded message management** for organized discussions.
* **Message editing** with full history preservation for version tracking.
* **Metadata attachment** to enrich messages with contextual details.
* **Context maintenance** across dialogue turns and branches.

## API Endpoints

| Method | Endpoint                                                                                 | Description                                            |
| ------ | ---------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| POST   | [/conversations](/reference/rag/conversations/create-a-new-conversation)                 | Create a new conversation.                             |
| GET    | [/conversations](/reference/rag/conversations/list-conversations)                        | List conversations with pagination.                    |
| GET    | [/conversations/](/reference/rag/conversations/get-conversation-details)                 | Retrieve details of a specific conversation.           |
| POST   | [/conversations/](/reference/rag/conversations/update-conversation)                      | Update an existing conversation.                       |
| DELETE | [/conversations/](/reference/rag/conversations/delete-a-conversation)                    | Delete a conversation.                                 |
| POST   | [/conversations//messages](/reference/rag/conversations/add-a-message-to-a-conversation) | Add a new message to a conversation.                   |
| POST   | [/conversations//messages/](/reference/rag/conversations/update-a-message)               | Update the content or metadata of an existing message. |


# Add message to conversation
Source: https://io.net/docs/reference/rag/conversations/add-a-message-to-a-conversation

openapi/rag-conversations/add-a-message-to-a-conversation.json post /api/r2r/v3/conversations/{id}/messages
Add a new message to a conversation. This endpoint adds a new message to an existing conversation.



# Create a new conversation
Source: https://io.net/docs/reference/rag/conversations/create-a-new-conversation

openapi/rag-conversations/create-a-new-conversation.json post /api/r2r/v3/conversations
Create a new conversation. This endpoint initializes a new conversation for the authenticated user.



# Delete a conversation
Source: https://io.net/docs/reference/rag/conversations/delete-a-conversation

openapi/rag-conversations/delete-a-conversation.json delete /api/r2r/v3/conversations/{id}
Delete an existing conversation. This endpoint deletes a conversation identified by its UUID.



# Get conversation details
Source: https://io.net/docs/reference/rag/conversations/get-conversation-details

openapi/rag-conversations/get-conversation-details.json get /api/r2r/v3/conversations/{id}
Get details of a specific conversation. This endpoint retrieves detailed information about a single conversation identified by its UUID.



# List conversations
Source: https://io.net/docs/reference/rag/conversations/list-conversations

openapi/rag-conversations/list-conversations.json get /api/r2r/v3/conversations
List conversations with pagination and sorting options. This endpoint returns a paginated list of conversations for the authenticated user.



# Update message in conversation
Source: https://io.net/docs/reference/rag/conversations/update-a-message

openapi/rag-conversations/update-a-message.json post /api/r2r/v3/conversations/{id}/messages/{message_id}
Update an existing message in a conversation. This endpoint updates the content of an existing message in a conversation.



# Update conversation
Source: https://io.net/docs/reference/rag/conversations/update-conversation

openapi/rag-conversations/update-conversation.json post /api/r2r/v3/conversations/{id}
Update an existing conversation. This endpoint updates the name of an existing conversation identified by its UUID.



# Overview
Source: https://io.net/docs/reference/rag/documents

The R2R Documents API handles ingestion, management, and enrichment of digital content. It enables transforming files, text, and media into structured, searchable knowledge objects for RAG, semantic retrieval, and AI-driven workflows.

A **Document** in R2R is the system’s **digital representation of any ingested content**—including PDFs, text files, web pages, images, and audio. It serves as the **central container** for all downstream data objects such as **Chunks**, **Entities**, and **Relationships**, forming the foundation for R2R’s knowledge processing pipeline.

Documents transform raw content into structured, searchable, and analyzable knowledge that powers **Retrieval-Augmented Generation (RAG)** and **agentic workflows**.

### Key Processes

Documents in R2R support several key stages of processing:

* **Ingestion** — Accepts multiple input formats (`.pdf`, `.docx`, `.txt`, `.png`, `.mp3`, etc.) via file upload, raw text, or predefined chunks.
* **Chunking** — Splits document content into smaller, retrievable **Chunks** for semantic search and analysis.
* **Metadata & Collections** — Associates documents with descriptive metadata (e.g., title, source) and organizes them into **Collections** for access control and sharing.
* **Enrichment (Optional)** — Extracts **Entities** and **Relationships** to build knowledge graphs or generates **embeddings** for semantic search.
* **Status Tracking** — Monitors ingestion, enrichment, and extraction progress for transparency and error handling.

## API Endpoints

| Method   | Endpoint                                                                          | Description                                                              |
| -------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `POST`   | [/documents](/reference/rag/documents/list-all-documents)                         | Ingest new information (file, text, or chunks) as a document.            |
| `GET`    | [/documents](/reference/rag/documents/upload-and-ingest-a-document)               | List existing documents with pagination and filtering.                   |
| `GET`    | [/documents/](/reference/rag/documents/get-document-by-id)                        | Retrieve metadata, ingestion status, or details for a specific document. |
| `GET`    | [/documents//download](/reference/rag/documents/download-original-file)           | Download the original source file of a document.                         |
| `GET`    | [/documents//chunks](/reference/rag/documents/get-document-chunks)                | List the text *Chunks* generated from a document’s content.              |
| `PATCH`  | [/documents//metadata](/reference/rag/documents/update-document-metadata-partial) | Add or update metadata for a document.                                   |
| `PUT`    | [/documents//metadata](/reference/rag/documents/replace-document-metadata)        | Replace all metadata for a document.                                     |
| `DELETE` | [/documents/](/reference/rag/documents/delete-document-by-id)                     | Delete a document and its associated data.                               |
| `DELETE` | [/documents/by-filter](/reference/rag/documents/delete-documents-by-filter)       | Delete multiple documents that match a filter.                           |
| `POST`   | [/documents/search](/reference/rag/documents/search-documents)                    | Search across generated document summaries.                              |
| `GET`    | [/documents/download\_zip](/reference/rag/documents/download-documents-as-zip)    | Download multiple original document files as a zip archive.              |
| `POST`   | [/documents//extract](/reference/rag/documents/extract-entities)                  | Start entity and relationship extraction for a document.                 |
| `GET`    | [/documents//entities](/reference/rag/documents/get-extracted-entities)           | List *Entities* identified within a document.                            |
| `GET`    | [/documents//relationship](/reference/rag/documents/get-relationships)            | List *Relationships* identified within a document.                       |
| `POST`   | [/documents//deduplicate](/reference/rag/documents/deduplicate-document)          | Start entity deduplication for a document.                               |


# Deduplicate entities
Source: https://io.net/docs/reference/rag/documents/deduplicate-document

openapi/rag-documents/deduplicate-document.json post /api/r2r/v3/documents/{id}/deduplicate
Deduplicates entities from a document.



# Delete a document
Source: https://io.net/docs/reference/rag/documents/delete-document-by-id

openapi/rag-documents/delete-document-by-id.json delete /api/r2r/v3/documents/{id}
Delete a specific document. All chunks corresponding to the document are deleted, and all other references to the document are removed.

**NOTE**: Deletions do not yet impact the knowledge graph or other derived data. This feature is planned for a future release.


# Delete documents by filter
Source: https://io.net/docs/reference/rag/documents/delete-documents-by-filter

openapi/rag-documents/delete-documents-by-filter.json delete /api/r2r/v3/documents/by-filter
Delete documents based on provided filters.

Allowed operators include: `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`, `ilike`, `in`, and `nin`. Deletion requests are limited to a user’s own documents.


# Export multiple documents as zip
Source: https://io.net/docs/reference/rag/documents/download-documents-as-zip

openapi/rag-documents/download-documents-as-zip.json get /api/r2r/v3/documents/download_zip
Export multiple documents as a zip file. Documents can be filtered by IDs and/or date range.

The endpoint allows downloading:

* Specific documents by providing their IDs
* Documents within a date range
* All accessible documents if no filters are provided

Files are streamed as a zip archive to handle potentially large downloads efficiently.


# Download document content
Source: https://io.net/docs/reference/rag/documents/download-original-file

openapi/rag-documents/download-original-file.json get /api/r2r/v3/documents/{id}/download
Downloads the original file content of a document.

For uploaded files, returns the original file with its proper MIME type. For text-only documents, returns the content as plain text.

Users can only download documents they own or have access to through collections.


# Extract entities and relationships
Source: https://io.net/docs/reference/rag/documents/extract-entities

openapi/rag-documents/extract-entities.json post /api/r2r/v3/documents/{id}/extract
Extracts entities and relationships from a document.

The entities and relationships extraction process involves:

1. Parsing documents into semantic chunks
2. Extracting entities and relationships using LLMs
3. Storing the created entities and relationships in the knowledge graph
4. Preserving the document’s metadata and content, and associating the elements with collections the document belongs to


# Retrieve a document
Source: https://io.net/docs/reference/rag/documents/get-document-by-id

openapi/rag-documents/get-document-by-id.json get /api/r2r/v3/documents/{id}
Retrieves detailed information about a specific document by its ID.

This endpoint returns the document’s metadata, status, and system information. It does not return the document’s content - use the `/documents/{id}/download` endpoint for that.

Users can only retrieve documents they own or have access to through collections. Superusers can retrieve any document.


# List document chunks
Source: https://io.net/docs/reference/rag/documents/get-document-chunks

openapi/rag-documents/get-document-chunks.json get /api/r2r/v3/documents/{id}/chunks
Retrieves the text chunks that were generated from a document during ingestion.

Chunks represent semantic sections of the document and are used for retrieval and analysis. Users can only access chunks from documents they own or have access to through collections. Vector embeddings are only included if specifically requested. Results are returned in chunk sequence order, representing their position in the original document.


# Get Extracted Entities
Source: https://io.net/docs/reference/rag/documents/get-extracted-entities

openapi/rag-documents/get-extracted-entities.json get /api/r2r/v3/documents/{id}/entities
Fetch list of named entities extracted from the document.



# Get Relationships
Source: https://io.net/docs/reference/rag/documents/get-relationships

openapi/rag-documents/get-relationships.json get /api/r2r/v3/documents/{id}/relationships
View semantic or knowledge graph relationships from extracted content.



# List documents
Source: https://io.net/docs/reference/rag/documents/list-all-documents

openapi/rag-documents/list-all-documents.json get /api/r2r/v3/documents
Returns a paginated list of documents the authenticated user has access to.

Results can be filtered by providing specific document IDs. Regular users will only see documents they own or have access to through collections. Superusers can see all documents. The documents are returned in order of last modification, with most recent first.


# Replace document metadata
Source: https://io.net/docs/reference/rag/documents/replace-document-metadata

openapi/rag-documents/replace-document-metadata.json put /api/r2r/v3/documents/{id}/metadata
Modify document metadata, given the document ID

<RequestExample>
  ```python Request Example theme={null}
  from r2r import R2RClient

  client = R2RClient('https://api.intelligence.io.solutions/api/r2r')
  client.set_api_key('<your-io-API-key>')

  response = client.retrieval.completion(
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "What is the capital of France?"},
          {"role": "assistant", "content": "The capital of France is Paris."},
          {"role": "user", "content": "What about Italy?"}
      ],
      generation_config={
          "model": "hosted_vllm/openai/gpt-oss-120b",
          "temperature": 0.7,
          "max_tokens": 150,
          "stream": False
      }
  )

  print(response)
  ```
</RequestExample>


# Search document summaries
Source: https://io.net/docs/reference/rag/documents/search-documents

openapi/rag-documents/search-documents.json post /api/r2r/v3/documents/search
Perform a search query on the automatically generated document summaries in the system.

This endpoint allows for complex filtering of search results using PostgreSQL-based queries. Filters can be applied to various fields such as document\_id, and internal metadata values.

Allowed operators include `eq`, `neq`, `gt`, `gte`, `lt`, `lte`, `like`, `ilike`, `in`, and `nin`.


# Append metadata to a document
Source: https://io.net/docs/reference/rag/documents/update-document-metadata-partial

openapi/rag-documents/update-document-metadata-partial.json patch /api/r2r/v3/documents/{id}/metadata
Appends metadata to a document. This endpoint allows adding new metadata fields or updating existing ones.



# Create a new document
Source: https://io.net/docs/reference/rag/documents/upload-and-ingest-a-document

openapi/rag-documents/upload-and-ingest-a-document.json post /api/r2r/v3/documents
Creates a new Document object from an input file, text content, or chunks.

The chosen `ingestion_mode` determines how the ingestion process is configured:

**Ingestion Modes:**

* `hi-res`: Comprehensive parsing and enrichment, including summaries and possibly more thorough parsing.
* `fast`: Speed-focused ingestion that skips certain enrichment steps like summaries.
* `custom`: Provide a full `ingestion_config` to customize the entire ingestion process.

Either a file or text content must be provided, but not both. Documents are shared through `Collections` which allow for tightly specified cross-user interactions.

The ingestion process runs asynchronously and its progress can be tracked using the returned task\_id.


# Overview
Source: https://io.net/docs/reference/rag/getting-started-with-the-rag-api

The R2R APIs enables developers to build powerful AI systems that integrates the strengths of semantic search, knowledge graphs, and prompt-based generation for advanced question answering and intelligent assistants.

## What Is RAG on R2R?

### **Retrieval and Generation Workflow:**

RAG operates in two phases:

1. **Retrieve** relevant document chunks via semantic search or knowledge graph lookup.
2. **Generate** coherent and contextually accurate responses using the retrieved chunks and your customized prompts.

* **Why It Matters:** By tapping into real, structured, or unstructured content, RAG systems produce answers grounded in facts, avoiding hallucinations and improving trustworthiness.

## Core Components

| Component              | Description                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| **Documents & Chunks** | Ingested files or text are segmented into **Chunks**, the basis for retrieval.                    |
| **Indices**            | Vector indices enable fast similarity search over chunk embeddings.                               |
| **Graphs**             | Knowledge graph extracts relationships and entities, enabling intelligent navigation of concepts. |
| **Prompts**            | Prompt templates shape the generation step, with type-safe inputs and version control.            |
| **System Endpoints**   | Provide health checks, diagnostics, and monitoring for your RAG pipeline.                         |

## Getting Started

To get started with the R2R APIs, you will need to:

* [Install R2R](https://github.com/SciPhi-AI/R2R) in your environment.
* Run the server with `python -m r2r.serve`, or configure FastAPI settings for production use.

For detailed installation and setup instructions, refer to the R2R [Installation Guide](https://r2r-docs.sciphi.ai/self-hosting/installation/overview).

## Authentication

### API keys

IO Intelligence APIs authenticate requests using API keys. You can [generate API keys from your account](https://ai.io.net/ai/api-keys):

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service on your backend server.
</Warning>

Include the API key in an `Authorization` HTTP header for all API requests:

```
Authorization: Bearer \$IOINTELLIGENCE_API_KEY
```

## Example of a RAG Workflow

### Step 1: Retreive relevant chunks

<CodeGroup>
  ```curl curl theme={null}
  curl -X POST https://api.intelligence.io.solutions/api/r2r/v3/retrieval/search /
    -H "Authorization: Bearer \$IOINTELLIGENCE_API_KEY" /
    -H "Content-Type: application/json" /
    -d '{
      "query": "What is Retrieval-Augmented Generation?",
      "top_k": 5
  }'
  ```
</CodeGroup>

### Step 2: Generate a response

Assuming you have retrieved relevant chunks and want to pass them as context:

<CodeGroup>
  ```curl curl theme={null}
  curl -X POST https://api.intelligence.io.solutions/api/r2r/v3/rag/generate /
    -H "Authorization: Bearer \$IOINTELLIGENCE_API_KEY" /
    -H "Content-Type: application/json" /
    -d '{
      "prompt_name": "default_rag",
      "inputs": {
        "query": "What is Retrieval-Augmented Generation?",
        "context": "Chunk 1 text/nChunk 2 text/nChunk 3 text" //it's just example chunk text
      }
  }'
  ```
</CodeGroup>

## Token Quotas & Usage

Each account has daily usage limits based on model and request volume. Refer to the [IO Intelligence Payments ](/guides/payment/io-intelligence-payments) for further information.

## Next Steps

Explore the following API references for more detailed guides:

* [**Retrieval**](/reference/rag/retrieval) – Perform semantic and hybrid search across ingested data
* [**Documents**](/reference/rag/documents) – Management and metadata of documents.
* [**Graphs**](/reference/rag/graphs) – Entity extraction and knowledge graphs.
* [**Indices**](/reference/rag/indices) – Create and configure embeddings.
* [**Chunks**](/reference/rag/chunks) – Ingest, list and search documents.
* [**Users**](/reference/rag/users) – Manage API users, authentication, and access control.
* [**Collections**](/reference/rag/collections) – Group related documents and control indexing scope.
* [**Conversations**](/reference/rag/conversations) – Manage chat sessions, history, and context retention.
* [**Prompts**](/reference/rag/prompts) – Template definition and versioning.
* [**System**](/reference/rag/system) – Health and diagnostics.


# Overview
Source: https://io.net/docs/reference/rag/graphs

The R2R Graphs API manages knowledge graphs tied to specific collections. It supports entity and relationship extraction, community detection, and synchronization with document data—enabling structured, queryable knowledge organization for advanced AI reasoning.

A **Graph** in R2R is a **knowledge graph** associated with a specific **Collection**. Each Graph organizes and connects extracted knowledge—such as entities, relationships, and communities—into a structured, queryable network. It serves as the **semantic backbone** of R2R, enabling advanced reasoning, knowledge discovery, and relational search.

Each Graph contains:

* **Entities** — extracted information nodes from documents (e.g., people, organizations, concepts).
* **Relationships** — links between entities that define how they relate.
* **Communities** — LLM-generated clusters of related entities identified through **Leiden clustering**.
* **Document Mappings** — records of which documents contributed to the graph’s knowledge base.

### Key Features

#### Git-like Model

* Each **Collection** has an independent, associated **Graph**.
* Graphs can **diverge and evolve** separately from their parent collection.
* The **pull operation** syncs knowledge from documents into the graph.
* Supports **experimental changes** without impacting the base Collection or source data.

#### Knowledge Organization

* Automatic **entity and relationship extraction** from documents.
* **Community detection** enables hierarchical knowledge structures.
* Support for **manual creation and editing** of entities, relationships, and communities.
* Rich **metadata and property management** for nodes and edges.

#### Access Control

* Graph operations inherit **Collection-level permissions**.
* Certain operations (e.g., community generation) require **superuser privileges**.
* **Document-level access checks** are enforced when pulling or synchronizing data.

## Core Graph Operations

| Method | Endpoint                                                           | Description                                                       |
| ------ | ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| GET    | [/graphs/](/reference/rag/graphs/get-graph-overview)               | Retrieve an overview of available graphs.                         |
| POST   | [/graphs//pull](/reference/rag/graphs/pull-and-rebuild-graph)      | Synchronize documents and extract their knowledge into the graph. |
| POST   | [/graphs//](/reference/rag/graphs/get-graph-data-for-a-collection) | Retrieve details of a specific collection’s graph.                |

## Entity Management

| Method | Endpoint                                                              | Description                                |
| ------ | --------------------------------------------------------------------- | ------------------------------------------ |
| GET    | [/graphs//entities](/reference/rag/graphs/list-graph-entities)        | List entities within a collection’s graph. |
| POST   | [/graphs//entities](/reference/rag/graphs/add-new-entities)           | Create a new entity.                       |
| GET    | [/graphs//entities/](/reference/rag/graphs/get-single-entity-details) | Retrieve details for a specific entity.    |

Similar **CRUD** endpoints exist for managing **relationships** (`/relationships`) and **communities** (`/communities`).


# Overview
Source: https://io.net/docs/reference/rag/graphs/communities



## Community management endpoints

Communities are groups of entities that are connected to each other. They can be generated using a clustering and summarization algorithm implemented by R2R.

To automatically generate communities from entities and relationships present in the graph, you can use the following endpoint:

| Method | Endpoint                                                                                                 | Description            |
| ------ | -------------------------------------------------------------------------------------------------------- | ---------------------- |
| GET    | [/graphs/\{collection\_id}/communities/build](/reference/rag/graphs/communities/build-graph-communities) | Create a new community |

Once communities are generated, you can manage them using the following endpoints. You can also add your own communities to the graph.

| Method | Endpoint                                                                                                       | Description                   |
| ------ | -------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| GET    | [graphs/\{collection\_id}/communities](/reference/rag/graphs/communities/list-communities)                     | Get relationships for a graph |
| POST   | [/graphs/\{collection\_id}/communities/\{community\_id}](/reference/rag/graphs/communities/)                   | Retrieve a community          |
| POST   | [/graphs/\{collection\_id}/communities/\{community\_id}](/reference/rag/graphs/communities/update-a-community) | Update community              |
| DELETE | [graphs/\{collection\_id}/communities/\{community\_id}](/reference/rag/graphs/communities/delete-a-community)  | Delete community              |


# Create a new community
Source: https://io.net/docs/reference/rag/graphs/communities/build-graph-communities

openapi/rag-graphs-communities/build-graph-communities.json post /api/r2r/v3/graphs/{collection_id}/communities/build
Creates communities in the graph by analyzing entity relationships and similarities.

Creates communities in the graph by analyzing entity relationships and similarities.

Communities are created through the following process:

1. Analyzes entity relationships and metadata to build a similarity graph
2. Applies advanced community detection algorithms (e.g. Leiden) to identify densely connected groups
3. Creates hierarchical community structure with multiple granularity levels
4. Generates natural language summaries and statistical insights for each community

The resulting communities can be used to:

* Understand high-level graph structure and organization
* Identify key entity groupings and their relationships
* Navigate and explore the graph at different levels of detail
* Generate insights about entity clusters and their characteristics

The community detection process is configurable through settings like:

* Community detection algorithm parameters
* Summary generation prompt


# Community: Delete
Source: https://io.net/docs/reference/rag/graphs/communities/delete-a-community

openapi/rag-graphs-communities/delete-a-community.json delete /api/r2r/v3/graphs/{collection_id}/communities/{community_id}
Permanently removes a specific community (cluster) from the graph.



# Retrieve a community
Source: https://io.net/docs/reference/rag/graphs/communities/get-community-details

openapi/rag-graphs-communities/get-community-details.json get /api/r2r/v3/graphs/{collection_id}/communities/{community_id}
Retrieves a specific community by its ID.



# List communities
Source: https://io.net/docs/reference/rag/graphs/communities/list-communities

openapi/rag-graphs-communities/list-communities.json get /api/r2r/v3/graphs/{collection_id}/communities
Lists all communities in the graph with pagination support.



# Update community
Source: https://io.net/docs/reference/rag/graphs/communities/update-a-community

openapi/rag-graphs-communities/update-a-community.json post /api/r2r/v3/graphs/{collection_id}/communities/{community_id}
Updates an existing community in the graph.



# Entities
Source: https://io.net/docs/reference/rag/graphs/entities



### Entity management endpoints

Entities are basic building blocks of a graph. They can be automatically extracted from a document and then added to a graph.

To manage entities extracted from a document, you can use the following endpoints:

| Method | Endpoint                                                                           | Description                                   |
| ------ | ---------------------------------------------------------------------------------- | --------------------------------------------- |
| GET    | [/documents/\{id}/entities](/reference/rag/graphs/entities/get-extracted-entities) | List *Entities* identified within a document. |

Once entities are added to a graph by a POST to “/graphs/\{id}/\{object\_type}” endpoint, you can manage them using the following endpoints:

| Method | Endpoint                                                                                                     | Description                                 |
| ------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| GET    | [/graphs/\{collection\_id}/entities](/reference/rag/graphs/entities/list-graph-entities)                     | List entities (/\[r2r-docs.sciphi.ai]/\[1]) |
| POST   | [/graphs/\{collection\_id}/entities](/reference/rag/graphs/entities/add-new-entities)                        | Create entity                               |
| GET    | [/graphs/\{collection\_id}/entities/\{entity\_id}](/reference/rag/graphs/entities/get-single-entity-details) | Get entity details                          |


# Create Entity
Source: https://io.net/docs/reference/rag/graphs/entities/add-new-entities

openapi/rag-graphs-entities/add-new-entities.json post /api/r2r/v3/graphs/{collection_id}/entities
Creates a new entity in the graph.



# Get Entity
Source: https://io.net/docs/reference/rag/graphs/entities/get-single-entity-details

openapi/rag-graphs-entities/get-single-entity-details.json get /api/r2r/v3/graphs/{collection_id}/entities/{entity_id}
Retrieves a specific entity by its ID.



# Get Entities
Source: https://io.net/docs/reference/rag/graphs/entities/list-graph-entities

openapi/rag-graphs-entities/list-graph-entities.json get /api/r2r/v3/graphs/{collection_id}/entities
Lists all entities in the graph with pagination support.



# Retrieve graph details
Source: https://io.net/docs/reference/rag/graphs/get-graph-data-for-a-collection

openapi/rag-graphs/get-graph-data-for-a-collection.json get /api/r2r/v3/graphs/{collection_id}
Retrieves detailed information about a specific graph by ID.



# Get graph overview
Source: https://io.net/docs/reference/rag/graphs/get-graph-overview

openapi/rag-graphs/get-graph-overview.json get /api/r2r/v3/graphs
Returns a paginated list of graphs the authenticated user has access to.

Results can be filtered by providing specific graph IDs. Regular users will only see graphs they own or have access to. Superusers can see all graphs. The graphs are returned in order of last modification, with most recent first.


# Pull latest entities to the graph
Source: https://io.net/docs/reference/rag/graphs/pull-and-rebuild-graph

openapi/rag-graphs/pull-and-rebuild-graph.json post /api/r2r/v3/graphs/{collection_id}/pull
Adds documents to a graph by copying their entities and relationships.

This endpoint:

1. Copies document entities to the graphs\_entities table
2. Copies document relationships to the graphs\_relationships table
3. Associates the documents with the graph

When a document is added:

* Its entities and relationships are copied to graph-specific tables
* Existing entities/relationships are updated by merging their properties
* The document ID is recorded in the graph’s document\_ids array

Documents added to a graph will contribute their knowledge to:

* Graph analysis and querying
* Community detection
* Knowledge graph enrichment

The user must have access to both the graph and the documents being added.


# Overview
Source: https://io.net/docs/reference/rag/graphs/relationships



## Relationship management endpoints

Relationships are basic building blocks of a graph. They can be automatically extracted from a document and then added to a graph.

To manage relationships extracted from a document, you can use the following endpoints:

| Method | Endpoint                                                                               | Description                                        |
| ------ | -------------------------------------------------------------------------------------- | -------------------------------------------------- |
| `GET`  | [/documents/\{id}/relationship](/reference/rag/graphs/relationships/get-relationships) | List *Relationships* identified within a document. |

Once entities are added to a graph using the “/graphs/\{id}/\{object\_type}/add” endpoint, you can manage them using the following endpoints:

| Method | Endpoint                                                                                          | Description                    |
| ------ | ------------------------------------------------------------------------------------------------- | ------------------------------ |
| GET    | [/graphs/\{id}/relationships](/reference/rag/graphs/relationships/get-graph-relationships)        | Get relationships for a graph  |
| GET    | [/graphs/\{id}/relationships/\{id}](/reference/rag/graphs/relationships/get-relationship-details) | Get a relationship for a graph |


# Get Relationships
Source: https://io.net/docs/reference/rag/graphs/relationships/get-graph-relationships

openapi/rag-graphs-relationships/get-graph-relationships.json get /api/r2r/v3/graphs/{collection_id}/relationships
Lists all relationships in the graph with pagination support.



# Get Relationship
Source: https://io.net/docs/reference/rag/graphs/relationships/get-relationship-details

openapi/rag-graphs-relationships/get-relationship-details.json get /api/r2r/v3/graphs/{collection_id}/relationships/{relationship_id}
Retrieves a specific relationship by its ID.



# Overview
Source: https://io.net/docs/reference/rag/indices

The R2R Indices API manages vector index structures that enable high-speed similarity search across chunks. It supports multiple index methods, configurable similarity measures, and concurrent building for optimized RAG retrieval performance.

An **Index** in R2R represents a **vector index structure** designed to optimize **similarity search** operations across document chunks. Indices are a core component of R2R’s **Retrieval-Augmented Generation (RAG)** architecture, enabling fast and scalable semantic retrieval.

By organizing vector embeddings efficiently, indices make it possible to perform **high-performance vector searches** across large datasets using different similarity metrics and indexing strategies.

### Key Capabilities

Indices in R2R provide:

* **Fast similarity search** for vector-based retrieval.
* **Multiple index methods**, including **HNSW** (Hierarchical Navigable Small World) and **IVF-Flat**.
* **Configurable similarity measures** such as cosine similarity or inner product.
* **Concurrent index building** to improve throughput and scalability.
* **Performance optimization** for large-scale vector operations.

## API Endpoints

| Method | Endpoint                                                        | Description                                              |
| ------ | --------------------------------------------------------------- | -------------------------------------------------------- |
| GET    | [/indices](/reference/rag/indices/list-all-indices)             | List available indices with pagination.                  |
| GET    | [/indices//](/reference/rag/indices/get-specific-index-details) | Retrieve details and configuration for a specific index. |
| DELETE | [/indices//](/reference/rag/indices/delete-an-index)            | Delete an existing index.                                |


# Delete Vector Index
Source: https://io.net/docs/reference/rag/indices/delete-an-index

openapi/rag-indices/delete-an-index.json delete /api/r2r/v3/indices/{table_name}/{index_name}
Delete an existing vector similarity search index.

This endpoint removes the specified index from the database. Important considerations:

* Deletion is permanent and cannot be undone
* Underlying vector data remains intact
* Queries will fall back to sequential scan
* Running queries during deletion may be slower
* Use run\_with\_orchestration=True for large indices to prevent timeouts
* Consider index dependencies before deletion

The operation returns immediately but cleanup may continue in background.


# Get Vector Index Details
Source: https://io.net/docs/reference/rag/indices/get-specific-index-details

openapi/rag-indices/get-specific-index-details.json get /api/r2r/v3/indices/{table_name}/{index_name}
Get detailed information about a specific vector index.

Returns comprehensive information about the index including:

* Configuration details (method, measure, parameters)
* Current size and row count
* Build progress (if still under construction)
* Performance statistics:
  * Average query time
  * Memory usage
  * Cache hit rates
  * Recent query patterns
* Maintenance information:
  * Last vacuum
  * Fragmentation level
  * Recommended optimizations


# List Vector Indices
Source: https://io.net/docs/reference/rag/indices/list-all-indices

openapi/rag-indices/list-all-indices.json get /api/r2r/v3/indices
List existing vector similarity search indices with pagination support.

Returns details about each index including:

* Name and table name
* Indexing method and parameters
* Size and row count
* Creation timestamp and last updated
* Performance statistics (if available)

The response can be filtered using the filter\_by parameter to narrow down results based on table name, index method, or other attributes.


# Overview
Source: https://io.net/docs/reference/rag/prompts

The R2R Prompts API manages reusable, type-safe prompt templates that structure interactions with language models. It supports dynamic generation, version control, and centralized governance to ensure consistent, high-quality AI behavior.

A **Prompt** in R2R represents a **templated instruction or query pattern** that standardizes how the system interacts with language models and other AI components. Prompts serve as reusable blueprints for generating consistent and context-aware outputs across workflows.

Managed by **superusers**, prompts ensure governance, maintain version control, and support type-safe customization for different application contexts.

### Key Capabilities

Prompts in R2R provide:

* **Templated instruction management** for reusable prompt definitions.
* **Type-safe input handling** to ensure structured and validated parameter substitution.
* **Centralized prompt governance** for system-wide consistency and quality control.
* **Dynamic prompt generation** to adapt templates based on context or input data.
* **Version control** for tracking updates and maintaining reproducibility.

## Available Endpoints

| Method | Endpoint                                            | Description                   |
| ------ | --------------------------------------------------- | ----------------------------- |
| POST   | [/prompts](/reference/rag/prompts/list-all-prompts) | Create a new prompt template. |


# List all prompts
Source: https://io.net/docs/reference/rag/prompts/list-all-prompts

openapi/rag-prompts/list-all-prompts.json post /api/r2r/v3/prompts
List all available prompts. This endpoint retrieves a list of all prompts in the system. Only superusers can access this endpoint.



# Overview
Source: https://io.net/docs/reference/rag/retrieval

The R2R Retrieval API provides vector search, knowledge graph retrieval, and RAG-based generation capabilities. It powers semantic search, conversational agents, and flexible AI generation across documents, enabling intelligent data interaction and discovery.

R2R’s **Retrieval** system provides advanced search and generation capabilities powered by **vector search**, **knowledge graphs**, and **large language models (LLMs)**.\
It offers multiple ways to interact with your data, enabling both direct retrieval and AI-augmented reasoning.

* Direct semantic search across documents and chunks
* Retrieval-Augmented Generation (RAG) for AI-powered answers
* Conversational RAG agents for complex queries
* Raw LLM completions for flexible text generation

## Core Features

### Vector Search

* Semantic similarity matching using document and chunk embeddings
* Hybrid retrieval combining vector and keyword search
* Complex filtering with Postgres-style operators
* Configurable search limits and similarity thresholds

### Knowledge Graph Search

* Retrieval based on entities and relationships
* Multi-hop traversal for connected information discovery
* Local and global search strategies for context depth
* Community-aware graph navigation and clustering

### RAG Generation

* Contextual responses grounded in retrieved content
* Customizable generation parameters (temperature, token limits, etc.)
* Source attribution and citation support
* Streaming responses for real-time output
* Optional web search integration for current information

### Deep Research Agent

* Multi-turn conversational capabilities
* Complex query decomposition and reasoning
* Context retention across multiple interactions
* Branch management for conversation trees
* Integration with web search for external knowledge

## API Endpoints

| **Method** | **Endpoint**                                                              | **Description**                                                                                 |
| ---------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `POST`     | [/retrieval/search](/reference/rag/retrieval/semantic-search)             | Perform semantic search with hybrid vector and knowledge graph capabilities.                    |
| `POST`     | [/retrieval/rag](/reference/rag/retrieval/retrieve-and-generate-rag)      | Generate contextual responses using retrieved information with optional web search integration. |
| `POST`     | [/retrieval/agent](/reference/rag/retrieval/agent-based-query-resolution) | Engage with a conversational RAG agent capable of web-enhanced query resolution.                |
| `POST`     | [/retrieval/completion](/reference/rag/retrieval/prompt-based-completion) | Generate free-form text completions using language models.                                      |
| `POST`     | [/retrieval/embedding](/reference/rag/retrieval/generate-embedding)       | Generate embeddings for documents or raw text for similarity search.                            |

## Search Settings

### Vector Search Example

<CodeGroup>
  ```json json theme={null}
  {
    "use_semantic_search": true,
    "filters": {"document_id": {"$eq": "3e157b3a-8469-51db-90d9-52e7d896b49b"}},
    "limit": 20,
    "use_hybrid_search": true
  }
  ```
</CodeGroup>

### Generation Configuration Example

<CodeGroup>
  ```json json theme={null}
  {
    "stream": false,
    "temperature": 0.7,
    "max_tokens": 150,
    "model": "gpt-4o-mini"
  }
  ```
</CodeGroup>

## Key Concepts

### Search

The `/retrieval/search` endpoint provides direct access to R2R’s retrieval capabilities, enabling semantic and graph-based search across your content. It supports advanced filtering, sorting by relevance, and hybrid retrieval using both embeddings and keywords.

### RAG

Retrieval-Augmented Generation (RAG) combines content retrieval with language model generation. It retrieves relevant context from your documents and optionally integrates live web search results to produce accurate, source-grounded responses.

### Agent

The `/retrieval/agent` endpoint provides a conversational interface for advanced retrieval. It maintains context, decomposes complex queries, and delivers responses with citations. The agent can also use web search to enhance context beyond internal data.

### Completion

The `/retrieval/completion` endpoint gives direct access to language model generation without retrieval. It supports both single-turn and multi-turn interactions, making it ideal for creative generation, summarization, and reasoning tasks.

## Filter Operations

Supported operators for content filtering include:

* `eq`: Equals
* `neq`: Not equals
* `gt`: Greater than
* `gte`: Greater than or equal
* `lt`: Less than
* `lte`: Less than or equal
* `like`: Pattern matching
* `ilike`: Case-insensitive pattern matching
* `in`: In list
* `nin`: Not in list

**Example:**

<CodeGroup>
  ```json json theme={null}
  {
    "filters": {
      "metadata.category": {"$eq": "research"},
      "created_at": {"$gte": "2024-01-01"},
      "collection_ids": {"$in": ["uuid1", "uuid2"]}
    }
  }
  ```
</CodeGroup>


# RAG-Powered Conversational Agent
Source: https://io.net/docs/reference/rag/retrieval/agent-based-query-resolution

openapi/rag-retrieval/agent-based-query-resolution.json post /api/r2r/v3/retrieval/agent
The R2R Agent endpoint provides a conversational RAG interface for retrieval, reasoning, and research. It supports multi-turn context, tool integration, streaming output, and both RAG and Research modes for dynamic AI-driven analysis.

The **RAG-powered Conversational Agent** enables interactive, multi-turn communication with an intelligent agent built on R2R’s Retrieval-Augmented Generation (RAG) system.

This endpoint allows users to engage in real-time dialogue with an AI capable of retrieving information from internal and external sources, reasoning through complex problems, executing computations, and maintaining context across multiple conversation turns.

It operates in two distinct modes: **RAG Mode** for knowledge-based responses and **Research Mode** for deep analytical reasoning.

## Operating Modes

### **RAG Mode (Default)**

Provides fast, grounded answers by combining retrieval and generation.

Features include:

* Semantic and hybrid search across documents and chunks
* Optional web search integration for live context
* Document-level and chunk-level content retrieval
* Source citation and evidence-based responses

## **Research Mode**

Extends RAG functionality with advanced reasoning and computational abilities.

Features include:

* Dedicated reasoning system for multi-step problem-solving
* Automated critique generation to identify biases or logical fallacies
* Python execution for quantitative analysis and code-based reasoning
* Deep exploration capabilities across multiple sources

## **Available Tools**

### **RAG Tools:**

* `search_file_knowledge` — Perform semantic or hybrid search across ingested documents.
* `search_file_descriptions` — Search file-level metadata and descriptions.
* `content` — Retrieve full documents or chunk structures.
* `web_search` — Query external search engines for up-to-date information.
* `web_scrape` — Extract content directly from specified web pages.

**Research Tools:**

* `rag` — Invoke the underlying RAG agent for information retrieval.
* `reasoning` — Use a dedicated reasoning model for deep analysis and logical inference.
* `critique` — Analyze the conversation for potential biases or reasoning flaws.
* `python_executor` — Execute Python code for computation, simulation, or data processing.

## **Streaming Output**

When streaming is enabled (`"stream": true`), the API emits **Server-Sent Events (SSE)** to deliver updates in real time.

Each event corresponds to a stage in the agent’s reasoning and response generation process.

| **Event Type** | **Description**                                                                          |
| :------------- | :--------------------------------------------------------------------------------------- |
| `thinking`     | Displays the model’s intermediate reasoning steps (enabled by `extended_thinking=true`). |
| `tool_call`    | Indicates when the agent invokes a tool.                                                 |
| `tool_result`  | Contains the output from an executed tool.                                               |
| `citation`     | Signals that a citation has been added to the response.                                  |
| `message`      | Streams partial tokens of the generated message.                                         |
| `final_answer` | Provides the complete generated response with structured citations.                      |

## **Conversations**

The agent maintains persistent conversational context using the `conversation_id` field.

**How it works:**

1. On the initial request, the system creates a new conversation and returns a `conversation_id`.
2. Include this ID in subsequent requests to continue the same thread.
3. If no conversation name exists, R2R automatically assigns one.

This design allows for **multi-turn, context-aware discussions**, where the agent can recall prior messages, reasoning, and results.


# Embeddings
Source: https://io.net/docs/reference/rag/retrieval/generate-embedding

openapi/rag-retrieval/generate-embedding.json post /api/r2r/v3/retrieval/embedding
The R2R Embedding endpoint generates vector embeddings from text using a specified model. It supports single or batch input, returning semantic vectors for use in search, clustering, and RAG applications.

The **Embedding** endpoint generates **vector embeddings** for the provided text using a specified model.

Embeddings are dense numerical representations of text that capture semantic meaning, enabling downstream applications such as **semantic search**, **clustering**, **classification**, and **RAG (Retrieval-Augmented Generation)** operations.

This endpoint provides a simple and efficient way to convert text into machine-readable vector form for use within R2R’s retrieval and analysis systems.

### Use Cases

Embeddings generated via this endpoint can be used for:

* **Semantic search** — Compare embedding vectors to find related content.
* **Clustering and classification** — Group similar documents or classify them by meaning.
* **Knowledge graph enhancement** — Connect semantically related entities.
* **RAG workflows** — Retrieve relevant content before passing context to language models.


# Prompt-Based Completion
Source: https://io.net/docs/reference/rag/retrieval/prompt-based-completion

openapi/rag-retrieval/prompt-based-completion.json post /api/r2r/v3/retrieval/completion
The R2R Completion endpoint generates text completions directly from a language model. It accepts structured messages, supports configurable generation parameters, and enables both streaming and non-streaming responses for flexible AI interaction.

The **Prompt-Based Completion** endpoint allows direct interaction with a language model by sending raw prompts or structured message sequences.

It provides a simple interface for generating completions, summaries, or other free-form outputs without performing any retrieval or grounding from the document corpus.

This endpoint is ideal for open-ended generation tasks such as text drafting, classification, rewriting, summarization, and chat-like conversations that do not require knowledge integration from R2R’s retrieval pipeline.

### Request Body

The request must include a `messages` list representing the conversational context and an optional `generation_config` object to control model behavior.


# RAG Query
Source: https://io.net/docs/reference/rag/retrieval/retrieve-and-generate-rag

openapi/rag-retrieval/retrieve-and-generate-rag.json post /api/r2r/v3/retrieval/rag
The R2R RAG Query endpoint performs Retrieval-Augmented Generation by combining semantic search, graph-enhanced context, and LLM generation. It supports streaming, source citation, and multiple model providers for contextually accurate AI responses.

The **RAG Query endpoint** executes a **Retrieval-Augmented Generation (RAG)** workflow by combining semantic search, optional knowledge graph integration, and large language model (LLM) generation.

It returns **contextually grounded, source-cited responses** derived from your document corpus and external web content (if enabled).

This endpoint is ideal for applications that require **explainable AI answers**, **document-grounded responses**, and **real-time contextual reasoning**.

### Key Features

* **Combined retrieval and generation**: Merges vector search, optional graph traversal, and LLM output generation in one request.
* **Automatic source citation**: Each referenced document includes a unique citation identifier.
* **Streaming and non-streaming modes**: Supports token-level updates or full-response delivery.
* **Provider flexibility**: Compatible with OpenAI, Anthropic, Ollama, and other LiteLLM-supported models.
* **Web search integration**: Optionally augments internal context with real-time external data.

### Model Support

| **Provider**  | **Description**                                                               |
| :------------ | :---------------------------------------------------------------------------- |
| **OpenAI**    | Default provider supporting GPT-based models (`gpt-4o`, `gpt-4o-mini`, etc.). |
| **Anthropic** | Supports Claude models (requires `ANTHROPIC_API_KEY`).                        |
| **Ollama**    | Enables local model execution via Ollama runtime.                             |
| **LiteLLM**   | Provides access to additional supported model providers.                      |

### Request Body

The request body combines **search configuration** (for retrieval) and **generation configuration** (for LLM behavior).\
All search parameters available in the `/search` endpoint can be reused here, including **filters**, **hybrid search**, and **graph-enhanced retrieval**.

### **Generation Configuration**

Control model behavior using the `rag_generation_config` object.

**Example:**

```json theme={null}
{
    "model": "openai/gpt-4o-mini",
    "temperature": 0.7,
    "max_tokens": 1500,
    "stream": true
}
```

**Parameters:**

* `model`: Specifies the model used for generation.
* `temperature`: Controls output randomness (0 for deterministic, 1 for creative).
* `max_tokens`: Sets maximum output length.
* `stream`: Enables or disables token streaming for real-time responses.

### Streaming Responses

When `stream: true` is enabled, the API emits **Server-Sent Events (SSE)** during processing.\
Each event type corresponds to a distinct phase of the retrieval and generation workflow.

| **Event Type**   | **Description**                                                      |
| :--------------- | :------------------------------------------------------------------- |
| `search_results` | Contains the initial search results from your documents.             |
| `message`        | Streams partial tokens as the model generates them.                  |
| `citation`       | Emits citation metadata when a source is referenced.                 |
| `final_answer`   | Contains the complete, generated response with structured citations. |

**Example Response:**

```json theme={null}
{
	"generated_answer": "DeepSeek-R1 is a model that demonstrates impressive performance...[1]",
	"search_results": { ... },
	"citations": [
    	{
        	"id": "cit.123456",
        	"object": "citation",
        	"payload": { ... }
    }
]
}
```


# Search R2R
Source: https://io.net/docs/reference/rag/retrieval/semantic-search

openapi/rag-retrieval/semantic-search.json post /api/r2r/v3/retrieval/search
The R2R Search Endpoint provides semantic, hybrid, and graph-enhanced retrieval across documents and chunks. It supports advanced filters, hybrid ranking, and knowledge graph traversal to deliver contextually relevant and explainable results.

The **Search** endpoint provides advanced retrieval capabilities across documents, chunks, and knowledge graphs within R2R.

It supports multiple **search modes**, **hybrid vector and keyword retrieval**, **graph-enhanced search**, and **metadata-based filtering**, enabling powerful and flexible information discovery for semantic, contextual, and RAG-driven applications.

This endpoint is designed for both simple semantic lookups and complex, structured search workflows that combine multiple retrieval strategies.

### **Search Modes**

The `search_mode` field determines the level of control and type of retrieval performed.

| **Mode**   | **Description**                                                                                                     |
| :--------- | :------------------------------------------------------------------------------------------------------------------ |
| `basic`    | Performs a standard **semantic search** using vector embeddings. Ideal for quick and simple retrievals.             |
| `advanced` | Combines **semantic search** with **full-text search** for broader and more comprehensive results.                  |
| `custom`   | Grants full control via a `SearchSettings` object, allowing fine-tuned configurations for specialized applications. |

### **Filters**

Filters can be used to restrict search results by document attributes or metadata. Apply filters directly inside `search_settings.filters.`

**Supported operators:**

`$eq`, `$neq`, `$gt`, `$gte`, `$lt`, `$lte`, `$like`, `$ilike`, `$in`, `$nin`.

**Example:**

```json theme={null}
{
	"filters": {
		"document_id": {"$eq": "e43864f5-a36f-548e-aacd-6f8d48b30c7f"}
	}
}
```

**Complex Filters Example:**

```json theme={null}
{
  "filters": {
    "$and": [
      {"document_type": {"$eq": "report"}},
      {"metadata.topic": {"$ilike": "finance"}}
    ]
  }
}
```

### **Hybrid Search**

Hybrid search combines **semantic similarity** with **keyword-based retrieval**, improving result relevance by leveraging both vector embeddings and traditional text search.

Enable hybrid search by setting `use_hybrid_search`: `true` in `search_settings `and configure with `hybrid_settings` .

**Configuration Example:**

```json theme={null}
{
	"use_hybrid_search": true,
	"hybrid_settings": {
    	"full_text_weight": 1.0,
    	"semantic_weight": 5.0,
    	"full_text_limit": 200,
    	"rrf_k": 50
	}
}
```

**Parameters:**

* `full_text_weight`: Adjusts the influence of keyword search.
* `semantic_weight`: Adjusts the influence of semantic similarity.
* `full_text_limit`: Limits keyword results before fusion.
* `rrf_k`: Rank fusion parameter controlling hybrid blending strength.

### **Graph-Enhanced Search**

The Search API supports **knowledge graph integration**, enabling entity- and relationship-aware retrieval.

This allows search results to include contextually related information based on graph traversal.

Knowledge graph integration is enabled by default. Configure it with `graph_search_settings` .

**Configuration Example:**

```json theme={null}
{
	"graph_search_settings": {
    	"use_graph_search": true,
    	"kg_search_type": "local"
	}
}
```

**Parameters:**

* `use_graph_search`: Enables or disables graph integration.
* `kg_search_type`: Defines scope — `"local"` (collection-level) or `"global"` (across all graphs).


# Streaming Retrieval API
Source: https://io.net/docs/reference/rag/retrieval/streaming-retrieval-api

The R2R Streaming Retrieval API provides real-time streaming for RAG and agent interactions, emitting structured events such as search results, reasoning steps, and final responses. It enables interactive, low-latency experiences for AI-driven applications.

The **Streaming Retrieval API** in R2R enables **real-time data flow** for Retrieval-Augmented Generation (RAG) and agent-based interactions. It delivers live updates as content is retrieved, processed, and generated, allowing client applications to display results incrementally.

This streaming approach significantly improves the user experience for interactive and latency-sensitive applications by providing immediate, progressive feedback instead of waiting for full completion.

### Key Capabilities

The Streaming Retrieval API supports:

* **Real-time event streaming** for RAG and agent operations.
* **Progressive response generation** with token-level updates.
* **Immediate access to intermediate results** such as retrieved documents or citations.
* **Fine-grained event structure** to handle reasoning steps, tool calls, and responses.
* **Improved responsiveness** for conversational and research-oriented applications.

## Streaming Events

During streaming, R2R emits structured event types that represent each stage of the retrieval and generation process:

| Event Type           | Description                                                              |
| -------------------- | ------------------------------------------------------------------------ |
| `SearchResultsEvent` | Contains initial search results from documents.                          |
| `MessageEvent`       | Streams partial response tokens as they are generated.                   |
| `CitationEvent`      | Indicates when a citation has been added to the response.                |
| `ThinkingEvent`      | Provides insight into the model’s internal reasoning steps (for agents). |
| `ToolCallEvent`      | Indicates when the model invokes a tool during processing (for agents).  |
| `ToolResultEvent`    | Returns the results from previously called tools (for agents).           |
| `FinalAnswerEvent`   | Contains the complete generated answer with citations.                   |

## Streaming RAG

### Basic Streaming RAG

To use streaming with basic RAG functionality:

<CodeGroup>
  ```python python theme={null}
  from r2r import (
      CitationEvent,
      FinalAnswerEvent,
      MessageEvent,
      SearchResultsEvent,
      R2RClient,
  )

  client = R2RClient("http://localhost:7272")

  result_stream = client.retrieval.rag(
      query="What is DeepSeek R1?",
      search_settings={"limit": 25},
      rag_generation_config={"stream": True},
  )

  for event in result_stream:
      if isinstance(event, SearchResultsEvent):
          print("Search results:", event.data)
      elif isinstance(event, MessageEvent):
          print("Partial message:", event.data.delta)
      elif isinstance(event, CitationEvent):
          print("New citation detected:", event.data)
      elif isinstance(event, FinalAnswerEvent):
          print("Final answer:", event.data.generated_answer)
          print("Citations:", event.data.citations)
  ```

  ```bash curl theme={null}
  curl -X POST https://api.intelligence.io.solutions/api/r2r/v3/retrieval/rag /
    -H "Content-Type: application/json" /
    -H "Accept: text/event-stream" /
    -d '{
      "query": "What is DeepSeek R1?",
      "search_settings": {"limit": 25},
      "rag_generation_config": {"stream": true}
    }' /
    -H "Authorization: Bearer \$IOINTELLIGENCE_API_KEY"
  ```
</CodeGroup>

### Streaming RAG with Web Search

To include web search in your streaming RAG:

<CodeGroup>
  ```python python theme={null}
  result_stream = client.retrieval.rag(
      query="What are the latest developments with DeepSeek R1?", 
      rag_generation_config={"stream": True},
      include_web_search=True
  )

  for event in result_stream:
      # Process events as shown in previous example
      pass
  ```
</CodeGroup>

## Streaming Agent

R2R provides powerful streaming agents that supports complex interactions with both document-based knowledge and web resources.

### Basic Streaming Agent

<CodeGroup>
  ```python python theme={null}
  from r2r import (
      ThinkingEvent,
      ToolCallEvent,
      ToolResultEvent,
      CitationEvent,
      MessageEvent,
      FinalAnswerEvent,
  )

  agent_stream = client.retrieval.agent(
      query="What does DeepSeek R1 imply for the future of AI?",
      generation_config={"stream": True},
      mode="research"
  )

  for event in agent_stream:
      if isinstance(event, ThinkingEvent):
          print(f"🧠 Thinking: {event.data.delta.content[0].payload.value}")
      elif isinstance(event, ToolCallEvent):
          print(f"🔧 Tool call: {event.data.name}({event.data.arguments})")
      elif isinstance(event, ToolResultEvent):
          print(f"📊 Tool result: {event.data.content[:60]}...")
      elif isinstance(event, CitationEvent):
          print(f"📑 Citation: {event.data}")
      elif isinstance(event, MessageEvent):
          print(f"💬 Message: {event.data.delta.content[0].payload.value}")
      elif isinstance(event, FinalAnswerEvent):
          print(f"✅ Final answer: {event.data.generated_answer[:100]}...")
          print(f"   Citations: {len(event.data.citations)} sources referenced")
  ```
</CodeGroup>

### Advanced Research Agent with Tools

The R2R agent can leverage multiple tools to perform in-depth research:

<CodeGroup>
  ```python python theme={null}
  agent_stream = client.retrieval.agent(
      query="Analyze DeepSeek R1's performance compared to other models",
      generation_config={
          "model": "anthropic/claude-3-7-sonnet-20250219",
          "extended_thinking": True,
          "thinking_budget": 4096,
          "temperature": 1,
          "max_tokens_to_sample": 16000,
          "stream": True
      },
      mode="research",
      rag_tools=["web_search", "web_scrape"]
  )

  # Process events as shown in previous example
  ```
</CodeGroup>

## Streaming Citations

R2R streaming citations provide detailed attribution information that links specific parts of the response to source documents:

<CodeGroup>
  ```json json theme={null}
  {
    "event": "citation",
    "data": {
      "id": "abc123",
      "object": "citation",
      "raw_index": 1,
      "index": 1,
      "start_index": 305,
      "end_index": 308,
      "source_type": "chunk",
      "source_id": "e760bb76-1c6e-52eb-910d-0ce5b567011b",
      "document_id": "e43864f5-a36f-548e-aacd-6f8d48b30c7f",
      "source_title": "DeepSeek_R1.pdf"
    }
  }
  ```
</CodeGroup>

Each citation includes:

* `id`: Unique identifier for the citation.
* `index`: The display index (e.g., /\[1], /\[2]).
* `start_index` and `end_index`: Character positions in the response.
* `source_type`: The type of source (chunk, graph, web).
* `source_id`: ID of the specific chunk/node.
* `document_id`: ID of the parent document.
* `source_title`: Title of the source document.

## Implementing Streaming UI

To create a responsive UI with Streaming RAG, consider the following:

### Frontend Implementation

<CodeGroup>
  ```python React theme={null}
  import { useState, useEffect } from 'react';

  function RAGComponent() {
    const [messages, setMessages] = useState([]);
    const [currentMessage, setCurrentMessage] = useState('');
    const [citations, setCitations] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (query) => {
      setIsLoading(true);
      setCurrentMessage('');
      setCitations([]);
      
      try {
        const response = await fetch('/api/rag', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            query,
            stream: true
          })
        });
        
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          
          const chunk = decoder.decode(value);
          const events = chunk.split('/n/n').filter(Boolean);
          
          for (const eventText of events) {
            if (!eventText.startsWith('data: ')) continue;
            
            const eventData = JSON.parse(eventText.slice(6));
            
            switch (eventData.event) {
              case 'message':
                setCurrentMessage(prev => prev + eventData.data.delta.content[0].payload.value);
                break;
              case 'citation':
                setCitations(prev => [...prev, eventData.data]);
                break;
              case 'final_answer':
                setMessages(prev => [...prev, {
                  role: 'assistant',
                  content: eventData.data.generated_answer,
                  citations: eventData.data.citations
                }]);
                break;
            }
          }
        }
      } catch (error) {
        console.error('Error with streaming RAG:', error);
      } finally {
        setIsLoading(false);
      }
    };

    return (
      <div className="rag-container">
        {/* UI implementation */}
        {isLoading && <div className="typing-indicator">{currentMessage}</div>}
        {/* Display messages and citations */}
      </div>
    );
  }
  ```
</CodeGroup>


# Overview
Source: https://io.net/docs/reference/rag/system

The R2R System API provides health check and monitoring capabilities for verifying platform availability and responsiveness. It enables diagnostics and readiness validation to ensure stable operation across internal and external services.

The **System** endpoints in R2R provide core operational insights and utilities for monitoring and maintaining the platform’s overall health. These endpoints are primarily used to verify uptime, perform diagnostics, and ensure that the infrastructure remains responsive for both API consumers and internal services.

They form the foundation for system reliability, enabling developers and administrators to quickly assess service readiness and detect potential performance issues.

### Key Capabilities

The System endpoints in R2R enable:

* **Health monitoring** for core platform services.
* **Diagnostics** to verify API and service responsiveness.
* **Operational readiness checks** for infrastructure stability.
* **Integration monitoring** to ensure dependent systems remain connected.
* **Foundational support** for automated uptime verification and alerting.

## API Endpoints

| Method | Endpoint                                      | Description                               |
| ------ | --------------------------------------------- | ----------------------------------------- |
| GET    | [/health](/reference/rag/system/health-check) | Check system health and readiness status. |


# Check system health
Source: https://io.net/docs/reference/rag/system/health-check

openapi/rag-system/health-check.json get /api/r2r/v3/health
Checks the availability and uptime status of the R2R API.



# Overview
Source: https://io.net/docs/reference/rag/users

The R2R Users API manages authenticated entities, enabling secure access, permissions, and collaboration. It provides endpoints for user details, collection membership, limits, and administrative control to support reliable identity management.

A **User** in R2R represents an **authenticated entity** that can interact with the platform. Users are the foundation of R2R’s **access control system**, enabling granular permission management, content organization, and activity tracking through collections and system-level privileges.

Users serve as the primary link between human operators and the R2R platform, managing ownership, collaboration, and administrative functions across all resources.

### Key Capabilities

Users in R2R provide:

* **Authentication and authorization** to ensure secure system access.
* **Collection membership management** for organizing and sharing content.
* **Activity tracking and analytics** for monitoring user behavior and engagement.
* **Metadata customization** to enrich user profiles and associated data.
* **Superuser capabilities** for managing system-wide configurations and administrative tasks.

## API Endpoints

| Method | Endpoint                                                                 | Description                                              |
| ------ | ------------------------------------------------------------------------ | -------------------------------------------------------- |
| GET    | [/users/](/reference/rag/users/get-user-by-id)                           | Retrieve detailed information about a specific user.     |
| GET    | [/users//collections](/reference/rag/users/list-users-collections)       | List all collections that the user is a member of.       |
| POST   | [/users//collections/](/reference/rag/users/add-collection-to-user)      | Add the user to a specified collection.                  |
| DELETE | [/users//collections/](/reference/rag/users/delete-user-from-collection) | Remove a user from a specified collection                |
| GET    | [/users//limits](/reference/rag/users/get-user-limits)                   | Retrieve user-specific limits and quotas.                |
| GET    | [/users/me](/reference/rag/users/get-current-user)                       | Retrieve details about the currently authenticated user. |


# Add user to collection
Source: https://io.net/docs/reference/rag/users/add-collection-to-user

openapi/rag-users/add-collection-to-user.json post /api/r2r/v3/users/{id}/collections/{collection_id}
Grants a user access to an existing collection.



# Remove user from collection
Source: https://io.net/docs/reference/rag/users/delete-user-from-collection

openapi/rag-users/delete-user-from-collection.json delete /api/r2r/v3/users/{id}/collections/{collection_id}
Remove a user from a collection. Requires either superuser status or access to the collection.



# Get authenticated user details
Source: https://io.net/docs/reference/rag/users/get-current-user

openapi/rag-users/get-current-user.json get /api/r2r/v3/users/me
Get detailed information about the currently authenticated user.



# Get user details
Source: https://io.net/docs/reference/rag/users/get-user-by-id

openapi/rag-users/get-user-by-id.json get /api/r2r/v3/users/{id}
Get detailed information about a specific user. Users can only access their own information unless they are superusers.



# Fetch User Limits
Source: https://io.net/docs/reference/rag/users/get-user-limits

openapi/rag-users/get-user-limits.json get /api/r2r/v3/users/{id}/limits
Return the system default limits, user-level overrides, and final “effective” limit settings for the specified user.

Only superusers or the user themself may fetch these values.


# List user's collections
Source: https://io.net/docs/reference/rag/users/list-users-collections

openapi/rag-users/list-users-collections.json get /api/r2r/v3/users/{id}/collections
Get all collections associated with a specific user. Users can only access their own collections unless they are superusers.



# Create Sub-API Key
Source: https://io.net/docs/reference/sub-keys/create-sub-key

openapi/sub-keys/create-sub-key.json post /v1/api-keys/sub-keys
Creates a new sub-API key scoped under an admin key, with optional model restrictions and per-key credit limits.

<Note>
  The full key `value` is returned **only once** at creation time. Store it securely — it cannot be retrieved again. Only the truncated `display` string is stored and returned in subsequent list or usage calls.
</Note>

<Note>
  Only admin API keys can create sub-keys. A sub-key cannot create further sub-keys. If you authenticate with a sub-key, the endpoint returns **403 Forbidden**.
</Note>

### Key fields

* `description` – A human-readable label to identify the key's purpose or owner.

* `allowed_models` – An optional list of model identifiers (e.g. `"meta-llama/Llama-3.3-70B-Instruct"`) that this sub-key is permitted to call. If omitted, all models available to the admin are accessible. Requests to unlisted models are rejected with **403 Forbidden**.

* `credit_limit` – Maximum IO Intelligence credits the sub-key may consume per refresh cycle. Once the limit is reached the key is automatically blocked until the cycle resets or the admin raises the limit via `PATCH`. Set to `null` to impose no per-key cap.

* `credit_refresh_cycle` – How often the usage counter resets: `"8h"`, `"daily"`, `"weekly"`, or `"monthly"` (default).

* `expires_at` – ISO 8601 date-time for key expiry, or the literal string `"never"` for a non-expiring key. Defaults to 180 days from creation when omitted.

* `key_prefix` – An optional lowercase slug (2–8 chars) prepended to the generated key value (e.g. `"acme"` produces `acme-v2-eyJ...`). Defaults to the standard `io-v2` prefix when omitted. Cannot start with `"io"` or contain version markers like `"-v2"`.


# Get All Sub-Keys Usage
Source: https://io.net/docs/reference/sub-keys/get-all-keys-usage

openapi/sub-keys/get-all-keys-usage.json get /v1/api-keys/sub-keys/usage
Returns aggregated token usage and credit cost for every sub-key owned by the admin, broken down by model for today and all time.

This endpoint is designed for admin-level billing dashboards. It returns a breakdown per sub-key, with each entry showing:

* **`today`** — token consumption and credit cost since midnight UTC.
* **`all_time`** — cumulative consumption since the sub-key was created.
* **`totals`** — aggregate `today_credit_cost` and `all_time_credit_cost` across all sub-keys.

Each entry's `models` array shows which models were used and their individual costs, allowing you to see exactly where credits are being spent.

<Note>
  This endpoint requires the Intelligence database to be reachable. It returns **503 Service Unavailable** if the intelligence database is temporarily unavailable.
</Note>


# Get Sub-Key Usage
Source: https://io.net/docs/reference/sub-keys/get-key-usage

openapi/sub-keys/get-key-usage.json get /v1/api-keys/sub-keys/{key_id}/usage
Returns credit status for a specific sub-key: credits used in the current billing period, the configured limit, and remaining allowance.

Use this endpoint to monitor whether a specific sub-key is approaching or has exceeded its credit limit.

The `remaining_credit` field is `null` when no `credit_limit` has been configured for the key — in that case, the key is only bounded by the admin's overall account balance.

<Note>
  Credit usage reflects **settled** payments processed by the billing pipeline. There may be a short lag (typically under a minute) between a completed inference call and the usage appearing here.
</Note>


# Get Own Usage (Sub-Key Self-Service)
Source: https://io.net/docs/reference/sub-keys/get-own-usage

openapi/sub-keys/get-own-usage.json get /v1/api-keys/sub-keys/me/usage
Allows a sub-key to check its own credit status without exposing the admin key to the sub-key holder.

This endpoint is authenticated with the **sub-key itself**, not the admin key. It is intended for scenarios where sub-key holders need to monitor their own remaining credits programmatically.

<Note>
  Authenticating with an admin key returns **403 Forbidden**. Use `GET /v1/api-keys/sub-keys/{key_id}/usage` with the admin key to inspect a specific sub-key's status.
</Note>

### Typical use case

A service that holds a sub-key can call this endpoint periodically to determine how much credit remains before being blocked:

```bash theme={null}
curl "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/me/usage" \
  -H "x-api-key: $SUB_API_KEY"
```

```json theme={null}
{
  "status": "succeeded",
  "data": {
    "key_id": "71775d2e-fbcc-4ef4-aa30-8aaeb82062c0",
    "credit_used": 7.82,
    "credit_limit": 10.0,
    "remaining_credit": 2.18,
    "credit_refresh_cycle": "monthly"
  }
}
```


# List Sub-API Keys
Source: https://io.net/docs/reference/sub-keys/list-sub-keys

openapi/sub-keys/list-sub-keys.json get /v1/api-keys/sub-keys
Returns all active sub-API keys owned by the authenticated admin key, including current-period credit usage for each key.

The response includes one entry per active sub-key with the following credit fields:

* `credit_limit` — the per-cycle cap configured for the key (`null` means no per-key cap).
* `credit_used` — credits consumed so far in the **current** billing period (resets according to `credit_refresh_cycle`).

<Note>
  Expired or revoked keys are not included in this list.
</Note>


# Revoke Sub-API Key
Source: https://io.net/docs/reference/sub-keys/revoke-sub-key

openapi/sub-keys/revoke-sub-key.json delete /v1/api-keys/sub-keys/{key_id}
Immediately revokes a sub-API key. All subsequent requests using the revoked key receive 401 Unauthorized.

<Warning>
  Revocation is **permanent and immediate**. Once revoked, the key cannot be restored. Issue a new sub-key if access needs to be reinstated.
</Warning>

Any in-flight request that was authenticated before revocation may still complete. Revocation takes effect for all new authentication attempts.


# Update Sub-API Key
Source: https://io.net/docs/reference/sub-keys/update-sub-key

openapi/sub-keys/update-sub-key.json patch /v1/api-keys/sub-keys/{key_id}
Updates one or more attributes of an existing sub-API key. Omitted fields are left unchanged.

All body fields are optional — only the fields you include will be updated.

### Unblocking an over-limit key

When a sub-key's `credit_used` exceeds its `credit_limit`, the key is automatically blocked (returns **429 Too Many Requests** on inference calls). To unblock it without waiting for the next cycle reset, raise the `credit_limit` via this endpoint:

```bash theme={null}
curl -X PATCH "https://api.intelligence.io.solutions/v1/api-keys/sub-keys/{key_id}" \
  -H "x-api-key: $ADMIN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"credit_limit": 50.0}'
```

### Clearing model restrictions

Pass an empty array for `allowed_models` to remove all model restrictions, giving the sub-key access to all models available to the admin:

```json theme={null}
{ "allowed_models": [] }
```


# Deploy a VM
Source: https://io.net/docs/reference/vmaas/deploy-vms

openapi/vmaas/deploy-vms.json post /enterprise/v1/io-cloud/vmaas/deploy



# Destroy Deployment
Source: https://io.net/docs/reference/vmaas/destroy-deployment

openapi/vmaas/destroy-deployment.json delete /enterprise/v1/io-cloud/vmaas/deployment/{deployment_id}
Terminate and remove an existing deployment. All VMs and resources allocated to the deployment will be released.

<Note>
  When deleting a deployment, charges are handled as follows;

  * The first hour is **ALWAYS non-refundable**.
  * After the first hour, charges are calculated **to the exact duration** the cluster was active (not rounded to whole hours).
  * Any unused prepaid time is **refunded proportionally**.

  Example: If you pre-paid for 3 hours and delete the deployment after 1.2 hours, you are charged for 1.2 hours and refunded the remaining 1.8 hours.
</Note>


# Cluster Deployment using APIs
Source: https://io.net/docs/reference/vmaas/example-deploying-using-APIs

Step-by-step guide for developers to deploy, price, and manage GPU clusters programmatically using io.net Cloud VMaaS APIs.

This page outlines the end-to-end flow for deploying a GPU cluster using [**io.net**](http://io.net) **Cloud VMaaS APIs**. It is intended to help you understand the steps you can take and API calls needed to provision, price, and manage a cluster programmatically.

### Workflow Summary

The cluster deployment process consists of the following steps:

1. **Retrieve available hardware**

   Use the [**GET Hardware List**](/reference/vmaas/get-hardware-list) endpoint to fetch all supported GPU hardware configurations, including available GPU counts, locations, and resource specifications.
2. **Select hardware and configuration**\
   From the hardware list response, select the desired hardware type, number of GPUs per VM, and deployment region.
3. **Validate deployment pricing (optional)**\
   Use the [**GET Deployment Price**](/reference/vmaas/get-deployment-price) endpoint to calculate the expected cost for the selected hardware configuration and duration.
4. **Deploy the cluster**

   Use the [**POST Deploy VM**](/reference/vmaas/deploy-vms) endpoint to provision the cluster using the selected hardware, GPU count, location, and duration.
5. **Manage the cluster lifecycle**

   After deployment, manage the cluster using one of the following endpoints:

   * [**POST Extend Cluster**](/reference/vmaas/extend-cluster) endpoint to increase the deployment duration.
   * [**DELETE Destroy Deployment**](/reference/vmaas/destroy-deployment) endpoint to terminate the cluster early.

<Note>
  The first hour of usage is non-refundable.
</Note>

<Steps>
  <Step title="Retrieving Available Hardware">
    Using the [GET Hardware List](/reference/vmaas/get-hardware-list) endpoint, retrieve all currently available GPU hardware configurations.

    **Request Example**

    ```bash theme={null}
    curl -X 'GET' \
      'https://api.io.solutions/enterprise/v1/io-cloud/vmaas/hardware' \
      -H 'accept: application/json' \
      -H 'x-api-key: <api-key>'
    ```

    <Accordion title="Response Example">
      ```json theme={null}
      {
          "data": {
              "hardware": [
                  {
                      "id": "12__2",
                      "deploy_id": 12,
                      "name": "GeForce RTX 4090",
                      "num_cards": 2,
                      "supplier": "internal",
                      "sold_out": false,
                      "price": 0.6,
                      "vram_per_card": 24,
                      "interconnect": null,
                      "nvlink": false,
                      "storage": 1000,
                      "vcpu": 39,
                      "memory": 125,
                      "location": "US"
                  },
                  {
                      "id": "12__1",
                      "deploy_id": 12,
                      "name": "GeForce RTX 4090",
                      "num_cards": 1,
                      "supplier": "internal",
                      "sold_out": false,
                      "price": 0.3,
                      "vram_per_card": 24,
                      "interconnect": null,
                      "nvlink": false,
                      "storage": 500,
                      "vcpu": 39,
                      "memory": 125,
                      "location": "US"
                  },
                  {
                      "id": "B200_sxm6x8__US",
                      "deploy_id": "B200_sxm6x8",
                      "name": "B200",
                      "num_cards": 8,
                      "supplier": "external",
                      "sold_out": false,
                      "price": 39.92,
                      "vram_per_card": 192,
                      "interconnect": "sxm6",
                      "nvlink": false,
                      "storage": 22528,
                      "vcpu": 208,
                      "memory": 2900,
                      "location": "US"
                  },
                  {
                      "id": "B200_sxm6x8__AU",
                      "deploy_id": "B200_sxm6x8",
                      "name": "B200",
                      "num_cards": 8,
                      "supplier": "external",
                      "sold_out": false,
                      "price": 39.92,
                      "vram_per_card": 192,
                      "interconnect": "sxm6",
                      "nvlink": false,
                      "storage": 22528,
                      "vcpu": 208,
                      "memory": 2900,
                      "location": "AU"
                  }
              ]       
           }
      }
      ```
    </Accordion>
  </Step>

  <Step title="Selecting your Hardware and Configuration">
    From the response of the [GET Hardware List](/reference/vmaas/get-hardware-list) endpoint, select your chosen GPU and save the following values:

    <ResponseField name="deploy_id" type="string/integer">
      Hardware identifier used for pricing and deployment. Can be a string or integer.
    </ResponseField>

    <ResponseField name="num_cards" type="integer">
      Number of GPUs per VM.
    </ResponseField>

    <ResponseField name="location" type="string">
      Deployment region.
    </ResponseField>
  </Step>

  <Step title="Validating your Deployment Price (Optional)">
    Using the [GET Deployment Price](/reference/vmaas/get-deployment-price) endpoint and the values you have saved, validate the price of your desired deployment before you deploy your cluster.

    **Request Example**

    ```bash theme={null}
    curl -X GET "https://api.io.solutions/enterprise/v1/io-cloud/vmaas/price" \
      -H "x-api-key: YOUR_API_KEY" \
      --data-urlencode "hardware_id=12" \
      --data-urlencode "gpus_per_vm=1" \
      --data-urlencode "replica_count=1" \
      --data-urlencode "duration_hours=1" \
      --data-urlencode "currency=usdc" \
      --data-urlencode 'location_ids=["US"]'
    ```

    Ensure that the following fields have been assigned a value:

    <ResponseField name="hardware_id" type="string/integer">
      Value of `deploy_id` from the Hardware List response.
    </ResponseField>

    <ResponseField name="gpus_per_vm" type="integer">
      Number of GPUs per VM. Value of `num_cards` from the Hardware List response.
    </ResponseField>

    <ResponseField name="duration_hours" type="integer">
      Duration of your deployment, in hours.
    </ResponseField>

    <ResponseField name="currency" type="string">
      Pricing currency.

      *Example:* `usdc`
    </ResponseField>

    <ResponseField name="location_ids" type="string">
      URL-encoded JSON array of locations. Use `--data-urlencode`  in your cURL request if you use a plain string.

      *Example:* `%5B%22US%22%5D` = `["US"]`
    </ResponseField>
  </Step>

  <Step title="Deploying your Cluster">
    Using the POST Deploy VM enndpoint, deploy your selected hardware for the specified duration.

    **Request Example**

    ```bash theme={null}
    curl -X POST "https://api.io.solutions/enterprise/v1/io-cloud/vmaas/deploy" \
      -H "Content-Type: application/json" \
      -H 'x-api-key: <api-key>'
      -d '{
        "resource_private_name": "name of cluster",
        "duration_hours": 1,
        "gpus_per_vm": 1,
        "hardware_id": 12,
        "location_ids": ["US"],
        "ssh_keys": {
          "name of key": "<public-key>"
        }
      }'
    ```

    Ensure that the following fields have been assigned a value:

    <ResponseField name="resource_private_name" type="string">
      The name of your cluster.
    </ResponseField>

    <ResponseField name="duration_hours" type="integer">
      Duration of your deployment, in hours.
    </ResponseField>

    <ResponseField name="gpus_per_vm" type="integer">
      Number of GPUs per VM. Value of `num_cards` from the Hardware List response.
    </ResponseField>

    <ResponseField name="hardware_id" type="string/integer">
      Value of `deploy_id` from the Hardware List response.
    </ResponseField>

    <ResponseField name="location_ids" type="string">
      Location of your chosen GPU.
    </ResponseField>

    <ResponseField name="ssh_keys" type="object">
      Your public SSH key, use RSA, ECDSA, or ED25519.

      *Format:* `"name of key": "<public-key>"`
    </ResponseField>
  </Step>
</Steps>


# Extend Cluster
Source: https://io.net/docs/reference/vmaas/extend-cluster

openapi/vmaas/extend-cluster.json post /enterprise/v1/io-cloud/vmaas/deployment/{deployment_id}/extend
Extend the lifetime or capacity of an existing deployment by adding more resources or increasing its duration.



# Get All Deployments
Source: https://io.net/docs/reference/vmaas/get-all-deployments

openapi/vmaas/get-all-deployments.json get /enterprise/v1/io-cloud/vmaas/deployments
Retrieve a list of all VMaaS deployments associated with the enterprise account, including their status, configuration, and metadata.



# Get Deployment Details
Source: https://io.net/docs/reference/vmaas/get-deployment-details

openapi/vmaas/get-deployment-details.json get /enterprise/v1/io-cloud/vmaas/deployment/{deployment_id}
Fetch detailed information about a specific deployment by its ID, including cluster specifications, runtime status, and associated resources.



# Get Deployment Price
Source: https://io.net/docs/reference/vmaas/get-deployment-price

openapi/vmaas/get-deployment-price.json get /enterprise/v1/io-cloud/vmaas/price
Calculate or retrieve the pricing details for a deployment based on selected resources (CPUs, GPUs, memory, and duration).



# Get Deployment VMs
Source: https://io.net/docs/reference/vmaas/get-deployment-vms

openapi/vmaas/get-deployment-vms.json get /enterprise/v1/io-cloud/vmaas/deployment/{deployment_id}/vms
List all virtual machines running within a given deployment, along with their current state and hardware details.



# Get Hardware List
Source: https://io.net/docs/reference/vmaas/get-hardware-list

openapi/vmaas/get-hardware-list.json get /enterprise/v1/io-cloud/vmaas/hardware
Retrieve a list of currently available GPUs and configurations.



# Getting Started with VMaaS API
Source: https://io.net/docs/reference/vmaas/get-started-with-vmaas-api



The **Virtual Machine as a Service (VMaaS) APIs** lets you programmatically deploy and manage virtual machines on io.net Cloud. Unlike CaaS (Containers as a Service), VMaaS provides full VM instances with CPU, GPU, memory, and storage resources — ideal for long-running workloads, custom environments, or GPU-intensive tasks.

## Generate an API key

You can obtain an API key for io.net Cloud to use VMaaS in two ways:

1. From the web interface.
2. By using a two-step process (first generate a JWT token, then request the API key using curl).

### Option 1: Generate an API Key via Web Interface

IO Clouds APIs authenticate requests using API keys. You can [generate API keys from your user](https://ai.io.net/ai/api-keys) account.\
**Note: When generating an API key, make sure to specify the associated IO Cloud project.**

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service in your backend server.
</Warning>

### Option 2: Generate an API Key Using a JWT Token

#### Step 1: Get a JWT Token

io.net APIs are built around [RESTful](https://en.wikipedia.org/wiki/REST) principles. You can use io.net APIs to gain insight into different elements of the network.

To use [io.net](http://io.net) APIs, you must provide a JWT token in the header of your request.

Follow the instructions below to generate a token:

1. Go to **io.net** > **IO ID** > **IO Clouds** tab.
2. In the UI, right-click and select **Inspect**.
3. In the Inspect tool, click **Network**.
4. Refresh the **IO Clouds** page.
5. In the list of elements, click **Devices**.
6. Scroll down to the **Request Headers** section.
7. Copy and store the token.

<Note>
  This token is valid for 21 days.
</Note>

<img alt="Vmaas1 Jp" />

#### Step 2. Generate an API Key via `curl`

Use the **JWT token** to request your API key:

```curl theme={null}
curl -X POST 'https://api.io.solutions/v1/api-keys/' \
  -H 'accept: application/json' \
  -H 'token: $JWT_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "description": "API Key Name",
    "expires_at": "2025-07-17T19:54:36.418Z",
    "project": "io-cloud",
    "scopes": ["all"]
}'
```

Use the returned key with the `X-API-KEY` header in your requests.

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service in your backend server.
</Warning>

<img alt="Vmaas2 Jp" />

## Making requests

<Note>
  Accessing APIs requires IO credits. Make sure you have sufficient IO credits before using any API endpoint.

  Contact support or visit the IO Credits documentation page for more details.
</Note>

Include the API key in an `Authorization` HTTP header for all API requests:

```
Authorization: X-API-KEY $IOCLOUD_API_KEY
```

Replace `$IOCLOUD_API_KEY` with your **API key**.

### Example: Deploy VMs

The following `curl` command demonstrates how to deploy VMs in IO Cloud.\
Make sure to include your `x-api-key` header and, if needed, adjust the query parameters such as `status`, `page`, or `page_size`.:

```curl theme={null}
curl -X POST "https://api.io.solutions/enterprise/v1/io-cloud/vmaas/deploy?page=0&page_size=10&status=running" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY_HERE" \
  -d '{
    "name": "test-deployment",
    "hardware_quantity": 2,
    "hardware_name": "NVIDIA A100",
    "region": "us-east-1"
  }'
```

This request should return a similar response:

```json theme={null}
{
  "data": {
    "deployments": [
      {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "status": "running",
        "name": "test-deployment",
        "completed_percent": 75,
        "hardware_quantity": 2,
        "brand_name": "NVIDIA",
        "hardware_name": "A100",
        "compute_minutes_served": 120,
        "compute_minutes_remaining": 240
      }
    ],
    "total": 1,
    "statuses": ["running"]
  }
}
```


# Get a VM's Jobs History
Source: https://io.net/docs/reference/vmaas/get-vms-jobs-history

openapi/vmaas/get-vms-jobs-history.json get /enterprise/v1/io-cloud/vmaas/deployment/{deployment_id}/vms-jobs/{container_id}
Retrieve the job execution history for a specific VM or container within a deployment. Includes logs and status of completed or active jobs.



