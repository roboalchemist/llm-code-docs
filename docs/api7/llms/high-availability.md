# Source: https://docs.api7.ai/ingress-controller/high-availability.md

# Source: https://docs.api7.ai/apisix/enterprise-feature/high-availability.md

# High Availability

High availability (HA) of an API gateway refers to its ability to provide uninterrupted service even in the face of failures or abnormal conditions. This is typically achieved through techniques such as redundancy and load balancing:

* **Redundancy** involves deploying multiple instances of the API gateway to eliminate single points of failure. If one instance fails, others can continue to handle requests seamlessly.
* **Load balancing** ensures that incoming requests are distributed across multiple API gateway instances. This helps maintain an acceptable workload on each instance, thereby enhancing overall service quality and reliability.

By combining these strategies, organizations can minimize downtime and maintain consistent performance, ensuring the gateway remains robust under various conditions.

## Key Features[â](#key-features "Direct link to Key Features")

API7 Enterprise extends high availability to both its control plane (CP) and data plane (DP), ensuring resilience and reliability across the entire system.

* **High Availability of Data Plane**: The data plane and control plane of API7 Enterprise are decoupled thanks to the stateless data plane. Users can retrieve configurations from both local devices and Amazon Simple Storage Service (S3) or use standalone mode, enabling effortless scaling and resizing. This design ensures that even if the control plane experiences downtime, the data plane remains fully operational. This enables API7 Enterprise to effortlessly handle millisecond-level configuration updates and support thousands of gateway nodes.

  Moreover, API7 Enterprise provides the [gateway health probing](https://docs.api7.ai/enterprise/best-practices/gateway-health-probe) for enhanced high availability. The load balancer (LB) can rely on health probes, such as a status endpoint provided by the API7 Gateway, to monitor its operational state. If an instance is deemed unhealthy, the LB will reroute requests to healthy instances, preventing disruptions and downtime. By implementing robust health check probing mechanisms, API7 Enterprise can maintain service continuity and ensure seamless traffic management.

* **High Availability of Control Plane**: Another crucial decision is to use PostgreSQL as the default configuration center. PostgreSQL provides mature high-availability solutions, including master-slave and multi-master backup, reducing downtime and maintaining data consistency. The control plane would periodically write configuration files to S3 for backup, ensuring data redundancy and minimizing the risk of data loss. By separating configuration and dashboard, API7 Enterprise allows users to deploy multiple dashboards, enhancing the system's flexibility.

* **API7 Cloud for CP High Availability**: In addition, users can realize the high availability of control plane using API7 Cloud, which can be maintained by API7 experts. Users can choose any cloud, including multi-cloud and hybrid-cloud, to deploy the data plane, and handle traffic and data within their infrastructure without data leakage. Furthermore, being SOC2 and GDPR compliant, API7 Cloud offers flexible pricing models; users can select the pay-as-you-go model or get special packages for custom requirements.

![High Availability Diagram of API7 Enterprise](https://static.api7.ai/uploads/2024/12/17/6g8Ay6Cf_high-availability.png)

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Disaster Recovery and Fault Tolerance[â](#disaster-recovery-and-fault-tolerance "Direct link to Disaster Recovery and Fault Tolerance")

With high availability, API7 Enterprise can safeguard systems against unexpected failures, such as server crashes or network outages. API7 Enterprise writes the configurations into Amazon S3 periodically, enhancing disaster recovery capabilities. Moreover, leveraging PostgreSQL with master-slave and multi-master configurations ensures data consistency and system resilience, even during significant disruptions.

This mechanism automatically redirects traffic to healthy nodes or failover systems, enabling uninterrupted API traffic flow. API7 Enterprise's high availability design also ensures system updates, maintenance, and scaling can occur with zero downtime, preserving the integrity and reliability of API services during these processes.

### Elastic Scalability for Growing Traffic Demands[â](#elastic-scalability-for-growing-traffic-demands "Direct link to Elastic Scalability for Growing Traffic Demands")

API7 Enterprise is designed to meet the scalability requirements of modern systems by leveraging a stateless data plane architecture. This design decouples the data plane from the control plane, enabling seamless and flexible scaling to accommodate fluctuating traffic volumes.

To further enhance reliability, API7 Enterprise supports standalone mode or retrieves configurations from robust storage solutions like local storage and Amazon S3. These mechanisms ensure uninterrupted service availability, even during unexpected disruptions or traffic surges. With its high availability and scalable design, API7 Enterprise efficiently handles sudden spikes in traffic without compromising performance or user experience.

### Multi-Cloud and Hybrid-Cloud Deployments[â](#multi-cloud-and-hybrid-cloud-deployments "Direct link to Multi-Cloud and Hybrid-Cloud Deployments")

Besides on-prem deployment, API7 Enterprise provides API7 Cloud, offering flexible deployment across multi-cloud and hybrid-cloud configurations. It ensures resilience and high availability in the control plane, safeguarding the system against potential disruptions. With API7 Cloud, organizations benefit from centralized API management, regardless of where the data plane is deployed.

Additionally, the expert support provided by API7 ensures proactive monitoring, timely updates, and swift resolution of any issues, further enhancing the high availability of the system. This approach empowers businesses to maintain continuous service delivery, comply with complex regulations, and scale their operations effectively in a multi-cloud or hybrid-cloud ecosystem.

### Health Check Probing for System Resilience[â](#health-check-probing-for-system-resilience "Direct link to Health Check Probing for System Resilience")

API7 Enterprise implements robust health check probing mechanisms that continuously assess the status of API instances. This proactive monitoring ensures that any instance that becomes unhealthy is swiftly identified and isolated. By automatically rerouting traffic to healthy instances, API7 Enterprise minimizes the risk of service disruptions during peak loads or unexpected failures.

This mechanism can inspect the running status of the gateway and check gateway readiness for traffic. This capability not only enhances overall system resilience but also supports uninterrupted API performance during critical operations, maintenance, and scaling activities, ensuring a reliable user experience at all times.
