# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-for-email/enateai-thank-you-email-evaluation.md

# EnateAI - 'Thank You' Email Evaluation

## Overview

Our 'Thank You Email Evaluation' pattern, available in [Marketplace](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace) in Builder automatically detects whether incoming emails to a resolved work are just simple 'thank you emails', and if so then have them automatically moved back to a state of 'resolved' without agent users having to manually perform such repetitive checks. Importantly, the 'Resolved' date of the work item remains as-is, i.e. it is unchanged when EnateAI automatically re-resolves the work item.

Check out this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTcxNzk3MA==>" %}

### Inputs & Outputs

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FRXKVR0Lf2EOYmB6prvyC%2Fimage.png?alt=media&#x26;token=04803e0d-b164-4710-b4fb-2df5c5443da9" alt=""><figcaption></figcaption></figure>

## How does EnateAI 'Thank You' Email Evaluation work at runtime <a href="#how-it-works-at-runtime" id="how-it-works-at-runtime"></a>

In Work Manager, when the AI closes a work item that has been re-opened by a thank you email, the status of the work item will be moved to resolved and a reason of 'updated by integration' will be provided to let the service agent know that the AI carried out this action.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FrDxwj7xJ7ACdyNUXY3Q5%2Fimage.png?alt=media&#x26;token=3a6a7c20-db3f-4bb3-82a9-cbd158dcafe3" alt=""><figcaption></figcaption></figure>

## How to turn on EnateAI 'Thank You' Email Evaluation

EnateAI requires zero configuration by Builder users and they can activate EnateAI 'Thank You' Email Evaluation via the Enate Marketplace using just one click. Activating EnateAI 'Thank You' Email Evaluation will enable it for all mailboxes.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fp1zbEfsdeOaOXj5TYhHZ%2Fimage.png?alt=media&#x26;token=ecbfe255-b00a-457c-8ae2-d2969eb15a00" alt=""><figcaption></figcaption></figure>

Builder users can dis-able 'Thank You' Email Evaluation on a mailbox-by-mailbox basis.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6O6xVpuYqSqBnm34MoH5%2Fimage.png?alt=media&#x26;token=62347a14-757a-4dff-8caf-7492fbbbd3ee" alt=""><figcaption></figcaption></figure>

### How do you set the confidence threshold for EnateAI Document Classification

Builder users can change the confidence threshold via the integrations section of the settings page of Builder.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FykSYFrN2AtxT1nirTTRP%2Fimage.png?alt=media&#x26;token=dfa535fc-79f7-4b39-afd9-8addf89d834f" alt=""><figcaption></figcaption></figure>

### Third party providers

Third party providers of document classification integrations can be found [here](https://docs.enate.net/enate-help/integrations/enate-integrations/auto-evaluate-thank-you-emails-thank-you-email-evaluation).
