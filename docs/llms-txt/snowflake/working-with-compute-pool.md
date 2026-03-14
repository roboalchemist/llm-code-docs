# Source: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/working-with-compute-pool.md

# Snowpark Container Services: Working with compute pools

A compute pool is a collection of one or more virtual machine (VM) nodes
on which Snowflake runs your Snowpark Container Services services (including job services).
You create a compute pool using the [CREATE COMPUTE POOL](../../sql-reference/sql/create-compute-pool.md) command.
You then specify it when
[creating a service](../../sql-reference/sql/create-service.md) or [executing a job service](../../sql-reference/sql/execute-job-service.md).

## Creating a compute pool

A compute pool is an account-level construct, analogous to a Snowflake virtual
warehouse. The naming scope of the compute pool is your account.
That is, you cannot have multiple compute pools with the same name in your
account.

The minimum information required to create a compute pool includes the following:

* The machine type (referred to as the *instance family*) to provision for the compute pool nodes
* The minimum nodes to launch the compute pool with
* The maximum number of nodes the compute pool can scale to (Snowflake manages the scaling.)

If you expect a substantial load or sudden bursts of activity on the services you intend to run within your compute pool, you can set a minimum node count greater than 1. This approach ensures that additional nodes are readily available when needed, instead of waiting for autoscaling to start.

Setting a maximum node limit prevents an unexpectedly large number of nodes from being added to your compute pool by Snowflake autoscaling. This can be crucial in scenarios such as unexpected load spikes or issues in your code that might cause Snowflake to allocate a larger number of compute pool nodes than originally planned.

To create a compute pool using [Snowsight](../../user-guide/ui-snowsight-gs.md), or SQL:

Snowsight:
:   1. In the navigation menu, select Compute » Compute Pools.
    2. Select your username at the bottom of the navigation bar and switch to the ACCOUNTADMIN role, or any role that is allowed to create a compute pool.
    3. Select + Compute Pool.
    4. In the New compute pool UI, specify the required information (the compute pool name, the instance family, and the node limit).
    5. Select Create Compute Pool.

SQL:
:   Execute the [CREATE COMPUTE POOL](../../sql-reference/sql/create-compute-pool.md) command.

    For example, the following command creates a one-node compute pool:

    ```sqlexample
    CREATE COMPUTE POOL tutorial_compute_pool
      MIN_NODES = 1
      MAX_NODES = 1
      INSTANCE_FAMILY = CPU_X64_XS;
    ```

The instance family identifies the type of machine you want to provision
for compute pool nodes. Specifying instance family in
creating a compute pool is similar to specifying warehouse size
(XSMALL, SMALL, MEDIUM, LARGE and so on) when creating a warehouse. The following table lists the available machine types. You can also use the [SHOW COMPUTE POOL INSTANCE FAMILIES](../../sql-reference/sql/show-compute-pool-instance-families.md) command to get this list of available instance families.

### Compute pool placement

A *placement group* is a fault-isolation domain within a Snowflake region, similar to an availability zone (AZ) in AWS or Azure. You can optionally specify which placement group to provision compute pool nodes in by using the `placement_group` parameter in the [CREATE COMPUTE POOL](../../sql-reference/sql/create-compute-pool.md) statement.

If `placement_group` is not specified, Snowflake places compute pool nodes based on availability, which might span multiple placement groups.

If you choose to specify a `placement_group`, you have two options:

* **Specify a specific placement group:** When you specify `placement_group`, Snowflake provisions all nodes for that pool from the specified placement group. You should set `placement_group` to a specific placement group in the following situations:

  * You need reduced cross-node latency and lower communication costs for highly
    interactive, tightly coupled services.
  * You are building a highly available service and you choose to deploy the same code
    across multiple services, each one running on a separate compute pool that is assigned to a distinct placement group.

  The following guidelines apply when you set a specific placement group for a compute pool:

  * Instance family availability varies by placement group and region. Smaller regions might offer fewer placement group options,
    especially for GPU families. Call the
    [SYSTEM$GET_INSTANCE_FAMILY_PLACEMENT_GROUPS](../../sql-reference/functions/system_get_instance_family_placement_groups.md) system function to list the placement groups available for
    a specific instance family in your region.
  * Placement group names are consistent within an account across different instance families.
    Different Snowflake accounts might observe different names for the same underlying placement groups.
  * When you configure a placement group for a compute pool, it restricts Snowpark Container Services’ flexibility to
    optimize node placement. This restriction can increase the likelihood of insufficient-capacity errors and lengthen startup times
    during peak demand.
  * You can alter a placement group only if the compute pool is fully suspended and your services
    don’t use block storage.
