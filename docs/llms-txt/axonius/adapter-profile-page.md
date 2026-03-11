# Source: https://docs.axonius.com/docs/adapter-profile-page.md

# Adapter Profile Page

Learn about the Adapter Profile page, including connection details, advanced settings, and how to manage gateways.

The **Adapter Profile** page displays information about each adapter, including its connections and their status. It also provides links to configure **Advanced Settings** for **Adapter Configuration**, **Advanced Configuration**, **Ingestion Rules Configuration**, and **Discovery Configuration**.

<Image alt="Adapter Profile New.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/AssetProfileNew.png" />

The **Adapter Profile** shows:

1. The adapter description. Click 'x' to close the description pane, and click the 'i' icon to display the description again.
2. The asset types the adapter fetches. Only the first five asset types are shown on the Description pane; the rest are displayed when you hover over the numeral that shows the additional number of asset types.
3. Information about the adapter connection as well as its status.

Hover over to see more details.

When you click on a connection, the **Edit Connection** drawer opens for more details. You can copy the URL and share it with others for direct access. Click 'x' to close the description pane, and click the 'i' icon to display it again.

To sort by a specific value, click on a column. For example, you can sort by **Connection Status**.

## The Side Pane

The side pane header provides a summary of the adapter's information, including the logo, category, number of connections, and their status.

You can click the arrow to collapse and expand the side pane. Use **Search** to find any value in the side pane.

## &#x20;Viewing More Connection Information

Click **Adapter Profile** in the side pane to display a summary of the connection configuration for each adapter. Each connection and its status are displayed in separate rows. Click **Adapter Connections** at the top of the page to view further information about the Adapter connections, or **Adapters Fetch History** to view the fetch history filtered by that adapter.

<Image alt="Adapter Profile Adapter Fetch History.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Profile%20Adapter%20Fetch%20History.png" />

In the **Advanced Settings** section, you can configure the following:

* [Adapter Configuration](/docs/advanced-settings) (Advanced Settings for each adapter)
* [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
* [Ingestion Rules Configuration](/docs/setting-adapter-ingestion-rules)
* [Discovery Configuration](/docs/adapter-discovery-configuration)

## Adding Adapter Memos (Editable Information)

Use **Adapter Memos** to add editable text to an adapter. This is useful when you want to draw attention to the adapter, for example, to remind another team to review, add an adapter as a favorite, and more. The Adapter Memo is displayed as a banner at the top of the Adapter Profile page. In addition, it is displayed in the adapters list either on the tile as a tooltip or as a column in the list.

**To add an Adapter memo:**

1. From the 3-dot menu at the top of the Adapter Profile page, choose **Add Adapter Memo**.

2. The Adapter memo dialog opens. Enter the text you want.

3. Select **Save**.

The adapter text is now displayed as a banner at the top of the adapter profile page.

**Deleting a Memo**

To delete text, choose **Edit Adapter** from the 3-dot menu and select **Clear memo**.

## Searching for Settings

Use the Adapter Profile page to search for settings in two areas:

### Search Connections

You can search for information about connections using the **Connections Search bar**. Enter any value to search the connections table.

### Search Settings in Side Pane

Enter search text in the **Search** bar in the left pane to easily search the **Connections** and **Configuration** settings names, as well as the titles and field names in the configuration pages for any setting that you need. This includes searching to find any Advanced Configuration setting for that adapter. As soon as you start entering text in the search bar, a list of options containing the search text appears, with the search text highlighted in blue.

Once you have results, select the entry you need, to jump to it. Click 'X' on the right side of the search bar to close the list of options.

#### Adding a New Connection

Click **Add Connection** to add a new connection for this adapter. See [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

#### Using a Gateway

An Axonius Gateway is required to connect adapters whose sources are accessible only by an internal network, and not from the primary Axonius instance, whether Axonius-hosted (SaaS) or customer-hosted (on-premises/private cloud). From the 3-dot menu, select **Manage Gateways** to add a Gateway for this adapter if needed.

For details about configuring and installing the Axonius Gateway, see [Installing the Axonius Gateway](/docs/installing-axonius-gateway).