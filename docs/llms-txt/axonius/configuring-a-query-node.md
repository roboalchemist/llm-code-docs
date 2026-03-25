# Source: https://docs.axonius.com/docs/configuring-a-query-node.md

# Configuring a Query Node

A **Query** node in an Axonius workflow is a powerful tool for dynamically fetching and using data from your environment. It allows you to build automations that require up-to-date information without needing to change the workflow's original trigger. The Query node enables you to perform lookups and conditional checks on your data, making your workflows more intelligent and adaptable. This node can be configured to fetch data for various asset types, such as Users, Devices, or Software, using saved queries and those that you customize. The results are then used for subsequent actions, such as bulk transformations or conditional logic.

<Callout icon="📘" theme="info">
  Note

  You can place a Query node after any triggering node (e.g., Manual or Scheduled) or another processing node.
</Callout>

## Key Features

* **Dynamic Data Retrieval** - Fetch data from Axonius based on dynamic conditions. This is useful for workflows where the user input or a previous step's output determines what data is needed.

* **Flexible Configuration** - Configure the Query node to work with different asset types (e.g., Users, Devices, Software) and use dynamic expressions within the query's filters, allowing for complex, multi-faceted data lookups in a single node.

* **Actionable Output** - The node's output provides the number of returned assets and the full result set. This data can be used in subsequent steps, like foreach loops to run an action on each asset, or in condition nodes to perform checks based on the query results.

* **Bulk Operations** - When placed at the start of a workflow and followed by an action, a Query node supports bulk operations, enabling you to process large sets of data efficiently.

## Use Cases

* Getting all users in a specific department.
* Checking if an email or username already exists in your organization.
* Using asset data to calculate the next available identity.

## Configuring the Query Node

You can configure a **Query** node with one or more queries, each of which can be a saved or a new custom query. The assets resulting from all queries in the node are combined (ORed), and the subsequent nodes in the Workflow are processed on this final asset list.

**To configure the Query node**

1. Click the **Query** node to open its configuration drawer.
   ![QueryNode1.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryNode1.png)

2. In **Name**, type a name for your query. The tab and node are automatically updated with this name.

3. Under **Define the query expression**, choose to configure a [**Custom** query](#configuring-a-custom-query) using the Query Wizard or select a [**saved query**](#using-a-saved-query). To confirm your criteria, click the **View Query Results** link; the Assets page opens in a new tab, displaying the list of assets matching your query’s criteria (displayed in the Search bar). This process ensures you can validate your query without interrupting the node's configuration.

4. To add another query to the **Query** node, click the **+ Add** button and repeat step 3 for either a custom or saved query.

### Configuring a Custom Query

Use this method to configure a **Query** node with a new query tailored to your workflow's dynamic needs. Subsequent nodes will run on the assets resolved from this customized query.

1. In the Queries section, click **Custom**.
2. From the **Module** dropdown, select an asset type (such as Users, Devices, or Software). This opens the Workflow Data repository, allowing you to use data from previous nodes when configuring the query (in the next step).
3. [Configure your query using the Query Wizard](/docs/query-wizard-and-query-filter#working-with-the-query-wizard). In the **Field Value** box, you can type a value or [copy a field value from the Workflow Data dialog](/docs/using-workflow-data-from-previous-nodes#selecting-a-field-from-the-workflow-data-bank) to set dynamic conditions.

### Using a Saved Query

1. In the Queries section, click **Saved query**.
2. From the **Module** dropdown, select an asset type (such as Users, Devices, Software).
3. From the **Query Name** dropdown, do one of the following:
   * Select a saved query from the list.
   * Click **+ Add Query** to [create a new query](/docs/chart-query-configuration#creating-a-new-query).