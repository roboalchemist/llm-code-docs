# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/working-with-analyzer-fields/fields-in-analyzer/about-field-hierarchies.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/fields-in-analyzer/about-field-hierarchies.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/fields-in-analyzer/about-field-hierarchies.md

# About field hierarchies

Some level fields (time periods, names, types, categories, etc.) belong to field hierarchies. Here are two examples of field hierarchies:

* Product Line >>Product Name
* Year >>Quarter >>Month >> Week >> Day

The field hierarchies help you in two primary ways.

First, it provides a quick and easy way to drill into more details on a report:

* When you click on a level field on the report, such as **Fiscal Quarter**, and then click **Also Show** from the context menu, all these fields will be available for selection if the field is part of a hierarchy.
* When you click on a level field value on the report, such as the year `'2007'`, the context menu displays the option **Keep Only 2007 And Show Quarters**.
* When you click on a level field value, such as 2007, and both the Year and Quarter are in the report, the context menu displays the **Drill up to Year** option. When you click the 2007-Q1 value, the context menu displays the **Drill Down to Month** option.

Second, when creating a filter, field hierarchies narrow down the list of available values. For example, if you have a filter Product Line='Snow Sports', then the list of possible choices when you filter **Product Names** are limited to the products that are part of the Snow Sports product line.

Additionally, field hierarchies sometimes control how fields are placed on the report. For example, fields from the same field hierarchy need to be placed on the same axis (row/column) and the report will automatically enforce this rule as you move and arrange your fields.
