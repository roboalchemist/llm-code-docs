# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-for-idp-document-extraction.md

# EnateAI for IDP - Document Extraction

### What does this AI Pattern do?

The EnateAI Document Extraction component automatically extracts the relevant data from the Files attached to incoming emails, so that this data can be used in further processing of the work item, saving your agents time and effort. Documents such as PDFs can be scanned and used both to start Cases in Enate and to form part of the ongoing process's activities.

{% embed url="<https://enate.cdn.spotlightr.com/watch/MTU0MzQwNQ==>" %}

When a Document Extraction Action runs for a Case, documents attached to the Case can be submitted to EnateAI for scanning, and processed JSON output files will be returned and automatically attached to the Case. The JSON files give you a structured breakout of data from within these documents, allowing for much easier and slicker downstream processing by further external systems and technologies.

If at any point EnateAI is not confident enough of the results, based on a [confidence threshold that you can set](https://docs.enate.net/enate-help/enateai/enateai/set-confidence-thresholds-for-your-ai-integrations), Enate will instantly transfer the work to an agent in Work Manager to look over and verify, giving you that 'human in the loop' support.

### Inputs & Outputs

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FLGlB2VNSDCcPDvSd7BeJ%2FDocument%20Data%20Extraction.png?alt=media&#x26;token=4724c382-b1a1-4e9b-94d9-0cd0ea904947" alt=""><figcaption></figcaption></figure>

## How does EnateAI Document Extraction work at runtime? <a href="#how-does-enateai-document-extraction-work-at-runtime" id="how-does-enateai-document-extraction-work-at-runtime"></a>

When a case is started in Enate by an incoming email with files attached, the agent can assign Tags to the individual files (or you can use EnateAI's Document Classification integration to have the system do this for you automatically). Once this is done, the case can move onto an **EnateAI Document Data Extraction Action** which has been set in the case flow.

The action will process all files that are tagged with the tags it has been configured to pick up. Once processed, if EnateAI is confident in its extraction results, the action will continue to the next point in the case flow, without the agent needing to intervene. A JSON output file of the extracted data (in a structured format) gets attached to the case, and the action will close automatically. Agents can still click to view the Action if they wish to, which will show the completed document extraction(s) and any output JSON files in the 'Files' tab.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FB1oSSYdvDfSO9wbtrTtN%2Fimage.avif?alt=media&#x26;token=712bfb59-36d2-4e3d-9ecd-c80602564fc5" alt=""><figcaption></figcaption></figure>

## Agents can verify when AI isn't confident enough - 'Validation Station' screen <a href="#agents-can-verify-when-ai-isnt-confident-enough-validation-station-screen" id="agents-can-verify-when-ai-isnt-confident-enough-validation-station-screen"></a>

If EnateAI confidence in its data extraction result drops below the designated threshold, the system will automatically set the action to be picked up by a human agent to process. When the agent opens the action they will see that it is in a state of 'To Do' - any documents needing their input will be marked with 'Requires verification'.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FmGzgb2E0ED2FvpyUBp7A%2Fimage.avif?alt=media&#x26;token=2a43505f-944a-44f0-86db-a9bd4b572680" alt=""><figcaption></figcaption></figure>

To verify the problem files the agent just needs to click the icon to open, and scroll to the EnateAI Validation Station screen to review and amend contents.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fm2ZrQJqLKtVz0X66yI55%2Fimage.png?alt=media&#x26;token=df434b14-5621-4493-9558-832def19e0f2" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: Only one document can be viewed at a time.
{% endhint %}

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FvofjYOgIHmeQ82VQ07ns%2Fimage.png?alt=media&#x26;token=5439358a-6b41-4e6c-a90a-335148e59b23" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FVLVLbiqbwqTfAzPqifff%2Fimage.png?alt=media&#x26;token=53a7f07e-8323-4f48-8f3b-ea5955e4bd76" alt=""><figcaption></figcaption></figure>

On this validation screen the agent will be able to see a scanned copy of the file, which can be multiple pages, alongside two tabs showing extracted data.

* The **Extracted Data** tab shows the agent key value pairs of the extracted data along with the confidence level that EnateAI has given them. The values can be adjusted when necessary and are saved once the agent clicks the update button for that value. Doing so will set the confidence value to 100% for that Key.
* The **Tables** tab shows any repeating data that has been picked out as a table. You can use the delete button to delete any rows that you do not need.

#### **Checkbox Data**

**Checkboxes** are recorded within the validation fields. EnateAI for IDP can record complicated **checkbox** questions such as those with multiple answers. The number or letter of **checkbox** will be recorded in the data validation field as well as any text answer that comes with the **checkbox**. See the example below:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FuBoATXaUgQ7efxNtF4F4%2Fimage.png?alt=media&#x26;token=c86e79f6-b30a-4384-818c-74efc00e6385" alt=""><figcaption></figcaption></figure>

#### Saving and Submitting

If the agent needs to leave the Validation Station screen at any time they can just click 'Save as Draft' to save their changes. The background processing allows the agent to move on to any other documents which require verification.

Once an agent is happy with the data all they need to do to submit the updated data is to click the 'Submit' button. EnateAI for IDP will finish processing in the background, and will update the Action screen when it's finished.

Once 'Submit' has been clicked for the last document needing validation, the Action screen auto-closes. Again, EnateAI for IDP is finishing processing in the background and will mark the Action as Resolved after a short time, then moved to Closed.

{% hint style="info" %}
Note: If an agent enters the validation screen on an Action that is not assigned to them, the data will be in read only mode and can not be edited. To be able to edit the data, the agent must first assign the Action to themselves.
{% endhint %}

### How to Activate EnateAI for Document Extraction in Marketplace <a href="#how-to-activate-enateai-for-document-extraction-in-marketplace" id="how-to-activate-enateai-for-document-extraction-in-marketplace"></a>

To activate the EnateAI Document Extraction component, Builder users navigate to the Enate Marketplace, use the filters (Provider and/or Category) to find the component and then click to activate. This will instantly activate the component without the need to input any additional keys as would be needed with similar integrations provided by external technologies.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FUEjgsNvwp3LXCg6RQC7r%2Fimage.avif?alt=media&#x26;token=5cd4a0af-74c1-4c02-a0aa-da86d0a193ba" alt=""><figcaption></figcaption></figure>

### How to configure EnateAI for Document Extraction Actions into your Cases <a href="#how-to-configure-enateai-for-document-extraction-actions-into-your-cases" id="how-to-configure-enateai-for-document-extraction-actions-into-your-cases"></a>

You can then add 'IDP Data Extraction' Actions into your desired Case flows in Builder. You can either add an existing one from the Actions list if one has already been created, or you can create a brand new one. To create an IDP Document Extraction Action in a Case, from the Action selection drop-down select to create a new Action.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FHXMYG5YV74amQ92Oblkv%2Fimage.avif?alt=media&#x26;token=a9cf4fa8-f076-4c10-901c-c707ec910db2" alt=""><figcaption></figcaption></figure>

Give the Action a name, add a description if you wish and for its type, select 'IDP Data Extraction Action'. When you click 'OK, the Action will be created and added to the Case flow.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FPnvtCCng5IT5mXproJfj%2Fimage.png?alt=media&#x26;token=7350bfe2-7682-416e-ad14-ea42ad29dbba" alt=""><figcaption></figcaption></figure>

On the Action Info tab you will need to set when it's due and set an Allocation rule (i.e. where to route the Action if it needs to be manually reviewed by an Agent when the technology's confidence levels aren't high enough).

There's also general settings for the Action too, and ability to set a custom card, again only really for use in the unlikely event that someone needs to intervene and view the action in Work Manager - though remember that the Validation Station screen will automatically show in such circumstances.

Next, go to the 'IDP Document Extraction tab' for the Action to define the settings which specifically relate to the approval activities.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FB9pv1ZWxWz1bu8FfgmTo%2Fimage.png?alt=media&#x26;token=69bfcac9-8e05-454d-8b56-5e3f12b94a68" alt=""><figcaption></figcaption></figure>

You'll need to fill in:

* **The Extraction Model** - this is the ID of the model you want to use for that process. See this section for more information on Extraction Models.
* **The Input File Tag -** the tag that the document must be tagged with in order for the Action to pick it up and perform data extraction on it. For example, setting this to 'Invoice' will ensure that only files tagged as 'Invoice' will be picked up. All other documents will be ignored by the Action.
* **The Output File Tag** - the tag that the Action will assign to the file once the document extraction process has completed. For example, you may want to set a value of 'Processed' for any documents will have been picked up.

Once you have filled in the above settings details, you can set the Case live and you'll now have automatic document data extraction working on your Case process.

### Extraction Models Available <a href="#extraction-models-available" id="extraction-models-available"></a>

EnateAI offers a range of extraction models to use when configuring your IDP Document Extraction action.

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FhGbfd9PdHZlHOoT3EmQn%2Fimage.png?alt=media&#x26;token=ecfd321c-0275-432c-8409-1b5262f5bfcd" alt=""><figcaption></figcaption></figure>

The current Extraction Models available are:

* **General**
* **Insurance Surrender**
* **Invoice**

All of these Extraction Models come from [**Azure's official list of pre-trained models**](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0) ensuring an industry standard. More of Azure's pre-trained models will be made available for users of EnateAI in coming releases. If you wish to investigate these extraction models further, follow the link to Azure's official documentation.

### What File Types are supported in IDP

All IDP integrations only accept PDF, PNG and JPG file types. All other file types are not supported in IDP.

### Current Limitations

* Only one document can be viewed at a time.
* The maximum file size is 15 pages.

### Third party providers <a href="#other-providers" id="other-providers"></a>

Third party providers of document classification integrations can be found [here](https://docs.enate.net/enate-help/integrations/enate-integrations/auto-extract-document-data-document-extraction).
