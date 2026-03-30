# Source: https://docs.pentaho.com/pdc-admin/manage-properties.md

# Manage properties

[Built-in properties](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-resource-properties-user-guide-cp#properties) are automatically provided by the product to describe common asset characteristics, such as technical metadata, usage information, and governance attributes. Admin can manage built-in properties and their visibility in Data Catalog.

### Enable or disable built-in properties

In Data Catalog, Admin can control the visibility of non-mandatory built-in properties in the **Properties** panel of the **Summary** tab. Enabling or disabling built-in properties helps tailor the Properties panel to your organization’s governance and metadata needs by showing only the most relevant fields. This reduces visual clutter, improves usability, and ensures users focus on meaningful metadata while preserving all existing values for audit and compliance purposes.

Perform the following steps to enable or disable built-in properties visibility in the Properties panel:

> ▶️ **Watch a walkthrough**
>
> You can watch a guided walkthrough that demonstrates how to [customize the visibility of built-in properties](https://assets.demos.hitachivantara.com/psl/54h0b23) in Data Catalog.
>
> {% embed url="<https://assets.demos.hitachivantara.com/psl/54h0b23>" %}

**Procedure**

1. In the left navigation menu, click **Management**.\
   The **Manage Your Environment** page opens.
2. In the **Built-in Properties** card, click **View Built-in Properties**.\
   The **Built-in Properties** page opens.
3. Click the **Non-mandatory** tab.\
   The **Non-Mandatory Properties Customization** table is displayed, listing all configurable built-in properties.\
   **Note**: You cannot control the visibility of mandatory properties.
4. In the list, locate the property you want to configure, then click the **Edit** icon in the **Scope Visibility** column.\
   The scope selection panel opens.
5. Select one or more scopes where you want the property to be visible or clear a checkbox to hide the property from that scope.
6. Click **Apply** to save your changes.\
   The updated visibility settings are applied immediately.

**Result**

After you apply the changes, the configured built-in property is shown or hidden in the Properties panel based on the selected scope. The visibility change takes effect immediately and applies consistently to all users across Data Catalog.

{% hint style="info" %}
Hidden properties no longer appear for the applicable assets, while any existing metadata values remain stored and are restored if the property is re-enabled.
{% endhint %}
