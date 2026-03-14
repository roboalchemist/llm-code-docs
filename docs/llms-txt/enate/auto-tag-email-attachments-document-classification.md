# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/auto-tag-email-attachments-document-classification.md

# Auto-tag email attachments - Document Classification

## Overview

The Document Classification component, available in Enate [Marketplace](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace), analyzes the attachments of incoming emails and automatically classifies them with a tag.&#x20;

This provides accurate tagging of the files in your work items without an agent needing to spend time doing this manually, saving time and effort and allowing them to focus on their core activities.

## Infrrd Set Up

There are a few steps to follow when it comes to switching Document Classification component on using Infrrd as yor provider.

1. [Marketplace Setup](#1.-marketplace-setup)
2. [Contract Setup](#2.-contract-setup)
3. [File Tag Setup](#3.-file-tag-setup)

### 1. Marketplace Setup

You'll first need go to the to Marketplace section of Enate Builder and click to activate the Infrrd Document Classification component.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjZn8m5Ivx5a0P6fL7RRV%2Fimage.png?alt=media&#x26;token=6ef691c9-e36a-450a-8a51-4d6183764d20" alt=""><figcaption></figcaption></figure>

In the following pop-up, you'll need to add the URL and account ID of your Infrrd platform.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FgPwGw9vUrI59Df9kFZhi%2Fimage.png?alt=media&#x26;token=9ef0f1a3-0b18-4096-a6cd-4aeb85d433da" alt=""><figcaption></figcaption></figure>

You'll then need to add the model(s) you want to use. To add a model, you'll first need to make sure that it is already configured in your Infrrd platform. You'll then need to enter the following information, all of which can be found in your Infrrd platform:

* Model ID
* Model name
* API key

You can add as many models as you like. These models are what determines how documents get classified. For example, you might have configured a model that is trained to only identify invoices, so that would be the model you would want to use for your invoice processes.

Once you have entered all of the above information, you'll need to test the connection.

Once the connection has been tested successfully, click to activate.

### 2. Contract Setup

Once the adapter is activated, you'll need to make sure that the correct model is used for the right process. This involves adding the model to the contract settings of the desired process.

To do this, go to the Service Matrix and open the contract settings of the desired process.&#x20;

You'll need to fill in the following two settings:

* Document Classification Model -  enter the model you want to use here. You can refresh to view the updated list of models available.
* Allowed File Types for Document Classification - enter the file types you want to be considered for file classification here.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKunxcq1zJBrjEhCVAXcX%2Fimage.png?alt=media&#x26;token=0d3a9707-11f1-456d-a5bc-5b5e68cb1daf" alt=""><figcaption></figcaption></figure>

### 3. File Tag Setup

You'll also need to make sure that all the file tags you might need are set up in the system. This is done from the File Tag section in the System Settings page of Enate Builder.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fzf0VoIp93dNorlFSpiEs%2Fimage.png?alt=media&#x26;token=70331714-f7f4-4ea9-8c7b-1ca7614e1e2c" alt=""><figcaption></figcaption></figure>

You can find more information about [adding and maintaining your file tags here](https://docs.enate.net/enate-help/builder/builder-2021.1/system-wide-settings/file-tags).&#x20;

And you're done.

### Infrrd Document Classification auto creation of file tags

Alongside manually created file tags, whenever the 'Infrrd Document Classification' Integration returns a document with a proposed file tag value, if the value it is proposing is not in the current list of file tags set in Enate, Infrrd will auto-populate the proposed file tag into this list in general settings. Be sure that your process configuration for any downstream actions which are intended to process such documents are set with am 'Input File Tag' whih corresponds with this.

Obviously you're stil in control of the file tags values will be in play in your process set up, since part of training your Infrrd system to recognize the desired type of document e.g. 'Invoice' or 'Payslip'. For more information on how to train Infrrd to recognize documents correctly, please see the following link: [Infrrd Document Classification](https://www.infrrd.ai/blog/understanding-idp-document-classification)
