# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes.md

# Email Routes

## Overview <a href="#a-adding-an-email-route" id="a-adding-an-email-route"></a>

Once you have some email connectors defined, you can reference them in email routing to specify where emails coming into each mailbox should be routed by Enate (i.e. which work items it should start).

The Email Routes page is where you can create new email routes and manage your existing ones.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjGvlUkYh3dPJzXKpliLH%2Fimage.png?alt=media&#x26;token=ac85971a-995e-4b99-9742-c00304eeeb5b" alt=""><figcaption></figcaption></figure>

Email routes are grouped by the email connector to which they are associated. These groups can be expanded and collapsed, making larger bodies of data easier to work with.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOXsVUj0Z74onN6qXpRId%2Fimage.png?alt=media&#x26;token=f5aa81a8-07aa-49bb-8fed-45e05eda1a22" alt=""><figcaption></figcaption></figure>

#### Filtering email routes

At header level, you can search to filter down your view to just one Connector:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FARwyVcOpruw8WsV9uJYI%2Fimage.png?alt=media&#x26;token=e06b9149-7af7-477b-885c-2501e37963ff" alt=""><figcaption></figcaption></figure>

#### Search by Connector details within each section&#x20;

You can search for a route at a connector-level, based on its email address, process and/or Ticket category (if relevant).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDBJhAi8yvnrNAFyw3dOl%2Fimage.png?alt=media&#x26;token=2c1d4013-0f1d-4e2c-a0d0-4ebab43e3de7" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note that these searches are all 'start with' searches rather than full wildcard searches, e.g. if you type 'France' it will search for items 'France\*' rather than \*France\*..
{% endhint %}

#### Folder Filter for Graph API Routes

For Graph API routes, you have the option to view folders as an additional filter at the top of the screen.

## Adding an Email Route <a href="#a-adding-an-email-route" id="a-adding-an-email-route"></a>

Watch this video to find out how to set up an Email Route:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MjY1NA==>" %}

More information about the attributes to configure when creating a new email route:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzqEubn9i5a7qsgGZxVBK%2Fimage.png?alt=media\&token=53761ac8-b829-46ef-8122-44ecfc74f98a)

| **Attribute**             | **Comments**                                                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Email Connector Name      | Select from list of pre-existing Connectors                                                                                  |
| Route Name                | Friendly name fo the Email Route                                                                                             |
| Email Address             |                                                                                                                              |
| Process                   | <p>The specific process, e.g. Ticket OR Case now.</p><p>(Select Customer, Contract, Service and Process).</p>                |
| Ticket Category           | The category value to set when launching a new Ticket (Relevant for Tickets only).                                           |
| Send Automated Emails     | This lets you choose whether or not you want to send automated emails to the work item's contacts. This is defaulted to OFF. |
| Create Work For Test Mode | If the email address can be used to create work in Test mode, or only in Live environment.                                   |
| Enable                    | Whether the routing setting is currently active.                                                                             |

{% hint style="info" %}
Note: The feature to send a Ticket Acknowledgment email to CC users is an enhancement of the existing functionality where an auto-confirmation email or acknowledgment is currently sent only to primary contact/sender but not to the CC users.
{% endhint %}

When editing an email route, you are also able to see its activity history by clicking on the Show Activity button. You can see when the email route was created and by who, as well as if any edits have been made to the email route, when they were made and by who.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpg6LWUc3pHK4L_bbl%2F-MWphT1_wgDJK75T735C%2Fimage.png?alt=media\&token=39731d74-de8a-4b1f-937b-ca2011fd6b04)

{% hint style="info" %}
Note: when you delete a Case or Ticket process or a Customer/Service/Contract that has linked Email Routes, you will be notified of this and will need to update the respective Email Routes in order to stop them from creating more work for the process.
{% endhint %}

### Quick-create Routes from Connector section shortcut

Additionally, as a useful shortcut you have to ability to add a new email route directly within a specific email connector itself - clicking on the '+' icon next to a connector will bring up the 'Create an Email Route' pop-up with the email connector name already filled it.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fu3ay3y1IdGoDOwv7GS7m%2Fimage.png?alt=media&#x26;token=01a6bcce-da0f-44a1-ad8c-26793594bc8c" alt=""><figcaption></figcaption></figure>

## Adding Email Routing Rules <a href="#adding-email-routing-rules" id="adding-email-routing-rules"></a>

You can add routing rules to an email route to provide a more fine-tuned way of determining where an incoming email gets routed to (and therefore what kind of work item gets created). Watch this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM2MjY2MA==>" %}

Routing rules can be based on the information of the incoming email including:

