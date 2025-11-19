# Source: https://docs.tavus.io/sections/conversational-video-interface/knowledge-base.md

# Knowledge Base

> Upload documents to your knowledge base for personas to reference during conversations.

<Note>
  For now, our Knowledge Base only supports documents written in English and works best for conversations in English.

  We’ll be expanding our Knowledge Base language support soon!
</Note>

Our Knowledge Base system uses RAG (Retrieval-Augmented Generation) to process and and transform the contents of your documents and websites, allowing your personas to dynamically access and leverage information naturally during a conversation.

During a conversation, our persona will continuously analyze conversation content and pull relevant information from the documents that you have selected during conversation creation as added context.

## Getting Started With Your Knowledge Base

To leverage the Knowledge Base, you will need to upload documents or website URLs that you intend to reference from in conversations.
Let's walk through how to upload your documents and use them in a conversation.

<Note>
  You can either use our [Developer Portal](https://platform.tavus.io/documents) or API endpoints to upload and manage your documents.
  Our Knowledge Base supports creating documents from an uploaded file or a website URL.
</Note>

<Steps>
  <Step title="Step 1: Ensure Website Resources are Publicly Accessible" titleSize="h3">
    For any documents to be created via website URL, please make sure that each document is publicly accessible without requiring authorization, such as a pre-signed S3 link.

    For example, entering the URL in a browser should either:

    * Open the website you want to process and save contents from.
    * Open a document in a PDF viewer.
    * Download the document.
  </Step>

  <Step title="Step 2: Upload your Documents" titleSize="h3">
    You can create documents using either the [Developer Portal](https://platform.tavus.io/documents) or the [Create Document](https://docs.tavus.io/api-reference/documents/create-document) API endpoint.

    If you want to use the API, you can send a request to Tavus to upload your document.

    Here's an example of a `POST` request to `tavusapi.com/v2/documents`.

    ```json  theme={null}
    {
        "document_name": "test-doc-1",
        "document_url": "https://your.document.pdf",
        "callback_url": "webhook-url-to-get-progress-updates" // Optional
    }
    ```

    The response from this POST request will include a `document_id` - a unique identifier for your uploaded document. When creating a conversation, you may include all `document_id` values that you would like the persona to have access to.

    Currently, we support the following file formats: .pdf, .txt, .docx, .doc, .png, .jpg, .pptx, .csv, and .xlsx.
  </Step>

  <Step title="Step 3: Document Processing" titleSize="h3">
    After your document is uploaded, it will be processed in the background automatically to allow for incredibly fast retrieval during conversations.
    This process can take 5-10 minutes depending on document size.

    During processing, if you have provided a `callback_url` in the [Create Document](https://docs.tavus.io/api-reference/documents/create-document) request body, you will receive periodic callbacks with status updates.
    You may also use the [Get Document](https://docs.tavus.io/api-reference/documents/get-document) endpoint to poll the most recent status of your documents.
  </Step>

  <Step title="Step 4: Create a conversation with the document" titleSize="h3">
    Once your documents have finished processing, you may use the `document_id` from Step 2 as part of the [Create Conversation](https://docs.tavus.io/api-reference/conversations/create-conversation) request.

    You can add multiple documents to a conversation within the `document_ids` object.

    ```json  theme={null}
    {
      "persona_id": "your_persona_id",
      "replica_id": "your_replica_id",
      "document_ids": ["d1234567890", "d1234567891"]
    }
    ```

    During your conversation, the persona will be able to reference information from your documents in real time.
  </Step>
</Steps>

## Retrieval Strategy

When creating a conversation with documents, you can optimize how the system searches through your knowledge base by specifying a retrieval strategy. This strategy determines the balance between search speed and the quality of retrieved information, allowing you to fine-tune the system based on your specific needs.

You can choose from three different strategies:

* `speed`: Optimizes for faster retrieval times for minimal latency.
* `balanced` (default): Provides a balance between retrieval speed and quality.
* `quality`: Prioritizes finding the most relevant information, which may take slightly longer but can provide more accurate responses.

```json  theme={null}
{
  "persona_id": "your_persona_id",
  "replica_id": "your_replica_id",
  "document_ids": ["d1234567890"],
  "document_retrieval_strategy": "balanced"
}
```

## Document Tags

If you have a lot of documents, maintaining long lists of `document_id` values can get tricky.
Instead of using distinct `document_ids`, you can also group documents together with shared tag values.
During the [Create Document](https://docs.tavus.io/api-reference/documents/create-document) API call, you may specify a value for `tags` for your document.
Then, when you create a conversation, you may specify the `tags` value instead of passing in discrete `document_id` values.

For example, if you are uploading course material, you could add the tag `"lesson-1"` to all documents that you want accessible in the first lesson.

```json  theme={null}
{
        "document_name": "test-doc-1",
        "document_url": "https://your.document.pdf",
        "tags": ["lesson-1"]
}
```

In the [Create Conversation](https://docs.tavus.io/api-reference/conversations/create-conversation) request, you can add the tag value `lesson-1` to `document_tags` instead of individual `document_id` values.

```json  theme={null}
{
  "persona_id": "your_persona_id",
  "replica_id": "your_replica_id",
  "document_tags": ["lesson-1"]
}
```
