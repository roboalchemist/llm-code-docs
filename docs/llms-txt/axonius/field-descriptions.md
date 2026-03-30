# Source: https://docs.axonius.com/docs/field-descriptions.md

# Field Descriptions

Descriptions for many fields are available in the Query Wizard. Use field descriptions to understand and use asset fields in queries. They explain the purpose of each field and its data type, making it easier to choose the right field for the query you are creating. The description also includes the data type, such as Single Select, Integer, String, Array, and more. In addition, an indicator on the bottom of the description pane shows all of the adapters that are fetching data for the field.

**To view field descriptions:**

1. From the [Query Wizard](/docs/query-wizard-and-query-filter), click in a field selector drop-down list. The field list is displayed.

2. In the left pane, select the category of fields you want to use.
   * When the aggregated adapter is selected, these categories are available:
     * **All Fields** - Includes all fields in Axonius from all adapters.
     * **Preferred** - Includes only the fields designated as Preferred. Preferred fields are determined by Axonius when more than one adapter source includes the same field. One of those fields is designated as being more reliable and is the preferred field.
   * When a specific adapter is selected, these categories are available:
     * **All Fields** - Includes all fields from the selected adapter.
     * **Common** - Includes fields fetched from all connections of the selected adapter.
     * **Specific** - Includes fields specific to that adapter.

3. In the center pane, hover over the field names. Descriptions are displayed in the rightmost pane.

4. On the bottom of the pane, an indicator shows all of the adapters that are fetching data for the field. When there are many adapters for a given field, you can hover over the number to view them all in a scrollable list.
   ![FieldDescription\_Adapters.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldDescription_Adapters.png)

5. You can also enter text into the Search bar.

The field drop-down when the aggregated adapter is selected:
![FieldDescriptionDropdown.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldDescriptionDropdown.png)

The field drop-down when a specific adapter is selected:
![FieldDescriptionDropdownNotAggregated.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FieldDescriptionDropdownNotAggregated.png)