# Source: https://docs.firehydrant.com/docs/signals-escalation-policies.md

# Escalation Policies

## Introduction to Escalation Policies

Escalation policies are a short-hand way for your team to get the right person involved with a potential incident. Escalation policies define how notifications from an Alert are sent to various team members, either as part of an on-call schedule or as an individual. Let’s dive into how escalation policies work.

<Image alt="Escalation policy example" align="center" width="400px" src="https://files.readme.io/d98d09c-escalation-policy.png">
  Escalation policy example
</Image>

* **Notification Steps -** Every escalation policy has a set of steps that outlines who should be notified for an Alert and how long to wait between those steps. Most users will choose [On-Call Schedules](https://docs.firehydrant.com/docs/signals-on-call-schedules) as targets for EP steps, but FireHydrant also allows directly notifying specific users and Slack channels.
  * If a given step targets an on-call schedule with no active shift or user on-call, FireHydrant will immediately escalate to the next step, even if a delay is configured on the next step.
* **Repeats & Hand-Offs -** For any escalation policy, you can define a repetition that makes sense for the kinds of Alerts you are sending to the policy. After the repetitions are completed (if there are any), you can also define a hand-off, which will send the Alert to another escalation policy for the team, or you can send the Alert to another Team. When sending an alert to another team, the default escalation policy for that team will be used.

> 📘 Note:
>
> An escalation policy cannot hand off to itself. You should configure Repeats instead.

**Default Escalation Policies -** Each team can set one Escalation policy as its default policy, allowing any other team or user to send an Alert to that team directly.

## Creating Escalation Policies

1. Navigate to the team where you want to create an escalation policy (Teams > Team Name) and click on the Escalations Policy tab.
2. Click “Add Escalation Policy” in the top right corner.
3. Add a Name and Description for your escalation policy.
4. If you’d like this escalation policy used whenever someone pages or sends an Alert to your team, select “Use as default team escalation policy.”
5. In the Notifications section, you must add a first step that will run automatically when an escalation policy is invoked. Then, you can add any additional steps to your policy. For each step, you can add:
   1. **Delay -** Except for the first step, which fires immediately, you can define a delay for each notification. This will delay the notification *after* the previous step has been completed. This includes any delays that the user has defined in their notification preferences.
   2. **Notify -** You must select a person or on-call schedule to notify each step. These notification targets will be limited to the team creating the escalation policy.
6. If you want to set a repetition or hand-off for your escalation policy,
   1. First, set a delay for the post-notification steps. Importantly, this will set a delay for both the repetitions and the handoff, giving the notified user in the final step some time to respond to the alert before either repeating the Escalation Policy steps or handing the alert off to another escalation policy or team.
   2. Then, if you want the escalation policy to repeat, select the number of times that you want the policy to repeat.
   3. If you’d like the alert to be handed off if no one has responded, you can specify a Hand-off. This allows you to send the alert to another escalation policy or team. The alert will only be handed off once the escalation policy and any repetitions have been completed.
7. Once you’ve configured the escalation policy, click “Save escalation policy” to set it in place.

## Using Escalation Policies

### ⚡️Automatic Alerts through Alert Rules

You can send Alerts to an escalation policy by creating an Alert Rule and selecting an escalation policy as the notification target. Any event that matches that rule will create an Alert sent to that escalation policy.

<Image alt="Automatically create alerts from signals with rules" align="center" width="800px" src="https://files.readme.io/3515cf4-alert-rule.jpg">
  Automatically create alerts from events with rules
</Image>

### 🙋 Ad-Hoc Alert through `/fh page` or the Web App

Additionally, any user in your organization can send a page (i.e., create a one-off Alert) in Slack or in the web application. Those alerts can be sent to your Escalation policy. If they are trying to page your team or a service your team owns, the default Escalation Policy for your team will be used.

<Image alt="Send an alert through Signals in Slack" align="center" width="400px" src="https://files.readme.io/157d6a6-sending-signals-page.png">
  Send an alert through Signals in Slack
</Image>

### Paging an entire team in a step

In cases where you need to page every member of a team in an instant, you can search for the team you'd like to page, and select the option under "Entire Team"

<Image align="center" className="border" border={true} src="https://files.readme.io/fa9c01db1b436a94afb6ae58b0031b81ff9403257dc1283cf7d0291684ef9e73-CleanShot_2024-09-26_at_15.11.132x.png" />

In the example above, every member of the Core Services team (all three of them) will receive an alert from Signals at the same time. If you add or remove members from the team in FireHydrant, we'll automatically update your escalation policy to only the most up-to-date membership.

> 🚧 Paging an entire team is exactly what it sounds like. If you have a team of 50 people, we will instantly page 50 people using their notification preferences. We recommend using this only in break-glass situations or later staged steps in escalation policies.

## Permissions

Users with <Glossary>Member</Glossary> permissions can configure and update any escalation policies within any teams they are members of. Users with <Glossary>Owner</Glossary> permission can edit the same for all teams regardless of their membership or lack thereof.

For more information, visit [Role-Based Access Controls](https://docs.firehydrant.com/docs/role-based-access-controls).