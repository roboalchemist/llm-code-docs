# Source: https://docs.base44.com/developers/references/sdk/docs/type-aliases/integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# integrations

***

## Overview

Integrations module for calling integration methods.

This module provides access to integration methods for interacting with external services. Unlike the connectors module that gives you raw OAuth tokens, integrations provide pre-built functions that Base44 executes on your behalf.

### Integration Types

There are two types of integrations:

* **Built-in integrations** (`Core`): Pre-built functions provided by Base44 for common tasks such as AI-powered text generation, image creation, file uploads, and email. Access core integration methods using:
  ```
  base44.integrations.Core.FunctionName(params)
  ```

* **Custom workspace integrations** (`custom`): Pre-configured external APIs set up by workspace administrators. Workspace integration calls are proxied through Base44's backend, so credentials are never exposed to the frontend. Access custom workspace integration methods using:

  ```
  base44.integrations.custom.call(slug, operationId, params)
  ```

  <Info>To call a custom workspace integration, it must be pre-configured by a workspace administrator who imports an OpenAPI specification. Learn more about [custom workspace integrations](/documentation/integrations/managing-workspace-integrations).</Info>

### Authentication Modes

This module is available to use with a client in all authentication modes:

* **Anonymous or User authentication** (`base44.integrations`): Integration methods are invoked with the current user's permissions. Anonymous users invoke methods without authentication, while authenticated users invoke methods with their authentication context.
* **Service role authentication** (`base44.asServiceRole.integrations`): Integration methods are invoked with elevated admin-level permissions. The methods execute with admin authentication context.

#### Example

<CodeGroup>
  ```typescript const response = await base44.integrations.Core.InvokeLLM({ theme={null}
    prompt: 'Explain quantum computing',
    model: 'gpt-4'
  });
  ```
</CodeGroup>

#### Example

<CodeGroup>
  ```typescript const result = await base44.integrations.custom.call( theme={null}
    'github',
    'get:/repos/{owner}/{repo}',
    { pathParams: { owner: 'myorg', repo: 'myrepo' } }
  );
  ```
</CodeGroup>

## Core Integrations Methods

Core package containing built-in Base44 integration functions.

### InvokeLLM()

> **InvokeLLM**(`params`): `Promise`\<`string` | `object`>

Generate text or structured JSON data using AI models.

#### Parameters

<ParamField body="params" type="InvokeLLMParams" required>
  Parameters for the LLM invocation
</ParamField>