* **Specify DISTRIBUTED:** When you set `placement_group` to DISTRIBUTED, Snowflake attempts to distribute nodes for that compute pool
  across all available placement groups. You should set `placement_group` to `DISTRIBUTED` if you want to maintain healthy fault tolerance across multiple placement groups. When compute pool nodes are distributed across multiple placement groups, if one placement group goes down, you don’t lose all the nodes

  The following behaviors apply when you set `placement_group` to DISTRIBUTED for a compute pool:

  * Node distribution: Snowflake uses an equal-partition strategy to spread nodes across all available placement groups in a region. If a
    specific placement group encounters insufficient capacity errors, nodes are provisioned in other placement groups with available capacity, which can result in an uneven distribution.
  * Service instances distribution: When there is more than one service instance, Snowflake attempts to evenly distribute the instances across placement groups.
    Sometimes even distribution can’t be achieved because of constraints, such as capacity limitations.
  * Outage behavior: In the current implementation, if a placement group fails, Snowflake doesn’t automatically fail over nodes to
    healthy placement groups. You should overprovision your service instances (N+1) so that nodes in the remaining placement groups can handle the traffic load during an outage. In the event of placement group outage, Snowflake takes the following actions:

    * Stops placing new service instances in the impacted placement group.
    * Routes ingress traffic to service instances in the healthy placement groups.
    * Recreates service instances in the impacted placement group on the healthy placement groups.

> **Note:**
>
> * In smaller Snowflake regions, some instance types might not be available across multiple placement groups, which can reduce the compute pool’s resilience to placement group failures.
> * After a placement group recovers, Snowflake doesn’t automatically move service instances back to it; the system gradually rebalances during node upgrades or routine service maintenance.

### Available instance families (machine types) for compute pool nodes