1. Important Flag on Email - if the email has been flagged as 'important'
2. Has Attachments of Type... - if the email has an attachment of a certain type - list of file extensions separated by a semi-colon e.g. .pdf; .docx
3. Key Words in the Subject Line - list of key words in the email subject line separated by semi-colons e.g. urgent; support; reset
4. Recipient List Includes - email address of the recipient of the email.  This can include multiple potential recipient email addresses, both individuals email addresses and [specified domains](#email-routing-by-domain). If there are multiple email addresses, each much be separated by a semi-colon e.g. <john.smith@example.net>; <brenda.johnson@acme.com>
5. Sender List Includes - email address of the sender of the email. This can include multiple potential sender email addresses, both individual email addresses and [specified domains](#email-routing-by-domain). If there are multiple email addresses, each much be separated by a semi-colon e.g. <john.smith@example.net>; <brenda.johnson@acme.com>
6. Sender's company name includes - lets you direct incoming mails based on the company the email sender belongs to. This stops you having to create multiple variations of slightly different email domain-based routings for your larger clients. Select the sender's company name from the dropdown. You are able to add multiple companies. Any emails arriving from email addresses belonging to the companies you have selected will start the process set in the email route.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJPEvDy8Q40ypi0iH6lUX%2Fimage.png?alt=media&#x26;token=b843f4c9-336b-4ca0-899a-efb2cf66f89c" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Please note that information from the incoming email body itself cannot be used when routing emails.
{% endhint %}

You can add multiple routing rules to an email route:​

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5lOGx3YsooyEWfRNkSg1%2Fimage.png?alt=media\&token=64a7cf3f-7aa2-46e0-8c34-45f34165d571)

#### Email Routing by Domain

You can route emails based on a particular email domain by adding a '\*' before the domain:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvgRNHy8wcs5givUjBD0V%2Fimage.png?alt=media&#x26;token=27c9f691-1d30-4d77-b67f-eaa729e4201e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note that this is only available for 'Sender List Includes' and 'Recipient List Includes'.
{% endhint %}

### Ordering Email Routes

You can easily adjust the ordering of the routes for a connector by dragging and dropping to the desired location. **When deciding on the order in which to run multiple related routings, you should place the most specific rules first, and set more generic ‘fallback’ routings last.**

Additional notes regarding email route reordering:

* Email routes cannot be dragged outside of their respective group.
* Reordering via the routes grid is only possible with the necessary permissions.
* Email route re-ordering will be blocked unless the route grid is sorted by **Priority Order: ascending** (as this makes the reordering interaction less confusing). When the route grid is not sorted by Priority Order: ascending, a message will show to alert you.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpg6LWUc3pHK4L_bbl%2F-MWphqJHAMevWL9UFeTJ%2Fimage.png?alt=media\&token=3b2af1be-a419-48e1-85db-45ef900285ea)

#### Quick Reordering of Email Routing <a href="#quick-reordering-of-email-routing" id="quick-reordering-of-email-routing"></a>

For connectors with extremely large numbers of routings, you may wish to manually set the order number directly (a useful alternative to having to drag routings hundreds of places up and down some of the larger lists). To do this, simply right-click the desired row and click the resulting tooltip:

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpg6LWUc3pHK4L_bbl%2F-MWphv_Wxma53mFlQ8hk%2Fimage.png?alt=media\&token=76c8b78d-32cf-4127-adba-2dcc181cf2c5)

## Fallback **Email** Routes

A fallback email route needs to be [set for the primary email address of each email mailbox in your system](https://docs.enate.net/enate-help/builder/builder-2021.1/email-connectors-detail#e-default-email-connector-for-outgoing-emails-1).

This will ensure that any mails arriving to that connector which don't get handled by the various email routes configured will at least be handled by this fallback and will kick off the Case or Ticket it routes to.&#x20;

Fallback email routes show in your email routes section with some specific impacts.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F7U7Q7CYQ1HVAjBAb8u3B%2Fimage.png?alt=media&#x26;token=209412eb-02c1-4449-bb2d-814c27502a42" alt=""><figcaption></figcaption></figure>

Details of this are as follows:

* These routes will always display at the foot of the Email Routes list
* The Routing Rule will be set to read-only
* The Email Connector will be set to read-only
* The 'Enable' setting is set to ON, and is read-only

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F0JBRc0GeaZ604jNYwu6E%2Fimage.png?alt=media&#x26;token=7df6ce67-c19a-4c7e-8925-1efc80d10c76" alt=""><figcaption></figcaption></figure>

## Email Route configuration limitations

When configuring email routes, if a sender is an unknown user or a new contact, a route that contains a company filter cannot match. This can lead to emails possibly being sent down the wrong route. To help avoid this, do not combine the following configurations:

* Combination One\
  1\. Auto create contacts\
  2\. Contacts locally scoped\
  3\. One or more email routes with a company filter
* Combination Two\
  1\. Contacts Locally scoped\
  2\. One or more email routes with a global company filter

Systems set up in this way may result in unpredictable and inconsistent routing of mails and should be avoided. These combinations of setup are not supported.
