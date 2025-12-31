# Source: https://docs.avaamo.com/user-guide/llamb/llamb-rest-apis/content-ingestion-apis.md

# Content ingestion APIs

## Upload document (HTML, URL) to LLaMB

<mark style="color:green;">`POST`</mark> `https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/upload-web`

{% hint style="info" %}
**Note:**&#x20;

1. The rate limit for the upload-web API is capped at 50 uploads per minute. Contact Avaamo Support with your use-case details if you wish to increase the rate limit for the API.&#x20;
2. Replace `{{instance-name}}` with your actual instance name, such as `c6` or `h1`.
   {% endhint %}

{% hint style="warning" %}
**Recommendation:**&#x20;

It is recommended to use the `upload-file` API instead of the `upload-web` API when uploading HTML content to the system. This approach ensures better control and consistency in content management.\
Using the upload-file API offers several advantages:

1. &#x20;**Content Persistence:** The uploaded HTML content is explicitly stored in the database, ensuring it is readily available for future reference.
2. **Seamless Retraining:** Since the content is saved, it can be easily accessed during document retraining operations initiated through the UI.
   {% endhint %}

#### Headers

<table><thead><tr><th width="222.17755126953125">Name</th><th width="100.478271484375">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>String</td><td><p>Unique access token of the user. <br></p><p>You can get the user access token from the Settings -> Users page.  See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr><tr><td>content-type</td><td>String</td><td>application/JSON</td></tr></tbody></table>

#### Request Body

<table><thead><tr><th width="226">Name</th><th width="95">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_group_id<mark style="color:red;">*</mark></td><td>Number</td><td><p>Unique identifier for the document group.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. See <a href="../../get-started/step-2-ingest-enterprise-content/create-document-groups#view-edit-a-document-group">View or edit document groups</a>, for more information.<br><br><strong>Note:</strong> You can use either the <code>document_group_id</code> or a combination of <code>agent_id</code> and <code>document_group_uuid</code> in the request body. Both approaches are supported.</p></td></tr><tr><td>agent_id</td><td>Number</td><td><p>Agent identifier.<br></p><p>You can get the agent identifier from the agent URL.</p></td></tr><tr><td>document_group_uuid</td><td>String</td><td><p>Unique user identifier for the document group.</p><p></p><p>You can get the document group UUID from the Document group -> View/Edit page. See <a href="../../get-started/step-2-ingest-enterprise-content/create-document-groups#view-edit-a-document-group">View or edit document groups</a>, for more information.</p></td></tr><tr><td>document<mark style="color:red;">*</mark></td><td>JSON</td><td>Document object that needs to be uploaded</td></tr><tr><td>document -> name<mark style="color:red;">*</mark></td><td>String </td><td><p>Name of the document.</p><p>Max length: 255 characters. </p></td></tr><tr><td>document -> attributes</td><td>Key-value</td><td><p>Define attributes for the uploaded documents or URLs in your LLaMB skill to facilitate disambiguation or filtering. </p><p></p><p>Example: <code>"attributes": "{\"key\": \"value\"}</code>"</p><p></p><p>Attributes can be metadata of the document. You define attributes in key-value pairs. See <a href="../get-started/step-2-ingest-enterprise-content/document-attributes">Document attributes</a>, for more information.</p></td></tr><tr><td>document -> type<mark style="color:red;">*</mark></td><td>String</td><td><p>Type of the document. </p><p>Supported values: html, url</p></td></tr><tr><td>document -> preview_url<mark style="color:red;">*</mark></td><td>String</td><td><p>Mandatory only for uploading HTML content.</p><p></p><p>Display the URL that needs to be opened when the user clicks the source citation in the response. </p><p></p><p>You can get the preview_url from the Document group -> Document -> View/Edit page. </p></td></tr><tr><td>document -> language</td><td>String</td><td>This refers to the document's language. If you specify a language during ingestion, LLaMB uses that language to extract the content. If you do not provide, LLaMB automatically detects the document’s language and processes it accordingly.</td></tr><tr><td>document -> parsing_template_id<mark style="color:red;">*</mark></td><td>Integer</td><td><p>Specify the parsing template identifier that must be used to parse the document. You can get the identifier from the <a href="../get-started/step-2-ingest-enterprise-content/parsing-templates">Parsing template</a> page. </p><p></p><p>Default value: default parsing template identifier is used. </p><p></p><p>It is recommended to create the parsing template in the Parsing template page and use the parsing_template_id in the API payload.</p></td></tr><tr><td>document -> source <mark style="color:red;">*</mark></td><td>String</td><td><p>If uploading from a URL, <code>source</code> is the actual source URL from where the content must be ingested.</p><p></p><p>If uploading a HTML content, <code>source</code> is the raw HTML content.</p><p></p><p>Raw HTML Content must be in the following format: </p><p><code>&#x3C;title>Name of document&#x3C;/title>&#x3C;body>valid html content&#x3C;/body></code></p></td></tr></tbody></table>

