# Source: https://docs.pentaho.com/pdc-use/ldc-resource-properties-user-guide-cp.md

# Resource properties

Pentaho Data Catalog modifies discovered resource properties to add user-defined metadata to the resource. This metadata holds business value or communicates the data quality of the resource.

## Properties

Pentaho Data Catalog discovers metadata properties of resources during the **Data Profiling** (for structured data) and **Data Discovery** (for unstructured data) processes. Data Catalog provides a set of built-in properties that are system-defined metadata attributes available for selected asset types. Built-in properties are predefined metadata fields that appear in the **Properties** section of supported assets, such as glossaries and policies. Unlike custom properties, built-in properties are created and managed by the system and follow a standardized structure. These properties are available by default and are intended to capture commonly required governance and descriptive information.

To access built-in properties in Data Catalog, log in as an administrator and click **Management** in the left navigation menu. On the Management page, click **View Built-in Properties** to view the list of system-defined properties and their descriptions.

<figure><img src="https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2FMJiZIjvl3LzCZ6jsv9v2%2Fimage.png?alt=media&#x26;token=665afcff-06bb-44fd-a02b-600658a283ff" alt=""><figcaption></figcaption></figure>

Built-in properties are grouped into two categories based on their purpose and level of control.

### **Mandatory properties**

Mandatory properties are core metadata attributes that are always visible in the **Properties** panel and cannot be hidden, as they are meant for the governance processes or actions. Mandatory properties are applied consistently across supported asset hierarchies to ensure that essential metadata is always available to users.

### **Non-mandatory properties**

Non-mandatory properties are optional built-in metadata attributes whose visibility in the **Properties** panel can be controlled by administrators by enabling or disabling them from the **Management** section. Non-mandatory properties allow organizations to simplify the user interface and remove properties that are not relevant to their business needs.