> | INSTANCE_FAMILY, see [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf) | vCPU | Memory (GiB) | Storage (GB) | Bandwidth limit (Gbps) | GPU | GPU Memory per GPU (GB) | Node limit | Description |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | CPU_X64_XS | 1 | 6 | 100 | Up to 12.5 | n/a | n/a | 150 | Smallest instance available for Snowpark Containers. Ideal for cost-savings and getting started. |
> | CPU_X64_S | 3 | 13 | 100 | Up to 12.5 | n/a | n/a | 150 | Ideal for hosting multiple services/jobs while saving cost. |
> | CPU_X64_M | 6 | 28 | 100 | Up to 12.5 | n/a | n/a | 150 | Ideal for having a full stack application or multiple services |
> | CPU_X64_SL (except China) | 14 | 54 | 100 | Up to 12.5 | n/a | n/a | 150 | For applications which need a large number of CPUs, memory and Storage. |
> | CPU_X64_L | 28 | 116 | 100 | 12.5 | n/a | n/a | 150 | For applications which need an unusually large number of CPUs, memory and Storage. |
> | HIGHMEM_X64_S | 6 | 58 | 100 | AWS and GCP: Up to 12.5, Azure: 8 | n/a | n/a | 150 | For memory intensive applications. |
> | HIGHMEM_X64_M | 28 | AWS: 240, Azure and GCP: 244 | 100 | AWS: 12.5, Azure and GCP: 16 | n/a | n/a | 150 | For hosting multiple memory intensive applications on a single machine. |
> | HIGHMEM_X64_SL (Azure and GCP, except GCP Dammam region) | 92 | 654 | 100 | 32 | n/a | n/a | 20 | Largest Azure or GCP high-memory machine available for processing large in-memory data. |
> | HIGHMEM_X64_L (AWS only) | 124 | 984 | 100 | 50 | n/a | n/a | 150 | Largest AWS high-memory machine available for processing large in-memory data. |
> | GPU_NV_S (AWS only, except Singapore, Switzerland North, Paris, and Osaka regions) | 6 | 27 | 300 (NVMe) | Up to 10 | 1 NVIDIA A10G | 24 | 150 | Our smallest NVIDIA GPU size available for Snowpark Containers to get started. |
> | GPU_NV_M (AWS only, except gov regions, Singapore, Switzerland North, Paris, and Osaka regions) | 44 | 178 | 3.4 TB (NVMe) | 40 | 4 NVIDIA A10G | 24 | 10 | Optimized for intensive GPU usage scenarios like Computer Vision or LLMs/VLMs. |
> | GPU_NV_L (AWS only, available only in AWS US West and US East non-gov regions by request; limited availability might be possible in other regions upon request) | 92 | 1112 | 6.8 TB (NVMe) | 400 | 8 NVIDIA A100 | 40 | On request | Largest GPU instance for specialized and advanced GPU cases like LLMs and Clustering, etc. |
> | GPU_NV_XS (Azure only, except Switzerland North, UAE North, Central US, and UK South regions) | 3 | 26 | 100 | 8 | 1 NVIDIA T4 | 16 | 10 | Our smallest Azure NVIDIA GPU size available for Snowpark Containers to get started. |
> | GPU_NV_SM (Azure only, except Central US region) | 32 | 424 | 100 | 40 | 1 NVIDIA A10 | 24 | 10 | A smaller Azure NVIDIA GPU size available for Snowpark Containers to get started. |
> | GPU_NV_2M (Azure only, except Central US region) | 68 | 858 | 100 | 80 | 2 NVIDIA A10 | 24 | 5 | Optimized for intensive GPU usage scenarios like Computer Vision or LLMs/VLMs. |
> | GPU_NV_3M (Azure only, except Central US, North Europe, and UAE North regions) | 44 | 424 | 100 | 40 | 2 NVIDIA A100 | 80 | On request | Optimized for memory-intensive GPU usage scenarios like Computer Vision or LLMs/VLMs. |
> | GPU_NV_SL (Azure only, except Central US, North Europe, and UAE North regions) | 92 | 858 | 100 | 80 | 4 NVIDIA A100 | 80 | On request | Largest GPU instance for specialized and advanced GPU cases like LLMs and Clustering, etc. |
> | GPU_GCP_NV_L4_1_24G (Google Cloud only) | 6 | 28 | 300 | Up to 16 | 1 NVIDIA L4 | 24 | 10 | Our smallest NVIDIA GPU size available for Snowpark Containers to get started. |
> | GPU_GCP_NV_L4_4_24G (Google Cloud only) | 44 | 178 | 1200 | Up to 50 | 4 NVIDIA L4 | 24 | 10 | GPU usage scenarios like Computer Vision or LLMs. |
> | GPU_GCP_NV_A100_8_40G (Google Cloud only, available only in GCP US Central1 and Europe West4 regions by request) | 92 | 654 | 2500 | Up to 100 | 8 NVIDIA A100 | 40 | On request | Optimized for memory-intensive GPU usage scenarios like Computer Vision or LLMs/VLMs. |

For information about available instance families, see
[CREATE COMPUTE POOL](../../sql-reference/sql/create-compute-pool.md).

### Autoscaling of compute pool nodes

After you create a compute pool, Snowflake launches the minimum number of nodes
and automatically creates additional nodes up to the maximum allowed. This is
called *autoscaling*. New nodes are allocated when the running nodes
cannot take any additional workload. For example,
suppose that two service instances are running on two nodes
within your compute pool. If you execute another service within
the same compute pool, the additional resource requirements might cause Snowflake to start an additional node.

However, if no services run on a node for a specific duration, Snowflake automatically removes the node, ensuring that the compute pool maintains the minimum required nodes even after the removal.

## Managing a compute pool

You can manage a compute pool using [Snowsight](../../user-guide/ui-snowsight-gs.md), or SQL.

In [Snowsight](../../user-guide/ui-snowsight-gs.md), you choose the more option (…) next to the compute pool name, and choose the desired operation from the menu. The section explains SQL commands you can use to manage a compute pool.

Snowpark Container Services provides the following commands to manage compute pools:

* **Monitoring:** Use the [SHOW COMPUTE POOLS](../../sql-reference/sql/show-compute-pools.md) command to get information about compute pools.
* **Operating:** Use the [ALTER COMPUTE POOL](../../sql-reference/sql/alter-compute-pool.md) command to change the state of a compute pool.

  ```sqlexample
  ALTER COMPUTE POOL <name> { SUSPEND | RESUME | STOP ALL }
  ```

  When you suspend a compute pool, Snowflake suspends all services except the job services. The job services continue to run until they reach a terminal state
  (DONE or FAILED), after which the compute pool nodes are released.

  A suspended compute pool must be resumed before you can start a new service. If the compute pool is configured to auto-resume
  (with the AUTO_RESUME property set to TRUE), Snowflake automatically resumes the pool when a service is submitted to it. Otherwise, you
  need to run the ALTER COMPUTE POOL command to manually resume the compute pool.
