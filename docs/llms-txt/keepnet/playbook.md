# Source: https://doc.keepnetlabs.com/next-generation-product/platform/incident-responder/playbook.md

# Playbook

The Incident Responder Playbook feature is used to create rules that automate the analysis and incident response to suspicious emails, which saves valuable time.

The Playbook rules will work only if the reported email matches the condition in the rules.

## Defining a Playbook Rule

From the sidebar on the left side of the dashboard, select **Incident Responder**. Select **Playbook** and click **+ NEW** to create a new rule with the criteria below.

<table><thead><tr><th width="152.54879972451124"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>Rule Name*</td><td>Name of the playbook rule</td></tr><tr><td>Description</td><td>More information/detailed description of the playbook rule</td></tr><tr><td>Priority</td><td>Priority level of the playbook rule</td></tr><tr><td>Tags</td><td>Tags related to the playbook rule</td></tr><tr><td>Active</td><td>Status of the playbook rule: active or passive</td></tr></tbody></table>

{% hint style="warning" %}
The fields marked with (\*) are required.
{% endhint %}

Click **Next** to set the conditions for use.

### Condition Criteria

The following parameters can be used to define reported emails:

<table><thead><tr><th width="152.54879972451124"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>From</td><td>Sender email address</td></tr><tr><td>To</td><td>Recipient email address</td></tr><tr><td>CC</td><td>Copied recipient email address</td></tr><tr><td>Sender IP</td><td>Sender IP address or Sender IP as a Regex pattern</td></tr><tr><td>Subject</td><td>Subject line of the email</td></tr><tr><td>Keyword</td><td>Specific words used in the email body</td></tr><tr><td>Attachment name</td><td>Name of the email attachment</td></tr><tr><td>Attachment hash</td><td>Hash (SHA512 or MD5) value of the e-mail attachment</td></tr><tr><td>Attachment extension</td><td>File extension of the e-mail attachment, e.g., .pdf, .docx</td></tr></tbody></table>

### Condition Types

The conditions can be defined using the following parameters:

<table><thead><tr><th width="152.54879972451124"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>contains</td><td>Contains the specified condition criterion</td></tr><tr><td>does not contain</td><td>Doesn’t contain the specified condition criterion</td></tr><tr><td>is equal to</td><td>Specified condition criteria match exactly</td></tr><tr><td>is not equal to</td><td>Specified condition criterion does not match exactly</td></tr><tr><td>exists</td><td>Specified condition criterion exists</td></tr><tr><td>does not exist</td><td>Specified condition criterion does not exist</td></tr></tbody></table>

### Actions

The following actions can be applied when a reported e-mail meets the criteria defined in a playbook rule:

<table><thead><tr><th width="152.54879972451124"></th><th width="581.1428571428571"></th></tr></thead><tbody><tr><td>Mark as</td><td>Mark the reported email as undetected, phishing, malicious, or simulation.</td></tr><tr><td>Analyze</td><td>Analyze the reported email with defined integrations.</td></tr><tr><td>Analyze > Investigate according to analyze results</td><td>Start an automatic investigation based on the analysis results. If the analysis results are phishing or malicious, an investigation will be started based on the configuration.</td></tr><tr><td>Investigate</td><td>Launch an investigation. Learn more about investigations <a href="investigations">here</a>.</td></tr><tr><td>Notify</td><td>User(s) are notified via email. The notification email template can be customized and the recipient(s) can be designated <a href="../company/company-settings/notification-templates">here</a>.</td></tr><tr><td>Notify According To Analysis Result</td><td>User(s) are notified via email when the reported email's analysis result matches the selected results.</td></tr><tr><td>Status</td><td>Case status is updated as Closed, In progress, Open, or False positive.</td></tr><tr><td>Tag</td><td>Use this tag to easily locate your playbook rule on the playbook page or elsewhere.</td></tr></tbody></table>

## Update Conditions or Settings of a Playbook Rule

To change a playbook rule, select **Incident Responder > Playbook** page from the left sidebar menu of the dashboard. All of the existing rules will be displayed. Select the rule(s) to be updated and click on the **pencil** (edit) icon under the **Action** column to update details of a playbook rule.

## Delete a Playbook Rule

To delete a playbook rule, select **Incident Responder > Playbook** page from the left sidebar menu of the dashboard. All of the existing rules will be displayed. Select the rule(s) to be deleted and remove them using the **trash can** icon.

## FAQ

### Q: Will deleting a playbook rule affect the results of previous investigations?

A: No. Earlier playbook results using the rule will not be affected.

### Q: Will creating a new playbook rule affect the results of previous investigations?

A: No. A new playbook rule will only affect future investigations.

### Q: If I edit an existing playbook rule, does it change the rules for current investigations?

A: No. There will be no changes to existing investigations. When you edit a rule, it will only affect future investigations where the rule applies.

### Q: If I set playbook rules that are similar or contradictory, which will have priority or be valid?

A: The priority and criteria assigned when setting the rule govern the actions taken.

### Q: How can I edit or update the notification email templates used with the Notify action?

A: You can go to **Company > Company Settings > Notification Templates** to view and update the template library. You can find additional information [here](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/notification-templates).
