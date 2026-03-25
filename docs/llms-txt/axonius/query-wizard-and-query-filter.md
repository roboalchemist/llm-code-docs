# Source: https://docs.axonius.com/docs/query-wizard-and-query-filter.md

# Creating Queries with the Query Wizard

You can create and save queries in the following modes:

* Create queries on assets using the Query Wizard.
* Basic mode using filters to define query parameters. For more information, refer to [Working with Basic Query Mode](/docs/basic-query-mode).
* Create System Queries on Activity logs, Fetch History, and Asset Investigation using filters. For more information, refer to [System Queries (Creating Queries Using Filters)](/docs/creating-queries-filters).

This page explains how to create queries on assets using the Query Wizard.

Use the Axonius **Query Wizard** to create granular queries to understand how assets adhere to their policies. You can define a wide variety of filters, from which you can easily drill down to the assets that match the required search criteria. For example, you can use the Query Wizard to show only Windows device assets that were seen in the last 7 days using filters where the value of the common field **OS: Type** equals Windows and the value of the common field **Last Seen** is within the last 7 days.
![ExampleQuery](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryWizardNew.png)

## Working with the Query Wizard

From the relevant assets page, click **Query Wizard** on the top right corner above the asset table. The Query Wizard definition box opens. The Query Wizard presents options appropriate to the selected asset type.
![QWFirstRow](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryWizardNew2.png)

<Callout icon="📘" theme="info">
  Note

  On the **Aggregated Security Findings** and **Software** pages, the Query Wizard is multi-level to provide vulnerability and software contextualization and help inform prioritization. See [ Creating Queries on Vulnerabilities](/docs/vulnerabilities#creating-queries-on-vulnerabilities) and [Creating Queries on Software](/docs/software#creating-queries-on-software) for more information.
</Callout>

Each row in the **Query Wizard** is a filter expression. You need to define the following elements:

1. WHERE/WHERE NOT switch
2. AND / OR / AND NOT / OR NOT  switch
3. NOT Flag
4. [Source drop-down](/docs/selecting-source-options-in-the-query-wizard)
5. Adapter drop-down
6. Field drop-down
7. [Operator drop-down](/docs/query-wizard-operators)
8. Value field
9. Bracket controls

Once you create a query you can save it for future use. Learn more about [Saved Queries](/docs/saved-queries-devices).

For Devices queries you can use the **[AI Query Assistant](/docs/using-natural-language-to-create-queries)** if it is enabled on your system.

### 1. WHERE/WHERE NOT Switch

Each expression starts with the term WHERE.
You can choose WHERE NOT to negate the complete filter expression and only match assets that do NOT match the complete expression.

### 2. AND / OR / AND NOT / OR NOT Switch

The AND/OR/AND NOT/OR NOT switch is only displayed on the second and subsequent filter rows. When you have more than one filter defined, use AND/OR to control whether all filters are required to match, or if just one filter can match. Use AND NOT/OR NOT to add an additional negation of the filter line, which can be either AND or OR, that is that all filters do not match, or just one filter will not match.

![AND NOT switch.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AND%20NOT%20switch.png)

### 3. NOT Flag

Click the NOT flag to negate the filter line, and only match assets that do NOT match the adapter, field, operator, and value specified.

For example:

<Image width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(217).png" />

means that Axonius will return all devices EXCEPT the devices where the OS type is Windows (including devices where the OS type is unknown or this field doesn’t apply, and not just devices that their OS type is defined and NOT Windows).

### 4. Source Drop-Down

The source drop-down contains the following options:

* **Aggregated Data** (displayed as **ALL**) -   Use **Aggregated Data** to query on all asset  common fields fetched from any of the adapter connections.  **Aggregated Data** is selected by default.
* **Complex Field** (displayed as **OBJ**) - Use Complex Field to query on assets with a specific complex field that meets the specified criteria.
* **Asset Entity** (displayed as **ENT**) -   Use **Asset Entity** to make a query on a specific asset entity, that is, an asset entity fetched from a specific adapter connection.
* **Field Comparison** (displayed as **CMP**) -   Use Field Comparison to compare between adapter field values, and only return assets which match the comparison.
* **Relationship** (displayed at **RLT**) - Use Relationship to query on assets that are connected to each other, i.e. that have a relationship between them, for instance Users that are connected to devices.

Learn more about [Selecting Source Options in the Query Wizard](/docs/selecting-source-options-in-the-query-wizard).

### 5. Adapter Drop-Down

The Adapter drop-down contains a list of all adapters that have fetched data for assets. The adapter you select in this drop-down determines the list of fields displayed in the Field drop-down, which shows fields fetched by the adapter selected. You can quickly search for adapters using the search bar at the top of this drop-down.

The first entry and default selection in this drop-down is **Aggregated** represented with the  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(213\).png) icon. All of the fields for **Aggregated** are the collated values from all of the data that was fetched for all adapters, considered as 'common' fields.

