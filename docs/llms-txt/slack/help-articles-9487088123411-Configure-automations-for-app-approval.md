# Configure automations for app approval

By default, members can install apps without approval from a Workspace Owner, but you can choose to [approve and restrict](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace) apps on a case by case basis, or you can automate the process by configuring rules so that apps that meet your assigned criteria are automatically approved.

**Note**: We recommend developing and testing these features in a testing environment before using the functionality in production.

## Before getting started

- Review the [Guide to automation rules for app approval](https://slack.com/help/articles/9978438318227-Guide-to-automation-rules-for-app-approval) to familiarize yourself with the outcomes of each rule.
- [Rate and review scopes](#h_01GHY35SHQ1Q8D2G0WGD1GEEDA) and their risk levels to use them in a rule.

## Create a rule

You can create rules based on a chain of comparisons for each app request to be checked against. Any app that meets the conditions of your rule will be automatically approved or restricted based on the resolution you specify.

### Free, Pro, and Business+ plans

1. From your desktop, click **Admin** in the sidebar.
2. Select **Apps and workflows** from the menu to open the Slack Marketplace.
3. Click **Requests** in the left sidebar, then select the **Automation rules** tab. If you don't see **Requests**, make sure [app approval](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace) is enabled for your workspace.
4. At the top of the list, select **Create a rule**, then give your rule a name and add a description.
5. Choose if **all** conditions need to match, or **any** single condition.
6. Choose what condition you’d like the rule to look for from the drop-down menu. You can also choose a comparison from the following drop-down menu, if you need to.
7. To add additional conditions, click **Add new condition.**
8. Choose to **Approve, Deny, Dismiss** or **Restrict** an app that meets the conditions.
9. If you'd like, select who to notify about the resolution and include a message to send the requestor.
10. Click **Save**.

### Enterprise plans

1. From your desktop, click your **organization name** in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **Integrations**, then click **Requests** and select the **Automation Rules** tab.
4. At the top of the list, select **Create a rule**, then give your rule a name and add a description.
5. Choose if **all** conditions need to match, or **any** single condition.
6. Choose what condition you’d like the rule to look for from the drop-down menu. You can also choose a comparison from the following drop-down menu, if you need to.
7. To add additional conditions, click **Add new condition.**
8. Choose to **Approve, Deny, Dismiss** or **Restrict** an app that meets the conditions.
9. If you'd like, select who to notify about the resolution and include a message to send the requestor.
10. Click **Save**.

**Tip**: Rules you create will not be enabled until you [activate them](#h_01GDBJRP4FM0PDTJJKME94DRZ4).

## Manage rules

### Free, Pro, and Business+ plans

1. From your desktop, click **Admin** in the sidebar.
2. Select **Apps and workflows** from the menu to open the Slack Marketplace.
3. Click **Requests** in the left sidebar.
4. Click **Automation rules** to view a list of your existing rules, then click the **three dots icon** next to the rule you’d like to **Activate**, **Pause**, **Edit**, or **Remove**.

### Enterprise plans

1. From your desktop, click your **organization name** in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **Integrations**, then click **Requests**.
4. Click **Automation Rules** to view a list of your existing rules, then click the **three dots icon** next to the rule you’d like to **Activate**, **Pause**, **Edit**, or **Remove**.

**Note**: Removing a rule will not undo previous requests that were resolved by this rule. Removing a rule cannot be undone, and you'll need to recreate it from scratch. Proceed with caution!

## Reorder rules

The order of the rules in the list is relevant to your automation, since a requested app will be resolved at the first matching rule. If you have multiple rules, you can reorder the list if you determine a rule should take priority over another.

### Free, Pro, and Business+ plans

1. From your desktop, click **Admin** in the sidebar.
2. Select **Apps and workflows** from the menu to open the Slack Marketplace.
3. Click **Requests** in the left sidebar.
4. Click **Automation rules** to view a list of your existing rules, then click **Reorder list**.
5. Using the available actions, choose if you’d like to move the rule up, down, to the top, or bottom of the automation rules list, then click **Save**.

### Enterprise plans

1. From your desktop, click your **organization name** in the sidebar.
2. Hover over **Tools & settings**, then click **Organization settings**.
3. From the left sidebar, click **Integrations**, then click **Requests**.
4. Click **Automation Rules** to view a list of your existing rules, then click **Reorder rules**.
5. Using the available actions, choose if you’d like to move the rule up, down, to the top, or bottom of the automation rules list, then click **Save**.

**Note**: To apply the same rating to multiple scopes, select all the desired scopes then click the **Rate as high risk**, **Rate as medium risk**, or **Rate as low risk** action at the top of the scope list.

**Who can use this feature?**

- **Workspace Owners/Admins, Org Owners**/**Admins**, and **members** with [permission to manage apps](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#choose-how-app-requests-work)
- Available on [**all plans**](https://slack.com/pricing)

**Awesome!**

Thanks so much for your feedback!

If you’d like a member of our support team to respond to you, please send a note to [feedback@slack.com](mailto:feedback@slack.com).

**Got it!**

If you’d like a member of our support team to respond to you, please send a note to [feedback@slack.com](mailto:feedback@slack.com).

**Was this article helpful?**

- Yes, thanks!
- Not really

**Sorry about that! What did you find most unhelpful?**
- This article didn’t answer my questions or solve my problem
- I found this article confusing or difficult to read
- I don’t like how the feature works
- Other

**Tip**: To apply the same rating to multiple scopes, select all the desired scopes then click the **Rate as high risk**, **Rate as medium risk**, or **Rate as low risk** action at the top of the scope list.

**Submit article feedback**

If you’d like a member of our support team to respond to you, please send a note to [feedback@slack.com](mailto:feedback@slack.com).