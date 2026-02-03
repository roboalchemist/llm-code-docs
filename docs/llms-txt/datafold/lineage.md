# Source: https://docs.datafold.com/data-explorer/lineage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Lineage

> Datafold offers a column-level and tabular lineage view.

## Column-level lineage

Datafold's column-level lineage helps users trace and document the history, transformations, dependencies, and both downstream and upstream processes of a specific data column within an organization's data assets. This feature allows you to pinpoint the origins of data validation issues and comprehensively identify downstream data processes and applications.

To view column-level lineage, click on the **Columns** dropdown menu of the selected asset.

<Frame caption="Lineage Graph Columns Dropdown">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a02dc2c18664786f79cf7bd4524e704e" data-og-width="1288" width="1288" data-og-height="717" height="717" data-path="images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9c130d844b643b166ae9c463cfcaadd8 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6444916bc9372372c91ebbe23fb182b1 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=661b8a083b296f41c04cf75e14b2a87a 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=8e89ac4be0530963c65fe8e57005299b 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f34ded861320eacb7669d0ce3854d48a 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_lineage_graph_columns-97a1aa84140dc7bd0b242eb70d6e5d81.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=493551ea4043f4bb8a70e8fc9a53bd07 2500w" />
</Frame>

### Highlight path between assets

To highlight the column path between assets, click the specific column. Reset the view by clicking the **Exit the selected path** button.

<Frame caption="Selected Path in Lineage Graph">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=0e261d393437069ff59ed1dd705569d8" data-og-width="1293" width="1293" data-og-height="704" height="704" data-path="images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=85ec0c08ca5571b544020a049a15e129 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=4ad457085f4061895693d9726c70a31f 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b7c97e3362a57d82b8b1789a445b7d51 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c5863c1fe1ca5b72c4d1501de23ffeb2 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=f5057227221485113c49196dbf14838c 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_app_lineage_selected_path-ae2fb8bab8b62f9479a6e148a399bc5a.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=72bb9126db549b41e5c72af6ea5abcba 2500w" />
</Frame>

## Tabular lineage

Datafold also offers a tabular lineage view.

You can sort lineage information by depth, asset type, identifier, and owner. Click on the **Actions** button for further options:

<Frame caption="Tabular Lineage Actions Dropdown">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=a2b72b5aafae515768c8f6bf8163ce66" data-og-width="1354" width="1354" data-og-height="432" height="432" data-path="images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=3daefd5b54ef180640eb3deb64e113bd 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=081c4d17bebe79f6dccc8f5f3d359f49 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=bfee4d7eda4bbf77d5fba112221e992e 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=9fa959dcf2358129f123981519ed7ef3 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=16970be473f622f0f0e9abd6ceca2fa0 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_dropdown-b583e8f59c747058d8a5c95ed6d12843.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=920fe4f1ceca3857b536787d4a9980a9 2500w" />
</Frame>

### Focus lineage on current node

Drill down onto the data node or column of interest.

### Show SQL query

Access the SQL query associated with the selected column to understand how the data was queried from the source:

<Frame caption="Show SQL Query in Tabular Lineage">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=285cc3de38895e398d74761a28927821" data-og-width="1229" width="1229" data-og-height="843" height="843" data-path="images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=f12dcffce34beaa8ad4bfb0434e2333d 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=e96b0225d99ce65bc67d0975b8b0377a 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=f1500087ef7bde586d1bd2d86b856bd2 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=bf8960aabf1aaf015413805961daec3c 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=17e50d7085c2a4b7a5419343f68e3695 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_show_sql_code-da905cea8201954e3b0eb17f3fe108de.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=db96f6c20a7785ad87267bff806439ba 2500w" />
</Frame>

### Show usage details

Access detailed information about the column's read, write, and cumulative read (the sum of read count including read count of downstream columns) for the previous 7 days:

