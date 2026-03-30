# Source: https://docs.airbyte.com/platform/connector-development/config-based/understanding-the-yaml-file/file-syncing.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/config-based/understanding-the-yaml-file/file-syncing.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/config-based/understanding-the-yaml-file/file-syncing.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/config-based/understanding-the-yaml-file/file-syncing.md

# File syncing

Copy Page

File syncing enables connectors to download and transfer files from API sources when an API endpoint returns a file. This capability supports all common file formats including documents, images, and structured data.

info

File syncing is experimental. It isn't available in the Connector Builder UI. You must implement this using manifest.yaml files in a manifest-only or hybrid connector.

## Overview[​](#overview "Direct link to Overview")

File syncing works in these steps.

1. Extracting file download URLs from API response records

2. Making authenticated HTTP requests to download files

3. Storing files locally with organized naming and metadata

4. Adding file reference information to each record for destination processing

## Schema[​](#schema "Direct link to Schema")

```
file_uploader:
  title: File Uploader
  description: (experimental) Describes how to fetch a file
  type: object
  required:
    - type
    - requester
    - download_target_extractor
  properties:
    type:
      type: string
      enum: [FileUploader]
    requester:
      description: Requester component that describes how to prepare HTTP requests to send to the source API.
      anyOf:
        - "$ref": "#/definitions/HttpRequester"
        - "$ref": "#/definitions/CustomRequester"
    download_target_extractor:
      description: Responsible for fetching the url where the file is located. This is applied on each records and not on the HTTP response
      anyOf:
        - "$ref": "#/definitions/DpathExtractor"
        - "$ref": "#/definitions/CustomRecordExtractor"
    file_extractor:
      description: Responsible for fetching the content of the file. If not defined, the assumption is that the whole response body is the file content
      anyOf:
        - "$ref": "#/definitions/DpathExtractor"
        - "$ref": "#/definitions/CustomRecordExtractor"
    filename_extractor:
      description: Defines the name to store the file. Stream name is automatically added to the file path. File unique ID can be used to avoid overwriting files. Random UUID will be used if the extractor is not provided.
      type: string
      interpolation_context:
        - config
        - record
      examples:
        - "{{ record.id }}/{{ record.file_name }}/"
        - "{{ record.id }}_{{ record.file_name }}/"
    $parameters:
      type: object
      additionalProperties: true
```

## Required properties[​](#required-properties "Direct link to Required properties")

### `type`[​](#type "Direct link to type")

Set to `FileUploader` to enable file syncing capability.

### `requester`[​](#requester "Direct link to requester")

Defines how to make HTTP requests for downloading files. Supports all standard requester types including authentication methods like OAuth, Bearer tokens, and Basic authentication.

### `download_target_extractor`[​](#download_target_extractor "Direct link to download_target_extractor")

Extracts the file download URL from each record. Uses DPath syntax to specify the field containing the download URL.

## Optional properties[​](#optional-properties "Direct link to Optional properties")

### `file_extractor`[​](#file_extractor "Direct link to file_extractor")

Extracts file content from the HTTP response when the entire response body isn't the file. Useful when the API wraps file content in a JSON response.

### `filename_extractor`[​](#filename_extractor "Direct link to filename_extractor")

Customizes file naming using Jinja templating with access to record data and configuration. If not provided, Airbyte uses a random UUID as the filename. It's critical you ensure file names are unique every time.

## Authentication[​](#authentication "Direct link to Authentication")

File downloads support independent authentication from the main API requests. This allows downloading files from different domains or services that require separate credentials.

## File size limitation[​](#file-size-limitation "Direct link to File size limitation")

Supports files up to 1.5-GB in size. Airbyte does not sync files larger than that.

## Format compatibility[​](#format-compatibility "Direct link to Format compatibility")

Works with any file format since it handles files as binary data. Common examples:

* Documents (PDF, DOCX, TXT)
* Images (PNG, JPG, GIF)
* Structured data (CSV, JSON, XML)
* Archives (ZIP, TAR)

## Dynamic URL handling[​](#dynamic-url-handling "Direct link to Dynamic URL handling")

The `url_base` can use the special `{{download_target}}` placeholder to dynamically set the base URL from the extracted download URL, enabling downloads from multiple domains.

## Custom file naming[​](#custom-file-naming "Direct link to Custom file naming")

The `filename_extractor` supports Jinja templating with access to record data, allowing organized file storage with meaningful names and directory structures.

## Usage example[​](#usage-example "Direct link to Usage example")

Here's how the [Zendesk Support connector](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-zendesk-support/source_zendesk_support/manifest.yaml) uses file syncing for article attachments.

manifest.yaml

```
streams:
  article_attachments_stream:
    retriever:
      type: SimpleRetriever
      requester:
        type: HttpRequester
        url_base: "https://{{ config['subdomain'] }}.zendesk.com"
        path: "/api/v2/help_center/articles/{{ stream_partition.parent_id }}/attachments.json"
        http_method: "GET"
        authenticator:
          type: SelectiveAuthenticator
          authenticator_selection_path: ["credentials", "credentials"]
          authenticators:
            oauth2.0: "#/definitions/bearer_authenticator"
            api_token: "#/definitions/basic_authenticator"
      record_selector:
        extractor:
          type: DpathExtractor
          field_path: ["article_attachments"]
    file_uploader:
      type: FileUploader
      requester:
        type: HttpRequester
        url_base: "{{download_target}}"
        http_method: GET
        authenticator:
          type: SelectiveAuthenticator
          authenticator_selection_path: ["credentials", "credentials"]
          authenticators:
            oauth2.0: "#/definitions/bearer_authenticator"
            api_token: "#/definitions/basic_authenticator"
      download_target_extractor:
        type: DpathExtractor
        field_path: ["content_url"]
      filename_extractor: "{{ record.id }}/{{ record.file_name }}/"
```
