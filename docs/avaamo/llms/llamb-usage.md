# Source: https://docs.avaamo.com/user-guide/how-to/manage-platform-settings/usage-reports/llamb-usage.md

# LLaMB Usage

`LLaMB’s Usage` feature provides real-time insights into how LLaMB is being utilized in your account. In the Avaamo Platform UI, click  `Profile Icon>Settings>Usage reports>LLaMB usage` to access the `Usage` page.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FdwT0N5dcx6MeUMmZPan7%2FScreenshot%202024-10-21%20at%202.18.07%E2%80%AFPM.png?alt=media&#x26;token=9c179f40-1bf3-41ea-bf45-3e11ec05b33f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**: The data displayed in the `Usage` page is at the account level, meaning that LLaMB usage of any agent in the Avaamo Conversational AI Platform under the account using a [`LLaMB content skill`](https://docs.avaamo.com/user-guide/llamb/get-started/step-1-create-llamb-content-skill) is consolidated and displayed in this page.
{% endhint %}

## Pre-requisites

* Ensure that you have met all the general prerequisites. See [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites), for more information.
* All users who can access the `Dashboard` can view all the sections of the `Usage` page, except for the `Limit threshold notification` section. This section is only accessible to users with the `Settings` role because configuring email threshold notifications is restricted and requires careful handling. See [Roles and Permissions](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/understand-roles-and-permissions), for more information.

## How to use it?

LLaMB license for an account is based on "Generations". An agent can either respond to users by referencing a previously stored answer (in its cache), or by using an LLM. Only the LLM-based responses count towards your generation quota.

Hence, the primary purpose of the `Usage` page is to understand the "Generations" and to set up a list of users to receive alerts daily or when a specific generation quota is reached. This enables the developers/users to take appropriate action when the generation quota is reached or nearly reaching the threshold.

See [Generation usage](#generation-usage) and [Limit threshold notifications](#limit-threshold-notifications), for more information.

### LLaMB usage

At the top, you can view `LLaMB usage` , which represents the total count of all the LLaMB responses (generated or cached) across all the agents with the [LLaMB content skill](https://docs.avaamo.com/user-guide/llamb/get-started/step-1-create-llamb-content-skill) in the current account.

### Generation usage

LLaMB license is based on generations and the total number of generations is configured for an account based on the license details. In this section, you can view the following details:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F9mMsA5It5z0IWPDYZkgH%2FScreenshot%202024-10-21%20at%202.18.07%E2%80%AFPM%20copy.png?alt=media&#x26;token=887eb2bf-cf7a-4a33-b66f-95d276836c3c" alt=""><figcaption></figcaption></figure>

**Generation usage**: Shows the count of utilized generations at the account level out of the total available generations.

**Date range**: By default, the generation usage for a week (7 days) from the current date is displayed.&#x20;

* Click the date range to select different date options as per your requirements.
* You can also view the Generation usage for Yesterday, Today, Last 7 Days, Last 30 Days, and Last 180 Days.
* Click `Custom range` to pick your custom date range by selecting the start and end dates. You can view up to 6 months of usage in this section.

### Export usage report

You can now easily export your LLaMB usage data using `Export usage report` for better tracking and analysis.

* Get a CSV report of your LLaMB usage, including regression testing details
* Use it to analyze trends, optimize usage, and make data-driven decisions

Following are the different columns available in the exported LLaMB usage CSV file.

* **Created By**: The name of the user who created the report.
* **Environment**: The environment where the response was generated.
* **Agent Type**: The type of agent (Standard or Advanced).
* **Agent ID**: The unique identifier of the agent.
* **Agent Name**: The name of the agent that generated the response.
* **Agent Creation Date (UTC)**: The date when the agent was created, in UTC
* **LLaMB Query Generations**: The total number of LLaMB-generated responses for the `first-time answers` when queries are asked.
* **LLaMB Regression Generations**: The total number of LLaMB-generated responses for the `first-time answers` during `regression testing`.
* **Cached Responses (Query + Regression)**: The total number of `cached` LLaMB responses, including both `queries and regression tests.`
* **Generated Responses (Query + Regression)**: The sum of `LLaMB Query Generations` and `LLaMB Regression Generations.`
* **Total Responses (Cached + Generated)**: The sum of `Cached Responses (Query + Regression)` and `Generated Responses (Query + Regression`**)**.

## Use case to understand LLaMB Usage

To understand the different components in the LLaMB Usage section, consider a `Travel assistant` where you have ingested a few travel policy documents in your LLaMB Content skill,

* **LLaMB responses**: This is the sum of `Generations + Cached responses` for the specified date range.
* **Generations**: Total number of generated LLaMB responses in the specified date range. If the user is asking a question on travel policy and this is the first time the answers are being generated by LLaMB, then it necessitates the use of LLM. This is counted as a generation.
* **Cached responses**: Total number of cached responses in the specified date range. For faster results and better efficiency, the responses generated by LLaMB are cached. If a user asks the same or similar query, then instead of generating a response from LLM, the cached response is displayed to the user. In the `Travel assistant`, if the user is asking the same or similar question on travel policy that is already generated, then the cached response is displayed.&#x20;
  * If the retrieved context is the same, and the query has only a slight variation, a cached response is used. For example, if there is a similar query and the articles/documents matched are the same as any of the earlier responses, then the system uses a cached response.
  * Once a response is cached, it is always available for future use as per the [data retention policy ](https://docs.avaamo.com/user-guide/ref/data-retention)and not deleted from the cache until then. This helps in optimizing the generation cost.
* **Performance gain**: This represents the growth in generation capacity resulting from caching and is computed by dividing the number of cache responses by the number of generations.&#x20;
* **Usage over time**: A graphical representation of the LLaMB usage for the account in the specified data range.

## Limit threshold notifications

In this section, you can set up a list of users to receive alerts daily or when specific generation limits are reached. You can add multiple users per notification.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FtPFLdziwP140vynUnQ6x%2FScreenshot%202024-10-22%20at%202.13.29%E2%80%AFPM.png?alt=media&#x26;token=25972507-b7c8-4f29-a62d-0774990d3a18" alt=""><figcaption></figcaption></figure>

* You can set up notifications to receive daily alerts or when the generation quota has reached 50%, 75%, or 90% of usage.&#x20;

{% hint style="info" %}
**Notes**:&#x20;

* To prevent inbox clutter, notifications for specific generation quota alerts are sent only once upon reaching the threshold except when the threshold is reached 100%. If the generation quota has reached 75%, then only the 75% generation quota alert is sent to the users, 50% generation quota alert, in this case, is not triggered again.

* When the generation quota reaches 100%,  the notification is sent to all the users configured to receive notifications for different threshold limits on a daily recurring basis until the generation quota limit is increased.

* If you prefer to receive recurring alerts, you can configure the `Daily` alert settings.
  {% endhint %}

* For each trigger, specify the required email IDs for whom the notifications must be sent and press `Enter`. You can provide any number of email IDs to receive the generation quota notification; presently, there are no limitations on the quantity.

* When the required generation quota is reached, the notification alert email is sent to the configured users.&#x20;

* When 90% or 100% generation quota is reached, warning messages are displayed in the `Usage` page allowing the users to take any further required actions.