{% tabs %}
{% tab title="400: Bad Request Bad " %}
Request indicates the payload is wrong
{% endtab %}

{% tab title="200: OK Successful request" %}

```javascript
{
    "https://avaamo.ai/privacy-policy/": {
        "status": true,
        "chunks": 8,
        "response_text": {
            "id": 85xxx,
            "name": "Privacy documents",
            "uuid": "01ca5f76-xxx-xxx-xxx-8784e8f61154",
            "document_type": "url",
            "status": "QUEUED",
            "language": 1,
            "language_string": "English (en-US)",
            "document_group": 10xx,
            "source_url": "https://avaamo.ai/privacy-policy/",
            "source_file": null,
            "preview_url": "https://avaamo.ai/gdpr-compliance/",
            "document_properties": null,
            "parsing_template": 6,
            "file_type": "url",
            "last_error": null,
            "updated_at": "2024-02-23T09:36:48.795473Z",
            "created_at": "2024-02-23T09:36:48.715125Z",
            "updated_by": "John Miller"
        }
    }
}
```

{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Key points**:

* Ensure that the right content is posted during upload, as the HTML content is sanitized before processing.
* All content must be present in the following tags: "h1", "h2", "h3", "h4", "h5", "p", "img", "span", "td", "figure", "ol", "ul", "dd", "dt", "a", "table", "details", "summary". This list can be modified by using parsing templates.
* The maximum request size should not exceed 5 MB. Contact Avaamo Support, if the size exceeds the limit.
  {% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location 'https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/upload-web' \
--header 'access-token: 8ce0573xxxxxxxxxxxx7ccd9e60f3bd5' \
--header 'Content-Type: application/json' \
--data '{ 
    "document_group_id": 10xx, 
      "document": { 
         "name": "Privacy documents", 
          "type": "url", 
          "source": "https://avaamo.ai/privacy-policy/",
          "preview_url": "https://avaamo.ai/gdpr-compliance/",
          "parsing_template_id": 6
     } 
}'
```

{% endcode %}
{% endtab %}

{% tab title="node.JS" %}
{% code overflow="wrap" %}

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://cx.avaamo.com/llamb-content-skill/content-ingestion/upload-web',
  'headers': {
    'access-token': '8ce0573xxxxxxxxxxxx7ccd9e60f3bd5',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    "document_group_id": 10xx,
    "document": {
      "name": "Privacy documents",
      "type": "url",
      "source": "https://avaamo.ai/privacy-policy/",
      "preview_url": "https://avaamo.ai/gdpr-compliance/",
      "parsing_template_id": 6
    }
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});



```

{% endcode %}
{% endtab %}
{% endtabs %}

### Response attributes

The following is a sample API response for uploading a document:

```json
{
    "https://avaamo.ai/privacy-policy/": {
        "status": true,
        "response_text": {
            "id": 85xxx,
            "name": "Privacy documents",
            "uuid": "01ca5f76-xxx-xxx-xxx-8784e8f61154",
            "document_type": "url",
            "status": "QUEUED",
            "document_group": 10xx,
            "source_url": "https://avaamo.ai/privacy-policy/",
            "source_file": null,
            "preview_url": "https://avaamo.ai/gdpr-compliance/",
            "document_properties": null,
            "parsing_template": 6,
            "file_type": "url",
            "last_error": null,
            "updated_at": "2024-02-23T09:36:48.795473Z",
            "created_at": "2024-02-23T09:36:48.715125Z",
            "updated_by": "John Miller"
        }
    }
}
```

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th width="222">Attribute</th><th width="406.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>status</td><td>true if the document was updated successfully</td><td>Boolean</td></tr><tr><td>response_text -> id</td><td>Unique document identifier</td><td>Integer</td></tr><tr><td>response_text -> name</td><td>Document name</td><td>String</td></tr><tr><td>response_text -> uuid</td><td>Unique internal identifier of the document. </td><td>String</td></tr><tr><td>response_text -> document_type</td><td>Type of the document uploaded</td><td>String</td></tr><tr><td>response_text -> status</td><td><p>Status can be any one of the following values: Uploaded, Queued, Extracting, Learning, Complete, Error, or Warning.</p><p></p><p>See <a href="#document-status">Status</a>, for more information.</p></td><td>String</td></tr><tr><td>response_text -> document_group</td><td>Group identifier of the updated document.</td><td>Integer</td></tr><tr><td>response_text -> source_url</td><td>Source of the URL used for uploading the document.</td><td>String</td></tr><tr><td>response_text -> source_file</td><td>Source of the file used for uploading the document.</td><td>String</td></tr><tr><td>response_text -> preview_url</td><td>Preview URL of the updated document.</td><td>String</td></tr><tr><td>response_text -> created_at</td><td>Created Datetime of file</td><td>String</td></tr><tr><td>response_text -> file_type</td><td>Type of file uploaded </td><td>String</td></tr><tr><td>response_text -> parsing_template</td><td>Parsing template used to upload file</td><td>Integer</td></tr><tr><td>response_text -> updated_at</td><td>Updated Datetime of file</td><td>String</td></tr><tr><td>response_text -> updated_by</td><td>User who updated the file</td><td>String</td></tr><tr><td>last_error</td><td>Last error encountered with respect to the document</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases for uploading a document to LLaMB:

<table><thead><tr><th width="268.0422031374631">Use case</th><th width="498.34526508220097">Request payload</th></tr></thead><tbody><tr><td>Uploading a document using URL</td><td><p></p><pre class="language-json" data-overflow="wrap"><code class="lang-json">{ 
    "document_group_id": 10xx, 
      "document": { 
         "name": "Privacy documents", 
          "type": "url", 
<strong>          "source": "https://avaamo.ai/privacy-policy/",
</strong>          "preview_url": "https://avaamo.ai/gdpr-compliance/",
          "parsing_template_id": "6",
          "attributes": "{\"product\": {\"value\": \"Avaamo\", \"priority\": 0}}"
     } 
}
</code></pre></td></tr><tr><td>Uploading a document using HTML</td><td><p></p><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
 "document_group_id": 10xx,
 "document": {
   "source": "&#x3C;title>Terms of Use&#x3C;/title>&#x3C;body>&#x3C;h1>Privacy Policy&#x3C;/h1>&#x3C;p>Avaamo, Inc. ('Avaamo') provides this Privacy Policy to inform you of our policies and procedures regarding the collection, use and disclosure of Personally Identifiable Information that we may obtain through the use of Avaamo products such as Avaamo Platform ('Software'), applications such as Avaamo Messenger ('Application'), and access to www.avaamo.com, referred to as ('Site').&#x3C;/p>&#x3C;/body>",
   "name": "Terms of Use",
   "parsing_template_id": 6,
   "type": "html",
   "preview_url": "https://avaamo.ai/privacy/"
 }
}
</code></pre><p><br></p></td></tr><tr><td>Uploading a document using HTML using <code>agent_id</code> and <code>document_group_uuid</code> </td><td><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
 "agent_id": 71xx,
 "document_group_uuid": 539axxxx-xxxx-xxxx-xxxx-xxxxxxxxx4d2,
 "document": {
   "source": "&#x3C;title>Terms of Use&#x3C;/title>&#x3C;body>&#x3C;h1>Privacy Policy&#x3C;/h1>&#x3C;p>Avaamo, Inc. ('Avaamo') provides this Privacy Policy to inform you of our policies and procedures regarding the collection, use and disclosure of Personally Identifiable Information that we may obtain through the use of Avaamo products such as Avaamo Platform ('Software'), applications such as Avaamo Messenger ('Application'), and access to www.avaamo.com, referred to as ('Site').&#x3C;/p>&#x3C;/body>",
   "name": "Terms of Use",
   "parsing_template_id": 6,
   "type": "html",
   "preview_url": "https://avaamo.ai/privacy/"
 }
}
</code></pre></td></tr></tbody></table>

