# Source: https://docs.axonius.com/docs/peer-group-simulator.md

# Peer Group Simulator

Use the Peer Group Simulator to compare the individual identity access and entitlements against a defined set of similar individuals or entities, known as peers. This set of identities is called a "peer group".

The simulator is useful in identifying excessive permissions or outliers by highlighting deviations from the norm within the peer group. This helps detect entitlement drift and prevents security risks by ensuring that employees do not accumulate unnecessary or excessive permissions over time.

Most peer group members have the same set of entitlements. When a peer group member has different entitlements than the rest of the group, there may be a security issue.

By visually comparing a team member's entitlements against those of the rest of the team, differences and similarities are easier to understand. This can highlight key insights that might be missed in text-based reports.

<Callout icon="📘" theme="info">
  Note

  A peer group is not a Group asset type. A peer group is the set of identities that match the defining attributes using the options described below.
</Callout>

A team is defined as a minimum number of employees that share the same group-defining attributes. This is configurable in System Settings. See [Peer Group Analysis Settings](/docs/configuring-data-processing-settings#peer-group-analysis-settings).

By default, once a day Axonius fetches information on all managed identities and compares several parameters such as excessive entitlement count. This can be configured in Settings. See [Configuring Discovery Settings](/docs/configuring-discovery-settings).

* To access the Peer Group Simulator, hover over a managed identity in the [Managed Identities](/docs/managed-identities-page) page and click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PeerGroupAnalysisSimulatorHoverIcon.png).

<Image align="center" alt="ManagedIdentities-SimulatorHoverIcon.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManagedIdentities-SimulatorHoverIcon.png" />

The Peer Group Simulator consists of two side-by-side graphs. The graph on the left shows the selected managed identity and related entitlements. The graph on the right shows the comparison peer group and the entitlements granted to each member of the group.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PeerGroupSimulator.png)

Each node represents a specific entitlement.

* The color and other attributes of the node indicate the similarities or differences between the entitlements of the individual selected identity and the peer group as a whole.
* The node label indicates the source of the entitlement and the adapter connection through which the entitlement was discovered.

You can move the nodes in the graph by clicking and dragging.

<Image alt="PeerGroupSim-SelectedIdentityEntNode.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PeerGroupSim-SelectedIdentityEntNode.png" />

The green ring around the icon tells you the percentage of identities in the graph have that entitlement. Since there is only one identity in this graph that has the entitlement, the ring is full and shows that 100% of the identities have the entitlement. Nodes in the peer group graph may not all be 100% indicating that not all peer group members have that entitlement.

Use the node legend to understand the meaning of the different nodes.

Click **Legend** in the upper-right corner above the simulator to display the node legend.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PeerGroupSimLegend.png)

* Entitlement status:
  * **Assigned to both sides** - Both the selected identity and the peer group have this entitlement.
  * **Assigned to this member only** - Only the selected identity has this entitlement.
  * **The sub-entitlements are assigned to all group members** - All peer group members have this entitlement.
  * **Assigned only to other members of the team** - An entitlement that the examined member doesn't have but most of the other users in the group do have it.
  * **The sub-entitlements are assigned to the examined member as well** - All peer group members have this entitlement including the examined member.
  * **Assigned to a small portion of the team** - Indicates a partially drifted entitlement. An entitlement that the examined member and their group have, but it is still considered to be drifted related the threshold of how many within the group also have the same entitlement. This is configured in [Peer Group Analysis Settings](/docs/configuring-data-processing-settings#peer-group-analysis-settings).

* Indications:
  * Number of nested entitlements
  * Includes administrative entitlements
  * Sub entitlements
  * Percentage of members assigned the entitlement.

### Searching the Nodes

Use the **Search** field and the filter lists to show the entitlements you want to view. Search and filters apply to both graphs simultaneously.

<Image align="center" alt="PGSSearch.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PGSSearch.png" />

#### Filtering by Entitlement Status

You can filter the entitlement nodes by their status.
From the **Entitlement Status** filter, select the entitlements you want to display.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EntitlementStatusFilter\(1\).png)

### Finding Drifted Entitlements

Drifted entitlement calculation is done immediately on accessing the Peer Group Analysis simulator.

There are 3 attributes to a drifted user:

* Is User Drifted
* Drifted entitlements
* Last Drift Detection Date

### Download CSV

You can download a copy of the information shown in the graph to a CSV file.

To download a CSV file of the information presented in the graphs, click **Download CSV** above the upper-right corner of the simulator.