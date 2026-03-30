# Source: https://docs.axonius.com/docs/all-statement-syntax.md

# "All" Statement Syntax

For each asset matching the Enforcement Set query, the *All* Dynamic Value statement (also referred to as *statement*) assigns to an Action field (using `set_value`) the value of an adapter field, relationship field, or custom input, or the value returned by a function applied on one or more of these.

<Callout icon="📘" theme="info">
  **IMPORTANT**

  All values, operators, and syntax elements in statements are lower case and case sensitive.
</Callout>

* You can apply *All* statements on asset, Activity Logs, and Adapters Fetch History modules; not on Asset Investigation and Findings modules. View [here](/docs/assets-page#viewing-assets-by-type) a full list of supported asset types.
* You can use **or** to define multiple options per Action field. The defined options are applied in the order that they are written. The first option that uses a field with a non-empty valid value is applied and the remaining options are ignored. If none of the fields have a value, the default value assigned to the action field in the form itself is used.
* You can use **also** to assign a value to an additional action field in the statement.

The basic syntax of *All* statements for four of the supported asset types — Device, User, Vulnerability, and Software — is presented in the following table, followed by a description of the statement elements.

| Asset Type    | Basic Syntax                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| Device        | `device all then form.fieldname set_value [device.adapters_data.adapter_name.field_name]`               |
| User          | `user all then form.fieldname set_value [user.adapters_data.adapter_name.field_name]`                   |
| Vulnerability | `vulnerability all then form.fieldname set_value [vulnerability.adapters_data.adapter_name.field_name]` |
| Software      | `software all then form.fieldname set_value [software.adapters_data.adapter_name.field_name]`           |

* **device**, **user**, **vulnerability**, **software** — Name of the asset type on which to apply the statement. The asset type must match the query used in the Enforcement Set.

<Callout icon="📘" theme="info">
  **Note:**

  There are many [supported asset types](/docs/assets-page#viewing-assets-by-type). These are only the names of the asset types shown in the above table.
</Callout>

* **all** — Applies the statement on **all** assets of the specified asset type (for example: all devices, users, vulnerabilities, or software) that match the query.
* **then** — On all assets that match the query, *then* applies the value from the Adapter field (source) to the Action form field (destination).
* **form.fieldname** — The destination field in the Action form. Use Autocomplete, [Syntax Helper](/docs/using-the-syntax-helper), or the [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) to get the correct field name.
* **set\_value** — Sets the value of *form.fieldname* to match that of the source field of the Adapter. Functions can be used to determine this value.
* **`[<asset-type>.adapters_data.adapter_name.field_name]`** — The source field in the Adapter; must be enclosed in square brackets. The prefix **`<asset-type>`** indicates the type of asset query — for example: *device*, *user*, *vulnerability*, or *software*. Use [Syntax Helper](/docs/using-the-syntax-helper) or the [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) to get the correct field name.

***

### All Statement Examples

These additional functions and operators are used in the following examples:

* **or** — Defines multiple options for the action field.
* **concat** — Concatenates the specified values. *concat* supports an unlimited number of string arguments (values and/or fields). The *concat* operator must be followed by a space and then the parameters within `( )`. Field inputs and static strings can be used in any order.
* **sum** — Adds the values in the indicated field.

You can construct more complex statements using the many functions and operators available. After entering `set_value` in the statement, the Autocomplete feature shows the available functions and operators that you can choose from. See [Enforcement Action Statement Syntax Table](/docs/enforcement-action-condition-syntax-table) for a complete list of available statement elements, and their syntax and usage rules.

<Callout icon="📘" theme="info">
  **Note:**

  * You can use the Wizard to construct a simple `set_value` statement, an alternative of statements using *or*, or to assign values to more than one action field using *also*.
  * When using operators, such as *concat* and *join*, it is important to choose the relevant field types — list or single value; Aggregated fields (hold lists of values) or Preferred fields (hold single values). To learn more, see [Preferred and Aggregated Fields in the Syntax Helper](/docs/using-the-syntax-helper##aggregated-and-preferred-fields-in-the-syntax-helper).
</Callout>

The following examples illustrate some ways that **All** asset statements can be used.

***

**Example:**
For all devices that match the query, configure an Enforcement Action — Add Tag to Device Assets, with a statement that sets **form.tag\_name** to the last seen date from the BigID adapter (`device.adapters_data.bigid_adapter.last_seen`). Otherwise, if the BigID last seen field is empty, sets **form.tag\_name** to the last seen date from the AWS adapter (`device.adapters_data.aws_adapter.last_seen`).

```text
device all then form.tag_name set_value [device.adapters_data.bigid_adapter.last_seen] or [device.adapters_data.aws_adapter.last_seen]
```

A Tag field in the configured color is added to the devices that match the query. This field displays the last seen date and time, if it has been fetched from the BigID or AWS adapters.

<Image alt="ECTagsResults" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECTagsResults.png" />

***

**Example:**
For all devices that match the query, configure an Enforcement Action — Send Email, with a statement that sets **form.emailList** to **device.specific\_data.data.hostname\_preferred** (the Aggregated Adapter preferred hostname) + `"@gmail.com"`.

```text
device all then form.emailList set_value concat([device.specific_data.data.hostname_preferred], "@gmail.com")
```

Once the Enforcement Set completes, you can see the outcome of the run.

<Image alt="ECRun" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECRun.png" />

Clicking *Successful Affected Assets* shows under *EC: Result Details* that an email has been sent for this device.

<Image alt="ECResultDetails" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECResultDetails.png" />

***

**Example:**
For all software that match the query, configure an Enforcement Action — Add Custom Data to Software Assets, with a statement that sets **form.custom\_data\_value** to the value in **software.adapters\_data.azure\_adapter.last\_seen** (the *last\_seen* field from the Azure adapter), if not empty. Otherwise, if empty, sets it to **software.adapters\_data.cisco\_meraki\_adapter.last\_seen** (the *last\_seen* field from the Cisco adapter).

```text
software all then form.custom_data_value set_value [software.adapters_data.azure_adapter.last_seen] or [software.adapters_data.cisco_meraki_adapter.last_seen]
```

***

**Example:**
For all vulnerabilities that match the query, set **form.field\_name** to the sum of the values in **vulnerability.adapters\_data.tenable\_security\_center\_adapter.cvss\_vector** (the Tenable.sc (SecurityCenter) CVSS Vector field *cvss\_vector*).

```text
vulnerability all then form.field_name set_value sum([vulnerability.adapters_data.tenable_security_center_adapter.cvss_vector])
```

***

**Example:**
For all devices that match the query, configure an Enforcement Action — Add Tag to Device Assets, with a statement that sets the value of **form.tag\_name** to a concatenation of `"name"` + **device.specific\_data.data.hostname** (the Aggregated Adapter hostname) + `"os_type"` + **device.specific\_data.data.os.type** (the Aggregated Adapter OS type), using the *concat* operator.

```text
device all then form.tag_name set_value concat("name", [device.specific_data.data.hostname], "os_type", [device.specific_data.data.os.type])
```