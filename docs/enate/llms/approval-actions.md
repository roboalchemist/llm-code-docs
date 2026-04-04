# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/approval-actions.md

# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/approval-actions.md

# Approval Actions

## What are Approval Actions? How do they work?

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NDEwNw==>" %}

Often within the Case flows of business processes which are built in Enate there are points where external people (i.e. people working **outside** Enate - this could be business managers within your company or the relevant client company) need to sign off on activities before the process can continue. Payroll processes are good examples of such processes, where client management need to sign off on payroll reports before the process can be allowed to continue.

Enate's Approval Action is built to specifically support these approval request scenarios in a more integrated way - to ensure that this 'approval cycle' is tightly managed and visible within the flow of activities in Enate.&#x20;

## How Approval Actions work at Runtime

Approval requests get sent out to agents working externally from Enate to approve or decline.

There are a few different types of approval that affect how the decision is made:

* In a multilevel scenario, the request email is sent to each new level upon successful approval from previous, up to a maximum of 3 levels. If any person declines, the approval is declined.&#x20;
* In a parallel any scenario, the request email is sent to all approvers and the first decision is taken.&#x20;
* In a parallel all scenario, the request email is sent to all approvers and ALL must approve for the request to be approved. If any decline, the approval is declined.

If the request gets approved by all necessary parties, the approval Action gets successfully resolved and closed automatically, so no Work Manager Agent will need to pick it up, although the closed Action can always be viewed by manually clicking on it.

## Exceptions - handled by Agent in Work Manager

There are, however, a couple of scenarios where a Work Manager agent might need to pick up and carry out any required activities to further process an approval Action:

* The approval has been declined&#x20;
* No approvers (or insufficient approvers) have been determined automatically

### Approval Request Declined

In the scenario where an approval request has been **declined**, the Action will move into a state of 'To Do' and so will ultimately need to be dealt with by a Work Manager Agent. They should review the approval decline reason provided by the approver and decide how to proceed. They can either:

1. **Update as needed and Resend the request by setting the Action to 'Wait'.** This will auto-send out the approval request email again\*\* and place the Action in a state of 'Wait for More Information' - since we're waiting for external information (an approval response) to be registered back into the system before activity can proceed.&#x20;
2. **Mark the Action as Unable to complete.** This will alert the Case owner who then needs to decide how to proceed - perhaps by reworking the Case or closing the Case entirely.
3. **Mark the Action as Resolved** which will manually mark the request as approved. The Case with then progress to the next Action.

{% hint style="info" %}
\*\*Note: Approval request email sending will start again from the beginning, i.e. all requesters will be mailed again. If they click on any previously sent emails, they will be met with a message telling them that THAT specific approval request is no longer valid, as the details of what is being requested may have changed). &#x20;
{% endhint %}

### **Insufficient Approvers**

In the scenario where an agent needs to add in approvers because one or more required approvers is blank (or make changes which result in the approval requests needing to be sent out again), the Agent will pick up the Approval Action in a state of To Do. Once they have finished making any adjustments and / or filling in missing Approver names, the must **then place the Action in a state of Wait**. Once they do this will auto-send the approval request email and then move the Action to a state of 'Wait for more information' as it is waiting for external info (approval) before proceeding.

{% hint style="info" %}
Note: While an Approval Action is state of 'To Do', or 'In Progress', external parties who were mailed out approval requests will NOT be able to approve or decline. Instead the will be met with a message informing them that the item in question is currently being processed. Work Manager Agents MUST move the Action back to a state of 'Wait for more information' if they wish the approval activity to recommence.&#x20;
{% endhint %}

### If Approval Requests Time out..

Another potential scenario is that the approval Action might auto-close because it has timed out as no/insufficient responses were received in time. In this case, the Action will automatically be set to Resolved, and the Case will continue. No Work Manager agent will need to pick up an Action in this scenario, although the closed Action can always be viewed by manually clicking on it.
