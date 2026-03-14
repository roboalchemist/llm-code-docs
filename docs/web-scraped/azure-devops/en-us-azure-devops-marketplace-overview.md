# Source: https://learn.microsoft.com/en-us/azure/devops/marketplace/overview

Title: Extensions overview - Azure DevOps

URL Source: https://learn.microsoft.com/en-us/azure/devops/marketplace/overview

Markdown Content:
**Azure DevOps Services | Azure DevOps Server | Azure DevOps Server 2022**

Extensions are add-ons that you can use to customize and extend your experience with Azure DevOps. They're written using standard technologies such as HTML, JavaScript, and CSS, and can be developed using your preferred development tools.

Extensions are published on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/azuredevops), where they can be kept private for you and your team or [shared publicly](https://learn.microsoft.com/en-us/azure/devops/extend/publish/overview?view=azure-devops) with millions of developers currently using Azure DevOps.

Extensions use our [RESTful API Library](https://learn.microsoft.com/en-us/rest/api/azure/devops/) to easily interact with Azure DevOps and other applications/services.

![Image 1: Screenshot of components of an extension.](https://learn.microsoft.com/en-us/azure/devops/extend/media/extension-components.png?view=azure-devops)

The following items make up an extension:

*   [JSON manifest file](https://learn.microsoft.com/en-us/azure/devops/extend/develop/manifest?view=azure-devops): Contains basic info about the extension.
*   Discovery assets: Markdown and images that make up the extension's overview and aesthetics in the Marketplace.
*   Static files: Contain the logic of the extension, including HTML, JS, and CSS files. Static files are only applicable to contribution-based extensions.

These files and assets get bundled up to make a [VSIX file](https://learn.microsoft.com/en-us/visualstudio/extensibility/anatomy-of-a-vsix-package?view=vs-2022&preserve-view=true) that gets published to the Marketplace.

From the Marketplace, users can [install extensions](https://learn.microsoft.com/en-us/azure/devops/marketplace/install-extension?view=azure-devops) directly into their organization. If you don't have permissions to install an extension, but you're a project member, you can [request an extension](https://learn.microsoft.com/en-us/azure/devops/marketplace/request-extensions?view=azure-devops) instead.

There are dozens of ways you can use an extension and places where you can add to the user interface, and we're adding more every sprint. Learn about all of the places where you can add a hub in the [Extensibility points](https://learn.microsoft.com/en-us/azure/devops/extend/reference/targets/overview?view=azure-devops).

*   [Provide new Azure Pipelines tasks](https://learn.microsoft.com/en-us/azure/devops/extend/develop/add-build-task?view=azure-devops) that teams can use in their builds.
*   Use [dashboard widgets](https://learn.microsoft.com/en-us/azure/devops/extend/develop/add-dashboard-widget?view=azure-devops) to get custom views within Azure DevOps.
*   Extend the [work item form](https://learn.microsoft.com/en-us/azure/devops/extend/develop/add-workitem-extension?view=azure-devops) with new tabs, sections, and actions.
*   Create [your own hub](https://learn.microsoft.com/en-us/azure/devops/extend/develop/add-hub?view=azure-devops) to embed new capabilities within our Agile, code, build, and test experiences.
*   Develop [actions](https://learn.microsoft.com/en-us/azure/devops/extend/develop/add-action?view=azure-devops) that can be run on hubs, whether they're ours or ones you created.

To evaluate a Marketplace extension, review the information and resources described in the following table. You can find this information in the extension information

**Information**

**Usage**

* * *

**Top Publisher badge**![Image 2: Screenshot showing Top Publisher badge and label.](https://learn.microsoft.com/en-us/azure/devops/marketplace/media/top-publisher-badge.png?view=azure-devops)

The publisher demonstrates commitment to its customers and the Marketplace through excellent policies, quality, reliability, and support. For more information, see [Top Publisher](https://learn.microsoft.com/en-us/azure/devops/extend/publish/overview?view=azure-devops#top-publisher).

* * *

**Q & A**

The Q & A section of published extensions might answer questions you have. Also, they're a good mechanism to engage with the extension’s publishers to have a meaningful dialogue to make yourself comfortable. Use the Q & A information to understand the development, testing, and security practices the publisher follows. It also gives you a sense of the publisher's responsiveness.

* * *

**Ratings & reviews**

Ratings and reviews indicate how others perceive the offering. For more information, see [Respond to customer feedback](https://learn.microsoft.com/en-us/azure/devops/extend/publish/overview?view=azure-devops#respond-to-marketplace-extension-reviews).

* * *

**Privacy, license, and support policies**

See if the publisher provided them and if they meet your needs or concerns. For more information, go to [Safety information](https://learn.microsoft.com/en-us/azure/devops/marketplace/overview#safety-information).

* * *

The Marketplace ensures the safety and integrity of extensions through the following measures:

*   **Malware scan**: The Marketplace runs a virus scan on each new and updated extension package to ensure its safety. Until the scan is clear, the extension isn't published for public usage. If a concern surfaces, the Marketplace team can disable the extension immediately and notify its existing customers.

*   **Content scan**: The Marketplace scans the content of every new and updated extension to avoid surfacing inappropriate or offensive content on the Marketplace pages.

*   **Access to approved scopes only**: An extension can only operate within the granted scopes. For example, an extension with read-only permissions on work items can't modify your features and bugs. Azure DevOps web extensions run in a sandboxed browser iframe and can only access Azure DevOps data and APIs approved for the extension. During installation, admins are prompted to approve permissions and scopes. To protect yourself, carefully review the scopes the extension requests.

Note

If the scopes change for an extension, you must approve the update before it can be applied to your organization or collection. 
*   **Third-party build and release tasks**: Tasks are implemented as code that executes on an agent machine. Tasks can only access secrets explicitly provided to them (see [variable secrets](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops&tabs=yaml%2Cbatch#secret-variables)), but generally have full access to the agent machine itself. To reduce risk, run builds on Microsoft-hosted agents, which are VMs isolated from other jobs and recycled after each job. Alternatively, limit file and network access on private hosted agent machines. Learn more about [build and release agents](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/agents?view=azure-devops&preserve-view=true#microsoft-hosted-agents).

*   **Third-party code execution on the server**: Extensions can't install or execute any code on Azure DevOps Server.

Before you build an extension, familiarize yourself with the extension types already available within the Marketplace, [Extensions for Azure DevOps](https://marketplace.visualstudio.com/azuredevops). Learn how to build your first extension and check out our full set samples.

*   [Develop your first extension](https://learn.microsoft.com/en-us/azure/devops/extend/get-started/node?view=azure-devops)
*   [Samples](https://learn.microsoft.com/en-us/azure/devops/extend/develop/samples-overview?view=azure-devops)

For more information about building extensions, see the following articles:

*   [REST APIs](https://learn.microsoft.com/en-us/rest/api/azure/devops/)
*   [Service Hooks](https://learn.microsoft.com/en-us/azure/devops/service-hooks/overview?view=azure-devops)
*   [Package, publish, and install your extension](https://learn.microsoft.com/en-us/azure/devops/extend/publish/overview?view=azure-devops)
*   [Package and publish your integration with an external app or service](https://learn.microsoft.com/en-us/azure/devops/extend/publish/integration?view=azure-devops)
*   [Share your work publicly with the entire community](https://learn.microsoft.com/en-us/azure/devops/extend/develop/manifest?view=azure-devops#mark-an-extension-public)

*   [Visual Studio Marketplace](https://marketplace.visualstudio.com/azuredevops)
*   [Extension Publisher Page](https://marketplace.visualstudio.com/manage)
*   [Visual Studio Partner Program](https://partner.microsoft.com/solutions/microsoft-visual-studio)
*   [Extension manifest reference](https://learn.microsoft.com/en-us/azure/devops/extend/develop/manifest?view=azure-devops)
