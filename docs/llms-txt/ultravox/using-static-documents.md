# Source: https://docs.ultravox.ai/tools/rag/using-static-documents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Static Documents

> Use text, PDF, Word, and other documents in your corpus.

You can use files as sources for any of your corpora.

Files can be added via the [Web App](https://app.ultravox.ai/rag) or via the [Create Corpus File Upload API](/api-reference/corpora/corpora-uploads-post).

## Upload Files via Web App

<Steps>
  <Step title="Create New Source">
    * Go to [RAG](https://app.ultravox.ai/rag) in the Ultravox web application.
    * Click `New Source` in the top right corner.
  </Step>

  <Step title="Add Details and Files">
    * Select the `Collection` to which you want to add the content.
    * (Optionally) Add a `Name` and `Description` for the new source.
    * Select `Document` and add files.

    <img className="block dark:hidden" src="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-light.png?fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=2616c28a81a5dafb62cd2d5712c32ef4" data-og-width="2880" width="2880" data-og-height="1600" height="1600" data-path="images/screenshots/corpus/add-source-from-document-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-light.png?w=280&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=802e784f43b6beef12d7ac5b1ac99435 280w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-light.png?w=560&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=40e86993ea00a4224c896a31f3e9bf76 560w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-light.png?w=840&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=cd56678e9acb8aac42809e1c2373cb67 840w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-light.png?w=1100&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=1260329194bb3d495e60d85717854767 1100w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-light.png?w=1650&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=a5aaa8d8e0222bb5b6ea414632d55a25 1650w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-light.png?w=2500&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=9b8aa735aa0e389bc6df1ce39266365f 2500w" />

    <img className="hidden dark:block" src="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-dark.png?fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=4ab070525dd834a2bceac7df3a00488b" data-og-width="2880" width="2880" data-og-height="1600" height="1600" data-path="images/screenshots/corpus/add-source-from-document-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-dark.png?w=280&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=309a7b33c07f8a9ec85c3fab313b6036 280w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-dark.png?w=560&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=88a894914ba790f0568b1c2fd6082012 560w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-dark.png?w=840&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=17f230f09146053e5ed1d9699f9c262a 840w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-dark.png?w=1100&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=52d48036aa982edc622dbc95b192859e 1100w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-dark.png?w=1650&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=f8184389e961e5513194af1d7ccb33dd 1650w, https://mintcdn.com/fixie-ff99b187/RRU3EPaTCQ6pUNKk/images/screenshots/corpus/add-source-from-document-dark.png?w=2500&fit=max&auto=format&n=RRU3EPaTCQ6pUNKk&q=85&s=26e39f90a57ea9edbaa0f258adb37d5c 2500w" />
  </Step>

  <Step title="Save">
    * Click `Save` and wait a few moments for your content to be uploaded and ingested.
  </Step>
</Steps>

## Upload Files via API

To upload files using the API, follow these steps:

<Steps>
  <Step title="Step 1: Request Upload URL">
    * Use the [Create Corpus File Upload API](/api-reference/corpora/corpora-uploads-post)
    * Include the MIME type string in the request body
    * This returns the URL to use for upload and the unique ID for the document
    * URLs expire after 5 minutes. Request a new one if it expires before using it

    <Note>The URL that is returned is tied to the provided MIME type. The same MIME type must be used during upload.</Note>
  </Step>

  <Step title="Step 2: Upload File">
    * Use the `presignedUrl` from Step 1 to upload the document
    * Ensure the MIME type in the upload matches what was specified in Step 1

    For example, if we requested an upload URL for a text file (MIME type `text/plain`):

    ```bash  theme={null}
    FILE_PATH="/path/to/your/file"
    UPLOAD_URL="https://storage.googleapis.com/fixie-ultravox-prod/..."

    curl -X PUT \
      -H "Content-Type: text/plain" \
      --data-binary @"$FILE_PATH" \
      "$UPLOAD_URL"
    ```
  </Step>

  <Step title="Step 3: Create New Source with Uploaded Document">
    * Use the [Create Corpus Source API](/api-reference/corpora/corpora-sources-post)
    * Use `upload` to provide the `documentId` from Step 1

    <Note>You can provide an array of Document IDs to bulk create a source.</Note>
  </Step>
</Steps>

## Supported File Types

The following types of static files are currently supported:

| File Extension | Type of File                               | MIME Type                                                                 |
| -------------- | ------------------------------------------ | ------------------------------------------------------------------------- |
| doc            | Microsoft Word Document                    | application/msword                                                        |
| docx           | Microsoft Word Open XML Document           | application/vnd.openxmlformats-officedocument.wordprocessingml.document   |
| txt            | Plain Text Document                        | text/plain                                                                |
| md             | Markdown Document                          | text/markdown                                                             |
| ppt            | Microsoft PowerPoint Presentation          | application/vnd.ms-powerpoint                                             |
| pptx           | Microsoft PowerPoint Open XML Presentation | application/vnd.openxmlformats-officedocument.presentationml.presentation |
| pdf            | Portable Document Format                   | application/pdf                                                           |

## Limits

See the [Overall Limits](/api-reference/corpora/overview#overall-limits) section for details on limits for the number of sources, file sizes, and more.
