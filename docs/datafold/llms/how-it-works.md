# Source: https://docs.datafold.com/deployment-testing/how-it-works.md

# Source: https://docs.datafold.com/data-explorer/how-it-works.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How It Works

> The UI visually maps workflows and tracks column-level or tabular lineages, helping users understand the impact of upstream changes.

Our **Data Explorer** offers a comprehensive overview of your data assets, including [Lineage](/data-explorer/lineage) and [Profiles](/data-explorer/profile).

You can filter data assets by Data Connections, Tags, Data Owners, and Asset Types (e.g., tables, columns, and BI-created assets such as views, reports, and syncs). You can also search directly to find specific data assets for lineage analysis.

<Frame caption="Data App Lineage Overview">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9014fc5bee3d6f583a7ea851cf7558fe" data-og-width="1703" width="1703" data-og-height="887" height="887" data-path="images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8a1a5e2cfab0c5b299b49a93215ccd01 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=630385a4c30cf26ebdb5c1c6e8cde749 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a94f066e41e1a6776f1b0f0bfa1876a4 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6ea25f18b750438941c9fd88dfe044fe 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=df229108a49b3697e09fa89ceea0369e 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_overview-3ffe6ae5a34c4e7d8918fae232eb1ed1.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=cdb6e9c57eb24c8b9f6fb2afa82e7e82 2500w" />
</Frame>

After selecting a table or data asset, the UI will display a **graph of table-level lineage** by default. You can toggle between **Upstream** and **Downstream** perspectives and customize the lineage view by adjusting the **Max Depth** parameter to your preference.

<Frame caption="Lineage Graph">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e55cacaf6922d256a43f3f78d90ea8b4" data-og-width="1703" width="1703" data-og-height="767" height="767" data-path="images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b4f9bf05eb17c2adb144347d3fe1b778 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c815bd96fa6fdb0ca3a4a534daa30288 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d000be10b365da1e8e06ba4e952def9d 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=2f4b67b0d071d16c4b05f7e8f687b3b4 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=90b34018ad4eea7f9a50d48d2f9680a6 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph-c33d286a7a8c4787f229e5590d32d2ff.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=179c1da5fc08e093049589ac22aebbb0 2500w" />
</Frame>
