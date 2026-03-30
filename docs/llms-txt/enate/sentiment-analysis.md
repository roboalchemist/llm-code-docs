# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-for-email/sentiment-analysis.md

# Enate AI Sentiment Analysis

## Overview

Our sentiment analysis pattern, available in [Marketplace](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace) in Builder enables the analysis of the content of incoming emails and determine if, for example, they are positive or negative. This assessment can be passed back into Enate Work Manager so that Agents can tell at a glance what the tone of the mail is as headline information as they start to deal with it.

Check out this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTcxNjIwNw==>" %}

### Inputs & Outputs

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVCfxwpx41UKy8OevE7Im%2FEmail%20Sentiment%20Analysis.png?alt=media&#x26;token=c676fba4-0919-4d62-b697-a9e8b9c6cbbf" alt=""><figcaption></figcaption></figure>

## How does EnateAI Sentiment Analysis work at runtime <a href="#how-it-works-at-runtime" id="how-it-works-at-runtime"></a>

When EnateAI Sentiment Analysis is active it will read incoming emails and highlight their sentiment using a traffic light system.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fme3Wv14kmvpXrQh1K4Bp%2Fimage.png?alt=media&#x26;token=575af21a-d509-4d35-b883-bf2d5125c955" alt=""><figcaption><p>Positive Sentiment</p></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FaK9VyirFPsMSytZqW203%2Fimage.png?alt=media&#x26;token=791f0f0d-d32b-45f3-a4e4-2805330c491e" alt=""><figcaption><p>Neutral sentiment</p></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F4svyiN3CvGxFmqbM6Do7%2Fimage.png?alt=media&#x26;token=7446fdc3-ffbc-4ee6-9983-af7f1ddf3c1b" alt=""><figcaption><p>Negative sentiment</p></figcaption></figure>

If you hover over a sentiment marker on an email the confidence score of the AI will be displayed.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FKWPjAQVoMwifrkUFWZ22%2Fimage.png?alt=media&#x26;token=4541d86b-1c08-4e44-9044-7fbd7b5dfe2d" alt=""><figcaption></figcaption></figure>

## How to turn on EnateAI Sentiment Analysis

EnateAI requires zero configuration by Builder users and they can activate EnateAI Sentiment Analysis via the Enate Marketplace using just one click. Activating EnateAI Sentiment Analysis will enable it for all mailboxes.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FjpWj9ces7axaaX0vmPXL%2Fimage.png?alt=media&#x26;token=38d638de-3d85-43d6-8d68-467625455c34" alt=""><figcaption></figcaption></figure>

Builder users can dis-able Sentiment Analysis on a mailbox-by-mailbox basis.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F6U8uzk7lYsNjKGqKrOH2%2Fimage.png?alt=media&#x26;token=5e02f620-6000-4dee-af0c-6c569edd8cce" alt=""><figcaption></figcaption></figure>

### Known Issue -&#x20;

Please note that there is a known issue with Microsoft 365 Graph API for Outlook, which affects its ability to identify out of office emails, which are normally ignored for Sentiment Analysis.

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtVI1PqQoIvFeXGcbaVnM%2FOffice%20365%20Graph%20API%20Known%20Issue.pdf?alt=media&token=c540e84d-b425-4ff0-a9e0-40faa48f2e25>" %}

### Third party providers

Third party providers of document classification integrations can be found [here](https://docs.enate.net/enate-help/integrations/enate-integrations/analyse-sentiment-in-emails-sentiment-analysis).
