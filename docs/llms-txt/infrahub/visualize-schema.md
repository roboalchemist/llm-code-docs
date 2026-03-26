# Source: https://docs.infrahub.app/vscode/guides/visualize-schema.md

# How to Visualize Your Schema

If you want to explore and understand the structure of your Infrahub schema, this guide shows you how to use the Schema Visualizer to view nodes, relationships, and attributes in an interactive graph.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Infrahub VSCode extension installed and configured
* At least one Infrahub server configured and online
* Network access to your Infrahub instance

## Step 1: Open the Schema Visualizer[​](#step-1-open-the-schema-visualizer "Direct link to Step 1: Open the Schema Visualizer")

1. Open the **Infrahub Servers** panel in the Activity Bar
2. Locate your connected server (indicated by a green status dot)
3. Click the graph icon next to the server name

![Infrahub Server Tree with Graph Icon](/assets/images/infrahub-server-tree-graph-e9daa17f9434791d44bef34236681290.png)

Alternatively, right-click on the server and select **Visualize Schema** from the context menu.

## Step 2: Select a branch[​](#step-2-select-a-branch "Direct link to Step 2: Select a branch")

When prompted, select the branch whose schema you want to visualize. The extension fetches the schema directly from the server for the selected branch.

## Step 3: Explore the schema graph[​](#step-3-explore-the-schema-graph "Direct link to Step 3: Explore the schema graph")

The visualizer displays your schema as an interactive graph with nodes representing schema types and edges representing relationships.

![Schema Visualizer Main View](/assets/images/infrahub-graph-b80d49e589dc544429944cd11d0d1f37.png)

The **Schema Overview** panel in the top-left shows statistics:

* **Visible**: Number of schemas currently displayed
* **Total**: Total schemas in the branch
* **Nodes**: Regular schema nodes
* **Profiles**: Profile configurations
* **Templates**: Template definitions
* **Generics**: Generic/reusable types

### Navigate the graph[​](#navigate-the-graph "Direct link to Navigate the graph")

* **Pan**: Click and drag on the background
* **Zoom**: Use mouse scroll or the zoom controls in the bottom toolbar
* **Move nodes**: Click and drag individual schema nodes
* **Select node**: Click on a node to view its details

## Step 4: Filter schemas[​](#step-4-filter-schemas "Direct link to Step 4: Filter schemas")

Click the filter icon in the bottom toolbar to open the Filter Schemas panel.

![Filter Panel](/assets/images/infrahub-filter-panel-6e10589ec24e6830d665ce493024b8f0.png)

The filter panel provides:

* **Search**: Type to find schemas by name, label, or kind
* **Namespace toggles**: Show or hide entire namespaces
* **Individual toggles**: Enable or disable specific nodes

By default, the visualizer hides schemas from the Core and Builtin namespaces to reduce visual clutter. Enable them in the filter panel if needed.

## Step 5: View node details[​](#step-5-view-node-details "Direct link to Step 5: View node details")

Click on any schema node to open the details panel on the right side.

![Node Details Panel](/assets/images/infrahub-graph-node-detail-a7e773143f278158cb543563f2b51294.png)

The details panel shows:

### Properties[​](#properties "Direct link to Properties")

* **Namespace**: The schema's namespace
* **Name**: The schema name
* **Kind**: Full identifier (Namespace + Name)
* **Description**: What this schema represents
* **Inherit from**: Parent schemas this type inherits from

### Attributes[​](#attributes "Direct link to Attributes")

Lists all attributes with their:

* Name and type (Text, Number, Boolean, Dropdown)
* Flags: optional, unique, read-only
* Inheritance status (inherited attributes shown with "inherited" label)

### Relationships[​](#relationships "Direct link to Relationships")

Lists all relationships with:

* Relationship name
* Cardinality: `one` or `many`
* Target schema type
* Inheritance status

## Step 6: Use the toolbar controls[​](#step-6-use-the-toolbar-controls "Direct link to Step 6: Use the toolbar controls")

The bottom toolbar provides visualization controls:

![Bottom Toolbar](/assets/images/infrahub-bottom-menu-bar-8f6aeee413fcf312c53367525a712645.png)

From left to right:

| Control            | Function                                               |
| ------------------ | ------------------------------------------------------ |
| **-**              | Zoom out                                               |
| **Fit**            | Fit all nodes in view                                  |
| **+**              | Zoom in                                                |
| **Smooth/Stepped** | Toggle edge style between curved and right-angle lines |
| **→**              | Auto-layout horizontally (left to right)               |
| **↓**              | Auto-layout vertically (top to bottom)                 |
| **Filter**         | Toggle the filter panel                                |
| **Reset**          | Reset view to default state                            |
| **Export**         | Download as PNG or SVG                                 |

## Step 7: Export the visualization[​](#step-7-export-the-visualization "Direct link to Step 7: Export the visualization")

To save your schema visualization:

1. Arrange the graph as desired
2. Click the export button (download icon) in the toolbar
3. Choose PNG or SVG format
4. The image downloads with your current view

Exported images are useful for documentation, architecture reviews, and sharing schema designs with team members.

## Validation[​](#validation "Direct link to Validation")

To verify the visualizer is working correctly:

1. **Connection check**: Ensure your server shows a green status indicator
2. **Branch selection**: Verify you can see and select branches
3. **Schema loading**: The overview panel should show non-zero counts
4. **Interaction**: Click nodes to confirm the details panel opens

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Visualize Schema option is disabled[​](#visualize-schema-option-is-disabled "Direct link to Visualize Schema option is disabled")

* The server must be online (green status indicator)
* Check your network connection to the Infrahub instance
* Verify server credentials in extension settings

### Schema shows zero nodes[​](#schema-shows-zero-nodes "Direct link to Schema shows zero nodes")

* The selected branch may have no custom schemas defined
* Enable Core and Builtin namespaces in the filter panel
* Check if the branch exists and has schema data

### Graph is too cluttered[​](#graph-is-too-cluttered "Direct link to Graph is too cluttered")

* Use the filter panel to hide unnecessary namespaces
* Use auto-layout to organize nodes automatically
* Zoom out to see the full structure

### Export produces blank image[​](#export-produces-blank-image "Direct link to Export produces blank image")

* Ensure nodes are visible in the current view
* Try using "Fit" before exporting
* Check that your browser allows downloads

## Related resources[​](#related-resources "Direct link to Related resources")

* [How to Manage Branches](/vscode/guides/manage-branches.md)
* [Understanding Schema Validation](/vscode/topics/schema-validation.md)
* [Extension Commands Reference](/vscode/reference/commands-settings.md)
