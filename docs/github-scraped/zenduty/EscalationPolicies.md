---
id: EscalationPolicies
title: Escalation Policies
---
Each [service](Services.md) in a Zenduty [team](Teams.md) is governed by an Escalation Policy. This Escalation policy combines various [schedules](Schedules.md) and tasks to be performed for the [users](Users.md) in the team as a set of rules. When an incident is triggered in the service, alerts are triggered according to the Escalation Policy specified.

To view Escalation Policies of a Team, simply click the "Manage" button corresponding to the Team. On the secondary header, select the tab "Escalation Policies"

![](/img/ep_1.png)

A list of all the Escalation Policies in a team will be visible to you.

## Adding a New Escalation Policy

1. To create a new escalation policy, simply click the "Create Escalation Policy" button.

2. Give it a name and summary

3. To create Escalation Rules, keep the following in mind:
 * You can pick who to notify when an incident is created. It can be specific persons, or the person on call from your team's schedule or a combinations of the same.
 
 * You can pick when else someone should be notified ex. the Team Lead to be notified 15 minutes later. This is shown below:

 ![](/img/ep_2.png)

 * How each person is notified depends on the [notification rules](Users.md) they or their team managers/admins have set up.

4. To put your escalation chain in a loop, change the **Repeat Escalation Cycle** value and add the number of time you'd like to run the escalation chain in a loop.

5. By default, Zenduty moves to the next escalation rule if the current rule(which only has a single on-call schedule) has no user on-call. To stop Zenduty from automatically moving to the next rule, unselect/deactivate the **Move to next rule if no user found in current rule** slider option.

## Editing an Escalation Policy

Simply click on the "View" button next to the policy you want to edit. Edit the form that shows up, and Save

![](/img/ep_3.png)

## Deleting an Escalation Policy

To delete an Escalation Policy, click on the "Remove" button next to the corresponding policy, and confirm.

![](/img/ep_4.png)
