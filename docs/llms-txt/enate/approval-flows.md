# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/approval-flows.md

# Approval Flows

Enate allows you to create, manage and use approval request flows by using the dedicated 'Approvals' Action type.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NDEwNw==>" %}

## What are Approval Actions? How do they work?

Often within the Case flows of business processes which are built in Enate there are points where external people (i.e. people working **outside** Enate - this could be business managers within your company or the relevant client company) need to sign off on activities before the process can continue. Payroll processes are good examples of such processes, where client management need to sign off on payroll reports before the process can be allowed to continue.

Enate's Approval Action is built to specifically support these scenarios in a more integrated way - to ensure that this 'approval cycle' is tightly managed and visible within the flow of activities in Enate. When an Enate Case reaches an Approval Action in a flow, things then work as follows:

1. Enate uses uploaded business rules to **determine the Approvers** to whom approval request emails should be sent (standard email templates are available, but these can be modified to contain information sufficient for approver to review what is being requested). See dedicated section describing how your approver business rules can be uploaded into Builder.
2. Once the approvers are determined, **Enate sends out Approval Requests** and then **Waits for their response**. Depending on the type of approval defined, this might send out one request after another (awaiting approval from the first) in a multilevel request, or might send the request to a group of people in one go, waiting for either one or all to approve before continuing.\
   \&#xNAN;*Note: While this is happening, the Approval Action in Work Manager sits in a state of '**Wait for more Information**'*
3. Those **approvers can then approve or decline**, via a link in the email sent to them which takes them to an online form.
4. Once all required Approvals have been received, **the Case process can continue again\***.&#x20;

#### Exceptions - handled by Agent in Work Manager

There may be some exception scenarios to the above where an Agent in Enate can access the Approval Action in Work Manager to carry out any required activities. The can be:

* **No approvers (or insufficient approvers) have been determined automatically**. The Agent needs to add approver names and set the Action to 'Wait for more Information' in order for the system to send out approval request mails.
* **The approval has been declined.** The Agent then must either organise whatever adjustments may be necessary before setting the Action back to 'Wait for more Information' in order for the system to send out approval request mails, OR mark mark the activity as unable to resolve, OR mark the Action as 'Resolved', which will approve the request and move the Case on in the flow.

