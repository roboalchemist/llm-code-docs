# Source: https://docs.axonius.com/docs/working-with-profiles.md

# Working with Profiles

Use Profiles to define a group of entitlements as logical entity that can be applied to managed identities either directly or by a [Rule](/docs/rules-page).

Profiles simplify and streamline managing user entitlements by allowing admins to create and manage groups of entitlements collectively. Additionally, Profiles enable consistent and secure permission assignments and they provide a more efficient process for users to request access to resources.

Profiles are assets under the Identity section of the [Assets page](/docs/assets-page). You can easily search for Profiles,[query](/docs/managing-queries) them, create [asset relationships](/docs/exploring-connections-and-asset-relationships), use them in [dashboard](/docs/working-with-dashboard-spaces) and [reports](/docs/reports-page), and more.

<Image alt="ProfilesPage.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProfilesPage.png" />

Profiles give you the following benefits:

* **Efficiency** - Reduces the administrative overhead associated with managing individual entitlements.
* **Consistency** - Ensures that entitlements are assigned uniformly across similar roles or profiles.
* **Security** - Minimizes the risk of incorrect or incomplete access configurations, enhancing overall security.
* **User Experience** - Simplifies the access request process by allowing users to select from predefined roles or Entitlement Set instead of individual entitlements.

From the Profiles page you can also access the simulators:

* [**Role Mining**](/docs/using-the-role-mining-simulator) - A visual representation for analysis of the relationship between entitlements and identities in your environment.
* [**Entitlement Consolidation Simulator**](/docs/entitlement-consolidation-simulator) - A visual representation to analyze existing entitlements (groups and roles) to identify similarities and redundancies.

## Creating a Profile

**To create a profile:**

1. In the [Role Mining Simulator](/docs/using-the-role-mining-simulator) chart, select the entitlements you want to group together into a set. You can select multiple entitlements by Shift+Clicking on nodes or by draging over the nodes in Select mode.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RoleMiningChart-NodeSelection.png)

2. Right-click on the selected entitlements and select **View Entitlements**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RoleMiningChart-CreateEntSet.png)

3. The selected entitlements are listed in the **Profile review** drawer. Use the Search field to find specific entitlements. The name, type and any exiting tags are listed for each entitlement.

4. Click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ProfileEditIcon.png) (Edit) to give the profile a name and description.

5. Click **Save**. The profile is added to the Profiles table on the Profiles asset page.

6. Click **Cancel** to return to the Profile review without saving.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RoleSIMProfileReviewDrawer.png)

## Assigning Profiles

A Profile is assigned to an identity via a Rule, an Access Request, or Direct from the UI.

When an Profile is assigned to an Identity or a Rule, Axonius performs several actions to ensure proper integration:

**Addition to Asset List** -  The Profile is added to the list of Profile assets associated with the Identity. This means the Identity's profile now includes these new entitlements as part of the Profile.

**Granting Entitlements** -  All individual entitlements specified within the Profile are granted to the Identity. This process ensures that the user receives all the necessary permissions and access rights defined in the Entitlement Set.

1. **Assign Entitlement Set** - The Profile is assigned to an Identity or Rule.
2. **Update Asset List** - The Profile is added to the Identity's list of assets.
3. **Grant Entitlements** - All permissions and access rights within the Profile are given to the user.

### Performing Actions on Devices

Select one or more devices and use the options in the **Actions** menu to perform various actions. Refer to [Asset Actions](/docs/devices-actions).

<Callout icon="📘" theme="info">
  Notes

  When a Profile is deleted, the Profile is removed from the assets and replaced by the individual entitlements and content that were originally contained within the Profile. This ensures that the assets retain the necessary permissions and content even after the Profile itself no longer exists.
</Callout>

## Export a List of Assets

Export CSV