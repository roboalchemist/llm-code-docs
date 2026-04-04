# Source: https://docs.zenml.io/user-guides/best-practices/choose-orchestration-environment.md

# Choosing an Orchestrator

When embarking on a machine learning project, one of the most critical early decisions is where to run your pipelines. This choice impacts development speed, costs, and the eventual path to production. In this post, we'll explore the most common environments for running initial ML experiments, helping you make an informed decision based on your specific needs.

### Local Environment

The local environment — your laptop or desktop computer - is where most ML projects begin their journey.

| <h4>Pros:</h4><ul><li><strong>Zero setup time</strong>: Start coding immediately without provisioning remote resources</li><li><strong>No costs</strong>: Uses hardware you already own</li><li><strong>Low latency</strong>: No network delays when working with data</li><li><strong>Works offline</strong>: Develop on planes, in cafes, or anywhere without internet</li><li><strong>Complete control</strong>: Easy access to logs, files, and debugging capabilities</li><li><strong>Simplicity</strong>: No need to interact with cloud configurations or container orchestration</li></ul> | <h4>Cons:</h4><ul><li><strong>Environment inconsistency</strong>: "Works on my machine" problems</li><li><strong>Limited resources</strong>: RAM, CPU, and GPU constraints</li><li><strong>Poor scalability</strong>: Difficult to process large datasets</li><li><strong>Limited parallelization</strong>: Running multiple experiments simultaneously is challenging</li></ul> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Ideal for:

* Quick proof-of-concepts with small datasets
* Early-stage algorithm development and debugging
* Small datasets, low compute requirements
* Small teams with standardized development environments
* Projects with minimal computational requirements

### Cloud VMs/Serverless Functions

When local resources become insufficient, cloud virtual machines (VMs) or serverless functions offer the next step up.

| <h4>Pros:</h4><ul><li><strong>Scalable resources</strong>: Access to powerful CPUs/GPUs as needed</li><li><strong>Pay-per-use</strong>: Only pay for what you consume</li><li><strong>Flexibility</strong>: Choose the right instance type for your workload</li><li><strong>No hardware management</strong>: Leave infrastructure concerns to the provider</li><li><strong>Easy snapshots</strong>: Create machine images to replicate environments</li><li><strong>Global accessibility</strong>: Access your work from anywhere</li></ul> | <h4>Cons:</h4><ul><li><strong>Costs can accumulate</strong>: Easy to forget running instances</li><li><strong>Setup complexity</strong>: Requires cloud provider knowledge (if not using ZenML)</li><li><strong>Security considerations</strong>: Data must leave your local network</li><li><strong>Dependency management</strong>: Need to configure environments properly</li><li><strong>Network dependency</strong>: Requires internet connection for access</li></ul> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Ideal for:

* Larger datasets that won't fit in local memory
* Projects requiring specific hardware (like GPUs)
* Teams working remotely across different locations
* Experiments that run for hours or days
* Projects transitioning from development to small-scale production

### Kubernetes

Kubernetes provides a platform for automating the deployment, scaling, and operations of application containers.

| <h4>Pros:</h4><ul><li><strong>Containerization</strong>: Ensures consistency across environments</li><li><strong>Resource optimization</strong>: Efficient allocation of compute resources</li><li><strong>Horizontal scaling</strong>: Easily scale out experiments across nodes</li><li><strong>Orchestration</strong>: Automated management of your workloads</li><li><strong>Reproducibility</strong>: Consistent environments for all team members</li><li><strong>Production readiness</strong>: Similar environment for both experiments and production</li></ul> | <h4>Cons:</h4><ul><li><strong>Steep learning curve</strong>: Requires Kubernetes expertise</li><li><strong>Complex setup</strong>: Significant initial configuration</li><li><strong>Overhead</strong>: May be overkill for simple experiments</li><li><strong>Resource consumption</strong>: Kubernetes itself consumes resources</li><li><strong>Maintenance burden</strong>: Requires ongoing cluster management</li></ul> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Ideal for:

* Teams already using Kubernetes for production
* Experiments that need to be distributed across machines
* Projects requiring strict environment isolation
* ML workflows that benefit from a microservices architecture
* Organizations with dedicated DevOps support

### Databricks

Databricks provides a unified analytics platform designed specifically for big data processing and machine learning.

| <h4>Pros:</h4><ul><li><strong>Optimized for Spark</strong>: Excellent for large-scale data processing</li><li><strong>Collaborative notebooks</strong>: Built-in collaboration features</li><li><strong>Managed infrastructure</strong>: Minimal setup required</li><li><strong>Integrated MLflow</strong>: Built-in experiment tracking</li><li><strong>Auto-scaling</strong>: Dynamically adjusts cluster size</li><li><strong>Delta Lake integration</strong>: Reliable data lake operations</li><li><strong>Enterprise security</strong>: Compliance and governance features</li></ul> | <h4>Cons:</h4><ul><li><strong>Cost</strong>: Typically more expensive than raw cloud resources</li><li><strong>Vendor lock-in</strong>: Some features are Databricks-specific</li><li><strong>Learning curve</strong>: New interface and workflows to learn</li><li><strong>Less flexibility</strong>: Some customizations are more difficult</li><li><strong>Not ideal for small data</strong>: Overhead for tiny datasets</li></ul> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Ideal for:

* Data science teams in large enterprises
* Projects involving both big data processing and ML
* Teams that need collaboration features built-in
* Organizations already using Spark
* Projects requiring end-to-end governance and security
