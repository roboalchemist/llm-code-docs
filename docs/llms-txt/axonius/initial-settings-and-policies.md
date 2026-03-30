# Source: https://docs.axonius.com/docs/initial-settings-and-policies.md

# Initial Settings and Policies

To access Agent Coverage:

1. At the top of the left navigation bar, click **Workspaces**.

<Image align="center" border={false} width="400px" src="https://files.readme.io/1712e45ced143059003ab1c4beaa05bde7081510e12824ae89410979bb0e3354-image.png" />

2. Select **Agent Coverage** from the list of workspaces.
3. The left navigation bar and main page of Agent Coverage are displayed. The title **Agent Coverage** appears next to the Axonius logo.

<Image align="center" border={false} src="https://files.readme.io/0c433a7e5f874753abe8c2a6334756516b6b3563e884d6be008351352f1f3081-agent_coverage_workspace.png" />

### Recommended Adapter Categories

To efficiently use Agent Coverage, we recommend you connect adapters from at least some of the following categories:

* MDM/EMM
* EDR/EPP
* Configuration and Patch Management
* Encryption

### Policy Components of Agent Coverage

Agent Coverage Policies are defined by the following components.

* [**Managed and active devices**](/docs/initial-settings-and-policies#managed-and-active-devices) - Defines the analysis scope through queries - which devices in scope (managed) and active.
* [**Device categories**](/docs/initial-settings-and-policies#device-categories) - Classifies in-scope devices by device type, operating system, and deployment type, for granular agent coverage policies.
* [**Agents deployment status**](/docs/initial-settings-and-policies#agents-deployment-status) - Defines device categories per agent; and specifies which device categories should be monitored for each agent installation. Administrators can configure coverage requirements for each individual agent.
* [**Agent-Specific Exceptions (targeted exclusions)**](/docs/issues-and-actions#exception-handling-\(optional\)) - Allows administrators to create specific exclusions for individual agents on targeted devices or device groups; and provides flexibility to handle unique deployment scenarios without modifying the overall coverage policy.

After defining these policies:

1. Managed queries are created based on the policy definitions.
2. These managed queries are used as building blocks to create managed dashboards.
3. Each dashboard displays key metrics and issues detected by the managed queries.

## Managed and Active Devices

Before configuring agent coverage monitoring, you must first establish the scope of devices to be monitored. You must review and configure these baseline scopes before proceeding with agent-specific coverage rules, to ensure that your coverage focuses on the right devices.

Agent Coverage operates on two fundamental device classifications:

* **Managed devices** - Devices that must have agents installed according to your organization's policy. These represent your core coverage requirements.
* **Active devices** - Devices that remain operationally active within your environment (excluding decommissioned or retired systems).

The most effective implementation monitors devices that are both managed and active. However, these definitions vary significantly between organizations based on their specific policies and operational requirements.

You must click **Save** in each of the following configuration pages to apply your changes.

### Out-of-Scope Devices

Create or select a query to exclude devices from coverage. The scope of agent coverage depends on your security policies. For example, you may want to exclude devices of a specific type, like employees' personal phones.

<Image alt="OutOfScopePage" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-4WWD9SX1.png" />

You have three options to define out-of-scope devices:

* **Agent Coverage - Out-of-Scope** - An Axonius predefined query that cannot be edited. Click **Review Query** to see which field it uses to define out-of-scope devices. The query covers scope aspects such as data cleaning, devices that were not seen by any agent-based adapter, or devices that were seen only by a single adapter.
* **Select your own query** - Define a Devices Query tailored to your needs. It is most recommended to use the Axonius predefined query as a baseline, as it excludes low fidelity devices from your scope. For example, you can include it as a saved query and add more fields:

<Image alt="saved_query" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-9YU1YRUR.png" />

* **Define later** - You can choose to address the question of out-of-scope devices at a later time. However, your inventory may contain devices that should not be managed by policy and therefore, shouldn't have agents installed on them. If you do not exclude these devices from coverage, they might appear as potential issues, which will result in lower-fidelity findings. We recommend coming back to defining out-of-scope devices as soon as possible.

### Active Devices

After devices are not seen by any tool or adapter for a certain number of days, they become inactive. You need to define after how many days devices that were not seen become inactive.

You can define that active devices are devices that were seen either in the last 7 or 30 days; or, you can **select your own query** and define a custom range.

<Image alt="ActiveDevices" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-97GZ43RG.png" />

### Device Categories

Your devices inventory is grouped by different categories, predefined by Axonius. The responsibility for various parts of the network is often divided between teams, and different devices employ different tools. Device categories are based on that information.

Devices categories are dynamic: the number of devices in each category changes according to the configurations you've made for out-of-scope and active devices. For example, if you change the definition of active devices from "Last seen in 7 days" to "Last seen in 30 days", this might affect the inventory in the device categories. Review the number of devices in each category to make sure they make sense.

Each device category comprises the following criteria:

* Device type - server, laptop, physical workstation, etc.
* Operating system - Linux, Windows, MacOS
* Deployment type - cloud, on-prem, or physical deployment for end-user devices

### Using Shared Queries for Agent Coverage

Queries and other resources used in the Agent Coverage Hub must have access permissions of 'Shared'. To create and edit shared resources, the option **Allow sharing dashboards and queries to all Data Scopes** must be enabled under **Special Permissions** in **System Settings**. When this option is not enabled, a notification is displayed in the Agent Coverage Hub. To enable resource sharing, click **Enable Sharing**. When this option is enabled, the notification does not appear.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/workspaces/AgentCoverageHubEnableSharing.png" />

## Agents Deployment Status

This table shows the status of your covered devices: which of them are active, and are there any issues involving missing, unhealthy or inactive agents.

<Image border={false} src="https://files.readme.io/0082fb1ae3d2a49278e64b72e90de7a8a3b6a3b11d8324781306ea6f1e70e350-image.png" />

<br />

The table contains the following columns:

* **Name** - The name of the tool.
* **Status** - Possible statuses are either Done or Incomplete Setup.
  * When the status is Done, that means that you've completed all configurations required to define this tool's coverage scope.
  * When the status is Incomplete Setup, that means you have several more configurations to complete to ensure accurate coverage.

<Callout icon="📘" theme="info">
  Note

  When you first start to use the Agent Coverage, all statuses for all tools are "Incomplete setup". We recommend completing all required configurations as soon as possible.
</Callout>

* **Active Agents** - The number of active agents detected by the adapter. An agent is active when it's installed on an active, in-scope (managed) device and is functioning properly.
* [**Potential issues** and **Actions**](/docs/issues-and-actions)