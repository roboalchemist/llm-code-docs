# Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-faq

Title: Frequently asked questions

URL Source: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-faq

Markdown Content:
This article addresses frequently asked questions about Azure Container Instances.

The maximum size for a deployable container image on Azure Container Instances is 15 GB. You might be able to deploy larger images depending on the exact availability at the moment you deploy, but larger image size isn't guaranteed.

The size of your container image impacts how long it takes to deploy, so generally you want to keep your container images as small as possible.

Because one of the main determinants of deployment times is the image size, look for ways to reduce the size. Remove layers you don't need, or reduce the size of layers in the image (by picking a lighter base OS image). For example, if you're running Linux containers, consider using Alpine as your base image rather than a full Ubuntu Server. Similarly, for Windows containers, use a Nano Server base image if possible.

You should also check the list of precached images in Azure Container Images, available via the [List Cached Images](https://learn.microsoft.com/en-us/rest/api/container-instances/2022-09-01/location/list-cached-images) API. You might be able to switch out an image layer for one of the precached images.

See more [detailed guidance](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-troubleshooting#container-takes-a-long-time-to-start) on reducing container startup time.

Note

Due to issues with backward compatibility after the Windows updates in 2020, the following image versions include the minimum version number that we recommend you use in your base image. Current deployments using older image versions aren't impacted, but new deployments should adhere to the following base images. After June 14, 2021, ACI will no longer support deployments using older version numbers.

Note

Confidential containers on Azure Container Instances currently doesn't support Windows containers.

Important

From now through 31 December 2022, you can continue to deploy Windows Server 2016 container groups on Azure Container Instances. After this date, Windows Server 2016 images will no longer be supported. See [How do I migrate my Windows Server 2016 container groups to Windows Server 2019 images?](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-faq#how-do-i-migrate-my-windows-server-2016-container-groups-to-windows-server-2019-images-) for instructions on how to transition your workloads.

* [Nano Server](https://hub.docker.com/_/microsoft-windows-nanoserver): `sac2016`, `10.0.14393.3568` or newer
* [Windows Server Core](https://hub.docker.com/_/microsoft-windows-servercore): `ltsc2016`, `10.0.14393.3568` or newer

Note

Windows images based on Semi-Annual Channel release 1709 or 1803 aren't supported.

* [Nano Server](https://hub.docker.com/_/microsoft-windows-nanoserver): `1809`, `10.0.17763.1040` or newer
* [Windows Server Core](https://hub.docker.com/_/microsoft-windows-servercore): `ltsc2019`, `1809`, `10.0.17763.1040` or newer
* [Windows](https://hub.docker.com/_/microsoft-windows): `1809`, `10.0.17763.1040` or newer

Use the smallest image that satisfies your requirements. For Linux, you could use a _runtime-alpine_ .NET Core image, which has been supported since the release of .NET Core 2.1. For Windows, if you're using the full .NET Framework, then you need to use a Windows Server Core image (runtime-only image, such as _4.7.2-windowsservercore-ltsc2016_). Runtime-only images are smaller but don't support workloads that require the .NET SDK.

Note

ACI can't pull images from non OCI-compliant registries.

ACI supports image pulls from ACR and other non-Microsoft container registries such as DockerHub. ACI supports image pulls from ACR and other non-Microsoft OCI compatible container registries such as DockerHub with an endpoint that is publicly exposed to the internet.

1. Identify what Windows base image you're currently using.

If you're pulling directly from Microsoft Container Registry (MCR), then that image name is your base image.

If you're working with a private registry, you'll need to look at your Dockerfile to identify the base image, which will be stated after the ['FROM' line](https://docs.docker.com/engine/reference/builder/#from).

1. Select the new base image you want to use from Windows Server 2019. The following examples show commonly used Windows Server 2016 images on Azure Container Instances and our recommendations for replacement Windows Server 2019 images.

| Windows Server 2016 Image | Recommended Windows Server 2019 Images |
| --- | --- |
| mcr.microsoft.com/windows/servercore/iis | mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019 |
| mcr.microsoft.com/windows/servercore:ltsc2016 | mcr.microsoft.com/windows/servercore:ltsc2019 |
To learn more, read about [image discovery](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/container-base-images#image-discovery).

Note

If you would like assistance selecting your new base image, create an Azure Support Ticket.
3.   Follow the [Update containers in Azure Container Instances how-to guide](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-update) to update your ACI container group to use your new base image.

If you're using MCR for your container registry, you can pass the MCR image name directly into the [container group image parameter](https://learn.microsoft.com/en-us/azure/templates/microsoft.containerinstance/containergroups?tabs=bicep&pivots=deployment-language-bicep#containerproperties).

If you're using a private container registry, follow the steps in [Upgrade containers to a new version of the Windows operating system](https://learn.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/upgrade-windows-containers#create-new-container-instances-using-the-new-os-version). Make sure the container group's [image registry parameters](https://learn.microsoft.com/en-us/azure/templates/microsoft.containerinstance/containergroups?tabs=bicep&pivots=deployment-language-bicep#imageregistrycredential) are updated if you've changed them.

This really depends on your workload. Start small and test performance to see how your containers do. [Monitor CPU and memory resource usage](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-monitor), and then add cores or memory based on the kind of processes that you deploy in the container.

Make sure also to check the [resource availability](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability) for the region you're deploying in for the upper bounds on CPU cores and memory available per container group.

Note

A small amount of a container group's resources is used by the service's underlying infrastructure. Your containers are able to access most but not all of the resources allocated to the group. For this reason, plan a small resource buffer when requesting resources for containers in the group.

Azure Container Instances aims to be a serverless containers-on-demand service, so we want you to be focused on developing your containers, and not worry about the infrastructure! For those that are curious or wanting to do comparisons on performance, ACI runs on sets of Azure VMs of various SKUs, primarily from the F and the D series. We expect this to change in the future as we continue to develop and optimize the service.

Yes (sometimes). See the [quotas and limits](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-quotas) article for current quotas and which limits can be increased by request.

See the [big containers](https://learn.microsoft.com/en-us/azure/container-instances/big-containers) article for compute and memory intensive workloads. Big containers has support for vCPU counts greater than 4 and memory capacities of 16 GB, with a maximum of 32 vCPU and 256 GB per standard container group and 32 vCPU and 192 GB per confidential container group.

Current region availability is published [here](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability). If you have a requirement for a specific region, contact Azure Support.

Currently, scaling isn't available for containers or container groups. If you need to run more instances, use our API to automate and create more requests for container group creation to the service.

You can [deploy container groups in an Azure virtual network](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-vnet) of your choice, and delegate private IPs to the container groups to route traffic within the virtual network across your Azure resources. For networking scenarios and limitations with Azure Container Instances, see [Virtual network scenarios and resources](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-virtual-network-concepts).

Yes, the ACI service does reserve the following ports for service functionality: 22, 1025-1027, 3389-3399, 9999, 19000, 19080, 19390, 19100, 20000-30000, 49152-65534. Avoid using these ports in your container group definition.

Container group IP addresses are subject to change after being created or deleted. We recommend that your application code doesn't take a dependency on the container group's IP address. We also suggest using [NAT Gateway](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-nat-gateway) or [Application Gateway](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-application-gateway) if you would like to maintain a static IP address.

Container group duration is calculated from the time that we start to pull your first container's image (for a new deployment) or your container group is restarted (if already deployed), until the container group is stopped. See details at [Container Instances pricing](https://azure.microsoft.com/pricing/details/container-instances/).

Meters stop running once your entire container group is stopped. As long as a container in your container group is running, we hold the resources in case you want to start the containers up again.

Confidential computing is an industry term defined by the Confidential Computing Consortium (CCC) - a foundation dedicated to defining and accelerating the adoption of confidential computing. The CCC defines confidential computing as: The protection of data in use by performing computations in a hardware-based Trusted Execution Environment (TEE). ACI Confidential Containers introduce hardware-based protection, code integrity, and verification of the Trusted Execution Environment (TEE). Confidential containers apply the latest in confidential computing hardware enabling customers to deploy their existing applications without any modifications while taking advantage of the hardware-based data protection. Code integrity, and verification of the TEE are achieved through the attestation of a confidential computing enforcement policy, which is attached to the container group at deployment time. If any of the properties of the container group differ from those of the confidential computing enforcement policy, the environment fails to launch ensuring that the TEE isn't compromised.

Confidential containers can be used for a wide variety of elastic workloads but are especially a great fit for workloads that require strong data protection guarantees. Some examples of these workloads include machine learning workloads that utilize data sets that include personal data or with algorithms that are considered intellectual property. Healthcare customers can use it for analyzing patient data and researching. Financial services customers may use it for credit analysis risk calculation, and portfolio balancing.

Confidential computing enforcement policies can be generated using the confcom extension with the Azure CLI. For more information, see [confcom extension](https://github.com/Azure/azure-cli-extensions/blob/main/src/confcom/azext_confcom/README.md).

GPU based ACI container deployments and Windows containers aren't supported with confidential containers.

Current region availability for confidential containers is published [here](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability).

Confidential containers on Azure Container Instances do have an additional cost compared to standard SKU container groups. For more information, see [pricing page](https://azure.microsoft.com/pricing/details/container-instances/).

ACI Spot containers are a new feature that allows customers to run interruptible, containerized workloads on unused Azure capacity at up to 70% discounted prices vs regular-priority ACI containers.

ACI Spot containers may be preempted when Azure has insufficient surplus capacity and customers are billed for per-second memory/core usage. With ACI Spot Containers, you can now run your containerized workloads such as batch processing, Monte Carlo simulations, dev/test workloads and parallelizable offline workloads that can tolerate interruptions on Azure at a fraction of the cost of traditional ACI pricing. This offering is targeted at customers who wants to run interruptible workloads with no strict availability requirement.

GPU based ACI container deployments, availability zones, support for ACI deployments with Public IP and ACI deployments behind custom virtual network with Private IP aren't supported with Spot containers.

All customers get a default quota of 10 vCPU cores and 10 container groups.

Customers can file support request to increase capacity for Spot containers by selecting the issue type as "Services and Subscription limits(quotas)" and new quota type as "StandardSpotCores" added for ACI Spot containers offering when you're requested to fill in the requested details.

Azure Container Instances(ACI) Spot containers are only available in select regions during Public Preview. See [Resource and region availability](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-region-availability) for more information.

ACI Spot containers are offered at discounted price and offer up to a 70% discount on top of regular priority ACI containers. The discounts would vary per month in each region. For more information, see the [pricing page](https://azure.microsoft.com/pricing/details/container-instances/).

* [Learn more](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-overview) about Azure Container Instances.
* [Troubleshoot common issues](https://learn.microsoft.com/en-us/azure/container-instances/container-instances-troubleshooting) in Azure Container Instances.
