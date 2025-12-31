# Source: https://docs.kaisar.io/kaisar-network/kaisar-architecture/architecture-overview.md

# Architecture Overview

## 1. Overview

### 1.1  Key Components

Kaisar Network mainly comprises of three components:

* **Kaisar Zero Node:** Kaisar’s Chrome extension, enables users to track key metrics like location and uptime while contributing to the decentralized AI compute layer Allowing users to monetize their hardware and support decentralized infrastructure.
* **Kaisar OneNode:** Kaisar OneNode optimizes GPU use for AI through a decentralized, transparent system. With Providers, Checkers, and Explorer on PEAQ Blockchain, ensure performance and reliability.
  * **Kaisar Provider**: Provider offer GPU computing resources and report their status to the PEAQ Blockchain, receiving rewards for their contributions.
  * **Kaisar Checker**: The Kaisar Checker ( Kaisar Checker Node) ensures resource integrity and functionality by performing checks and submitting Proof of Physical Work, earning rewards from the PEAQ Blockchain.
  * **Kaisar Explorer**: An advanced web platform provides real-time visibility into Kaisar’s on-chain metrics and operations for seamless navigation. Kaisar leverages PEAQ Blockchain, a multi-chain layer-one blockchain optimized for DePIN. It supports over 100,000 transactions per second (TPS) with minimal costs and enables seamless interaction with Polkadot, Cosmos, Solana, Binance, and Ethereum via Wormhole.
* **Kaisar Cloud (End-Users):** End-users seek to rent GPUs within the Kaisar Network, directly engaging with the blockchain to access GPU rental, payment processing, and cancellation services.

### 1.2 Kaisar Network Overview

**1.2.1 - Kaisar Cloud&#x20;*****(End-Users)***

* **Order & Payment** : End-users place an order and make a payment for utilizing GPU compute resources.The payment process will require connecting a wallet and completing the transaction through the wallet.
* **Connect Container/Cluster** : After the payment, the end-users are connected to the required container or cluster provided by the Providers.
* **Reporting**: End-users usage of the GPU computing resources is reported to the PEAQ Blockchain.
* **Refund**: If needed, end-users can get refunds via PEAQ Blockchain consensus. The refund is converted into points, which users can then use for discounts or promotions when purchasing new services.

**1.2.2 - Kaisar Provider**

* **Register :** Provider register their computing resources (PC, Laptop, Server, Bare metal with GPU) on the PEAQ Blockchain.When providers register, they will need to connect their wallet and make a payment in order to register a worker. These processes are connected with Peaq.
* **Providing Services to Network:** Providers make their registered resources available to end-users for connection and usage.
* **Report:** Providers report status and usage of their GPU computing resources to the PEAQ Blockchain.
* **Reward:** Providers receive rewards from the PEAQ Blockchain based on the reports.

**1.2.3 - Kaisar Checker**

* **Checking:** Kaisar Checker (Nodes) perform checks on the computing resources provided by the Providers.
* **Proof of Work (PoPW):** After performing checks, Kaisar Checkers provide Proof of Physical Work (PoPW) to the PEAQ Blockchain.The checker will send performance evaluation tasks to the worker, and then update the results on the chain.
* **Report:** Kaisar Checkers report provider findings and the status of the resources to the PEAQ Blockchain.
* **Reward:** Kaisar Checkers receive rewards from the PEAQ Blockchain for their services based on the reports.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FGs0gk4JEGsmkDlfY39i2%2Fkaisar%20ar%20overview.png?alt=media&#x26;token=3edb22f3-1364-4cc8-a393-832dc02ae108" alt=""><figcaption></figcaption></figure>

## 2. Detailted Architecture

### 2.1 Kaisar Process: From Wallet Connection to Container Service Utilization

The Kaisar process covers the entire journey from wallet connection to end-user utilization of the container service. Each step involves specific entities and actions to ensure secure, verified, and efficient deployment and interaction with the service.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FXCUow67O5wygGSYNv653%2Fdetail%20arc.png?alt=media&#x26;token=efa99ab1-2c8d-4a12-91ef-96d98edd15d0" alt=""><figcaption></figcaption></figure>

