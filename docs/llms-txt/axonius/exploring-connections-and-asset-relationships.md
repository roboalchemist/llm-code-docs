# Source: https://docs.axonius.com/docs/exploring-connections-and-asset-relationships.md

# Exploring Connections and Asset Relationships

Relationships between assets indicate how they are connected in the environment and are shown as arrows linking the asset nodes in the graph. Axonius discovers these relationships during Discovery and correlation. You can also create [custom relationships](/docs/exploring-connections-and-asset-relationships#custom-relationships) between assets of different types, as well as assets of the same type.

For example, a common relationship between assets of different types is that between devices and users. Devices are accessed by users. A user managing other users is an example of a relationship between assets of the same type.

In the graph, labels indicate the type of relationship between assets. For example:

* **Last Used by** - Indicates there are users associated with the asset.
* **Has** - Indicates that these assets have vulnerabilities associated with them.
* **Affected by** - Indicates other assets that affect another asset, such as settings.
* **Accessing** - Indicates that an asset is accessible or used by another asset, such as users.

<Image alt="AssetGraph-HoverConnectionArrows.png" width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-HoverConnectionArrows.png" />

When some members of one asset group have relationships to some members of another group or individual asset, hover over one of them to see relationship arrows between the assets.

## Exploring Relationships

Use the Explore Relationships drawer to show assets with specific relationships to the node selected. For example, you can show all assets related to Users including related devices, software, managers, and more. You can also select to show the inverse, i.e., assets that have no connection to the selected asset. This is useful when looking for unmanaged assets and other scenarios where the lack of connection is important. See [Managing Custom Relationships](/docs/managing-custom-relationships) for more about creating custom relationships.

![AssetGraph-ExploreRelationshipsDrawer.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-ExploreRelationshipsDrawer.png)

When a large number of assets are selected in the graph, a warning appears that system response time may be affected while the Explore Relationships action is in progress.

For the selected asset, you select a combination of an asset type (devices, software, tickets, users, etc.) and a relationship (Relates to, Used by, Has, Last used by, etc.) between the selected asset in the Asset Graph and the selected asset type. The available asset types and relationships are determined by the selections you make.

**To explore relationships:**

1. Click on the node whose relationships you want to investigate and select **Explore Relationships**.
2. Under **Select asset types**, select the asset types whose connections you want to view. You can select more than one asset type. Note that **Filter Results** is only available when one asset type is selected.
3. Click **Filter Results** to define filter criteria to further refine which assets are displayed in the Asset Graph. See [Filtering Asset Groups](/docs/asset-graph#filtering-asset-groups) for more about creating filters.
4. If you want to explore the default relationship, click **Explore**. Each asset type has a default relationship.
5. If you want to explore other relationships, click **Advanced Options**,  and then, under **Select a relationship** select the relationship you want to explore. Custom relationships also appear in this list. See [Managing Custom Relationships](/docs/managing-custom-relationships) for more about how Relationships work and how to create them.
6. Also under **Advanced Options**, select whether to show assets that are related or unrelated.
   * **Related** *(default)*- Shows assets that have are related to selected asset types.
   * **Unrelated** - Shows the assets that do not have any connection with the selected asset. This is useful when looking for unmanaged assets and other scenarios where the lack of connection is important.
7. Click **Explore**. The results are displayed in the Asset Graph.

For example, to see all assets related to Cisco devices, take the following steps (starting from the bottom of the steps list):
![ExploreRelationships-CiscoExample.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExploreRelationships-CiscoExample.png)

The results are displayed on the graph:

<Image alt="ExploreRelationships-CiscoExampleGraph.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExploreRelationships-CiscoExampleGraph.png" />

The select asset and the number of relationships are shown in the top left of the graph. In this example, Cisco(16).

## Custom Relationships

Create custom relationships to define your own connections between asset types based on your needs and understanding of the environment, business structure, and logical functions.

See [Managing Custom Relationships](/docs/managing-custom-relationships) for more about how relationships work and how to create them.

## Viewing a Single Asset's Adapter Connections

Use Segment by Entity to view an individual asset's adapter connections.

**To view an asset's adapter connections:**

1. Click on a single asset node and select **Segment by entity**.

<Image alt="AssetGraph-BeforeAssetEntity.png" width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-BeforeAssetEntity.png" />

2. The adapter connections are displayed as square icons. The number of assets using the connection is indicated on the node icon.

<Image alt="AssetGraph-AfterAssetEntity.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-AfterAssetEntity.png" />

You can further explore the assets using these adapter connections by expanding and viewing the assets connected to them.