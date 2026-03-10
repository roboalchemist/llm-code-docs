# Source: https://firebase.google.com/docs/reference/js/ai.urlcontexttool.md.txt

# URLContextTool interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

A tool that allows you to provide additional context to the models in the form of public web URLs. By including URLs in your request, the Gemini model will access the content from those pages to inform and enhance its response.

**Signature:**

    export interface URLContextTool 

## Properties

| Property | Type | Description |
|---|---|---|
| [urlContext](https://firebase.google.com/docs/reference/js/ai.urlcontexttool.md#urlcontexttoolurlcontext) | [URLContext](https://firebase.google.com/docs/reference/js/ai.urlcontext.md#urlcontext_interface) | ***(Public Preview)*** Specifies the URL Context configuration. |

## URLContextTool.urlContext

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Specifies the URL Context configuration.

**Signature:**

    urlContext: URLContext;