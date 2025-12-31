# Kaisar Documentation

Source: https://docs.kaisar.io/llms-full.txt

---

# Overview & Mission

Kaisar is a decentralized GPU network designed to provide unlimited computing power to machine learning (ML) and AI applications.&#x20;

Our mission is to make computing scalable, accessible, and efficient by leveraging underutilized GPU resources from independent data centers, crypto miners, and consumer households. We aim to assemble over a million GPUs from these diverse sources to create a robust and decentralized computing infrastructure.

\\


# Challenges


# Exponential Change in Spending and Compute Requirements

According to [GlobalTechCouncil](https://www.globaltechcouncil.org/artificial-intelligence/global-spending-on-ai-expected-to-double-in-four-years/), global spending on AI-centric systems is forecast to reach $154 billion in 2023 and is expected to continue growing rapidly, driven by increasing investments in AI by various industries such as banking, retail, and professional services.

Key areas of AI hardware spending include GPUs, TPUs, and custom AI chips. The broader IT spending landscape also highlights significant growth in data center systems, with spending projected to increase from $237 billion in 2023 to $260 billion in 2024. This growth is part of a broader trend of increasing investment in software, IT services, and communications services driven by the adoption of AI and other emerging technologies (Source: [Splunk](https://www.splunk.com/en_us/blog/learn/it-tech-spending.html)).

To gain insights into projected hardware use by AI Systems, [Stanford AI Index Report 2024](https://aiindex.stanford.edu/report/)) highlights the economic impact of AI, showing a significant increase in the use of training compute for notable machine learning models&#x20;

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXe_u0jdzSPhsoYrW8F2EZZvLp8euaPE7MIptNAaJrB6HXLqOB-94pttYH5_fx5KsKaf7hmfKVk-twi3IsWiWLx_th5XPsJSLkSwHNVOK7vxxoXBqJhC4OEz88s8wd8F-G9SUs0JNcyXSysaBBayg0gUzn0?key=UbI8YI3-VF8UhldN54mDkg" alt=""><figcaption></figcaption></figure>

\\


# Cost challenges with traditional cloud GPU providers.

The cost challenges associated with cloud GPU providers is highlighted by [Splunk](https://www.splunk.com/en_us/blog/learn/cloud-cost-trends.html) where the demand for GPUs, especially for training large AI models, has surged, leading to capacity constraints. Instances where multiple users require a large number of GPUs simultaneously can lead to contention and underutilization, driving up costs as cloud providers struggle to balance supply and demand efficiently.&#x20;

Other prominent reasons for cost challenges are:&#x20;

* Hidden costs such as egress fees also contribute significantly to the overall expense, often catching businesses by surprise (Source:[Splunk](https://www.splunk.com/en_us/blog/learn/cloud-cost-trends.html)).
* The methods for deploying GPU resources in the cloud, such as pass-through can be wasteful for smaller applications. GPU virtualization.(Source: [SpringerLink](https://link.springer.com/article/10.1007/s00170-023-11252-0)).
* Use of advanced technologies in AI models has introduced new costs in compute. While these technologies improve the performance of AI models they still require significant investment in infrastructure.(Source: [ar5iv](https://ar5iv.org/pdf/2401.12230)).

The plot from [ar5iv](https://ar5iv.org/pdf/2401.12230) below shows how the number of GPUs provisioned scales with the fluctuating request rate over time. As the request rate increases or decreases, the number of GPUs provisioned also adjusts accordingly to match the demand, demonstrating elastic resource scheduling.

<figure><img src="https://lh7-rt.googleusercontent.com/docsz/AD_4nXeWBvB1Z0HKEyiofCTEeU2sYs-GC2YhP8kmtrg9yX4b8vhzzm5Yy05pP_eNX5m--y4O9qLtRFCcN2W_9Dn1LX2TDVWFJ63cNz1ApKg21x3Dw8AXEhjhr950i4XQwoGgomA3q0KHKDneCfOPrbXoMzewNtfd?key=UbI8YI3-VF8UhldN54mDkg" alt=""><figcaption></figcaption></figure>


# Centralized GPU Computing Challenges

The compute challenges associated with centralized cloud GPU providers are plenty. Below are some statements from prominent publications:

* As demand for GPU compute grows, scaling centralized infrastructure can be challenging. According to Gartner, "GPU-accelerated computing is becoming more prevalent, but scaling GPU resources efficiently remains complex."(Source: Gartner, "Disaggregate Compute and Storage to Enable Scalable, Flexible, and Cost-Effective Data Centers" (2020))
* High-performance GPUs are expensive, and centralizing them can lead to significant upfront costs. A Springer publication notes that "the capital expenditure for large GPU clusters can be prohibitive for many organizations."(Source: Springer, "A Survey on GPU-Based Cloud Computing" (2019))
* GPUs consume substantial power and generate significant heat. Centralizing many GPUs intensifies these challenges. Gartner highlights that "power and cooling requirements for dense GPU deployments are a major consideration in data center design."(Source: Gartner, "Data Center Infrastructure Planning Tool" (2020))
* Network latency: For some applications, network latency between centralized GPUs and distributed data sources can be problematic. Gartner points out that "data locality and network performance are critical factors in GPU-accelerated computing architectures."(Source: Gartner, "Best Practices for Building a Scalable Data Science Platform" (2020))
* Centralized GPU computing requires specialized software stacks and tools. Gartner notes that "the rapidly evolving GPU software ecosystem can create integration and compatibility challenges."(Source: Gartner, "Magic Quadrant for High-Performance Computing" (2020))


# Building the Kaisar Network

At Kaisar Network we are focused on developing a slew of innovative tools that mitigate the challenges above.&#x20;

Our network intelligently aggregates and redistributes new and idle GPUs from enterprises, data centers, cryptocurrency mining operations, and single vendors. This emerging approach, called Decentralized Physical Infrastructure Network (DePIN), is poised to disrupt traditional business practices.

This decentralized network enables easy comparison, selection, and utilization of GPUs, for consolidating geographically dispersed resources to handle large-scale AI workloads.&#x20;

Kaisar's approach will reduce global dependence on centralized cloud providers and pave the way for a more efficient and connected global GPU cloud economy.

For more information on Kaisar solutions please check the Problem Statement/Solution page.

\\


# Problem Statement

The escalating demand for GPU computing power, driven by the increasing complexity and volume of AI/ML workloads, presents significant challenges for organizations. Major cloud providers impose complex permission models, long-term contracts, and high costs, making it difficult to quickly scale capacity to meet demand. This gap is expected to widen as the need for GPU computing continues to grow, necessitating a 2-3-fold increase in cloud GPU capacity in the near future.

Meanwhile, a substantial portion of global GPU capacity remains underutilized:

* Independent Data Centers: The average server utilization rate in US data centers was around 18% in 2019, indicating a significant amount of idle capacity (Source: DatacenterDynamics, 2019).
* Crypto Miners: The Ethereum transition has left many crypto miners with idle GPUs, resulting in a surplus of mining hardware (Source: TechSpot, 2022).
* Consumer GPUs: Many consumers use their GPUs for low-intensity tasks, leaving a significant portion of GPU capacity underutilized (Source: Tom's Hardware, 2020).

To address this imbalance, there is a critical need for solutions that can efficiently leverage this underutilized GPU capacity, integrating it seamlessly into existing workflows and meeting the surging demand for compute power without the prohibitive costs and constraints imposed by major cloud providers.

\\

\\


# The Solution: Kaisar's Decentralized GPU Network

Kaisar addresses the problem statement by creating a decentralized network of GPUs sourced from independent data centers, crypto miners, and consumer households. Kaisar enables you to do the following:

1. **Cost Efficiency:** By leveraging underutilized GPUs, Kaisar can offer computing power at a lower price than traditional cloud providers.
2. **Speed:** Users can access GPU supply and deploy clusters in seconds, compared to the weeks-long process required by traditional providers.
3. **Flexibility and Control:**  Kaisar provides users with exceptional flexibility and control over their GPU allocations based on specific project needs.


# Kaisar's Competitive Edge

* Kaisar offers a fundamentally different approach to cloud computing. We leverage a distributed and decentralized model that provides increased control and flexibility for users. Kaisar's services don't involve complicated permission models and are cost-efficient. The combination of all these factors sets Kaisar in its own league of decentralized providers.
* Kaisar is a GPU DePIN, or Decentralized Physical Infrastructure Network that leverages blockchains, IoT, and the greater Web3 ecosystem to create, operate, and maintain real-world physical infrastructure. These networks use token incentives to coordinate, reward, and safeguard members of the network.

Kaisar leverages [the peaq blockchain](https://www.peaq.network/), a multi-chain layer one blockchain specifically designed and optimized for DePIN. The network can scale beyond 100,000 transactions per second (TPS) (pending upgrade) while maintaining a minimal transaction cost of approximately $0.00025


# Technical Specifications

* Kaisar utilizes peaq Blockchain which boasts the most environmentally friendly blockchain architecture and boasts the second-largest developer ecosystem in Web3.&#x20;
* Blockchain technology allows for a clear record of data origin, processing, and ownership, enabling the tracking of data lineage and provenance, which is crucial in AI/ML applications where data quality and integrity are paramount.
* Peaq's blockchain enables decentralized AI/ML model training while allowing for a more distributed and collaborative approach to AI development.
* Peaq's sharded architecture allows for parallel processing of AI/ML tasks across multiple nodes, reducing training times and increasing the overall efficiency of the AI computing tasks.
* Kaisar connects a global network of customers to GPU providers. Our network facilitates the seamless exchange of computational resources through smart contracts. Customers can request compute clusters tailored to their specific requirements, paying with KAI tokens. Providers, on the other hand, can share their underutilized processors and earn rewards through our platform.
* With Kaisar, customers can choose a list of GPU providers/containers with unmatched flexibility, a list of randomly selected GPU containers is rendered to the customer based on their ability to provide the highest quality of service with the lowest possible latency and cost.
* GPU providers are evaluated for their ability to deliver the best possible user experience, considering factors such as processing speed and uptime.
* Kaisar offers a wide range of GPU rig rentals including the NVIDIA RTX series and AMD Ryzen series to join as GPU providers/containers for providing services to customers (Coming Soon).
* Kaisar automatically detects risks and blocks unauthorized GPU containers. Operating in a multi-tenant environment Kaisar ensures that your data remains highly secure and inaccessible to other clients. For highly sensitive workloads, we recommend our Secure Cloud option that complies with industry standards and regulations and meets your high security and privacy demands.
* Kaisar leverages an innovative concept of Proof: Proof of Physical Work (PoPW). This provides a token distribution mechanism that rewards participants of Kaisar Network for completing verifiable physical work in the real world. PoPW utilizes checkers that verify GPU Providers' device info, uptime, and performance. The work done by GPU Providers is submitted as proof which is validated and submitted to the blockchain. At the end, the blockchain calculates and distributes rewards to GPU Providers based on scores.
* From the start of the GPU rental period until the reward distribution, the GPUs are always committed to the AI/ML jobs. The containers are monitored in real time to eliminate GPU processes that do not comply with the concept of Proof.


# FAQ

In this section you will find answer to all general questions related to Kaisar Network


# What is Kaisar?

Kaisar is a Decentralized Physical Infrastructure Network (DePIN) optimized for decentralized computing and AI. It aggregates spare GPU resources using AI and blockchain, offering scalable, secure, and cost-efficient cloud computing services.


# Does Kaisar use blockchain technology?

Kaisar operates on the peaq blockchain, which is optimized for Decentralized Physical Infrastructure Networks. The peaq blockchain supports scalable, decentralized AI/ML model training and provides a secure, cost-effective environment for managing GPU resources.

\\


# What are the main products offered by Kaisar?

Kaisar offers several key products designed for high-performance computing and AI applications:

* **Kaisar GPU Container:** Encapsulates GPU workloads in containers for efficient GPU resource utilization.
* **Kaisar Ray Node & Ray Cluster:** Tools for managing and scaling Ray clusters, enabling distributed AI/ML tasks.
* **Kaisar K8s:** A fully managed Kubernetes service tailored for GPU container deployment.
* **Kaisar Worker:** Allows users to contribute their GPU resources to the Kaisar network and earn rewards.


# Can I contribute my GPU resources to Kaisar?

Yes, Kaisar Worker allows users to contribute their GPUs to the network. Whether you have a PC, laptop, or server with GPUs, you can join the network and earn rewards for your contributions


# What is Proof of Physical Work (PoPW)?

Proof of Physical Work (PoPW) is a token distribution mechanism used by Kaisar to reward GPU providers for completing verifiable physical work in the real world. It involves validating the performance, uptime, and device info of GPU providers through checkers, with rewards distributed based on these scores.


# How does Kaisar GPU Container work?

* Kaisar GPU Container allows users to run GPU-intensive applications within containers, providing easy access to GPU resources.&#x20;
* Users can customize their container environments, monitor GPU usage in real-time, and manage their deployments through a user-friendly dashboard.&#x20;
* The service supports popular AI/ML frameworks like TensorFlow and PyTorch.


# What frameworks are supported by Kaisar GPU Container?

Kaisar GPU Container supports several major frameworks, including:

* TensorFlow
* PyTorch
* Jupyter Notebook
* Stable Diffusion
* NVIDIA CUDA
* Visual Studio Code

These frameworks can be deployed using pre-built templates provided in the Kaisar portal.

\\


# How do I deploy a GPU Container?

To deploy a GPU container follow step-by-step instructions from the Guides section. Here is an overview of 5 step Deployment process.

1. Log in/Signup to the Kaisar portal.
2. Select a pre-built template from GPU frameworks.
3. Set Parameters.
4. Choose a pricing model (e.g., on-demand, 1 month, 3 months).
5. Review and finalize the deployment details, then proceed with payment.


# What payment methods are accepted?

Kaisar accepts payments via USDT (Tether), and will soon support credit card payments for purchase of KAI tokens to use in Kaisar Decentralized Physical Infrastructure Network (DePIN).

\\


# How is pricing determined?

Pricing is based on the selected GPU model, the duration of use, and the pricing plan (on-demand, monthly, etc.).

\\


# What GPUs are supported?

Kaisar supports a range of GPUs, including the NVIDIA RTX series and AMD Ryzen series.

\\


# How do I monitor my GPU container?

You can monitor your GPU container from the dashboard, which displays metrics such as CPU, memory, network usage, and more.

\\


# How does Kaisar ensure security of containers?

* Kaisar uses multiple layers of security, including robust access control and a secure cloud option for highly sensitive workloads.&#x20;
* Kaisar transactions are facilitated through smart contracts on the peaq blockchain. Customers pay for compute clusters using KAI tokens, and providers receive rewards based on their GPU contributions.

\\


# How do I get started with Kaisar?

To get started, create an account on the [Kaisar portal](http://cloud.kaisar.io), log in, and explore the dashboard. You can deploy GPU containers, manage your account settings, and monitor your resources through the portal.

\\


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


# Products


# Kaisar ZeroNode

## 1. What is Kaisar ZeroNode

Kaisar is a DePIN protocol uniting global GPU and CPU resources into a universal AI compute layer. It enables individuals to connect devices, earn rewards, and access decentralized infrastructure, offering AI developers and businesses a scalable, affordable alternative to traditional cloud services.

ZeroNode, Kaisar’s Chrome extension, empowers users to contribute to this next-gen computing layer by tracking key metrics like location and uptime. Your participation supports the upcoming launch of the worker node (Kaisar OneNode), allowing you to further monetize your hardware and drive the shift toward decentralized infrastructure.

## 2. ZeroNode Rewards

ZeroNode rewards are derived from four key components:

### 2.1. Running a ZeroNode

Rewards for running a ZeroNode are tied to its uptime—the time your node is online and operational. You can earn up to **300 points daily** for maintaining 24 hours of uptime, incentivizing consistent participation and ensuring network reliability.

**Kaisar NFT holders** enjoy a significant advantage: owning a Kaisar NFT doubles your earnings. For example, if your node earns 300 points daily, NFT holders will earn **600 points**, highlighting their integral role in the Kaisar ecosystem.

[**Download the ZeroNode extension now**](https://chromewebstore.google.com/detail/kaisar-zeronode/mmlnljdcfjnfeikeioghbkobdcmnhgko) to start earning rewards and contributing to the decentralized future!

### 2.2. Referrals

Both the referrer and the referee receive one ticket when you invite a new member to the network. Additionally, the referrer earns an extra 10% reward from the earnings of their referrals. Tickets earned from referrals can be used to participate in lucky draws.

Please note that the referrer will only receive the bonus once the referee’s node has been running for 6 consecutive hours.

### 2.3. Missions

A wide array of missions will be introduced upon launch, and we’ll continue to roll out new challenges weekly, ranging from easy to difficult.&#x20;

To kick things off, we’ll offer tasks such as completing daily check-ins and engaging in various social activities to earn additional points. Your rewards for daily check-ins will grow with each consecutive day of check-in, culminating in a maximum payout on the seventh day. The cycle then repeats.

We’ll unveil more missions in the future, so be sure to follow Kaisar closely for the latest updates.

### 2.4. Lucky Draw

Our innovative Lucky Draw feature sets us apart, offering you a unique opportunity to win exciting rewards. To participate, simply collect tickets. Here are the primary ways to acquire tickets:

* **Referrals:** Invite your friends and earn tickets for each successful referral. The more referrals you make, the more tickets you’ll receive.
* **Points Burning:** Burn 300 points from your active ZeroNode to receive a ticket. You can burn unlimited points to get as many tickets as possible.&#x20;
* **Campaign Participation:** Keep an eye out for our ongoing campaigns and giveaways, where you can earn tickets by completing specific tasks.
* **Future Initiatives:** As we continue to evolve, we may introduce additional ways to earn tickets, such as through limited-time events or community challenges.

The rewards and mechanics of our Lucky Draw are subject to change, ensuring that there are always fresh and exciting opportunities for our community.

## 3. Empowering the Future of advanced and decentralized AI

Kaisar envisions a future where individuals can reclaim control over their computing resources, breaking free from centralized monopolies that have dominated the infrastructure landscape. By participating in the Kaisar ecosystem, you are not only contributing to a more equitable distribution of computing power but also helping to shape the future of decentralized AI.&#x20;


# Kaisar OneNode

**Kaisar OneNode** is a decentralized infrastructure that optimizes GPU resource use through a trustless, transparent system, ensuring efficient allocation, secure validation, and fair rewards, built on the PEAQ Blockchain.

* **Network Integrity**: Providers supply GPU power while Checkers validate their contributions, with status updates and audits maintaining reliability in a scalable ecosystem.
* **Explorer Platform**: Explorer, an advanced web platform, provides real-time visibility into Kaisar OneNode’s operations for seamless navigation.
* **Key Insights**:
  * Track network earnings, connected providers/checkers, and available resources.
  * Access details on GPU power, CPU cores, memory, and capacity.
  * Monitor provider and checker activity live for oversight.
* **Synergy**: Kaisar OneNode deliver a robust, transparent computing network with actionable insights for efficiency and growth.


# Kaisar Provider


# What is Kaisar Provider


# Introduction

As a Kaisar Provider on Kaisar Network, you contribute to supporting and expanding the network, ensuring businesses and developers have reliable access to the computational power they need to run their workloads seamlessly and efficiently.

1. **Provide GPU Power** – Connect your GPU servers to Kaisar Network, making them available for businesses and developers who require high-performance computing for their workloads.
2. **Ensure Performance** – Provide your GPUs to support network reliability and security. Regularly monitor server performance to meet operational standards, prevent downtime, and ensure a smooth and efficient computing experience for users.
3. **Manage & Earn** – Track your earnings from providing GPU resources, manage your servers efficiently, and oversee financial transactions with security. Use the platform’s tools to monitor service fees, claim rewards, and ensure smooth and transparent financial operations.

Your contribution helps power a reliable and efficient cloud ecosystem.\\


# Benefits of Running a Kaisar Provider

**Operating as a Kaisar Provider: Empowering a Distributed Cloud Network**\
Running a Kaisar Provider offers a unique opportunity to contribute to a state-of-the-art distributed cloud network that powers artificial intelligence (AI) and advanced computational workloads. Below are the key benefits of becoming a Kaisar Provider (Worker Node Operator):

1. **Financial Rewards**\
   Earn substantial revenue by providing GPU computing power to businesses and developers who require scalable infrastructure for AI, machine learning, and other resource-intensive applications.
2. **Scalable and Flexible Operations**\
   Effortlessly expand your resource pool by integrating additional nodes as demand increases, enabling you to enhance both your earnings and your impact within the network.
3. **Secure and Decentralized Ecosystem**\
   Participate in a transparent and secure framework where your contributions are safeguarded, and compensation is equitably distributed across the network.
4. **Sustainable Computing Infrastructure**\
   Support a shift away from large, centralized data centers, contributing to a more energy-efficient and environmentally responsible cloud computing ecosystem.
5. [Kaisar Provider Rewards Mechanism](https://docs.kaisar.io/kaisar-network/kaisar-rewards-mechanism/rewards-for-kaisar-providers)

These core advantages underscore the value of participation, delivering both operational and societal impact in a concise and compelling manner.


# How to Manage Kaisar Provider


# Get started

**Step 1:** Go to [Kaisar Explorer](https://onenode.kaisar.io/explorer) and click on "Provider".

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2Fhy0MbLzEvBHtZWDGVpPg%2Fimage.png?alt=media&#x26;token=ce2034eb-8bfa-4e6e-bdd4-4d8f34be994e" alt=""><figcaption></figcaption></figure>

**Step 2:** Browse the list of Providers and choose one to stake with.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FEkMLzO7yki8mkMY78Lhz%2Fimage.png?alt=media&#x26;token=e2eb7d8e-0c89-40fe-ab3c-34384d6c0506" alt=""><figcaption></figcaption></figure>

**Step 3:** Click on any Providers to view detailed information.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FxJdzbstT9uK9ym0OYpAv%2Fscreencapture-stg-explorer-kaisar-io-provider-0xF3AF26527b14769f23d9B0a23B6437Ac1EA57091-2025-05-19-08_55_24.png?alt=media&#x26;token=b5d1c7af-9774-4a3a-8e7e-61ab39564b79" alt=""><figcaption></figcaption></figure>


# Connect wallet

1. **Connect Wallet**: Click the **"Connect Wallet"** button on the interface.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FcP4kH5Fq4Uesjyim1JTL%2Fimage.png?alt=media&#x26;token=f0d62962-50b0-4248-ab82-ed5a515a38c8" alt=""><figcaption></figcaption></figure>

2. **Select Wallet:** Choose your preferred wallet and connect to it.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2Fuar0LcUsYmq0umE5BmcH%2Fimage.png?alt=media&#x26;token=c22a7091-a435-497a-8234-e34f35567cda" alt=""><figcaption></figcaption></figure>

3. **Sign In:** Click the **"Sign In"** button to confirm and complete the login process with your wallet.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FTvHkeuloLsqhfXr5O4pH%2Fimage.png?alt=media&#x26;token=6edc96d9-e5bf-4285-89ca-5afe94bf7f84" alt=""><figcaption></figcaption></figure>


# How to run Kaisar Provider App


# Linux CLI

## Kaisar Provider CLI Installation Guide for Contributing to Kaisar Network

### Requirements

To run the Kaisar Provider, ensure your system meets the following specifications:

* **Operating System:** Ubuntu 20.04+, CentOS 8+, or compatible 64-bit Linux distribution
* **Memory:** 4GB RAM
* **Processor:** 64-bit CPU with virtualization support
* **Storage:** 100GB HDD/SSD
* **Internet Speed:** 100Mbps or higher

### Dependencies

The following packages and libraries are required (the setup script will install them automatically if missing):

* Node.js (v18 or higher recommended)
* npm
* pm2
* curl
* tar
* git (for some operations)

***

### 1. Download the Setup Script

Download the latest setup script from the Kaisar releases repository:

```bash
curl -O https://raw.githubusercontent.com/Kaisar-Network/kaisar-releases/main/kaisar-provider-setup.sh
```

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FmRalOMd4ABB3DCtiTodx%2Fimage.png?alt=media&#x26;token=48ac7d6c-5b48-46d4-a339-b7d031115f90" alt=""><figcaption></figcaption></figure>

***

### 2. Make the Script Executable

```bash
chmod +x kaisar-provider-setup.sh
```

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FWh7n6ngqPo96z0vtCpHZ%2Fimage.png?alt=media&#x26;token=56b868a3-3081-4a6b-89a9-f2d408627cf8" alt=""><figcaption></figcaption></figure>

***

### 3. Run the Setup Script with Root Privileges

```bash
sudo ./kaisar-provider-setup.sh
```

The script will automatically:

* Install Node.js, npm, and pm2 if not already present
* Download the latest release of Kaisar Provider CLI
* Install all required dependencies
* Set up the CLI globally on your system

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FiyKf5BbOng6vJwoxhdrh%2Fimage.png?alt=media&#x26;token=e2ae222a-eecc-45aa-8c5a-7871ee42d66c" alt=""><figcaption></figcaption></figure>

***

### 4. Verify the Installation

After installation, verify by running:

```bash
kaisar
```

If you see a welcome message, the installation was successful!

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2F3JW12CaGbfzEEN5Sc93y%2Fimage.png?alt=media&#x26;token=d5cb4a62-639e-47c8-a793-7c12c2e3b0e9" alt=""><figcaption><p>kaisar command result</p></figcaption></figure>

***

### 5. Start Using the CLI

You can now join the network with the following commands:

```bash
kaisar start          # Start the Provider App
kaisar create-wallet -e <your email> # Create Wallet
kaisar import-wallet -e <your email> -k <your private key> # Import your existed wallet
kaisar status         # Check node status
kaisar log            # Check details log of Provider App
```

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FAIsx8sRSdgk6lmz2BREE%2Fimage.png?alt=media&#x26;token=b519c04d-b7b3-44fd-9c2c-b500ad83f885" alt=""><figcaption></figcaption></figure>

***

**Notes:**

* Wallet and configuration data are stored in `/var/lib/kaisar-provider-cli`, so your data will not be lost when updating to a new version.
* To earn rewards, follow the instructions to create a wallet and connect your account to the Kaisar Network.

***

Good luck and enjoy earning rewards with Kaisar Network!


# MacOS & Windows GUI

Follow these steps to set up the Kaisar Provider application on your system and start operating as a Kaisar Provider Node.

### 1. Download and Install

Download and install Kaisar Provider app from link below base on your OS (operating system)

* MacOS for Apple Silicon (M1, M2, M3): [Download here](https://drive.usercontent.google.com/download?id=1Ljcgd60HlXcQQ555hfq5KrUqEtUZDLcV\&export=download\&authuser=0\&confirm=t\&uuid=0dc925d1-371b-44e3-8c44-f132133cce4c\&at=AN8xHorpw6X_hRKxZWWYp9576mu1:1754592127732)
* MacOS for Intel-based Macs: [Download here](https://drive.usercontent.google.com/download?id=1myQNB9wCIN3rw-_wy91_Q1m7IySRc0De\&export=download\&authuser=0\&confirm=t\&uuid=710b7751-bd90-436b-885e-87b330d916fd\&at=AN8xHoq-q42nEhORRugwcgBPEhwE:1754592137742)
* Windows version: [Download here](https://drive.usercontent.google.com/download?id=1gsnJ3eKsirqEPRE5bshT6J4rJOmG4QH9\&export=download\&authuser=0\&confirm=t\&uuid=45191f6e-bdfe-4927-b8f1-9c14b9b185ed\&at=AN8xHorpYIrYc_s2dOSoxBTcSHTC:1754592241608)

**Installing Docker (Optional)**

To support development or deployment tasks, you may need to install Docker. Follow the steps below based on your operating system:

* **For MacOS (Apple Silicon or Intel-based Macs)**: [Docker Desktop for Mac installation](https://docs.docker.com/desktop/install/mac-install/).
* **For Windows**: [Docker Desktop for Windows installation](https://docs.docker.com/desktop/install/windows-install/).

### 2. Create or import an existing wallet

* Create a new wallet or import a wallet by click on button **"Create"** or **"Import Wallet"**&#x20;

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FPm2UExGRSm7soZhH5lcF%2Fimage.png?alt=media&#x26;token=bf0c93bf-d0b8-4d71-ad96-c07a810bc7eb" alt=""><figcaption></figcaption></figure>

#### &#x20;Create a New Wallet

1. Enter your email address.
2. Set a secure wallet password.
3. Click **"Create Wallet"** to generate a new wallet.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FpKrueCqe7XS4Ed0bdYGN%2Fimage.png?alt=media&#x26;token=35c00454-4d35-455f-af17-388e31686777" alt=""><figcaption></figcaption></figure>

* In the app, click **"Create Smart Account"** to initialize your smart account.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2Fm5lJAMinkUdeKVeJ3DeS%2Fimage.png?alt=media&#x26;token=115bbfac-d52f-4be7-9cbf-c94ec07b0624" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FrQKEcA9mxKm4QVBPywxE%2Fkaisarprovider2png.png?alt=media&#x26;token=f05211f9-dece-449b-beb5-e425850ebce3" alt=""><figcaption></figcaption></figure>

If the registration fails, click **"Retry"** to attempt again, or select **"Create Smart Account"** to start over.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FN4O5mU1vDxEXkIwGzvZZ%2Fkaisarprovider3.png?alt=media&#x26;token=7bffc9ef-5eb3-45c4-b6fa-a5aa4cbe6ff7" alt=""><figcaption></figcaption></figure>

* Once successful, click **"Complete"** to finalize the device registration.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FqOkTl9GmC4Hp6Fq9tAtU%2Fkaisarprovider4.png?alt=media&#x26;token=ddc7f0a7-b34f-4d5d-bc93-5c21d3b44c29" alt=""><figcaption></figcaption></figure>

#### Import an Existing Wallet

1. Follow the prompts to import your existing wallet using your recovery phrase or private key.
2. Enter your email address
3. Set a secure wallet password
4. Click **"Import Wallet"** to import your wallet

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2F1CkrBlDBJfFviIENlVmz%2Fimportwallet.png?alt=media&#x26;token=a388512d-c0aa-4aaa-866d-c2a942dc0381" alt=""><figcaption></figcaption></figure>

* Congratulations! Your Kaisar Provider Node is now registered and ready to operate.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FmP92WvRQsVg0lwyKaWow%2FkaisarProvider5.png?alt=media&#x26;token=f0e16350-23c9-4139-8fcf-6405ca47f23e" alt=""><figcaption></figcaption></figure>

### 3. Access Wallet Management

1. Open the **Kaisar Provider** application.
2. On the main interface, look at the top right corner where your wallet address is displayed.
3. Click on the wallet address to open the options menu. The menu will show two options:

   * **Export Private Key**
   * **Disconnect Wallet**

   <figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2F7QtXULyzdgrGrysJTdEQ%2Fimage.png?alt=media&#x26;token=f09a0b34-6d4a-49cb-9649-106362ccc029" alt=""><figcaption></figcaption></figure>

### 4.  Export Private Key

1. In the options menu, select **Export Private Key**.
2. A window titled **"Export Private Key"** will appear, prompting you to enter your password:
   * Enter your wallet password in the **Password** field.
   * Click the eye icon (if needed) to reveal the entered password.
3. Click **Export** to proceed.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2F8BgH98cWEHLZVJGb3mqM%2FScreenshot%202025-05-16%20110830.png?alt=media&#x26;token=556c0789-f941-43de-8456-8f0133c699ea" alt=""><figcaption></figcaption></figure>

If the password is correct, a new window will display your private key\
\&#xNAN;**"Keep your private key secure. Do not share or reveal it to anyone."**

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FKgAPwu81s6fG82yDiPHg%2Fkaisarprivatekey.png?alt=media&#x26;token=3fa79dc9-8d7f-4426-bde4-e769d04c1a3f" alt=""><figcaption></figcaption></figure>

4. Click **Copy** to copy the private key to your clipboard, then store it securely.
5. Click **Close** to exit the window.

**Note:** The private key is highly sensitive information. Losing it or exposing it could result in loss of access to your wallet and its assets.

### 5. Remove Wallet (Disconnect Wallet)

1. In the options menu, select **Disconnect Wallet**.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FsaNX3HBVyWffW00KavvS%2Fimage.png?alt=media&#x26;token=35c553d8-b924-40f2-b94a-e857e7bdd643" alt=""><figcaption></figcaption></figure>

2. A window titled **"Remove Wallet"** will appear with a warning:\
   \&#xNAN;**"Warning: This action will remove your wallet and all associated data. This action cannot be undone."**
3. Enter your wallet password in the **Confirm Password** field.
4. Click the **Remove Wallet** button (in red) to confirm wallet removal.

   If you change your mind, click **Cancel** to abort the action.

<div data-full-width="false"><figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FT8y0BhNWnY9okvyzug7k%2Fimage.png?alt=media&#x26;token=e9ad344d-32c8-460c-abf6-2d2ff509dfaf" alt=""><figcaption></figcaption></figure></div>


# Kaisar Checker


# What is the Kaisar Checker Node


# Introduction

The Kaisar Network is a decentralized infrastructure ecosystem, delivering a robust foundation for decentralized computing.\
As a Kaisar Checker Node operator on the Kaisar Network, you contribute to maintaining the network’s reliability, ensuring resources function seamlessly by verifying their integrity and performance for users across the ecosystem.

* **Verify Resources** – Operate your Checker Node to conduct thorough checks on GPU resources, submitting Proof of Physical Work to validate their functionality and uphold network standards.
* **Ensure Reliability** – Support network stability by monitoring resource performance, preventing failures, and ensuring a consistent, efficient experience for all users relying on the system.
* **Manage & Earn** – Track your rewards earned from the PEAQ Blockchain, manage your node operations efficiently, and utilize platform tools to oversee performance, claim incentives, and maintain transparent operations.\
  Your contribution as a Checker Node operator helps power a dependable and efficient decentralized network.


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


# Benefits of Owning a Checker Node

Owning a Checker Node offers several key advantages:

* **Rewards**: Earn regular incentives by contributing to network verification.
* **Empowerment**: Help decentralize AI infrastructure and create alternatives to traditional tech monopolies.
* **Community Impact**: Drive the growth of the Kaisar ecosystem while supporting global AI innovation.


# Node Sale Information

## **1. Checker Node Overview**

&#x20; **Kaisar Checker Node General Information**

* Total supply: 29998 KaiNodes
* Total reward pool for Checker Nodes: 20% of total supply
* Round 1 price: 0,208 ETH ( Fund Commitment Phase)
* Round 2 price: 0,26 ETH ( Public Node Sale)
* **Node sale platform:** [**nodes.kaisar.io**](http://nodes.kaisar.io)

Early purchasers from Phase 1: Fund Commitment Phase will receive:

* Reward Pool: 10 million $KAI (for Round 1 only)
* Daily Reward: 17 $KAI (per node) - up to 510 $KAI per node during the Round 1\*

*\*This is a special BONUS daily reward exclusively for early purchasers. It will be available for 30 days starting from the launch of the Phase 1 sale. The earlier you purchase, the more $KAI rewards you will receive during the commitment phase.*

## **2. Sale Mechanism**

The Kaisar Checker Node Sale is divided into two parts: Fund Commitment and Node Sale.

#### **2.1 Fund Commitment Phase (1 month)**

* Participants deposit funds as a commitment to purchase Checker Nodes, positioning themselves as early purchasers and gaining the following benefits:
* Whitelists:
  * **20% Discount**: Commit early to secure a 20% discount on your Node purchase (ensure you're whitelisted or buying through a referral link)
  * **Referral Link**: Receive a referral link to earn a 10% commission fee on referred purchase volumes.
  * **Referral Link Activation**: Buy at least one node to activate your referral link.
* **Benefits**:
  * Earn $KAI rewards during this phase.
    * A total of **10 million $KAI** will be airdropped to participants during the Fund Commitment phase.
    * From the moment funds are deposited into the vault, participants will receive a maximum of **17 $KAI daily**, up to the end of the commitment phase.
* **Referral Program**: Each participant who deposits will receive a referral link. When others use this link to purchase, the referrer will receive **10% cashback**, and the buyers will enjoy a **20% discount** on their purchases.
* From the moment funds are deposited into the vault, participants will receive a maximum of **17 $KAI daily**, up to the end of the commitment phase.
* Over the full duration of the phase, participants can earn a total of **510 $KAI**.
* **Late buyers** will receive proportionally fewer $KAI rewards.
* **Redistribution Bonus**: Any unallocated $KAI will be redistributed among early participants at the end of the phase.
* **Start Date**: 14/1/2025
* **End Date**: 14/2/2025

#### **2.2 Public Node Sale Phase**

* Checker Nodes are distributed in two tiers based on fund commitment and availability:
  * After Tier 1 purchases, remaining nodes will be available for public participants on a first-come, first-served (FCFS) basis at the full price of **0.26 ETH (Full Price)**.
  * **Discount Opportunity**: Buyers during the Phase 2 Public Sale can still receive a **5% discount** on their purchases if they use a referral link. Additionally, the person providing the referral link will earn a **10% commission fee** from the referred purchase volume.
  * **Referral Link Activation**: Buy at least one node to activate your referral link.
* **Start Date**: 15/2/2025
* **End Date**: up until all nodes are sold out.
* **Number of Nodes Available**: 29 998 Nodes will be made available for this phase.

#### **2.3 Whitelist Eligibility Criteria**

* **NFT Holders**: Users who hold specific Kaisar NFTs.
* **Kaisock Event Winners**: Participants who won the whitelist from the Kaisock event.
* **Early community members:** Ambassadors, Kaisar OG and Fan badges, the most active users (≥ level 20 on Discord) …
* **Giveaway Winners**: Winners from giveaways hosted by Kaisar or our partners.

#### **2.4 Payment Methods**

* Accepted payment options: Users can use **ETH**, **USDC**, and **PEAQ** from the following networks:
  * **Ethereum Mainnet**
  * **Arbitrum**
  * **Base**
  * **Optimism**
  * **PEAQ Mainnet**
* Supported payment gateways: Transactions will be facilitated via integrated blockchain wallet platforms supporting these networks.
* **Wallets**: Users can use **MetaMask** for the sale. Please ensure you have sufficient **ETH** for blockchain gas fees and **PEAQ** for transactions on the PEAQ mainnet.
* **Conversion Rates**: The conversion between ETH and USDC prices will be determined one day before the sale begins to ensure accurate pricing.

## 3. Sale Dynamics

**3.1 Distribution Strategy**

| Tier    | Access                                | Price                 | Availability            |
| ------- | ------------------------------------- | --------------------- | ----------------------- |
| Round 1 | Whitelisted (Commitment Phase Buyers) | 0.208 ETH (20% Off)   | Early Access            |
| Round 2 | Public (FCFS Basis)                   | 0.26 ETH (Full Price) | After Tier 1 Completion |

#### **3.2 Allocation Priority**

* Both rounds will be conducted on a first-come, first-served (FCFS) basis. Make sure to secure your node as soon as possible to take advantage of the limited availability and benefits!

#### **3.3 Refund and Dispute Policy**

* Refunds available for failed transactions.


# Referral Mechanism

**10%** commission fee is reserved for all referrers. Participants in the Node Sale will receive a referral code. When friends join the Node Sale using your code, you will earn 10% of their contribution amount.

**For referral purchasers:**

Round 1: 20% discount

Round 2: 5% discount


# What is the Checker Node License (NFT)

The Checker Node License is an ERC721 NFT that lets you earn rewards by running a Checker Node Client. You can run your Client on your own machine, through a Virtual Private Server (VPS), through a Node-as-a-Service (NaaS) Provider, or delegate it to another user's machine.

You can purchase your NFT from [nodes.kaisar.io](https://nodes.kaisar.io) or through the secondary market in the future. Contracts will be released soon, so stay tuned for updates.

Checker Node NFT Licenses cannot be transferred from the purchase wallet during the first year.


# Reward Unlock Period

Checker nodes will receive $vKAI tokens. These tokens can be converted to $KAI according to this unlocking schedule:

* **Unlock within 30 days**: Receive 25% of your total $vKAI
* **Unlock within 90 days**: Receive 50% of your total $vKAI
* **Unlock within 180 days**: Receive 100% of your total $vKAI

**Example**: Converting 10,000 $vKAI to $KAI:

* 30-day unlock: Receive 2,500 $KAI
* 90-day unlock: Receive 5,000 $KAI
* 180-day unlock: Receive 10,000 $KAI


# FAQs

* **What are Checker Nodes?**

  Checker Nodes validate transactions, monitor uptime, and ensure system reliability within the Kaisar DePIN protocol.
* **How does the two-phase sale work?**

  Participants reserve funds during the Fund Commitment Phase, which determines their priority for the Node Sale Phase. Additional benefits include $KAI rewards, tier-based pricing discounts, and referral bonuses.
* **What is the relationship between a KaiNode NFT owner and a Checker Node Operator?**

  A Checker Node Operator can operate multiple Kaisar NFTs and claim rewards from a single machine through the Checker Node Client.

  To become a KaiNode NFT owner, you can purchase your NFT from [nodes.kaisar.io](https://nodes.kaisar.io) or through the secondary market in the future. Contracts will be released soon, so stay tuned for further updates.
* **Who can run a checker node?**

  A Checker Node Operator owns Kaisar Node NFTs and can run the checker node client on their own machine, through a Virtual Machine, through Node-as-a-Service, or by delegating to another user's machine.
* **What rewards can I expect as a Checker Node operator?**

  Rewards are distributed based on your node’s performance and uptime contributions.
* **Can I purchase multiple Checker Nodes?**

  Yes, subject to purchase limits to ensure decentralization.
* **How does the referral program work?**

  Referrers earn 10% cashback for purchases made through their referral link, while buyers receive a 10% discount.
* **What happens to unallocated $KAI rewards?**

  Any remaining $KAI rewards will be redistributed among early participants at the end of the Fund Commitment phase.


# How to Purchase Checker Nodes


# Step 1 - Connect wallet

Connect wallet at [nodes.kaisar.io](http://nodes.kaisar.io/)

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FfEakQQmqIIzHtDeiG1RW%2FMints_Tra%CC%A3ng%20tha%CC%81i%20chu%CC%9Ba%20ke%CC%82%CC%81t%20no%CC%82%CC%81i%20vi%CC%81.png?alt=media&#x26;token=35906d36-3e36-48b0-b32e-75f7abd44884" alt=""><figcaption></figcaption></figure>


# Step 2 - Choose the Network

Connect your Metamask wallet and select the appropriate blockchain network (Ethereum Mainnet, Arbitrum, Base, Optimism, or PEAQ Mainnet).

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FkhsLFtG4m1IloP1vvjOK%2FPopup%20connect%20wallet.png?alt=media&#x26;token=617ff978-ef8f-4318-bcc7-a6e4ebc78dc5" alt=""><figcaption></figcaption></figure>


# Step 3 - Commitment Submission

Deposit funds to reserve your position in the Checker Node Sale.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2Fh53hCMIj8dKhr70mgId5%2F%5BUpdate%5D%20Checker%20Node%20Sale.png?alt=media&#x26;token=e5172451-b36a-4b06-baff-9a7679d39bb1" alt=""><figcaption></figcaption></figure>


# Step 4 - Referral Link Sharing

Share your unique referral link to earn cash back rewards and provide discounts to buyers.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FSWoBwTCeTn6I9F0ZYtgi%2FReferrals.png?alt=media&#x26;token=9df525df-0302-4eb1-9201-043d1f28bb6a" alt=""><figcaption></figcaption></figure>


# Step 5 - Confirmation

Receive confirmation of your commitment and eligibility for rewards.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FY4vrXpTPeWOi7PYFaAFK%2FLicense.png?alt=media&#x26;token=a157ab5d-6f87-4352-8920-c2cf9932012b" alt=""><figcaption></figcaption></figure>

Congratulations you have now successfully purchased your Checker Node License!


# What’s Next?

After purchasing an Kaisar node, investors will receive an ERC-721 NFT to the wallet addresses used during the Kaisar node sale. The NFT symbolizes ownership of the purchased Kaisar node. Keep in mind that there's no cap on the number of nodes you can buy.

You can purchase as many nodes as you want, if available. The Checker Node license gives buyers lifetime access. The NFTs will be non-transferable for the first year after the node sale.

The NFTs will be airdropped to buyer wallets directly at a later date. There's no claiming process. There will be sufficient time between the NFT airdrop and time for us


# FAQs

#### 1. **Where will the node sale take place?**

The Kaisar Checker Node Sale will take place on <https://nodes.kaisar.io>

#### **2. When will I be able to install and run the Checker node?**

Feb, 2025

#### **3. How will the node licences be distributed?**

After purchasing a node license on <https://nodes.kaisar.io>, node licenses will be distributed as NFTs to users' purchase wallets. Only wallets holding a node license can operate nodes and earn $KAI token rewards.


# Kaisar Explorer

**Discover the Kaisar Network through Explorer. Go to** <https://onenode.kaisar.io/explorer>

Kaisar Explorer, an advanced web platform, provides real-time visibility into Kaisar on-chain metrics and operations for seamless navigation.

* **Operational Insights**: Access detailed information about the Checkers and Providers actively powering the Kaisar Network, ensuring transparency and operational awareness.
* **Network Metrics**:
  * **Earnings Overview**: Monitor the financial performance with real-time network earnings data.
  * **Connected Entities**: Track the number of active providers and checkers contributing to the network.
  * **Resource Availability**: Assess the scope of resources accessible across the network.
* **Provider Capabilities**: Gain comprehensive insights into the aggregate offerings of online providers, including total CPU cores, memory allocation, and storage capacity.
* **Real-Time Monitoring**: Leverage cutting-edge real-time tracking to observe provider performance and activity as it unfolds, enabling informed decision-making.
* **Unlocking Potential**: Engage with Explorer to delve into the robust infrastructure and continuous evolution of the Kaisar Network, unlocking a deeper understanding of its capabilities and growth trajectory.

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2F8CPxescYvnhhY0AVyhW6%2Fscreencapture-onenode-kaisar-io-explorer-2025-05-21-08_30_50.png?alt=media&#x26;token=6a295a72-650c-42c1-9deb-b4dee9b0cfb8" alt=""><figcaption></figcaption></figure>

**Detailed information about the Providers actively**

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FxEW5rDSvZVh3mIJmfl0e%2Fscreencapture-onenode-kaisar-io-provider-2025-05-21-08_36_30.png?alt=media&#x26;token=2ddf1f4e-e9f4-4bf8-b109-dd3ee2a5d085" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3420828033-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRdDiw8sqrhonsv2Gsd47%2Fuploads%2FKHS7PtuX3BTzhzIn5n0G%2Fscreencapture-onenode-kaisar-io-provider-0xc623eb1b52784701D2d70f3e9C0D3AC1fEf8aB99-2025-05-21-08_38_47.png?alt=media&#x26;token=e2ff5a57-982d-41e2-97ef-db3d1bd4ec11" alt=""><figcaption></figcaption></figure>


# Kaisar Rewards Mechanism


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


# Get Real Campaign

**Get Real is Peaq’s growth campaign that rewards participants for joining as Kaisar Network providers**

**🚀 Join Kaisar Network:** <https://kaisar.io/>

The Get Real campaign leverages 5% of peaq’s initial supply (210,000,000 PEAQ) to incentivize the community to join the Machine Economy on peaq. Spanning across 12 seasons, the year-long campaign will reward real people for creating real value. The participants will also receive their own unique, customizable NFTs, which will evolve as they create real-world value. Get Real empowers people from around the world to join the movement and help build the Machine Economy — and the future where the world runs on Web3. Access the Get Real campaign [here](https://portal.peaq.network/portal/campaign/introduction).

### How to Complete Kaisar Network’s Quest in the Get Real Campaign and Unlock $PEAQ

To participate and earn rewards, follow these simple steps:

1️⃣ **Download Kaisar Provider App** – Coming Soon.[\
](https://drive.usercontent.google.com/download?id=1CpBXl2kGfWs9F9zjwQXab8ctxlG8EbWe)2️⃣ I**nstall and run the app** – Coming Soon.\
3️⃣ **Complete the Quest** – Follow the necessary steps as outlined in the campaign.\
4️⃣ **Unlock Your Rewards** – Receive $PEAQ as a reward for successfully becoming a provider.

Ready to get started? 🚀

📌Please contact the admin of Kaisar Network for a comprehensive step-by-step guide to install and run the Kaisar Provider App


# Contact and Support

For any queries or assistance during the sale, please contact:

* **Email**: <contact@kaisar.io>
* **Support Portal**: [nodes.kaisar.io](http://nodes.kaisar.io)
* **Official Channels**:
  * **X (formerly Twitter)**: <https://x.com/KaisarNetwork>
  * **Telegram**: <https://t.me/KaisarNetwork>
  * **Discord**: <https://discord.gg/KaisarNetwork>
  * **LinkedIn**: <https://www.linkedin.com/company/kaisar-network>


# Legal and Compliance

* Participants are responsible for ensuring compliance with local regulations.
* Kaisar holds the right to amend sale details as necessary.
* Terms and conditions apply; refer to the official Kaisar website for more information.


# Sale Disclaimer

* The Checker Node Sale is not an investment offering or securities sale. Participation is purely voluntary and is intended for individuals or entities seeking to actively support and contribute to the Kaisar ecosystem.
* Rewards and incentives are subject to change based on the discretion of Kaisar, market conditions, and participation levels.
* Funds committed during the Fund Commitment Phase are non-refundable unless otherwise stated in the Refund Policy.
* Kaisar is not liable for any financial losses, technical issues, or regulatory non-compliance arising from participation in the sale.
* Participants are advised to perform due diligence and seek independent advice before committing funds.
* By participating, individuals acknowledge and accept all terms and conditions outlined by Kaisar for the Checker Node Sale.