**2.1.1 - Initiating the Deployment**

1. **Connect to Wallet**

* Entity Involved: End-user
* Action: The end-user connects their wallet to the Console Portal to begin the deployment process.

2. **Buy New Container**

* Entity Involved: End-user
* Action: The end-user purchases a new container through the Console Portal

**2.1.2 - Transaction Handling**

1. **Issue Transaction**

* **Entities Involved:** Console Portal, Blockchain
* **Action:** The Console Portal issues a transaction to the Blockchain to record the purchase.

2. **Transaction Details**

* **Entities Involved**: Blockchain
* **Action:** The Blockchain records the transaction details, ensuring transaction integrity.

**2.1.3 - Port Exposure and Container Deployment**

1. **Request to Expose New Ports**

* **Entities Involved:** Console Portal, VPN
* **Action:** The Console Portal sends a request to the VPN to expose new ports for the container.

2. **Request Results**

* **Entities Involved:** VPN
* **Action:** The VPN processes the request and returns the results to the Console Portal.

3. **Deploy New Container**

* **Entities Involved:** Console Portal, Checkers
* **Action:** The Console Portal commands the Checkers to deploy the container.

4. **Deploy Container**

* **Entities Involved:** Checkers, Worker Node
* **Action:** The Checkers send the deployment command to the Worker Node where the container will be deployed.

**2.1.4 - Notification and Service Connection**

1. **Event Notification**

* **Entities Involved:** End-user
* **Action:** The end-user is notified of the deployment event.

2. **Container Deployment Confirmation**

* **Entities Involved:** End-user
* **Action:** The end-user receives confirmation of the container deployment.

3. **Connect to Container Service**

* **Entities Involved:** End-user
* **Action:** The end-user connects to the newly deployed container service.

**2.1.5 - Service Utilization**

1. **Request to Container Service**

* **Entities Involved:** End-user
* **Action:** The end-user makes requests to the container service.

2. **Request Result**

* **Entities Involved:** Container Service
* **Action:** The container service processes the requests and returns the results to the end-user.

### 2.2 Architecture Layers

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FukDOg8MdETa2kVqVzkCU%2Farc-layer.png?alt=media&#x26;token=f881c24c-e74d-44da-bb98-d351a2878e2a" alt=""><figcaption></figcaption></figure>

***Step-by-Step Flow:***\
\
1\.  Users interact through the Explorer, Kaisar Cloud Portal, or Worker Portal, depending on their role and requirements. -> Explorer is a public site, for viewing the summaries, reports of Network Capacity. Kaisar Cloud Portal is for End User (GPU Consumer). and Worker Portal is for (GPU Provider).

2\. All incoming connections pass through the VPN and Firewall for secure access. The IAM system verifies user credentials and permissions.

3\. Requests are routed to the API Gateway, which is running in a cluster mode to ensure high availability and load balancing.

4.The API Gateway uses a round-robin rule to distribute incoming requests to instances of the Backend( Service Management, Worker Management, Billing, Monitoring & Alert, Logging, and Analytics modules). Each of these modules runs multiple instances to handle the load efficiently.

5\. Depending on the request type, it's processed by the relevant backend service. For instance, compute jobs might be directed to the GPU Cluster through Worker Management.

6\. Some operations, those requiring immutable records or enhanced security, interact with the PEAQ Blockchain.

7\.   After processing, responses are sent back through the API Gateway to the respective frontend interface, providing users with the needed information. -> For asynchronous requests, the Portal will connect to a WebSocket endpoint on the API Gateway. Once the process is completed, the result will be returned to the Portal through WebSocket events.

*Below is the detailed working of the Kaisar Network, organized into architecture layers:*

#### 2.2.1 - Security Layer

The security layer ensures that the network is secure and accessible only by authorized entities.

**Tech Stack:**

