# Source: https://docs.kaisar.io/kaisar-network/kaisar-rewards-mechanism/rewards-for-kaisar-providers.md

# Rewards for Kaisar Providers

The Kaisar network uses a reward system to encourage participation and maintain efficient network operations. Users who run workers and provide GPU resources are rewarded with KAI tokens. The amount of rewards receive is calculated as described below.

In the Kaisar network, rewards for computing resource providers (workers) are distributed based on two main mechanisms: Proof of Capacity (PoC) and Proof of Delivery (PoD). Both mechanisms are designed to incentivize maintaining online resources and completing rendering tasks.

### 1.  Proof of Capacity (PoC)&#x20;

**Purpose:** Incentivize workers to keep computing resources (containers) online and ready for tasks, even when there are no specific jobs. This ensures the network maintains a stable and reliable pool of available resources.

**Eligibility:** Any container that remains online and meets the network’s uptime requirements qualifies for PoC rewards.

**Total PoC rewards in one Epoch**

$$
\text {PoC\_Total\_Reward} = (1- \text{Ratio} ) \times \text{Epoch\_Total\_Reward}
$$

**PoC reward for Worker node in one Epoch**

$$
\text{PoC\_Worker\_Reward} = \frac {\text{PoC\_Worker\_Score} \times  \text{PoC\_Total\_Reward}}{\text{PoC\_Total\_Score}}
$$

### 2. Proof of Delivery (PoD)

**Purpose:** To reward the successful completion of rendering tasks, incentivizing workers to actively contribute computational power to process workloads and deliver high-quality results.

**Conditions:** Containers that participate in rendering tasks and successfully complete them within the stipulated timeframe will be eligible to receive the PoD reward.

**Total PoD rewards in one Epoch**

$$
\text{PoD\_Total\_Reward} =\text{Ratio} \times \text{Epoch\_Total\_Reward}
$$

**PoD reward for Worker node in one Epoch**

$$
\text{PoD\_Worker\_Reward} =\frac { \text{PoD\_Worker\_Score} \times \text{PoD\_Total\_Reward}}{\text{PoD\_Total\_Score}}
$$

### 3. Worker Node Reward

For a given worker node 𝑖, the reward calculated per epoch is the total aggregated PoC and PoD rewards of the worker node, determined according to the following formula:

$$
\text{Worker\_Reward} = \frac{\text{Worker\_Score} \times \text{Epoch\_Total\_Reward} \times (1- \text{Commission)}}{\text{Total\_Score}}
$$

* **Worker\_Score**: The score of the worker in the epoch.
* **Epoch\_Total\_Reward**: The total reward allocated to all workers in one epoch.
* **Commission**: The commission rate rewarded to the delegator.
* **Total\_Score**: The total score of all workers.

### 4. Reward calculation for Delegator

At the end of each epoch, after reward calculations, a portion of the tokens allocated to Workers is distributed into the reward pool for supporting Delegators. The Delegator reward pool for each epoch is calculated as follows:

$$
\text{Delegator\_Total\_Reward} = \frac{\text{Worker\_Score} \times \text{Epoch\_Total\_Reward} \times \text{Commission}}{\text{Total\_Score}}
$$

For a Delegator, rewards are calculated per epoch based on the following factors:

$$
\text{Delegator\_Reward} = \frac{\text{Delegator\_Total\_Reward} \times \text{Delegator\_Stake}}{\text{Total\_Stake}}
$$

### 5. Formula for Calculating Worker Node Points&#x20;

The score of the node in one epoch is calculated according to the following formula:

$$
\begin{aligned}
\text{Worker\_Score} &= (Uptime + Jobtime \times W\_j) \\
&\quad \times \left( 1 + \frac{\text{Worker\_Stake}}{\text{Max\_Stake}} \right) \\
&\quad \times \left( A \times W\_a  + B \times W\_b + C \times W\_c + D \times W\_d +  E \times W\_e \right)
\end{aligned}
$$