## Upload different types of files (pdf, docx, pptx, xlsx, csv, html) to LLaMB

{% hint style="info" %}
**Note:**&#x20;

1. The rate limit for upload-file API is capped to 50 uploads per minute. Contact Avaamo Support with your use-case details if you wish to increase the rate limit for the API.&#x20;
2. Replace `{{instance-name}}` with your actual instance name, such as `c6,` `h1`.
   {% endhint %}

<mark style="color:green;">`POST`</mark> `https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/upload-file`

#### Headers

<table><thead><tr><th width="221">Name</th><th width="104">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>String</td><td><p>Unique access token of the user. <br></p><p>You can get the user access token from the Settings -> Users page.  See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr></tbody></table>

#### Request Body

<table><thead><tr><th width="224">Name</th><th width="107">Type</th><th>Description</th></tr></thead><tbody><tr><td>document_group_id<mark style="color:red;">*</mark></td><td>Number</td><td><p>Unique identifier for the document group.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. See <a href="../../get-started/step-2-ingest-enterprise-content/create-document-groups#view-edit-a-document-group">View or edit document groups</a>, for more information.<br><br><strong>Note:</strong> You can use either the <code>document_group_id</code> or a combination of <code>agent_id</code> and <code>document_group_uuid</code> in the request body. Both approaches are supported.</p></td></tr><tr><td>agent_id</td><td>Number</td><td><p>Agent identifier.<br></p><p>You can get the agent identifier from the agent URL.</p></td></tr><tr><td>document_group_uuid</td><td>String</td><td><p>Unique user identifier for the document group.</p><p></p><p>You can get the document group UUID from the Document group -> View/Edit page. See <a href="../../get-started/step-2-ingest-enterprise-content/create-document-groups#view-edit-a-document-group">View or edit document groups</a>, for more information.</p></td></tr><tr><td>name</td><td>String </td><td><p>Name of the file.</p><p>Max length: 255 characters. </p></td></tr><tr><td>type</td><td>String</td><td><p>Type of the document. </p><p>Supported types: pdf, docx, pptx, xlsx, csv</p></td></tr><tr><td>attributes</td><td>Key-value</td><td><p>Define attributes for the uploaded documents or URLs in your LLaMB skill to facilitate disambiguation or filtering. </p><p></p><p>Example: <code>"attributes": {"key": "value"}</code></p><p></p><p>Attributes can be metadata of the document. You define attributes in key-value pairs. See <a href="../get-started/step-2-ingest-enterprise-content/document-attributes">Document attributes</a>, for more information.</p></td></tr><tr><td>language</td><td>String</td><td>This refers to the file's language. If you specify a language during ingestion, LLaMB uses that language to extract the content.<br><br>If you set auto_detect_language to true, LLaMB automatically detects the document’s language and processes it accordingly.</td></tr><tr><td>source<mark style="color:red;">*</mark></td><td>String</td><td>The actual file that you wish to upload. Source is the file path location of the document.</td></tr><tr><td>preview_url<mark style="color:red;">*</mark></td><td>String</td><td><p>Display URL that needs to be opened when the user clicks the source citation link in the response. </p><p></p><p>Mandatory only for uploading HTML files.</p><p></p><p>You can get the preview_url from the Document group -> Document -> View/Edit page. </p></td></tr><tr><td>document -> parsing_template_id</td><td>Integer</td><td><p>Specify the parsing template identifier that must be used to parse the document. You can get the identifier from the <a href="../get-started/step-2-ingest-enterprise-content/parsing-templates">Parsing template</a> page<br><br>Default value: The default parsing template identifier is used. </p><p></p><p>It is recommended to create the parsing template in the Parsing template page and use the parsing_template_id in the API payload.</p></td></tr><tr><td>document -> auto_detect_language</td><td>String</td><td>If a user wants to upload a non-English document, LLaMB automatically detects its language if you set it to <code>true.</code></td></tr></tbody></table>

