# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reporting/reporting.md

# Source: https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reporting.md

# Usage Reports

{% hint style="info" %}
This feature is available for teams using Tabnine Enterprise (private installation).\
\
When using the Tabnine Enterprise (SaaS) option, the customer admin receives periodic reports via email. For more details, contact your Tabnine account manager.
{% endhint %}

{% hint style="info" %}
Take a look at the [Reports Glossary](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reporting/reports-glossary) to learn about terminology and definitions.
{% endhint %}

## Tabnine Enterprise (private installation) usage reports

Tabnine Enterprise admins can access usage reports for their teams.

These reports provide insights into the team members' onboarding status, usage volumes, and additional data.

Usage reports are **available on the admin level.** The rest of the Tabnine team has no access to the usage data. However, a team admin can export the report from the Tabnine admin console as CSV files and share them with the rest of the team if they wish.

Reports can be viewed for the entire organization or a specific team.

There are two types of reports:

* [Visual usage reports ](#visual-usage-reports)in the Tabnine management console
* [CSV-based usage reports](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reporting/reporting)

You can [schedule sending the CSV-based usage report](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reporting/reporting/configuring-scheduled-csv-reports) by email.

## Visual Usage Reports

{% hint style="info" %}
These reports have been available since version 5.7.0.
{% endhint %}

Go to the Tabnine management console and sign in as an admin.

Usage reports can be found on different pages:

* [Analytics / Overview](#overview-page): High-level usage overview and activity trend charts
* [Analytics / Usage](#usage-page): For more detailed usage reports for the entire organization or a specific team
* [Analytics / Usage per User](#usage-per-user-page): For a usage overview per user in the organization or a specific team

Additionally, you can view other reports on the following pages:

* [User Management reports](#user-management-report): High-level view of and insights into how many users have successfully onboarded Tabnine
* [Settings / License Utilization](https://docs.tabnine.com/main/administering-tabnine/settings/license-settings#account-utilization-history): Shows the current and historical account utilization

### Overview page

The overview contains a high-level overview and activity trends in your account:

### **Header Controls**

At the top of the page, you can filter data by team and by timeframe. This lets you narrow in on specific groups or review broader usage trends across your entire organization.

Here, you can choose from any of the teams OR the entire organization, as well as one of three options for timeframe:

1. Daily (Last 30 Days)
2. Weekly (Last 12 Weeks)
3. Monthly (Last 12 Months)

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c63e744e3eda86859ddf114b0b3110d0b6397e38%2FLast%2030%20Days.png?alt=media" alt=""><figcaption></figcaption></figure>

An export option is available for generating detailed reports.

### **Licenses Summary & Account Utilization Metrics**

The license banner shows how many users are currently registered compared to the total licenses available in your plan. This helps track adoption and capacity at a glance.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-84be8cf8999d0a409ec284a6e4f8af563bfa37fe%2Flicenses.png?alt=media" alt=""><figcaption></figcaption></figure>

Key performance indicators (KPIs) provide a quick snapshot of overall engagement.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ca6a35ab131ca0a994b8ef6c12ed86f661fd20c8%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Metrics here cover active users, chat activity, productivity factor, chat consumption rate, and automation factor.

#### Overview metrics

* **Registered Users:** The current number of [Registered Users](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#user-status) out of the total licenses available for this account (this number does not change for a specific team)
* **Active users:** The total number of users that have [actively used](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#active-user) Tabnine from the given population in the given timeframe
* **Total Usage:** The number of code completions and useful chat interactions performed by the population in the given timeframe
* **Automation Factor:** The code completion's[ automation factor](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#automation-factor) for the given population in the given timeframe (available when there is enough code completion activity)

#### **Active Users**

The numbers count active users as any users who has participated in at least one chat OR accepted one code completion that day. This chart displays the number of unique users active each day within the selected timeframe. Use it to identify adoption trends as well as spikes and ebbs in usage.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f4cc9b3c360ee01230cb4b8dd563994363840d98%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Total Usage**

The usage chart breaks down daily activity into three categories: inline actions, chat, and *accepted* code completions. The chart can be displayed by day, week, or month.

### Usage page

The Usage page contains more detailed usage reports and insights for the entire organization:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBNIsOBlawtxjYERGqPPT%2FUsage%205-28-2.png?alt=media&#x26;token=b95ebc0e-0d5a-4044-9cfa-d192647dcfb8" alt=""><figcaption></figcaption></figure>

#### Population Filter

The displayed data can be adjusted by populatio&#x6E;**:** "All Teams" (default) or a specific team.

#### Monthly accepted lines of code trend chart

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FVimCLEgqARGj1fAw5Klb%2FScreenshot%202026-02-22%20at%2015.49.00.png?alt=media&#x26;token=e22a3e0e-486b-4387-8c49-84cd7d132965" alt=""><figcaption></figcaption></figure>

The total number of lines of code in accepted code completions or useful chat interactions (that involved coping code) performed by the selected population

{% hint style="info" %}
**Note:** The lines of code chart have been available since version 5.8.0. The lines of code data has been collected since version 5.7.0
{% endhint %}

#### Useful chat interactions by consumption type

Display the distribution of [useful chat interactions](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#types-of-useful-chat-interactions) by consumption type (how did the users consume the chat answers) in the last 30 days.

**Note**: The data for this chart has been collected since version 5.7.0

#### Chat interactions by trigger

Display the distribution of [chat interactions](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#chat-interactions-and-useful-chat-interaction) by interaction trigger (Free text prompt or built-in command) in the last 30 days.

### **Agent Usage page**

The Agent Usage page in the Admin Console provides analytics on how your organization is using Tabnine Agent over a selected timeframe. It helps admins understand adoption, monitor cost, and optimize configuration.

#### **Timeframe**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FoISQeX7q55mFYNtbJNNg%2Fimage.png?alt=media&#x26;token=42cf5627-7b76-4574-a8ca-d1a23da42b63" alt="Agent Usage Timeframe"><figcaption></figcaption></figure>

At the top of the page, you can select a monthly timeframe (e.g., “Feb 2026”) from the dropdown menu. You will see a Month trend summary bar that shows:

* Total usage against your monthly budget or quota
  * Percentage used
  * Remaining budget/credits
  * Estimated number of days remaining at the current burn rate

#### **Usage by Model**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FOwxBZY9wNFLKJeIIiXxx%2Fimage.png?alt=media&#x26;token=177d183d-4ada-4605-b168-04cba842cb24" alt="Usage by Model"><figcaption></figcaption></figure>

The Usage by Model table shows how all the available AI models are being used in the above-selected timeframe, according to the following metrics:

* **Model name:** The name of the AI model. Each row represents one model.
* **Total tokens:** The total number of tokens processed by that model in the selected timeframe, including both:
  * **Input tokens:** The number of tokens sent to the model (prompts, instructions, context)
  * **Output tokens:** The number of tokens generated by the model in responses
* **Cache read:** The number of tokens served from cache rather than recomputed, if caching is in use
* **Cache write:** The number of tokens written into cache for potential reuse
* **USD:** The total cost attributable to this model in the selected timeframe, in US dollars

#### **Usage by Team**

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FKfpcBBv0uVm9jWWm0JvX%2FUsage%20by%20Team.png?alt=media&#x26;token=aa118edf-67c7-48fb-b676-c8f797a59d9e" alt=""><figcaption></figcaption></figure>

The Usage by Team table shows AI usage and costs are distributed across all of your organization’s teams (by the above-selected timeframe).

You will see a breakdown of 1) the **percentage** of usage conducted by team, and 2) the **cost** of each team’s operations.

### Usage Per User page

The Usage per User page contains a usage overview per user in the organization or team:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FcC57SaDUyW4fSEPOjdzD%2FUsage%20by%20User%205-28-2.png?alt=media&#x26;token=61d5be77-9ec7-481d-add4-f25d0c605611" alt=""><figcaption></figcaption></figure>

## Account utilization history

Include the account utilization for the current as well as previous months:

{% hint style="info" %}
Introduced in version 5.6.0, Moved under the **Analytics** menu in version 5.8.0
{% endhint %}

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FPnsAiTYndNutFxNU4Orp%2FAcct%20Utilization%205-38-2.png?alt=media&#x26;token=69256149-45cd-4542-ac59-e61eb5ff5fbb" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The data for the current month is not final. The data for previous months is final.
{% endhint %}

#### Registered users (throughout the month)

The total number of different users who registered throughout the month, including users who were deactivated by the end of the month

#### Registered users (end of month)

The total number of registered users at the end of the month

#### Deactivated users (end of month)

The total number of deactivated users at the end of the month

#### Users with pending invitations (end of month)

The total number of invited users at the end of the month

Learn more about [user status](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#user-status). In this context, **Registered** users are users in the status *Registered*, *Connected*, or *Used*.

### User Management report

The User Management page lets the admin monitor the number of users who were invited, registered, connected to the IDE, and started using Tabnine. It also helps the admin find users who have not yet successfully onboarded. [Learn more about the different statuses and flows in Tabnine.](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#the-following-chart-explains-the-user-status-flow-for-a-tabnine-user)

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2F0rgHAzdRXqcrqJx5p5Wn%2FUser%20Management%205-28-2.png?alt=media&#x26;token=9dd65eff-4102-46e7-9377-f760b3b9d7b9" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-58481787df0acd428982e13f562f6122ce989a3f%2FUser%20managementt%20report.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Team Filter

The displayed data can be adjusted by population: The entire organization (default) or a specific team.

#### Funnel Overview

**Licenses:** The total number of the licenses in the account (does not change for a specific team)

**Registered:** The total number of the current [registered](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#user-status) users: (Status=Registered, Connected, or Used)

**Used:** The total number of users who have ever used Tabnine (i.e., users who have completed at least one code completion or chat interaction, Status=Used)

#### Onboarding Gaps: Overview & Filters

This section shows different onboarding gaps, meaning the number of users is not in the Used status yet. Each label focuses on different onboarding statuses, letting the admin know how to guide these users towards using Tabnine.

These labels are status filters; the admin can click (or unclick it) to see only specific users.

* **Invited, not yet registered** (Status=[Invited](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#user-status)): These users should accept their email invitation and sign up for Tabnine. The admin can resend them an invitation as a reminder.
* **Registered, not yet connected** (Status=[Registered](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#user-status)): These users should install and connect to Tabnine in their IDEs.
* **Connected, haven't yet used** (Status=[Used](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#user-status)): These users should be able to use Tabnine. The admin may offer them some training material to make sure they are set for success.

#### Users List

The Users list shows the users adjusted by the team or onboarding status filters.

Each user appears with their email, team, role, status, and last seen.

**Status:** Invited, Registered, Connected, Used, or Deactivated. [Learn more](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reports-glossary#user-status)

**Last seen:** Is defined as follows for each status:

* Invited: Since the email invitation
* Registered: Since the signup date
* Connected: Since the last time the user was connected to the IDE
* Used: Since the deactivation date

The admin can perform different actions on the displayed users:

* Assign to an Admin or Member role
* [Resend or revoke](https://docs.tabnine.com/main/administering-tabnine/inviting-users-to-your-team#resend-an-invitation-or-revoke-an-existing-invitations) an email invite
* [Reset a user's password](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/deactivating-and-reactivating-users-1)
* [Deactivate or reactivate a user](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/deactivating-and-reactivating-users)
* [Anonymize a deactivated user](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/deleting-pii-data-of-a-deactivated-user)