<Frame caption="Usage Details in Tabular Lineage">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=962e7831072bdca9461ea7af185013ba" data-og-width="822" width="822" data-og-height="386" height="386" data-path="images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=0934f90a0698e59d071c0f902a1617b7 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=756536e2c1a7e72138599791b8cd5391 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=122bbab0f679498212f36d1809e50201 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=5d7834b2f9f087f922affb5f3aa41c98 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=77a66bcd0c894b7d96acee1dd3277a71 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_usage_details-c0462ebd7bee2bc769169ff2b7640d56.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=96229297db67384394c45837691729a0 2500w" />
</Frame>

## Search and filters

Datafold offers powerful search and filtering capabilities to help users quickly locate specific data assets and isolate data connections of interest.

In both the graphical and tabular lineage views, you can filter by tables or columns within tables, allowing you to go as granular as needed.

<Frame caption="Search and Filter in Tabular Lineage">
  <img src="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=e43f245bfe7f2a29932374343f0dd517" data-og-width="1351" width="1351" data-og-height="317" height="317" data-path="images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=280&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=a5a1facf226109031703a89d1f5a05bd 280w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=560&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=6a28c0454db7627b922a1da187fef03f 560w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=840&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=8df129d079244a5d215ac03e697d6cc8 840w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=1100&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=6c435a95a550e571ebc81efade558be4 1100w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=1650&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=50cdbd69157005ac330044d95380659c 1650w, https://mintcdn.com/datafold/4ZNRDufNo9R1p08Q/images/tabular_lineage_actions_search-f5cef28a24e5a1603e5c04d9696a4ff8.png?w=2500&fit=max&auto=format&n=4ZNRDufNo9R1p08Q&q=85&s=65de7f503af7c341b30029275457241c 2500w" />
</Frame>

### Table filtering

Simply enter the table's name in the search bar to filter and display all relevant information associated with that table.

### Column filtering

To focus specifically on columns, you can search using a combination of keywords. For instance, searching "column table" will display columns associated with a table, while a query like "column dim customer" narrows the search to columns within the "dim customer" table.

## Settings

You can configure the settings for Lineage under Settings > Data Connections > Advanced Settings:

<Frame caption="Lineage Advanced Settings">
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=685c29c694dcf151d533fb4d6922293f" data-og-width="1180" width="1180" data-og-height="581" height="581" data-path="images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=28e503fd88a4b984ee5657bd1e55c1ae 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9fdeb699720d9174b6fe8ba74a505cbd 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d960bb0706bce3d3d75e16d75d52db7d 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be841f4e6e774ab5b146b2eae9cb5829 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=b08aa127e50c1476119ce04388cb927d 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/lineage_advanced_settings-8787d8f5b01d1a6572b2d73f486ad49a.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f3ce489186e05783c2855f6cd8796520 2500w" />
</Frame>

### Schema indexing schedule

Customize the frequency and timing of when to update the indexes on database schemas. The schedule is defined through a cron tab expression.

### Table inclusion/exclusion

You can filter to include and/or exclude specific tables to be shown in Lineage.

When the inclusion list is set, only the tables specified in this list will be visible in the lineage and search results.

When the inclusion list is not set, all tables will be visible by default, except for those explicitly specified in the exclusion list.

### Lineage update schedule

Customize the frequency and timing of when to scan the query history of your data warehouse to build and update the data lineage. The schedule is defined through a cron tab expression.

## FAQ

<AccordionGroup>
  <Accordion title="How is lineage computed?">
    Datafold computes column-level lineage by:

    1. Ingesting, parsing and analyzing SQL logs from your databases and data warehouses. This allows Datafold to infer dependencies between SQL statements, including those that create, modify, and read data.
    2. Augmenting the metadata graph with data from various sources. This includes metadata from orchestration tools (e.g., dbt), BI tools, and user-provided documentation.
  </Accordion>

  <Accordion title="Is there a programmatic way to retrieve lineage?">
    Currently, the schema of the Datafold GraphQL API, which we use to expose lineage information, is not yet stable and is considered to be in beta. Therefore, we do not include this API in our public documentation.

    If you would like to programmatically access lineage information, you can explore our GitHub repository with a few examples: [datafold/datafold-api-examples](https://github.com/datafold/datafold-api-examples). Simply clone the repository and follow the instructions provided in the `README.md` file.
  </Accordion>
</AccordionGroup>