* **Modifying:** Use the [ALTER COMPUTE POOL](../../sql-reference/sql/alter-compute-pool.md) command to change compute pool properties.

  ```sqlexample
  ALTER COMPUTE POOL <name> SET propertiesToAlter = <value>
  propertiesToAlter := { MIN_NODES | MAX_NODES | AUTO_RESUME | AUTO_SUSPEND_SECS | PLACEMENT_GROUP | INSTANCE_FAMILY | TAG | COMMENT }
  ```

  When you decrease MAX_NODES, note the following potential effects:

  * Snowflake might need to terminate one or more service instances and restart them on other available nodes in the compute pool. If
    MAX_NODES is set too low, Snowflake might be unable to schedule certain service instances.
  * If the node terminated had a job service execution in progress, the job execution will fail. Snowflake will not restart the job service.

    **Example:**

    > ```sqlexample
    > ALTER COMPUTE POOL my_pool SET MIN_NODES = 2  MAX_NODES = 2;
    > ```
>
* **Removing:** Use the [DROP COMPUTE POOL](../../sql-reference/sql/drop-compute-pool.md) command to remove a compute pool.

  > **Example:**
  >
  > > ```sqlexample
  > > DROP COMPUTE POOL <name>
  > > ```
  > >
  > > You must stop all running services before you can drop a compute pool.
* **Listing compute pools and viewing properties:** Use SHOW COMPUTE POOLS and DESCRIBE COMPUTE POOL commands. For examples, see [Show Compute Pools](../../sql-reference/sql/show-compute-pools.md).

### About the target_nodes compute pool property

This section explains the `target_nodes` property with examples. The `target_nodes` property indicates the number of nodes that Snowflake is targeting for your compute pool. If `active_nodes` isn’t equal to the `target_nodes`, Snowflake autoscales the cluster
to add or remove the nodes.

There are several properties related to the number of nodes in a compute pool. These includes: `min_nodes`, `max_nodes`, `active_nodes`, `idle_nodes`, and `target_nodes`. For more information about these properties, see [DESC COMPUTE POOL](../../sql-reference/sql/desc-compute-pool.md) and [SHOW COMPUTE POOLS](../../sql-reference/sql/show-compute-pools.md).

The following examples demonstrate how to interpret the values in the `target_nodes` column.

#### Example 1

Suppose in a [CREATE COMPUTE POOL](../../sql-reference/sql/create-compute-pool.md) command, you specify MIN_NODES=1 and MAX_NODES=3.

While Snowflake is provisioning a node, initially the value in the `active_nodes` and `idle_nodes` columns is 0, and the value in the `target_nodes` column is 1. (The value in the `target_nodes` column is the same as the value that you specified for the MIN_NODES parameter.) This indicates that there should be one node in the compute pool that Snowflake is provisioning.

After Snowflake provisions one node, the value in the `idle_nodes` column is 1 (assuming that there are no services running). The value in the `target_nodes` column is still 1, indicating there should be one node in the compute pool.

#### Example 2

Snowflake might try to add a node to an existing compute pool due to autoscaling or changes to the minimum number of nodes (through [ALTER COMPUTE POOL … SET MIN_NODES](../../sql-reference/sql/alter-compute-pool.md)).

While Snowflake is provisioning a node, the value in the `state` column is `resizing`. To determine how many nodes Snowflake is adding, check the value in the `target_nodes` column.

For example, suppose that the value in the, `active_nodes` column is 1, the value in the `idle_nodes` column is 0, and you resize the compute pool by updating the MIN_NODES property from 1 to 2. In this case, the value in the `target_nodes` column is 2 (the number of nodes that should be in the compute pool). From this, you can infer that Snowflake is provisioning one additional node.

## Compute pool lifecycle

A compute pool can be in any of the following states:

* **IDLE:** The compute pool has the desired number of virtual machine (VM) nodes, but no
  services are scheduled. In this state, autoscaling can shrink the
  compute pool to the minimum size due to lack of activity.
* **ACTIVE:** The compute pool has at least one service running or
  scheduled to run on it. The pool can grow (up to the maximum nodes) or
  shrink (down to the minimum nodes) in response to load or user actions.
