# Source: https://docs.axonius.com/docs/configuring-data-processing-settings.md

# Configuring Data Processing Settings

Use Data Processing settings to configure settings related to Identities.

## Automatic Revocation Window Settings

Select the revocation window to use. See [Using Automatic Revocation and Guardrails](/docs/using-auto-revocation-and-guardrails).

* **Revocation Window Option** *(default: Immediate Revocation)* -
  * **Immediate Revocation** - Revoke entitlements immediately upon rule trigger.
  * **Scheduled Revocation** - Revoke entitlements at the next scheduled discovery fetch, processing all pending revocations.
  * **Custom Revocation Window** - Define a specific time window (in days) for processing automatic revocations.

## Rule Suggestion Settings

* **Enable the generation of rule suggestions** - When Rule suggestions is enabled, Axonius can analyze the roles and permissions and suggest rules to enhance security and access.
* **Use the following user attributes** - The Axonius ML engine will use the enumerated attributes to build suggested rules.
* **Print rules to logs (rules will not be saved to DB)** - Add log entries when rules are triggered.

## Permission Consolidation Setting

* **Enable the generation of permission consolidation suggestions** - When enabled, Axonius will suggest permission consolidation rules.

## Role Mining Settings

Use Role Mining settings to enable the role mining engine and configure which adapter connections and entitlements to analyze.

* **Enable Role Mining engine** - Turn on the role mining engine.
* **Enable the generation of profile suggestions** - When selected, Axonius will suggest profiles.
* **Adapter Connection IDs to analyze** - Select the adapter connections you want analyzed from the list.
* **Types of entitlements to analyze** - Select the entitlement types to analyze.
* **Direct entitlement assignment only** - When selected, only entitlements directly assigned are analyzed. Entitlements assigned secondarily are not analyzed.

## Peer Group Analysis Settings

Use Peer Group Analysis settings to enable peer group analysis and configure how groups are defined.

![DataProcessingSettings.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DataProcessingSettings.png)

* **Enable peer group analysis engine** - Enable to use Peer Group Analysis.

* **Group defining attributes** - The user parameter fields used to define a group.
  The set of attributes that define the identity peers with which we want to compare. It can be a single value or a combination between attributes.
  For example:
  * Identities within the same department: `Specific_data.data.user_department`
  * Identities with the same direct manager: `specific_data.data.user_manager_mail`

* **Minimum group size** *(default: 3)* - Minimum "team" size needed to compare the drift.

* **Count if only a certain percentage of users in the team have the entitlement** *(default: 20%)* - Defines how a drifted/excessive entitlement is calculated; where the entitlement exists for a certain percentage of the team or lower. If only a small percentage of users have a particular entitlement, consider that entitlement as drifted.

## Justifications

* **If an in-app revocation occurs, any justification for entitlement is rendered invalid** - When selected, The Justification provides the info about who and when of the permission being granted. There is a Justification for each rule that grants an entitlement.
* **Enable storing previous entitlements** - When enabled, the adapter will store previously assigned entitlements.

## Abnormal Login Settings

* **Abnormal login threshold (days)** *(default: 90)* - The time between the last login and the current login attempt that is considered abnormal. For example, a user has not logged in to Okta for 95 days and then logs in. This login will be recorded as abnormal in the "Renewed Activities" list of the user asset. This record includes the date of the previous login, the new login and the gap duration in days.

## Access Request Management

* **Select Direct Manager email field** - Select the field that contains the email address of the requester's direct manager.
* **Enable these entitlements for selection** - Selected entitlements are included in the list of available access that users can request.