# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-document-classification.md

# EnateAI - Document Classification

## Overview

The EnateAI Document Classification component, available in Enate [Marketplace](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace), analyzes the attachments of incoming emails and automatically classifies them with a tag.

This provides accurate tagging of the files in your work items without an agent needing to spend time doing this manually, saving time and effort and allowing them to focus on their core activities.

Check out this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTcxNTc4NA==>" %}

Tagging is very helpful to add more structure to your files information, and it opens up further features such as auto-attaching files with certain tags to emails being auto-sent by the system, or into canned response mail sections in emails you're composing. Similarly, file tagging allows external automation routines to know which specific files to pick up from a work item at various points in the process, so it can often be crucial to do this if a file tag is needed later on in the work item's processing.

If at any point EnateAI is not confident of its results, based on a confidence threshold that Builder users can set via the Integrations section of the General Settings page, Enate will highlight this to a service agent in the files tab of a work item for them to look over and complete, giving you that 'human in the loop' support.

A confidence level will be displayed where such automated suggestions of file tag values have been made, so agents can see just how sure the system is in this classification.

When confidence levels are lower, the tag will be highlighted in orange. In this scenario, make sure to confirm it if you agree with the suggested tag in order to set it, or alternatively change it to your preference. Every time you do this, EnateAI will learn and get a little bit better at suggesting the right tag. If you notice that the AI is regularly getting its suggestions wrong, speak to your admin team about modifying the confidence threshold.

EnateAI Document Classification can be switched on by your admin in the Marketplace section of Enate Builder.

## How does EnateAI Document Classification work at runtime <a href="#how-it-works-at-runtime" id="how-it-works-at-runtime"></a>

In Work Manager, when an email comes in for that process with an attachment, if the attachment is of the right file type as defined in the process' contract, it will be analyzed and automatically classified with a tag by EnateAI.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUFxKElG3DrOWljAg4lDO%2Fimage.png?alt=media&#x26;token=b323ab38-4ea0-42e4-b2c9-6470a9e4de64" alt=""><figcaption></figcaption></figure>

A confidence level will be displayed where such automated suggestions of file tag values have been made, so agents can see just how sure the system is in this classification.

When confidence levels are lower, the tag will be highlighted in orange.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F075yRYiBzDMULrSohNlJ%2Fimage.png?alt=media&#x26;token=66dbe12a-6bb3-429a-a240-cb30941a592b" alt=""><figcaption></figcaption></figure>

In this scenario, make sure to confirm it if you agree with the suggested tag in order to set it, or alternatively change it to your preference.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmZdQ7n8Wm3VF5bYJTDOZ%2Fimage.png?alt=media&#x26;token=7a01a504-46f6-49be-b598-e9be277f54cd" alt=""><figcaption></figcaption></figure>

If you notice that the technology is regularly getting its suggestions wrong, speak to your admin team about modifying the confidence threshold.

It should be noted that even when the AI is confident of its decision, the user can still click to expand the tag to see the details and reject the AI's decision.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FGb7KI1u2noEGTlylh0r2%2Fimage.png?alt=media&#x26;token=6c78253d-514d-48c3-b178-3f17b24ef772" alt=""><figcaption></figcaption></figure>

## How to turn on EnateAI Document Classification

EnateAI requires zero configuration by Builder users and they can activate EnateAI Document Classification via the Enate Marketplace using just one click. Activating EnateAI Document Classification will enable it for all mailboxes.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fic2ZgPuKzwZhe0J7TktJ%2Fimage.png?alt=media&#x26;token=b105adcd-3b9f-46cb-8c15-af4cf3b5f890" alt=""><figcaption></figcaption></figure>

Then at the contract level of a business process select the EnateAI Classification model.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjNItQ44DbIK7JirP9pyJ%2Fimage.png?alt=media&#x26;token=4783e1dd-92d9-4c61-b19d-46a9b6740727" alt=""><figcaption></figcaption></figure>

Underneath the Document Classification Model drop down, you have the option to specify what files types are to be allowed for document classification.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6Quw08ZLFyecZdFLLmeM%2Fimage.png?alt=media&#x26;token=cf5fbd82-2e1c-49be-926d-d73ae63d6385" alt=""><figcaption></figcaption></figure>

### How do you set the confidence threshold for EnateAI Document Classification

Builder users can change the confidence threshold via the integrations section of the settings page of Builder.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FhYoxqqdl02LC1V6SKvna%2Fimage.png?alt=media&#x26;token=4f241d97-f992-4bbd-8780-3ec8bd0fb8af" alt=""><figcaption></figcaption></figure>

### Third party providers

Third party providers of document classification integrations can be found [here](https://docs.enate.net/enate-help/integrations/enate-integrations/auto-tag-email-attachments-document-classification).
