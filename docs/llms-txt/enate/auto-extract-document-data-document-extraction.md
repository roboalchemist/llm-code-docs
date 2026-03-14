# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/auto-extract-document-data-document-extraction.md

# Auto-extract document data - Document Extraction

## Overview

The Document Extraction component, available in Enate [Marketplace](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace),  automatically extracts the relevant data from files attached to incoming emails so that this data can be used in further processing of the work item, saving your agents time and effort. This also means that documents such as PDFs can be scanned and used both to start Cases in Enate and to form part of the ongoing process's activities.&#x20;

## Infrrd Set Up

There are a few steps to follow when it comes to switching Document Extraction component on with Infrrd.

1. [Marketplace Setup](#1.-marketplace-setup)
2. [Case Flow Setup](#2.-case-flow-setup)

Watch this video to find out more about integrating Enate and Infrrd Document Extraction.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTQ5NTQ1OA==>" %}

### 1. Marketplace Setup

You'll first need go to the to Marketplace section of Enate Builder and click to activate the Infrrd Document Extraction component.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBItFTKTVlty34w4E8Wc2%2Fimage.png?alt=media&#x26;token=1004c233-ed9f-4ba7-b347-f8f47dd08e15" alt=""><figcaption></figcaption></figure>

In the following pop-up, you'll need to add the URL and account ID of your Infrrd platform, as well as the model(s) you want to use.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvXx5RnGHtdmKrc1JqqLi%2Fimage.png?alt=media&#x26;token=2e184eee-488b-4f30-9845-2e7fecb676bc" alt=""><figcaption></figcaption></figure>

To add a model, you'll first need to make sure that it is already configured in your Infrrd platform. You'll then need to enter the following information, all of which can be found in your Infrrd platform.

* Model ID
* Model name
* API key

You can add as many models as you like. These models are what determines how documents get classified. For example, you might have configured a model that is trained to only identify invoices, so that would be the model you would want to use for your invoice processes.

Once you have entered all of the above information, you'll need to test the connection.

Once the connection has been tested successfully, click to activate.

### 2. Case Flow Setup

You'll then need to set up your Case flow to support the Document Extraction component. This involves adding an 'IDP Data Extraction' Action in Enate Builder to use in your desired Case flows.&#x20;

You can either add an existing one from the Actions list if one has already been created, or you can create a brand new one.&#x20;

IDP Data Extraction Actions can be created in the same way any other Action is created in Enate: either from the Service Line page, or directly from within your Case flow.

To create an IDP Data Extraction Action from the Service Line page, select to create a new Action under the desired service line, give the action a name and a description and choose approval action from the type drop down. You can also give the Action a global checklist if you wish.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fo0xtCjMHDbFi48mf9gRE%2Fimage.png?alt=media&#x26;token=d81237ef-3d24-4aef-892d-7547571d9b9d" alt=""><figcaption></figcaption></figure>

To create an IDP Document Extraction Action directly from the Case flow itself, open a Case flow in edit mode, click on an Action's menu and then instead of clicking to add an existing Action, select to create a new Action by clicking the '+' icon.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FXU9CmNPh4Pods7vkRvhB%2Fimage.png?alt=media&#x26;token=1296d751-ff36-4200-b1ca-f0fb85801c8e" alt=""><figcaption></figcaption></figure>

Give the Action a name, add a description if you wish and for its type, select 'Approval'. When you click 'OK, the Action will be created and added to the Case flow.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FTSAtpTRomKoepRbTpi2M%2Fimage.png?alt=media&#x26;token=320725a9-3f32-40b3-8eb7-37b91705a843" alt=""><figcaption></figcaption></figure>

Once you have added your approval action to your flow, you will then need to fill out its settings.

On the Action Info tab you will need to set when it's due and set an Allocation rule.&#x20;

{% hint style="info" %}
Note that this Allocation should be who the Action should go to to review if the extraction technology is not confident enough in its data extraction results. If the technology you're using is confident enough about its data extraction results, this Action won't even need to be seen by a human user, it will simply be completed automatically and the Case will move on to the next Action.
{% endhint %}

There's also general settings for the Action too, and ability to set a custom card, again only really for use in the unlikely event that someone needs to intervene and view the action in Work Manager.

Next, go to the IDP Document Extraction tab to define the settings which specifically relate to the approval activities.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKDDhkPDPpmDY5UEB2vZ4%2Fimage.png?alt=media&#x26;token=ad2b5918-ab1f-4d32-b8c6-41d614822995" alt=""><figcaption></figcaption></figure>

You'll need to fill in the Extraction Model - this is the ID of the model you want to use for that process.

You'll also need to fill in the input and output tags. The input tag is the tag that the file/document must be tagged with in Work Manager in order to be eligible for document extraction processing and output tags. The output tag is the tag that will be assigned to the file/document in Work Manager once the document extraction process has completed.&#x20;

Once you have filled in the above settings details, set the Case live.
