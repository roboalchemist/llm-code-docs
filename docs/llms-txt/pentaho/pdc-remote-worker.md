# Source: https://docs.pentaho.com/pdc-use/pdc-remote-worker.md

# Remote Worker

The Remote Worker in Pentaho Data Catalog is a distributed component that facilitates metadata extraction, task execution, and data affinity management in environments where direct access to data sources might be restricted. It acts as an intermediary between the Data Catalog Ops Server and the data sources, enabling efficient metadata ingestion and task delegation.

The following table shows various scenarios, associated challenges, and how the Remote Worker addresses each challenge in Data Catalog:

| Scenario                                                                            | Challenge                                                                                         | How Remote Worker Helps                                                                                                                  |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Data is stored behind a firewall and cannot be accessed directly by Data Catalog.   | Data Catalog Ops Server cannot directly access data sources due to network security restrictions. | Remote Worker is deployed within the firewall, allowing metadata extraction and task execution without exposing the database externally. |
| Metadata extraction is slow due to network latency when accessing remote databases. | Query execution over long distances causes delays and inefficiencies.                             | Remote Worker executes queries locally and only transmits metadata to Data Catalog, reducing latency and improving response time.        |
| Multiple data centers exist, and tasks must be assigned efficiently.                | Ensuring tasks are routed to the correct data center for execution.                               | Affinity-based task assignment ensures tasks are handled by the nearest available Remote Worker, optimizing processing.                  |
| Security policies restrict direct database access from the Data Catalog Ops Server. | Database access credentials and network policies prevent external access.                         | Remote Worker operates within secure network boundaries, eliminating the need for external database access from Data Catalog Ops Server. |
| Large-scale metadata ingestion is required across multiple data sources.            | Managing high-volume metadata extraction without overloading central resources.                   | Distributed Remote Workers process metadata ingestion in parallel, ensuring scalability and load balancing.                              |
| Task execution should be resilient and monitored for failures.                      | Detecting failed tasks and reassigning them without manual intervention.                          | Heartbeat mechanism and monitoring allow Data Catalog to detect failed tasks and automatically reassign them to an active Remote Worker. |

For instructions on installing and configuring a Remote Worker, see the [Broken link](https://docs.pentaho.com/pdc-use/broken-reference "mention") topic in the [Get started with Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/uhk9gkhnIr3lLhiJ0Ubq/) document.

## Key benefits of a Remote Worker

The Remote Worker gives several advantages that enhance the functionality and performance of Data Catalog.

* **Security**: Works within the organization's security boundaries, eliminating the need for direct database exposure.
* **Scalability**: Supports multiple workers across different data centers to parallelize metadata extraction.
* **Efficient metadata extraction**: Collects metadata from data sources and transfers only essential information, reducing network overhead.
* **Firewall compatibility**: Functions seamlessly in environments where direct database access is restricted, making it ideal for enterprise deployments.
* **Automated task execution**: Manages test connections, metadata ingestion, and job execution to ensure efficient processing and performance.

## How Remote Worker works within Data Catalog

The Remote Worker is deployed near the data sources using a Dockerized approach to ensure easy scalability and seamless integration with existing infrastructure. It is configured to connect with the Ops Server for task assignments and with a centralized MongoDB database for logging and storing metadata.

Each Remote Worker is assigned an affinity, which defines the specific data sources it can access. When a user begins a task, such as metadata ingestion or a test connection, the system automatically assigns the task to the most suitable Remote Worker based on affinity, ensuring optimized processing and resource utilization.

When assigned a task, the Remote Worker executes it locally, extracting metadata from the designated data source and sending metadata and execution results back to the central Data Catalog system. This localized execution reduces network latency and enhances overall efficiency. The processing is optimized to minimize bandwidth usage, ensuring smooth metadata ingestion.

To ensure continuous availability and reliability, the Remote Worker maintains a heartbeat mechanism, regularly updating the Ops Server about its status. With this, the system can monitor active workers and reassign tasks if necessary. Users can track the worker status, task progress, and execution logs directly from the Workers section in Data Catalog, providing full transparency and control.
