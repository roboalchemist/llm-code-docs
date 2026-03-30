# Source: https://docs.axonius.com/docs/creating-a-finding.md

# Creating a Finding

You can fully customize a Finding (Finding type = System Finding) or create a new one on the basis of a rule template predefined by Axonius.

<Callout icon="📘" theme="info">
  Note

  * You can create Custom Findings only.

  * You can define Findings per Data Scope (as with Queries).

  * Findings cannot use private queries (as in the Action Center).
</Callout>

**To create a Finding**

1. On the [**Findings Center** page](/docs/findings-center-page) page, click Create Finding ![CreateFindingButton](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateFindingButton.png). The **Create Finding** dialog opens. The **Finding type** is **System Finding** (not modifiable).

![CreateFinding](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateFinding.png)

2. From the **Rule Template** dropdown, select a template on which to base the new Finding.
   * Select **Custom** (the default) to define a Finding from scratch. In this case, the fields of the Create Finding dialog are filled in with default values.

   * Select an Axonius-defined rule template to use as a basis for the new Finding. The available rule templates are listed in the dropdown in alphabetical order (see screen below). Once selected, the fields in the **Create Finding** drawer are filled in with those of the selected rule template. You can modify these fields, as described in the following steps.

![RuleTemplateDropdown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RuleTemplateDropdown.png)

3. In **Finding name**, type a unique name for the Finding. For template-based Findings, the Finding name is by default the template name. In this case, it is recommended to change the name.
4. In the **Description** field, type a description of the Finding (optional).
   * If a Custom Finding, click **+ Add description** to open this **Description** field.
   * For template-based Findings, you can modify the description.
