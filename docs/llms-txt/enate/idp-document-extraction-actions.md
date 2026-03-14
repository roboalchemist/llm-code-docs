# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/idp-document-extraction-actions.md

# IDP: 'Document Extraction' Actions

## Overview

The Document Extraction component automatically extracts the relevant data from files attached to incoming emails so that this data can be used in further processing of the work item, saving your agents time and effort. This also means that documents such as PDFs can be scanned and used both to start Cases in Enate and to form part of the ongoing process's activities.&#x20;

When a Document Extraction Action runs for a Case, documents attached to the Case can be submitted to your desired technology for scanning and the processed output files will be returned and automatically attached to the Case.

If at any point the technology you're using is not confident enough of the results, based on a confidence threshold that you can set, Enate will instantly transfer the work to an agent in Work Manager to look over and verify, giving you that 'human in the loop' support.

This component can be switched on by your admin in the [Marketplace ](https://docs.enate.net/enate-help/builder/builder-2021.1/integrations-marketplace)section of Enate Builder.

Check out this video to find out more:

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTgwNzUwMw==>" %}

## How it works at runtime

When the Case is run in Work Manager, relevant data from files attached to incoming emails for it will be automatically analyzed and extracted.

If the technology you're using is confident enough about its data extraction results, this Action won't even need to be seen by a human user, it will simply be completed automatically and the Case will move on to the next Action. The completed data extraction Action can still be viewed if you click on it, but it won't need to be handed over to a human user for involvement.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5x5hGES3lDv4IeonVeVS%2Fimage.png?alt=media&#x26;token=d780fad0-e13d-4f09-aab1-92d50045b3b3" alt=""><figcaption></figcaption></figure>

However, if the extraction technology is less confident in its data extraction results, the Action will be handed over to a human user when you next hit 'pull from Queue' in their home page, to pick up and look over. When an agent opens the Action, you'll see that it's been given to them because some further checks are required.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fy9Y9HDnAUp1iAZPBElZt%2Fimage.png?alt=media&#x26;token=2e5fe576-dd63-48da-88af-d5a26e72e880" alt=""><figcaption></figcaption></figure>

To view and validate each document, click on the icon to open, and scroll to the 'validation station' screen in the Action, which shows the scanned document image and the resulting extracted table of data values. This lets you see where those lower confidence levels are highlighted, review them and make any necessary corrections manually. This can viewed in-situ, or expanded out to a popup to display full screen.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FENjWUXcMkUCNFGf5gEq9%2Fimage.png?alt=media&#x26;token=ecc6a608-3dd1-41d1-9b48-a647a6b0f74c" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FEq2V55uyAAiyTKogXKvi%2Fimage.png?alt=media&#x26;token=06749f49-5a26-48fb-8cb8-9a6b4a4676cc" alt=""><figcaption></figcaption></figure>

On this validation screen the agent will be able to see a scanned copy of the file, which can be multiple pages, alongside two tabs showing extracted data.

* The **Extracted Data** tab shows the agent key value pairs of the extracted data along with the confidence level that EnateAI has given them. The values can be adjusted when necessary and are saved once the agent clicks the update button for that value. Doing so will set the confidence value to 100% for that Key.
* The **Tables** tab shows any repeating data that has been picked out as a table. You can use the delete button to delete any rows that you do not need.

#### **Checkbox Data**

**Checkboxes** are recorded within the validation fields. EnateAI for IDP can record complicated **checkbox** questions such as those with multiple answers. The number or letter of **checkbox** will be recorded in the data validation field as well as any text answer that comes with the **checkbox**. See the example below:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fi07bEs95sUCtOiAofGVm%2Fimage.png?alt=media&#x26;token=616a1331-6779-4e1a-a02f-5ca3d7418562" alt=""><figcaption></figcaption></figure>

#### Saving and Submitting

If the agent needs to leave the Validation Station screen at any time they can just click 'Save as Draft' to save their changes for a particular document. &#x20;

{% hint style="info" %}
Note: If an agent enters the validation screen on an Action that is not assigned to them, the data will be in read only mode and can not be edited. To be able to edit the data, the agent must first assign the Action to themselves.
{% endhint %}

Once an agent is happy with the data all they need to do to submit the updated data is to click the 'Submit' button. EnateAI will finish processing in the background, and will update the Action screen to confirm when it's finished. The background processing allows the agent to move on to any other documents which require verification.

Once 'Submit' has been clicked for the last document needing validation, the Action screen auto-closes. Again, EnateAI is finishing processing in the background and will mark the Action as Resolved after a short time, then moved to Closed.

*Note: Every time you review and update data items, EnateAI will learn and get a little bit better at its data extraction suggestions. If you notice that the technology is regularly getting its suggestions wrong, speak to your admin team about modifying the confidence threshold.*&#x20;

### Current Limitations

* Only one document can be viewed at a time.
* The maximum file size is 15 pages.
