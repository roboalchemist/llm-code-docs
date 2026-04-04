# Source: https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/upload-content.md

# Upload content

You can ingest the following types of documents in the `LLaMB Content` skill:

* URL - Publicly accessible HTML content
* CSV (Comma-separated values)
* Microsoft Word document (docx)
* Microsoft PowerPoint (pptx)
* Microsoft Excel (xlsx)
* HTML documents (html, htm)

{% hint style="info" %}
**Note:** You can also ingest your articles or documents using the DataSync feature. Refer [DataSync](https://docs.avaamo.com/user-guide/datasync-ai), for for more information.
{% endhint %}

To upload content, you must first decide which document group you want to add the content to. See [Create Document Groups](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/create-document-groups) for more information on document groups.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3wxbPGsPJDPAzhISHNAG%2FScreenshot%2013-01-2025%20at%2017.24.png?alt=media&#x26;token=448941e6-2fc3-4318-b86f-ebc6e4896db2" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can manage a skill immediately after creating the skill. See [Create LLaMB skill](https://docs.avaamo.com/user-guide/llamb/get-started/step-1-create-llamb-content-skill), for more information.
* If you wish to edit skills in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click Edit to unlock the agent before editing.
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

You can use the `Status` dropdown on the right side of the page to filter the documents based on the document upload status. Along with the status, you can also view the document count for each status in the dropdown. This feature helps when you have a large set of documents uploaded to a document group and want to view only the errored documents in the group.

### **Upload Documents**

* Choose the document group to which you want to add documents. Click the `Document group` to open it.
* Click `Add Documents`**.**
* Click `Select Files` to upload documents. You can upload multiple documents at a time.
* Add a `Preview URL` - Indicates the URL that is opened when the user clicks [Citation links](https://docs.avaamo.com/user-guide/llamb/citation-links) in the response. This field is optional.
* `Auto language detection toggle:` Allows you to enable or disable automatic detection of the uploaded document’s language.
* `Language selection`**:** If you turn off auto-detection, you can manually select the document’s language from a dropdown. The dropdown displays all [languages configured](https://docs.avaamo.com/user-guide/configuration/language) for the agent, allowing accurate classification of the uploaded document.
* Click `Import`. The Avaamo Platform extracts content from the specified documents to seamlessly create a knowledge base. You can view the upload status for each document in the [Status](#document-status) column.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FRaoNjm5g8iqCYgrNjVZP%2FScreenshot%202025-11-19%20at%205.40.17%E2%80%AFPM.png?alt=media&#x26;token=e9259298-23b7-4ecf-a784-e047264f3f4b" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
**Key Points**:&#x20;

* Avoid documents with too many graphics as those are ignored.
* PDFs must have permission to read from and write to and must not be access-controlled or password-protected.
* All text captured in a single knowledge base must be under 2 MB in base Unicode representation.
  {% endhint %}

### **Upload from URL**

* Choose the document group to which you want to upload content from a URL. Click on the document group to open it.
* Click `Add URL`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXSIQfKuIYXowbBTQgGaR%2Fimage.png?alt=media&#x26;token=4f563ad2-7a48-426a-bf16-49d69b159d52" alt=""><figcaption></figcaption></figure>

* Specify the following details:
  1. **URL:** The URL from which content is to be uploaded.
  2. **Title:** Name/title for this content - to identify it.
  3. **Language**: The language of the content.
  4. **Template:** The template used for parsing the content. For URLs, is always an HTML document.
  5. **Attributes**: Attributes associated with the content. Attributes allow you to personalize responses based on the user properties. See [Document attributes](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/document-attributes), for more information.
* Click `Create`. The content from the specified URL is extracted by the Avaamo Platform to create a knowledge base seamlessly. You can view the status of the upload for each document in the `Documents` tab. You can view the status of the upload for each document in the [Status](#document-status) column.&#x20;

{% hint style="success" %}
**Key Points**:

* It is recommended to use the Content Ingestion APIs to upload multiple URLs. See [Content Ingestion API](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/answers-rest-apis/content-ingestion-apis-recommended), for more information.
* Only the specific page in the URL is uploaded. Content from links to other pages or websites is not uploaded.
* URL must not redirect to an authorization page.
* URL must allow cross-origin from the Avaamo Platform.
* URL must not include assets like PDFs, Docx. If you wish to process asset-type documents (PDFs), then you can upload them as documents instead of URLs.
* Avoid pages with browser-window popups.
* All the text captured in one knowledge base must be under 2 MB in base Unicode representation.
  {% endhint %}

### Upload from API

You can also upload content using Content ingestion APIs. This allows you to set up a pipeline to ingest the content from any external system seamlessly. See [Content Ingestion API](https://docs.avaamo.com/user-guide/llamb/llamb-rest-apis/content-ingestion-apis), for more information.

### Upload using DataSync

You can upload content using DataSync, which offers flexibility by allowing ingestion from various sources, such as `SharePoint, Websites, files,` and `ServiceNow`. Users can choose from these sources to integrate relevant content into their LLaMB skill, enhancing the versatility and adaptability of their content management workflows. See [DataSync AI](https://docs.avaamo.com/user-guide/datasync-ai), for more information.

### Document status

The `Status` can be any of the following values based on the status of the uploaded content:&#x20;

* **Uploaded:** The document has been added to the skill.
* **Queued:** The content is placed in a queue for further processing.
* **Extracting**: Chunks of content are being extracted.
* **Learning:** Acronyms and vocabulary are being generated.
* **Complete**: The document is uploaded successfully. The extracted knowledge from the document has been populated and is ready for use by any agent. See [View and Edit Knowledge](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/view-and-edit-knowledge), for more information.
* **Error**: The upload failed. In case of errors, you can click `Error` in the `Status` column to view more details. See [Troubleshooting tips](https://docs.avaamo.com/user-guide/llamb/troubleshooting-tips), for more information.
* **Warning:** No business vocabulary was found in the document.

### Next Steps

After successfully ingesting the content, your agent is ready for testing. See [Test your agent](https://docs.avaamo.com/user-guide/llamb/get-started/step-3-test-your-agent), for more information. You can continue to fine-tune and edit the knowledge base based on the user conversation history. See [View and Edit Knowledge](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/view-and-edit-knowledge), for more information.

You can also perform specific actions on the knowledge base such as retraining, editing the uploaded documents or URLs, or deleting the documents or URLs from the knowledge base, as required. See [Common actions](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/common-actions), for more information.
