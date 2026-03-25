# Source: https://docs.axonius.com/docs/add-remove-tag.md

# Axonius - Add and Remove Tag to/from Assets

The **Axonius - Add Tag to Assets** action adds one or more defined tags to all relevant assets.
The **Axonius - Remove Tag from Assets** action removes one or more defined tags from all relevant assets.

The relevant assets are:

* Assets returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Add Tag to Assets

### Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Tag names** - Search for and choose one or more tags from a list of all the tags defined in the system. These tags will be added to all relevant assets. If the desired tag name does not exist in the system, you click **Add New** to add it.

  Use **Select All** to select all tags, and **Clear All** to clear all selected tags from the list.

* **Tag color** - Set a color for the tag background. The default background color is white.

### Additional Fields

These fields are optional.

* **Remove this tag from entities not found in the saved query results** -  Select whether to also remove the configured tags from all entities that are not part of the list of assets the **Enforcement Task** ran on. To see a list of these assets, view the [run history](/docs/view-ec-set-history) detail and click **Additional** in the drawer header.
  ![ECRunHistory-Additional.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECRunHistory-Additional.png)

**Expiration date type**
You can set an automatic expiration date for a tag or a group of tags on assets
in a query. In this way you can add a tag to one or more assets for a defined period of time; once the defined time ends, the tag is automatically removed from the assets. This can be useful for instance, if you have a system that cannot be patched for a specific period of time. You can create a saved query that will exclude assets with this specific tag. As a result, tagged assets will not be included in reports and dashboards using that saved query for the set time, until the tag expires.

From the drop down select an option

* **No Expiration**
* **Specific Date**
* **Days from Now**

By default, tags do not have an expiration date.

**Setting a Specific Date**

1. Select **Specific Date**
2. In **Expiration date** field that appears, click **Select Date**.
3. In the date picker that is displayed, choose a date.
4. Click **Save**.

*Expiration Date:* now appears in the Auto-Expiring Tags column on the relevant Assets page.

**Setting Days From Now**

* Select **Days From Now**.
* Click in the **Days to expiration** field that appears.
* Using the Up/Down arrows, select the number of days from now for the tag to expire.
* Click **Save**.

*Expiration Date:* now appears in the Auto-Expiring Tags column on the relevant Assets page.

## Remove Tag from Assets

### Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Tag names**  -  Search for and choose one or more tags from a list of all the tags defined in the system. These tags will be removed only from entities that are already tagged with the specific tag name. Use **Select All** to select all tags, and **Clear All** to clear all selected tags from the list.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).