* **SUSPENDED:** The pool currently contains no running virtual machine nodes, but if the AUTO_RESUME compute pool property is set to TRUE, the pool will automatically resume when a service is scheduled.

The following states are transient:

* **STARTING:** When you create or resume a compute pool, the compute pool enters the STARTING state until at least one node is provisioned.
* **STOPPING:** When you suspend a compute pool (using ALTER COMPUTE POOL), the compute pool enters the STOPPING state until Snowflake has released all nodes in the compute pool. When you suspend a compute pool, Snowflake suspends all services except the job services. The job services continue to run until they reach a terminal state (DONE or FAILED), after which the compute pool nodes are released.
* **RESIZING:** When you create a compute pool, initially it enters the STARTING state. After it has one node provisioned, it enters the RESIZING state until the minimum number of nodes (as specified in CREATE COMPUTE POOL) are provisioned. When you change a compute pool (ALTER COMPUTE POOL) and update the minimum and maximum node values, the pool enters the RESIZING state until the minimum nodes are provisioned. Note that autoscaling of a compute pool also puts the compute pool in the RESIZING state.

For information about how the costs incurred during the different states of the compute pool lifecycle, see [Compute pool cost](accounts-orgs-usage-views.md).

## Compute pool privileges

When you work with compute pools, the following privilege model applies:

* To create a compute pool in an account, the current role needs the
  CREATE COMPUTE POOL privilege on the account. If you create a pool, as an owner you have OWNERSHIP permission, which grants full control over that compute pool. Having OWNERSHIP of one compute pool doesn’t imply any permissions on other compute pools.
* For compute pool management, the following privileges (capabilities)
  are supported:

  | Privilege | Usage |
  | --- | --- |
  | MODIFY | Enables altering any compute pool properties, including changing the size. |
  | MONITOR | Enables viewing compute pool usage, including describing compute pool properties. Enables access to the monitoring endpoint exposed by the compute pool. |
  | OPERATE | Enables changing the state of the compute pool (suspend, resume). In addition, enables stopping any scheduled services (including job services). |
  | USAGE | Enables creating services in the compute pool. Note that when a compute pool is in a suspended state and has its AUTO_RESUME property set to true, a role with USAGE permission on the compute pool can implicitly trigger the compute pool’s resumption when they start or resume a service, even if the role lacks the OPERATE permission. |
  | OWNERSHIP | Grants full control over the compute pool. Only a single role can hold this privilege on a specific object at a time. Enables access to the monitoring endpoint exposed by the compute pool. |
  | ALL [ PRIVILEGES ] | Grants all privileges, except OWNERSHIP, on the compute pool. |

## Compute pool maintenance

As part of routine internal-infrastructure maintenance, Snowflake regularly updates
compute pool nodes to ensure optimal performance and security. This includes
operating system upgrades, driver enhancements, and security fixes. Maintenance
involves replacing outdated nodes with updated ones every few weeks, with each
node active for up to a month.

### Maintenance window

In general, scheduled maintenance occurs every Saturday from 8 PM to Sunday at 8 AM, and every Sunday from 8 PM to Monday at 8 AM. For [early access accounts](../../user-guide/intro-releases.md), maintenance takes place daily starting at 11 PM and can last up to 6 hours.

### Service disruption

During maintenance, Snowflake automatically recreates service instances running on older compute pool nodes on the new nodes. Snowflake uses a rolling method to recreate service instances.

* If a service only has one instance, service disruption occurs while Snowflake is recreating the instance.
* For services with multiple instances, Snowflake recreates the service instances incrementally on the upgraded nodes. No more than 50
  percent of the service instances are replaced at a time. Note that this might lead to fewer available instances than the MIN_INSTANCES
  requested for the service. If the available instances drop to fewer than MIN_READY_INSTANCES, it causes the service to transition from
  the READY state to the PENDING state, causing service disruption. Therefore, to avoid service disruption, consider setting
  MIN_READY_INSTANCES to less than 50 percent of MIN_INSTANCES.

Ongoing job services will be disrupted and must be restarted by customers after maintenance is complete.

