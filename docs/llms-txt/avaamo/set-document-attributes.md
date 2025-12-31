# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/files/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/website/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/servicenow/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/sharepoint/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/files/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/website/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/servicenow/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/sharepoint/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/files/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/website/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/servicenow/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/sharepoint/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/files/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/website/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/servicenow/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/sharepoint/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Set document attributes

In this step, you can create new attributes and assign them to the documents you selected in the previous step.

1. You can assign the attributes to all selected documents.
2. &#x20;Click the dropdown menu and choose `+ Additional property` to create a new attribute and assign a corresponding value.

{% hint style="info" %}
**Note:** You can assign multiple values to the same attribute by passing a comma-separated value, such as `value1, value2.`
{% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Ff2gxvum0B2VivfbJIl1m%2FScreenshot%202025-10-22%20at%204.49.58%E2%80%AFPM.png?alt=media&#x26;token=41377808-d72b-4d55-b475-d41b047bfe27" alt=""><figcaption></figcaption></figure>

3. Click `Submit`.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F0F9Lb4l9kmaKv8MaZ5mM%2FScreenshot%202025-10-22%20at%204.51.18%E2%80%AFPM.png?alt=media&#x26;token=7831f5af-b7c9-449c-b3bc-a408ea8614a8" alt=""><figcaption></figcaption></figure>

4. You can view all the ingested documents for the created job. Enter keywords in the search bar to search for specific ingested articles.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHlUrwHZOHw7cgdiOb2zJ%2FScreenshot%202025-10-22%20at%204.53.25%E2%80%AFPM.png?alt=media&#x26;token=263e3c50-f71d-493a-8f48-c8fb1cb9168a" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="247">Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Total Documents</td><td>It is the sum of the number of  <code>Processing</code>, <code>Ingested</code>, and <code>Failed</code> Documents</td></tr><tr><td>Processing</td><td>Number of Documents ingestion is under process</td></tr><tr><td>Ingested</td><td>Number of Documents ingested</td></tr><tr><td>Failed</td><td>Number of Documents failed to ingest</td></tr><tr><td>Column name: TITLE</td><td>Name of the documents </td></tr><tr><td>Column name: SITE</td><td>URL or folder name from where the document is selected.</td></tr><tr><td>Column name: TYPE</td><td>Type of articles ingested like Documents, Lists, or Pages</td></tr><tr><td>Column name: STATUS</td><td><p>Status of the articles. You can also filter with these statuses.<br><br><code>Queued</code><strong>:</strong> Initial status of the articles while processing the ingestion</p><p><code>Extracting</code>: Processing the information in the documents as Knowledge</p><p><code>In Progress</code><strong>:</strong> Ingestion process in progress<br><code>Ingested</code><strong>:</strong> Articles successfully ingested<br><code>Error</code><strong>:</strong> Ingestion was unsuccessful</p></td></tr><tr><td>Column name: ACTION</td><td>Click the three dots to  <code>View, Delete, Edit and Reingest</code> the ingested document.</td></tr></tbody></table>

{% hint style="info" %}
**Note:** If a document shows the status of `Error`, then the following tips can help:

* Empty article: Check to ensure the document is not empty
* API issues: Verify that the API connections are functioning as expected
* Insufficient permissions: Ensure that you have the necessary permissions to access and ingest the document

In such situations, create a new ingestion job and attempt to reingest the document. This often resolves the problem.
{% endhint %}
