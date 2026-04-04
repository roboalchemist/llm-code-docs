# Source: https://io.net/docs/guides/clouds/start-using-io-cloud.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Discover the simple steps for creating, configuring, deploying, and managing clusters, giving you complete control over your computing power.

## Introduction

IO Cloud enables the deployment and management of on-demand, decentralized GPU clusters, giving users access to powerful GPU resources without significant hardware investments or the complexity of managing infrastructure. IO Cloud democratizes GPU access by leveraging a decentralized model, providing machine learning engineers and developers with the same seamless experience as traditional cloud providers.

The platform utilizes a distributed network of nodes, IO workers, to offer flexible, scalable compute resources. IO Cloud clusters are self-healing, fully meshed GPU systems that ensure high availability and fault tolerance. With IO Cloud, you can tap into a decentralized network of GPUs and CPUs capable of running Python-based machine learning workloads. It is ideal for AI projects requiring distributed compute. The platform is natively built on the Ray framework, the same distributed computing technology used by OpenAI to train models like GPT-3 and GPT-4 across hundreds of thousands of servers.

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/IZ7qjUFucdo" title="Start Using IO Cloud: Your First Steps Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## IO Clouds Integration Flow

The diagram below provides a high-level overview of how users integrate with IO Cloud - from choosing a compute resource to launching AI workloads. It illustrates the end-to-end flow across key components, including cluster selection, container deployment, and runtime execution.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f317543b116c7a9e1ca2f52fb70034ee1796079973adb11871d6a244dde709b9-IO_Cloud_v3.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=9a455f1ba395f34093f602e5d7d285e2" alt="" data-og-width="4212" width="4212" data-og-height="3188" height="3188" data-path="images/docs/f317543b116c7a9e1ca2f52fb70034ee1796079973adb11871d6a244dde709b9-IO_Cloud_v3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f317543b116c7a9e1ca2f52fb70034ee1796079973adb11871d6a244dde709b9-IO_Cloud_v3.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1edd7c9eca42f9f2171e5fb61681e9ab 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f317543b116c7a9e1ca2f52fb70034ee1796079973adb11871d6a244dde709b9-IO_Cloud_v3.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=355f4e0bdbafda3c85b39ad05baf65de 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f317543b116c7a9e1ca2f52fb70034ee1796079973adb11871d6a244dde709b9-IO_Cloud_v3.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=bb0a14a60260bebd736d9c9c0dbc930b 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f317543b116c7a9e1ca2f52fb70034ee1796079973adb11871d6a244dde709b9-IO_Cloud_v3.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=ce9ccb4cdfcf7ba75ece6409a775c192 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f317543b116c7a9e1ca2f52fb70034ee1796079973adb11871d6a244dde709b9-IO_Cloud_v3.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=d42e19c9f48d82984df6807d88fa1816 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f317543b116c7a9e1ca2f52fb70034ee1796079973adb11871d6a244dde709b9-IO_Cloud_v3.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=c368dddda49732a916e7a49a9416e88a 2500w" />
</Frame>

## Create Account

To create an account, go to [cloud.io.net](https://cloud.io.net/cloud/home) using Google, Apple ID, GitHub, Hugging Face, X, Worldcoin, or simply with a one-time password by clicking the "Login with Email" button.

<img src="https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=470902a5e8a08e075157120cae667cd7" alt="Newlogin1 Jp" data-og-width="1868" width="1868" data-og-height="1058" height="1058" data-path="images/docs/login_process/newlogin1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=280&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=129a29b9bac3df741db40e99bda417d2 280w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=560&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=4b7d81b89eb0b45a1c968b111b852850 560w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=840&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=7a6eb785992b9c0ecf6d76c5b0a9c3cf 840w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=1100&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=076a5c9517bc68d1a06efc5429ce5c8a 1100w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=1650&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=900b615e45f5d691226cbc7930a1ea3d 1650w, https://mintcdn.com/ionet-cca8037f/1nusXKdPVUHoDz-x/images/docs/login_process/newlogin1.jpg?w=2500&fit=max&auto=format&n=1nusXKdPVUHoDz-x&q=85&s=fd4ba61049c65504f7c2b618ed7762d3 2500w" />

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
  <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6bc0b6e9298d06a9c4ca84121681dd7dbec173b401dea926e5a600471b020dc0-IOClouds.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=e57f1e27f3463a840f0f5d200a129f44" alt="" className="mx-auto" style={{ width:"56%" }} data-og-width="1082" width="1082" data-og-height="1288" height="1288" data-path="images/docs/6bc0b6e9298d06a9c4ca84121681dd7dbec173b401dea926e5a600471b020dc0-IOClouds.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6bc0b6e9298d06a9c4ca84121681dd7dbec173b401dea926e5a600471b020dc0-IOClouds.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=9035269133ad77443b98f26de613b689 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6bc0b6e9298d06a9c4ca84121681dd7dbec173b401dea926e5a600471b020dc0-IOClouds.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=d973a713b14916067f76d5e670798718 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6bc0b6e9298d06a9c4ca84121681dd7dbec173b401dea926e5a600471b020dc0-IOClouds.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=cde274097559299ff02e98a69fde06e8 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6bc0b6e9298d06a9c4ca84121681dd7dbec173b401dea926e5a600471b020dc0-IOClouds.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=e69750c63c111a00522fd8b5939b5ba3 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6bc0b6e9298d06a9c4ca84121681dd7dbec173b401dea926e5a600471b020dc0-IOClouds.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=75f5b83e5a2a21fd35e162a462651081 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/6bc0b6e9298d06a9c4ca84121681dd7dbec173b401dea926e5a600471b020dc0-IOClouds.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=1aa748e5d5fa108a1e9f5b75a3f4dc8f 2500w" />
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
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78530e4-view_cluster_tab.png?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=8b7d48cc314eef32b150fb5051a2abfb" alt="" data-og-width="2660" width="2660" data-og-height="952" height="952" data-path="images/docs/78530e4-view_cluster_tab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78530e4-view_cluster_tab.png?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=9947425d45f1973c01dcc385eda9df82 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78530e4-view_cluster_tab.png?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=9f83d1c45b99333c56a77c3a7275d349 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78530e4-view_cluster_tab.png?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=a0be91c116f27d53292127f64679af4b 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78530e4-view_cluster_tab.png?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=346b7160368c45959acebb26e7794f49 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78530e4-view_cluster_tab.png?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=952dfdbd4342ae02086bcbf9a91a2ea2 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/78530e4-view_cluster_tab.png?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=885b5c49587d1c52cf51d53a3fc4cb49 2500w" />
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
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3981a0-view_cluster2.png?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=97a269996aec90b7f118d0eb55b918d0" alt="" data-og-width="2604" width="2604" data-og-height="2498" height="2498" data-path="images/docs/f3981a0-view_cluster2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3981a0-view_cluster2.png?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=62f1fa7b54c038e198b6468d1af7e12e 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3981a0-view_cluster2.png?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=c84a0c6bc8e6c1b46cfccc25e892dd89 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3981a0-view_cluster2.png?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=1d9e13f953b95b44e1bf46d7f7e70e20 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3981a0-view_cluster2.png?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=05e54591efa0b6b2426b8cde2bb34488 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3981a0-view_cluster2.png?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=c597678ecb183628c1bf5ce47edb571b 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/docs/f3981a0-view_cluster2.png?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=7a659b480fa24ae500c956651b8d77c1 2500w" />
</Frame>