* MESH VPN for secure communication
* Firewall for network traffic control
* Authentication Service via Wallet login for user authentication and authorization\
  \
  Here are some features of MESH VPN :

1\. Robustness: The network is highly resilient to individual node failures, thanks to multiple pathways for data transfer.

2\. Scalability: Adding new nodes does not significantly impact the overall network performance.

3\. Low Latency: Direct connections between nodes help minimize the number of transmission steps, reducing delays.

4\. Optimal Load Distribution: Traffic is evenly distributed, avoiding congestion and ensuring optimal performance.

#### 2.2.2 - Backend Layer

The backend layer comprises of core backend services supporting the Kaisar Network operations.

* Providers (GPU Providers) : Offers GPU compute resources as worker Nodes.
* Tech Stack: Docker, Kubernetes
* Cluster / GPU Management: Management of Worker Node Cluster.
* Tech Stack: Kubernetes,&#x20;
* Fault Monitoring: Monitoring for faults using Kaisar Checker Nodes..
* Autoscaling: Automatically adjusting GPU compute resources based on demand.
* Tech Stack: Kubernetes, HPA (Horizontal Pod Autoscaler)

#### 2.2.3 - Infrastructure Layer

**Manages computational resources and task orchestration.**

* GPU Pool: Collection of GPUs available for compute tasks.
* Tech Stack: Nvidia GPUs, CUDA
* List of GPUs is available in GPU Model Scoring Page .
* Orchestration: Tools for managing GPU pools
* Tech Stack: Kubernetes, Docker

#### 2.2.4 - Frontend Layer

* Authentication Service : Manages user authentication and authorization via wallet integration.
* Logging Service: Records system activities on blockchain
* Console Portal: Front end interface for user interaction.

## 3. Core Workflows

### 3.1 - Kaisar Checkers

#### <mark style="color:blue;">Overview</mark>

Kaisar Checkers assesses the uptime, bandwidth, and performance of physical devices provided by Providers within the VPN network. Checkers transmit proof of device functionality to the blockchain and receive rewards based on their performance.

Checker is designed to ensure the integrity and performance of Containers in the Kaisar Network. Verifying the technical specifications of the Containers provided is essential to maintain service quality and network transparency.

**Testing procedure:**

* At registration: A container will be checked when it is registered on the Kaisar Network.
* In standby state: For containers in standby mode, checks will be conducted randomly.
* During rendering state: Service information is collected and examined in detail to evaluate the actual state and quality of the service.

**Evaluation method:**

* Performance parameters: Checker will directly read data about Container performance.
* Simulation testing: Checker will act as a real user to run test applications and analyze received data to ensure the Container is always interactive and complies with set technical requirements.

**Test results:**

* Registration authentication: Checker will confirm the Container's specifications to authenticate the registration of that Container on the Kaisar system.
* Impact on scheduling: Test results directly affect the Manager's scheduling and priority for that Container.
* Quality control: If a certain Container provides services with unsecured quality, Checker will determine the penalty for that Container.

After a Checker Node completes a task, it signs the results with its private key and sends them to Kaisar Blockchain. Each node that delivers the same results as the majority will be rewarded with tokens.

<mark style="color:blue;">**Workflow**</mark>

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FWcw4KFOzaLc7nFFFxmkI%2Fchecker%20work%20flow.png?alt=media&#x26;token=6830203f-c8b4-47eb-82d9-2c7046ebbfbd" alt=""><figcaption></figcaption></figure>

