# Source: https://docs.enate.net/enate-help/integrations/enate-integration-services-powered-by-snaplogic/build-your-pipeline-enate-integration-pattern-1.md

# Build your Pipeline - Enate Integration Pattern 1

This walkthrough will take you through how to integrate an external system into Enate using our Enate Integration Services iPaaS approach powered by Snaplogic. This will demonstrate one of the four standard patterns which you can achieve with iPaaS, specifically [Pattern 1](https://docs.enate.net/enate-help/integrations/ipaas-patterns#pattern-1-enate-workflow-updates-external-application) where we want to **update or get data from an external system at a known point in an Enate Workflow**. The shortcuts to the main sections for building this pattern are:

[**Enate Configuration - Case, Action & Data Fields**](#configuration-in-enate)

[**SnapLogic Pipeline Construction - Building the Snaps**](#snaplogic-pipeline-overview)

[**Getting Enate to call the Pipeline**](#how-do-i-get-enate-to-call-the-snaplogic-pipeline)

### Prerequisites

What you'll need in order to connect Enate with 3rd party systems using Enate Integration Services:

* Enate Access – An Enate instance where you have Builder-level admin access
* Enate Integration Services (Snaplogic) Access – speak to your account manager to discuss purchasing Enate Integration Services for this access.
* Familiarization with Snaplogic – see the [**SnapLogic Overview section**](https://docs.enate.net/enate-help/integrations/enate-integration-services-powered-by-snaplogic/snaplogic-overview) for this.
* A 3rd Party system (in this example HubSpot), where you have configuration-level admin access.

## Process Overview

We will build a standard Enate Case process which gets created each time there is a new business Deal in our area of the business. Part of this case calls an external system (we'll use HubSpot here) to bring data into the Enate Case process. This could just as easily be e.g. SAP, Salesforce etc.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fis9C0AySMZbo7IA9zHdC%2Fimage.png?alt=media&#x26;token=f8fce611-fd8c-401c-b988-98a28fcf609f" alt=""><figcaption></figcaption></figure>

This will be done by calling out to Enate Integration Services (powered by Snaplogic) which will grab the data from HubSpot, update the Enate Action, and then confirm that the API call is complete. The main activities in the end-to-end flow are as follows:

1. **In Enate: External API Call** – a ‘Trigger External API’ action is placed into the Case flow in Builder. This calls out to Enate Integration Services (Snaplogic) to run a specific Pipeline.\
   \
   Then the SnapLogic pipeline...
2. **Calls the 3rd party System (HubSpot) –** In Snaplogic a pipeline is called, this will make a call out to the 3rd party system, in this case HubSpot.
3. **Obtains Data from HubSpot -** The incoming information passed into HubSpot will allow the relevant values to be identified and sent back to Snaplogic.
4. **Generates a Bearer Token for Accessing Enate** - while this part isn't strictly necessary to complete the final snap in the pipeline (which will actually use a Callback URL for authorization instead in this example), knowing how to generate a Bearer Token for getting authorized access to your Enate system will be essential for your pipeline work going forward.
5. **Updates Enate Data Fields & Confirms Completion of Enate Action –** The updated field values are sent back to the Action in Enate, ‘Trigger External API’ action in Enate is marked as complete, allowing the Enate Case to move onto the next part of the Enate flow.

## Configuration in Enate&#x20;

### Create Case, Custom Fields, Custom Card

Steps for the required Enate configuration are as follows:

* In your Builder environment, create a new Case process for New Deals.
* In conjunction, create a series of new Custom Data fields and a Custom Card for them to show on.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FNYdvjr41ROOPW4fnoB0I%2Fimage.png?alt=media&#x26;token=09c52881-9298-45f7-aa30-40dc0f56fe6b" alt=""><figcaption></figcaption></figure>

Set Field values as follows:

<table data-header-hidden><thead><tr><th width="182" valign="top"></th><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">Field Name</td><td valign="top">Field Type</td><td valign="top">Dropdown Values</td></tr><tr><td valign="top">Deal Name</td><td valign="top">Text</td><td valign="top">New Business; Existing Client</td></tr><tr><td valign="top">Deal Type</td><td valign="top">Simple Dropdown</td><td valign="top"> </td></tr><tr><td valign="top">Deal owner</td><td valign="top">Text</td><td valign="top"> </td></tr><tr><td valign="top">Priority</td><td valign="top">Simple Dropdown</td><td valign="top">Low; Medium; High</td></tr><tr><td valign="top">Deal Amount</td><td valign="top">Number</td><td valign="top"> </td></tr><tr><td valign="top">Created Date</td><td valign="top">Date/Time</td><td valign="top"> </td></tr><tr><td valign="top">Close Date</td><td valign="top">Date/Time</td><td valign="top"> </td></tr></tbody></table>

* Link the Custom Card to the Case configuration.
* Add a new Action at the relevant point in your Case process. You may need to create a brand new Action. Give it a sensible name, and choose type ‘**Trigger External API Action’.**
* You’ll need to set the following information as part of the detailed Action settings:

<table data-header-hidden><thead><tr><th width="151" valign="top"></th><th width="373" valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">Attribute</td><td valign="top">Value</td><td valign="top">Notes</td></tr><tr><td valign="top">API Integration URL</td><td valign="top">url would be of this format..<br><br><a href="https://emea.snaplogic.com/api/1/rest/slsched/feed/enatepoc/projects/Sam%20Ward/S4Hana%20Get%20Demo?bearer_token=2FLJiVLav3OvRtzAMlTnFbhnvX1T6Icf">https://emea.snaplogic.com/api/1/rest/slsched/feed/enatepoc/projects/Sample%20Project/HubSpot%20Get%20Demo?bearer_token=2FLJiVLav3OvRtzAMlTnFbhnvX1T6Icf</a><br><br></td><td valign="top">See <strong>section below</strong> on setting this value.</td></tr><tr><td valign="top">Response Expected</td><td valign="top">True</td><td valign="top">Set this if you wish the process to time out if you have not received a response after a certain amount of time.</td></tr><tr><td valign="top">Response Expected Within (Mins)</td><td valign="top">10</td><td valign="top">You can set your desired timeout minutes here, this value is a suggestion only.</td></tr></tbody></table>

### Setting the API Integration URL & Bearer Token in your Enate API Action

The API Integration URL you enter here will call a specific Pipeline in Enate Integration Services (Snaplogic). To add that url in this Enate action’s config, you’ll first have to create that Pipeline in Snaplogic. In addition to pointing this action at the right Snaplogic location and instance, the Pipeline will also require some authentication before it will allow the action to access it. This is done by adding in a ‘Bearer Token’ as a variable at the end of the url. The format of the url is:

https\://\[snaplogic pipeline link] + ‘?bearer\_token=’ + \[the pipeline’s bearer token’], e.g.

<https://emea.snaplogic.com/api/1/rest/slsched/feed/enatepoc/projects/Sample%20Project/HubSpot%20Get%20Demo?bearer_token=2FLJiVLbv6OvRtzAMlTnFbhnvX1G6Idf>

Check out this section on [**How to obtain the pipeline url and the bearer token from Snaplogic**](#how-do-i-get-enate-to-call-the-snaplogic-pipeline).

Once you’ve completed your steps to create your pipeline and token, you will need to circle back round to here to complete your action configuration (at which point you may then be ready to test the end to end process).

#### Additional Action Level Configuration to complete

* Set an Allocation rule to route the Action back to the work item starter – this would be used in the situation where the action times out, to provide a ‘human in the loop’ to deal with any issues.

## Snaplogic Pipeline Construction

Now that your Enate action to trigger your Enate Integration Services pipeline is almost complete, we can move over to Snaplogic and start to create the Pipeline. As a prerequisite, check out the [**SnapLogic Overview**](https://docs.enate.net/enate-help/integrations/enate-integration-services-powered-by-snaplogic/broken-reference) section to make sure you are comfortable navigating around Snaplogic and creating Pipelines.

### Pipeline Overview

Here is downloadable example of this Pipeline:

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtRbkwFE6Jn2QKXTxwi6c%2FExample%20Pipeline_2025_02_05.slp?alt=media&token=6f49e58c-026f-42aa-9363-5bf4cf59573b>" %}

## Walk-through of each Snap

This section walks through how to configure each of the snaps in the pipeline. Once this is done, you can [configure Enate to call this pipeline](#create-a-triggered-task-and-add-url-into-enate-action-config).\
\&#xNAN;*Snaps 2 & 3 relate to the third party system, in this example Hubspot. When building your own version of this, the details of how to configure equivalent snaps will obviously be specific to YOUR third party system.*

{% tabs %}
{% tab title="Snap 1" %}

### Create Pipeline & Add Snap 1 - JSON Parser

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FdeE2keS3rfs8ogcOJPPy%2FSnap1.png?alt=media&#x26;token=19b24fdf-7852-4ab4-9239-dc0d33300926" alt=""><figcaption></figcaption></figure>

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTc3NzgxNg==?utm_source=gitbook&utm_medium=iframely>" %}
{% endtab %}

{% tab title="Snap 2" %}

### Snap 2 - HubSpot Bulk Read (Accessing your 3rd Party System)

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FOZGcGs0EXhaX3NEifHIb%2FSnap2.png?alt=media&#x26;token=ea459bf2-6d1e-4da1-a8ca-486927710823" alt=""><figcaption></figcaption></figure>

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTc3NzgyMQ==?utm_source=gitbook&utm_medium=iframely>" %}
{% endtab %}

{% tab title="Snap 3" %}

### Snap 3 - HTTP Client - Get Open Deals from HubSpot (3rd Party System)

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKdhEy0CrWmlyctQkh4Zu%2FSnap3.png?alt=media&#x26;token=c6911163-7d6f-4d49-8be2-0a20f03b0ae9" alt=""><figcaption></figcaption></figure>

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTc3Nzg2MA==?utm_source=gitbook&utm_medium=iframely>" %}
{% endtab %}

{% tab title="Snap 4" %}

### Snap 4 - HTTP Client - Get Enate Bearer Token

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FyppdJP0T0KuUrhFffcfR%2FSnap4.png?alt=media&#x26;token=0ce37947-765d-476f-aefc-6b71355e31a5" alt=""><figcaption></figcaption></figure>

This snap is an essential for almost all pipelines you may build, as it gets a Bearer Token from Enate which can be used in many of the subsequent Snaps you build which need to Access Enate\*.\
\&#xNAN;*\*the other way to get authorization is to use the 'Callback URL' which forms part of Enate's external API call out to Snaplogic)*

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTc3Nzg0Nw==?utm_source=gitbook&utm_medium=iframely>" %}
{% endtab %}

{% tab title="Snap 5" %}

### Snap 5 - HTTP Client - Update Action & Complete

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FWhqQRzKjIiQ9WuM0QrjJ%2FSnap5.png?alt=media&#x26;token=7a0c2e24-8d83-49b2-a98a-06317be79a8d" alt=""><figcaption></figcaption></figure>

This snap updates the Enate Action which called the Pipeline, sending the values grabbed from HubSpot and mapping them to the Enate fields to be updated. It also tells Enate that the action is complete and it can move on.

Note that rather than use the Bearer Token approach to authorize access to Enate here, we're instead going to reference the 'Callback URL' which would be supplied to Snaplogic by the calling Enate 'Trigger External API' action.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTc3Nzg1Nw==?utm_source=gitbook&utm_medium=iframely>" %}

As a sample of the kind of code you'd be writing here to update fields back in Enate, here is the code used in the above snap to update the calling action with values from the 3rd party HubSpot system:

```
{
  "DataFields": {
    "DealName": $original.entity.deals[0].deal_name,
    "DealType": $original.entity.deals[0].deal_type,
    "Priority": $original.entity.deals[0].priority,
    "DealAmount": $original.entity.deals[0].deal_amount,
    "DealOwner": $original.entity.deals[0].deal_owner,
   "CreatedDate": $original.entity.deals[0].created_date,
   "CloseDate": $original.entity.deals[0].close_date
  },
 "Success": true
}
```

{% endtab %}
{% endtabs %}

Once this Pipeline is created, it's time to circle back to the Enate configuration to tell the Enate Action which Pipeline to call from SnapLogic. This is done by creating a Triggered Task in SnapLogic...

***

## How do I get Enate to call the SnapLogic Pipeline?&#x20;

### Create a Triggered Task & add url into Enate Action Config

To tell Enate how to call this pipeline we need to:

* create a Triggered Task in SnapLogic
* Paste the url for this Triggered Task back into the configuration settings for the Enate Action, along with **an additional variable for a SnapLogic Bearer Token.**

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTc3Nzg1NA==?utm_source=gitbook&utm_medium=iframely>" %}
