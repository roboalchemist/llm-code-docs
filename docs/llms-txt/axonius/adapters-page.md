# Source: https://docs.axonius.com/docs/adapters-page.md

# Adapters Page

The **Adapters** page displays the list of the solutions Axonius integrates with, called adapters.

To open the **Adapters** page, click the **Adapters** icon on the left navigation panel. If you are working with a smaller screen, you may need to click **More** to find the **Adapters** icon.

The **Adapters** page shows all the adapters in the system, the category to which they belong, the assets they fetch and their connection status.  You can use categories and asset types to help you decide which additional adapters you can connect, and to easily find adapters relevant for your use case and the asset types you want to investigate.

The adapters are arranged as cards. The top section of the page shows  adapters that have connections configured (out of all available adapters) in alphabetical order, while all the other adapters are shown below.

When you choose an adapter category, **Configured Adapters** shows the number of adapters configured in that category out of all the adapters available in that category.

<Image alt="Adapters Page New without graphics.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapters%20Page%20New%20without%20graphics.png" />

## Card Information

<Image alt="TileExample" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TileExample.png" />

The following information is shown on each adapter card:

* **Adapter logo** - A unique logo that represents the adapter in the Axonius system.

* **Adapter Name** - The name of the adapter.

* **Assets Fetched** - Adapters can fetch a wide range of assets. Some assets are fetched by default for that adapter, while others must be configured using advanced configuration. Up to four asset types are displayed for each adapter, if there are more, a number shows that there are more asset types. Hover over to see all asset types in a list.

* **Category** - Categories to which the adapter belongs. An adapter can belong to more than one category. Up to three categories are displayed for each adapter, if there are more, a number shows that there are more categories. Hover over to see all categories in a list.

* **Number of connections and their status** - Each adapter can have more than one connection. The numbers show the number of connections, while the color indicates their status.
  * Green - The number of successfully connected connections for this adapter.
  * Red - The number of configured adapter connections with connection errors.
  * Dark gray - The number of configured connections set as inactive  for this adapter.

