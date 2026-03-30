# Source: https://firebase.google.com/docs/reference/js/ai.urlcontextmetadata.md.txt

# URLContextMetadata interface

Metadata related to [URLContextTool](https://firebase.google.com/docs/reference/js/ai.urlcontexttool.md#urlcontexttool_interface).

**Signature:**

    export interface URLContextMetadata 

## Properties

| Property | Type | Description |
|---|---|---|
| [urlMetadata](https://firebase.google.com/docs/reference/js/ai.urlcontextmetadata.md#urlcontextmetadataurlmetadata) | [URLMetadata](https://firebase.google.com/docs/reference/js/ai.urlmetadata.md#urlmetadata_interface)\[\] | List of URL metadata used to provide context to the Gemini model. |

## URLContextMetadata.urlMetadata

List of URL metadata used to provide context to the Gemini model.

**Signature:**

    urlMetadata: URLMetadata[];