# Source: https://docs.axonius.com/docs/condition-statement-concepts.md

# Dynamic Value Statement Concepts

The following sections describe the basics of Dynamic Value statements (also referred to as 'statements').

### The Asset Pool

Every Enforcement Set is based on a query triggered each time the Enforcement Set is run.

The set of assets that matches the query parameters is the *asset pool* that the Enforcement Set runs on *for that run*.

The asset pool can be different for each run of the same Enforcement Set, as changes in asset status may occur between runs. Statements use the data from those assets.

### Adapter Fields to Enforcement Action Form Fields - Source to Target

Adapter fields are the asset attributes that contain data about the asset. These are the "source" fields named in the statement. A statement takes these values, applies the statement, and performs whatever function is defined.

The result is placed in an Action form field, the "target" field. Action form fields include all fields available in the Enforcement Action configuration dialog, either to be written to a 3rd party product (such as a ticketing system or email) or on the asset itself as tags or [custom data](/docs/working-with-custom-data) fields.

The following describes the process:

Take values from **Adapter Fields**.
-> Apply statements, functions, and operators.
-> Populate **Enforcement Action Fields** with resulting values.

### Dynamic Value Statements

Dynamic value statements are used to add dynamic values to fields in Enforcement Actions.

You can easily write statements using either of the following:

* [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard)
* [Autocomplete feature and Syntax Helper](/docs/using-the-syntax-helper). With autocomplete, as you type a statement, Autocomplete presents a relevant choice of action form fields, functions, or operators. This  makes it easy to find and choose statement components with minimal typing and syntax errors.

<Callout icon="📘" theme="info">
  Note

  When the statement requires you to enter an asset field, Autocomplete directs you to the Syntax Helper to make a choice.
</Callout>

Axonius provides the [Dynamic Value Statement Simulator](/docs/using-the-simulator) tool to effectively debug Dynamic Value statements.

If you have used [Refine Data Display](/docs/setting-page-columns-display#refining-the-data-displayed-in-table-columns-and-rows) to filter out values from assets, Dynamic Value statements run on query results filtered according to the data refinement configuration (for all options with the exception of Refine field values by adapter connection).

### Using the Correct Field Names

Field names as shown in the asset tables, asset details, or Enforcement Action configuration dialog are not the same as the field names in the Axonius database. These are user-friendly names used in the Axonius application. In the statement, you need to use their unique names as they exist in the Axonius database, the database field name. You can use the Wizard to choose the adapter field names and action for field names. When using the Wizard, you choose the adapter, and then choose from the relevant fields in the Field dropdown. When using the Autocomplete feature, for Action form fields only (and not for asset fields), you can choose the database name from the autocomplete suggestions. And for asset fields, you can use the [Syntax Helper](/docs/config-ec-conditions#using-the-syntax-helper) to find the database field name.

### Asset Field Example

In the following asset example, there are four Adapter fields: **Asset Name**, **Host Name**, **Last Seen**, and **Network Interfaces: MAC**.

<Image alt="ECConditionsFieldNames.png" width="900px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECConditionsFieldNames.png" />

In this asset example, the database field names may be similar to:

| Adapter Field Name          | Database Field Name                                        |
| --------------------------- | ---------------------------------------------------------- |
| **Asset Name**              | `device.specific_data.data.name`                           |
| **Host Name**               | `device.specific_data.data.hostname`                       |
| **Last Seen**               | `device.specific_data.data.last_seen`                      |
| **Network Interfaces: MAC** | `device.adapters_data.some_adapter.network_interfaces.mac` |

In statements, you are required to use the Database Field Name. Use the [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) or [Syntax Helper](/docs/config-ec-conditions#using-the-syntax-helper) to find the database field name.

An asset field value can be fetched from a single specific adapter (a single-value field), be aggregated values from several adapters (known as Aggregated field; a list of values), or be the preferred value from the aggregated values (known as Preferred field; a single-value field). The available fields can be found in the asset table as columns and in the asset profile page.

### Action Form Field Example

In the following Action form example, there are three fields: **Incident short description**, **Incident description**, and **Message severity**.

![ActionFieldsExample.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActionFieldsExample.png)

In this Action form example, the database field names may be similar to:

| Action Form Field Name         | Database Field Name         |
| ------------------------------ | --------------------------- |
| **Incident short description** | `form.incident_title`       |
| **Incident description**       | `form.incident_description` |
| **Message severity**           | `form.severity`             |

In statements, use the Database Field Name.
Use the Wizard, choose a relevant autocomplete suggestion, or use the [Syntax Helper](/docs/config-ec-conditions#using-the-syntax-helper) to find the database field name.

### Field Types

All fields (both adapter fields and action fields) are configured with a data type. The most common field value types you’ll encounter are:

* String
* Integer
* Float
* Date (Epoch)
* Boolean (true/false)

Additionally, all types can be configured as either a single value or as a list (array) with multiple values. When you create a custom field, you select both value type and field type, i.e., whether that field contains single or multiple values.

For example, **Hostname** is a list field, meaning it can contain multiple text string values for every asset in that field. **Preferred Hostname** is a single-value field as it is the chosen single hostname value from multiple values for a given asset.

<Callout icon="📘" theme="info">
  Note

  If an Adapter source field contains a list of values (array) and the target Action field is a single value field, the first value from the source field list is used for the comparison. It is recommended to use specific adapter fields or preferred fields, rather than aggregated fields that tend to be multi-value.
</Callout>