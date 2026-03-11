# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic.md

# Incoming Emails - Processing Logic

## Processing Logic

When new emails arrive into Enate, the system analyses the email to determine whether it’s a brand new request or related to an existing one, and then determines how to proceed. The system will try using the following matching methods **in this order**.

1. ['In Reply To' Logic](#id-1.-in-reply-to-logic)
2. [Plus Addressing](#id-2.-plus-addressing)
3. [Unique identifier in email body](#id-3.-unique-identifier-in-email-body)\
   \
   For older clients this additional method may kick in be used if the above approaches have failed to find a match.
4. [Work Item Reference in email subject or body](#id-4.-work-item-reference-in-email-subject-or-body)

#### **1.      ‘In Reply To’ Logic**

The system will first try to find a match using the following logic:

* If the 'InReplyTo' field of the incoming email aligns with the Message-ID of a prior email AND&#x20;
* if the AssociatedBecauseOf or AssociatedBecauseofPlus email addresses are still in the recipient fields (i.e. To or CC) of the incoming email

{% hint style="info" %}
Additional Note:&#x20;

* If your system is using Traditional/Mixed mode, we verify if the 'InReplyTo' field corresponds to the Message-ID of ANY previously received email, irrespective of being incoming or outgoing.
* If your system is running in Exclusive (i.e. Plus Addressing ONLY Mode), we verify if the 'InReplyTo' field corresponds to the Message-ID of previous INCOMING received emails only (not outgoing mails).
  {% endhint %}

#### **2.	Plus Addressing**

If no match is found using the above logic, the system will then see if Plus Addressing has been configured in your system. If plus addressing has been enabled, the system will try and find a match using plus addressing, i.e. using the Work Item reference number found directly in the email address, if there is one. See here for an explanation of [**Plus Addressing**](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic/plus-addressing-in-emails).

#### **3.	Unique identifier in email body**

If no match can be found using Plus Addressing, the system will then try and find a match based on if it can find a unique identifier in email message body. If the incoming email has been sent as a response to an email which was sent out from Enate, it will likely contain a unique identifier tag as part of the email body text.

#### **4.	\*Work item reference in email subject or body**

*Note: This option is only available for older clients who may previously have been using this approach in earlier product versions. This method is NOT available for any new setups going forward, and clients who have this option are encouraged to switch if OFF as an approach to use in the long term.*

If no match can be found using the other 3 methods - and then only if your system has been set up to allow matching based on work item reference in email subject or body - the system will try this final matching method.&#x20;

{% hint style="warning" %}
\*Caution: Existing clients who have this option available in General Settings are strongly encouraged to switch this option OFF, as it could lead to data breaches if incorrect or irrelevant work item references numbers are present in an incoming email subject or body. You can check in the relevant part of the [General Settings](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/general-settings#work-item-plus-addressing) section for how this option can switched off.
{% endhint %}

***

**If the system finds a match to a work item using one of the above matching methods, then, depending on the state that work item is in, it will behave as follows:**

## **Sending an Incoming Email to an existing running work item**

If the system finds a match to an existing Ticket, Case or Action that is in a state of DRAFT, TO DO or IN PROGRESS, the system will:

* append the email to the work item
* mark the work item with ‘new information received’

The same applies to auto-generated emails that are matched to an existing work item in a state of DRAFT, TO DO or IN PROGRESS. Please see the [section below](#auto-generated-emails-detection-logic) for more information on how the system detects auto-generated emails.

## **Sending an Incoming Email to a work item in a state of Waiting**

If an incoming email is matched to an existing work item that is in a state of WAITING, the system will:

* append the email to the work item
* mark the work item with ‘new information received’

In additio&#x6E;**,** if the Wait type is 'Waiting for more information, the system will:

* change the state of the work item from WAITING to TO DO
* As a result of the change in state to TO DO, a Queue and assignee will be set to the work item and it will move back to the responsible agent’s Enate Inbox, marked with ‘new information received’
* If the work item is an Action and both the Action and its parent Case are in a state of WAITING with a wait type of Waiting for more information, the state of the parent Case will change to IN PROGRESS

The same rules apply to auto-generated emails that are matched to an existing work item in a state of Waiting or Waiting for more Information. Please see the [section below](#auto-generated-emails-detection-logic) for more information on how the system detects auto-generated emails.

## **Sending an Incoming Email to a Resolved Work Item (Case & Ticket)**

If an incoming email is matched to an existing work item that is in a state of RESOLVED (note that only Cases and Tickets can be in a state of RESOLVED), the system will:

* Append the email to the work item
* Reopen the work item and set it back to TO DO
* As a result of the change in state to TO DO, a Queue and assignee will be set to the work item and it will move back to the responsible agent’s Enate Inbox, marked with ‘new information received’.

The same rules apply to auto-generated emails that are matched to an existing work item in a state of RESOLVED. Please see the [section below](#auto-generated-emails-detection-logic) for more information on how the system detects auto-generated emails.

## **Sending an Incoming Email to a Closed Work Item**

If an incoming email is matched to an existing work item that is in a state of CLOSED, the system may take various courses of action depending upon the type of work item:

* The system will firstly ‘go up’ the work item chain to look for a parent work item e.g.
  * if the email is matched to an Action that is CLOSED, the system will see if the Action’s parent Case is still open.
  * if the email is matched to a Case that is CLOSED, the system will see if the Case has a parent Case or Ticket that is still open.
  * if the email is matched to a Ticket that is CLOSED, the system will see if the Ticket has a parent Ticket that is still open.
* If the system *does* find a parent work item that is still open, the system will then apply the rest of the email processing logic to the parent work item (i.e. all of the logic in the above sections on running work items).
* If the system *cannot* find a parent work item that is still open, the incoming email will NOT be appended to the already closed work item. It will instead create a new work item following the [rules below](#if-unable-to-match-an-incoming-email-to-an-existing-work-item) for what happens when the system is unable to match an email to an existing work item, and copy all the information (comms, files, defects, contacts and custom data) from the existing closed work item to the new work item.
* If the email is sent to a closed child split ticket, the system creates a new work item for the email.

## **If unable to match an incoming email to an existing work item**

If no information can be identified to link the email to a currently running work item, the system will generate a brand new work item (Ticket or Case) based on the email’s configured routing rules. A confirmation email will be automatically sent back out to the requesting email address containing the reference number if the email route settings specified in Builder have ‘send response’ set to ‘on’.

## **Further specifics**

* **Split Ticket** – if an incoming email is matched to a split Ticket – either the original Ticket that was split or one of the child Tickets it was split into – the email will be appended to each of the CHILD Tickets. The system will then apply the rest of the email processing logic to each of the child Tickets independently.
* **Merged Ticket -** if an incoming email is matched to a merged Ticket – either one of the original Tickets that were merged or the ‘target’ Ticket that they were merged into – the email will be appended to the ‘target’ Ticket. The system will then apply the rest of the email processing logic to the ‘target’ Ticket.
* **Ticket converted into a Case –** if an incoming email is matched to a Ticket that was Resolved by being converted into a Case, the email will be appended to the Case. The system will then apply the rest of the email processing logic to the Case.

## **Auto-Generated Emails Detection Logic**

The system detects auto-generated emails by one-or more of the following:

* A « x-autoreply » header exists
* A « x-autorespond » header exists
* A « auto-submitted » header exists and the value is either « auto-generated » or « auto-replied »
* A « content-type » header exists and the value is either « multipart/report » or « delivery-status »
* The ReturnPath header exists and has a value of « <> » or « <<>> »

## Important Note - Incoming Emails from your Enate instance will be ignored

Before processing any emails Enate will check to see if it sent it. Every email has a unique identifier which should not change. Enate stores the unique identifiers of emails that it has sent and uses these to perform this check.

This Enate behaviour is to avoid duplicate processing of items which Enate may well have already processed before the outgoing email has been sent, for example (but not limited to) auto-appending of mails to linked work items via Plus Addressing logic.

## How does Enate decide which processes to start when it receives an Email?

When deciding which process to start, Enate looks at all the routes for the connector for the email address under consideration (NB\* *This means that if you spread routes across connectors, you’ll get odd behaviour*!).

Enate then looks at each route in the order you have defined, starting at the top (1) checking for the criteria you have added. If all the criteria match then the route is used, if any of the criteria don’t match, Enate will move onto the next route.

The last route is a catch all (fallback) route, however if the email has been sent to an alias, then the catch all route will not match and the email will be made available for processing in ‘Unprocessed View’.

If you have EnateAI Classification enabled on your system, it will override the above rules as it will automatically attempt to classify the Work Item. This may cause the Work Item classification to differ, from what it was classified originally.

## Emails received by BCC

If the email has been sent to Enate using Blind Carbon Copy (BCC) then by design Enate is not able to see which email address the email has been sent To (If Enate could see the address list it wouldn’t be ‘blind’). This causes all routes to fail to match.

To support this Enate allows you to define one or more special 'Wildcard' routes that have ‘\*’ (meaning any) as the email address. If you do this then you must also specify a sender address. You can also apply any other criteria as appropriate. These Wildcard Routes must be placed at the bottom of the order (but above the fallback route). See this [explanation of Wildcard Route configuration](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic/wildcard-routes-for-incoming-bcc-emails) for more information on this.

To help users understand how using wildcard routes will impact BCC emails, see this [table which shows the possible scenarios that can occur](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/incoming-emails-processing-logic/wildcard-email-routes-possible-scenarios)

## Handling of Incoming Reply emails

A specific scenario to handle for incoming email processing is where someone CC'd on a mail sent into Enate replies to that email. Enate recognizes the situation and will attach that mail to the original work item, rather than creating a brand new work item.&#x20;

The technical specifics of this are as follows: Improved 'InReplyTo' logic has been added for processing incoming mails. We now validate if the 'InReplyTo' field of the incoming email aligns with the Message-ID of a prior email. When matched, the email/communication is appended to the relevant work item. In short: if we can tell that a mail has been sent in reply to a mail we already know about, we direct that new mail to the previous mail's work item.

{% hint style="info" %}
Additional Note:

* If your system is using Traditional/Mixed mode, we verify if the 'InReplyTo' field corresponds to the Message-ID of **ANY** previously received email, irrespective of being incoming or outgoing.
* If your system is running in Exclusive (i.e. Plus Addressing ONLY Mode), we verify if the 'InReplyTo' field corresponds to the Message-ID of previous **INCOMING** received emails only (not outgoing mails).
  {% endhint %}
