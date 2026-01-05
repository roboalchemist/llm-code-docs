# Source: https://docs.velodb.io/cloud/4.x/management-guide/cluster-management

Version: 4.x

On this page

# Cluster Management

In each paid warehouse, you can create multiple clusters to support different
workloads, such as writing data, customer-facing reporting, user profiles, and
behavior analytics.

The cluster only contain compute resource, cache resource and cached data. All
clusters in the warehouse share the stored data.

## New Cluster​

To create a new cluster in a paid warehouse, you can click **Clusters** on the
navigation bar.

If a cluster already exists, you will see the **Cluster Overview** page.

![cluster list existing](/assets/images/cluster-list-
existing-2d9d00a1d4eeb41bf33100aba6983194.png)

Click **New Cluster** on the wizard page or **Cluster Overview** page to
create a new cluster.

![create_cluster](/assets/images/create-cluster-
fdda47a3ec19565f7dab70360bf89667.png)

**Parameter** | **Description**|  Cluster Name| Required. Must start with a letter, up to 32 characters, you can use letters (case insensitive), numbers and _.| Compute| Default is minimum 4 vCPU, maximum 1024 vCPU per cluster, if you need a higher quota, please [get help](mailto:support@velodb.io) to apply. Currently, the ratio of vCPU to memory is fixed at 1:8.| Cache| The upper and lower limits of the cache space will vary depending on the compute size.| Storage| Pay as you go, no need to preset storage space. All clusters in the warehouse share the stored data.| Billing Method| Default is **On-Demand (Hourly)** billing, suitable for scenarios that need to be flexibly changed or deleted at any time, such as temporary test verification.| Auto Pause/Resume| When enabled, the compute cluster will automatically pause after a period of inactivity. It will automatically resume upon a new query request.  
---|---  
  
Creating a new cluster will incur a charge. Therefore, before creation, please
ensure sufficient available amount or open and enable the cloud marketplace
deduction channel. Otherwise, you will see the following error prompt.

![insufficient cash-balance](/assets/images/insufficient-cash-
balance-a173fc56f41649ad5bc6f813c36eb480.png)

> **Note**
>
>   * After confirming the creation, you can see the new cluster on the
> **Cluster overview** page. It takes about 3 minutes to complete the
> creation, and the cluster status will be changed from "**Creating** " to
> "**Running** ".
>   * The SaaS model free trial clusters do not support new cluster creation.
>

## Reboot Cluster​

In certain situations (such as cluster exceptions or modification of certain
parameters), you may need to reboot the cluster. On the **Cluster Overview**
page, find the target cluster card, click **Reboot** operation, and confirm
again. The cluster status will be changed to "**Rebooting** ", and no other
operations can be performed on the cluster at this status.

![cluster rebooting](/assets/images/cluster-rebooting-
en-a729a4a2e55fc2603b10261f34c08b3f.png)

> **Note**
>
>   * It takes about 3 minutes for the cluster to reboot. When it is done, the
> cluster status will be changed from "**Rebooting** " to "**Running** ".
>   * The rebooting of cluster may cause business requests to experience
> crashes or delayed responses.
>   * During the cluster rebooting process, VeloDB Cloud will still meter and
> charge the cluster.
>

## Pause/Resume Cluster​

### Manual Pause/Resume Cluster​

You may wish to save costs when the cluster is idle. On the **Cluster
Overview** page, find the target cluster card. When the cluster status is
"**Running** " and it is confirmed that the cluster is unloaded, you can
manually pause the cluster, click **Pause** operation and confirm again. The
cluster status will be changed to "**Pausing** ", and no other operations can
be performed on the cluster at this time. VeloDB Cloud will release the
computing resource of the cluster while retaining the cache space and its
data.

![cluster pausing](/assets/images/cluster-pausing-
en-3f7440c003695f4f90659947221cb39c.png)  
![cluster paused](/assets/images/cluster-paused-
en-27e7474bb39d489dc1ed92b5fcc11ed2.png)

> **Note**
>
>   * It takes about 3 minutes for the cluster to pause. When it is done, the
> cluster status will be changed from "**Pausing** " to "**Paused** ".
>   * The cluster will not respond to business requests during the pause
> period.
>   * During the cluster suspension period, VeloDB Cloud will no longer meter
> and charge for computing resource, but will still meter and charge for cache
> space.
>   * Clusters containing monthly/yearly billing resources do not support the
> pause/resume function.
>

When you need the cluster to continue responding to business requests, you can
manually resume the "**paused** " cluster. On the **Cluster Overview** page,
find the target cluster card, click **Resume** operation and confirm again.
The cluster status will be changed to "**Resuming** ", and no other operations
can be performed on the cluster at this status. VeloDB Cloud will pull up
computing resource and mount the reserved cache space and its data.

