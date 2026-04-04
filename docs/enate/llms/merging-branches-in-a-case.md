# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/merging-branches-in-a-case.md

# Merging Branches in a Case

## Overview

You can merge branches in your Case workflow processes to help you streamline the creation of your business Case flows.&#x20;

Sometimes creating a business process can leave you with many different routes that you want to lead onto the same action depending on the criteria of the step. By using this new merge feature you will be able to choose different Actions to end in the same outcome.&#x20;

Watch the following video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTM1Mjg5OQ==>" %}

## How to merge branches

You can choose to merge together parallel branches or conditional branches.&#x20;

To merge multiple Actions together, click on the menu of one of the Actions you want to merge and select 'Merge', then 'Add'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnuSJmP3tWci2jOD8EEuK%2Fimage.png?alt=media&#x26;token=58120e9d-8e0f-422f-b7da-132cff4c4ea6" alt=""><figcaption></figcaption></figure>

In the following pop-up select the other Actions you want to merge it with from the list of Actions that are available for merging.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJhq38Y2oJ3RJEtnqfy3q%2Fimage.png?alt=media&#x26;token=92ee4b73-35ba-4392-8ade-6caaed1a57af" alt=""><figcaption></figcaption></figure>

Then select which Action you want them to be merged into - you can either choose from an existing Action type or you can choose to create a brand new Action type for this.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FzrfkGzLw5RWaz6apZeTS%2Fimage.png?alt=media&#x26;token=07fb07d6-26a4-4222-b2f0-a8703a5b5b88" alt=""><figcaption></figcaption></figure>

The merged Action will then appear in the flow.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBvOvl1P44Ac1NiCjLP6H%2Fimage.png?alt=media&#x26;token=8158ef7f-9061-41e4-9dd1-b123a306aee0" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note that you can only merge together Actions within the same step.
{% endhint %}

## Specifics of merging parallel branches

If you are merging together Actions from parallel branches, the merge Action will wait for **all** of its the predecessor Action to complete before it can start.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtZBpV22HZFxsjctJsaB4%2Fimage.png?alt=media&#x26;token=49e43684-4041-436e-9ede-5c656afad60f" alt=""><figcaption></figcaption></figure>

## Specifics of merging conditional branches

If you are merging together Actions from conditional branches, the merge Action will start when **one** of the conditional branches has been completed.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FLfnumZjdT4bR0weLWFRK%2Fimage.png?alt=media&#x26;token=822c1f16-44fd-4e03-90da-abf3990aa286" alt=""><figcaption></figcaption></figure>
