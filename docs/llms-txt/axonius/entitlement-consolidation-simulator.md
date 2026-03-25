# Source: https://docs.axonius.com/docs/entitlement-consolidation-simulator.md

# Using the Entitlement Consolidation Simulator

Use the Entitlements Consolidation simulator to identify and reduce redundancy within your organization's access entitlements. It analyzes your organization's applications and systems to find duplicate or highly similar entitlements that have been granted via groups or roles. The outcome of the analysis is to recommend merging or consolidating these redundant access points, which in turn helps to reduce the overall complexity of your access landscape and streamlines how access is managed across your enterprise.

Key capabilities:

* Identify entitlements with overlapping permissions.
* AI/ML-based suggestions to consolidate duplicate or similar entitlements across applications, streamlining your access management.
* Streamline the process of merging redundant entitlements.

There are two use case scenarios:

* Find the entitlements with 100% the *exact* same nested permissions.
* Find entitlements that have *similarity* in terms of overlapping of permissions. An IAM admin can consider consolidating groups or roles that are not 100% the same but close.

When using the simulator, you select the adapter connection related to the entitlements you want to evaluate.

**To open the Entitlements Consolidation simulator:**

1. From the Profiles page, click **Simulators** and then **Entitlements Consolidation**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AccessEntitlementSim.png)

   When the simulator opens, entitlements fetched with the first adapter connection are displayed in the graph.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntitlementConsolidationPage.png)

2. Expand the left panel.

<Image align="center" alt="EntConsolidateExpandPanel.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntConsolidateExpandPanel.png" />

3. If you want, select a different adapter connection from the **Adapter connection scope** list.
4. From **Entitlement types**, select whether to show entitlements granted to **Groups** or **Roles**.

<Image align="center" alt="EntConsolidatePanel.png" border={false} width="275px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntConsolidatePanel.png" />

5. Under **Profiles**, you can search the list of profiles and select the one you want. In the Source list, select whether to view **Manually** created profiles or **Suggested** profiles.
   The simulator graph updates as you make your selections.

The **Entitlement Consolidation** page has three sections:

* The right drawer lists the available adapter connections, allows you to select which types of entitlements to show on the graph: Group or Role, and lists the available profiles. Some profiles may be suggested by Axonius' AI engine.
* The main part of the page is the simulator graph.
* The left drawer is the [Profile preview](/docs/using-the-role-mining-simulator#viewing-the-profile-review) and lists the entitlements and identities represented by the selected nodes. It also gives you the capability to create a new profile (logical group of entitlements) from the listed entitlements.

Hover over a node to see information about that entitlement.

<Image alt="EntCosolidHover.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntCosolidHover.png" />

The following information is displayed:

* The number of entitlements represented by the node in parentheses next to the popup title.
* **Account** - The account name through which the entitlement was fetched.
* **Entitlement** - The name of the entitlement.
* **Type** - The entitlement type: Group, Application, Permission, Resource.
* **Identities** - The number of identities that have been granted this entitlement.

## How the Graph Works

The Entitlement Consolidator graph is specifically designed for analyzing entitlement and identity information.

### Graph Input and Output

The input, the scope, of the simulator is the identity and entitlement data fetched via the selected adapter connection. This is the data that the Axonius ML engine will analyze.

The output is the graph showing the nodes where each node represents one entitlement.

Select an adapter connection to focus the simulation on specific segments of your organization or system. The graph only shows entitlements granted to identities that are fetched via the selected adapter connection. For example, if you have multiple Okta accounts and each has it's own adapter connection, you can select a particular connection to simulate the entitlements granted via that Okta connection.

### Interpreting Graph Nodes

You can analyze entitlements granted by role or by group. Each node in the graph represents either a group or a role.

The location of the nodes on the graph are based on the similarity of the nested permissions each entitlement has. A group or role may inherit entitlements from other groups or roles. When a group is a member, or child, of another group, the child inherits entitlements from the parent. These are nested permissions. The simulator shows all entitlements both directly assigned or inherited from a parent group or role.

The color of the node indicates how many groups or roles with a similar or exact list of nested permissions. The darker the color of the node is the more groups or roles with 100% overlapping of nested permissions.

When there are groups or roles that have the same or almost the same entitlements, consider consolidating them into one group or role to simplify management.

The following example illustrates groups in Entra ID. The darker node shows that there are 2 groups with 100% match of nested permissions.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntraIDGroups.png)

This example shows that both groups in the graph have the exact same entitlements.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntraIDGroupsIdenticalEntlmnts.png)

The closer the nodes are, the more groups or roles have the same or nearly the same entitlements. A darker node indicates that multiple groups or roles have the exact same entitlements.

Overlapping nodes indicate that the entitlements are granted to some of the same groups or roles but not an exactly matching list.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RM-OverlappingNodes.png)

## Viewing the Profile Review

Use the Profile Review drawer to see a list of selected entitlements and create profiles for entitlement groups commonly granted together. Additionally, you can see a list of all identities that have the selected entitlements. Also, by scrolling the lists you can get a quick glance whether there are anomalies and there are identities that should not have the selected entitlements.

**To view the Profile Preview drawer:**

1. Select the nodes you want to group together.
2. Right-click and select **View Entitlements**.
3. The **Profile Preview** drawer opens listing the entitlements of the selected nodes.
   The drawer has two tabs: Entitlements and Identities
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProfilePreviewPane.png)

You can filter the list of *entitlements* by the following:

* **Search** - Enter text into the search box. All fields are searched for the entered text.

You can filter the list of *identities* by the following:

* **Search** - Enter text into the search box. All fields are searched for the entered text.
* **Match any entitlements** *(default)* - Identities that have at least one of the selected entitlements.
* **Match all entitlements** - Lists identities that have all the selected entitlements.
* **Missing some entitlements** - Lists identities that do not have some of the selected entitlements.
* **Missing all entitlements** - Lists all identities within the applied scope that have none of the selected entitlements.

Click **Reset** to clear the filters.

### Creating a New Profile from Selected Entitlements

You can create a new profile from the entitlements selected on the graph. This is useful when there are nodes (entitlements) that are close together indicating that many identities have these entitlements. Creating a profile makes it easier to manage the entitlements and who gets them.
See [Working with Profiles](/docs/working-with-profiles) to learn how to create and manage profiles.

<Image alt="ProfilePreview.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProfilePreview.png" />

## Zooming, Panning, and Selecting Nodes

Use the tools in the lower-left corner of the graph to zoom in and out, pan the graph, and select nodes.

**To zoom in or out:**

* Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RoleMining-ZoomIn.png) or ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RoleMining-ZoomOut.png) .

**To pan the graph:**

* Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RoleMining-Pan.png) and drag the graph to the position you want.

**To select nodes:**

* Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RoleMining-Select.png) and drag over the nodes you want to select.

## Filtering the Simulator Graph

You can filter the data to show only what you want on the graph. Using the filter bar at the top you can filter by:

* **Search** - Enter text to find matching nodes.
* **Entitlement types** - Show only entitlements of a specific type.
  * Application
  * Group
  * Permission
  * Resource
  * Role

Once you select criteria the graph is filtered immediately.
Click **Reset** to clear all filter selections.