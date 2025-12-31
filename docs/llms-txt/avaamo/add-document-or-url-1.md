# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/add-document-or-url-1.md

# Upload Content

Content is added to Document Groups. To upload content, you must first decide which document group you want to add the content to. See [Create Document Groups](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/create-document-groups) for more information on document groups.

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).
* You can manage a skill immediately after creating the skill. See [Create new Answers skill](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/create-new-knowledge-base), for more information.
* If you wish to edit skill in an agent, then:
  * Navigate to the Agents tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click Edit to unlock the agent before editing.
  * In the Agent page, navigate to the Skills option in the left navigation menu. Search and open the required skill.&#x20;
    {% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FgZRpetvzq4kTZKvGFKTV%2F6.4-answers-document-group.png?alt=media&#x26;token=22eef552-a2ae-4a7d-bb64-76244a8d6611" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note**: You can use the **Status** dropdown in the right side of the page to filter the documents based on the document upload status. Along with the status, you can also view the count of documents for each status in the dropdown. This feature helps when you have a large set of documents uploaded in a document group and say you wish to view only errored-out documents in the group.
{% endhint %}

### **To upload Documents**

* Choose the document group to which you want to add documents. Click on the document group to open it.
* Click **Add Documents.**
* Click **Select Files** to upload documents. You can upload multiple documents at a time.
* Click Import and choose the following for each file:
  * **Language**: Choose the language of the document. By default, the language is set to English. You can upload documents in any language as long as the language is configured or added to your agent. See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information on adding languages to your agent. See [Multi-lingual answering](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/multilingual-answering), for more information.
  * **File Format**: For a pdf file, based on the way the file is formatted, pick the closest option from the following:
    * **Indexed Section**: Choose this if the PDF document format is in the form of sections such as 1, 1.1, 1.2, 1.3,.....
    * **Chapters, Articles, Sections, Appendices**: Choose this if the PDF document format is in the form of Chapters, Articles, Sections, Appendices such as Chapter 1, Section 1.2,...
    * **Font based hierarchy, example**: Choose this if the format of the information in the PDF document is based on the font style.
    * **Hierarchy in the form..**: Select this format if the PDF document format is in the form of roman letters, numbers, and alphabet bullet points.
* Click **Import**. The content from the specified documents is extracted by the Avaamo Platform to seamlessly create a knowledge base. You can view the status of the upload for each document in the Status column. The following status values are displayed:

  * **Uploaded:** The document has been added to the skill.
  * **Queued:** The content is placed in a queue for further processing.
  * **Extracting**: Chunks of content is being extracted.
  * **Learning:** Entities, acronyms, vocabulary and knowledge graph are being generated.
  * **Complete**: The document is uploaded successfully. Extracted knowledge from the document is populated and is ready to be used by any agent. See [View and Edit Knowledge](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/view-and-edit-knowledge), for more information.
  * **Error**: The upload has errored out. In case of errors, you can click Error in the Status column to view more details. See [Debug Answers](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/troubleshooting-tips), for more information.
  * **Warning:** No business vocabulary was found for the document.

{% hint style="success" %}
**Key Points**:&#x20;

* Avoid documents with too many graphics as those are ignored.
* PDFs must have permission to read-from and write-to and must not be access-controlled or password-protected.
* All the text captured in one knowledge base must be under 2 MB in base Unicode representation.
* Avaamo Answers supports uploading Word documents with `.docx` extension only.
  {% endhint %}

### **To upload from URL**

* Choose the document group to which you want to upload content from a URL. Click on the document group to open it.
* Click **Add URL**.
* Specify the following details:
  1. **URL:** The URL from which content is to be uploaded.
  2. **Title:** Name/title for this content - to identify it.
  3. **Language**: The language of the content.
  4. **Template:** The template for content that is added from a URL is always an HTML document.
  5. **Attributes**: Attributes for the content uploaded from the URL.
* Click **Create**. The content from the specified URL is extracted by the Avaamo Platform to seamlessly create a knowledge-base. You can view the status of the upload for each document in the Documents tab. The following status values are displayed:
  1. **Uploading**: The information is being extracted and currently getting processed by the Avaamo Platform.
  2. **Complete**: The URL is uploaded successfully.
  3. **Error**: The upload has errored out. In case of errors, you can click Error in the Status column to view more details. See [Debug Answers](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/troubleshooting-tips), for more information.

{% hint style="success" %}
**Key Points**:

* Use the document parsing utility to upload multiple URLs at once. Contact Avaamo Support to get access to the document parsing utility.&#x20;
* Only the specific page in the URL is uploaded. Content from links to other pages or websites is not uploaded.
* All URLs must be publicly available or the URLs must allow content to be downloaded by a scraping server.
* URL must not redirect to an authorization page.
* URL must allow cross-origin from the Avaamo Platform.
* URL must not include assets like PDFs, Docx. If you wish to process asset-type documents (PDFs), then you can upload them as documents instead of URLs.
* Avoid pages with browser-window popups.
* All the text captured in one knowledge base must be under 2 MB in base Unicode representation.
* You can upload documents in any language as long as the language is configured or added to your agent. See [Add languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-languages), for more information on adding languages to your agent. See [Multi-lingual answering](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/multilingual-answering), for more information.
  {% endhint %}

**Note**: You can ingest content to Answers using any CMS Webhooks or pull content and upload it to the Answers knowledge base. See [Content ingestion using Webhooks](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/content-ingestion), for more information.

{% hint style="info" %}
Contact Avaamo Support to start using this feature, and for more information on repo access and API documentation.
{% endhint %}

### Next Steps

Once the upload of documents or URLs to the knowledge base is successful, your Avaamo Answers skill is ready for testing. See [Test Answers](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/test-avaamo-answers), for more information. You can continue to fine-tune and edit the knowledge base based on the user conversation history. See [View and Edit Knowledge](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/view-and-edit-knowledge), for more information.

You can also perform certain actions on the knowledge base such as retraining, editing the uploaded documents or URLs, or deleting the documents or URLs from the knowledge base, as required. See [Perform Common Actions](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/perform-common-actions), for more information.
