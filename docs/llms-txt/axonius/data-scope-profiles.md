# Source: https://docs.axonius.com/docs/data-scope-profiles.md

# Data Scope Profiles

Use data scope profiles to manage restricted fields separately. Profiles can be applied to multiple data scopes easily, without configuring each data scope's restricted fields individually. You can create profiles for each type of user and role and apply that profile to the data scope assigned to those users or roles.

Profiles are saved sets of included and excluded fields that allow you to mask the full data set and manage the restricted fields in one place. You can include specific fields from specific adapters. When fields are included, only those fields specifically included are available within the data scope. When fields are excluded, all other fields are available and only the excluded fields are not available.

Profiles are listed on the **Data Scope Profiles** tab of the Data Scopes page.

**To access the Data Scope Profiles tab:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/System%20Settings%20icon.png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **User and Role Management**, and select **Data Scopes**.
3. Click the **Data Scope Profiles** tab.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DSProfilesPage\(1\).png)

The Data Scope Profiles tab provides the following information:

* **Profile Name** - The name of the profile.
* **Data Scope Name** - The names of the data scopes to which the profile is applied.
* **Assets** - The asset types defined in the profile.
* **Last Updated** - The time stamp when the profile was last updated.
* **Updated By** - The user that last updated the profile.

## Enabling Data Scope Profiles

To use data scope profiles, you must enable them globally in the Data Scope Settings for all data scopes. Once enabled, the **Data scope profile** section appears in the data scope configuration drawer of each data scope. See [Data Scope Settings](/docs/data-scope-management#data-scope-settings)

## Adding a Data Scope Profile

**To add a new data scope profile:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **User and Role Management**, and select **Data Scopes**.
3. Click the **Data Scope Profiles** tab and then **+ Data Scope Profile**.
4. In the **Name** field, give the profile a name. Profile names are case sensitive. Once you enter a name it appears in the title bar of the drawer.
5. Click **+ Add description** to add an optional description of the profile in the Description field.
6. To define the profile by assets and fields:
   a. On the **Assets and fields** tab select the asset types you want and click **Apply**.

<Image align="center" alt="DSProfileNewSelectAssets-1.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DSProfileNewSelectAssets-1.png" />

The selected asset types are listed. Note that next to each asset type the `All Data` tag indicates that there is no restriction yet on which assets will be included in the data scope.

<Image align="center" alt="DSProfile-AssetsFields.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DSProfile-AssetsFields.png" />

b. Expand each asset type to configure fields to include or exclude from the data scope when the profile is applied. Profile selections override any included or excluded fields configured as part of the data scope. When fields are included or excluded the `Partial Data` tag appears next to the relevant asset type.

<Image align="center" alt="DSProfile-AssetsFieldsExpanded.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DSProfile-AssetsFieldsExpanded.png" />

c. To change the asset types you selected, click **Edit** and select the asset types you want from the list and click **Apply**. Then select the fields to include or exclude for each type.

<Image align="center" alt="DSProfile-AssetsTypesEdit.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DSProfile-AssetsTypesEdit.png" />

7. To hide all data from selected adapters, on the **Define by Adapters** tab, select from the list the adapters whose data you want to completely hide. See [Managing Data Scopes](/docs/data-scope-management#defining-a-data-scope-by-adapter).

<Image align="center" alt="ProfileHideByAdapter.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProfileHideByAdapter.png" />

9. Click **Save** to create the profile. It is added to the Profiles list and can be applied to any data scope.

## Applying a Profile to a Data Scope

Once a profile is created, it can be added to any data scope.

**To apply a profile to a data scope:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **User and Role Management**, and select **Data Scopes**.
3. Click the **Data Scopes** tab and then select a data scope.
4. In the drawer, under to **Data scope profile**, enable **Apply**.
5. From the list, select a profile. Only one profile can be applied to a data scope. The field restrictions in the profile override the included and excluded fields configured under the [**Refine data by fields**](/docs/data-scope-management#defining-a-data-scope-by-assets) section.

<Image align="center" alt="DSProfile-ApplyToDS.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DSProfile-ApplyToDS.png" />

6. Configure the rest of the data scope details and click **Save**. The profile is applied to the data scope. When a profile is used, the **Refine data by fields** option is disabled and the field configurations from the profile are shown greyed. The `Partial Data` tag appears next to the asset type name.

   <Image align="center" alt="DSProfileAppliesFieldsGreyed-box.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DSProfileAppliesFieldsGreyed-box.png" />

## Editing a Profile

You can edit a profile at any time. Note that when a profile is applied to multiple data scopes, changing a profile may affect all those data scopes to which it is applied.

**To edit a profile:**

1. From the Profiles tab of the Data Scopes page, select a profile.
2. Make the changes you want. You can change any aspect of the profile.
3. Click **Save**. If the profile is applied to one or more data scopes, a message is displayed listing those data scopes. To save the changes, click **Yes**.