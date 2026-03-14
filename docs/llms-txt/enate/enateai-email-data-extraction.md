# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-for-email/enateai-email-data-extraction.md

# EnateAI - Email Data Extraction

## Overview

Our 'Email Data Extraction' pattern, available in [Marketplace](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace) in Builder auto-populates important information from emails into custom cards in your Tickets and Cases, saving agents from having to do this manually.

Check out this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTcxNzUwNA==>" %}

### Inputs & Outputs

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJTTdVoOVmF1pIqTjTsGG%2FEmail%20Data%20Exraction.png?alt=media&#x26;token=ad6ba6c7-3d9d-4145-8d07-5559a538b7a2" alt=""><figcaption></figcaption></figure>

Note: Although ticket category information *is* passed through to the AI, the adapter does not currently make use of this information.

## How does EnateAI Email Data Extraction work at runtime <a href="#how-it-works-at-runtime" id="how-it-works-at-runtime"></a>

When EnateAI Email Data Extraction is active it will read the contents incoming emails, analyze it, compare it to the data fields in the custom card for the work item it is creating and then auto-populate the card with the relevant data.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJ9b1Hy10pgDLAjjdPwIz%2Fimage.png?alt=media&#x26;token=c9230eca-9f37-4ea3-9f2a-d68e443d66d6" alt=""><figcaption></figcaption></figure>

## Configuring Custom Data Fields for Email Data Extraction

When you are configuring the custom data fields which are going to be auto-populated in a Work Item card by EnateAI Email Data Extraction, there are some important things to keep in mind to help optimize the effectiveness of the auto-population:&#x20;

1. When trying to find a match in the email for the fields in the work item, the AI will use the *safename* of the data field rather than the display name.&#x20;
2. This safename does not have to be an *exact* match to text in the email body to be selected - as long as it's similar the AI should be able to find it. Think of it in the same way that if a human agent could work out what data the safename is asking for from the email, the AI should be able to work this out too. So when your creating (and naming) your data fields, aim for a safename that is likely to match text that will appear in the mail. Avoid abstracted or 'code-type' naming that has little relation to the texts the AI will be looking for in incoming mails.
3. The following types of content in incoming email text are currently NOT supported with Email Data extraction:

   1. Check boxes\*
   2. Currency
   3. Repeating rows of data (i.e. ones that would equate to Table fields in Enate)&#x20;
   4. Multi-Level Lists

   \*The AI model does not support data extraction from check boxes within the email body if you've used a 'check box' data type for your custom data field. However, if you configure a 'List' type data field (with appropriate value options in the list!) to collect data from a check box question within the email, the AI should be able to accurately extract the check box data value and populate the list.
4. While the email extraction AI does have a high accuracy rate for all custom data types that it works with, there are some data types where there’s variation on how it may appear on an incoming email, and this can sometime affect accuracy of extraction. Date fields is a good example of this, given the number of different date formats that exist.

### Email Data Extraction Example

Let's have a look at an incoming email and the custom card on its resulting work item to see some examples of custom data fields that have been filled in by the AI with extracted data.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZE9sMNYUcQ7QBgcR7WSW%2Fimage.png?alt=media&#x26;token=9062e468-10e2-434b-a846-0b3c026d2534" alt=""><figcaption></figcaption></figure>

We can see that the AI has successfully extracted the first and last name of the sender just from using the text at the end of the email where the sender has signed off. The address and email address have also been similarly extracted without either being presented in a structured format in the email stating that the address is the sender's address or that the email is their email.&#x20;

The number of software packages that the sender is looking to purchase (500) has been extracted from within a continuance sentence within the email, again demonstrating that the AI is able to extract the required data without the sender having to structure the email in a way so that it exactly matches the name of the custom data field.

The last two data fields on the custom card are handling the two check box questions on the email, asking whether the request is urgent and if it has been approved by senior management. Due to the current AI model not supporting check box type data fields, the two data fields to capture this in Enate have been configured as List type fields, and are able to pick up these check box answers correctly. Additionally, we can see that even though the names of these two custom data fields do not match the questions of the check boxes exactly, the AI has still been able to correctly identify and extract the data.

### Example showing non-supported content

Let us now look at an example where an email has come in and, alongside mail content which the AI *can* deal with, there are examples of the kind of content which it currently *cannot* deal with, specifically: Check boxes\*; Currency; Repeating rows of data; and Multi-Level Lists.\
\*EnateAI can deal with checkbox content if you a 'List' type field to store the data.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FFgD9fdaT6DIwG0SIMjc6%2Fimage.png?alt=media&#x26;token=6fc2a42d-d08b-4e8c-bbb6-e7e2630d3ad8" alt=""><figcaption></figcaption></figure>

We can see in the card below from the resulting work item that we have a currency field, a check box field, a multi-level list field and a table. As extraction of the kind of mail content that would relate to field types like this is currently not supported by the AI, it has failed to extract any of the relevant data automatically, and this content would still have to be manually transposed onto card.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FABYkKCMw7JmXi1Cb95oU%2Fimage.png?alt=media&#x26;token=51d0d240-31a7-4775-b99e-5690383b401f" alt=""><figcaption></figcaption></figure>

Potential approaches to minimize the amount of data not extracted:

* A field of type 'Text' could be used to support extraction of the currency data.&#x20;
* A field of type 'List' could be used to support extraction of the check box information.

## How to turn on EnateAI Email Data Extraction

EnateAI requires zero configuration by Builder users and they can activate EnateAI 'Email Data Extraction' integration via the Enate Marketplace using just one click. Activating EnateAI 'Email Data Extraction' will enable the integration for all mailboxes.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fc29lZ1CajSj53xaVMyZ6%2Fimage.png?alt=media&#x26;token=38ee9ef4-b247-44d2-9ef4-b219640f3f22" alt=""><figcaption></figcaption></figure>

Builder users can disable Email Data Extraction on a mailbox-by-mailbox basis. This can be adjusted in the configuration 'Integrations' settings for an email [connector](https://docs.enate.net/enate-help/enateai/enateai/enateai-for-email/email-connector-level-control-over-email-integrations).

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FQK8aMAHEWWWijSMzODYY%2Fimage.png?alt=media&#x26;token=1ab45fe8-48e7-4880-af23-4c00fb632d81" alt=""><figcaption></figcaption></figure>

### Third party providers

Third party providers of document classification integrations can be found [here](https://docs.enate.net/enate-help/integrations/enate-integrations/auto-populate-custom-cards-with-email-info-email-data-extraction).