{% hint style="info" %}
Built-in property visibility management is currently supported for the Glossary and Policies asset types. When a non-mandatory property is disabled, it is hidden from the user interface, but any existing metadata values are retained. Re-enabling the property restores its visibility and retains its existing values. For more information, see [Manage properties #Enable or disable built-in properties](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-properties#enable-or-disable-built-in-properties "mention").
{% endhint %}

> ▶️ **Watch a walkthrough**
>
> You can watch a guided walkthrough that demonstrates how to [customize the visibility of built-in properties](https://assets.demos.hitachivantara.com/psl/54h0b23) in Data Catalog.
>
> {% embed url="<https://assets.demos.hitachivantara.com/psl/54h0b23>" %}

## Custom properties

Custom properties let organizations extend the metadata model in Data Catalog by defining additional attributes that are specific to their business, governance, or operational needs. You can use custom properties to:

* Capture organization-specific metadata that is not provided out of the box.
* Standardize how additional information is recorded across assets.
* Improve data understanding and governance by adding structured, validated attributes.
* Reduce reliance on free-text descriptions for structured information.

Custom properties complement other metadata features such as descriptions, business terms, tags, and data labels, and are designed to work consistently across supported hierarchies. The following hierarchies support custom properties:

* **Data resources** (datasets, files, tables, and data collections)
* **Business glossaries** (glossaries, categories, and terms)
* **Applications**
* **Policies and standards**
* **Business Intelligence assets**
* **Physical Assets**
* **Machine Learning (ML) Models**

Custom properties are user-defined metadata that let organizations extend the metadata model in Data Catalog by defining additional attributes that are specific to their business, governance, or operational needs. You can use custom properties to:

* Capture organization-specific metadata that is not provided out of the box.
* Standardize how additional information is recorded across assets.
* Improve data understanding and governance by adding structured, validated attributes.
* Reduce reliance on free-text descriptions for structured information.

Custom properties complement other metadata features such as descriptions, business terms, tags, and data labels, and are designed to work consistently across supported hierarchies. The following hierarchies support custom properties:

* **Data resources** (datasets, files, tables, and data collections)
* **Business glossaries** (glossaries, categories, and terms)
* **Applications**
* **Policies and standards**
* **Business Intelligence assets**
* **Physical Assets**
* **Machine Learning (ML) Models**

Custom properties appear in the **Custom Properties** pane on the **Summary** or **Custom** **Properties** tab when you select a resource. The description below each field typically explains how the property is used or what values it can take. For example:

<table><thead><tr><th width="228.55548095703125">Category</th><th width="232.77777099609375">Example custom property</th><th>Example values</th></tr></thead><tbody><tr><td><strong>Business context</strong></td><td>Business Unit</td><td>Retail, Finance, HR</td></tr><tr><td><strong>Data management</strong></td><td>Data Owner</td><td>John Smith, Jane Doe</td></tr><tr><td><strong>Compliance</strong></td><td>Regulatory Zone</td><td>GDPR, HIPAA, CCPA</td></tr><tr><td><strong>Operations</strong></td><td>Criticality Level</td><td>High, Medium, Low</td></tr><tr><td><strong>Technical</strong></td><td>Source System</td><td>SAP, Salesforce, Snowflake</td></tr></tbody></table>

### Role-based responsibilities <a href="#role-based-responsibilities" id="role-based-responsibilities"></a>

In Data Catalog, custom properties follow a clear separation of responsibilities based on user roles, ensuring that metadata definitions remain controlled while allowing domain experts to populate accurate values.:

* **Administrators** manage the lifecycle of custom properties. They create, edit, and delete properties and define where those properties apply.
* **Stewards** (such as Data Stewards and Business Stewards) assign values to custom properties on individual assets within their area of responsibility.
* **Other users** can view custom properties and their assigned values, but cannot modify them.

To know more about user roles, see [User roles and permissions in Data Catalog](https://docs.pentaho.com/pdc-use/pdc-user-roles-and-permissions).

#### Centralized management model <a href="#centralized-management-model" id="centralized-management-model"></a>

Custom properties are managed from a centralized **Custom Properties** area in the **Management** section in Data Catalog. From the management area, administrators can create new custom properties, define where each property applies, and edit or delete existing custom properties. For more information, see [Manage custom properties](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/manage-custom-properties "mention").

#### Supported field types <a href="#supported-field-types" id="supported-field-types"></a>

Custom properties support multiple field types to ensure accurate data capture and validation. The field type determines how values are entered, validated, and displayed when stewards assign values to assets. The following table describes the field types available when creating a custom property, including their purpose, expected values, and behavior during value assignment.

<table><thead><tr><th width="157">Field type</th><th>Description</th><th>Typical use cases</th></tr></thead><tbody><tr><td><strong>Free Text</strong></td><td>Stores free-form text without format restrictions. It accepts alphanumeric and special characters. No format validation is applied.</td><td>Notes, comments, descriptive qualifiers</td></tr><tr><td><strong>URL</strong></td><td>Stores a web address that links to an external resource. It accepts only valid URL formats and displays as a clickable link.</td><td>Policy documents, external systems, reference links</td></tr><tr><td><strong>Number</strong></td><td>Stores numeric values only. It accepts numeric input only.</td><td>Scores, thresholds, numeric identifiers</td></tr><tr><td><strong>Boolean</strong></td><td>Stores a true or false (binary) value.</td><td>Compliance flags, approval indicators, and status attributes</td></tr><tr><td><strong>Date</strong></td><td>Stores a calendar date. It uses a date picker to prevent invalid date formats.</td><td>Review dates, expiration dates, and certification dates</td></tr><tr><td><strong>Users</strong></td><td>Stores multiple Data Catalog users. It allows selecting multiple valid users.</td><td>Shared ownership, review groups, escalation contacts</td></tr><tr><td><strong>Select String</strong></td><td>Stores a text value selected from a predefined list. It allows selection from predefined string options and doesn’t accept arbitrary values.</td><td>Status values, categories, standardized labels</td></tr><tr><td><strong>Select Number</strong></td><td>Stores a numeric value selected from a predefined list. It allows selection from predefined numeric options and doesn’t accept arbitrary values.</td><td>Priority levels, rating scales, and standardized numeric classifications</td></tr></tbody></table>

{% hint style="warning" %}
Once a custom property is created, its field type cannot be changed. If you need a different type, you must delete the property and create a new one.
{% endhint %}

### Applicability and scope control <a href="#applicability-and-scope-control" id="applicability-and-scope-control"></a>

When creating a custom property, an administrator defines its scope to prevent unnecessary properties from appearing on unrelated assets, reducing visual and semantic clutter. Scope determines where the property is available for use. Scope definition includes:

* **Hierarchy selection**: Specifies which catalog hierarchies the property applies to, such as Data Canvas, Business Glossary, Applications, Policies and Standards, BI assets, Physical Assets, or ML Models. Additionally, custom properties can be restricted to specific roots within a selected hierarchy. For example, a property can apply only to terms under a particular glossary domain and not to the entire glossary.
* **Asset type selection**: Limits the property to specific asset types within a hierarchy, such as tables, columns, schemas, or glossary terms.
* **Root-level restriction** (optional): Further narrows applicability to specific roots within a hierarchy, allowing fine-grained control. However, fine-grained root selection is available when a single hierarchy is selected.

When creating a custom property, administrators can specify whether the property appears on the **Summary** tab by default. This option helps to highlight important properties for quick visibility and hide less frequently used properties.

{% hint style="info" %}
These display settings affect only visibility, not assignment availability.
{% endhint %}

### Assign values to custom properties <a href="#assign-values-to-custom-properties" id="assign-values-to-custom-properties"></a>

You can assign values to custom properties on assets to enrich assets with structured, business-specific metadata. These values provide additional context that supports governance, ownership, compliance, and data discovery. Custom property values are assigned at the asset level and are governed by role-based permissions and field-type validation rules.

Perform the following procedure to assign a value to a custom property of an asset in Data Catalog:

Only users with appropriate steward roles can assign values to custom properties.

**Before you begin**

Ensure that the following conditions are met:

* A custom property is already created and assigned to the relevant hierarchy and asset type.
* You are signed in as a **Data Steward** or **Business Steward**, and have access to the asset on which you want to assign the custom property value.

**Procedure**

1. In the left navigation menu, select a hierarchy depending on the asset type.
2. Browse the hierarchy and select the asset to which you want to assign a custom property value.\
   For example, select a folder, schema, table, or column.
3. In the asset content pane, click the **Custom Properties** tab.
4. In the **Custom Properties** table, locate the custom property for which you want to assign a value.
5. In the **Value** column, enter or select a value based on the field type of the custom property:
   * **Free Text**: Type the required text.
   * **URL**: Enter a valid URL.
   * **Number**: Enter a numeric value.
   * **Boolean**: Select true or false.
   * **Date**: Select a date from the date picker.
   * **Users**: Select one or more users from the list.
   * **Select String / Select Number**: Select a value from the predefined list.
6. Press **Enter** or click outside the field to save the value.\
   The value is saved automatically.

**Result**

The custom property value is assigned to the selected asset and is displayed in the **Custom Properties** tab. If the property is configured to appear in the **Summary** view, the value is also visible in the **Custom Properties** panel on the **Summary** tab.

#### Role-based responsibilities

In Data Catalog, custom properties follow a clear separation of responsibilities based on user roles, ensuring that metadata definitions remain controlled while allowing domain experts to populate accurate values.:

* **Administrators** manage the lifecycle of custom properties. They create, edit, and delete properties and define where those properties apply.
* **Stewards** (such as Data Stewards and Business Stewards) assign values to custom properties on individual assets within their area of responsibility.
* **Other users** can view custom properties and their assigned values, but cannot modify them.

To know more about user roles, see [User roles and permissions in Data Catalog](https://docs.pentaho.com/pdc-use/pdc-user-roles-and-permissions).

#### Centralized management model

Custom properties are managed from a centralized **Custom Properties** area in the **Management** section in Data Catalog. From the management area, administrators can create new custom properties, define where each property applies, and edit or delete existing custom properties. For more information, see [Manage custom properties](https://docs.pentaho.com/pdc-admin/manage-custom-properties).

#### Supported field types

Custom properties support multiple field types to ensure accurate data capture and validation. The field type determines how values are entered, validated, and displayed when stewards assign values to assets. The following table describes the field types available when creating a custom property, including their purpose, expected values, and behavior during value assignment.

<table data-header-hidden><thead><tr><th width="135.22222900390625"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Field type</strong></td><td><strong>Description</strong></td><td><strong>Typical use cases</strong></td></tr><tr><td><strong>Free Text</strong></td><td>Stores free-form text without format restrictions. It accepts alphanumeric and special characters. No format validation is applied.</td><td>Notes, comments, descriptive qualifiers</td></tr><tr><td><strong>URL</strong></td><td>Stores a web address that links to an external resource. It accepts only valid URL formats and displays as a clickable link.</td><td>Policy documents, external systems, reference links</td></tr><tr><td><strong>Number</strong></td><td>Stores numeric values only. It accepts numeric input only.</td><td>Scores, thresholds, numeric identifiers</td></tr><tr><td><strong>Boolean</strong></td><td>Stores a true or false (binary) value.</td><td>Compliance flags, approval indicators, and status attributes</td></tr><tr><td><strong>Date</strong></td><td>Stores a calendar date. It uses a date picker to prevent invalid date formats.</td><td>Review dates, expiration dates, and certification dates</td></tr><tr><td><strong>Users</strong></td><td>Stores multiple Data Catalog users. It allows selecting multiple valid users.</td><td>Shared ownership, review groups, escalation contacts</td></tr><tr><td><strong>Select String</strong></td><td>Stores a text value selected from a predefined list. It allows selection from predefined string options and doesn’t accept arbitrary values.</td><td>Status values, categories, standardized labels</td></tr><tr><td><strong>Select Number</strong></td><td>Stores a numeric value selected from a predefined list. It allows selection from predefined numeric options and doesn’t accept arbitrary values.</td><td>Priority levels, rating scales, and standardized numeric classifications</td></tr></tbody></table>

Once a custom property is created, its field type cannot be changed. If you need a different type, you must delete the property and create a new one.

#### Applicability and scope control

When creating a custom property, an administrator defines its scope to prevent unnecessary properties from appearing on unrelated assets, reducing visual and semantic clutter. Scope determines where the property is available for use. Scope definition includes:

* **Hierarchy selection**: Specifies which catalog hierarchies the property applies to, such as Data Canvas, Business Glossary, Applications, Policies and Standards, BI assets, Physical Assets, or ML Models. Additionally, custom properties can be restricted to specific roots within a selected hierarchy. For example, a property can apply only to terms under a particular glossary domain and not to the entire glossary.
* **Asset type selection**: Limits the property to specific asset types within a hierarchy, such as tables, columns, schemas, or glossary terms.
* **Root-level restriction** (optional): Further narrows applicability to specific roots within a hierarchy, allowing fine-grained control. However, fine-grained root selection is available when a single hierarchy is selected.

When creating a custom property, administrators can specify whether the property appears on the **Summary** tab by default. This option helps to highlight important properties for quick visibility and hide less frequently used properties.

These display settings affect only visibility, not assignment availability.

### Assign values to custom properties

You can assign values to custom properties on assets to enrich assets with structured, business-specific metadata. These values provide additional context that supports governance, ownership, compliance, and data discovery. Custom property values are assigned at the asset level and are governed by role-based permissions and field-type validation rules.

Perform the following procedure to assign a value to a custom property of an asset in Data Catalog:

Only users with appropriate steward roles can assign values to custom properties.

**Before you begin**

Ensure that the following conditions are met:

* A custom property is already created and assigned to the relevant hierarchy and asset type.
* You are signed in as a **Data Steward** or **Business Steward**, and have access to the asset on which you want to assign the custom property value.

**Procedure**

1. In the left navigation menu, select a hierarchy depending on the asset type.
2. Browse the hierarchy and select the asset to which you want to assign a custom property value.\
   For example, select a folder, schema, table, or column.
3. In the asset content pane, click the **Custom Properties** tab.
4. In the **Custom Properties** table, locate the custom property for which you want to assign a value.
5. In the **Value** column, enter or select a value based on the field type of the custom property:
   * **Free Text**: Type the required text.
   * **URL**: Enter a valid URL.
   * **Number**: Enter a numeric value.
   * **Boolean**: Select true or false.
   * **Date**: Select a date from the date picker.
   * **Users**: Select one or more users from the list.
   * **Select String / Select Number**: Select a value from the predefined list.
6. Press **Enter** or click outside the field to save the value.\
   The value is saved automatically.

**Result**

The custom property value is assigned to the selected asset and is displayed in the **Custom Properties** tab. If the property is configured to appear in the **Summary** view, the value is also visible in the **Custom Properties** panel on the **Summary** tab.

## Data labels

Data labels in Data Catalog are structured metadata elements defined as key-value pairs, designed to provide standardized, informative machine-readable labels derived from data content to data assets such as tables, columns, datasets, and files. Data Labels are intended for use by consumers of data, such as ML Models. While similar in format to [#custom-properties](#custom-properties "mention"), which also use key-value pairs, Data labels are meant for a specific purpose of data labeling, a concept required for supervised machine learning.&#x20;

This structured approach helps you to manage metadata more effectively, particularly for use cases involving AI, machine learning, and data governance. With data labels, you can classify data using consistent terminology, such as '*Sensitivity*: *Confidential*' or '*Data Quality*: *High*', which improves model training, search accuracy, and compliance.
