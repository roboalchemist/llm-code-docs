# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/automation-and-workflows/alerts-and-rules/alerting-and-automation-for-bug-reporting.md

# Alerting & Automation for Bug Reporting

coThe testing process can be a lengthy manual process where the tester/user has to do several actions to submit thorough feedback including:

* Include all relevant screenshots.
* Pull all logs from the device
* Explain how to reproduce the bug
* Manually submit a ticket to the tracking system

Luciq helps you automate this entire process, as well as extra automation capabilities that you can utilize to save time and eliminate a handful of manual tasks.

### Set up your integrations

Luciq natively integrates with plenty of workflow management and messaging tools (Jira, Slack, MS Teams, PagerDuty, ServiceNow, and more), you can easily create an integration from the dashboard by navigating to the setting from the left menu

<figure><img src="https://files.readme.io/0281e99640ff02701316224b5859fe1c23d993d638d21d89695c14fa4ef297d2-product-guides-br-workflow-automation-1.png" alt="2876"><figcaption><p>Settings Menu - Bottom left of the dashboard</p></figcaption></figure>

On this menu you will see a list of all configured integrations, get started by integrating with your current workflow tools. If your tool is not listed here, you can use “Zapier” or “Webhooks” integrations if that tool is compatible with any of those integrations.\
Read more about our integrations [here](https://docs.luciq.ai/docs/integrations)

<figure><img src="https://files.readme.io/b9703d0-Bug_Reporting_Workflow_2.png" alt="862"><figcaption><p>Integrations hub</p></figcaption></figure>

After creating your integrations, you shall now start creating rules and alerts, In this section we will cover the possible workflow automation options for bug reporting.

**Workflow Automation Examples**:

* Keep your users updated with the status of their reports.
* Create alerts to get your team notified about any updates.
* Assign issues to the right team members
* Triage and manage issues from your preferred system, no need to manage tickets on multiple tools

### Create your rules

To get started with bug reporting workflow automation, hover the the left navigation menu and click on “Alerts & Rules”

<figure><img src="https://files.readme.io/c5d5cb102c737d0fda99b97bd9a0d2602a7be21b4e8aa797a9a499d37794a515-product-guides-br-workflow-automation-3.png" alt="2874"><figcaption><p>Alerts and Rules page from the Luciq menu</p></figcaption></figure>

You can view a list of all created rules, you can also use the filters to view only rules for bugs, crashes or performance metrics, click on “Create” to get started.

<figure><img src="https://files.readme.io/236c5dea069b0fca154434f9c2d563c023aadabf27b33fde4bf0aa8f12a978d9-product-guides-br-workflow-automation-4.png" alt="2874"><figcaption><p>Use this filter to view previously created rules</p></figcaption></figure>

### Bug Reporting Alert

Select “Bugs” from the dropdown menu under the “For”

<figure><img src="https://files.readme.io/63dce70ac9024ab1edefe7364c15283084c6535fc6561c9f1f4055a448869072-product-guides-br-workflow-automation-5.png" alt="2874"><figcaption><p>Choose a type - "For" - "Bugs"</p></figcaption></figure>

### Triggers

Then you need to select a trigger, below is a list of all available triggers:

* ***Bug is reported***: Get notified or apply several actions when a bug is reported, like forwarding to your ticketing tools, replying to the user and more.
* ***Bug is forwarded***: Get notified or apply other actions whenever a bug is forwarded to any integration
* ***Status changes***: Stay updated whenever the status of a bug report is changed
* ***Assignee changes***: Stay updated whenever the assignee for a bug report is changed
* ***Priority changes***: Stay updated whenever the priority of a bug report is changed
* ***Tag is added***: Apply several actions whenever a tag is added to the bug report. This can be used as a quick and easy way to automate any workflow simply by adding a tag to the bug report

<figure><img src="https://files.readme.io/9affe4b94f075aa246db12b02b1b49e205f1ac6385dc1e6451d269753d64710b-product-guides-br-workflow-automation-6.png" alt="2874"><figcaption><p>Choose a trigger</p></figcaption></figure>

### Conditions

After selecting the trigger, you can select a set of conditions that need to be met for the rule to be triggered.

{% hint style="warning" %}

#### Make sure you set the condition

If you do not select any conditions, the rule will be applied to any reported bug.
{% endhint %}

**Below is a list of all available conditions**:

* ***Title***: Specify if the bug description should include any keywords for the rule to be triggered
* ***Reporter’s email***: Can be used if you want to focus on reports coming from internal testers
* ***App version***
* ***Current View***: The screen used right before reporting the bug (screen affected by the bug)
* ***Categories***: These can be the main categories (Report a bug, Suggest an improvement, Ask a question) or one of the custom report categories you use
* ***Tags***: Tags can be added manually to a bug report, or [automatically added through code](https://docs.luciq.ai/reference/add-tags)
* ***Device***: Device type/name used to report the bug
* ***Status***: The status of the bug report on the dashboard
* ***Priority***: The priority of the bug report on the dashboard
* ***Assignee***: The team member assigned to the bug report on the dashboard
* ***OS***: OS type/name used to report the bug
* ***Location (City/Country)***: Specify the location of the reporter as a condition
* ***User attributes***: Specify conditions for the user attributes (e.g login status, paying status, user ID and more). Know how to [add user attributes here](https://docs.luciq.ai/reference/user-attributes)

You can add as many conditions as you see fit, you can also choose to “AND” or “OR” the selected conditions.

<figure><img src="https://files.readme.io/8b518b7b746709d6be65a483fbd1c0f2b228807f082cc74cb9518de7b1d5f465-product-guides-br-workflow-automation-7.png" alt="2874"><figcaption><p>Choose one of the conditions</p></figcaption></figure>

### Alerting channels

The last thing you need to do is specify the actions you want to automate using this rule. There are various actions available:

* ***Forward it to***: Forward the bug report to any of the setup integrations (Slack, Jira, Zendesk, Github and more). See more info about available integrations and how to set up here
* ***Reply to user***: Send an in-app message to the reporter to update them on the status of the report, ask them further questions and more. This is a 2-way conversation
* ***Assign to member***: Automatically assign bugs to the right team member
* ***Change its status to***: Change the status of the report to one of: New, In-progress & Closed. This can be used to close reports coming from very old app versions
* ***Change its priority to***: Change the priority of the report (Trivial, Minor, Major, Blocker)
* ***Tag it with***: Automatically add tags to a report
* ***Delete it***: Automatically delete a report, can be used to delete reports coming from very old app versions
* ***Send email to***: Send an email to a dashboard member(s)

You can add as many actions as you see fit, helping you eliminate several manual tasks using a single rule.

The below rule example is going to evaluate each bug report against the specified conditions, if they’re met then the bug will be forwarded to the Jira project, change the report status to in-progress and send an automated reply to the user.

<figure><img src="https://files.readme.io/4010aa0717884b9212ff38b95274d21612cbcbba645d1ec724a8627eacd1c54c-product-guides-br-workflow-automation-8.png" alt="2874"><figcaption><p>Choose one of the actions, for example: forward to the relevant Jira project</p></figcaption></figure>

Finally you need to provide a title to the rule and click “Save”, you can also assign this rule to a team for ownership and to easily find rules related to your team. [You can create teams on the dashboard here](https://dashboard.luciq.ai/company/teams).

<figure><img src="https://files.readme.io/a70dbb7ff74e659b8c83d73816bc4868a931d185d1bba11a15adf55caf551192-product-guides-br-workflow-automation-9.png" alt="2876"><figcaption><p>Choose the team that owns this rule</p></figcaption></figure>

Now let’s discover different scenarios for workflow automations, and how you can use the rules to achieve this:

***Scenario A***:\
You have an internal testing program and you’re using Luciq to streamline the feedback process, and you want to forward all bugs reported by the company members to the designated Jira project, receive Slack notifications and add the appropriate tag(s) to the report

<figure><img src="https://files.readme.io/179f7eedb8e6936024ab6e5a7192908374799c5b521ea8d247ed3ab60eef1842-image.png" alt=""><figcaption></figcaption></figure>

***Scenario B***:

You want to be connected to your users as much as possible, you want to send an auto reply to them once they report an issue, and also keep them posted with any updates that happen on the report.

The below rule will send an auto reply to the reporter

<figure><img src="https://files.readme.io/b69d3171de419bd438dfe167a55f41015dbc38eb766dd885abbac935c92ed975-image.png" alt=""><figcaption></figcaption></figure>

You can also leverage the report tags, which can be used as a quick way to apply several actions, like updating the user once any action is taken on the bug report.

Below are a couple of examples on how to utilize tags, the relevant actions will be applied once you add the appropriate tag to the bug report.\
The below two examples will send a different message to the user based on the added tag

<figure><img src="https://files.readme.io/7f32bb1b1f2413dd5c81d25014b8e691ab185320d50d84b47dfa5e9ec0df5c88-image.png" alt=""><figcaption></figcaption></figure>

If you need further assistance on setting up rules, please feel free to contact our [support team](mailto:contactus@luciq.ai).