By default, all adapters are selected. You can control the adapter data sources that are used when evaluating a filter for a common field.  You can choose to only evaluate the operator and value query data in a common field from a subset.

You can select the adapter sources that will be searched for  Aggregated Data / common field. When you only select specific adapters to be used for common fields, the ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(213\).png) icon is replaced by ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(811\).png), to show that specific sources are  selected. By default, all adapter sources are queried.

![AdapterDropDown.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterDropDown.png)

### 6. Field Drop-Down

The field drop-down contains a list of all the fields that were fetched for the selected adapter as well as [descriptions for many fields](/docs/field-descriptions). When **Aggregated** is selected in the Adapter drop-down, this is a list of all fields whose data is collated from all adapters.

1. Select a specific adapter or the common field option (![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(213\).png) icon, default option) to search any generic field. Common fields are asset properties retrieved from multiple adapters.

2. Click in the **Field** list. The drop-down lists the available fields by category. Select a category and then a field. As you hover over the field names, a [Field description](/docs/field-descriptions) appears in the right pane.

3. Select the field you want. Use the search bar to search for a specific field name.
   ![FiledDropdown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldDescriptionDropdownNotAggregated.png)

4. To use criteria from a [saved query](/docs/saved-queries-devices), select **Saved Query**.
   1. The Query Name drop-down list appears and displays a list of saved queries you can select for that asset page.
   2. To view a saved query's details, hover over the query name and click the View Query icon. A drawer the query's details opens on the right side of the page.
      ![ViewSavedQuery](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ViewQueryDetails\(1\).png)

#### Complex Fields Display in the Field Drop-Down

Complex fields appear in the field drop-down in a hierarchical display: you can expand each complex field to view all of its child fields, or collapse it to hide them.

![CollapsedComplexFields](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-QMVH30EO.png)

When searching for a field in the Query Wizard:

* If the searched value appears in the title of the complex field, the search results will include the complex field with all of its child fields.
* If the searched value does **not** appear in the title of the complex field, but does appear in the title of one or some of its child fields - the search results will include the complex field with only the child fields that match the search criteria.

**Example**\
By typing "installed" in the Fields search box, we get the **Installed Software** complex field with all of its child fields; However, there's another complex field called **OS Available Security Patches**, which doesn't include the word "installed" - so none of its child fields are listed except for **Installed By**.

![InstalledResults](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-WOZ9MTFX.png)

Learn more about [complex fields](/docs/asset-profile-page-complex-fields).

### 7. Operator Drop-Down

Once a field is selected, you need to select a comparison function from a drop-down list. For each field type there is a list of possible functions. Learn more about [Query Wizard Operators](/docs/query-wizard-operators).

### 8. Value Field

Specify the value to be compared by the field and function. Different relevant value options are enabled according to the field type and the operator/function chosen.

![ValueField.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ValueField.png)

#### Autocomplete Suggestions for Equals Values

On certain fields, when the operator is set to equals the value drop down box displays all of the values that exist in the system, so that you will easily be able to formulate a valid query, without having to guess the exact name of the component on your system.
Once you type 3 letters, the system presents possible values for the field.
For instance, for “Installed Software: Software Name” if you are looking for Chrome start typing 'chr', and a drop down box will appear, showing all the installed software with these letters in it.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Enum%20eg\(3\).png)

<Callout icon="📘" theme="info">
  Note

  Up to 100 values can be displayed in the Value drop down list.
</Callout>

### 9. Parentheses Controls

When defining multiple expressions with a combination of "OR" and "AND" operands between them, usage of parentheses impacts the query definition.

![Parentehse controls.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Parentehse%20controls.png)

In some complex expressions, multiple parentheses may be required. To increase/decrease the number of parentheses, click the up/down arrows in the Parentheses Control.

When you use OR NOT and AND  NO, use of parenthesis is mandatory. You have to close the brackets, otherwise the expression will not work.

You can configure the Query Wizard to display the columns on the Query Results table. Learn about [Working with Columns and Rows in the Query Wizard](/docs/working-with-columns-on-the-query-wizard).

### Expression Indicative Error

When an error occurs for a given expression, an indicative text referring to that error appears in red in the bottom of the **Query Wizard**. Use it to correct the expression.
For example, missing right bracket:
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MissingRightBracket_Query.png)

## Running the Query

When you complete a filter expression, the contents of the asset table are refreshed with the results of your query.   When you finish building the query expression, click **Search**.  The final query expression is displayed in the Query Filter Bar.

Click **Clear** to clear all expressions in the wizard, which also clears the saved query, when used, refreshes the asset table and displays all existing devices.

