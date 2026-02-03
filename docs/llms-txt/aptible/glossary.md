# Source: https://www.aptible.com/docs/reference/glossary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Glossary

## Apps

On Aptible, an [app](/core-concepts/apps/overview) represents the deployment of your custom code. An app may consist of multiple Services, each running a unique command against a common codebase. Users may deploy Apps in one of 2 ways: via Dockerfile Deploy, in which you push a Git repository to Aptible and Aptible builds a Docker image on your behalf, or via Direct Docker Image Deploy, in which you deploy a Docker image you’ve built yourself outside of Aptible.

## App Endpoints

[App endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) are load balancers that allow you to expose your Aptible apps to the public internet or your stack’s internal network. Aptible supports three types of app endpoints - HTTP(s), TLS, and TCP.

## Container Recovery

[Container recovery](/core-concepts/architecture/containers/container-recovery) is an Aptible-automated operation that restarts containers that have exited unexpectedly, i.e., outside of a deploy or restart operation.

## Containers

Aptible deploys all resources in Docker [containers](/core-concepts/architecture/containers/overview). Containers provide a consistent and isolated environment for applications to run, ensuring that they behave predictably and consistently across different computing environments.

## CPU Allocation

[CPU Allocation](/core-concepts/scaling/cpu-isolation) is amount of isolated CPU threads allocated to a given container.

## CPU Limit

The [CPU Limit](/core-concepts/scaling/container-profiles) is a type of [metric](/core-concepts/observability/metrics/overview) that emits the max available CPU of an app or database. With metric drains, you can monitor and set up alerts for when an app or database is approaching the CPU Limit.

## Database Endpoints

[Database endpoints](/core-concepts/managed-databases/connecting-databases/database-endpoints) are load balancers that allow you to expose your Aptible databases to the public internet.

## Databases

Aptible manages and pre-configures [databases](/core-concepts/managed-databases/managing-databases/overview) that provide data persistence. Aptible supports many database types, including PostgreSQL, Redis, Elasticsearch, InfluxDB, MYSQL, and MongoDB.

Aptible pre-configures databases with convenient features like automatic backups and encryption. Aptible offers additional functionality that simplifies infrastructure management, such as easy scaling with flexible container profiles, highly available replicas by default, and modifiable backup retention policies. These features empower users to easily handle and optimize their infrastructure without complex setup or extensive technical expertise.

Additionally, Aptible databases are managed and monitored by the Aptible SRE Team – including responding to capacity alerts and performing maintenance.

## Drains

[Log drains](/core-concepts/observability/logs/log-drains/overview) and [metric drain](/core-concepts/observability/metrics/metrics-drains/overview) allow you to connect to destinations where you can send the logs and metrics Aptible provides for your containers for long-term storage and historical review.

## Environments

[Environments](/core-concepts/architecture/environments) provide logical isolation of a group of resources, such as production and development environments. Account and Environment owners can customize user permissions per environment to ensure least-privileged access. Aptible also provides activity reports for all the operations performed per environment. Additionally, database backup policies are set on the environment level and conveniently apply to all databases within that environment.

## High Availability

High availability is an Aptible-automated configuration that provides redundancy by automatically distributing apps and databases to multiple availability zones (AZs). Apps are automatically configured with high availability and automatic failover when horizontally scaled to two or more containers. Databases are automatically configured with high availability using [replication and clustering](/core-concepts/managed-databases/managing-databases/replication-clustering).

## Horizontal Scaling

[Horizontal Scaling](/core-concepts/scaling/app-scaling#horizontal-scaling) is a scaling operation that modifies the number of containers of an app or database. Users can horizontally scale Apps on demand. Databases can be horizontally scaled using replication and clustering. When apps and databases are horizontally scaled to 2 or more containers, Aptible automatically deploys the containers in a high-availability configuration.

## Logs

[Logs](/core-concepts/observability/logs/overview) are the output of all containers sent to `stdout` and `stderr`. Aptible does not capture logs sent to files, so when you deploy your apps on Aptible, you should ensure you are logging to `stdout` or `stderr` and not to log files.

## Memory Limit

The [Memory Limit](/core-concepts/scaling/memory-limits) is a type of [metric](/core-concepts/observability/metrics/overview) that emits the max available RAM of an app or database container. Aptible kicks off memory management when a container exceeds its memory limit.

## Memory Management

[Memory Management](/core-concepts/scaling/memory-limits) is an Aptible feature that kicks off a process that results in container recovery when containers exceed their allocated memory.

## Metrics

Aptible captures and provides [metrics](/core-concepts/observability/metrics/overview) for your app and database containers that can be accessed in the dashboard, for short-term review, or through metric drains, for long-term storage and historical review.

## Operations

An [operation](/core-concepts/architecture/operations) is performed and logged for all changes to resources, environments, and stacks. Aptible provides activity reports of all operations in a given environment and an activity feed for all active resources.

## Organization

An [organization](/core-concepts/security-compliance/access-permissions#organization) represents a unique account on Aptible consisting of users and resources. Users can belong to multiple organizations.

## PaaS

Platform as a Service (PaaS) is a cloud computing service model, as defined by the National Institute of Standards and Technology (NIST), that provides a platform allowing customers to develop, deploy, and manage applications without the complexities of building and maintaining the underlying infrastructure. PaaS offers a complete development and deployment environment in the cloud, enabling developers to focus solely on creating software applications while the PaaS provider takes care of the underlying hardware, operating systems, and networking. PaaS platforms also handle application deployment, scalability, load balancing, security, and compliance measures.

## Resources

Resources refer to anything users can provision, deprovision, or restart within an Aptible environment, such as apps, databases, endpoints, log drains, and metric drains.

## Services

[Services](/core-concepts/apps/deploying-apps/services) define how many containers Aptible will start for your app, what [container command](/core-concepts/architecture/containers/overview#container-command) they will run, their Memory Limits, and their CPU Isolation. An app can have many services, but each service belongs to a single app.

## Stacks

[Stacks](/core-concepts/architecture/stacks) represent the underlying infrastructure used to deploy your resources and are how you define the network isolation for an environment or a group of environments. There are two types of stacks to create environments within:

* Shared stacks: [Shared stacks](/core-concepts/architecture/stacks#shared-stacks) live on infrastructure that is shared among Aptible customers and are designed for deploying resources with lower requirements, such as deploying non-sensitive or test resources, and come with no additional costs.

* Dedicated stacks: [Dedicated stacks](/core-concepts/architecture/stacks#dedicated-stacks) live on isolated infrastructure and are designed to support deploying resources with higher requirements–such as network isolation, flexible scaling options, VPN and VPC peering, 99.95% uptime guarantee, access to additional regions and more. Users can use dedicated stacks for both `production` and `development` environments. Dedicated Stacks are available on Production and Enterprise plans at an additional fee per dedicated stack.

## Vertical Scaling

[Vertical Scaling](/core-concepts/scaling/app-scaling#vertical-scaling) is a type of scaling operation that modifies the size (including CPU and RAM) of app or database containers. Users can vertically scale their containers manually or automatically (BETA).
