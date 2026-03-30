# Source: https://docs.acceldata.io/documentation/adoc-architecture.md

# Architecture - Deep Dive

> The architecture is a high-level overview of the Data Plane, Control Plane, Installation, and Security. These are the critical components of ADOC infrastructure. Proper installation and security procedures are critical to ensuring that the ADOC operates efficiently and safely.

## ADOC Architecture Overview

The Acceldata Data Observability Cloud (ADOC) is an integrated system that provides reliable data observability solutions. The design is purposefully divided into two distinct settings - the Control plane which is managed by the Acceldata and the Data Plane - to enable effective data handling and monitoring.

The present architectural diagram depicts the dynamic interplay between these two settings by highlighting the major components and their relationships.

The following diagram illustrates the architecture of ADOC:

![ADOC Architecture](https://uploads.developerhub.io/prod/Yoq2/3amaxjo0ed65bof56eu2rn25pe58a597w2thdvo434g4dmo649w0bi9v98yydjts.png)

## Control Plane

This environment represents the nerve center of the ADOC platform, powered by Amazon Web Services (AWS). It encapsulates a suite of AWS services meticulously orchestrated to host and run the ADOC platform, with Acceldata being accountable for the management of the cloud infrastructure.

![Control Plane](https://uploads.developerhub.io/prod/Yoq2/rpuj1tehrj4eii2admd8cme5cbl4r9nutfra87a68yv4l1n5avt3pb8oadrgmxfe.png)

### Key Features of Control Plane

Managed by Acceldata, the control plane is the epicenter for administrative operations. It houses the core microservices, orchestrating tasks, managing configurations, and overseeing communication across the platform. It encompasses several critical microservices.

- **Virtual Private Cloud (VPC)**: The backbone of this network architecture, a VPC provides logically isolated sections of the AWS cloud where resources can be launched in a defined virtual network.

![VPC Layer - Control Plane](https://uploads.developerhub.io/prod/Yoq2/izjc05mhhoutc9mr2jbd2f49se3s7031lr1zvowdp7yj4is79olflm8wibdixvc0.png)

- **Zones**: The ADOC Control Plane's design is divided into zones that reflect distinct regions of the VPC. These zones aim to improve the system's resilience and availability. By compartmentalizing resources, each zone can run semi-independently, resulting in efficient load distribution and robust fault tolerance. Zone 1, Zone 2, Zone 3,each numbered zone represents a subnet or cluster within the VPC. This multi-zone architecture guarantees that services are distributed across multiple physical locations, lowering the chance of simultaneous outages and providing geographic redundancy. Workloads are balanced among these zones to improve speed and minimize latency for end users.

![Zones - Control Plane](https://uploads.developerhub.io/prod/Yoq2/htbu6p7ciyhcqlt3wp3qm2ps6qh45n364cldgxxpkcuzv8qdtndecmtre181zxlr.png)

- **Public Subnets**: These subnets are part of the cloud network visible to the public internet, hosting resources that need to be accessed directly, such as the Cloud User Interface.
- **Private Subnets** : Contrary to public subnets, these are isolated sections of the cloud network that house resources requiring additional security, limiting public access.

![Subnets Layer - Control Plane](https://uploads.developerhub.io/prod/Yoq2/daj3a4uvc8ra7xz4smdr77hqnn8ksittjdz55h4ba0ee5nbj8k6xwaopjlsr3xq9.png)

- **Load Balancers**:  These are strategically placed to distribute the incoming network traffic across multiple servers, preventing any one server from becoming a bottleneck, thus ensuring efficiency and high availability.

![Load Balancers - Control Plane](https://uploads.developerhub.io/prod/Yoq2/5ogef36ohoojsd8d1nqq3d7zgzuobm8v7sb7wbdkl43yorayxney3f95n7old03r.png)

- **Nodes**: Nodes are individual instances or servers in a subnet that make up a bigger network infrastructure. Each node acts as a separate entity capable of processing, storing, and forwarding data. The connections between nodes are network routes that enable communication and data exchange. These connections are critical for a network's dispersed activities, guaranteeing that each node can work together to accomplish collective tasks or services.

![Nodes - Control Plane](https://uploads.developerhub.io/prod/Yoq2/dpnjjgdrto55jd6o9c73ylvkgxz6dgvzxikl034t35jbdf9pgtvhlcga4h42umvy.png)

- **Secure Channel**: The Control Plane communicates with Data Planes over a private, encrypted channel powered by [Cloudbridge](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/adoc-architecture#cloudbridge-secure-connectivity-between-control-plane-and-data-plane).

![Secure Channel](https://uploads.developerhub.io/prod/Yoq2/jz1hvni4hswnqfhlc6rsmk4n3zwso6tqoh2p3su3x7jcp7dwytiwvwfo3yo4nun5.png)

- **Datastore Search**: The Search Datastore is a specialized database within the ADOC platform designed for efficiently handling and executing search queries across vast datasets. This datastore indexes data in a way that optimizes search operations, allowing for rapid querying and retrieval. It's engineered to support complex searches, including full-text and multi-parameter searches, facilitating immediate access to relevant data for analytics and monitoring tasks.

![Datastore Search - Control Plane](https://uploads.developerhub.io/prod/Yoq2/sw8yd9adunyo6yiq9wt6o9kj6u0rtm9xl9ifzfi79go0ed9utumdesc5cpoifex2.png)

- **Cloud Storage**: Cloud Storage within the ADOC platform represents scalable and secure data storage solutions in the cloud. It is used for persisting large volumes of data generated and used by the platform, including logs, metrics, and configuration information. Cloud Storage ensures data durability and high availability, making it accessible for processing and analysis by other components within the platform. It supports the platform's infrastructure by providing a reliable foundation for storing and managing data that is crucial for observability and operational intelligence.

![Cloud Storage - Control Plane](https://uploads.developerhub.io/prod/Yoq2/qr61d7pf09o2ehndmqv0hhfaoid616grf42hl9iy0d3b4t4405tefu57wne0eoia.png)

- **Message Bus:** The Message Bus in the ADOC Control Plane architecture is a powerful communication system that facilitates the exchange of information between different components and services within the platform. It acts as a central conduit for message passing, ensuring that data flows seamlessly and efficiently across the system. The Message Bus is designed to handle high-throughput, low-latency messaging, which is essential for real-time data processing and event-driven architectures. It provides a reliable and scalable way to decouple system components, allowing for flexible and maintainable codebases.

![Message Bus - Control Plane](https://uploads.developerhub.io/prod/Yoq2/bdlr9fkotq2wh65cz2vnup0bx55cl7p6kdmej4snl5f523qkafywq5gw3m0r0xyk.png)

- **Database:** The Database component serves as the persistent storage solution within the ADOC Control Plane architecture. It is responsible for securely storing all the platform's configuration data, metadata, and the observability data collected from various sources. The database is optimized for high performance and availability to ensure that data retrieval and storage operations can keep pace with the demands of the observability platform. It plays a vital role in data management, supporting transactional operations, complex queries, and providing a foundation for analytics and reporting functionalities.

![Database - Control Plane](https://uploads.developerhub.io/prod/Yoq2/m0vopr3rc3e6zqpyrtlkrzplmuujexwiqre8h3a9xos43zpq73rmvqav1tjcmq8s.png)

These components work together to create an ecosystem that not only ensures operational efficiency and system resilience but also offers scalability to accommodate the growing needs of the users. The Acceldata Environment, with its advanced architecture, empowers organizations to maintain a clear lens into their data landscape, fostering informed decision-making and proactive problem-solving.

### Cloudbridge: Secure Connectivity Between Control Plane and Data Plane

Acceldata Cloudbridge is a secure connection system that enables the Control Plane to securely communicate with every Data Plane instance, **without requiring customers to expose any public inbound ports**.

Cloudbridge uses an **always-on, outbound-only, mutual TLS (mTLS)** connection initiated from the Data Plane and authenticated by the Control Plane. This ensures that all orchestration (crawling, analysis, profiling, scheduling, policy execution, and metadata collection) happens over a private, verified, encrypted channel.

#### Key Capabilities

- **Zero Ingress Requirement:** Customers do _not_ open any inbound network access. Data Plane only connects outwards.
- **Mutual TLS Authentication:** Both sides verify each other using Acceldata-issued certificates managed by the Acceldata’s PKI.
- **Continuous Secure Channel:** Each Data Plane maintains a long-running mTLS connection to the Control Plane.
- **Per-Request Ephemeral Channels:** For every action the user triggers in ADOC UI, the Control Plane creates a short-lived encrypted channel over the already established mTLS channel.
- **Automated Certificate Lifecycle:** Certificates are issued and revoked automatically based on the data plane’s lifecycle.

#### How Cloudbridge Fits Into the Control Plane

Cloudbridge is part of the Control Plane’s networking and orchestration layer. Several new and enhanced components support secure connectivity:

#### How Control Plane Uses Cloudbridge During Operations

1. **Data plane Initiates a Secure Connection**
    - When deployed, the Data Plane’s Cloudbridge-Client opens an outbound mTLS connection to the Control Plane Cloudbridge-Server.
    - This mTLS channel remains connected indefinitely.

2. **User Performs an Action in ADOC UI**
    - Example: Crawl Snowflake, refresh schema, run profiling, execute reliability policy, run pushdown job.
    - Control Plane identifies the appropriate Data Plane and uses the already established mTLS secure channel.

3. **Secure Per-Request Channel Created**
    - Cloudbridge-Server creates a temporary encrypted channel over the persistent mTLS channel created by the Cloudbridge-Client.
    - The Data Plane executes the requested task.

4. **Response Returns Through the Same Secure Channel**
    - Control Plane receives the response from the data plane via the same secure channel the request went through and the temporary channel will be closed.

---

## ADOC Control Plane Components

![Component - Control Plane](https://uploads.developerhub.io/prod/Yoq2/vagrtgvys2pbciz66qxrnknkiycxngvdf51phd7oznxw8neevo2hnpop5g1ut07a.png)

### Infrastructure

![Component - Infrastructure](https://uploads.developerhub.io/prod/Yoq2/b2mqqsm3j97cevbrmacoacdf7edsa1c3fiodk842rbuegcubzkx60yvsi5hjr5i4.png)

| **Name** | **Description** | 
| ---- | ---- | 
| Reverse Proxy | Acts as an intermediary for requests from clients seeking resources from the ADOC platform. It ensures load balancing, provides SSL termination, and facilitates secure access control, enhancing security and system performance. | 
| Dashplots | It is a visualization tool that offers real time data representations, helping users to interpret complex datasets through dashboards. It streamlines decision-making processes by transforming data into accessible and actionable insights. | 
| Admin Central | This is the operational hub where administrators can perform a wide array of tasks, ranging from user management to system-wide configurations. It provides tools and interfaces to maintain and optimize the ADOC platform's performance. | 
| Incident Manager | This component acts as a command center for incident detection and response. It automates the identification of system incidents, streamlines the response process, and ensures that incidents are resolved efficiently and effectively. | 
| Alerts | The alert system is engineered to monitor system health and trigger notifications for predefined events or metrics that exceed acceptable thresholds. It helps maintain system integrity by prompting immediate attention to potential issues. | 
| Management | The management component oversees operational processes and resources within the ADOC infrastructure. It is responsible for task scheduling, resource allocation, and operational oversight, ensuring the system runs at peak efficiency. | 


### Platform

![Component - Platform](https://uploads.developerhub.io/prod/Yoq2/3eyclkech4xmqaqszhhv9bqhh93wq3lo8aemy9qvwvhb2ljca2wujsfcua5d9bg7.png)

| **Name** | **Description** | 
| ---- | ---- | 
| Auth | This component is responsible for ensuring secure access to the ADOC platform. It handles authentication protocols, granting permissions and verifying the identities of users or services that interact with the platform. By employing robust security measures, such as two-factor authentication or OAuth tokens, the Auth module safeguards sensitive data and system integrity. | 
| Secret Manager | Protects and manages sensitive information necessary for the platform's operations. It centralizes the handling of secrets, which is essential for maintaining secure and automated access to credentials and keys within the platform's ecosystem. | 
| Columnar Database | Specialized database optimized for reading and analyzing data stored in columns, improving query performance and facilitating faster data analytics. | 
| Cache | Serving as a temporary storage area, the Cache component dramatically boosts the ADOC platform's performance. By caching frequently accessed data, it minimizes latency and reduces the load on the primary storage system, ensuring that repeated data requests are served quickly and efficiently. This not only enhances user experience but also optimizes resource utilization. | 


### Compute

![Component - Compute](https://uploads.developerhub.io/prod/Yoq2/7zk6ck818eiqjhlz44mjj3mzorcwxuulepq0bz5k9kw40cp859l4l2aeepxvv9rr.png)

| **Name** | **Description** | 
| ---- | ---- | 
| Databricks Connectors | Interfaces that link compute resources, ensuring seamless data flow and integration between compute operations and the ADOC platform. | 
| Snowflake Connectors | Custom connectors designed to work with Snowflake data warehousing solutions, facilitating efficient data transfer and processing. | 
| Consumer APP Worker | Manages the storage and analysis of time-series data, crucial for monitoring trends, patterns, and anomalies over time. | 


### Machine Learning

![Component - ML](https://uploads.developerhub.io/prod/Yoq2/s1arkre8cc94klbl4qempsgpkgd1lov12mph4er7dfw7vo2oam3n4btqwfpd2hcd.png)

| **Name** | **Description** | 
| ---- | ---- | 
| Time Series ML | This component leverages advanced machine learning algorithms to perform in-depth analyses and generate predictions from time-series data. By examining patterns and trends over time, Time Series ML enhances the ADOC platform's capability to deliver forward-looking insights, predictive analytics, and intelligent forecasts that can inform decision-making and strategic planning. | 
| Time Series Ingestion | The ingestion module is dedicated to the collection and assimilation of time-based data streams into the ADOC platform. It ensures that the data is accurately captured, timestamped, and made ready for further processing. This component is essential for handling high-velocity data that may come from various sources like IoT devices, application logs, or system monitors. | 
| Time Series Management | This component serves as the administration hub for time-series data. It manages the lifecycle of the data, including storage, retention policies, indexing, and aggregation. Time Series Management is critical for maintaining data integrity, facilitating rapid query responses, and optimizing the storage system for efficient retrieval and analysis of time-dependent data. | 


#### Reliability

![Component - Reliability](https://uploads.developerhub.io/prod/Yoq2/q16w7cirstedjeuyc92y2qvhs9ztejkq6lm6dagkrcnhy20iy7zzg7lzsw8inbqz.png)

| **Name** | **Description** | 
| ---- | ---- | 
| Pipeline Service | Monitors and ensures the operational health of services within the ADOC ecosystem, proactively addressing issues to maintain system reliability. | 
| Reporting Service | Generates comprehensive reports on system performance, data quality, and operational insights, aiding in decision-making and strategy formulation. | 
| Catalog Server | Manages and catalogs metadata from various data sources, providing a structured and searchable repository for efficient data retrieval and management. | 


---

## Data Plane

The Data Plane within the ADOC architecture is the layer that directly interacts with and manages the client's data resources. Managed by the client, it is structured to provide efficient data handling, processing, and storage capabilities, vital for comprehensive data observability. The Data Plane architecture employs SSL encryption to ensure the secure transmission of data, showcasing the commitment of the platform to data security and integrity.

![Data Plane](https://uploads.developerhub.io/prod/Yoq2/1w7vo2lkf7k1vj14pax226sj6ixdv5wcsk24ooyhvoz3eh09zl9fy66mwmgskm1j.png)

### Data Plane Services

![Data Plane - Services](https://uploads.developerhub.io/prod/Yoq2/0wtz18hx65mj351y9dli3bu1a9vw4v0mbzhfjjj43uo5k1nlinq1rrmt63p1j6pq.png)

| **Name** | **Description** | 
| ---- | ---- | 
| Crawler | Discovers and catalogs available data sources and metadata within your environment, ensuring that all client datasets are known. | 
| Analysis Services | Executes local data validation, transformation and computation of observability metrics (e.g. freshness, reliability). | 
| Monitor Services | Continuously collects telemetry, health-checks and metrics from data sources and processing jobs for real-time observability. | 
| Reverse Proxy | Provides a secure entry point for Control-Plane communication and client queries, routing traffic over an SSL-encrypted channel. | 


### Spark Services

![Data Plane - Spark Services](https://uploads.developerhub.io/prod/Yoq2/9gdym0nxna6ye8ha3ejo47lkr2w5cb38oqa37l8rizdkl0wl9xkh1nuxuc2ftk5q.png)

| **Name** | **Description** | 
| ---- | ---- | 
| Spark Applications | Dedicated computational units that perform big data processing tasks using Apache Spark, which can handle batch and stream processing. | 
| Profiler Jobs | These jobs analyze data performance and quality, profiling data to ensure it meets the standards and requirements of the organization. | 
| Spark Operator | Orchestrates and manages Spark applications, ensuring efficient resource allocation and scheduling of data processing tasks. | 
| YARN Scheduler | Manages and schedules jobs across the cluster, optimizing the use of system resources and improving job execution times. | 


### Client Data Sources

The foundation upon which data observability is built, comprising databases and storage systems that store and serve the raw data. Each data source is a repository that may include relational databases, NoSQL databases, file systems, and data warehouses.

These client-managed data sources are crucial for the ongoing collection and provision of data, enabling the Data Plane to perform its monitoring and analysis functions effectively.

![](https://uploads.developerhub.io/prod/Yoq2/bpjesiokizfk5fr8mq4vqdy2dp4vynugiwk8glvq7nh2gi8zu4heeiao2zwllkui.png)

All customer databases, data services, and cloud data repositories are included in the customer data section. Once the database is integrated into ADOC as a data source, ADOC continuously monitors the data on the customer data platform. Once configured, the data plane connects to your data platform to retrieve data for computation and reliability activities. Overall, ADOC's customer data sector is critical to its operations since it gives access to valuable client databases and data services. ADOC can assure dependable access to this data for multiple activities by continuously monitoring and configuring the data plane.

> You can also create [Pipelines](https://docs.acceldata.io/sdk) to automate tasks. A Pipeline is a set of jobs that are executed in a sequential order. When a pipeline execution begins, all the jobs in the pipeline are executed. You can also use Acceldata's [Software Development Kit (SDK)](https://docs.acceldata.io/sdk/getting-started-python) to monitor Python data pipelines.

## Integration with the Control Plane

While the Data Plane focuses on direct data management and operational tasks, it integrates seamlessly with the Control Plane, which provides overarching governance, administration, and strategic management of the ADOC platform. This integrated approach ensures that data flows smoothly from the point of collection and storage to analysis, enabling enterprises to have a real-time and historical view of their data landscape.

> Data communication between the Acceldata Environment and Customer Environment is carried through a secure channel.