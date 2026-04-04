# Source: https://io.net/docs/guides/architecture/io-architecture.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Architectural Layers

> The IO Portal architecture is a multi-layered, cohesive structure that provides a seamless, secure, and efficient user experience. Each layer has a distinct role, working in tandem to ensure the system's optimal performance. The architecture is built upon modern technologies, ensuring scalability, reliability, and robustness.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e965e2c-ionet-arch-diagram.png?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=18b06700ec750345cfcef0dcb83044ff" alt="" data-og-width="1302" width="1302" data-og-height="3821" height="3821" data-path="images/docs/e965e2c-ionet-arch-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e965e2c-ionet-arch-diagram.png?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=28507e6bb075bcb69047c2e1bf4e8678 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e965e2c-ionet-arch-diagram.png?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=fba7610d00166f15f3fa3f541a3cb5c8 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e965e2c-ionet-arch-diagram.png?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=ad10781702a3bcded5f0fb087cbac458 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e965e2c-ionet-arch-diagram.png?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=c19d516f23e7ff4fa3a4d97f39538490 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e965e2c-ionet-arch-diagram.png?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=7a1edbb26e2e1859ee0d794eac7c3640 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e965e2c-ionet-arch-diagram.png?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=4c59a3bd8accc228d1fb595e90a48624 2500w" />
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