{% tabs %}
{% tab title="200: OK Successful request" %}

```javascript
{
    "MACPIZZA_Policy.pdf": {
        "status": true,
        "response_text": {
            "id": 85xxx,
            "name": "MACPIZZA_Policy.pdf",
            "uuid": "1b0d1416-xxxx-48df-xxxx-f013e72fce9f",
            "document_type": "pdf",
            "status": "UPLOADED",    
            "document_group": 1058,
            "source_url": null,
            "source_file": "<<source_file_URL_path>>",
            "preview_url": null,
            "document_properties": null,
            "parsing_template": 12,
            "file_type": "application/pdf",
            "last_error": null,
            "updated_at": "2024-02-26T08:24:02.771628Z",
            "created_at": "2024-02-26T08:24:02.771606Z",
            "updated_by": "John Miller"
        }
    }
}
```

{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Key points**:

* The maximum request size should not exceed 5 MB. Contact Avaamo Support, if the size exceeds the limit.
* You can upload only one file at a time.
* Password-protected PDFs are not supported.
  {% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location 'https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/upload-file' \
--header 'access-token: 8ce05739e61f48829a47xxxxxxxxxxxx' \
--form 'source=@"o5pyxxxxx/MACPIZZA Policy.pdf"' \
--form 'document_group_id="10xx"' \
--form 'type="pdf"'
```

{% endcode %}
{% endtab %}

{% tab title="node.JS" %}
{% code overflow="wrap" %}

```javascript
var request = require('request');
var fs = require('fs');
var options = {
  'method': 'POST',
  'url': 'https://cx.avaamo.com/llamb-content-skill/content-ingestion/upload-file',
  'headers': {
    'access-token': '8ce05739e61f48829a47xxxxxxxxxxxx'
  },
  formData: {
    'source': {
      'value': fs.createReadStream('o5pyxxxxx/MACPIZZA Policy.pdf'),
      'options': {
        'filename': '',
        'contentType': null
      }
    },
    'document_group_id': '10xx',
    'type': 'pdf'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});

```

{% endcode %}
{% endtab %}
{% endtabs %}

### Response attributes

The following is a sample API response for uploading a document:

{% code overflow="wrap" %}

```json
{
    "MACPIZZA_Policy.pdf": {
        "status": true,
        "response_text": {
            "id": 85xxx,
            "name": "MACPIZZA_Policy.pdf",
            "uuid": "1b0d1416-xxxx-48df-xxxx-f013e72fce9f",
            "document_type": "pdf",
            "status": "UPLOADED",
            "document_group": 1058,
            "source_url": null,
            "source_file": "<<source_file_URL_path>>",
            "preview_url": null,
            "document_properties": null,
            "parsing_template": 12,
            "file_type": "application/pdf",
            "last_error": null,
            "updated_at": "2024-02-26T08:24:02.771628Z",
            "created_at": "2024-02-26T08:24:02.771606Z",
            "updated_by": "John Miller"
        }
    }
}
```

{% endcode %}

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th width="222">Attribute</th><th width="406.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>status</td><td>true if the document was updated successfully</td><td>Boolean</td></tr><tr><td>response_text -> id</td><td>Unique document identifier</td><td>Integer</td></tr><tr><td>response_text -> name</td><td>Document name</td><td>String</td></tr><tr><td>response_text -> uuid</td><td>Unique internal identifier of the document. </td><td>String</td></tr><tr><td>response_text -> document_type</td><td>Type of the document uploaded</td><td>String</td></tr><tr><td>response_text -> status</td><td><p>Status can be any one of the following values: Uploaded, Queued, Extracting, Learning, Complete, Error, or Warning.</p><p></p><p>See <a href="#document-status">Status</a>, for more information.</p></td><td>String</td></tr><tr><td>response_text -> document_group</td><td>Group identifier of the updated document.</td><td>Integer</td></tr><tr><td>response_text -> source_url</td><td>Source of the URL used for uploading the document.</td><td>String</td></tr><tr><td>response_text -> source_file</td><td>Source of the file used for uploading the document.</td><td>String</td></tr><tr><td>response_text -> preview_url</td><td>Preview URL of the updated document.</td><td>String</td></tr><tr><td>response_text -> created_at</td><td>Created Datetime of file</td><td>String</td></tr><tr><td>response_text -> file_type</td><td>Type of file uploaded </td><td>String</td></tr><tr><td>response_text -> parsing_template</td><td>Parsing template used to upload file</td><td>Integer</td></tr><tr><td>response_text -> updated_at</td><td>Updated Datetime of file</td><td>String</td></tr><tr><td>response_text -> updated_by</td><td>User who updated the file</td><td>String</td></tr><tr><td>last_error</td><td>Last error encountered with respect to the document</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases for uploading a document to LLaMB:

<table><thead><tr><th width="236.9472199894152">Use case</th><th width="498.34526508220097">Request payload</th></tr></thead><tbody><tr><td>Uploading a pdf document</td><td><pre class="language-bash" data-overflow="wrap"><code class="lang-bash"><strong>curl --location 'https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/upload-file' \
</strong>--header 'access-token: 8ce05739e61f48829a47xxxxxxxxxxxx' \
--form 'source=@"o5pyxxxxx/MACPIZZA Policy.pdf"' \
--form 'document_group_id="10xx"' \
--form 'type="pdf"'\
--form 'attribute="{\"country\" : \"Japan\"}"'
</code></pre></td></tr><tr><td>Uploading a html file</td><td><pre class="language-bash" data-overflow="wrap"><code class="lang-bash">curl --location 'https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/upload-file'
--header 'access-token: 5b190f6c144xxxxxxxxxxxxxxxxxx'
--form 'source=@"o5pyxxxxx/MACPIZZA Policy.html"' 
--form 'document_group_id="6xxx"'
--form 'type="html"'
--form 'preview_url="https://avaamo.ai/privacy/"'
</code></pre></td></tr><tr><td>Uploading a html file using <code>agent_id</code> and <code>document_group_uuid</code> </td><td><pre class="language-bash" data-overflow="wrap"><code class="lang-bash">curl --location 'https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/upload-file'
--header 'access-token: 5b190f6c144xxxxxxxxxxxxxxxxxx'
--form 'source=@"o5pyxxxxx/MACPIZZA Policy.html"' 
--form 'agent_id="7xxx"'
--form 'document_group_uuid="539axxxx-xxxx-xxxx-xxxx-xxxxxxxxx4d2"'
--form 'type="html"'
--form 'preview_url="https://avaamo.ai/privacy/"'
</code></pre></td></tr></tbody></table>

## Delete the document from the specified document group&#x20;

<mark style="color:red;">`DELETE`</mark> `https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/delete-document`

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | String | <p>The user access token. <br></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information </p><p></p><p>User must have at least edit permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information on agent permissions.</p> |
| content-type                                   | String | application/JSON                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

#### Request Body

| Name                                                  | Type    | Description                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| document\_group\_id<mark style="color:red;">\*</mark> | Integer | <p>Unique identifier of the document group from which you wish to delete a document.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. See <a href="../get-started/step-2-ingest-enterprise-content/create-document-groups">Create document groups</a>, for more information.</p> |
| document\_id<mark style="color:red;">\*</mark>        | Integer | <p>Unique identifier of the document that you wish to delete from the document group.</p><p></p><p>You can get the document\_id from the Document group -> Document -> Edit pop-up window. See <a href="../../get-started/step-2-ingest-enterprise-content/common-actions#edit">Edit document</a>, for more information.</p>      |

{% tabs %}
{% tab title="200: OK Successful request" %}

```json
{
    "82xxx": {
        "status": true,
        "response_text": {
            "id": null,
            "name": "Privacy policy",
            "uuid": "1a35c363-xxxx-xxxx-xxxx-aa26b14fc6ef",
            "document_type": "url",
            "status": "COMPLETE",
            "document_group": 10xx,
            "source_url": "https://avaamo.ai/privacy-policy/",
            "source_file": null,
            "preview_url": null,
            "document_properties": "",
            "parsing_template": 6,
            "file_type": "url",
            "last_error": null,
            "updated_at": "2024-02-16T06:02:13.199489Z",
            "created_at": "2024-02-16T06:01:07.934949Z",
            "updated_by": "John Miller"
        }
    }
}
```

{% endtab %}

{% tab title="400: Bad Request Bad request indicates payload is wrong" %}

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location --request DELETE 'https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/delete-document' \
--header 'access-token: xxxxxxxxx61f48829a47ccd9xxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{ 
"document_id": 82xxx,
"document_group_id": 10xx
}'
```

{% endcode %}
{% endtab %}

{% tab title="node.JS" %}
{% code overflow="wrap" %}

```javascript
var request = require('request');
var options = {
  'method': 'DELETE',
  'url': 'https://cx.avaamo.com/llamb-content-skill/content-ingestion/delete-document',
  'headers': {
    'access-token': 'xxxxxxxxx61f48829a47ccd9xxxxxxxx',
    'Content-Type': 'application/json',
  },
  body: '{ \n"document_id": 82xxx,\n"document_group_id": 10xx'

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Response attributes

The following is a sample API response for uploading a document:

```json
{
    "82xxx": {
        "status": true,
        "response_text": {
            "id": null,
            "name": "Privacy policy",
            "uuid": "1a35c363-xxxx-xxxx-xxxx-aa26b14fc6ef",
            "document_type": "url",
            "status": "COMPLETE",
            "document_group": 10xx,
            "source_url": "https://avaamo.ai/privacy-policy/",
            "source_file": null,
            "preview_url": null,
            "document_properties": "",
            "parsing_template": 6,
            "file_type": "url",
            "last_error": null,
            "updated_at": "2024-02-16T06:02:13.199489Z",
            "created_at": "2024-02-16T06:01:07.934949Z",
            "updated_by": "John Miller"
        }
    }
}
```

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th width="223">Attribute</th><th width="406.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>status</td><td>true if the document was deleted successfully</td><td>Boolean</td></tr><tr><td>response_text -> id</td><td>Unique document identifier</td><td>Integer</td></tr><tr><td>response_text -> name</td><td>Document name</td><td>String</td></tr><tr><td>response_text -> uuid</td><td>Unique internal identifier of the document. </td><td>String</td></tr><tr><td>response_text -> document_type</td><td>Type of the document uploaded</td><td>String</td></tr><tr><td>response_text -> document_properties</td><td>Document attributes, if any.</td><td>JSON</td></tr><tr><td>response_text -> status</td><td><p>Status can be any one of the following values: Uploaded, Queued, Extracting, Learning, Complete, Error, or Warning.</p><p></p><p>See <a href="#document-status">Status</a>, for more information.</p></td><td>String</td></tr><tr><td>response_text -> document_group</td><td>Group identifier of the deleted document</td><td>Integer</td></tr><tr><td>response_text -> source_url</td><td>Source of the URL used for uploading the document.</td><td>String</td></tr><tr><td>response_text -> source_file</td><td>Source of the file used for uploading the document.</td><td>String</td></tr><tr><td>response_text -> preview_url</td><td>Preview URL of the deleted document.</td><td></td></tr><tr><td>response_text -> created_at</td><td>Created datetime of document</td><td>String</td></tr><tr><td>response_text -> file_type</td><td>Type of file uploaded </td><td>String</td></tr><tr><td>response_text -> parsing_template</td><td>Parsing template used to upload document</td><td>Integer</td></tr><tr><td>response_text -> updated_at</td><td>Last updated datetime of file</td><td>String</td></tr><tr><td>response_text -> updated_by</td><td>User who updated the file</td><td>String</td></tr><tr><td>last_error</td><td>Last error encountered with respect to the document</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases for deleting a document from the `LLaMB Content` skill:

<table><thead><tr><th>Use case</th><th>Request payload</th></tr></thead><tbody><tr><td>Delete a document from a document group</td><td><p></p><pre class="language-json"><code class="lang-json">{ 
"document_id": 82xxxx,
"document_group_id": 10xx
}
</code></pre></td></tr></tbody></table>

## Update the document name or document preview URL&#x20;

<mark style="color:orange;">`PUT`</mark> `https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/update-document`

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| access-token<mark style="color:red;">\*</mark> | String | <p>Unique access token of the user. <br></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |
| content-type                                   | String | application/JSON                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

#### Request Body

| Name                                                       | Type        | Description                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| document\_group\_id<mark style="color:red;">\*</mark>      | Number      | <p>Unique identifier for the document group.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. </p><p></p><p>See <a href="../get-started/step-2-ingest-enterprise-content/create-document-groups">Create document groups</a>, for more information.</p>                      |
| document<mark style="color:red;">\*</mark>                 | JSON Object | Document object that needs to be updated.                                                                                                                                                                                                                                                                                    |
| document -> name                                           | String      | <p>Name of the document.</p><p>Max length: 255 characters. </p>                                                                                                                                                                                                                                                              |
| document -> preview\_url                                   | String      | URL that needs to be opened when user clicks in the response. See [Create document groups](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/create-document-groups), for more information.                                                                                              |
| document -> document\_id<mark style="color:red;">\*</mark> | Integer     | <p>Unique identifier of the document that you wish to update from the document group.</p><p></p><p>You can get the document\_id from the Document group -> Document -> Edit pop-up window. See <a href="../../get-started/step-2-ingest-enterprise-content/common-actions#edit">Edit document</a>, for more information.</p> |

{% tabs %}
{% tab title="200: OK Successful request" %}

```json
{
    "https://docs.avaamo.com/user-guide/": {
        "status": true,
        "response_text": {
            "id": 194636,
            "name": "Avaamo User Manual",
            "uuid": "8459623c-5df4-45ec-bc0c-831c6eaa08e9",
            "document_type": "url",
            "status": "COMPLETE",
            "document_group": 3455,
            "source_url": "https://docs.avaamo.com/user-guide/",
            "source_file": null,
            "preview_url": null,
            "document_properties": null,
            "parsing_template": 6,
            "file_type": "url",
            "last_error": null,
            "updated_at": "2023-07-18T10:49:20.486860Z",
            "created_at": "2023-07-18T10:48:06.145736Z",
            "updated_by": "John Miller"
        }
    }
}
```

{% endtab %}

{% tab title="400: Bad Request Bad request indicates payload is wrong" %}

{% endtab %}
{% endtabs %}

### Code request snippets <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location --request PUT 'https://{{instance-name}}.avaamo.com/llamb-content-skill/content-ingestion/update-document' \
--header 'access-token: xxxxxxxxx61f48829a47ccd9xxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "document_group_id": 10xx,
  "document": {
    "document_id": 82xxx,
    "name": "Avaamo Privacy Policy"
  }
}'
```

{% endcode %}
{% endtab %}

{% tab title="node.JS" %}
{% code overflow="wrap" %}

```javascript
var request = require('request');
var options = {
  'method': 'PUT',
  'url': 'https://cx.avaamo.com/llamb-content-skill/content-ingestion/update-document',
  'headers': {
    'access-token': 'xxxxxxxxx61f48829a47ccd9xxxxxxxx',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    "document_group_id": 10xx,
    "document": {
      "document_id": 82xxx,
      "name": "Avaamo Privacy Policy"
    }
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});

```

{% endcode %}
{% endtab %}
{% endtabs %}

### Response attributes

The following is a sample API response for updating the document:

```json
 {
    "82xxx": {
        "status": true,
        "response_text": {
            "id": 82xxx,
            "name": "Avaamo Privacy Policy",
            "uuid": "f9a5bd9d-xxxx-xxxx-xxxx-581304c847e1",
            "document_type": "url",
            "status": "COMPLETE",
            "document_group": 10xx,
            "source_url": "https://avaamo.ai/privacy-policy/",
            "source_file": null,
            "preview_url": null,
            "parsing_template": 6,
            "file_type": "url",
            "last_error": null,
            "updated_at": "2024-02-16T07:04:09.070652Z",
            "created_at": "2024-02-16T06:54:20.278755Z",
            "updated_by": "John Miller"
        }
    }
}
```

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th width="223">Attribute</th><th width="406.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>status</td><td>true if the document was updated successfully</td><td>Boolean</td></tr><tr><td>response_text -> id</td><td>Unique document identifier</td><td>Integer</td></tr><tr><td>response_text -> name</td><td>Document name</td><td>String</td></tr><tr><td>response_text -> uuid</td><td>Unique internal identifier of the document. </td><td>String</td></tr><tr><td>response_text -> document_type</td><td>Type of the document uploaded</td><td>String</td></tr><tr><td>response_text -> status</td><td><p>Status can be any one of the following values: Uploaded, Queued, Extracting, Learning, Complete, Error, or Warning.</p><p></p><p>See <a href="#document-status">Status</a>, for more information.</p></td><td>String</td></tr><tr><td>response_text -> document_group</td><td>Group identifier of the updated document.</td><td>Integer</td></tr><tr><td>response_text -> source_url</td><td>Source of the URL used for uploading the document.</td><td>String</td></tr><tr><td>response_text -> source_file</td><td>Source of the file used for uploading the document.</td><td>String</td></tr><tr><td>response_text -> preview_url</td><td>Preview URL of the updated document.</td><td>String</td></tr><tr><td>response_text -> created_at</td><td>Created Datetime of file</td><td>String</td></tr><tr><td>response_text -> file_type</td><td>Type of file uploaded </td><td>String</td></tr><tr><td>response_text -> parsing_template</td><td>Parsing template used to upload file</td><td>Integer</td></tr><tr><td>response_text -> updated_at</td><td>Updated Datetime of file</td><td>String</td></tr><tr><td>response_text -> updated_by</td><td>User who updated the file</td><td>String</td></tr><tr><td>last_error</td><td>Last error encountered with respect to the document</td><td>String</td></tr></tbody></table>

### Examples

<table><thead><tr><th width="233.0677598735653">Use case</th><th>Request payload</th></tr></thead><tbody><tr><td>Update the name of the document</td><td><p></p><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
  "document_group_id": 10xx,
  "document": {
    "document_id": 82xxx,
    "name": "Avaamo Privacy Policy"
  }
}
</code></pre></td></tr><tr><td>Update the preview URL of the document</td><td><p></p><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
  "document_group_id": 10xx,
  "document": {
    "document_id": 82xxx,
    "preview_url": "https://avaamo.ai/gdpr-compliance/"
  }
}
</code></pre></td></tr></tbody></table>

## Document Status&#x20;

The `Status` can be any of the following values based on the status of the uploaded content:&#x20;

* **Uploaded:** The document has been added to the skill.
* **Queued:** The content is placed in a queue for further processing.
* **Extracting**: Chunks of content are being extracted.
* **Learning:** Acronyms and vocabulary are being generated.
* **Complete**: The document is uploaded successfully. The extracted knowledge from the document is populated and ready to be used by any agent. See [View and Edit Knowledge](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/view-and-edit-knowledge), for more information.
* **Error**: The upload has errored out. In case of errors, you can click `Error` in the `Status` column to view more details. See [Troubleshooting tips](https://docs.avaamo.com/user-guide/llamb/troubleshooting-tips), for more information.
* **Warning:** No business vocabulary was found in the document.
