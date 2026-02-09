# Source: https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/advanced-attributes-handler.md

# Advanced Attributes Handler

If you missed configuring attributes during ingestion, or if you need to update attributes for already ingested documents or articles, you can use the **Advanced Attribute Handler**. This feature enables you to apply or modify document attributes using custom JavaScript logic during a sync run.

The Advanced Attribute Handler supports bulk append or update of document attributes at the job level in the DataSync AI tool, allowing attributes to be applied to selected documents as required.

This approach also allows you to safely validate attribute logic before applying it across documents during a sync operation, reducing the risk of incorrect attribute updates.

**To configure the advanced attribute handler**

1. Navigate to the required DataSync job.
2. Click the three-dot menu next to the job name and select `Advanced Attribute Handler`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FskJpemOuOI0oiGGPtCXs%2FScreenshot%202026-01-29%20at%204.34.33%E2%80%AFPM.png?alt=media&#x26;token=153aa24a-8455-4d98-a4af-a630500e33ca" alt=""><figcaption></figcaption></figure>

3. A side panel opens with the configuration options. Toggle the `Enabled` switch to enable the attribute handler.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FcM2zV3mC5DQiFDrECxot%2FScreenshot%202026-01-29%20at%204.50.53%E2%80%AFPM.png?alt=media&#x26;token=268387b7-8f17-48eb-8cb5-56460298a5e6" alt=""><figcaption></figcaption></figure>

4. Under `Configure attribute handler`, provide the JavaScript code that returns the updated attributes you want to apply to the documents.
5. In the `Test` option in the attribute handler panel. Update the test JavaScript input with actual sample data.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FMu3yrRu1v1tBcAK8DBuu%2FScreenshot%202026-01-29%20at%204.53.34%E2%80%AFPM.png?alt=media&#x26;token=735f41eb-36ba-4edb-bcb2-580250c47848" alt=""><figcaption></figcaption></figure>

6. Click **Test** to validate the script execution. Review the output to confirm that the attributes are updated correctly for the selected document or article.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FK7aCk7AlzCx5Ay0EoB5n%2FScreenshot%202026-01-29%20at%204.54.47%E2%80%AFPM.png?alt=media&#x26;token=1f52659b-e70c-4d67-8da8-4a1233256284" alt=""><figcaption></figcaption></figure>

7. Once you have configured and tested the attribute handler, choose one of the following actions:

* **Cancel** – Discard the changes if you do not want to apply the attribute configuration.
* **Save** – Save the configuration. The attribute handler will be applied the next time [AutoSync](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/auto-sync) or [SyncNow](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/sync-now) is triggered.
* **Save & Apply** – Save the configuration and immediately run a `manual sync` to apply the attribute handler to the selected documents.
