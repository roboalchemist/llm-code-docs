# Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale

Title: Azure Functions Scale and Hosting

URL Source: https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale

Markdown Content:
When you create a function app in Azure, you must choose a hosting option for your app. Azure provides you with these hosting options for your function code:

| Hosting option | Service | Availability | Container support |
| --- | --- | --- | --- |
| **[Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)** | Azure Functions | Generally available (GA) | None |
| **[Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan)** | Azure Functions | GA | Linux |
| **[Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan)** | Azure Functions | GA | Linux |
| **[Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview)** | Azure Container Apps | GA | Linux |
| **[Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan)** | Azure Functions | Windows - GA Linux - Retired | None |

Important

After 30 September 2028, the option to host your function app on Linux in a Consumption plan is retired. To avoid disruptions, migrate your existing Consumption plan apps that run on Linux to the [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan) before that date. Apps running on Windows in a Consumption plan aren't affected by this change.

After 30 September 2025, no new features and no new language stack support are added to the Linux Consumption plan. The last supported language versions for Linux Consumption are: .NET 9, Python 3.12, Node.js 22, PowerShell 7.4, and Java 21. Newer language versions aren't supported for Linux Consumption.

For more information, see [Migrate Consumption plan apps to the Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/migration/migrate-plan-consumption-to-flex).

The Azure App Service infrastructure on both Linux and Windows virtual machines facilitates the Azure Functions hosting options. The hosting option you choose dictates the following behaviors:

*   How your function app is scaled.
*   The resources available to each function app instance.
*   Support for advanced functionality, such as Azure Virtual Network connectivity.
*   Support for Linux containers.