5. Select the **Severity** of the Finding: *Informational*, *Low* (default), *Medium*, *High*, or *Critical*.
6. From the **Finding Category** dropdown, select the category of the new Finding.
7. [Set the trigger condition](#selecting-a-trigger-condition).
8. [Schedule when to run the Finding](#scheduling-the-finding-checking) to check for criteria on the selected assets.
9. [Add mute conditions](#adding-mute-conditions) to pause notifications for a certain period of time.
10. [Configure external notification on the alert](#adding-external-notification)(optional; available only for customers with the Action Center add-on).
11. Click **Create**. Note that the Create button becomes enabled only after all the fields required to create the Finding are filled in.

## Selecting a Trigger Condition

You can configure a FInding to trigger alerts based on the number of assets returned by the query.

You can configure Findings with complex conditions, including the following types:

* **Simple query threshold**
  * Compares number of assets
  * Triggers an alert when a query returns more/less than X (number) results. For example, when:
  * Adapter failed fetches `>` 0
  * There are more than 100 devices with 100+ installed SW
* **Query comparison** - Trigger an alert when query A returns X or X% more/less assets than query B. This enables cross-entity comparison, using a different asset in each query. For example, when:
  * Devices with Tanium fall below 95% of all devices.
  * The number of devices is not more than 20% of the number of users.
  * More than 10% of all devices have over 50 critical CVEs.
  * There is more than a 10% difference between the number of Tanium and Windows devices.
* **Query change over time** - Timeline comparison. Trigger an alert when a query returns X or X(%) more/less results compared to Y days earlier. For example, when:
  * AD group gains more than 10% a week.
  * Number of CVEs grows more than 20% per day.
  * Number of managed devices drops more than 15% a week.

### Setting the Simple Query Threshold Trigger

You can configure a **Simple Query Threshold** condition to trigger an alert in either of the following scenarios:

* The number of assets returned by the query is more/less than the specified number.

**To set the Simple Query Threshold trigger**

1. From the **Condition Type** dropdown, select **Simple query threshold**.
   The following condition opens.
   ![SimpleQueryThreshold](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimpleQueryThreshold.png)

2. From the **Module** dropdown, select an asset module.

3. From the **Select Query** dropdown, select a query.

4. The comparison is based on **Number of assets** returned from the query. This is currently the only option.

5. Select **More** or **Less**.

6. In the value box, type a number - the threshold to compare the number of assets or aggregated value returned by the query. Minimum possible value is **0**.

### Setting the Query Comparison Trigger

You can configure a **Query Comparison** condition to trigger an alert in either of the following scenarios:

* When query A returns X or X% more/less assets than query B.

**To set the Query Comparison trigger**

1. From the **Condition Type** dropdown, select **Query Comparison**.
   The following condition opens.
   ![QueryComparison(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryComparison\(1\).png)

2. From the **Module** dropdown, select the asset module for query A.

3. From the **Select Query** dropdown, select query A.

4. The comparison is based on **Number of assets** returned from the query. This is currently the only option.

5. In the value box, type a number. Minimum possible value is 0.

6. Click the **%** sign (blacken) to compare percentage, or leave as is to compare actual values.
   * Percentage comparison:
     ![PercentageComparisonB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PercentageComparisonB.png)

   * Actual values comparison:
     ![ActualValuesComparisonB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActualValuesComparisonB.png)

7. Select **More** or **Less**.

8. Repeat steps 2-4 for query B.

### Setting the Query Change over Time Trigger

You can configure a **Query change over time** condition to trigger an alert in either of the following scenarios:

* When a query returns X or X% more/less assets compared to Y days before the current execution time.
* When a query with calculation returns an aggregated value X or X% greater/less than the aggregated value returned Y days before the current execution time.

**To set the Query change over time trigger**

1. From the **Condition Type** dropdown, select **Query change over time**.
   The following condition opens, with a note that Findings will be first triggered after the configured number of days.
   ![QueryChangeOverTime](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryChangeOverTime.png)

2. From the **Module** dropdown, select an asset module.

3. From the **Select Query** dropdown, select a query.

4. The comparison is based on **Number of assets** returned from the query. This is currently the only option.

5. In the value box, type a number. Minimum possible value is 0.

6. Click the **%** sign (blacken) to compare percentage, or leave as is to compare actual values.
   * Percentage comparison
     ![PercentageComparison](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PercentageComparison.png)

   * Actual values comparison
     ![ActualValuesComparison](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActualValuesComparison.png)

7. Select **More** or **Less**.

8. In the **days before** box, type the number of days in the timeline prior to the current execution time. When the query executes, the number of resulting assets is compared to the number of assets resulting from the query run executed the configured number of days earlier.

## Scheduling the Finding Checking

You can schedule when to check whether the assets that are returned from the query meet the trigger condition. The following scheduling is available:

* Every global discovery cycle (default)
* Every x hours
* Every x days
* Days of week
* Days of month

**To schedule the Finding**

1. Click the **Check and Notify** box. The scheduling options dropdown opens.

![SchedulingDropDown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedulingDropDown.png)

2. From the **Check and Notify** dropdown, select one of the following options:
   * **Every global discovery cycle** (the default)
     ![SchedEveryGlobalDiscoveryCycle](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedEveryGlobalDiscoveryCycle.png)

   * **Every x hours** - For this option, in **Scheduled run every (hours)**, type the frequency in hours that the Finding runs and checks.
     ![SchedEveryXHours](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedEveryXHours.png)

   * **Every x days** - For this option, in **Scheduled run every (days)**, type the frequency in days that the Finding runs and checks, and in **Scheduled run time**, click the clock to select the time at which to run on those days.
     ![SchedEveryXDayss](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedEveryXDayss.png)

   * **Days of week** - In **Scheduled run day(s)**, remove the days on which to not run the Finding, and in **Scheduled run time**, click the clock to select the time at which to run on those days.
     ![SchedDaysofWeek](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedDaysofWeek.png)

   * **Days of month** - In **Scheduled run day(s)**, remove the days on which to not run the Finding, and in **Scheduled run time**, click the clock to select the time to run on those days.
     ![SchedDaysofMonth](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedDaysofMonth.png)

## Adding Mute Conditions

You can define mute conditions per Finding to suppress the Finding checks for a specified period of time. Instead of the same Finding checking for matches over and over again, you can make a pause following the first match, giving you the opportunity to fix the alert, enabling the best signal to noise ratio.
Some examples:

* Pause for 24 hours after the first match.
* Suppress alerts on users who haven't changed passwords from December 23rd until January 6th.
* Trigger an alert if Tanium coverage suddenly drops. As you know it will take you one or two weeks to fix it, you can define a mute period of two weeks before you get another alert.

**To add mute conditions**

1. Toggle on **Add Mute Conditions**.
2. From the **Mute Type** dropdown, select one of the following:
   * Mute time after first alert (default) - Select the number of days to mute alerts after the first match.
     ![MuteTypeA](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MuteTypeA.png)

   * Mute on specific dates -[Select a specific period of time to mute alerts](/docs/viewing-alerts#filtering-by-date).
     ![MuteTypeB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MuteTypeB.png)

   * Mute daily in this time range - Select a specific time range during which to mute alerts every day. In **From** and **To**, select the start time and end time.
     ![MuteTypeC](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MuteTypeC.png)

**To remove mute conditions**

1. Toggle off **Add Mute Conditions**.

## Adding External Notification

<Callout icon="📘" theme="info">
  Note

  Only customers with the Action Center add-on can configure an external notification of alerts in the system.
</Callout>

You can configure an external notification for any alert in the system using an Enforcement Action from the **Notify** category. This creates an Enforcement Set in the **Findings Notification Enforcements** folder and appears also in the **Shared Enforcements** folder. Once configured, when an alert is triggered, a notification is automatically sent to you via the selected notification system (for example, Slack or email).

<Callout icon="📘" theme="info">
  Note

  Once created, these Enforcement Sets are disabled and cannot be edited or run from the Action Center.
</Callout>

**To configure an external notification**

1. In the **Create Finding** dialog, click **+ Add External Notification**.
2. In the **Add External Notification** section that opens, from the **Select Action** dropdown, select the **Notify** category Enforcement Action to use to notify about the alert. The required and additional fields of the selected Enforcement Action open.

![AddExternalNotification](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddExternalNotification.png)

The following screen shows the results of selecting the **Slack - Send Message to Channel** Enforcement Action to send the external notification.\
![AppliedExternalNotification](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AppliedExternalNotification.png)

3. Fill in the required and additional fields, as relevant, and then click **Apply**. Note that the Apply button becomes enabled only after you fill in the required fields. The External Notification configuration is saved, and the configuration section of the **Create Finding** drawer opens. You can scroll down to see the name of the selected Enforcement Action under **External Notification**. The selected Enforcement Action is added to the Action Center **Findings Notification Enforcements** folder.

<Callout icon="📘" theme="info">
  Note

  * At any time before clicking **Apply**, you can click **Back to Rule Configuration** to leave the External Notification configuration without saving it, and return to the configuration section of the **Create Finding** drawer.
  * After you click **Apply** to save the External Notification, you can [modify the external notification](#modifying-the-external-notification) or [remove the external notification](#removing-the-external-notification), if required.
</Callout>