<Accordion title="Properties">
  <ParamField body="prompt" type="string" required>
    The prompt text to send to the model
  </ParamField>

  <ParamField body="add_context_from_internet" type="boolean">
    If set to `true`, the LLM will use Google Search, Maps, and News to gather real-time context before answering.
  </ParamField>

  <ParamField body="response_json_schema" type="object">
    If you want structured data back, provide a [JSON schema object](https://json-schema.org/understanding-json-schema/reference/object) here. If provided, the function returns a JSON object; otherwise, it returns a string.
  </ParamField>

  <ParamField body="file_urls" type="string[]">
    A list of file URLs (uploaded via UploadFile) to provide as context/attachments to the LLM. Do not use this together with `add_context_from_internet`.
  </ParamField>
</Accordion>

#### Returns

`Promise<string | object>`

<Accordion title="Properties">
  <ResponseField name="an" type="Promise<string | object>" required>
    Promise resolving to a string (when no schema provided) or an object (when schema provided).
  </ResponseField>
</Accordion>

#### Examples

<CodeGroup>
  ```typescript Basic prompt theme={null}
  const response = await base44.integrations.Core.InvokeLLM({
    prompt: "Write a haiku about coding."
  });
  ```

  ```typescript Prompt with internet context theme={null}
  const response = await base44.integrations.Core.InvokeLLM({
    prompt: "What is the current stock price of Wix and what was the latest major news about it?",
    add_context_from_internet: true
  });
  ```

  ```typescript Structured JSON response theme={null}
  const response = await base44.integrations.Core.InvokeLLM({
    prompt: "Analyze the sentiment of this review: 'The service was slow but the food was amazing.'",
    response_json_schema: {
      type: "object",
      properties: {
        sentiment: { type: "string", enum: ["positive", "negative", "mixed"] },
        score: { type: "number", description: "Score from 1-10" },
        key_points: { type: "array", items: { type: "string" } }
      }
    }
  });
  // Returns object: { sentiment: "mixed", score: 7, key_points: ["slow service", "amazing food"] }
  ```
</CodeGroup>

***

### GenerateImage()

> **GenerateImage**(`params`): `Promise`\<`GenerateImageResult`>

Create AI-generated images from text prompts.

#### Parameters

<ParamField body="params" type="GenerateImageParams" required>
  Parameters for image generation
</ParamField>

<Accordion title="Properties">
  <ParamField body="prompt" type="string" required>
    Description of the image to generate.
  </ParamField>
</Accordion>

#### Returns

`GenerateImageResult`

<Accordion title="Properties">
  <ResponseField name="url" type="string" required>
    URL of the generated image.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Generate an image from a text prompt theme={null}
  const {url} = await base44.integrations.Core.GenerateImage({
    prompt: "A serene mountain landscape with a lake in the foreground"
  });
  console.log(url); // https://...generated_image.png
  ```
</CodeGroup>

***

### UploadFile()

> **UploadFile**(`params`): `Promise`\<`UploadFileResult`>

Upload files to public storage and get a URL.

#### Parameters

<ParamField body="params" type="UploadFileParams" required>
  Parameters for file upload
</ParamField>

<Accordion title="Properties">
  <ParamField body="file" type="File" required>
    The file object to upload.
  </ParamField>
</Accordion>

#### Returns

`UploadFileResult`

<Accordion title="Properties">
  <ResponseField name="file_url" type="string" required>
    URL of the uploaded file.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Upload a file in React theme={null}
  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    const { file_url } = await base44.integrations.Core.UploadFile({ file });
    console.log(file_url); // https://...uploaded_file.pdf
  };
  ```
</CodeGroup>

***

### SendEmail()

> **SendEmail**(`params`): `Promise`\<`any`>

Send emails to registered users of your app.

#### Parameters

<ParamField body="params" type="SendEmailParams" required>
  Parameters for sending email
</ParamField>

<Accordion title="Properties">
  <ParamField body="to" type="string" required>
    Recipient email address.
  </ParamField>

  <ParamField body="subject" type="string" required>
    Email subject line.
  </ParamField>

  <ParamField body="body" type="string" required>
    Plain text email body content.
  </ParamField>

  <ParamField body="from_name" type="string">
    The name of the sender. If omitted, the app's name will be used.
  </ParamField>
</Accordion>

#### Returns

`Promise<any>`

Promise resolving when the email is sent.

***

### ExtractDataFromUploadedFile()

> **ExtractDataFromUploadedFile**(`params`): `Promise`\<`object`>

Extract structured data from uploaded files based on the specified schema.

Start by uploading the file to public storage using the [`UploadFile()`](#uploadfile) function. Then, use the `file_url` parameter to extract structured data from the uploaded file.

#### Parameters

<ParamField body="params" type="ExtractDataFromUploadedFileParams" required>
  Parameters for data extraction
</ParamField>

<Accordion title="Properties">
  <ParamField body="file_url" type="string" required>
    The URL of the uploaded file to extract data from.
  </ParamField>

  <ParamField body="json_schema" type="object" required>
    A [JSON schema object](https://json-schema.org/understanding-json-schema/reference/object) defining what data fields you want to extract.
  </ParamField>
</Accordion>

#### Returns

`Promise<object>`

Promise resolving to the extracted data.

#### Examples

<CodeGroup>
  ```typescript Extract data from an already uploaded file theme={null}
  const result = await base44.integrations.Core.ExtractDataFromUploadedFile({
    file_url: "https://example.com/files/invoice.pdf",
    json_schema: {
      type: "object",
      properties: {
        invoice_number: { type: "string" },
        total_amount: { type: "number" },
        date: { type: "string" },
        vendor_name: { type: "string" }
      }
    }
  });
  console.log(result); // { invoice_number: "INV-12345", total_amount: 1250.00, ... }
  ```

  ```typescript Upload a file and extract data in React theme={null}
  const handleFileExtraction = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    // First, upload the file
    const { file_url } = await base44.integrations.Core.UploadFile({ file });

    // Then extract structured data from it
    const result = await base44.integrations.Core.ExtractDataFromUploadedFile({
      file_url,
      json_schema: {
        type: "object",
        properties: {
          summary: {
            type: "string",
            description: "A brief summary of the file content"
          },
          keywords: {
            type: "array",
            items: { type: "string" }
          },
          document_type: {
            type: "string"
          }
        }
      }
    });
    console.log(result); // { summary: "...", keywords: [...], document_type: "..." }
  };
  ```
</CodeGroup>

***

### UploadPrivateFile()

> **UploadPrivateFile**(`params`): `Promise`\<`UploadPrivateFileResult`>

Upload files to private storage that requires a signed URL to access.

Create a signed URL to access uploaded files using the [`CreateFileSignedUrl()`](#createfilesignedurl) function.

#### Parameters

<ParamField body="params" type="UploadPrivateFileParams" required>
  Parameters for private file upload
</ParamField>

<Accordion title="Properties">
  <ParamField body="file" type="File" required>
    The file object to upload.
  </ParamField>
</Accordion>

#### Returns

`UploadPrivateFileResult`

<Accordion title="Properties">
  <ResponseField name="file_uri" type="string" required>
    URI of the uploaded private file, used to create a signed URL.
  </ResponseField>
</Accordion>

#### Examples

<CodeGroup>
  ```typescript Upload a private file theme={null}
  const { file_uri } = await base44.integrations.Core.UploadPrivateFile({ file });
  console.log(file_uri); // "private/user123/document.pdf"
  ```

  ```typescript Upload a private file and create a signed URL theme={null}
  const handlePrivateUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    // Upload to private storage
    const { file_uri } = await base44.integrations.Core.UploadPrivateFile({ file });

    // Create a signed URL that expires in 1 hour (3600 seconds)
    const { signed_url } = await base44.integrations.Core.CreateFileSignedUrl({
      file_uri,
      expires_in: 3600
    });

    console.log(signed_url); // Temporary URL to access the private file
  };
  ```
</CodeGroup>

***

### CreateFileSignedUrl()

> **CreateFileSignedUrl**(`params`): `Promise`\<`CreateFileSignedUrlResult`>

Generate temporary access links for private files.

Start by uploading the file to private storage using the [`UploadPrivateFile()`](#uploadprivatefile) function. Then, use the `file_uri` parameter to create a signed URL to access the uploaded file.

#### Parameters

<ParamField body="params" type="CreateFileSignedUrlParams" required>
  Parameters for creating signed URL
</ParamField>

<Accordion title="Properties">
  <ParamField body="file_uri" type="string" required>
    URI of the uploaded private file.
  </ParamField>

  <ParamField body="expires_in" type="number">
    How long the signed URL should be valid for, in seconds.
  </ParamField>
</Accordion>

#### Returns

`CreateFileSignedUrlResult`

<Accordion title="Properties">
  <ResponseField name="signed_url" type="string" required>
    Temporary signed URL to access the private file.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Create a signed URL for a private file theme={null}
  const { signed_url } = await base44.integrations.Core.CreateFileSignedUrl({
    file_uri: "private/user123/document.pdf",
    expires_in: 7200 // URL expires in 2 hours
  });
  console.log(signed_url); // https://...?signature=...
  ```
</CodeGroup>

## Custom Integrations Methods

Module for calling custom pre-configured API integrations.
Custom integrations allow workspace administrators to connect any external API by importing an OpenAPI specification. Apps in the workspace can then call these integrations using this module.

### call()

> **call**(\
> `slug`,\
> `operationId`,\
> `params?`\
> ): `Promise`\<`CustomIntegrationCallResponse`>

Call a custom integration endpoint.

#### Parameters

<Accordion title="Properties">
  <ParamField body="slug" type="string" required>
    The integration's unique identifier, as defined by the workspace admin.
  </ParamField>

  <ParamField body="operationId" type="string" required>
    The endpoint in `method:path` format. For example, `"get:/contacts"`, or `"post:/users/{id}"`. The method is the HTTP verb in lowercase and the path matches the OpenAPI specification.
  </ParamField>

  <ParamField body="params" type="CustomIntegrationCallParams">
    Optional parameters including payload, pathParams, and queryParams.
  </ParamField>
</Accordion>

#### Returns

`Promise<CustomIntegrationCallResponse>`

Promise resolving to the integration call response.

#### Throws

If slug is not provided.

#### Throws

If operationId is not provided.

#### Throws

If the integration or operation is not found (404).

#### Throws

If the external API call fails (502).

#### Throws

If the request times out (504).

#### Examples

<CodeGroup>
  ```typescript Call a custom CRM integration theme={null}
  const response = await base44.integrations.custom.call(
    "my-crm",
    "get:/contacts",
    { queryParams: { limit: 10 } }
  );

  if (response.success) {
    console.log("Contacts:", response.data);
  }
  ```

  ```typescript Call with path params and request body theme={null}
  const response = await base44.integrations.custom.call(
    "github",
    "post:/repos/{owner}/{repo}/issues",
    {
      pathParams: { owner: "myorg", repo: "myrepo" },
      payload: {
        title: "Bug report",
        body: "Something is broken"
      }
    }
  );
  ```
</CodeGroup>

## Type Definitions

### Core

> **Core**: `CoreIntegrations`

Core package containing built-in Base44 integration functions.

#### Example

<CodeGroup>
  ```typescript Invoke an LLM theme={null}
  const response = await base44.integrations.Core.InvokeLLM({
    prompt: 'Explain quantum computing',
    model: 'gpt-4'
  });
  ```
</CodeGroup>

### custom

> **custom**: `CustomIntegrationsModule`

Workspace integrations module for calling pre-configured external APIs.

#### Example

<CodeGroup>
  ```typescript Call a custom integration theme={null}
  const result = await base44.integrations.custom.call(
    'github',
    'get:/repos/{owner}/{repo}',
    { pathParams: { owner: 'myorg', repo: 'myrepo' } }
  );
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).