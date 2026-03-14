# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/dealing-with-incoming-out-of-office-emails.md

# Dealing with Incoming Out of Office Emails

## How does Enate deal with Out of Office emails?

Enate deals with incoming 'Out of Office' emails in two ways:

1. If the 'Out of Office' email is generated in response to receiving an email written by a user in Enate, Enate will append the 'Out of Office' email to the work item and mark the work item with ‘new information received’. See below for further specifics.
2. If the ‘Out of Office’ email is sent in response to an auto-generated email from Enate (e.g. acknowledgement of Ticket creation), the 'Out of Office' email will NOT be appended to the work item and the work item will not be marked with ‘new information received’ - it will effectively be ignored.

Expanding on the logic for situation 1 above where an 'Out of Office' email is generated in response to receiving an email written by a user in Enate...

## **Incoming Out of Office Emails matched to an existing running work item**

If the incoming 'Out of Office' email is matched to an existing Ticket, Case or Action that is in a state of DRAFT, TO DO or IN PROGRESS, the system will:

* append the email to the work item
* mark the work item with ‘new information received’

Note: This logic above applies to all auto-generated incoming emails that are matched to an existing work item in a state of DRAFT, TO DO or IN PROGRESS (i.e. incoming Out of Office emails are treated in exactly the same was as other incoming auto-generated emails in these states). Please see this [section ](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic#auto-generated-emails-detection-logic)for more information on how the system *detects* auto-generated emails.

## **Incoming Out of Office Emails matched to a work item in a state of Waiting**

If the incoming 'Out of Office' email is matched to an existing work item that is in a state of WAITING, the system will:

* append the email to the work item
* mark the work item with ‘new information received’

In additio&#x6E;**,** if the Wait type is 'Waiting for more information', the system will:

* change the state of the work item from WAITING to TO DO
* As a result of the change in state to TO DO, a Queue and assignee will be set to the work item and it will move back to the responsible agent’s Enate Inbox, marked with ‘new information received’
* If the work item is an Action and both the Action and its parent Case are in a state of WAITING with a wait type of Waiting for more information, the state of the parent Case will change to IN PROGRESS

The same rules apply to other auto-generated incoming emails that are matched to an existing work item in a state of Waiting or Waiting for more Information (i.e. incoming Out of Office emails are treated in exactly the same was as other incoming auto-generated emails in this state). Please see this [section ](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic#auto-generated-emails-detection-logic)for more information on how the system detects auto-generated emails.

## **Incoming Out of Office Emails matched to a Resolved Work Item (Case & Ticket)**

If the incoming 'Out of Office' email is matched to an existing work item that is in a state of RESOLVED (note that only Cases and Tickets can be in a state of RESOLVED), the system will:

* Append the email to the work item
* Reopen the work item and set it back to TO DO
* As a result of the change in state to TO DO, a Queue and assignee will be set to the work item and it will move back to the responsible agent’s Enate Inbox, marked with ‘new information received’.

The same rules apply to other auto-generated incoming emails that are matched to an existing work item in a state of RESOLVED (i.e. incoming Out of Office emails are treated in exactly the same was as other incoming auto-generated emails in this state). Please see this [section ](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic#auto-generated-emails-detection-logic)for more information on how the system detects auto-generated emails.

## **Incoming Out of Office Emails matched to a Closed Work Item**

If the incoming 'Out of Office' email is matched to an existing work item that is in a state of CLOSED, the system may take various courses of action depending upon the type of work item:

* The system will firstly ‘go up’ the work item chain to look for a parent work item e.g.
  * if the email is matched to an Action that is CLOSED, the system will see if the Action’s parent Case is still open.
  * if the email is matched to a Case that is CLOSED, the system will see if the Case has a parent Case or Ticket that is still open.
  * if the email is matched to a Ticket that is CLOSED, the system will see if the Ticket has a parent Ticket that is still open.
* If the system *does* find a parent work item that is still open, the system will then apply the rest of the email processing logic to the parent work item (i.e. all of the logic in the above sections on running work items).
* If the system *cannot* find a parent work item that is still open, the incoming email will NOT be appended to the already closed work item. It will instead create a new work item following the [rules below](#if-unable-to-match-an-incoming-email-to-an-existing-work-item) for what happens when the system is unable to match an email to an existing work item.

The same rules apply to other auto-generated incoming emails that are matched to an existing work item in a state of CLOSED (i.e. incoming Out of Office emails are treated in exactly the same was as other incoming auto-generated emails in this state). Please see this [section ](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic#auto-generated-emails-detection-logic)for more information on how the system detects auto-generated emails.

## **If unable to match an incoming out of office email to an existing work item**

If no information can be identified to link the incoming 'Out of Office' email to a currently running work item, the system will generate a brand new work item (Ticket or Case) based on the email’s configured routing rules.&#x20;

If a Ticket has been created, even if the email route settings specified in Builder have the ‘send response’ option set to ‘on’, a confirmation email will NOT be automatically sent back out to the to the email address that the 'Out of Office' email originated from as the 'Disable Automated Emails' option will be automatically switched on.
