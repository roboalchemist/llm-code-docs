# Source: https://docs.axonius.com/docs/creating-the-custom-enrichment-rule.md

# Creating the Custom Enrichment Rule

Four types of rules exist, each one based on a different field type:

* [Field from a Specific Adapter](#creating-a-rule-based-on-a-field-from-a-specific-adapter)
* [Aggregated field](#creating-a-rule-based-on-an-aggregated-field)
* [Enforcement Action field](#creating-a-rule-based-on-an-enforcement-action-field)
* [Preferred field](#creating-a-rule-based-on-a-preferred-field)

<Callout icon="📘" theme="info">
  Note

  * Complex fields are NOT supported in any rule types.

  * The **Adapter Connection Label** field is not supported. Instead, you can use the **Last Fetched From Connection Label** field, which is set with the value of the existing connection label of the connection.
    ![SyntaxHelperLastFetched](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxHelperLastFetched.png)
</Callout>

## Common Syntax to All Rule Types

For the rules based on Adapter, Aggregated, and EC fields, the syntax begins with:
source.test\_field operator asset\_type.

The syntax of the Preferred field rule begins with:
source.preferred\_host\_name\_field operator asset\_type.

<Callout icon="📘" theme="info">
  Note

  Exception to the rule: The source follows the **contains** operator.
</Callout>

These syntax elements are described in the following table:

| Element                                           | Description                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **source.**                                       | Indicates that the field is in a CSV source file.                                                                                                                                                                                                                                                                                                   |
| **test\_field**, **preferred\_host\_name\_field** | A variable. The column name in the CSV file that is used to identify which assets are enriched.  Note: There can be no white spaces in the source's field name. For example: 'source.Application Name' is invalid. The field name must be changed to Application\_Name so that the source field is without white spaces: 'source.Application\_Name' |
| **operator**                                      | One of the following available operators: **==** (case-sensitive equals)`=` (case-insensitive equals)**contains** (case-insensitive)**in** (case-sensitive contains)**in\_net** (network range). The source’s network field must list a specific network range. For example: 10.0.0.0/24                                                            |
| **asset\_type.**                                  | A variable. Type of asset on which to apply the rule.                                                                                                                                                                                                                                                                                               |

<Callout icon="📘" theme="info">
  Note

  Make sure to use spaces between the sections of the rule, as shown in this example:

  ```Text
  source.mail == user.[Google Workspace].[Email Address]
  ```
</Callout>

The following example shows the difference between the **contains** and **in** operators.

```Text
enrich 'devices' with (subnet_description) on (device.csv_adapter.hostname contains source.subnet_owner)
enrich 'devices' with (subnet_description) on (source.subnet_owner in device.csv_adapter.hostname)
```

**The first enrichment means:** If the value of the **hostname** field in the CSV adapter contains the string value in the **subnet\_owner** field of the CSV file (regardless of case), enrich the device with the value contained in the **subnet\_description** field in the CSV file.
**The second enrichment means:** If the string value in the **subnet\_owner** field of the CSV file is in the value of the **hostname** field in the CSV adapter and the letters are of the same case, enrich the device with the value contained in the **subnet\_description** field in the CSV file.

Note that the source follows the case-insensitive **contains** operator, while the source precedes the case-sensitive **in** operator.

## Using Square Brackets in Rules

In Custom enrichment rules, you can use either the human-readable field names and adapter names (i.e., the format of the names in the Query Wizard Adapter and Field dropdowns) or the internal Axonius adapter and field names.
When you enclose a human-readable field name or adapter name in square brackets \[ ], it automatically resolves it into its internal Axonius name.
For example, when creating a custom enrichment rule on a field in the Google Workspace adapter (see figure below), you are required to enter \[Google Workspace] so that the square brackets resolve it into its internal Axonius name.

![QueryWizardAdapterDropdown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryWizardAdapterDropdown.png)

In the following examples, \[Google Workspace] is translated to 'google\_mdm\_adapter' and \[AWS] to 'aws\_adapter'.

Therefore, the following are equivalent statements:

```Text
enrich 'users' with (*) on (source.mail == user.google_mdm_adapter.mail)
enrich 'users' with (*) on (source.mail == user.[Google Workspace].mail)
```

and

```Text
enrich 'devices' with (*) on (source.policy == device.[AWS].[Policies: Policy ARN])
enrich 'devices' with (*) on (source.policy == device.aws_adapter.user_attached_policies.policy_arn)
```

## Creating a Rule Based on a Field from a Specific Adapter

This rule tries to match the value of a specific field of a specific adapter with one of the values in the first column of the CSV. If there is a match, the asset is enriched.

The syntax of the rule is:

source.test\_field operator asset\_type.\[Adapter Name].\[adapter\_field]

See [a description of the **source**, **test\_field**, **operator**, and **asset\_type**](#common-syntax-to-all-rule-types).

The following syntax elements describe the Adapter name and field:

* \[**Adapter Name**] - A variable. The human-readable name of the adapter on which to apply the rule or \* to apply the rule on all adapters. Must be enclosed in \[  ].
* \[**adapter\_field**] - A variable. The human-readable name of the field on which you apply the rule. Aggregated fields and Custom Fields can be used in Custom Enrichments. Must be enclosed in \[  ].

<Callout icon="📘" theme="info">
  Note

  If you know the internal Axonius adapter or field name, you can write it without enclosing it in \[].
</Callout>

For example, a full statement with this type of Rule:

```Text
enrich 'devices' with (Name,Email,Physical_Address) on (source.id == device.[AWS].[Account ID])
```

**This means:** If the value in the **id** column in the CSV file that was uploaded is the same as the value in the AWS adapter **Account ID** field, enrich the device with the values contained in the **Name**, **Email**, and **Physical\_Address** fields in the CSV file.

## Creating a Rule Based on an Aggregated Field

This rule tries to match the value of an aggregated field with one of the values in the first column of the CSV. If there is a match, the asset is enriched.

The syntax of the Rule is:

source.test\_field operator asset\_type.specific\_data.data.\[Aggregated Field]

See [a description of the **source**, **test\_field**, **operator**, and **asset\_type**](#common-syntax-to-all-rule-types).

The following syntax elements describe the Aggregated field:

* **specific\_data.data** - Indicates an aggregated field.
* \[**Aggregated Field**] - A variable. The human-readable name of the aggregated field on which you apply the rule.This field can be a Custom Field. Must be enclosed in \[  ].

For example, a full statement with this type of rule:

```Text
enrich 'devices' with (Name,Email,Physical_Address) on (source.id == device.specific_data.data.[Account ID])
```

**This means:** If the value in the **id** column in the CSV file is the same as the value in the aggregated field **Account ID**, enrich the device with the values contained in the **Name**, **Email**, and **Physical\_Address** fields in the CSV file.

<Callout icon="📘" theme="info">
  Note

  All fields in a Custom Enrichment rule must be from the same adapter, as they are written alongside the matching field. Using fields from two different adapters in a single statement causes the Manage Custom Enrichment enforcement action to fail. You can see the error (under the **Additional Info** column) when you drill down into the red 'Failed' assets and open the **Enforcement Runs** tab of a specific failed asset:
  *Custom Enrichment failed: Failed to run EC Manage Enrichment action: Wrong query syntax, can't use multiple adapters in one query.*
  It is recommended to use the aggregated field, which writes that data into a new field under the aggregated adapter as *Common Enrichment: field name* (or if the option is enabled in the Enforcement Action, into a new field under the EC Artifacts adapter as *Enrichment: field name*).
</Callout>

## Creating a Rule Based on an Enforcement Action Field

This rule tries to match the value of a field populated by an Enforcement Action with one of the values in the first column of the CSV. If there is a match, the asset is enriched.

The syntax of the rule is:

source.test\_field operator asset\_type.\[EC: ec\_field\_name]

See [a description of the **source**, **test\_field**, **operator**, and **asset\_type**](#common-syntax-to-all-rule-types).

The following syntax elements describe the Enforcement Action field:

* **\[EC: ec\_field\_name]** - This whole part must be enclosed in \[  ]. There must be a space between these two elements:
  * **EC:** - Indicates that the field is from an Enforcement Action.
  * **ec\_field\_name** - A variable. The human-readable name of the field in the Enforcement Action form. This field can be a Custom Field.

For example, a full statement with this type of rule:

```Text
enrich 'devices' with (Name,Email,Physical_Address) on (source.id == device.[EC: Issue_ID])
```

**This means:** If the value in the **id** column in the CSV file is the same as the value in the Enforcement Action field **Issue\_ID**, enrich the device with the values contained in the **Name**, **Email**, and **Physical\_Address** fields in the CSV file.

## Creating a Rule Based on a Preferred Field

This rule tries to match the value of a preferred field with one of the values in the first column of the CSV. If there is a match, the asset is enriched.

The syntax of the rule is:

source.preferred\_host\_name\_field operator asset\_type.specific\_data.data.\[Preferred Host Name]

See [a description of the **source**, **test\_field**, **operator**, and **asset\_type**](#common-syntax-to-all-rule-types).

The following syntax elements describe the Preferred field:

* **specific\_data.data** - Indicates an aggregated field.
* \[**Preferred Host Name**] - A variable. The human-readable name of the preferred field on which you apply the rule. This field can be a Custom Field. Must be enclosed in \[  ].

For example, a full statement with this type of Rule:

```Text
enrich 'devices' with (Name,Email,Physical_Address) on (source.preferred_host_name_field == specific_data.data.[Preferred Host Name])
```

**This means:** If the value in the **preferred\_host\_name\_field** column in the CSV file is the same as the value in the preferred aggregated field **Preferred\_Host\_Name**, enrich the device with the values contained in the **Name**, **Email**, and **Physical\_Address** fields in the CSV file.

## Using and/or Operators and ( )

The **and** and **or** operators can be used to combine enrichment rules. This allows you to create more flexible rules.

The **and** operator requires all rules to return valid values.
The **or** operator requires only one of the rules to return a valid value.

* The **and**/**or** operators are NOT case-sensitive. Therefore, you can also use AND, And, OR, Or, and more.

* You can use parentheses ( ) to create nested rules that give you more control over the enrichment results. Expressions in the innermost parentheses are evaluated first, working out to the outermost parentheses.
  For example, you can create enrichment rules, such as:

```Text
enrich 'users' with (*) on ((A or B or C) and (D or E))
```

```Text
enrich 'users' with (*) on (A or (B and C) or (D and E))
```

```Text
enrich 'users' with (*) on ((A) or (B and C) or ((D) and E))
```

* Parentheses are NOT mandatory, but advisable, as they make the query more readable.

* AND has precedence over OR. For example: *A or B and C or D* is the same as *A or (B and C) or D*

**Examples**
The following are examples of how **and**, **or**,  and parentheses can be used.

```Text
enrich 'devices' with (*) on (source.host_name = device.json_file_adapter.host_name or (source.mac == device.json_file_adapter.network_interfaces.mac and (device.json_file_adapter.network_interfaces.ips in_net source.subnet))
```

```Text
enrich 'devices' with (field1,field2) on (source.host_name == device.json_file_adapter.host_name AND source.mac == device.json_file_adapter.network_interfaces.mac AND device.json_file_adapter.network_interfaces.ips in_net source.subnet)
```

```Text
enrich 'devices' with (field1,field2) on (source.host_name in device.json_file_adapter.host_name or source.mac == device.json_file_adapter.network_interfaces.mac and device.json_file_adapter.network_interfaces.ips in_net source.subnet)
```