![cluster resuming](/assets/images/cluster-resuming-
en-d84b09981edbf0147fa70031b091a7b2.png)  
![cluster running](/assets/images/cluster-running-
en-93a53c5f3f329474bf025b4f3e87e67f.png)

> **Note**
>
>   * It takes about 3 minutes for the cluster to resume. When it is done, the
> cluster status will be changed from "**Resuming** " to "**Running** ".
>   * The cluster will not respond to business requests during the resuming
> process.
>   * After the cluster is resumed, it can respond to business requests, and
> VeloDB Cloud will restore metering and billing for the pulled up computing
> resource.
>   * Clusters containing monthly/yearly billing resources do not support the
> pause/resume function.
>

### Auto Pause/Resume Cluster​

If you want to automatically start and stop idle clusters, you can click **Set
Auto Start/Stop** to the right of **Started On** or in the upper right corner
on the **Cluster Details** page, and turn on the **Auto Start/Stop** switch to
customize the idle duration of the shutdown trigger condition.

![cluster-auto-stop-start_en](/assets/images/cluster-auto-stop-start-
en-3098e717998861a4e7853fa534564964.png)

## Cluster Details​

Before performing any operation on a cluster, you may need to first know the
detailed information of the cluster. On the **Cluster Overview** page, find
the target cluster card, and if the cluster status supports, click on the
cluster card to enter the **Cluster Details** page.

![cluster-detail-CPU-arch-en](/assets/images/cluster-detail-CPU-arch-
en-d0ab3caebc2428a5d157daa391c05263.png)

The **Cluster Details** page includes two main content areas: basic
information and on-demand billing resources, as well as corresponding
functional operations. The specific explanation is as follows: **Basic
Information** :

**Parameter** | **Description**|  Cluster ID| The globally unique ID of the cluster. Start with "c-", followed by 18 characters, randomly combined with 26 lowercase letters and 10 numbers.| Cluster Name| It is unique in a warehouse, and supporting one click copying and locally renaming. If you need to modify the cluster name, click the edit icon, enter the new cluster name in the input box that appears (it is recommended that the name should indicate the meaning), click the confirm icon and confirm again.  
**Note**  
\- The VeloDB Core syntax will use the cluster name, for example:  
`USE { [catalog_name.]database_name[@cluster_name] }`  
\- The cluster name must start with a letter, up to 32 characters, you can use
letters (case insensitive), numbers and _.  
\- After modifying the cluster name, it is necessary to ensure that the
business uses the new cluster name or sets the default cluster for the
relevant database users, otherwise it will cause the relevant requests to
fail.| Created By| The user who created the cluster. Multiple users in the
same organization can perform corresponding operations on warehouses and their
clusters according to their privileges.| Created At| The time when the cluster
was created.| Started At| The time when the cluster was last rebooted or
resumed.| Running Time| The running time of the cluster since it was last
rebooted or resumed.| Zone| The availability zone where the cluster is
located.| CPU Architecture| The CPU architecture of cluster computing
resource.  
**Note**  
\- Currently, only VeloDB Cloud warehouses deployed on AWS can see the CPU
architecture of the cluster, which may be x86 or ARM.  
\- Core version 4.0.4 or above is required to create an ARM architecture
cluster. If the core version is too low, please upgrade the core version.  
\- On the same specifications, ARM architecture has a performance improvement
of over 30% compared to x86 architecture.  
\- In the SaaS model, the pricing of cluster computing resources for ARM
architecture and x86 architecture is consistent in the same cloud platform and
region. In the BYOC model, the pricing of computing resources for different
CPU architectures may vary within the same cloud platform and region,
depending on the cloud provider.  
\- It cannot be modified after the cluster is created.| **On-Demand
Resources** :|  
---|---  
**Parameter** | **Description**|  Compute| Displays the current compute resource of the cluster.| Cache| Displays the current cache space of the cluster.| Scale Out/In| If the performance of the current cluster does not meet the business requirements, you can increase or decrease compute resource or cache space to adjust the capacity of the current cluster by clicking **Scale Out/In**.  
---|---  
  
## Scale Cluster​

### Manual Scaling​

Based on your business requirements, you can click **Scale Out/In** in the
upper right corner on the **On-Demand Resources** content area of the
**Cluster Details** page, and select **Manual Scaling** to adjust the capacity
of the current cluster.

![cluster scaling manual en](/assets/images/cluster-scaling-manual-
en-8d7009c8374a257ad01053374d906e42.png)

