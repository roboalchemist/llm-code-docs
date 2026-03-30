# Source: https://docs.axonius.com/docs/customizing-node-labels.md

# Customizing Node Labels

You can now customize the label of nodes in an asset graph. By selecting an adapter and a field, the field value that applies to that node will be used as the label. This is useful, for example, when viewing a graph of devices by owner and using the device owner name or email address as the label. Another use case is when creating [reports](/docs/reports-page). The labels of the graph could be customized to match the report contents. Custom label settings can be set as the system default so that all assets of this type will be labeled with the appropriate field value.

<Image align="center" alt="AssetGraph-CustomizeNodes-1.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-CustomizeNodes-1.png" />

**To customize node labels:**

1. On the **Asset Graph** page, in the upper-right corner, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomizeLabelsIcon.png) (Customize Nodes).

   In the drawer, there are two lists of asset types. Asset types that currently appear in the graph are listed under **Displayed assets**.

   <Image align="center" alt="CustomizedLabelsDisplayedAssets.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomizedLabelsDisplayedAssets.png" />

   Asset types that are not currently displayed in the graph are listed under **Additional assets**.

   <Image align="center" alt="CustomizedLabelsAdditionalAssets.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomizedLabelsAdditionalAssets.png" />

2. In each list, select the asset types to customize and then an adapter and field for each. The value of the field will be used as the label for that asset type.

3. Click **x** to remove an asset type from the list.

4. To keep these selections as the system default for the configured asset types, select **Set as system default**.

<Image align="center" alt="CustomizedLabelsFullDrawer.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomizedLabelsFullDrawer.png" />

6. To clear all the custom label settings and return to the system defaults, click **Reset to system default**.
7. Click **Apply**. The label selections are applied to the graph.

In the example below, email addresses from the *Email address* field are used as labels for the devices:
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomizeAssetGraphLabelsExample.png)