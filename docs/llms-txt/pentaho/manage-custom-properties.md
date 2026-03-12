# Source: https://docs.pentaho.com/pdc-admin/manage-custom-properties.md

# Manage custom properties

In Pentaho Data Catalog, you can create custom properties that collect additional metadata about resources specific to their business environment or engagement. For example, you can define a custom property to include a business username for a data resource. Alternatively, you could define a property that includes values that are used by system-level processes. To know more, see [Resource properties #Custom properties](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-resource-properties-user-guide-cp#custom-properties "mention") in the [Use Pentaho Data Catalog](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/) guide.

With the Data Catalog admin role, you can manage custom properties from the **Custom Properties** card in the **Management** section of Data Catalog. This centralized location provides a single place to view and govern all custom properties defined in the system. From this page, properties are organized into tabs that let you review all properties, only data labels, or only custom properties, along with their field types, applicable hierarchies, and asset types. In this page, you can create custom properties, define where they apply by selecting hierarchies and asset types, update their scope or display settings, and delete properties when they are no longer needed.

{% hint style="info" %}
To know more about managing data labels, see [Manage data labels](https://docs.pentaho.com/pdc-admin/pdc-manage-data-labels).
{% endhint %}

> ▶️ **Watch a walkthrough**
>
> You can watch a guided walkthrough that demonstrates [how to create, edit, and delete custom properties](https://assets.demos.hitachivantara.com/psl/mgh0eqo?g=cmkz4gqm2000004ifa3md3nkc\&s=0) in Pentaho Data Catalog.
>
> {% embed url="<https://assets.demos.hitachivantara.com/psl/mgh0eqo?g=cmkz4gqm2000004ifa3md3nkc&s=0>" %}

## Create a custom property

In Data Catalog, [custom properties](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-resource-properties-user-guide-cp#custom-properties) allow you to capture organization-specific information and control where that information applies across supported hierarchies and asset types. From the **Management** section, Data Catalog admins can create custom properties, define their scope, control whether they appear on the Summary tab, and manage them centrally throughout their lifecycle. After a property is created, stewards assign values to applicable assets from the asset-level **Custom Properties** tab.

Perform the following steps to add a custom property in Data Catalog:

**Procedure**

1. Click **Management** in the left navigation menu.

   The **Manage Your Environment** page opens.
2. In the **Custom Properties** card, click **View Custom Properties**.

   The **Custom Properties** page opens.
3. Click **Create Custom Property**.\
   The **Create Custom Property** dialog box appears.
4. In the **Property Name** field, enter a unique name for the custom property.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If you want to create a standard custom property, do not toggle the <strong>Data Label</strong> switch. Toggle the switch only if you want to create a data label. See <a data-mention href="pdc-manage-data-labels">pdc-manage-data-labels</a> for more information.</p></div>
5. In the **Field Type** list, select how users will enter values for the custom property.

   <table><thead><tr><th width="149.09088134765625">Field type</th><th>Description</th><th>Typical use cases</th></tr></thead><tbody><tr><td><strong>Free Text</strong></td><td>Stores free-form text without format restrictions. It accepts alphanumeric and special characters. No format validation is applied.</td><td>Notes, comments, descriptive qualifiers</td></tr><tr><td><strong>URL</strong></td><td>Stores a web address that links to an external resource. It accepts only valid URL formats and displays as a clickable link.</td><td>Policy documents, external systems, reference links</td></tr><tr><td><strong>Number</strong></td><td>Stores numeric values only. It accepts numeric input only.</td><td>Scores, thresholds, numeric identifiers</td></tr><tr><td><strong>Boolean</strong></td><td>Stores a true or false (binary) value.</td><td>Compliance flags, approval indicators, and status attributes</td></tr><tr><td><strong>Date</strong></td><td>Stores a calendar date. It uses a date picker to prevent invalid date formats.</td><td>Review dates, expiration dates, and certification dates</td></tr><tr><td><strong>Users</strong></td><td>Stores multiple Data Catalog users. It allows selecting multiple valid users.</td><td>Shared ownership, review groups, escalation contacts</td></tr><tr><td><strong>Select String</strong></td><td>Stores a text value selected from a predefined list. It allows selection from predefined string options and doesn’t accept arbitrary values.</td><td>Status values, categories, standardized labels</td></tr><tr><td><strong>Select Number</strong></td><td>Stores a numeric value selected from a predefined list. It allows selection from predefined numeric options and doesn’t accept arbitrary values.</td><td>Priority levels, rating scales, and standardized numeric classifications</td></tr></tbody></table>

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Once a custom property is created, its field type cannot be changed. If you need a different type, you must delete the property and create a new one.</p></div>
6. In **Assign to a hierarchy**, select one or more hierarchies where the property should be available.\
   Supported hierarchies include Data Canvas, Data Collections, Glossary, Applications, Business Intelligence, Policies, Physical Assets, and ML Models.
7. In **Assign to an item**, select the asset types within the selected hierarchy where the property should apply. For example, tables, columns, terms, files, models, or resources.
8. (Optional) In **Assign to a root**, restrict the property to specific roots within the selected hierarchy.

   Root-level restriction is available only when a single hierarchy is selected.
9. (Optional) Select **Show it in the summary** if you want the property to appear on the asset’s Summary tab.
10. Click **Create Property**.

**Result**

You have successfully created a custom property, which is now available for value assignment on all applicable assets based on the selected hierarchy and scope. Stewards can now assign values to this property from the **Custom Properties** tab of supported assets.

## Edit a custom property

In Data Catalog, as an admin, you can modify existing custom properties to update their scope or display settings. You can modify the hierarchies, asset types, root restrictions, and Summary visibility.

{% hint style="warning" %}
The field type cannot be changed after the property is created.
{% endhint %}

Perform the following steps to edit a custom property.

**Procedure**

1. Click **Management** in the left navigation pane.\
   The **Manage Your Environment** page opens.
2. In the **Custom Properties** card, click **View Custom Properties**.\
   The **Custom Properties** page opens.
3. On the **Custom Property** tab, locate the custom property that you want to edit, and click the **Edit** (pencil) icon.\
   The **Edit Custom Property** dialog box opens.
4. Update the fields as needed:
   * Update the **Property Name**, if necessary.
   * Update the **Assign to a hierarchy** selection.
   * Update the **Assign to an item** selection.
   * (Optional) Update the **Assign to a root** selection. Root-level restriction is available only when one hierarchy is selected.
   * (Optional) Select or clear **Show it in the summary**.
5. Click **Save Changes**.

**Result**

You have successfully updated the custom property. Changes to hierarchy or asset type scope affect where the property is available for value assignment. If the property is removed from a hierarchy or asset type, it is no longer available in those locations.

{% hint style="info" %}
When you edit or delete a custom property, Data Catalog applies the change via a background **worker job** across all objects that use the custom property. The more linked objects, the longer it can take. The Custom Properties view doesn’t auto-refresh. After the job finishes, switch tabs or reload the page to see the update.
{% endhint %}

## Delete a custom property <a href="#delete-a-custom-property" id="delete-a-custom-property"></a>

In Data Catalog, as an admin, you can permanently remove or delete a custom property. Deleting a custom property removes it from all applicable hierarchies and asset types, including any values previously assigned to assets.

{% hint style="warning" %}
Use caution when deleting custom properties, because you cannot recover the data.&#x20;
{% endhint %}

Perform the following steps to remove or delete a custom property.

**Procedure**

1. Click **Management** in the left navigation pane.\
   The **Manage Your Environment** page opens.
2. In the **Custom Properties** card, click **View Custom Properties**.\
   The **Custom Properties** page opens with the list of existing custom properties.
3. Find the property you want to remove and click the **Delete** (trash) icon.\
   A confirmation dialog opens to confirm the deletion.
4. Click **Confirm** to delete the selected custom property.\
   If the property is used by other objects, Data Catalog first disassociates it from all linked entities and then deletes it. If the property isn’t used elsewhere, it is deleted immediately.

**Result**

You have successfully removed the custom property from the system. The property no longer appears in any assets, and all previously assigned values have been deleted.

{% hint style="info" %}
When you edit or delete a custom property, Data Catalog applies the change via a background **worker job** across all objects that use the custom property. The more linked objects, the longer it can take. The Custom Properties view doesn’t auto-refresh. After the job finishes, switch tabs or reload the page to see the update.
{% endhint %}