> **Note**
>
>   * After confirming the scaling, you can see the cluster status be changed
> from "**Running** " to "**Scaling** " on the **Cluster Overview** page. It
> takes about 3 minutes to complete the scaling, and the cluster status will
> be changed from "**Scaling** " to "**Running** ".
>   * The SaaS free trial clusters do not support scaling.
>

### Time-based Scaling​

If the cluster needs to deal with periodic business peaks and lows, you can
click **Scale Out/In** in the upper right corner on the **On-Demand
Resources** content area of the **Cluster Details** page, and select **Time-
based scaling** , customize and add at least two different target vCPU time-
based rules, and enable time-based scaling policy.

![cluster scaling time based en](/assets/images/cluster-scaling-time-based-
en-3f994662caceeb78e1b5e67b94a8483c.png)

> **Note**
>
>   * The SaaS free trial clusters do not support scaling.
>   * The on-demand billing cluster does not support configuring a time-based
> rule with a target vCPU of 0.
>   * The time-based rule is valid and executed when the cluster is running
> normally. When the cluster is not running normally (such as pausing,
> rebooting, upgrading, etc.), it will wait for a retry, and will not be
> executed after more than 30 minutes.
>   * If the current organization does not have sufficient available amount or
> open and enable the cloud marketplace deduction channel, the time-based rule
> will be considered invalid and abandoned by VeloDB Cloud.
>   * The execution period of the time-based rule defaults to every day and
> does not currently support modification.
>   * There should be at least an hour interval between the time-based rules,
> so a maximum of 23 time-based rules can be configured.
>   * The execution time of the time-based rule cannot be repeated with
> existing time-based rules.
>   * Scaling cluster may cause some requests to experience crashes or delayed
> responses.
>   * When scaling in, the cache space will automatically scale in
> proportionally with the computing resource (vCPU), and cache data that
> exceeds the target cache space will be eliminated. The response time of some
> requests may experience significant delays.
>

## Delete Cluster​

If the business no longer requires the current cluster, you can delete it. In
the upper right corner of the **Cluster Details** page, click **Delete
Cluster** operation and confirm again.

![delete cluster en](/assets/images/delete-cluster-
en-229056ed54eb5f80def638c01800e4da.png)

> **Note**
>
>   * Deleting the SaaS model free trial cluster will also delete the free
> trial warehouse, storage resources, and their data.
>   * Clusters containing monthly/yearly billing resources do not support
> early deletion. You need to wait until the cluster expires and be converted
> to on-demand billing by default. If you want monthly billing resources to
> expire and be converted to on-demand billing as soon as possible, you need
> to confirm that the auto renew function is not enabled, otherwise the
> cluster may not expire.
>   * All resources and cached data of the cluster will be deleted by VeloDB
> Cloud, and you need to adjust the business accessing the cluster in a timely
> manner, otherwise related business requests will fail.
>

## Multi-Availability Zone Disaster Recovery​

The virtual cluster provides high availability and disaster recovery
capabilities across Availability Zones by establishing an active-standby
cluster architecture. In the event of a failure in the primary Availability
Zone, the system automatically triggers a failover to ensure business
continuity. Leveraging a real-time data synchronization mechanism, it
effectively prevents service interruptions and data loss, thereby guaranteeing
high availability for your business.

![virtual cluster intro](/images/cloud/virtual-cluster-intro-en.png)

Before creating a high-availability virtual cluster, two physical clusters
must be prepared. They must be in the Running state and located in different
Availability Zones.

![virtual cluster physical](/images/cloud/virtual-cluster-physical.png)

On the Virtual Cluster page, click **New Virtual Cluster** to navigate to the
cluster configuration page.

![virtual cluster create](/images/cloud/virtual-cluster-create.png) ![virtual cluster new intro](/images/cloud/virtual-cluster-new.png) **Parameter** | **Description**|  Virtual Cluster Name| The cluster name must start with a letter, up to 32 characters, you can use letters (case insensitive), numbers and _.| Active Cluster| The cluster that is actively serving traffic.| Standby Cluster| The disaster recovery cluster that becomes active upon failover. Note: Identical specifications are recommended.  
---|---  
  
After the virtual cluster is successfully created, you can click on its card
on the overview page to navigate to the details page. There, you can modify
the active/standby cluster configuration or delete the virtual cluster.

![virtual cluster detail](/images/cloud/virtual-cluster-detail.png)

On This Page

  * New Cluster
  * Reboot Cluster
  * Pause/Resume Cluster
    * Manual Pause/Resume Cluster
    * Auto Pause/Resume Cluster
  * Cluster Details
  * Scale Cluster
    * Manual Scaling
    * Time-based Scaling
  * Delete Cluster
  * Multi-Availability Zone Disaster Recovery

