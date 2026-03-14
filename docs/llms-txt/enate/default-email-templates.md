# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-template-configuration/default-email-templates.md

# Default Email Templates

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MjY4OQ==>" %}

## Overview

A list of default email templates are available to you that are immediately ready to use. You can edit  and adjust the content of these Default templates, but you cannot delete them.

There are three types of Default Email Template in Enate:

1. System Email Templates
2. Ticket/Case Email Templates
3. Feedback Footer Templates

## System Email Templates <a href="#b-system-email-templates" id="b-system-email-templates"></a>

A number of System Email Templates are available by default. These can be edited but cannot be deleted, and new System Email Templates cannot be created. Current System Email Templates are as follows:

* New Agent User Creation - will trigger when a new user is created
* Forgot Password - triggers when a user clicks on 'forgot password' on the login screen
* SSO Forgot Password - triggers when an SSO user clicks on 'forgot password' on the login screen
* Password Reset Confirmation - triggers to confirm when a user has successfully reset a password

{% hint style="info" %}
Note: Default Email Template content is supplied in English only, however you are able to [manually specify translations in other system-supported languages](https://docs.enate.net/enate-help/builder/builder-2021.1/adding-localisations).
{% endhint %}

## Ticket/Case Email Templates <a href="#d-ticket-email-templates" id="d-ticket-email-templates"></a>

Ticket/Case Email Templates are fully editable, and new ones can be created. Ticket Email Templates that are available by default are:

* Request Acknowledgement - triggers when a Ticket has successfully been created. Includes Ticket reference number. Goes to the primary contact of the recipient, and to any CC contacts.
* Ticket Launched Case - triggers when a Ticket has successfully been converted into a Case
* Ticket No Response - gets sent when a Ticket is in a state of 'Waiting for more information' and no response received within waiting time set. Goes to Primary Contact.
* Ticket Split - gets sent when a Ticket has been successfully split to the primary contact.

#### Setting Email Templates on Cases vs Action

When you set an Email Template (e.g. the Default Template) in the Case settings as part of Case configuration, this template will be used whenever an Agent chooses to manually compose an email while on the Case screen in Work Manager.

Note that this will NOT take effect for that Cases' Actions - you will need to set a specific Email template against an Action for it to display when an agent is manually composing an email when on an Action screen.

## Feedback Footer Templates <a href="#e-feedback-footer-templates" id="e-feedback-footer-templates"></a>

Feedback footer templates are fully editable and new ones can be created.&#x20;

The same GUI is used for defining Feedback Footer templates as for Email Templates, however it is only the HTML Body content that you define which will be used – it will be appended to the bottom of whatever email is being sent (if it’s configured to do add footers in).&#x20;

Any Files and Subject text configured which you might (irrelevantly) set when you’re defining a footer template will be ignored; only the body text is selected.

## Approval Email Templates

Enate allows you to create, manage and use approval request flows.

As part of this, the person who will make the approval decision will receive an automated email containing the information they need to make the decision.&#x20;

You can set the template of that email in the Email Templates section of Builder.&#x20;

You can either select one of the system standard templates, depending on the approval type, or you can select from one of your own custom email templates.

There are two system standard templates available:

* Approval Request Multi-Level - make sure to select this option if you're approval is multilevel
* Approval Request Parallel  - make sure to select this option if you're approval is a parallel request

If the system standard templates don't quite meet you needs, you can modify the existing pre-created approval templates, or create your own from scratch. When you are creating your own from scratch, make sure to set the purpose of the template as 'approval request' in order for it to appear as an option for you to choose from when you are designing your approval process in the Case screen.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FCGqJvHc7g7QOq50ErFop%2Fimage.png?alt=media&#x26;token=11b9164e-a14b-41c6-8c0e-c9141b5f4cb0" alt=""><figcaption></figcaption></figure>

You can insert or edit the approve and reject buttons to you email using the 'Insert Approval Buttons' option.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVTVQdupqMraZ2WERkPQj%2Fimage.png?alt=media&#x26;token=6da69b5e-b0d1-4cd3-873b-310ed54b2e6d" alt=""><figcaption></figcaption></figure>

These buttons are editable using the button details pop up.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUg8q0lxLxRsmQxmuRXkA%2Fimage.png?alt=media&#x26;token=ad46e3c6-dca5-48bb-a288-e72cd32378a8" alt=""><figcaption></figcaption></figure>

You can also add approval-specific custom fields to the template which will auto-populate with the details relevant for each specific approval request.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMuHJvgwloqMd7TImt19P%2Fimage.png?alt=media&#x26;token=7752e7dd-b5ba-4aee-bf52-411662eadbfe" alt=""><figcaption></figcaption></figure>

These fields include:&#x20;

* Approval Accept Request Link - inserts a hyper link to the approval acceptance page
* Approval Decline Request Link - inserts a hyper link to the approval decline page
* Approver Level - inserts the level of approver (this will only be relevant for multi-level approvals)
* Other Approver Names - inserts the names of the remaining approvers (this will only be relevant for multi-level approvals)
* Total Number of Approvers - inserts the total number of approvers
* Type of Approval - inserts the type of approval (i.e. multi-level and parallel)

Once you save it, you can select to use this template in your approval processes from the Case flow.

At runtime, when the flow of a Case reaches your approval action, the email will be automatically sent out to one or more approvers. The mail links for approval decision will take them to the relevant approval decision page, let them confirm a decision and add any comments if they want. If they've decided to decline the request, they will have to specify a rejection reason. The rejection reasons they can choose from are set in Builder, see the following section to find out more.
