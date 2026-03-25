# Source: https://docs.axonius.com/docs/viewing-finding-information.md

# Viewing Finding Information

From the **Findings** table, you can do the following:

* [View information on a Finding originating from the Findings Center](#viewing-a-findings-center-finding).

* [View information on a Finding originating from the Enforcement Center](#viewing-an-enforcement-center-finding).

## Viewing a Findings Center Finding

From the **Findings** table, you can click a Finding to open its **Findings Info** drawer with the following:

* **Overview** tab -[Displays a summary of the Finding](#viewing-the-finding-overview).

* **Alerts History** tab -[Lists the Finding's triggered alerts](#viewing-the-alerts-of-a-finding).

### Viewing the Finding Overview

The **Overview** tab displays a summary of the selected Finding.

**To view the overview of a Finding**

1. In the [**Findings** table](/docs/findings-center-page#findings-table), click a Finding originating from the Findings Center (**Source`=`Findings Center**). The **Finding Info** drawer opens with the **Overview** tab open.

<Image alt="FindingDetails" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FindingDetails.png" />

The **Finding** drawer **Overview** tab displays the following:

* Information on the latest alert triggered by the Finding (same as in the Findings table):
  * **Latest Alert ID** - The ID of the latest alert triggered by this Finding.

  * **Last Notified** - The timestamp in UTC of the latest not muted alert triggered by the Finding.

  * **Latest Alert Status** - The status of the latest alert triggered by the Finding. Available statuses: *Open*, *In Progress*, *Closed*, *Canceled*.
    * A New label ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewBadge.png) indicates that the latest alert of this Finding was triggered since the last time you visited the Findings Center page. The badge is removed when you leave the Finding details drawer. The label appears even if the Finding is muted.

  * **Latest Alert Result** - The number of assets related to the latest alert.
* **Trigger Condition** - The configuration of the condition in the rule that triggered this alert.
* **Activity Status** - The status of the triggering rule. **Active** - If the **Activate** toggle in the **Finding Configuration** is on; **Inactive** - If the **Activate** toggle is off.
* **Severity** - Severity of the Finding. Available options are: *Informational*, *Low*, *Medium*, *High*, *Critical*. The severity of an alert is equivalent to the severity of the Finding that triggered it. The severity of alerts from sources other than Findings Center is fixed per source and is not user configurable.
* **Asset Type** - The type of asset being checked by the Finding. For example, *Devices*, *Application Settings*, *Adapters Fetch History*,*Tickets*, *Users*.
* **Finding Category** - The category of the Finding. For example, *Cyber Asset Management*, *Internal System*, *SaaS Management*.
* **Check and Notify** - The schedule according to which the Finding is configured to check the entity. Relevant for Findings Center Findings only.
* **Mute Condition** - The time period selected for muting alerts.
* **Alerts Count** - The number of times that the Finding checked that the condition exists and created an alert until and including the most recent notification. Alerts created during muting of notifications are only added to the count the next time an alert is created with notification.

### Viewing the Alerts of a Finding

In the **Alerts History** tab, you can view all the alerts triggered by a selected Finding.

* From the Alerts History table, you can open a **Related Assets** drawer that lists the Assets related to the alert, and pivot to their Assets page.

* After investigating the cause of an alert, you can change the status of the alert directly from the alert row in the **Alerts History** page.

* A blue notification dot appears near the **Alerts History** tab to indicate that there are new alerts for this Finding. Once you open the tab, this notification dot disappears.

* Near each new alert in this tab, including those triggered by a muted Finding, there is a New label ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewBadge.png).
  * The **New** label remains near the alert until you open the **Related Assets** or change the **Status** of the Alert in the **Alerts History** table, or leave the **Alerts History** page. The new label shows up even near alerts triggered when the Finding is muted.

**To view the Finding Alerts**

1. In the **Finding Info** drawer, click the **Alerts History** tab.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AlertsHistory_Findings_Center.png)

The **Alerts History** tab includes the following:

* Alert Filter -
  * **Search Alert** - Type free text found in the message of the alerts to display.
  * **Status** - From the dropdown, select the statuses of the alerts to display.
  * **From, To** - Select the period of time for which to display the alerts.

* Click **From** and select the date and optionally the time (right pane) from which to display results. Repeat for **To** and then click **OK**.

  * Both **From** and **To** dates must be filled in and be earlier than or on the current date.
  * Click the arrows to the left/right of the Month/Year header to open the previous/next month's or year's calendar page.
  * To filter results only for a specific date, select the same date twice.

  <Image align="center" border={false} src="https://files.readme.io/6b19ca195289e1ee67a949b991005bec6fc46d86a40a9b080d92b17d01ead376-FromToFilter.png" />

* **Total** - Displays the total number of alerts triggered by the Finding.

* Alerts table, with the following information:
  * **Alert ID** - The ID number of the alert. This number is assigned by the system in sequential order.
  * **Message** - The message generated by the alert.
  * **Trigger Date** - The timestamp in UTC that the finding triggered the alert.
  * **Related Assets** - The number of times the rule triggered alerts at the specified date and time.
    * Related Assets are relevant only for Findings originating from the Findings Center.
    * Clicking the link in the **Related Assets** column opens the [**Related Assets** drawer](#viewing-the-assets-related-to-the-alert) for this alert. This link is clickable only for unmuted Findings.
    * When you open the related assets of a New alert in this table, the **New** label is removed from the alert and from the **Latest Alert Status** column in the Findings table.
  * **Status** - The status of the alert. Available statuses: *Open*, *In Progress*, *Closed*, *Canceled*. You can hover over this field, and from the dropdown that opens, select a new status for this alert, as relevant. The status is also updated in the Findings table under the **Latest Alert Status** column.

#### Viewing the Assets Related to the Alert

In the **Alerts History** page of a Finding originating from the Findings Center, click the link under the **Related Assets** column to  open the **Related Assets** drawer, which displays a list of those assets that met the Trigger Condition and therefore triggered the alert.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RelatedAssets2.png)

* Click the arrow at the start of the Related Asset row to show the information per adapter connection.

* The table of assets is only available for unmuted alerts.

* For Query Comparison triggers, the alerts of the first query's assets are shown. For example, **Devices**.

* When an unmuted alert has no related assets to show, an empty table is displayed.

* In the **Related Assets** drawer, the table displays the list of assets that crossed the threshold of the trigger condition and therefore created the alert. See the documentation of the relevant Assets page for a description of the fields in the table (a subset of the fields on the Assets page).

* **Total** (above the table) displays the number of assets from the query (the first query in a Query Comparison trigger) related to the alert.

* Click the **Open in Asset Screen** link to [pivot to the Assets page](#viewing-related-assets-on-assets-page) in a new tab, listing the complete list of assets related to the alert (with all fields).

<Callout icon="📘" theme="info">
  Note

  If the Finding has been modified, the table does not show the assets related to the alerts that were triggered prior to the Finding modification. To learn more, refer to the note in [Editing the Custom Finding Configuration](/docs/managing-findings#editing-the-custom-finding-configuration).
</Callout>

#### Viewing Related Assets on Assets Page

From the **Related Assets** tab in the Alerts drawer, click the **Open in Asset Screen** link to pivot to the relevant Assets page showing the list of assets that triggered the alert. The Assets page opens in a new tab, listing the complete list of assets related to the alert at the date and time that the alert was triggered. See [what you can do on an Assets page](https://docs.axonius.com/pl/docs/working-with-assets-pages).
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FreezeAlertResults.png)

<Callout icon="📘" theme="info">
  Note

  * Verify that [Historical Snapshot Retention Settings](/docs/configuring-retention-settings) are enabled.

  * When you pivot to the assets list, it lists the assets that triggered an alert at the time of the alert (based on a historical snapshot from the time of the alert). As assets are constantly added, deleted, and correlated over time in the system, it is possible that some assets that were in the original list may no longer be in the system. Change the date to the current date from the **Display by Date** field (above figure - enclosed in red rectangle) to view a current up-to-date asset list.
</Callout>

### Investigating the Cause of a Findings Center Alert

**To investigate the cause of a Findings Center alert**

1. In the **Alerts History** drawer, click the **Related Assets** link of an Alert to [view the assets that met the Trigger Condition](#viewing-the-assets-related-to-the-alert) and therefore triggered the alert.
2. [Open the rule that triggered these alerts](#opening-the-finding-configuration).
3. Attempt to fix the issue that caused the alert.
4. [Manually update the status of the alert](/docs/managing-findings#updating-the-status-of-a-finding-alert), as relevant.

## Viewing an Enforcement Center Finding

From the **Findings** table, you can click a Finding to open its **Findings Info** drawer - **Alerts History** tab.
In the **Alerts History** tab, you can view the alerts triggered by the selected Finding that originated from the Enforcement Center. The top row is the current alert, and the rows below it are previous alerts, from the most recent to the earliest.

* After investigating the cause of an alert, you can change the status of the alert directly from the alert row in the Alerts History page.

* A blue notification dot appears near the **Alerts History** tab to indicate that there are new alerts for this Finding. Once you open the tab, this notification dot disappears.

* Near each new alert in this tab, there is a New label ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewBadge.png).
  * The New label remains near the alert until you change the **Status** of the Alert in the **Alerts History** table, or leave the **Alerts History** page.

**To view the Finding Alerts**

1. In the [**Findings** table](/docs/findings-center-page#findings-table), click a Finding originating from the Enforcement Center (**Source`=`Enforcement Center**).

The **Finding Info`-`Alerts History** tab opens.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FindingDetailsDrawerECFinding\(1\).png)

The **Alerts History** tab includes the following:

* Alert Filter -
  * **Search Alert** - Type free text found in the message of the alerts to display
  * **Status** - From the dropdown, select the statuses of the alerts to display.
  * **From, To** - Select the period of time for which to display the alerts.

* Click **From** and select the date and optionally the time (right pane) from which to display results. Repeat for **To** and then click **OK**.

  * Both **From** and **To** dates must be filled in and be earlier than or on the current date.
  * Click the arrows to the left/right of the Month/Year header to open the previous/next month's or year's calendar page.
  * To filter results only for a specific date, select the same date twice.

  <Image align="center" border={false} src="https://files.readme.io/6b19ca195289e1ee67a949b991005bec6fc46d86a40a9b080d92b17d01ead376-FromToFilter.png" />

* **Total** - Displays the total number of alerts triggered by the Finding.

* Alerts table, with the following information:
  * **Alert ID** - The ID number of the alert. This number is assigned by the system in sequential order.
  * **Message** - The message generated by the alert.
  * **Trigger Date** - The timestamp in UTC that the finding triggered the alert.
  * **Related Assets** - Not relevant.
  * **Status** - The status of the alert. Available statuses: *Open*, *In Progress*, *Closed*, *Canceled*. You can hover over this field, and from the dropdown that opens, select a new status for this alert, as relevant. The status is also updated in the Findings table under the **Latest Alert Status** column.

### Investigating the Cause of an Enforcement Center Alert

**To investigate the cause of an Enforcement Center alert**

<Image alt="FindingECMessage" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FindingECMessage.png" />

**To view the source of an Enforcement Center alert**

1. In the [**Findings** table](/docs/findings-center-page#findings-table), click a Finding originating from the **Enforcement Center**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FindingECMessage.png)

The drawer opens with information on the alerts triggered by the Findings.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FindingDetailsDrawerECFinding\(1\).png)

2. Open the [Enforcement Set Run History page](/docs/view-ec-set-history) of the Enforcement Set referred to in the **Message** column. From the Run History drawer, you can open the assets.

3. Attempt to fix the cause of the alert.

4. Under the **Status** column in the drawer, select a new status for this alert, as relevant. The status is updated in the Findings table under the **Latest Alert Status** column.