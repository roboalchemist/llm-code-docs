# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-for-email/enate-ai-email-classification.md

# Enate AI - Email Classification

## Overview

Our email classification pattern, available in [Marketplace](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace) in Builder enables the automatic classification and categorization of Tickets, without agents having to do this manually so that by the time an agent picks a Ticket it up, it's already where it needs to be.

Check out this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTcxNTc5MA==>" %}

### Inputs & Outputs

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FeyFaKCjiNKPSAVTlP6tf%2FEmail%20Classification.png?alt=media&#x26;token=2bb5cea3-18f0-41f7-8850-c3f9baf0e29e" alt=""><figcaption></figcaption></figure>

## How does EnateAI Email Classification work at runtime <a href="#how-it-works-at-runtime" id="how-it-works-at-runtime"></a>

When EnateAI Email Classification is active it will read the subject line and contents of incoming emails and then categorize them correctly to start a new Ticket.

In the settings card of the Ticket, you will be able to see which category the AI has selected for the Ticket as well as the confidence level of the AI.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FDoMl3vB2CgRUoY2WAVXL%2Fimage.png?alt=media&#x26;token=79fd4dc2-2dbf-4b76-8235-46c22af4b921" alt=""><figcaption></figcaption></figure>

If the AI's confidence falls below the threshold level, then highlight this to the service agent and ask them to either edit the category or accept it.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F3QgXYDqkmrcmSD6OBPrH%2Fimage.png?alt=media&#x26;token=b56b9246-ba67-411d-8453-e41a19407c93" alt=""><figcaption></figcaption></figure>

Even if the AI is 100% sure, the service agent will always have the ability to edit the category if they wish.

## How to turn on EnateAI Email Classification

EnateAI requires zero configuration by Builder users and they can activate EnateAI Email Classification via the Enate Marketplace using just one click. Activating EnateAI Email Classification will enable it for all mailboxes.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FfMpYIjIG3qYuEzGjIc6K%2Fimage.png?alt=media&#x26;token=b58d1eb5-051d-410e-9ea0-1bae94e64472" alt=""><figcaption></figcaption></figure>

Builder users can dis-able Email Classification on a mailbox-by-mailbox basis.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FgqsIXWAMaOvoZjVnBJ53%2Fimage.png?alt=media&#x26;token=8acecec1-c6ec-47b7-bf49-cea8fdfcc58f" alt=""><figcaption></figcaption></figure>

### How do you set the confidence threshold for EnateAI Document Classification

Builder users can change the confidence threshold via the integrations section of the settings page of Builder.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJ7UQfKlrIBDEEX4q0mQc%2Fimage.png?alt=media&#x26;token=230c19b4-6f9b-4cda-85d7-0e82935d75ce" alt=""><figcaption></figcaption></figure>

### Third party providers

Third party providers of document classification integrations can be found [here](https://docs.enate.net/enate-help/integrations/enate-integrations/auto-classify-emails-email-classification).