You can always toggle back to the **Query Wizard**, change and refine the query, and create a multi-filter expression, by adding AND/OR operators between them:

* To add a new expression, click  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(218\).png)
* To remove an expression, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(219\).png)
* To reorder the expressions, hover over the expression to use the drag and drop functionality ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(307\).png)

For each added or removed expression the Asset table results are dynamically updated.

Once you create a query you can save it for future use. Learn more about [Saved Queries](/docs/saved-queries-devices).

You can also include or exclude a specific value from the Assets table directly to the **Query Wizard**, in addition to copying a value from the asset table so it can easily be pasted into the Query Wizard or anywhere else. For more information, see [Including/Excluding Values From Assets to the Query Wizard](/docs/assets-page#includingexcluding-values-from-assets-to-the-query-wizard).

### Running a Query Directly from the Assets Page's URL

A quick way to generate and run a query without using the Query Wizard is to add an Axonius Query Language expression to  the URL of an Assets Page.
In the Assets Page URL, after the Assets Page's name, enter ?aql= and then the Axonius Query Language expression. For example, to run a query from the Devices page, type the following string into the address bar:

`https://domain/assets/devices?aql=("specific_data.data.name" == regex("example", "i"))`

## Saving Queries

After you create a new query, or update an existing one, select **Save As** to  save the query and add it to the **Saved Queries** list for future and advanced use. Saved queries are also used in Enforcement Sets, Dashboard Charts, Reports and more.

### Using a Saved Query as a Filtering Condition in Query Wizard Expressions

You can use a saved query to create complex queries based on pre-defined queries. You can either use a pre-defined query, or a query created by you or another user. You can only select saved queries whose access is not private.

![SavedQueryBased.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SavedQueryBased.png)

## Updating Query Details

Once you configure filters or a Search and saved them as a query, Update Details is available as a drop-down from  **Save As**.
Click  **Update Details** to change any other query details, such as the name, description, tags and folder where it is saved.

## Adding Notes to Query Expressions

Complex queries are constructed in an iterative process, layering expressions to refine results. As queries grow in complexity, the rationale behind specific parameters or conditions can become difficult to recall or interpret. To resolve this issue, you can add notes to individual query expressions. Such notes allow for:

* **Maintainability:** The original query creator can document their logic for future reference when revisiting the query.
* **Collaboration:** Query expression notes provide context for team members reviewing or reverse-engineering the query, ensuring the logic is transparent and understandable.
* **Auditing:** Notes are required to clearly describe query expressions when using Axonius for security audits.

**To add notes to query expressions:**

1. Next to the query expression, hover over the notebook icon and click **Add Expression Note**.

   ![AddNoteButton](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/queries/AddExpressionNote.png)
2. Enter your note (up to 250 characters) and click **Apply**.

   This option is available in each query expression that you add.
3. The notebook icon now appears with a red dot, and when you hover over it, you can edit the note text, or remove it.

   ![EditNoteButton](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/queries/EditExpressionNote.png)

Notes added to expressions in [Saved Queries](https://docs.axonius.com/axonius-help-docs/docs/saved-queries-devices) appear in the Saved Query drawer under **Query Expression**, and you can add, remove, or edit them from there as well.

## Advanced Querying

### Free Text Search in Table

The search bar lets you search free text and filter on assets with or without a predefined 'search by' option. By typing the required search text and pressing Enter, the results filter all entities in the table that contain the given text in any properties.

The available search options are:

* **Free text search** - Axonius runs the following search logic on the specified search value:
  * 'Case sensitive exact match' search in any of the selected columns.
  * 'Case insensitive exact match/ start with' search in the following columns for Devices and Users:
    * **Devices** page:  Host Name, Network Interfaces: MAC, Device Manufacturer Serial, Last Used Users.
    * **Users** page: User Name, Email.

![FreeTextSearch.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FreeTextSearch\(1\).png)

* **Predefined 'search by' option**
  * Click the search bar dropdown button or press the down arrow key to select one of the predefined 'search by' options:
    * **Host Name** - to run 'contains' search on 'Host Name' only.
    * **Last Used Users** - to run 'contains' search on 'Last Used Users'.
    * **IP Address** - to run 'contains' search on 'Network Interfaces: IPs'.
    * **Installed Software Name** - to run 'contains' search on 'Installed Software: Software Name'.

  * Each 'search by' option consists of a different set of columns, that can be personalized and saved as the user's search default view. For more details, see [Editing Table Columns](/docs/devices-page#editing-table-columns).

![Searchby.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Searchby.png)

![SearchbyHostName.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SearchbyHostName\(2\).png)

All searches are tracked and stored. Click the search bar drop-down button or press the down arrow key to browse the search **History** and the recent **Saved Queries** that were run.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Saved%20Searches.png)