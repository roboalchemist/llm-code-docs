# Source: https://doc.keepnetlabs.com/next-generation-product/platform/reports/executive-reports/how-to-setup-manager-reporting.md

# How to Setup Manager Reporting

**Manager Reporting** lets you **automatically email managers** a scheduled report in excel format that shows **their team’s Phishing Simulation** and/or **Security Awareness Training** statistics. This helps managers track progress, follow up with their team, and supports a stronger security culture with less manual work for system admins.

## Prerequisite: Add Manager Information to Target Users

Before scheduling manager reports, ensure each target user has a manager assigned.

* Go to **Company > Target Users**
* **Create** or **Edit** a target user
* Fill the required manager fields:
  * **Manager First Name** *(Required)*
  * **Manager Last Name** *(Required)*
  * **Manager Email** *(Required)*

### Optional: Sync manager info via SCIM (Entra ID)

If you want to automatically sync Manager data (first name, last name, email address) via SCIM for your target users, [follow this guide](https://doc.keepnetlabs.com/next-generation-product/getting-started/2.-add-target-users/add-users-via-scim/scim-setup-in-entra-id).

## Step 1: Create an Executive Report with Manager Metrics

You create an Executive Report first, then schedule it.

* Go to **Reports > Executive Reports**
* Click **+ NEW**
* Expand **Manager Metrics**
* Choose **one** of the following *(one manager metric per executive report)*:
  * **Phishing Activity** (for simulation statistics)
  * **Training Activity** (for training statistics)
* Customize the report:
  * **Executive Report Name**
  * **Date Range**
  * **Date Created**, **Company Name**
* Click **Save Report.**

{% hint style="warning" %}
If you want both **Phishing Activity** and **Training Activity** manager reporting, create **two separate Executive Reports** (one per metric).
{% endhint %}

## Step 2: Schedule the Report to Send to Managers

After the Executive Report is saved, schedule it for delivery.

* Go to **Reports > Scheduled Reports**
* Click **+ NEW**
* Fill the schedule settings:
  * **Schedule Name**
  * **Frequency** (One Time, Weekly, Every two weeks, Monthly, Quarterly)
  * **Report Type:** Executive Report
  * **Report:** Select your **Manager Executive Report**
  * **Schedule Time** and **Timezone**
  * (Optional) Enable **Region-Aware Time Zone Delivery**
* In **Send to Manager**:
  * Select the managers who will receive the report
* Click **Save.**

After saving:

* Managers receive the first email shortly after (then continue based on the selected frequency).
* Each manager’s report reflects **their team members**, based on the **Manager fields** you set under **Target Users**.

## FAQs

### Q: What must be configured before Manager Reporting works?

A: Target users must have **Manager First Name, Manager Last Name, and Manager Email** filled in under **Company > Target Users**. Without these required fields, the platform cannot generate and route reports to managers.

### Q: Can I include both Phishing Activity and Training Activity in one manager report?

A: No. You can select **only one Manager Metric per Executive Report**. Create **two Executive Reports** if you need both.

### Q: Who receives the report?

A: Only the managers selected in **Send to Manager** in the scheduled report settings will receive the email.

### Q: What data will the manager see?

A: The manager receives team-level statistics related to the selected report type, such as:

* Phishing simulation performance (Phishing Activity), or
* Training progress/completion (Training Activity)

### Q: What if managers don’t receive the email?

A: Check these common items:

* Target users include **Manager First Name, Manager Last Name, and Manager Email** under **Company > Target Users** page.
* The **Scheduled Report** is **Active**
* The scheduled time/timezone is correct
* The correct Executive Report (with **Manager Metrics**) is selected

### Q: Can manager info be synced automatically?

A: Yes. You can sync manager attributes via SCIM using Entra ID. Follow the SCIM integration guide:\
<https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/scim-settings/azure-ad-scim-integration>
