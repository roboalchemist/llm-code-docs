## Eclipse Zenoh FAQ

Zenoh unifies data in motion, data at rest, and computations. It provides efficient pub/sub, geo-distributed storage, queries, and computations in a highly efficient manner. This FAQ covers essential questions developers might have when starting with Zenoh, categorized by key areas of interest.

## Getting Started

### What is zenoh and how does it compare to MQTT/DDS/Kafka/ROS2?
**Zenoh** focuses on unifying data in motion (pub/sub), data at rest (storage/query), and computations. Compared to **MQTT** or **Kafka**, zenoh offers a more comprehensive model by integrating pub/sub with distributed queries and storage. Unlike **DDS**, it is designed to efficiently handle both constrained environments and geo-distributed systems. Compared to **ROS2**, zenoh bridges connectivity across different domains, offering transparency and extensibility.

### How do I install zenoh?
You can install Zenoh following the [installation instructions](https://zenoh.io/docs/getting-started/installation/) on the official website. Zenoh can be built using cargo, the Rust package manager:  
```shell
cargo build --release
```
Ensure you have Rust installed and updated.

### What programming languages does zenoh support?
Zenoh primarily targets Rust but provides bindings for **C**, **C++**, **Python**, **Kotlin**, **Java**, and **TypeScript** through various projects.

### Do I need a broker/server to use zenoh?
No, Zenoh can operate in a peer-to-peer mode without a central broker, enabling decentralized communication. However, a Zenoh router daemon (`zenohd`) can be used to increase efficiency and support plugins for additional functionality.

### What's the difference between zenoh router, peer, and client mode?
- **Router**: Acts as a central node to route data between peers and optimize network use.
- **Peer**: Can communicate directly with other peers and can be configured dynamically for various roles.
- **Client**: Connects to peers or routers to interact within the Zenoh network but does not participate in routing decisions.

## Key Expressions and Selectors

### What is a key expression?
A **key expression** is a pattern used in Zenoh to identify resources. It supports hierarchical structures similar to directory paths.

### How do wildcards work? (*, **, $*)
- `*`: Matches any single segment of a path.
- `**`: Matches any number of segments, used for more extensive patterns.
- `$*`: Denotes a variable-length, zero-or-more-segment match with certain conditions.

### What's the difference between * and **?
`*` matches a single segment, while `**` matches multiple segments, including potential subdirectories.

### What is a Selector?
A **selector** is a key expression that selects resources for operations like querying or subscribing.

### How do key expression operators work (&, |)?
- `&` (AND): Combines expressions; matches resources that satisfy all sub-expressions.
- `|` (OR): Matches resources satisfying any of the sub-expressions.

## Pub/Sub

### How does pub/sub differ from traditional MQTT?
Zenoh’s pub/sub integrates with querying, allowing users to request data from storage in addition to live data streams, enhancing versatility.

### What is Locality filtering?
**Locality filtering** optimizes data delivery based on location (network proximity), reducing unnecessary data transmission.

### What are the priority levels and when do I use them?
Priority levels determine the order in which Zenoh processes messages, useful for prioritizing critical messages over routine data.

### What's the difference between BestEffort and Reliable?
- **BestEffort**: Data is sent without acknowledgment, potentially leading to loss under network issues.
- **Reliable**: Guarantees delivery with acknowledgment, retransmission on failure.

### What is CongestionControl and when does Drop vs Block matter?
**CongestionControl** manages data flow:
- **Drop**: Discards messages on overload.
- **Block**: Waits to send until system capacity stabilizes.

### How do I handle backpressure?
Handle backpressure by configuring publishers to either drop messages, block, or adjust sending rates based on network feedback.

## Query/Reply (Queryable)

### What is a Queryable and when do I use it instead of a subscriber?
A **Queryable** handles queries to provide requested historical data or computed results, perfect for retrieving stored data, whereas a subscriber receives current pub/sub messages.

### What is ConsolidationMode?
**ConsolidationMode** affects how responses are aggregated or processed, such as fetching only the latest data or compiling multiple responses.

### How does storage work with queries?
Zenoh queries utilize the distributed storage system to access or compute data on demand from various storage backends like databases or memory.

### What's the difference between a Querier and session.get()?
A **Querier** sets up a persistent querying entity, whereas `session.get()` is a one-time blocking or asynchronous query operation.

## Liveliness

### What is liveliness and when should I use it?
**Liveliness** ensures resources or communications remain active, useful in real-time applications to monitor system functionality.

### How is liveliness different from a regular pub/sub heartbeat?
Liveliness focuses on asserting the operational status of a resource, while a heartbeat is merely a routine status signal.

### How do I detect when a node leaves the network?
Configure liveliness detection mechanisms to pop alerts or handle network peer absence proactively.

## Performance

### How fast is zenoh? (throughput, latency numbers from blog posts)
Zenoh achieves high throughput exceeding 1Gbps with efficient use of small payloads (128 bytes) and low-latency communication even in constrained environments.

### When should I use shared memory?
Leverage shared memory in Zenoh for intra-node communication where extremely low latency is required. It is particularly useful in high-performance computing environments.

### How does zenoh compare to DDS performance?
Zenoh offers competitive performance advantages, especially in mixed data models and geo-distributed environments, with lower overheads than DDS.

### What configuration settings improve performance?
Tuning concurrency levels, transport selection, payload sizes, and message prioritization can have significant impacts on performance outcomes.

## Deployment

### When do I need a zenoh router vs just peers?
Use a **zenoh router** when you need to route data efficiently across complex network layouts or use extended functionalities via plugins.

### How does peer discovery work?
Zenoh leverages a scouting protocol to allow peers to discover each other without relying on multicast, depending on network topology.

### Can zenoh work over the internet (WAN)?
Yes, zenoh can manage cross-site communication with considerations for latency and bandwidth variations, making it suitable for WAN operations.

### How do I connect multiple sites?
Utilizing the routing and peer discovery features, you can bridge multiple geographical sites, creating a seamless Zenoh network.

## ROS 2

### How do I bridge ROS 2 topics over zenoh?
Use the Zenoh-ROS2 bridge to migrate topics between ROS 2 and Zenoh networks, facilitating data exchange in mixed environments.

### Does the bridge support services and actions?
Yes, the bridge supports not just topics but also ROS 2 services and actions to ensure full feature interoperability.

### How does zenoh compare to DDS for ROS 2?
Zenoh presents simpler integration for connectivity beyond DDS's capabilities, especially in resource-constrained or large-scale distributed systems.

### Can I have multiple robots in the same zenoh network?
Zenoh supports multi-robot networks efficiently, allowing several robots to operate and communicate concurrently within the same network space.

## Embedded / IoT

### What is zenoh-pico?
**Zenoh-pico** is a lightweight C implementation of the Zenoh protocol designed specifically for resource-constrained embedded systems and microcontrollers.

### Which microcontrollers does zenoh-pico support?
Zenoh-pico supports a broad range of microcontrollers compatible with C, leveraging the minimal resources they provide efficiently.

### How does zenoh-pico connect to a full zenoh network?
Zenoh-pico nodes connect as full participants in a zenoh network, enabling interaction with more capable devices seamlessly.

## Troubleshooting

### My publisher and subscriber aren't connecting — what's wrong?
Check your network configuration, ensure peer discovery/barriers are not impeding connections, review firewall rules, and validate application-level configurations.

### Scouting isn't finding other peers — how do I debug?
Verify network connectivity, review discovery settings in configuration files, and check for network policies that may restrict multicast or P2P traffic.

### Messages are being dropped — what should I check?
Review congestion control settings, ensure system resources are sufficient, and validate the configuration of reliability features to prevent drops.

### How do I enable logging/debugging?
Enable logging via Zenoh's configuration to tap into trace data, using verbosity settings to adjust the level of detail, assisting in in-depth diagnostics.