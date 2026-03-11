# Source: https://docs.axonius.com/docs/external-exposures-workspace.md

# External Exposures Workspace

### The Challenge

Organizations often struggle to gain a clear understanding of which system components are exposed to the public internet. Determining this may require writing complex queries and reviewing large tables of raw data, which are often cluttered, difficult to interpret, and time-consuming.

### Our Solution

External Exposures provides a clear, intuitive view of which system components are connected to or isolated from the public internet. This view maximizes visibility and reduces noise from raw data, which empowers security and IT teams to:

* Identify publicly exposed assets, which might include critical assets and crown jewels
* Track changes and security trends over time
* Prioritize remediation efforts based on data-driven decisions
* Communicate network exposure confidently to leadership
* Take faster, more informed actions to reduce the overall organizational attack surface

## Before You Begin

### Products Required for this Workspace

To access and use this workspace, you must have access to [Axonius Exposures](/docs/exposures-overview).

### Additional Configuration

To ensure that the workspace correctly identifies public-facing elements, configure all networks outside the RFC 1918 address space as **internal networks** when appropriate. This configuration helps the logic of mapping Network Routes distinguish between truly public and internal routes, and reduce false positives when handling public IP addresses that should be treated as internal. For more information, see [Configuring Network Settings](https://docs.axonius.com/axonius-help-docs/docs/configuring-network-settings)

<br />

## Workspace Assets and Modules

<Callout icon="📘" theme="info">
  **Note**

  Each workspace has its own use-case-focused navigation menu on the left. The assets and modules available from this menu depend upon your access configuration.
</Callout>

You can access the following assets directly from this workspace:

[Devices](https://docs.axonius.com/axonius-help-docs/docs/devices-page)

[Network Routes](https://docs.axonius.com/axonius-help-docs/docs/network-routes)

## Use Cases this Workspace Helps You Fulfill

The External Exposures' Home page displays charts and KPIs of special interest, divided into functional areas that help you focus on specific use-case information.

The data displayed on the charts relies mainly on the [Risk Score settings](/docs/risk-score-settings) you have defined for your assets. If needed, you can always change those settings to get the most accurate risk picture.

### General Internet Exposure Picture

The **Overview** section at the top of the page provides a simple, straightforward view of your most critical assets that are exposed to the public internet. It shows data the following data:

* The total number of publicly exposed devices
* The total number of publicly exposed devices with **Critical** vulnerabilities, which represent the ultimate attack path.
* The total number of publicly exposed devices that are at Critical Risk Level. This number is determined by the [Axonius Risk Levels](/docs/creating-a-risk-score#defining-risk-levels) you defined. Mapping Risk Levels to exposure levels helps you device which assets demand immediate attention to enhance security posture.

![ExternalExposuresOverview](https://files.readme.io/43aa7014336c9d94d1f5d131626f0abda46d2aff48635ae1f6e92d3cd1cc9080-image.png)

<br />

### Recognizing Exposure Components in Context

The workspace shows you publicly exposed devices broken down by different criteria: by Operating System and by Risk Score. These different displays help you zoom in on specific connections between asset components and risks.

For example, the **Publicly-Exposed Devices by Operating System** chart might reveal operating systems exposed to the internet that shouldn't be exposed at all.

![ExposedDevicesBreakdownByOS](https://files.readme.io/b21014c05918df74b219024eeb2900a1b458ab3f5acb57866bf236b09fbc9cac-image.png)

<br />

Click on the colored portion of an operating system in the chart to open the Devices page with the appropriate filters. For example, show only publicly exposed devices with a Windows operating system:

![ExposedDevicesWindowsFilter](https://files.readme.io/a1378d52066fc163a7f4a67c8cf67bb5992a1401858811139be42c8288ebc20e-image.png)

<br />

From the Devices page, you can explore a specific device on its [Asset Profile page](/docs/asset-profile-page); or implement remediation workflows such as opening [tickets](/docs/tickets-1) and [cases](/docs/cases-1) for selected devices.

Click the data in any chart in the workspace to take the same actions and additional actions from the Assets page that it opens.

The workspace also provides information on the potential network distribution components at risk, as well as potential entry points in the network route that attackers might exploit. The following data is available:

* Publicly exposed devices with no firewall protection
* Publicly exposed Load Balancers
* Publicly exposed Load Balancers with no firewall protection, which provide attackers with a direct path to multiple backend systems

### Tracking Exposure Trends Over Time

The workspace shows charts that detail how many publicly exposed devices exist in your environment over a certain period of time - both general devices and devices at critical risk. This data help you outline a long-term security plan and make changes to it over time according to your needs.

### Clear View of Publicly Exposed Assets

The workspace displays comprehensive lists (Assets tables) of publicly exposed Device and Network Route assets. Each table contains key information on each asset. Click **View all Results** to open the relevant Assets page in a new tab.