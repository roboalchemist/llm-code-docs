# Source: https://docs.axonius.com/docs/manually-creating-an-asset.md

# Manually Creating an Asset

You can manually create assets based on custom data. This allows you to create your own assets with your own data. This is useful for assets with “one-off” characteristics. Once created, these assets are exactly the same as any other asset in the system.
When creating a new asset, the required field names for that asset are automatically presented in the dialog. You can save the new asset only after assigning values for all required fields, and in the case of a required complex field, first choosing an object (i.e., child field) and then assigning it a value.

**To create an asset manually:**

1. On the relevant [Assets page](/docs/assets-page), in the "More Actions" 3-dot menu above the top-right corner of the Assets page, click **Create new asset**.

<Image alt="CreateNewAsset" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewAsset.png" />

The **Create new asset** dialog opens with entries for the required fields of the asset type being added.

For example, the following is the dialog for creating a new **Application Extensions** asset. You need to fill in **Name** and **Extension Type** fields with values in order to create the new asset.

<Image alt="CreateNewAssetRequiredFields" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewAssetRequiredFields.png" />

2. For all required fields, fill in values or select a value from the dropdown options. For complex fields, select an object (i.e., child field) to enable the **Value** field. The **Value** must match the **Field type** and **Value type**.

<Callout icon="📘" theme="info">
  Note

  It is currently not possible to add a valid IP/IPv4 address to the *Network Interfaces: IPs* / *Network Interfaces: IPv4s* field on an asset.
</Callout>

3. For each existing or new field that you want to add to the asset, click **+ Add Custom Field**, and in the field row that opens, select an existing field or start typing the name of a new field and then click **+ New Field Name** (learn [how to create new custom fields](/docs/working-with-custom-data#creating-new-custom-fields) -  steps 3 to 6). Fill in values for added fields (step 3 above).

<Image align="center" alt="CreateNewAssetDialog.png" border={false} width="800px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewAssetDialog.png" />

<Callout icon="📘" theme="info">
  Note

  It is recommended to add an asset name to the new asset even if it is not a required field, as it enables identifying the asset in the Assets table by name.
</Callout>

4. Click **Save Changes**. The following notification appears: **Created new asset View Asset**. You can click the **View Asset** link to open the Asset Profile page of the new asset.
   The new asset is added to the Assets table. You may need to filter the table to see it.

### Example - Creating a New Expense Asset

The following screen shows the **Create new asset** dialog that opens when creating a new **Expense** asset.

<Image alt="CustomFieldDate" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomFieldDate.png" />

In this example, you must add a value to the two existing required aggregated fields:

* **Amount (USD)`-`Float** type field.
* **Transaction Date`-`Date** type field.

In addition to the required fields that appear on the new asset's screen, you can add optional existing fields or new fields. When you add these optional fields, you need to assign them values in order to create the new asset.