# Source: https://docs.axonius.com/docs/issues-and-actions.md

# Issues and Actions

## Handling Potential Issues

From the agent's row, select **View issues** from under the **Actions** column to view all issues identified by the adapter.

For each device category from the selected scope, the table shows how many potential issues were detected. If there are no issues, a green *No issues* indication appears.

Issues can be of the following types:

* **Inactive agent** - The device has been seen recently, but the agent didn't report within the expected time frame.
* **Missing agent**  - The device is in scope but is missing an agent that should be installed on it.

To view all issues for a specific device category in the Devices page, click the ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-MU4RCP6H.png) button under the **Actions** column. This opens the Devices page with results filtered by the predefined query for this specific issue.

**Example**

For SentinelOne, the system detected 3987 potential issues, broken down by the following device categories:

<Image align="center" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/asset_cloud/AgentSentintelOneDrawer.png" />

When you navigate to the Devices page from the first category row, you can see the Devices table filtered by the following query:

![IssuesDevices](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-MJ14RFBM.png)

From the Devices page you can perform different actions, for example:

* Explore a specific device on its [Asset Profile page](/docs/asset-profile-page)
* Create a ticket to escalate an issue, or send an email notification to its stakeholder using [Enforcement Actions](/docs/using-the-ec-page)
* Adding devices to a [case](/docs/cases-1)

## Additional Actions

From the **Actions** column, you can:

* View all issues, as explained above
* Generate a dashboard for each tool
* Go to the **Agents Settings** page to review or edit the following settings for each tool. Note that this is a mandatory step to be able to access dashboards.

### Agent Deployment Scope

Select the device categories you want to cover by this tool. For example, your organization might be installing Zoom only on Windows Cloud Workstations. In this case, for the Zoom adapter, select Windows Cloud Workstations and click **Save**. You can select more than one category.

### Agent States

Review the definitions for active, inactive and missing agents. These are defined by Axonius predefined queries. Click **Review Query** for the full query details.

### Exception Handling (Optional)

Use this section to exclude devices **from a category that should be in scope**. For example, you might want to cover a specific device category, but you have one or several devices with an incompatible operating system, and those shouldn't be covered.

The device exception process is done by assigning an exclusion tag to the relevant device(s). For each tool, the system generates an exclusion tag of the following format: **Exception - \[Adapter Name] - Agent Coverage**, as demonstrated below in the CrowdStrike Falcon page:

![](https://files.readme.io/b2c9f26f3b9bef1ee08b91f2b340610d860a8d3e01f228ba1f3eaa7c979320c9-image.png)

The tag card displays the following information:

* **Excluded devices** - The number of devices excluded by this tag.
* **EC Actions** - The number of Enforcement Actions used to tag devices with this exclusion tag (see more details below).
* The predefined query of assets this tag was assigned to. Click **Review Query** to review the query fields.

**To exclude devices from coverage:**

1. Copy the tag's name.
2. Go to your **Devices** page.
3. Select device(s) and add this tag to them. You can either do it manually using the **Tag** button or use an Enforcement Action. For a detailed explanation on how to tag assets, see [Working with Tags](/docs/working-with-tags) and [Axonius - Add and Remove Tag to/from Assets](/docs/add-remove-tag).
4. Save your changes.
5. The data updates as follows:
   1. The number of excluded devices is updated in the tag card. For example, if you excluded two devices from CrowdStrike Falcon coverage, the number of excluded devices will be 2.
   2. The number of **EC Actions** updates according to how many Enforcement Actions you configured to tag devices with this exclusion tag.
   3. The number of potential issues for this tool should be lower, as issues related to the tagged devices were excluded.
   4. From the predefined query, if you click **Review Query** and then **Run Query**, you will see only the excluded devices in the Devices page.