See the [Agent activity for Approval Action exceptions](#agent-activity-for-approval-action-exceptions) section for more detailed information around this. This is found within the [How Approval Actions Work at Runtime](#how-approval-actions-work-at-runtime) section.&#x20;

## Setting up Approval Actions in your Case flows&#x20;

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NDEzMw==>" %}

To start using approval flows in Enate, you'll first need to set up a few things up in in Builder before it can be used in Work Manager at runtime. The things you need to set up are:

* [The Approval Flow as part of a Case](#setting-up-an-approval-flow)
* [Approval email templates](#creating-approval-email-templates) - setting up the email the person who will make the approval decision will receive
* [Approval rejection reasons](#creating-approval-rejection-reasons) - these are the reasons an approver can select from when declining a request
* [Approval rules](#defining-approval-rules) - supplying the rules which determine who approval request are to be sent to

### Add an Approval Action to your Case flow

To set up an approval flow within your Case flow, you just add a single Approval Action. You can either add an existing one from the Actions list if one has already been created, or you can create a brand new one.&#x20;

Approval Actions can be created in the same way any other Action is created in Enate: either from the Service Line page, or directly from within your Case flow.

To create an Approval Action from the Service Line page, select to create a new Action under the desired service line, give the action a name and a description and choose approval action from the type drop down. You can also give the Action approval type a global checklist if you wish.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUfjUGDVmTZDLLT3mBUby%2Fimage.png?alt=media&#x26;token=53e94a91-a34e-4d90-95ca-aca7b6116f20" alt=""><figcaption></figcaption></figure>

To create an Approval Action directly from the Case flow itself, open a Case flow in edit mode, click on an Action's menu and then instead of clicking to add an existing Action, select to create a new Action by clicking the '+' icon.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FwTYKnyd3czrpVuQdoSUS%2Fimage.png?alt=media&#x26;token=cbc20b86-37ed-4667-b085-d3113063bcca" alt=""><figcaption></figcaption></figure>

Give the Action a name, add a description if you wish and for its type, select 'Approval'.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZ9zMKKhw3RR0w9SgZ4Mz%2Fimage.png?alt=media&#x26;token=01c4426c-c15c-453e-945c-6769791cfeb9" alt=""><figcaption></figcaption></figure>

When you click 'OK, the Action will be created and added to the Case flow.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FdFnSLUY4drB6Q6XANzrF%2Fimage.png?alt=media&#x26;token=f206e78a-561f-4f01-8b82-e2dd3ff7e73f" alt=""><figcaption></figcaption></figure>

### Fill out the Action's settings

Once you have added your approval Action to your flow, you will then need to fill out its settings.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Ftek9xybbsPn4ogSdxjGx%2Fimage.png?alt=media&#x26;token=032184b0-dcc2-4345-b439-292acb1e8e5e" alt=""><figcaption></figcaption></figure>

On the Action Info tab you will need to set when it's due and set an allocation rule.&#x20;

{% hint style="info" %}
Note that this Allocation is NOT for sending to the approver, this determines where that Action would be routed to in Work Manager **should any issues be encountered**. The actual Approval decision doesn't happen in Work Manager, it's a mailed out link, and the rules for determining where it should go aren't managed this way - see the '[Defining Approval Rules](#defining-approval-rules)' section for an explanation.&#x20;
{% endhint %}

There's also general settings for the Action too, and ability to set a custom card, again only really for use in the unlikely event that someone needs to intervene and view the action in Work Manager.

Next, go to the Approvals tab to define the settings which specifically relate to the approval activities.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZFI7PdtuZoAkiVW6iMpM%2Fimage.png?alt=media&#x26;token=a5796c4f-a329-4112-ba1a-0797e489a05d" alt=""><figcaption></figcaption></figure>

### Approval Types

You'll need to fill in the **Approval Type**. There are three approval types that you can choose from:&#x20;

<table><thead><tr><th width="181">Approval Type</th><th>Use</th><th>Note</th></tr></thead><tbody><tr><td>Multilevel</td><td>More than one level of approval is required. Request is sent to the first-level approver and, only if approved, onto the next level, and so on, up to a maximum of three levels. </td><td>If you've selected Multilevel, you will also need to add how many levels of approval are needed in the 'Approval Levels' column (maximum 3).</td></tr><tr><td>Parallel Any</td><td>The approval request is sent to multiple people at the same time, and the decision is taken from the first one to respond.</td><td>A maximum of 5 approvers can be specified at runtime.</td></tr><tr><td>Parallel All</td><td>The approval is sent to multiple people at the same time, and approval is needed from all of them. If any decline, the approval is declined.</td><td>A maximum of 5 approvers can be specified at runtime.</td></tr></tbody></table>

If you have selected 'Multilevel' as your approval type, you will also need to add how many approval levels you would like the request to have, up to a maximum of 3. If you have selected either of the two parallel approval types, the approval levels will automatically be set to 1.

In the Approval Request Email column, select which approval email template you would like to be sent out to the approvers. See the [following section](#creating-approval-email-templates) to find out how to create and adjust approval email templates.

## Creating approval email templates

The person who will make the approval decision will receive an automated email containing the information they need to make the decision.&#x20;

You can set the template of that email in the Email Templates section of Builder.&#x20;

You can either select one of the system standard templates, depending on the approval type, or you can select from one of your own custom email templates.

There are two system standard templates available:

* Approval Request Multi-Level - make sure to select this option if you're approval is multilevel
* Approval Request Parallel  - make sure to select this option if you're approval is a parallel request

If the system standard templates don't quite meet you needs, you can modify the existing pre-created approval templates, or create your own from scratch. When you are creating your own from scratch, make sure to set the purpose of the template as 'approval request' in order for it to appear as an option for you to choose from when you are designing your approval process in the Case screen.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOzIJMZRfVoEN2VWRs9Ke%2Fimage.png?alt=media&#x26;token=bc33e3e1-e566-448f-bd46-c0b08972266b" alt=""><figcaption></figcaption></figure>

You can insert or edit the approve and reject buttons to you email using the 'Insert Approval Buttons' option.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfHAIXxvS7rg9B7AR8tU1%2Fimage.png?alt=media&#x26;token=33c92052-b045-4ce1-8972-ebb324d8d70d" alt=""><figcaption></figcaption></figure>

These buttons are editable using the button details pop up.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVErqA9mvhlijD1bX6lO1%2Fimage.png?alt=media&#x26;token=5989725b-ccd9-4011-9f87-e58dab0da7ab" alt=""><figcaption></figcaption></figure>

You can also add approval-specific custom fields to the template which will auto-populate with the details relevant for each specific approval request.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOkPl4bTUJo0h9hMITeej%2Fimage.png?alt=media&#x26;token=f06cd43b-c937-4f11-a0a1-be744e383a4d" alt=""><figcaption></figcaption></figure>

These fields include:&#x20;

* Approval Accept Request Link - inserts a hyper link to the approval acceptance page
* Approval Decline Request Link - inserts a hyper link to the approval decline page
* Approver Level - inserts the level of approver (this will only be relevant for multi-level approvals)
* Other Approver Names - inserts the names of the remaining approvers (this will only be relevant for multi-level approvals)
* Total Number of Approvers - inserts the total number of approvers
* Type of Approval - inserts the type of approval (i.e. multi-level and parallel)

Once you save it, you can select to use this template in your approval processes from the Case flow.

At runtime, when the flow of a Case reaches your approval action, the email will be automatically sent out to one or more approvers. The mail links for approval decision will take them to the relevant approval decision page, let them confirm a decision and add any comments if they want. If they've decided to decline the request, they will have to specify a rejection reason. The rejection reasons they can choose from are set in Builder, see the following section to find out more.

## Creating Approval Rejection Reasons

At runtime, if an approver decides to decline a request, they will have to specify a rejection reason.

The rejection reasons they can choose from are set the 'Approval Rejection Reasons' section of the System Settings page in Builder.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVVEFKqdTjtn4q4S7YrzA%2Fimage.png?alt=media&#x26;token=58e03b82-ba98-423a-980a-a4ab18d62c39" alt=""><figcaption></figcaption></figure>

There are a number of default, out-of-the-box reasons, which include:

| Rejection Reason                    | Description                                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Budget Constraints                  | The requested funds exceed the allocated budget or available funds for the specified period.            |
| Duplicate Requests                  | The same request has been submitted multiple times.                                                     |
| Incorrect or Incomplete Information | The submitted data or documentation is inaccurate, incomplete, or contains errors.                      |
| Missing Supporting Documentation    | Required supporting documents, such as invoices, receipts, or contracts, are missing.                   |
| Policy Non-Compliance               | The request or transaction violates company policies, regulatory requirements, or compliance standards. |
| Vendor or Partner Issues            | The proposed vendor or partner has encountered issues or concerns that impact the request's viability.  |

If these don't quite meet your needs, you can also create new rejection reasons. To create a brand new reason, click on the plus symbol.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6hfQEQyQVvR3Gae40yVt%2Fimage.png?alt=media&#x26;token=ba50bb0f-abf4-4c2e-9675-04fcc04aa91a" alt=""><figcaption></figcaption></figure>

Give the reason a name and a description and click to create.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FMzKPlVh7xn7WJXNsHFIF%2Fimage.png?alt=media&#x26;token=db1c5ae0-9bd3-478e-bbde-6acecbdb9259" alt=""><figcaption></figcaption></figure>

You can always edit a rejection reason after it has been created by clicking on it and editing its details in the subsequent pop-up, and you can delete a reason by hovering over the reason and clicking on the 'X'.&#x20;

## Defining Approval Rules

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NjM1MQ==>" %}

The most important part of this approval action set up to be aware of is supplying the rules which determine who approval request are to be sent to. There can be any number of different business rules, from the simple to very complex, involved here. Rather than create a dedicated rule interface in Builder for you to try to build them directly there (which would be very unlikely to cover such a wide range of required business scenarios), we instead use an approach where you can upload an Excel file where you can define whatever business rules you need to, as long as the result passes up to Enate the names of the individuals who are to be the approvers.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FviPnxHjMHfvdzOFXSlMZ%2Fimage.png?alt=media&#x26;token=7d24ea9a-4e37-4386-b77c-01e254f34fd5" alt=""><figcaption></figcaption></figure>

You can download an Excel template from the Approval Rules section of the System Settings page in Builder that you can use as a guide for your own rule creation.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FcGH66DdFk8k2BZYntvgt%2Fimage.png?alt=media&#x26;token=51a8d8fc-8b05-4a7d-90dd-e77d5801797b" alt=""><figcaption></figcaption></figure>

The first sheet of the template contains instructions about how you should correctly format your own approval rules.

Some of the excel template consists of standard sections where you'll need to provide data in a certain way, while other sections are more freeform where you can enter whatever business logic you need to. Note that the variables defined will need to be information Enate has access to, and the Approvers specified will at least need to have a Contact record set for them within the system.

The Input Parameters sheet is were you define the values that they will use in their rule conditions.

The Rules sheet is where users define your rule conditions. These rules should be based on the Input Parameters specified in the Input Parameters tab.

The Approver sheet is where you provide their approvers, and their approval levels. When an approval process is triggered in Enate, Enate will use these values to determine who to send the approval request to.

Whenever an Approval Action is triggered in a workflow, Enate will automatically run through the rules in the Excel template (passing in whatever variable values are asked for from the work item) extract the resulting approver names and email addresses and then send the approval requests to those individuals.

Once you have uploaded a valid rule file, it will be marked as having 'Validated Changes' .&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FIFbEoalzlT8Qopkx3nYS%2Fimage.png?alt=media&#x26;token=393b6933-591e-42a3-9a9e-3ebda3d2be7d" alt=""><figcaption></figcaption></figure>

This means it can be used for testing in Work Manager using test mode. Once you have done your testing and you are happy with your rules, set the rules sheet to live so that it can be used in live processes.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FbBb6JF0IgUVvxcsnCzU0%2Fimage.png?alt=media&#x26;token=e434ce28-5c9b-4f39-ad45-4e5d99b1965e" alt=""><figcaption></figcaption></figure>

You can also download, delete and view the activity history of the rules file using the ellipses menu on each uploaded sheet.

## How Approval Actions work at Runtime

Approval requests get sent out to agents working externally from Enate to approve or decline.

There are a few different types of approval that affect how the decision is made:

* In a multilevel scenario, the request email is sent to each new level upon successful approval from previous, up to a maximum of 3 levels. If any person declines, the approval is declined.&#x20;
* In a parallel any scenario, the request email is sent to all approvers and the first decision is taken.&#x20;
* In a parallel all scenario, the request email is sent to all approvers and ALL must approve for the request to be approved. If any decline, the approval is declined.

If the request gets approved by all necessary parties, the approval Action gets successfully resolved and closed automatically, so no Work Manager Agent will need to pick it up, although the closed Action can always be viewed by manually clicking on it.

### Agent activity for Approval Action exceptions

There are, however, a couple of scenarios where a Work Manager agent might need to pick up and further process an approval Action, if the approval has been rejected or if the agent needs to add in approvers because one or more required approvers is blank.

In the scenario where an approval request has been **declined**, the Action will move into a state of 'To Do' and so will ultimately need to be dealt with by a Work Manager Agent. They should review the rejection reason provided by the approver and decide how to proceed. They can either:

1. **Update as needed and Resend the request by setting the Action to 'Wait'.** This will auto-send out the approval request email again\*\* and place the Action in a state of 'Wait for More Information' - since we're waiting for external information (an approval response) to be registered back into the system before activity can proceed.&#x20;
2. **Mark the Action as Unable to complete.** This will alert the Case owner who then needs to decide how to proceed - perhaps by reworking the Case or closing the Case entirely.
3. **Mark the Action as Resolved** which will manually mark the request as approved. The Case with then progress to the next Action.

{% hint style="info" %}
\*\*Note: Approval request email sending will start again from the beginning, i.e. all requesters will be mailed again. If they click on any previously sent emails, they will be met with a message telling them that THAT specific approval request is no longer valid, as the details of what is being requested may have changed). &#x20;
{% endhint %}

#### **While Agents are dealing with an Approval Action, and how to Set it going again..**

In the scenario where an agent needs to add in approvers because one or more required approvers is blank (or make changes which result in the approval requests needing to be sent out again), the Agent will pick up the Approval Action in a state of To Do. Once they have finished making any adjustments and / or filling in missing Approver names, the must **then place the Action in a state of Wait**. Once they do this will auto-send the approval request email and then move the Action to a state of 'Wait for more information' as it is waiting for external info (approval) before proceeding.

{% hint style="info" %}
Note: While an Approval Action is state of 'To Do', or 'In Progress', external parties who were mailed out approval requests will NOT be able to approve or decline. Instead the will be met with a message informing them that the item in question is currently being processed. Work Manager Agents MUST move the Action back to a state of 'Wait for more information' if they wish the approval activity to recommence.&#x20;
{% endhint %}

## If you want to time out Approval Requests..

By default, Approval Actions will continue in their current state when the action reaches its Due Date, even if sufficient approvals have yet to be received. If, alternatively, you would like the action to time out at that point, you can switch the 'Auto-complete on Timeout' setting in the General Settings for this Action to ON (the default for this is OFF). Set like this, upon reaching its due date the Action would instead close and the Case will be flagged for an Agent to look at and resolve as they see necessary, e.g. starting another Approval Action or reworking the Case from a previous point. The Case would not resume until the Agent has specified how to do so.