* **Uptime**: The total operational time of the Worker, measured in hours.
* **Jobtime**: The time taken to complete a Job, measured in hours.
* **Worker\_Stake**: The amount of KAI tokens staked for the Worker Node.
* **Stake\_Max**: The maximum amount of KAI tokens that can be staked for the Worker Node.
* **A:**  The bandwidth score of the node (0-1)
* **B:**  The CPU score of the node (0-1)
* **C:**  The GPU score of the node (0-10)
* **D:**  The Disk score of the node (0-1
* **E:**  The Memory score of the node (0-1)

Balancing weights are assigned to each factor:

Wa = 2 , Wb = 1, Wc = 3, Wd = 1, We = 1, Wj = 3

**Bandwidth scoring system**

| Tier         | Speed                                             | Score |
| ------------ | ------------------------------------------------- | ----- |
| Ultra Speed  | Download: 1600 mb/s Upload: 1200 mb/s             | 0.8   |
| High Speed   | <p>Download: 800 mb/s </p><p>Upload: 600 mb/s</p> | 0.6   |
| Medium Speed | <p>Download: 400 mb/s </p><p>Upload: 300 mb/s</p> | 0.4   |
| Low Speed    | <p>Download: 75 mb/s </p><p>Upload: 75 mb/s</p>   | 0.2   |

**CPU scoring system**

| Tier         | Cores  (GB) | Score |
| ------------ | ----------- | ----- |
| Ultra Cores  | >128        | 0.8   |
| High Cores   | 64-128      | 0.6   |
| Medium Cores | 32-64       | 0.4   |
| Low Cores    | <32         | 0.2   |

**Disk scoring system**

| Tier            | Capacity     | Score |
| --------------- | ------------ | ----- |
| Ultra Capacity  | >1024        | 0.8   |
| High Capacity   | 5120 - 10240 | 0.6   |
| Medium Capacity | 512  - 5120  | 0.4   |
| Low Capacity    | <512         | 0.2   |

**Memory scoring system**

| Tier       | Memory    | Score |
| ---------- | --------- | ----- |
| Ultra Mem  | >512      | 0.8   |
| High Mem   | 128 - 512 | 0.6   |
| Medium Mem | 32 - 128  | 0.4   |
| Low Mem    | <32       | 0.2   |

**GPU scoring system**

| Supplier | GPU Model                | Score |
| -------- | ------------------------ | ----- |
| NVIDIA   | GPU\_H100\_80GB\_SXM     | 10    |
| NVIDIA   | GPU\_H100\_80GB\_PCIE    | 10    |
| NVIDIA   | GPU\_A100\_80GB\_PCIE    | 5     |
| NVIDIA   | GPU\_A100\_80GB\_NVLINK  | 5     |
| NVIDIA   | GPU\_RTX\_A6000          | 1.5   |
| NVIDIA   | GPU\_RTX\_A8000          | 1     |
| NVIDIA   | GPU\_RTX\_A5000          | 0.75  |
| NVIDIA   | GPU\_RTX\_A4000          | 0.4   |
| NVIDIA   | GPU\_A40                 | 2     |
| NVIDIA   | GPU\_A10                 | 0.75  |
| NVIDIA   | GPU\_RTX\_4090           | 0.75  |
| NVIDIA   | GPU\_RTX\_4080           | 0.5   |
| NVIDIA   | GPU\_RTX\_4070S\_TI      | 0.25  |
| NVIDIA   | GPU\_RTX\_4070           | 0.25  |
| NVIDIA   | GPU\_RTX\_4060\_TI       | 0.25  |
| NVIDIA   | GPU\_RTX\_3090           | 0.5   |
| NVIDIA   | GPU\_RTX\_3080           | 0.25  |
| NVIDIA   | GPU\_RTX\_3070           | 0.25  |
| NVIDIA   | GPU\_RTX\_3060\_TI       | 0.25  |
| NVIDIA   | GPU\_NVIDIA\_TESLA\_T4   | 0.4   |
| NVIDIA   | GPU\_NVIDIA\_TESLA\_P4   | 0.25  |
| NVIDIA   | GPU\_NVIDIA\_TESLA\_P40  | 0.25  |
| NVIDIA   | GPU\_NVIDIA\_TESLA\_P100 | 0.25  |
| NVIDIA   | GPU\_GTX\_1080           | 0.25  |
| NVIDIA   | GPU\_NVIDIA\_TESLA\_V100 | 0.75  |
