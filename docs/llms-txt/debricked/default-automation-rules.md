# Source: https://docs.debricked.com/product/automation/default-automation-rules.md

# Default automation rules

To make things easier for you, OpenText Core SCA has created a set of default rules that are activated on your first scan and applicable to all of your repositories. **As an administrator**, you are also able to disable existing default rules and can assign new rules to be added to integrated repositories by default.&#x20;

Keep in mind that once a rule is marked as default, it will be enabled for new repositories, even if it was disabled for existing repositories.

### Set a rule as a default rule

1. Go to **Automation** on the left side menu. Here, you can [**create new automation rules**](https://docs.debricked.com/product/automation/create-an-automation-rule), as well as [**edit**](https://docs.debricked.com/product/automation/edit-an-automation-rule) the existing rules&#x20;
2. Click **Default rule.**
3. In the confirmation modal, select whether the rule should be activated for only newly integrated repositories or existing repositories as well.
4. Click **Confirm.** From now on, only newly integrated repositories will be affected by your default rule.\
   &#x20;

This can also be done when creating or editing an automation rule:

1. Click **New+** to create a rule OR **Edit rule** in an existing rule.
2. Tick the **Default rule** checkbox.
3. Click **Save**. From now on, newly integrated repositories will be affected by your default rule.

### Remove a rule as a default rule

1. Go to **Automation** on the left side menu. Here, you can [**create new automation rules**](https://portal.debricked.com/automation-46/how-do-i-create-an-automation-rule-146), as well as [**edit**](https://portal.debricked.com/automation-46/how-do-i-edit-an-automation-rule-147) the existing rules.&#x20;
2. Click **Default rule.**
3. On the confirmation modal, click **Go ahead**. From now on, newly integrated repositories will no longer be affected by your default rule.

### Disable default automation rules using API

&#x20;You can disable these rules through our API to create your own custom policy.

The default rules can be accessed through the endpoint:

*api/1.0/open/admin/user/default-rules-enabled*

You can check the current status of your default rules:

```
curl -X 'GET' \  'https://debricked.com/api/1.0/open/admin/user/default-rules-enabled' \  -H 'accept: */*' \  -H 'Authorization: Bearer <token>'
```

The response will show you “true” if the default rules are enabled and “false” if they are disabled, e.g.:

```
{    "defaultRulesEnabled": true}
```

You can change the current status using “*enabled”:true* and *“enabled”:false*. Here’s an example of how to disable it:

```
curl -X 'PATCH' \  'https://debricked.com/api/1.0/open/admin/user/default-rules-enabled' \  -H 'accept: */*' \  -H 'Authorization: Bearer <token>' \  -H 'Content-Type: application/json' \  -d '{  "enabled": false}'
```

Once you disable the default rules using the API, the automation rules will not trigger when a new repository is added to your account. Remember to set up your own rules to optimize your use of OpenText Core SCA tool.
