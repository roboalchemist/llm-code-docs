# Source: https://www.aptible.com/docs/core-concepts/scaling/container-profiles.md

# Container Profiles

> Learn about using Container Profiles to optimize spend and performance

# Overview

<Info> CPU and RAM Optimized Container Profiles are only available on [Production and Enterprise plans.](https://www.aptible.com/pricing) </Info>

Container Profiles provide flexibility and cost-optimization by allowing users to select the workload-appropriate Profile. Aptible offers three Container Profiles with unique CPU-to-RAM ratios and sizes:

* **General Purpose:** The default Container Profile, which works well for most use cases.
* **CPU Optimized:** For CPU-constrained workloads, this Profile provides high-performance CPUs and more CPU per GB of RAM.
* **RAM Optimized:** For memory-constrained workloads, this Profile provides more RAM for each CPU allocated to the Container.

The General Purpose Container Profile is available by default on all [Stacks](/core-concepts/architecture/stacks). Whereas CPU and RAM Optimized Container Profiles are only available on [Dedicated Stacks.](/core-concepts/architecture/stacks#dedicated-stacks)

All new Apps & Databases are default created with the General Purpose Container Profile. This applies to [Database Backups](/core-concepts/managed-databases/managing-databases/database-backups) and [Database Replicas.](/core-concepts/managed-databases/managing-databases/replication-clustering)

# Specifications per Container Profile

| Container Profile | Default | Available Stacks   | CPU:RAM Ratio   | RAM per CPU | Container Sizes | Cost           |
| ----------------- | ------- | ------------------ | --------------- | ----------- | --------------- | -------------- |
| General Purpose   | ✔️      | Shared & Dedicated | 1/4 CPU:1GB RAM | 4GB/CPU     | 512MB-240GB     | \$0.08/GB/Hour |
| RAM Optimized     |         | Dedicated          | 1/8 CPU:1GB RAM | 8GB/CPU     | 4GB-752GB       | \$0.05/GB/Hour |
| CPU Optimized     |         | Dedicated          | 1/2 CPU:1GB RAM | 2GB/CPU     | 2GB-368GB       | \$0.10/GB/Hour |

# Supported Availability Zones

It is important to note that not all container profiles are available in every AZ, whether for app or database containers.
In the event that this occurs during a scaling operation:

* **App Containers:** Aptible will handle the migration of app containers to an AZ that supports the desired container
  profile seamlessly and with zero downtime, requiring no additional action from the user.
* **Database Containers:** However, for database containers, Aptible will prevent the scaling operation and log an error
  message, indicating that it is necessary to move the database to a new AZ that supports the desired container profile.
  This process requires a full disk backup and restore but can be easily accomplished using Aptible's 1-click "Database
  Restart + Backup + Restore.” It is important to note that this operation will result in longer downtime and completion
  time than typical scaling operations. For more information on resolving this error, including expected downtime, please
  refer to our troubleshooting guide.

# FAQ

<Accordion title="How do I modify the Container Profile for an App or Database?">
  Container Profiles can only be modified from the Aptible Dashboard when scaling the app/service or database.  The Container Profile will take effect upon restart.

    <img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Container-Profiles-2.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=b6916dae9f51cfcb9264970b2a25d467" alt="" data-og-width="2800" width="2800" data-og-height="2000" height="2000" data-path="images/Container-Profiles-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Container-Profiles-2.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=a9c13a3fb9e20f8da2e2a89cc93a5a17 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Container-Profiles-2.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=2b5637dfa031e391874bc7811ac6603a 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Container-Profiles-2.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=cf2bd019f3a7ae252d0164d497456d16 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Container-Profiles-2.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=731a93358d34741017e590f49e1ec377 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Container-Profiles-2.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=ab557b4f865270d8e047ba3132561b95 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/Container-Profiles-2.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=1ed8f636cb342225117c0a595e5c4409 2500w" />
</Accordion>