* The Checker initiates the process by connecting to a wallet that holds an NFT license. This license is essential for authenticating the Checker within the Kaisar Network.
* The Checker stakes KAI tokens. Staking KAI is a prerequisite to access Kaisar's resources and services.
* Upon staking KAI, the Kaisar system provides authentication information back to the Checker. This information is used to verify the Checker’s identity and permission to use the network.
* With the authentication information, the Checker connects to the Kaisar VPN. This connection allows the Checker to securely interact with the Kaisar Network.
* Once connected to the VPN, the Checker queries the Kaisar system to check the usage and workload of various Worker Nodes. This step involves retrieving data on how much work each Worker Node is handling and their availability.
* The results of the Worker Node usage and workload check are returned to the Checker. This information helps the Checker decide which Worker Node to use.
* The Checker submits Proof of Physical Work (PoPW) of the selected Worker Node to the Kaisar Blockchain. This submission records the Checker's findings and the performance of the Worker Node on the blockchain.
* After submitting the PoPW, the Checker receives a reward. This reward is an incentive for the Checker to accurately monitor and report on Worker Node performance.

### 3.2 - Kaisar Cloud (End-User) Workflow

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FUYJzyBBo4QMZoy34svud%2Fenduser.png?alt=media&#x26;token=ef012279-7c00-4afa-af94-0bd29f7afa9e" alt=""><figcaption></figcaption></figure>

1. End Users initiates the process by connecting their wallet to the Console Portal of Kaisar to pay for GPU resources.
2. After connecting the wallet, the end-user buys a new container through the Console Portal.
3. The Console Portal issues a transaction that involves multiple Kaisar components like VPN and Blockchain.
4. The VPN processes the transaction details and communicates with the Blockchain.
5. The Blockchain component handles the request to expose new ports to the Proxy/Gateway for accessing the container services.&#x20;
6. The Kaisar Checkers is responsible for deploying the new container. It sends the deployment request to the Provider's Worker Node.
7. The Worker Node in the Provider's infrastructure deploys the container.An event is triggered once the container is deployed, which is communicated back through the Checkers component.
8. The Console Portal updates the end-user with the status: "Container is deploying..." and eventually, "Your Container has been deployed successfully.".
9. Finally the GPU resources are available as Container services by the Providers

* Types of Container Services:&#x20;

&#x20;       \-  Worker Node (Container): Hardware: CPU, RAM, GPU, storage.( By Q2 2024 )

&#x20;       \-  Worker Cluster: Comprises multiple Worker Nodes to allows pooling of resources from multiple  nodes.(Available by Q4 2024)

&#x20;        \-  End users rent resources from mobile nodes provided by Providers.(Available by Q3 2025)

### 3.3 - Kaisar Providers

#### <mark style="color:blue;">Overview</mark>

Providers offer CPU/GPU physical devices for the Kaisar Network, also known as Containers. This is where the actual usage of the cloud takes place, including application execution and rendering. The purpose of Containers is to ensure a seamless experience in the cloud, delivering an optimal user experience.

**Notes on Activities:**

* Availability: Containers must always be in a high state of availability, ready to be activated immediately upon consumer request.
* Usability: Each Container must have the necessary applications or services installed and configured to allow users to access and start up as quickly as possible.
* Processing capacity: Containers need to meet specific computing power and graphics requirements to handle the unique demands of applications or services.
* Network efficiency: Containers must have stable bandwidth and network infrastructure to support high-speed data transmission and low-latency interactions.

**Container Selection Process:**

* Performance-based: Containers are randomly selected based on their ability to provide the highest quality of service with the lowest possible latency and cost.
* Experience optimization: Containers are evaluated for their ability to deliver the best possible user experience, considering factors such as processing speed and uptime.

#### <mark style="color:blue;">Workflow</mark>

*<mark style="color:blue;">Worker Node Provision</mark>*

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FpgDN6aBgEMGKuTKX8pLa%2Fworker%20flow.png?alt=media&#x26;token=85c8b934-1680-4633-b9e1-58f68f29299f" alt=""><figcaption></figcaption></figure>

*Steps:*

1. Provider registers a new worker node.
2. Registration request sent to Kaisar Network.
3. Console Portal responds with setup scripts.
4. Worker node runs setup scripts.
5. Worker node connects to a wallet.
6. Worker node requests a new peer node from blockchain.
7. Connection established.
8. Worker node executes a benchmark job.
9. Benchmark job result sent to Kaisar Network.
10. Worker node registered successfully.
