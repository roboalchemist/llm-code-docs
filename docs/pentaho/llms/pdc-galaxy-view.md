# Source: https://docs.pentaho.com/pdc-use/pdc-galaxy-view.md

# Galaxy view

The Galaxy view feature in Pentaho Data Catalog provides a comprehensive visual representation of data assets, providing users with an interactive and consolidated view of their entire data ecosystem. This feature shows the visualization of all available data assets within a single, unified interface to create a visual galaxy of interconnected data assets. You can explore data relationships and visualize the connections and dependencies between varied data assets and data lineage relationships based on metadata and data flows.

To access Galaxy view, on the left navigation menu, click **Galaxy**. The Galaxy view displays the base node and along with all data assets. You can expand any node by clicking on it.

![Galaxy view in Pentaho Data Catalog](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-6b06582af382e7bd0dfeabe58305b89ba554f650%2FGalaxy%20view%3DGUID-DA223A29-3D73-4CCA-96CA-8837643AC001%3D1%3Den%3DLow.jpg?alt=media)

## Data assets in Galaxy view

In Data Catalog, Galaxy view consolidates various data assets into a single visual interface, allowing users to explore relationships and connections between the following categories:

* **Data sources**: The origins of your data, such as databases, tables, and columns for structured data and files in case of unstructured data. See [Exploring your data](https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp) to know more about data sources and their entities.
* **Business glossary:** Business glossary assets are glossaries, categories, and key business terms that standardize data understanding across the organization. See [Business Glossary](https://docs.pentaho.com/pdc-use/pdc-business-glossary) to learn more about business glossaries.
* **Reference data:** Reference data contains data sets defined as authoritative sources within your data environment.
* **Applications:** Application assets, like external applications, groups, and categories help you understand what type of data is linked from an external application. See [Applications](https://docs.pentaho.com/pdc-use/pdc-applications-ug) to learn more about applications.
* **Policies:** Governance policies and standards can be applied to your data assets. For more information, see [Policies and standards](https://docs.pentaho.com/pdc-use/pdc-policies-and-standards-ug).
* **Asset hierarchy:** The structured organization of industrial data generated through data ingestion from Pentaho Edge OT (Operation Technology), defining relationships between various physical components in an industrial operation. See Asset hierarchy to learn more about Asset hierarchy.
* **Metadata rules:** Metadata rules define and govern the structure and management of metadata within your data environment. See the [Metadata rules](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-rules-cp-ag/pdc-manage-metadata-rules-cp/pdc-metadata-rules "mention")for more information.

## Relationship types in Galaxy view

In Data Catalog, Galaxy view shows two types of relationships between the data assets:

### **Parent-child relationship**

The relationship between the parent and child entities within the same hierarchy, such as a relationship among database, table, and column or a relationship among glossary, category, and term. These relationships are shown with a solid line.

![Parent-child relationship in Data Catalog Galaxy view](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-988869629ec3ebef8744834617ecf29f1b53f636%2FParent-child%20relationship%3DGUID-37114110-7AE8-4C48-907E-1A6F15745724%3D1%3Den%3DLow.jpg?alt=media)

### **Association relationship**

An association relationship is a connection between the various entities within different hierarchies. It can include relationships between a database and its assigned business terms, policies, policies, or other related entities. Also, it can be the relation between a business term and the associated dictionary and patterns. Association relationships are shown with a dotted line in the galaxy view.

![Association relationship in Data Catalog Galaxy view](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-0bbb1d9a5da5d0bad178345a09b66a20abbc9cec%2FAssociation%20relationship%3DGUID-272BEADC-EEEE-441E-B430-0446C86FEE4D%3D1%3Den%3DLow.jpg?alt=media)

## Key functionalities of Galaxy view

Galaxy view offers several key functionalities to enhance the user experience and facilitate data exploration.

* **Expand and Collapse**: You can click on any node to expand to reveal all children and their relationships or to collapse them to hide these details. This feature gives control over the level of detail shown at any given time.
* **Search and Locate**: The **Search** functionality gives precise results across the data catalog and as a result it expands the nodes which have the results. You can use the **Locate** functionality to search only within expanded nodes and highlight the relationship that has the results.
* **Filters**: You can apply filters to refine the shown data, focusing on specific categories like data sources, rules, glossary terms, applications, policies, and reference data to refine the view of relevant data assets.
* **Node Limit**: Use the node limit to control the number of nodes (or data elements) rendered on the screen for each node at the child level, including relations once to 25, 50, or 75, to allow a clear and manageable view. The node limit applies separately to each hierarchy, not collectively. For example, when you expand a glossary term, it shows up to 25 related data assets such as applications, policies, rules, and so on, but each type is limited to 25. By default, the node limit is set to 25. If the desired entity is not within the first 25 nodes, you can load more to see additional nodes without rendering all of them at once. Once you change the node limit, it will be replicated across future sessions.

Additionally, when you right-click on any node within the Galaxy view, you get the following additional options.

* **Navigate To**: Opens the data asset into its respective canvas view in focus mode, showing detailed information about the selected data asset in a new tab. For example, for a business term, it opens the term in the Business Glossary page with a focused view.
* **View Details**: Opens a side panel that displays key summary information about the selected data asset. Based on your role and access permissions, you can perform basic end-user operations in this panel, such as providing a rating, updating key information, or adding tags to the asset.
* **Show Hierarchy**: Highlights the parent-child relationship tree for the selected node, providing a clear view of its place within the overall data structure.
* **Show Children or Hide Children:** Toggles the visibility of all children related to the selected node.

  **Note:** **Show Children** or **Hide Children** options are available only when the node is expanded.
* **Show Relations or Hide Relations**: Toggles the visibility of relationships between the selected node and other data assets.

  **Note:** **Show Relations** or **Hide Relations** options are available only when the node is expanded and has association relationships.
* **Hide Siblings**: Hides all sibling nodes that are direct descendants of the same parent node as the selected node and helps to focus on a specific branch of the hierarchy without being overwhelmed by unrelated nodes.

  **Note:** The **Hide Siblings** option is available for a node only when it is connected to its parent node.
