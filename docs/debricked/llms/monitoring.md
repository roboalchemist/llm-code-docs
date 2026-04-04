# Source: https://docs.debricked.com/product/automation/monitoring.md

# Monitoring

OpenText Core SCA automation policies normally trigger based on pipeline events, such as committing a code to a repository. When the source code is committed, a OpenText Core SCA scan starts and automations run. However, in some cases, you might want to use automations to check the status of a repository even if you have not made any changes to it. For example, new vulnerabilities might be discovered for dependencies in repositories that are not updated regularly. Monitoring allows you to get timely warnings about issues in such repositories by automatically and periodically checking the rules regardless of pipeline events. It is possible to configure monitored automations to either result in webhooks or emails when triggered.

To enable monitoring for a new rule, follow these steps:

1. From a repository page, go to the **Automations** tab. On the Automations page, you can view the list of automation rules created.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FsgvZzz0gxODF3AY0VDd9%2Fimage.png?alt=media&#x26;token=88291b8f-be81-4efa-bc35-32ba84701125" alt=""><figcaption></figcaption></figure>

2. On the Automations page, click **New** -> **Add rule**. The Add a new rule page is displayed.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2Fu73E87iO852Fmaq6fC2a%2Fimage.png?alt=media&#x26;token=79642feb-274a-4858-b9e4-d3c99c27cc3e" alt=""><figcaption></figcaption></figure>

3. On the Add a new rule page, select the valid vulnerability condition from the drop-down. The vulnerability condition must be either 'CVSS' or 'discovery date' or both.
4. Select the valid trigger events from the drop-down. The trigger events must be either 'notify by email', 'notify user groups by email' or 'trigger webhook'.
5. Click **Enable monitoring** check box to enable the monitoring for the rule.&#x20;
6. Click **Generate rule** and review any warnings (if applicable).&#x20;
7. Click **Save**.

{% hint style="info" %}
When the monitoring is enabled for a rule, on the Automations page, you can view the ![](https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FOvOkUgw2P4DJbsHepGBF%2Fimage.png?alt=media\&token=af485690-1467-4555-9ab1-a140d622b1ad) icon next to the rule.
{% endhint %}

To enable monitoring for an existing rule, follow these steps:

1. From a repository page, go to the **Automations** tab. On the Automations page, you can view the list of automation rules created.
2. Click the **… (three dots)** on the right-hand side of the rule.
3. Select **Edit rule.**

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FmXBGpuGOpBCYThkA5TiR%2FScreenshot%202025-01-10%20161000.png?alt=media&#x26;token=6fffec60-80bc-4945-93ab-47f640c61278" alt=""><figcaption></figcaption></figure>

4. On the Edit rule page, select the valid vulnerability condition from the drop-down. The vulnerability condition must be either 'CVSS' or 'discovery date' or both.
5. Select the valid trigger events from the drop-down. The trigger events must be either 'notify by email', 'notify user groups by email' or 'trigger webhook'.
6. Click **Enable monitoring** check box to enable the monitoring for the rule.
7. Click **Generate rule** and review any warnings (if applicable).&#x20;
8. Click **Save**.

To filter the rules, follow these steps:

1. From a repository page, go to the **Automations** tab. On the Automations page, you can view the list of automation rules created.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FsgvZzz0gxODF3AY0VDd9%2Fimage.png?alt=media&#x26;token=88291b8f-be81-4efa-bc35-32ba84701125" alt=""><figcaption></figcaption></figure>

2. On the Automations page, click **filter**. The Filter by page is displayed.

<figure><img src="https://1696666310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FXrChfOBHOF0MXs8qC14m%2Fuploads%2FQgrHXBBRcO6b6XBE0U4w%2FScreenshot%202025-08-05%20161443.png?alt=media&#x26;token=3f9f1571-8232-4a95-925c-e68639c0fc31" alt=""><figcaption></figcaption></figure>

3. On the Filter by page, select the appropriate values to filter the rules. You can filter the rules based on:
   * Activation: The values are 'Active' and 'Inactive'.
   * Action: The values are 'Fail pipeline', 'Pipeline warning', 'Notify by email', 'Mark as unaffected', 'Flag as vulnerable' and 'Trigger webhook'.
   * Monitoring: The values are 'Enabled' and 'Disabled'.
   * Default rules: The values are 'Default rules' and 'Non default rules'.
