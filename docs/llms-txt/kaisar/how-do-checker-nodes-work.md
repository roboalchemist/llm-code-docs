# Source: https://docs.kaisar.io/kaisar-network/kaisar-architecture/products/kaisar-onenode/kaisar-checker/what-is-the-kaisar-checker-node/how-do-checker-nodes-work.md

# How do Checker Nodes Work

The Kaisar Checker evaluates the uptime, bandwidth, and performance of physical devices that Providers supply to the VPN network. It sends proof of device functionality to the blockchain and earns rewards based on its performance.

The Checker's primary role is to verify the integrity and performance of Containers in the Kaisar Network. This verification of technical specifications ensures high service quality and network transparency.

#### Testing procedure

* At registration: The Container undergoes verification when registered on the Kaisar Network.
* In standby state: Random checks are performed on idle Containers.
* During rendering state: Detailed service information is collected to assess operational quality and status.

#### Evaluation method

* Performance parameters: The Checker directly monitors Container performance metrics.
* Simulation testing: The Checker simulates user behavior by running test applications, analyzing the data to verify Container responsiveness and compliance with technical requirements.

#### Test results

* Registration authentication: The Checker validates Container specifications during system registration.
* Impact on scheduling: Test outcomes directly influence the Manager's Container prioritization and scheduling.
* Quality control: The Checker assigns penalties to Containers that deliver substandard service quality.

Upon task completion, the Checker Node digitally signs the results with its private key and submits them to the Kaisar Blockchain. Nodes whose results align with the majority receive token rewards.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2Fngfvoi0ih8CraHyMjCmK%2Fimage%20(1).png?alt=media&#x26;token=8f63b338-7688-421f-b2eb-01d88b752a8d" alt=""><figcaption><p>Workflow</p></figcaption></figure>

1. The Checker starts by connecting to a wallet containing an NFT license, which authenticates it within the Kaisar Network.
2. After connecting a wallet, the Kaisar system sends back authentication credentials to verify the Checker's identity and network permissions.
3. Using these credentials, the Checker establishes a secure connection to the Kaisar VPN.
4. Through the VPN, the Checker queries the system for Worker Node status, gathering data about current workloads and availability.
5. The system returns Worker Node status information, helping the Checker determine which node to utilize.
6. The Checker then submits Proof of Physical Work (PoPW) for the chosen Worker Node to the Kaisar Blockchain, documenting its performance assessment.
7. Upon successful PoPW submission, the Checker earns a reward for its accurate monitoring and reporting.

## Banning Scenarios

* A Checker Node will be banned from receiving rewards for one month (no task assignments) if it makes 2 or more incorrect calculations within a week.
* A Checker Node will be banned from receiving rewards for six months (no task assignments) if it makes 5 or more incorrect calculations within a month.
* A Checker Node will be permanently banned and lose its Checker qualification if its total incorrect calculations exceed 10.

## Checker Node Status

Checker Nodes operate in one of five statuses. Each status reflects the node's current operational state, which is essential for effective management and troubleshooting within the Kaisar Network.

* **Checking**: Actively performing verification tasks.
* **Ready**: Prepared to receive new tasks, but not currently checking.
* **Offline**: Not operational due to network issues or maintenance.
* **Banned**: Disqualified from earning rewards due to repeated failures or policy violations.
* **Pending**: Awaiting approval for delegation.
