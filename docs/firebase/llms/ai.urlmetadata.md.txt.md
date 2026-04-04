# Source: https://firebase.google.com/docs/reference/js/ai.urlmetadata.md.txt

# URLMetadata interface

Metadata for a single URL retrieved by the [URLContextTool](https://firebase.google.com/docs/reference/js/ai.urlcontexttool.md#urlcontexttool_interface) tool.

**Signature:**

    export interface URLMetadata 

## Properties

| Property | Type | Description |
|---|---|---|
| [retrievedUrl](https://firebase.google.com/docs/reference/js/ai.urlmetadata.md#urlmetadataretrievedurl) | string | The retrieved URL. |
| [urlRetrievalStatus](https://firebase.google.com/docs/reference/js/ai.urlmetadata.md#urlmetadataurlretrievalstatus) | [URLRetrievalStatus](https://firebase.google.com/docs/reference/js/ai.md#urlretrievalstatus) | The status of the URL retrieval. |

## URLMetadata.retrievedUrl

The retrieved URL.

**Signature:**

    retrievedUrl?: string;

## URLMetadata.urlRetrievalStatus

The status of the URL retrieval.

**Signature:**

    urlRetrievalStatus?: URLRetrievalStatus;