> **Attention:**
>
> Service disruptions during a maintenance window or critical updates are not covered by the Service Level set forth in [Snowflake’s Support Policy and Service Level Agreement](https://www.snowflake.com/legal/support-policy-and-service-level-agreement/).

### Best practices to minimize downtime

* **Run multiple service instances:** Having multiple instances minimizes service disruption during maintenance, ensuring high availability.
* **Store application state in persistent storage:** Store data and stateful objects on persistent storage including block storage, Snowflake stages, or Snowflake tables.
* **Catch the SIGTERM signal:** When terminating a service instance, Snowflake first sends a SIGTERM signal to each service container (see [Terminate service](working-with-services.md)). As part of processing the signal, the container code can save the service state before the service instance is shut down or restarted.
* **Design high availability services to run in degraded state during maintenance:** To remain available during maintenance, your service must be tolerant to running with only 50% of the instances.
* **Provide a readiness probe:** If you don’t provide a readiness probe, Snowflake assumes your service instance is ready as soon as the code starts executing. Typically it takes some time for a container to complete initialization and be ready to handle requests. You should provide a readiness probe in the service configuration to explicitly tell Snowflake when your service instance is ready to handle requests.
* **Monitor maintenance schedules:** Avoid scheduling critical tasks during a maintenance window.
* **Avoid scheduling job Service to run during maintenance windows:** Snowflake might cancel a running job during a maintenance window.
* **Perform regular backups or checkpoints:** Periodically back up or checkpoint your application state on persistent storage (including block storage, Snowflake stages, or Snowflake tables).

## How services are scheduled on a compute pool

At the time of [creating a service](../../sql-reference/sql/create-service.md), you might choose to run multiple instances to manage incoming load.
Snowflake uses the following general guidelines when scheduling your service
instances on compute pool nodes:

* All containers in a service instance always run on a single compute pool node.
  That is, a service instance never spans across multiple nodes.
* When you run multiple service instances,
  Snowflake may run these service instances on the same node or different
  nodes within the compute pool. When making this decision, Snowflake considers any specified hard
  resource requirements (such as memory and GPU) as outlined in the
  service specification file (see [containers.resources field](specification-reference.md)).

  For example, suppose each node in your compute pool provides 8 GB of memory.
  If your service specification includes a 6-GB memory requirement, and
  you choose to run two instances when creating a service,
  Snowflake cannot run both instances on the same node. In this case,
  Snowflake schedules each instance on a separate node within the compute pool to fulfill
  the memory requirements.

> **Note:**
>
> Snowflake supports stage mounts for use by application containers. Snowflake internal stage is one of the supported storage volume types.
>
> For optimal performance, Snowflake now limits the total number of [stage volume](snowflake-stage-volume.md) mounts to eight per compute pool node, regardless of whether these volumes belong to the same service instance, the same service, or different services.
>
> When the limit on a node is reached, Snowflake doesn’t use that node to start new service instances that use a stage volume. If the limit is reached on all nodes in the compute pool, Snowflake will be unable to start your service instance. In this scenario, when you execute the SHOW SERVICE CONTAINERS IN SERVICE command, Snowflake returns PENDING status with the “Unschedulable due to insufficient resources” message.
>
> To accommodate this stage mount allotment limit on a node, in some cases, you can increase the maximum number of nodes that you request for a compute pool. This ensures that additional nodes are available for Snowflake to start your service instances.

## System compute pools

Snowflake automatically provisions two compute pools in each Snowflake account. These compute pools are provided exclusively for the following Snowflake workloads.

* Notebooks
* Model serving
* ML jobs

By using system compute pools, users can run these workload without needing an account administrator to configure a compute pool first.

The system compute pools have the following default configuration:

* **Compute pool name:** SYSTEM_COMPUTE_POOL_GPU

  * **Instance family:** Depending on whether your Snowflake account is in AWS or Microsoft Azure regions, Snowflake uses the following GPU instance family for this compute pool.

    * In Azure, GPU_NV_SM.
    * In AWS, GPU_NV_S.

    Note that, the following regions do not support SYSTEM_COMPUTE_POOL_GPU:

    * In AWS: Singapore, Switzerland North, Paris, and Osaka.
    * In Azure: Central US.
    * Google Cloud: GPU compute pool isn’t available.
  * **Default configuration:**

    * MIN_NODES=1
    * MAX_NODES=50
    * INITIALLY_SUSPENDED=true
    * AUTO_SUSPEND_SECS=600
* **Compute pool name:** SYSTEM_COMPUTE_POOL_CPU

  * **Instance family:** CPU_X64_S
  * **Default configuration:**

    * MIN_NODES=1
    * MAX_NODES=150
    * INITIALLY_SUSPENDED=true
    * AUTO_SUSPEND_SECS=600

Note that,

* Compute pools are initially in a suspended state and only begin incurring costs when a supported Snowflake workload starts using them.
* If no workloads are running, these compute pools are automatically suspended after 10 minutes. To modify the auto-suspension policy for default compute pools, use the [ALTER COMPUTE POOL SET AUTO_SUSPEND_SECS](../../sql-reference/sql/alter-compute-pool.md) command.

### Managing the system compute pools

In a Snowflake account, the ACCOUNTADMIN role owns these system compute pools. Administrators have full control over the compute pools, including modifying their properties, suspending operations, and monitoring consumption. The ACCOUNTADMIN role can delete the compute pool. For example:

```sqlexample
USE ROLE ACCOUNTADMIN;
ALTER COMPUTE POOL SYSTEM_COMPUTE_POOL_CPU STOP ALL;
DROP COMPUTE POOL SYSTEM_COMPUTE_POOL_CPU;
```

By default, the USAGE permission on system compute pools is granted to the PUBLIC role, allowing all roles in the account to use them. However, the ACCOUNTADMIN can modify these privileges to restrict access if necessary.

To restrict access to system compute pools to specific roles in your account, use the ACCOUNTADMIN role to revoke the USAGE permission from the PUBLIC role and grant it to the desired role(s). For example:

> ```sqlexample
> USE ROLE ACCOUNTADMIN;
> REVOKE USAGE ON COMPUTE POOL SYSTEM_COMPUTE_POOL_CPU FROM ROLE PUBLIC;
> GRANT USAGE ON COMPUTE POOL SYSTEM_COMPUTE_POOL_CPU TO ROLE <role-name>;
> ```

System compute pools can be associated with [budgets](../../user-guide/budgets.md). for cost management.

### Configuring your own preferred compute pools for Notebooks

By default, Notebook services run in system compute pools. If you don’t want to use the Snowflake-provisioned compute pools, you have the option to choose other compute pools in your account for Notebooks. To override the Snowflake-provisioned compute pools you can set these parameters ([DEFAULT_NOTEBOOK_COMPUTE_POOL_CPU](../../sql-reference/parameters.md) and [DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU](../../sql-reference/parameters.md)). Note that, this will change your Snowsight experience. When creating a Notebook in Snowsight, the compute pool you configure using these parameters appears as the first preference in the UI. The following example commands set these parameters:

* Configure `my_pool` as the account-level compute pool preferred for Notebooks using GPU runtime.

  ```sqlexample
  ALTER ACCOUNT SET DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU='my_pool';
  ```

* Configure `my_pool` as the compute pool preferred for Notebooks created in the database `my_db`.

  ```sqlexample
  ALTER DATABASE my_db SET DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU='my_pool';
  ```

* Configure `my_pool` as the compute pool preferred for Notebooks created in the schema `my_db.my_schema`.

  > ```sqlexample
  > ALTER SCHEMA my_db.my_schema SET DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU='my_pool';
  > ```

Use the following commands to check the current GPU compute pool preference configured in your account to run Notebooks:

```sqlexample
SHOW PARAMETERS LIKE 'DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU' IN ACCOUNT;

SHOW PARAMETERS LIKE 'DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU' IN DATABASE my_db;

SHOW PARAMETERS LIKE 'DEFAULT_NOTEBOOK_COMPUTE_POOL_GPU' IN SCHEMA my_db.my_schema;
```

For more information, see [SHOW PARAMETERS](../../sql-reference/sql/show-parameters.md).

## Guidelines and limitations

* **CREATE COMPUTE POOL permission:** If you cannot create a compute pool under the current role,
  consult your account administrator to grant permission. For example:

  ```sqlexample
  GRANT CREATE COMPUTE POOL ON ACCOUNT TO ROLE <role_name> [WITH GRANT OPTION];
  ```

  For more information, see [GRANT <privileges> … TO ROLE](../../sql-reference/sql/grant-privilege.md).
* **Per account limit on compute pool nodes**.

  * The maximum number of nodes you can create in your account (regardless of the number of compute pools) is 500.
  * The maximum number of nodes per compute pool is 50.

  In addition, there is a limit on the number of nodes allowed for each instance family (see the **Node limit** column in the instance family table). If you see an error message like `Requested number of nodes <#> exceeds the node limit for the account`, you have encountered these limits. For more information, contact your account representative.
