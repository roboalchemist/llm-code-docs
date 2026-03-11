# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/appendix/system-behaviour-for-determining-assignee-owner-and-queue-for-work-items.md

# System behaviour for Determining Assignee, Owner & Queue for Work Items

As part of managing Tickets, Cases & Actions in your workflows in Enate, the system will regularly evaluate who the work is assigned to, who is set as the Owner, and which Queue the work item is linked to. There are detailed sets of rules which are followed, in order, when determining this.&#x20;

Before looking at these detailed sets of rules, it’s important to understand the higher-level pattern of how such work item allocations are evaluated, and indeed when. The way this works is as follows:

1. First we [determine WHEN such re-evaluations occur](#determining-when-re-evaluations-occur) – essentially this happens when anything changes in the 'Status’ card of a Work item.
2. When the system determines it needs to do such an evaluation, we initially use the work item’s status/situation to [determine which of the Assignee, Owner and Queue values need to be Set, and which need to be Cleared](#determining-if-assignee-owner-and-queue-values-need-to-be-set-or-cleared) completely.
3. [For those which require setting](#how-an-assignee-owner-and-queue-are-set):

   a. If a Queue is to be set, it's simple - just select the Queue referenced in the Allocation rule (there are only two types of Queue allocation rule to follow).

   b. For Assignee and Owner, there's more detail - we have to run through a series of rules, in order, for these - stopping when the rule is met and a valid\* target is selected.

\*[Validity check](#validity-checks) - As part of the Assignee / Owner allocation rule check, we have to determine if the target is **valid** (there are a number of validity check rules which it must pass). If not, we continue through the rules in part 3 until a valid target is found.

Now that the higher-level pattern at play has been described, we can go look at each set of rules which are run through for sections 1-3 above, and for the target validity checks.

## **Determining WHEN re-evaluations occur**

The system will re-evaluate the Assigned User, Owner and Queue whenever the information in the Status card changes, specifically:

* the Status changes
* the Wait Type changes
* the Scheduled Follow Up On date changes
* the Wait for More Information Until date changes
* the Waiting For option changes (for Cases only)
* the Ticket Context changes
* the Ticket Category changes
* the In Peer Review status changes
* New Information is received on the work item
* A Case encounters a Problem

## **Determining if Assignee, Owner and Queue values need to be set or cleared**

When the system determines it needs to do such an evaluation, we initially use the work item’s STATE to determine which of the Assignee, Owner and Queue values need to be Set, and which need to be Cleared completely. You can see this information in the table below:

| **Work Item Status/Situation**               | **Assignee** | **Owner**   | **Queue**   |
| -------------------------------------------- | ------------ | ----------- | ----------- |
| Closed                                       | Clear value  | Clear value | Clear value |
| Draft                                        | Set a value  | Clear value | Clear value |
| New Information Received                     | Set a value  | Clear value | Set a value |
| Needs Attention (only relevant to a Case)    | Set a value  | Clear value | Set a value |
| To Do or In Progress for an Action or Ticket | Set a value  | Clear value | Set a value |
| To Do or In Progress for a Case              | Clear value  | Set a value | Clear value |
| Resolved or Waiting                          | Clear value  | Set a value | Clear value |

&#x20;

## **How an Assignee, Owner and Queue are set**

* **Queues** - If a Queue is to be set, it's simple – the configured [Queue Allocation Method](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours#setting-a-queue-method) is run.
* **Assignee and Owner** - If an Assignee or Owner is to be set, there's more detail. We have to run through a series of rules, in order, stopping when the rule is met and a [valid target](#validity-checks) is selected.

Before the list of rules is run, there is one higher check: if an Assignee/Owner is currently set, **don't change the Assignee/Owner unless the Ticket Category has changed**.

Otherwise, run the following rules, in order, stopping when you a valid target is identified:

1. If the ‘Keep with me' option has been set on a work item, the Assignee/Owner is set as the user who has selected ‘Keep with me’. If not or the resulting user is not valid, then
2. If the Owner user is not blank, then set Assignee to that value also. If not or the resulting user is not valid, then
3. If the work item is a Ticket and the Ticket Category has changed and either the Wait Type has changed or the status is Resolved then the Assignee/Owner is set as the user currently updating the Ticket. If not then
4. If the work item is not a Ticket OR it is a Ticket (where the Ticket Category hasn't changed AND we have more than 2 status history rows - i.e. it is not in its first non-draft state), then:
   1. Set Assignee and Owner to the last user/robot to update work item. If none or the resulting user is not valid, then
   2. Set Assignee/Owner as (any) previously assigned to user/robot in descending order of when it was assigned to them. If none or the resulting user is not valid, then    &#x20;
   3. If Action started by Workflow (i.e. not manual ad-hoc), then set the Assignee/Owner as the last user/robot to work on the same previously completed Action in the Case (or Peer Review the Action if in peer review). If none or the resulting user is not valid, then
5. Run the [Allocation Rule](https://docs.enate.net/enate-help/builder/builder-2021.1/shared-standardised-settings-flavours/allocation-flavours) for this work item:       &#x20;
   1. If the primary push allocation is configured to a specific user, set Assignee/Owner to that user. If none or the resulting user is not valid, then
   2. If the secondary push allocation is configured to a specific user, set Assignee/Owner to that user. If none or the resulting user is not valid, then
   3. If Primary push allocation configured to Position, from the users that occupy this position set the Assignee/Owner as the user with the fewest work items in their inbox. If none or the resulting user is not valid, then
   4. If Secondary push allocation configured to Position from the users that occupy this position set the Assignee/Owner as the user with the fewest work items in their inbox. If none or the resulting user is not valid, then
6. If the work item is a Case, set Assignee/Owner as the user/robot that started that Case.&#x20;

## **Validity Checks**

As part of the Assignee / Owner allocation rule check, we have to determine if the target is valid. To be valid, there are a number of validity check rules which it must pass. If not, we continue through the rules of setting an Assignee/Owner until a valid target is found. The validity checks that are run through are as follows:

* If the User/Robot is not allowed to work on work items of this type (i.e. Live/Testing) then block    &#x20;
* If the User/Robot is retired then block&#x20;
* If the User does not have permission then block (no permission check for Robots)         &#x20;
* If the Robot is suspended then block   &#x20;
* If the Robot has performed Get More Work more than 3 times for this work item then block
* If the user selected is a Robot and the work item is an Action that is in the Peer Review stage then block (Robots cannot perform Peer Reviews)           &#x20;
* If the user selected is a Robot and the work item is an Action and no Robot Farm is configured for the Action then block&#x20;
* If the user selected is a Robot and the work item is an Action and the Robot is not a member of the Robot Farm configured for the Action then block
* If the user selected is a Robot and the work item is a Case then block (Robots cannot be assigned Cases)
* If the work item is a manual with Peer Review Action that is on the Peer Review stage and the User performed 1 or more updates while it was on the Doing stage then block (users can’t peer review their own work)           &#x20;
* If the work item is a manual with Peer Review Action that is on the Doing stage and the User performed 1 or more updates while it was on the Peer Review stage then block (users can’t be asked to do work if they have previously peer reviewed it)
