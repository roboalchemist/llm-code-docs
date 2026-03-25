# Source: https://docs.axonius.com/docs/creating-a-case-from-the-findings-center-new.md

# Creating a Case from the Findings Center

You can create a Case on a Finding directly from the Findings Center table provided that:

* The Finding originates from the Findings Center.

* The Finding has triggered more than 0 alerts.

* You can also [create a Case from the Case Management page](/docs/creating-a-new-case), but in that case, you can only base it on a Simple Query, whereas, when you create a Case from a Finding, it is based on any of the following trigger conditions, as configured in the Finding:
  * **Simple query threshold** - Triggers an alert if the number of assets resulting from a query is less or more than a specified threshold.
  * **Query comparison** - Compares two queries and triggers an alert when the difference in their numbers of results is less or more than a specified threshold.
  * **Query change over time** - Compares the number of query results to the number of results on an earlier date, and triggers an alert when the difference in their numbers of results is above or below a certain threshold.

* When you create a Case on a Finding, it is created on the list of assets that triggered the alert (viewable by clicking the number link in the **Related Assets** column under **Finding> Alerts History**). When an alert is triggered by a Finding with Query comparison, this is the list of assets related to the first query in the alert. The Case is used to track remediation of this list of assets.

* You can manage the new Case together with already existing Cases from the [**Case Management** page](/docs/case-management-page), and open the configuration of any Case to track its progress and change its status or any other field (except the **Trigger Condition**, which you can not change in the Case; only in the Finding configuration).

* Case Progress is calculated based on assets from the Related Assets list that have been reconciled/remediated and no longer meet the criteria that triggered the alert.

  * For the **Simple Query** comparison trigger, there is progress each time an asset that crossed the threshold, which triggered the alert, is resolved. Progress reaches 100% and the Case is closed when all assets are resolved and all the assets (in the Related Assets list) that triggered the alert no longer cross the threshold. For example, a Simple Query that triggers an alert when the Query: number of Unmanaged Devices (no Agent or Manager) returns more than 100 assets. When all devices are resolved (all are managed), the Progress Bar reaches 100%. This works similar to a Case created from Case Management.
  * For the **Query comparison** trigger, there is progress when either Q1 has more resolved assets or Q2 has more resolved assets. For example, if the condition for triggering an alert is Q1 produces 10 more results than Q2, there is progress when Q1 resolves more assets (i.e., Q1 produces less results) or when Q2 resolves more assets (i.e., produces more results). The Progress Bar reaches 100% when the number of Q1 results = the number of Q2 results.
  * For the **Query change over time** trigger, there is progress when the query at the current date has more resolved assets or the query from the earlier time has more resolved assets. For example, if the condition for triggering an alert is Q1 produces 20 more results on the current day than it did 5 days earlier. Then, there is progress when Q1 resolves more assets on the current date (i.e., produces less results). The Progress Bar reaches 100% when the number of results from the query on the current date equals the number at an earlier date.

When all initial assets (with the exception of assets that may be removed from the system over the course of time) are remediated (Progress Bar reaches 100%), you can close a Case.

**To create a new Case from the Findings Center**

1. In the **Findings** page, select a Finding with Source = Findings Center and more than 0 alerts, and click the **Create Case** action or hover over the Finding and click the **Create Case** icon.

   The **Create Case** drawer opens.

   * The **Finding** button is enabled and the **Finding name** is displayed.
   * The **Simple Query** button is disabled, as here you can only create a Case from a Finding.
   * You can expand **Trigger Condition** to view the query configured in the Finding.

<Callout icon="📘" theme="info">
  Note

  It is not possible to create a Case from a Finding with a complex query. In this case, the Create Case icon and action are disabled.
</Callout>

![CreateCaseFromFindings](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateCaseFromFindings.png)

2. [Fill in the Case information](/docs/creating-a-new-case#filling-in-case-information).

3. Toggle on **Create case on future alerts** so that the system automatically creates a Case on future alerts triggered by the same Finding as this alert.
   * Enable the **Include only added entities from the previous alert** option to include in the Case automatically created on future alerts only assets not included in the previous alert.

![FindingsRulesCreateCaseonFuture](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FindingsRulesCreateCaseonFuture.png)

4. Optionally,[create one or more additional Queries related to the Case](/docs/creating-a-new-case#creating-additional-queries).
5. Optionally,[link Enforcements to the Case](/docs/creating-a-new-case#linking-enforcements-to-the-case).
6. If you want to inform the Case assignee (recommended) and others on the Case opening,[set an email notification](/docs/creating-a-new-case#setting-an-email-notification).
7. If you do not want to link tickets to the Case, click **Create**.  The Case is added to the **Case Management** table.

<Callout icon="📘" theme="info">
  Note

  The **Create** button becomes enabled only after you configure all required Case fields.
</Callout>

2. If you want to link a ticket to the Case, click **+ Link Ticket**. A new **Create Ticket** tab replaces the link.[Link a ticket to the Case](/docs/creating-a-new-case#creating-a-case-set) to create a **Case Set**.

If you toggled on **Set Email Notification** (see above), all email recipients specified receive an email in the following format: *A new Axonius case has been assigned to you* followed by a link to the new Case and the custom message.