# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/confluence/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/files/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/website/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/servicenow/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/sharepoint/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/confluence/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/files/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/website/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/servicenow/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Source: https://docs.avaamo.com/user-guide/skills/knowledge-skill/add-content-to-knowledge-skill/sharepoint/step-2-configure-content-source-and-ingest-content/set-document-attributes.md

# Set document attributes

In this step, you can assign attributes to the documents you selected in the previous step.

1. You can assign the attributes to all selected documents.
2. Click the dropdown menu and choose `+ Additional property` to create a new attribute and assign a corresponding value.

{% hint style="info" %}
**Note:** You can assign multiple values to the same attribute by passing a comma-separated value, such as `value1, value2.`
{% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F32dY7nuDMgWoofgnEgPV%2FScreenshot%202026-02-02%20at%202.07.07%E2%80%AFPM.png?alt=media&#x26;token=e24220ef-58eb-4e23-a0b4-ed26eb05c778" alt=""><figcaption></figcaption></figure>

### Configure Advanced Attribute Handler

1. Click  `Configure Advanced Attribute Handler`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2rjhYadTJQXkSYwrRPks%2FScreenshot%202026-02-02%20at%202.33.32%E2%80%AFPM.png?alt=media&#x26;token=ac78ecc1-7108-480a-a168-145cf3c30e36" alt=""><figcaption></figcaption></figure>

3. A side panel opens with the configuration options. Toggle the `Enabled` switch to enable the attribute handler.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FtXUZctxZEvZmjf7oeY6M%2FScreenshot%202026-02-02%20at%202.28.28%E2%80%AFPM.png?alt=media&#x26;token=3a68d6a1-7849-4015-a48e-a14ad7ceb3d9" alt=""><figcaption></figcaption></figure>

4. Under `Configure attribute handler`, provide the JavaScript code that returns the updated attributes you want to apply to the documents.
5. In the `Test` option in the attribute handler panel. Update the test JavaScript input with actual sample data.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FKNUaV2XRiQ26lETYcFYG%2FScreenshot%202026-02-02%20at%202.31.04%E2%80%AFPM.png?alt=media&#x26;token=8ad84f2f-7962-4656-bcc9-2bf720fe57f8" alt=""><figcaption></figcaption></figure>

6. Click `Run Test` to validate the script execution. Review the output to confirm that the attributes are updated correctly for the selected document or article.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FU8R5015Ji6ATMD5Xz2NQ%2FScreenshot%202026-02-02%20at%202.29.43%E2%80%AFPM.png?alt=media&#x26;token=f58d40c6-a21e-4701-bfed-1f69f7ba3c6f" alt=""><figcaption></figcaption></figure>

7. Once you have configured and tested the attribute handler, choose one of the following actions:

* **Cancel** – Discard the changes if you do not want to apply the attribute configuration.
* **Save** – Save the configuration.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FO3ns7haghtf7ovjGjvvS%2FScreenshot%202026-02-02%20at%202.40.10%E2%80%AFPM.png?alt=media&#x26;token=7eef02f4-67c3-4a2f-a278-71c20d5e6113" alt=""><figcaption></figcaption></figure>

8. Click `Submit`.&#x20;
9. You can view the configured attributes using the `View document attributes` option. When you click this option, a pop-up opens that displays the document's attribute details. You can also download the attributes as a CSV file for further analysis or use.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNrP753Ud4qH5lW65V9Bh%2FScreenshot%2002-02-2026%20at%2014.42.png?alt=media&#x26;token=5ac3e8c6-d226-416b-9ca6-5fcece7c8437" alt=""><figcaption></figcaption></figure>

10. You can view all ingested documents for the job you created here. Enter keywords in the search bar to search for specific ingested articles.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fh9QwVa11MqP7vVBcwQeM%2FScreenshot%2002-02-2026%20at%2014.45.png?alt=media&#x26;token=7056c634-3478-46c0-9710-3c07914ef27d" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="247">Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Total Documents</td><td>It is the sum of the number of  <code>Processing</code>, <code>Ingested</code>, and <code>Failed</code> Documents</td></tr><tr><td>Processing</td><td>Number of Documents ingestion is under process</td></tr><tr><td>Ingested</td><td>Number of Documents ingested</td></tr><tr><td>Failed</td><td>Number of Documents failed to ingest</td></tr><tr><td>Others</td><td>It is the combined total of all <code>Skipped</code> and <code>Warning</code> statuses.</td></tr><tr><td>Column name: TITLE</td><td>Name of the documents </td></tr><tr><td>Column name: SITE</td><td>URL or folder name from where the document is selected.</td></tr><tr><td>Column name: TYPE</td><td>Type of articles ingested like Documents, Lists, or Pages</td></tr><tr><td>Column name: STATUS</td><td><p>Status of the articles. You can also filter with these statuses.<br><br><code>Queued</code><strong>:</strong> Initial status of the articles while processing the ingestion</p><p><code>Extracting</code>: Processing the information in the documents as Knowledge</p><p><code>In Progress</code><strong>:</strong> Ingestion process in progress<br><code>Ingested</code><strong>:</strong> Articles successfully ingested<br><code>Error</code><strong>:</strong> Ingestion was unsuccessful</p></td></tr><tr><td>Column name: ACTION</td><td>Click the three dots to  <code>View, Delete, Edit and Reingest</code> the ingested document.</td></tr></tbody></table>

{% hint style="info" %}
**Note:** If a document shows the status of `Error`, then the following tips can help:

* Empty article: Check to ensure the document is not empty
* API issues: Verify that the API connections are functioning as expected
* Insufficient permissions: Ensure that you have the necessary permissions to access and ingest the document

In such situations, create a new ingestion job and attempt to reingest the document. This often resolves the problem.
{% endhint %}