The plan you choose also impacts the costs for running your function code. For more information, see [Billing](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#billing).

This article provides a detailed comparison between the various hosting options. To learn more about running and managing your function code in Linux containers, see [Linux container support in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/container-concepts).

The following table summarizes the benefits of the various options for Azure functions hosting.

| Option | Benefits |
| --- | --- |
| **[Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)** | Experience fast horizontal scaling, with flexible compute options, virtual network integration, and serverless pay-as-you-go billing. In the Flex Consumption plan, function instances dynamically scale out (up to 1,000) based on configured per-instance concurrency, incoming events, and per-function workloads for optimal efficiency. Consider the Flex Consumption plan when: ✔ You need a serverless host for your function code, paying only for on-demand executions. ✔ You require virtual network connectivity for secure access to Azure resources. ✔ Your workloads are variable and can go from no activity to demanding rapid, event-driven scaling. ✔ You want to customize compute with memory sizes (512 MB, 2,048 MB, or 4,096 MB) and reduce cold starts via one or more pre-provisioned (always-ready) instances. |
| **[Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan)** | Automatically scales based on demand using prewarmed workers, which run applications with no delay after being idle, runs on more powerful instances, and connects to virtual networks. Consider the Azure Functions Premium plan in the following situations: ✔ Your function apps run continuously, or nearly continuously. ✔ You want more control of your instances and want to deploy multiple function apps on the same plan with event-driven scaling. ✔ You have a high number of small executions and a high execution bill, but low GB seconds in the Consumption plan. ✔ You need more CPU or memory options than are provided by consumption plans. ✔ Your code needs to run longer than the maximum execution time allowed on the Consumption plan. ✔ You require virtual network connectivity for secure access to Azure resources. ✔ You want to provide a custom Linux image in which to run your functions. |
| **[Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan)** | Run your functions within an App Service plan at regular [App Service plan rates](https://azure.microsoft.com/pricing/details/app-service/windows/). Best for long-running scenarios where [Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/what-is-durable-task) can't be used. Consider an App Service plan in the following situations: ✔ You have existing and underutilized virtual machines that are already running other App Service instances. ✔ You must have fully predictable billing, or you need to manually scale instances. ✔ You want to run multiple web apps and function apps on the same plan ✔ You need access to larger compute size choices. ✔ Full compute isolation and secure network access provided by an App Service Environment (ASE). ✔ Very high memory usage and high scale (ASE). |
| **[Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview)** | Create and deploy containerized function apps in a fully managed environment hosted by Azure Container Apps. Use the Azure Functions programming model to build event-driven, serverless, cloud native function apps. Run your functions alongside other microservices, APIs, websites, and workflows as container-hosted programs. Consider hosting your functions on Container Apps in the following situations: ✔ You want control of the container image and want to package custom libraries with your function code to support line-of-business apps. ✔ You need to migrate code execution from on-premises or legacy apps to cloud native microservices running in containers. ✔ When you want to avoid the overhead and complexity of managing Kubernetes clusters and dedicated compute. ✔ Your functions need high-end processing power provided by dedicated GPU compute resources. |
| **[Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan)** | Pay for compute resources only when your functions are running (pay-as-you-go) with automatic scale on Windows. On the Consumption plan, function instances are dynamically added and removed based on the number of incoming events. Consider the Consumption plan when: ✔ You have a dependency on Windows. For example, using the v1 runtime, the full .NET Framework, or Windows-specific features like certain PowerShell modules. ✔ You want a serverless billing model and pay only when your functions are running. |

The remaining tables in this article compare hosting options based on various features and behaviors.

This table shows operating system support for the hosting options.

| Hosting | Linux 1 deployment | Windows 2 deployment |
| --- | --- | --- |
| **[Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)** | ✅ Code-only ❌ Container (not supported) | ❌ Not supported |
| **[Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan)** | ✅ Code-only ✅ Container | ✅ Code-only |
| **[Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan)** | ✅ Code-only ✅ Container | ✅ Code-only |
| **[Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview)** | ✅ Container-only | ❌ Not supported |
| **[Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan)**3 | ✅ Code-only (Retired) ❌ Container (not supported) | ✅ Code-only |

1.   Linux is the only supported operating system for the [Python runtime stack](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python).
2.   Windows deployments are code-only. Azure Functions doesn't currently support Windows containers.
3.   The ability to run your app on Linux in a Consumption plan will be retired on 30 September 2028. For more information, see [Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan).

The `functionTimeout` property in the [host.json](https://learn.microsoft.com/en-us/azure/azure-functions/functions-host-json#functiontimeout) project file sets the timeout duration for functions in a function app. This property applies specifically to function executions. After the trigger starts function execution, the function needs to return or respond within the timeout duration. When an execution exceeds this duration, a timeout error occurs and the language worker process restarts. For C# apps running in-process, the host process itself restarts. To avoid timeouts and subsequent process restarts, it's important to [write robust functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-best-practices#write-robust-functions). For more information, see [Improve Azure Functions performance and reliability](https://learn.microsoft.com/en-us/azure/azure-functions/performance-reliability#make-sure-background-tasks-complete).

The following table shows the default and maximum values (in minutes) for specific plans:

| Plan | Default | Maximum 1 |
| --- | --- | --- |
| **[Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)** | 30 | Unbounded 2 |
| **[Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan)** | 30 4 | Unbounded 2 |
| **[Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan)** | 30 4 | Unbounded 3 |
| **[Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview)** | 30 | Unbounded 5 |
| **[Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan)** | 5 | 10 |

1.   Regardless of the function app timeout setting, 230 seconds is the maximum amount of time that an HTTP triggered function can take to respond to a request. This limit exists because of the [default idle timeout of Azure Load Balancer](https://learn.microsoft.com/en-us/azure/app-service/faq-availability-performance-application-issues#why-does-my-request-time-out-after-230-seconds). For longer processing times, consider using the [Durable Functions async pattern](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-http-features#async-operation-tracking) or [defer the actual work and return an immediate response](https://learn.microsoft.com/en-us/azure/azure-functions/performance-reliability#avoid-long-running-functions).
2.   There's no maximum execution timeout duration enforced. However, the grace period given to a function execution is 60 minutes [during scale in](https://learn.microsoft.com/en-us/azure/azure-functions/event-driven-scaling#scale-in-behaviors) for the Flex Consumption and Premium plans, and a grace period of 10 minutes is given during platform updates.
3.   Requires the App Service plan be set to [Always On](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan#always-on). A grace period of 10 minutes is given during platform updates.
4.   The default timeout for version 1.x of the Functions host runtime is _unbounded_.
5.   When the [minimum number of replicas](https://learn.microsoft.com/en-us/azure/container-apps/scale-app#scale-definition) is set to zero, the default timeout depends on the specific triggers used in the app.

These values assume that the Azure Functions host process starts and runs correctly. There's a maximum timeout of 60 seconds for the language-specific worker process to also start. The worker process startup timeout isn't currently configurable.

For details on current native language stack support in Functions, see [Supported languages in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages).

The following table compares the scaling behaviors of the various hosting plans.

 Maximum instances are given on a per-function app (Consumption) or per-plan (Premium/Dedicated) basis, unless otherwise indicated.

| Plan | Scale out | Max # instances |
| --- | --- | --- |
| **[Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)** | Fast event-driven scaling decisions are calculated on a per-function basis, called [per-function scaling](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#per-function-scaling), which provides a more deterministic way of scaling the functions in your app. Except for HTTP, Blob storage (Event Grid), and Durable Functions, all other function trigger types in your app scale on independent instances. All HTTP triggers in your app scale together as a group on the same instances, as do all Blob storage (Event Grid) triggers. All Durable Functions triggers also share instances and scale together. | 1000 1 |
| **[Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan)** | [Event driven](https://learn.microsoft.com/en-us/azure/azure-functions/event-driven-scaling). Scale out automatically, even during periods of high load. Azure Functions infrastructure scales CPU and memory resources by adding more instances of the Functions host, based on the number of events that its functions are triggered on. | **Windows:** 100 6 **Linux:** 20-100 2,6 |
| **[Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan)** | Manual/autoscale | 10-30 3 100 (ASE) |
| **[Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview)** | [Event driven](https://learn.microsoft.com/en-us/azure/azure-functions/event-driven-scaling). Scale out automatically, even during periods of high load. Azure Functions infrastructure scales CPU and memory resources by adding more instances of the Functions host, based on the number of events that its functions are triggered on. | 300-1000 4 |
| **[Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan)** | [Event driven](https://learn.microsoft.com/en-us/azure/azure-functions/event-driven-scaling). Automatic scale based on the source of events. Functions infrastructure scales resources by adding more instances of the function host, based on the number of incoming trigger events. | **Windows:** 200 **Linux:** 100 5 |

1.   Flex Consumption plan has a regional subscription quota that limits the total memory usage of all instances across a given region. For more information, see [Regional subscription memory quotas](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#regional-subscription-memory-quotas). Flex Consumption plans currently only support Linux.
2.   In some regions, Linux apps on a Premium plan can scale to 100 instances. For more information, see the [Premium plan article](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan#region-max-scale-out).
3.   For specific limits for the various App Service plan options, see the [App Service plan limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-app-service-limits).
4.   On Container Apps, the default is 10 instances, but you can set the [maximum number of replicas](https://learn.microsoft.com/en-us/azure/container-apps/scale-app#scale-definition), which has an overall maximum of 1000. This setting is honored as long as there's enough cores quota available. For more information, see [Quotas for Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/quotas). When you create your function app from the Azure portal, you're limited to 300 instances.
5.   During scale-out, there's currently a limit of 500 instances per subscription per hour for Linux apps on a Consumption plan.
6.   For private endpoint restricted http triggers, scaling out is limited to at most 20 instances.

| Plan | Details |
| --- | --- |
| **[Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)** | Improved cold start even when scaled to zero. Supports [always ready instances](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#always-ready-instances) to further reduce the delay when provisioning new instances. |
| **[Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan)** | Supports [always ready instances](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan#always-ready-instances) to avoid cold starts by letting you maintain one or more _perpetually warm_ instances. |
| **[Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan)** | When it runs in a Dedicated plan, the Functions host can run continuously on a prescribed number of instances, which means that cold start isn't really an issue. |
| **[Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview)** | Depends on the [minimum number of replicas](https://learn.microsoft.com/en-us/azure/container-apps/scale-app#scale-definition): • When set to zero: apps can scale to zero when idle and some requests might have more latencies at startup. • When set to one or more: the host process runs continuously, which means that cold start isn't an issue. |
| **[Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan)** | Apps can scale to zero when idle, meaning some requests might have more latencies at startup. The consumption plan does have some optimizations to help decrease cold start time, including pulling from prewarmed placeholder functions that already have the host and language processes running. |

| Resource | [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan) | [Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan) | [Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan)/[ASE](https://learn.microsoft.com/en-us/azure/app-service/environment/overview) | [Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview) | [Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan) |
| --- | --- | --- | --- | --- | --- |
| Default [time-out duration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#timeout) (min) | 30 | 30 | 30 1 | 30 16 | 5 |
| Max [time-out duration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#timeout) (min) | unbounded 9 | unbounded 9 | unbounded 2 | unbounded 17 | 10 |
| Max outbound connections (per instance) | unbounded | unbounded | see [App Service limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-app-service-limits) | unbounded | 600 active (1200 total) |
| Max request size (MB)3 | 210 | 210 | 210 | 210 | 210 |
| Max query string length 3 | 4096 | 4096 | 4096 | 4096 | 4096 |
| Max request URL length 3 | 8192 | 8192 | 8192 | 8192 | 8192 |
| [ACU](https://learn.microsoft.com/en-us/azure/virtual-machines/acu) per instance | 210-840 | 100-840/210-250 10 | [varies](https://learn.microsoft.com/en-us/azure/container-apps/billing) | 100 | varies |
| Max memory (GB per instance) | 4 14 | 3.5-14 | 1.75-256/8-256 | [varies](https://learn.microsoft.com/en-us/azure/container-apps/billing) | 1.5 |
| Max instance count (Windows|Linux)15 | n/a|1000 | 20-100 | 10-30 (100 ASE)11 | 300-1000 18 | 200|100 |
| Function apps per plan 13 | 1 | 100 | unbounded 4 | unbounded 4 | 100 |
| [App Service plans](https://learn.microsoft.com/en-us/azure/app-service/overview-hosting-plans) | n/a | 100 per resource group | 100 per resource group | n/a | 100 per [region](https://azure.microsoft.com/global-infrastructure/regions/) |
| [Deployment slots](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-slots) per app 12 | n/a | 3 | 1-20 11 | not supported | 2 |
| Storage (temporary)5 | 0.8 GB | 21-140 GB | 11-140 GB | n/a | 0.5 GB |
| Storage (persisted) | 0 GB 7 | 250 GB | 10-1000 GB 11 | n/a | 1 GB 6,7 |
| Custom domains per app | 25 8 | 500 | 500 | not supported | 500 8 |
| Custom domain [TSL/SSL support](https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-bindings) | unbounded SNI SSL and one IP SSL connection included | unbounded SNI SSL and one IP SSL connection included | unbounded SNI SSL and one IP SSL connection included | not supported | unbounded SNI SSL connection included |

Notes on service limits:

1.   By default, the time-out for the Functions 1.x runtime in an App Service plan is unbounded.
2.   Requires the App Service plan be set to [Always On](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan#always-on). Pay at standard [rates](https://azure.microsoft.com/pricing/details/app-service/). A grace period of 10 minutes is given for HTTP triggered functions during platform updates but not for other triggers.
3.   These limits are [set in the host](https://github.com/Azure/azure-functions-host/blob/dev/src/WebJobs.Script.WebHost/web.config).
4.   The actual number of function apps that you can host depends on the activity of the apps, the size of the machine instances, and the corresponding resource utilization.
5.   The storage limit is the total content size in temporary storage across all apps in the same App Service plan. For Consumption plans on Linux, the storage is currently 1.5 GB.
6.   Consumption plan uses an Azure Files share for persisted storage. When you provide your own Azure Files share, the specific share size limits depend on the storage account you set for [WEBSITE_CONTENTAZUREFILECONNECTIONSTRING](https://learn.microsoft.com/en-us/azure/azure-functions/functions-app-settings#website_contentazurefileconnectionstring).
7.   On Linux, you must [explicitly mount your own Azure Files share](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations#mount-file-shares).
8.   When your function app is hosted in a [Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan), only the CNAME option is supported. For function apps in a [Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan) or an [App Service plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan), you can map a custom domain using either a CNAME or an A record.
9.   There's no maximum execution time-out duration enforced. However, the grace period given to a function execution is 60 minutes [during scale in](https://learn.microsoft.com/en-us/azure/azure-functions/event-driven-scaling#scale-in-behaviors) and 10 minutes during platform updates.
10.   Workers are roles that host customer apps. Workers are available in three fixed sizes: One vCPU/3.5 GB RAM; Two vCPU/7 GB RAM; Four vCPU/14 GB RAM.
11.   See [App Service limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#app-service-limits) for details.
12.   Including the production slot.
13.   There's currently a limit of 5,000 function apps in a given subscription.
14.   Flex Consumption plan instance sizes are currently defined as 512 MB, 2,048 MB, or 4,096 MB. For more information, see [Instance memory](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#instance-sizes).
15.   For details, see [Scale](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#scale) in the Hosting comparison article.
16.   When the [minimum number of replicas](https://learn.microsoft.com/en-us/azure/container-apps/scale-app#scale-definition) is set to zero, the default time-out depends on the specific triggers used in the app.
17.   When the [minimum number of replicas](https://learn.microsoft.com/en-us/azure/container-apps/scale-app#scale-definition) is set to one or more.

| Feature | [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan) | [Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan) | [Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan) | [Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan)/[ASE](https://learn.microsoft.com/en-us/azure/app-service/environment/intro) | [Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview)1 |
| --- | --- | --- | --- | --- | --- |
| [Inbound IP restrictions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#inbound-networking-features) | ✔ | ✔ | ✔ | ✔ | ✔ |
| [Inbound Private Endpoints](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#inbound-networking-features) | ✔ |  | ✔ | ✔ |  |
| [Virtual network integration](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#virtual-network-integration) | ✔ |  | ✔2 | ✔3 | ✔ |
| [Outbound IP restrictions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#outbound-ip-restrictions) | ✔ |  | ✔ | ✔ | ✔ |

1.   For more information, see [Networking in Azure Container Apps environment](https://learn.microsoft.com/en-us/azure/container-apps/networking).
2.   There are special considerations when working with [virtual network triggers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-networking-options#virtual-network-triggers-non-http).
3.   Only the Dedicated/ASE plan supports gateway-required virtual network integration.

| Plan | Details |
| --- | --- |
| **[Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan)** | Billing is based on number of executions, the memory of instances when they're actively executing functions, plus the cost of any [always ready instances](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#always-ready-instances). For more information, see [Flex Consumption plan billing](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan#billing). |
| **[Premium plan](https://learn.microsoft.com/en-us/azure/azure-functions/functions-premium-plan)** | Premium plan is based on the number of core seconds and memory used across needed and prewarmed instances. At least one instance per plan must always be kept warm. This plan provides the most predictable pricing. |
| **[Dedicated plan](https://learn.microsoft.com/en-us/azure/azure-functions/dedicated-plan)** | You pay the same for function apps in an App Service Plan as you would for other App Service resources, like web apps. For an ASE, there's a flat monthly rate that pays for the infrastructure and doesn't change with the size of the environment. There's also a cost per App Service plan vCPU. All apps hosted in an ASE are in the Isolated pricing model. For more information, see the [ASE overview article](https://learn.microsoft.com/en-us/azure/app-service/environment/overview#pricing). |
| **[Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/functions-overview)** | Billing in Azure Container Apps is based on your plan type. For more information, see [Billing in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/billing). |
| **[Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/consumption-plan)** | Pay only for the time your functions run. Billing is based on number of executions, execution time, and memory used. |

For a direct cost comparison between dynamic hosting plans (Consumption, Flex Consumption, and Premium), see the [Azure Functions pricing page](https://azure.microsoft.com/pricing/details/functions/). For pricing of the various Dedicated plan options, see the [App Service pricing page](https://azure.microsoft.com/pricing/details/app-service). For pricing Container Apps hosting, see [Azure Container Apps pricing](https://azure.microsoft.com/pricing/details/container-apps/).

In some cases, when trying to create a new hosting plan for your function app in an existing resource group you might receive one of the following errors:

*   The pricing tier isn't allowed in this resource group
*   <SKU_name> workers aren't available in resource group <resource_group_name>

These errors can occur when the following conditions are met:

*   You create a function app in an existing resource group that has yet to contain another function app or web app. For example, Linux Consumption apps aren't supported in the same resource group as Linux Dedicated or Linux Premium plans.
*   Your new function app is created in the same region as the previous app.
*   The previous app is in some way incompatible with your new app. This incompatibility can occur between versions, operating systems, or is due to other platform-level features, such as availability zone support.

Function app and web app plans are mapped to different pools of resources when they're created. Different plans require a different set of infrastructure capabilities. When you create an app in a resource group, that resource group is mapped and assigned to a specific pool of resources. If you try to create another plan in that resource group and the mapped pool doesn't have the required resources, the previously mentioned errors occur.

If this situation happens, create your function app and hosting plan in a new resource group instead.

*   [Deployment technologies in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies)
*   [Azure Functions developer guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference)
