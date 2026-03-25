# Source: https://learn.microsoft.com/en-us/azure/devops/server/requirements

Title: Setup & upgrade requirements - Azure DevOps Server

URL Source: https://learn.microsoft.com/en-us/azure/devops/server/requirements

Markdown Content:
**Azure DevOps Server |Azure DevOps Server |Azure DevOps Server 2022 | Azure DevOps Server 2020**

Prior to installing or upgrading an Azure DevOps deployment, review the requirements provided in this article.

In addition to these requirements, review the following articles as well:

*   [Client and on-premises build compatibility](https://learn.microsoft.com/en-us/azure/devops/server/compatibility?view=azure-devops-server)
*   [Service account requirements](https://learn.microsoft.com/en-us/azure/devops/server/account-requirements?view=azure-devops-server)
*   [Architecture overview](https://learn.microsoft.com/en-us/azure/devops/server/architecture/architecture?view=azure-devops-server)
*   [Default network ports and protocols](https://learn.microsoft.com/en-us/azure/devops/server/architecture/architecture?view=azure-devops-server#default-network-settings)
*   [Customizable network settings](https://learn.microsoft.com/en-us/azure/devops/server/architecture/architecture?view=azure-devops-server#customizable-network-settings)
*   [Azure Artifacts and version compatibility](https://learn.microsoft.com/en-us/azure/devops/artifacts/overview#versions-and-compatibility)

Azure DevOps on-premises can scale from an Express installation on a laptop that's used by a single person to a highly available deployment that's used by thousands of people. It can support high-use scenarios that have multiple application tiers behind a load balancer and multiple SQL instances that use SQL Always On.

The following recommendations apply to most Azure DevOps deployments. Your requirements might vary depending on how your team uses Azure DevOps. For example, if you have particularly large Git repositories or Team Foundation version control (TVC) branches, you might need higher-spec machines than those listed in the following sections. All the machines that are described in the next sections can be either physical or virtual.

A single-server deployment consists of a single machine with one octa-core processor, 16 GB of RAM, and a solid-state drive (SSD). For Elastic Search, you should use two dual-core processors and 8 GB of RAM. This configuration typically supports up to 250 users of core source control (Team Foundation Version Control or Git) and work item tracking functionality. Extensive use of automated build, test, or release likely will cause performance issues.

When you scale up a single server, the server can handle a larger number of users and an increased use of automated build, test, or release. A scaled-up server can also use search or reporting features. For example, increasing RAM to 8 GB should enable a single-server deployment to scale up to 500 users.

The following scenarios might require a multiple-server deployment:

*   Scaling beyond 500 users
*   Extensive use of automated build, test, or release
*   Using Code Search
*   Using reporting features

For a team of more than 500 users, consider the following setup:

*   An application tier with one octa-core processor, 16 GB of RAM, and a solid-state drive (SSD).
*   A data tier with one quad-core processor, 16 GB of memory, and high-performance storage, such as an SSD.

For a team of more than 2,000 users, consider the following setup:

*   An application tier with one quad-core processor, 16 GB or more of memory, and a fast hard-disk drive.
*   A data tier with two or more quad-core processors, 16 GB or more of memory, and advanced high-performance storage, like an SSD or high-performance SAN.

If you plan to use build, test, or release automation extensively, we recommend that you use higher-spec application and data tiers to avoid performance issues. For example, a team of 250 might use a multiple-server deployment that is more in line with the recommendations for a team of 500 to 2,000 users. We also recommend that you monitor your automated processes to ensure that they are efficient. For example, retrieve data from source control incrementally during builds whenever possible instead of fully refreshing with each build.

Note

Except for very small teams that have extremely limited use of these features, we don't recommend installing build, test, or release agents on your Azure DevOps Server or TFS application tiers.

If you plan to use Code Search, we recommend that you set up a separate server for Code Search. For more information, see the [hardware requirements for Code Search](https://learn.microsoft.com/en-us/azure/devops/project/search/install-configure-search?).

If you plan to use reporting features, we recommend that you set up a separate server for your warehouse database and SQL Server Analysis Services cube. Another option is to use a higher-spec data tier.

If you want to guarantee high availability, consider using multiple application tiers behind a load balancer and multiple SQL Server instances. In this scenario, we recommend that you put your Azure DevOps databases in an Always On Availability Group.

Build service has the same operating system requirements as Azure DevOps Server and TFS. Usually, it makes sense to run the build service on a separate machine from the application tier. Hardware requirements for the build service are the same as the operating system on which it's running. However, you can optimize build service performance by tailoring the hardware specs of your build machine to the types of builds your team will use.

[](https://learn.microsoft.com/en-us/azure/devops/server/requirements) The following operating systems are supported for the indicated versions of Azure DevOps Server.

Azure DevOps Server runs on either a Windows Server operating system or a Windows client operating system and only on a 64-bit operating system. We recommend that you use a server operating system unless your Azure DevOps Server is for evaluation or personal use.

| Azure DevOps Serverversion | Supported server operating systems |
| --- | --- |
| Azure DevOps Server | Windows Server 2025 (Server Core and Server with Desktop are supported) Windows Server 2022 |
| Azure DevOps Server 2022 | Windows Server 2022 Windows Server 2019 |
| Azure DevOps Server 2020 | Windows Server 2019 Windows Server 2016 |
| Azure DevOps Server 2019 | Windows Server 2019 Windows Server 2016 Windows Server 2012 R2 (Essentials, Standard, Datacenter) Windows Server 2012 (Essentials, Standard, Datacenter) |
| TFS 2018 | Windows Server 2016 Windows Server 2012 R2 (Essentials, Standard, Datacenter) Windows Server 2012 (Essentials, Standard, Datacenter) |

The [Server Core](https://learn.microsoft.com/en-us/windows-server/administration/server-core/what-is-server-core) installation option is supported for Azure DevOps Server, Azure DevOps Server 2022, Azure DevOps Server 2020, Azure DevOps Server 2019, and TFS 2018. [Windows Server version 1709](https://learn.microsoft.com/en-us/windows-server/get-started/get-started-with-1709) isn't supported.

| Azure DevOps Server version | Supported client operating systems |
| --- | --- |
| Azure DevOps Server Azure DevOps Server 2022 | Windows 11 Version 24H2 |
| Azure DevOps Server 2020 | Windows 10 (Enterprise) Version 1803 Windows 10 (Professional, Enterprise) 1809 or later |
| Azure DevOps Server 2019 | Windows 10 (Professional, Enterprise) Version 1607 or later |
| TFS 2018 | Windows 10 (Professional, Enterprise) Version 1607 or later |

Although you can install Azure DevOps Server on a client operating systems, we don't recommend client operating system installation except for evaluation purposes or personal use. You can't install Azure DevOps Server Proxy on client operating systems.

The proxy server is available only when you install Azure DevOps Server on a Windows server operating system. Supported systems are listed in the following table for each version.

Note

The hash algorithm that takes part of the authorization process was changed from SHA1 to SHA256. Please, make sure to update the proxy server to avoid disruptions.

| Azure DevOps Proxy Server version | Supported Windows OS systems |
| --- | --- |
| Azure DevOps Proxy Server | Windows Server 2025 Windows Server 2022 Windows Server Core |
| Azure DevOps Proxy Server 2022 | Windows Server 2022 Windows Server 2019 Windows Server Core |
| Azure DevOps Proxy Server 2020 | Windows Server 2019 Windows Server 2016 Windows Server Core |
| Azure DevOps Proxy Server 2019 | Windows Server 2019 Windows Server 2016 Windows Server 2012 R2 (Essentials, Standard, Datacenter) Windows Server 2012 (Essentials, Standard, Datacenter) Windows Server Core |
| Team Foundation Proxy Server 2018 | Windows Server 2016 Windows Server 2012 R2 (Essentials, Standard, Datacenter) Windows Server 2012 (Essentials, Standard, Datacenter) |

Review the following hardware recommendations to determine the optimal hardware to use for Azure DevOps Server Proxy.

Unlike operating system requirements, hardware recommendations for proxy are different from hardware recommendations for setting up the application tier of Azure DevOps Server. The application tier requires more robust hardware than the proxy server.

Recommended hardware is based on the size of the team that will use the proxy server. Usually, this is the team in your remote office. The larger your team, the more robust your hardware must be.

| Remote team size | Hardware recommendations (CPU/RAM) for Azure DevOps Server Proxy |
| --- | --- |
| 450 or fewer users | One processor, 2.2-GHz CPU, 4 GB of RAM |
| Between 451 and 2,200 users | Two processors, 2.0-GHz CPU, 8 GB of RAM |
| Between 2,201 and 3,600 users | Four processors, 2.0-GHz CPU, 8 GB of RAM |

Azure DevOps on-premises deployments require some version of SQL Server. Azure DevOps Server supports Express, Standard, and Enterprise [SQL Server editions](https://www.microsoft.com/sql-server/sql-server-downloads). The Express edition is recommended only for evaluation purposes, personal use, or for very small teams. We recommend the SQL Server Standard or Enterprise versions for all other scenarios.

Note

Consider enabling the Query Store (QDS) on your SQL Server to help monitor performance.

For production deployments, use one of the following versions of SQL Server.

| Azure DevOps version | Supported SQL Server version |
| --- | --- |
| Azure DevOps Server | Azure SQL Database Azure SQL Managed Instance SQL Server 2025 SQL Server 2022 |
| Azure DevOps Server 2022 | Azure SQL Database Azure SQL Managed Instance SQL Server 2022 SQL Server 2019 |
| Azure DevOps Server 2020 | Azure SQL Database SQL Server 2019 SQL Server 2017 SQL Server 2016 (minimum SP1) |
| Azure DevOps Server 2019 Update 1.1 | Azure SQL Database SQL Server 2019 SQL Server 2017 SQL Server 2016 (minimum SP1) |
| Azure DevOps Server 2019 | Azure SQL Database SQL Server 2017 SQL Server 2016 (minimum SP1) |
| TFS 2018 | SQL Server 2017 SQL Server 2016 (minimum SP1) |

Note

SQL Server on Linux isn't supported.

The following information applies to the indicated SQL Server version:

*   **Azure SQL Database**: Only supported when you also use Azure Virtual Machines. For details, see [Use Azure SQL Database with Azure DevOps Server](https://learn.microsoft.com/en-us/azure/devops/server/install/install-azure-sql?view=azure-devops-server).
*   **SQL Server 2016**: If you use SQL Server 2016, you must install a Visual C++ runtime [update](https://support.microsoft.com/kb/3138367).

You can install Azure DevOps on more than one server if the servers are all joined to an Active Directory domain that's based on a functional level that the servers support. You can install Azure DevOps on a single server that's joined to an Active Directory domain or that is a member of a workgroup.

Microsoft doesn't always immediately support major new versions of dependencies like SQL Server. Sometimes, we must release updates to add support for those versions. However, when Microsoft supports a major version, we always support the latest service pack immediately when it's released. We work with product teams to test service packs before they're released.

You can install Azure DevOps in various languages on supported operating systems. However, you can't use any combination of localized operating system with Azure DevOps Server and TFS. Also, you can't install multiple languages on a single Azure DevOps Server or TFS server.

The following table outlines the language combinations that are supported:

| Operating system | Azure DevOps Server |
| --- | --- |
| English | English |
| English | Language other than English |
| Language other than English | English |
| Language other than English | Language must match the operating system |

If you're running an English language operating system, you can install any language version of Azure DevOps Server. If you aren't running an English language operating system, you must install the English version of Azure DevOps Server or the version that has been localized for the same language as the operating system.

Azure DevOps Proxy Server and Team Explorer don't have additional language requirements specific to working with Azure DevOps Server.

Test controllers and agents have their own language requirements. For more information, see [Test controller and test agent requirements](https://learn.microsoft.com/en-us/visualstudio/test/test-controller-and-test-agent-requirements-for-load-testing).

*   [Client and on-premises build compatibility](https://learn.microsoft.com/en-us/azure/devops/server/compatibility?view=azure-devops-server)
*   [Service account requirements](https://learn.microsoft.com/en-us/azure/devops/server/account-requirements?view=azure-devops-server)
*   [Architecture overview](https://learn.microsoft.com/en-us/azure/devops/server/architecture/architecture?view=azure-devops-server)
*   [Default network ports and protocols](https://learn.microsoft.com/en-us/azure/devops/server/architecture/architecture?view=azure-devops-server#default-network-settings)
*   [Customizable network settings](https://learn.microsoft.com/en-us/azure/devops/server/architecture/architecture?view=azure-devops-server#customizable-network-settings)
*   [Azure Artifacts and version compatibility](https://learn.microsoft.com/en-us/azure/devops/artifacts/overview#versions-and-compatibility)
