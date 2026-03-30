# Source: https://docs.debricked.com/product/automation/set-up-webhooks.md

# Set up webhooks

In order to send a webhook request when an automation rule is triggered, add a "trigger webhook" action to the rule and enter the URL for the webhook in the URL field. When the rule is triggered, a POST request will be sent to the given URL with JSON-encoded data about the event.

The JSON will contain the following keys:

| Key          | Type    | Description                                                                                                                       |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| repository   | string  | Name of the repository which was scanned                                                                                          |
| branch       | string  | Name of the branch which was scanned                                                                                              |
| commit       | string  | Name of the commit which was scanned                                                                                              |
| commitLink   | string  | Link to a page debricked.com, where scan results for this commit are available                                                    |
| ruleId       | integer | Unique identifier for the rule that was triggered                                                                                 |
| ruleLink     | string  | Link to a page in debricked.com, where the triggered rule can be viewed or edited                                                 |
| triggeredFor | array   | Array of objects, where each element describes a combination of a vulnerability and a dependency which caused the rule to trigger |

Each element of *triggeredFor* will contain the following keys:

| Key                | Type          | Description                                                                                                                                      |
| ------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| dependency         | string        | Name of the dependency which caused the rule to trigger                                                                                          |
| dependencyLicenses | array         | Array of licenses affecting the dependency, each encoded as a string using the same name as shown in the license view                            |
| dependencyLink     | string        | Link to the dependency on debricked.com                                                                                                          |
| cve                | object / null | Information about the vulnerability which caused the rule to trigger, or null if the rule doesn't have any conditions related to vulnerabilities |
| cve.name           | string        | Name of the vulnerability that caused the rule to trigger                                                                                        |
| cve.link           | strint        | Link to the vulnerability on debricked.com                                                                                                       |
| cve.cvss2          | number / null | CVSS2 score for the vulnerability, or null if not available                                                                                      |
| cve.cvss3          | number / null | CVSS3 score for the vulnerability, or null if not available                                                                                      |

### **Send a sample request** <a href="#howdoisendasamplerequest" id="howdoisendasamplerequest"></a>

A sample webhook request can be sent to the specified URL by clicking **Send sample request**. The *triggeredFor* array will be populated using up to three vulnerabilities that were found the last time this repository was scanned. Note that these vulnerabilities may not necessarily fulfill the conditions specified in the rule.

### **Verification secret** <a href="#verificationsecret" id="verificationsecret"></a>

To ensure that a webhook request was sent by Debricked, a key can be specified in the *verification secret* field. When a verification secret is specified, webhook requests made by this rule will include the header X-Debricked-Signature, containing an SHA256-HMAC signature generated using the webhook payload and the verification secret.

### Set up a webhook with slack through Zapier <a href="#howdoisetupawebhookwithslackthroughzapier" id="howdoisetupawebhookwithslackthroughzapier"></a>

You can use the automation engine to send notifications to Slack, with the help of middleware, e.g. Zapier. Keep in mind that this is currently only possible using the premium version of Zapier.

**To create a webhook URL:**

1. Open [Zapier](https://zapier.com/app/zaps).
2. Click **+Create Zap**.
3. Search for and select **Webhooks by Zapier**.
4. Go to the **Event** drop-down, select **Catch Hook** and click **Continue**.
5. Copy the Webhook URLI.
6. Click **Continue** and then **Test trigger**.
7. Once you have the URL, open the Debricked tool and go to **Automations** on the left-side menu.
8. You can either create a new rule or edit an existing one in the **Then** statement. Once done, add the **trigger webhook** action.
9. Paste the Webhook URL copied from Zapier into the field.
10. If needed, click **Send sample request** to test if everything works correctly.
11. Click **Generate rule** and **Save.**

### **Set up notifications in slack using webhook**

To manage your notifications in Slack:

1. Open [Zapier](https://zapier.com/app/zaps).
2. Click **Action** and select **Slack.**
3. Go to the **Event** drop-down and select the desired action. For example, **Send Channel Message**.
4. Click **Choose account** and follow the instructions on the page to connect your Slack account to Zapier.
5. Click **Set up action** and select the data that you want to send.
6. Click **Message text** and select the information to be included in the message.
7. Click **Test action**.
8. Click **Publish Zap**.

Now you are ready to receive Slack notifications from Debricked!