* Memo - An icon is displayed if a memo was added to an adapter. Hover over to see the [memo text](docs/adapter-profile-page#adding-adapter-memos-editable-information).

* Hover over the card to see the adapter description.

* Hover over the right corner of the card, and from the 3-dot menu select:

  <Image alt="AdapterOptionsTile" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterOptionsTile.png" />

  * **Add Connection** to add a [new adapter connection](/docs/adding-a-new-adapter-connection)

### Finding Adapters

You can use the search and filters to find adapters you want to connect.

**Search Adapters**
Type in the **Search Adapters** field to find adapters, as soon as you start typing, the system presents you with possible matches.

<Image alt="Search Adapters New.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Search%20Adapters%20New.png" />

**Search Categories**

Click in the **Search Categories** field to search for one or more category names. All the adapters in those categories are displayed.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Search%20Adapter%20Categories.png" />

The system also shows you how many adapters in the category you have already configured. Note that *Configured adapters*  relates to the number of adapters in the category you chose and not to the total number of adapters in the system.

Click **x** next to an adapter category to remove it from the selection or use **Clear All** to clear all your choices.

**Search Asset Types**

Click in the **Search Asset Type** field to search for one or more asset types. All the adapters that fetch that asset type are displayed.  Learn more about [asset types](/docs/assets-page#viewing-assets-by-type).

<Image alt="Search Asset Types Adapters Page.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Search%20Asset%20Types%20Adapters%20Page.png" />

Click **x** next to an adapter category to remove it from the selection or use **Clear All** to clear all your choices.

### Changing Views

The adapter list can also be displayed as a table.
Use the card/table button to toggle the views. The same information is shown on the table as on the cards.

<Image alt="AdapterviewToggle" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterviewToggle.png" />

<Image alt="Adapter Table View.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Table%20View.png" />

### Viewing Information for a Specific Adapter

You can view information for a specific adapter on the **Adapters** page.

1. Click on an adapter card or, if in table view, anywhere in the row of the adapter you would like to view.
2. The **Adapter Profile** page opens for that adapter. You can see all the connections for that adapter. In addition, you can review the information in the **Advanced Settings** tabs.

<Image alt="Adapter Profile New" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Profile%20New.png" />

When you click **Adapter Connections**, the **Connections** page opens, filtered to that adapter.

### Asset Inventory

Connecting adapters enables Axonius to pull asset information from many sources across the organization. The more adapters you connect, the more comprehensive your asset inventory will be. It is recommended you connect any of the following to Axonius adapters:

* **Device and User management consoles**: such as [Microsoft Active Directory](/docs/microsoft-active-directory-ad), [Microsoft Endpoint Configuration Manager (MECM) (formerly SCCM)](https://docs.axonius.com/docs/microsoft-sccm), or [Jamf Pro](/docs/jamf-pro).

* **Endpoint security agents**: such as [McAfee ePolicy Orchestrator (ePO)](/docs/mcafee-epolicy-orchestrator-epo), Symantec,[CrowdStrike Falcon](/docs/crowdstrike-falcon), or [VMware Carbon Black EDR](/docs/carbon-black-cb-response).

* **Networking**: Axonius integrates with networking infrastructure from a wide variety of vendors including [Aruba](/docs/aruba),[Cisco](/docs/cisco),[Checkpoint](/docs/checkpoint-infinity),[Fortinet](/docs/fortinet-fortigate),[Juniper](/docs/juniper-junos), and [Palo Alto](/docs/palo-alto-networks-panorama).

* **Identity Access Management**: such as [Okta](/docs/okta),[Google Workspace (formerly G Suite)](/docs/g-suite-by-google),[Duo Beyond](/docs/duo-beyond), or other platforms

* **Vulnerability / Patch Management:** such as [Qualys Cloud Platform](/docs/qualys-cloud-platform),[Tenable Nessus](/docs/tenable-nessus),[Rapid7 Nexpose](/docs/rapid7-nexpose),[Kenna Security Platform](/docs/kenna-security-platform), or other platforms.

* **Cloud Providers**: such as [Amazon Web Services](/docs/amazon-web-services-aws),[Microsoft Azure](/docs/microsoft-azure), or [Google Cloud Platform](/docs/google-cloud-platform-gcp).

* **Collaboration**: such as [Asana](/docs/asana),[Airtable](/docs/airtable-enterprise),[Docusign](/docs/docusign),[Zendesk](/docs/zendesk-adapter),[Zoom](/docs/zoom), and more.

To see a full list of supported adapters, visit [Adapters List](/docs/adapters-list).

## Adding a New Adapter Connection

To connect a new adapter, provide the access credentials needed.  The details vary by adapter, but include some combination of:

1. IP Addresses
2. User Names
3. Passwords
4. API keys
5. Key Files
6. Any other credentials needed to access the adapters being used

For example, the **Amazon Web Services (AWS)** adapter configuration drawer:
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AWSEG1.png)

You can add a new adapter connection either from the **Adapters** page or from the **Connections** page.
Learn more about [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Bulk Set Advanced Settings

Use **Bulk Set Advanced Settings** to set [Adapter Advanced Settings](/docs/advanced-settings) values for all adapters or for adapters without configured connections. You can use this to set new defaults for Adapter Advanced settings on your system.

<Callout icon="📘" theme="info">
  Note

  To modify the advanced settings for a single adapter, click the relevant adapter and then  **Advanced Settings**.
</Callout>

In  **Bulk Set Advanced Settings**, select the settings you want to set for all adapters, then set the required value in the corresponding input fields.
Then select whether to apply these new values to all adapters or only to adapters without configured connections.

<Image align="center" alt="BulkSEt" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BulkSEt.png" />

## Adapters Fetch History

The [**Adapters Fetch History**](/docs/adapters-fetch-history) opens the Adapters Fetch History page and displays the fetch results over time for each adapter and for specific adapter connections.

## Connections

Click **Adapter Connections** to open the **Connections** page. The **Connections** page displays detailed information about each connection. See **[Adapter Connections](/docs/adapter-connections)**.