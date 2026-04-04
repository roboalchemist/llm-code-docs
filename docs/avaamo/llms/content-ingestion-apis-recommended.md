# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/answers-rest-apis/content-ingestion-apis-recommended.md

# Content ingestion APIs (Recommended)

## Upload document (HTML, URL) to the Answers knowledge base

<mark style="color:green;">`POST`</mark> `https://mx.avaamo.com/content-ingestion/parse-document`

#### Path Parameters

| Name                                            | Type | Description                                                                                                                                            |
| ----------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mx.avaamo.com<mark style="color:red;">\*</mark> | URL  | <p>Avaamo instance where the data is to be uploaded. Example: <https://m0.avaamo.com></p><p></p><p>Contact Avaamo Support to know the server name.</p> |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | String | <p>Unique access token of the user. <br></p><p>You can get the user access token from the Settings -> Users page.  See <a href="../../../../../manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../../manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../../../build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |
| content-type<mark style="color:red;">\*</mark> | json   | application/json                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

#### Request Body

| Name                                                                | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| document\_group\_id<mark style="color:red;">\*</mark>               | Number      | <p>Unique identifier for the document group.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. See <a href="../../manage-avaamo-answers-1/create-document-groups#view-edit-a-document-group">View or edit document groups</a>, for more information.</p>                                                                                                                                                                                                                                                                                                                                                                                                |
| document<mark style="color:red;">\*</mark>                          | JSON Object | Document object that needs to be uploaded                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| document -> name<mark style="color:red;">\*</mark>                  | String      | <p>Name of the document.</p><p>Max length: 255 characters. </p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| document -> type<mark style="color:red;">\*</mark>                  | String      | <p>Type of the document. </p><p>Supported values: html, url</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| document -> content                                                 | String      | <p>Content of the document HTML body/Text/Base64 text of PDF file. </p><p></p><p>This field is mandatory for HTML document types but not required for URLs. </p><p></p><p>Content must in the format: </p><p><code>\<title>Name of document\</title>\<body>valid html content\</body></code></p>                                                                                                                                                                                                                                                                                                                                                                                                        |
| document -> attributes                                              | Key-value   | <p>Define attributes for the uploaded documents or URLs in your Answers skill to facilitate disambiguation or filtering. </p><p></p><p>Attributes can be metadata of the document. You define attributes in key-value pairs. See <a href="../../manage-avaamo-answers-1/perform-common-actions#defining-attributes-for-documents-or-urls">Defining attributes for documents or URLs</a>, for more information. </p>                                                                                                                                                                                                                                                                                     |
| document -> preview\_url<mark style="color:red;">\*</mark>          | String      | <p>URL that needs to be opened when the user clicks in the response. </p><p></p><p>You can get the preview\_url from the Document group -> Document -> View/Edit page. </p><p></p><p></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| document -> language                                                | String      | <p>Language of the document.</p><p>Default value: en-US</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| document -> parsing\_template                                       | JSON        | <p>Template to be used to parse the document. This is a JSON file that can be configured as a template while parsing a URL with the purpose of better extraction of content from the URL during the parsing process. </p><p></p><p>Default value: default parsing template</p><p></p><p>Contact Avaamo Support to get access to the parsing template repository.  </p><p></p><p>Note instead of defining the parsing template in the document -> parsing\_template object, it is recommended to create the parsing template in the Parsing template page and use the parsing\_template\_id in the API payload. See  <a href="../parsing-templates">Parsing template page</a>, for more information.</p> |
| document -> parsing\_template\_id<mark style="color:red;">\*</mark> | String      | <p>Specify the parsing template identifier that must be used to parse the document. You can get the identifier from the <a href="../parsing-templates">Parsing template page</a>. </p><p></p><p>Default value: default parsing template identifier is used. </p><p></p><p>Note instead of defining the parsing template in the document -> parsing\_template object, it is recommended to create the parsing template in the Parsing template page and use the parsing\_template\_id in the API payload.</p>                                                                                                                                                                                            |
| parsing\_template -> template\_json                                 | JSON        | Custom template to parse a URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| parsing\_template -> key                                            | String      | Key for inbuilt parsing template, if not provided custom template is used. See [Parsing template](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/parsing-templates#inbuilt-parsing-templates), for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

{% tabs %}
{% tab title="201: Created Successful request" %}

```json
{
    "chunks": 1,
    "response_text": {
        "created_at": "2022-04-04T06:07:06.429408Z",
        "document_group": 887,
        "document_properties": null,
        "document_type": "url",
        "file_type": "url",
        "id": 17472,
        "language": 1,
        "language_string": "English (en-US)",
        "last_error": null,
        "name": "Avaamo Docs",
        "parsing_template": 6,
        "preview_url": null,
        "source_file": null,
        "source_url": "https://docs.avaamo.com/user-guide/",
        "status": "UPLOADED",
        "updated_at": "2022-08-01T10:03:53.585745Z",
        "updated_by": "John Miller",
        "uuid": "9ffb4cbb-f62d-4757-b7b7-70b67ca4d0cc"
    },
    "status": true// Response
}
```

{% endtab %}

{% tab title="400: Bad Request Bad request indicates payload is wrong" %}

{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Key points**:

* Ensure that the right content is posted during upload as the HTML content is sanitized before processing.
* All content must be present in the following tags: "h1", "h2", "h3", "h4", "h5", "p", "img", "span", "td", "figure", "ol", "ul", "dd", "dt", "a", "table", "details", "summary". This list can be modified by using parsing templates.
* The maximum request size should not exceed 5 MB. Contact Avaamo Support, if the size exceeds the limit.
* Password-protected PDFs are not supported.
* The images inside HTML must be base64 encoded or must be public images.
  {% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location 'https://mx.avaamo.com/content-ingestion/parse-document' \
--header 'access-token: xxxxxx39e61f48829a47ccd9e6xxxxxx' \
--header 'Content-Type: application/json' \
--data '{ 
    "document_group_id": 35xx, 
     "api_server": "https://mx.avaamo.com", 
      "document": { 
         "name": "Avaamo Docs", 
          "type": "url", 
          "preview_url": "https://docs.avaamo.com/user-guide/", 
          "parsing_template_id":"6"
     } 
}'
```

{% endcode %}
{% endtab %}

{% tab title="node.JS" %}

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://mx.avaamo.com/content-ingestion/parse-document',
  'headers': {
    'access-token': 'xxxxxx39e61f48829a47ccd9e6xxxxxx',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "document_group_id": 35xx,
    "api_server": "https://mx.avaamo.com",
    "document": {
      "name": "Avaamo Docs",
      "type": "url",
      "preview_url": "https://docs.avaamo.com/user-guide/",
      "parsing_template_id": "6"
    }
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});


```

{% endtab %}
{% endtabs %}

### Response attributes

The following is a sample API response for uploading a document:

```json
{
    "https://docs.avaamo.com/user-guide/": {
        "status": true,
        "chunks": 4,
        "response_text": {
            "id": 203021,
            "name": "Avaamo Docs",
            "uuid": "0ffa5161-1adb-479e-b5a1-4035fxxxxxx",
            "document_type": "url",
            "status": "QUEUED",
            "language": 1,
            "language_string": "English (en-US)",
            "document_group": 35xx,
            "source_url": "https://docs.avaamo.com/user-guide/",
            "source_file": null,
            "preview_url": null,
            "document_properties": null,
            "parsing_template": 6,
            "file_type": "url",
            "last_error": null,
            "updated_at": "2023-07-20T12:28:04.639826Z",
            "created_at": "2023-07-20T12:28:04.512307Z",
            "updated_by": "John Miller"
        }
    }
}
```

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th width="217">Attribute</th><th width="426.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>chunks</td><td>Chunks of the uploaded document </td><td>Integer</td></tr><tr><td>response_text -> created_at</td><td>Created Datetime of document</td><td>String</td></tr><tr><td>response_text -> document_group</td><td>Knowledge pack identifier where document is uploaded</td><td>String</td></tr><tr><td>response_text -> document_type</td><td>Type of the document uploaded</td><td>String</td></tr><tr><td>response_text -> document_properties</td><td>Document attributes, if any.</td><td>JSON </td></tr><tr><td>response_text -> file_type</td><td>Type of file uploaded </td><td>String</td></tr><tr><td>response_text -> id</td><td>Document identifier</td><td>String</td></tr><tr><td>response_text -> language</td><td>Document language identifier</td><td>String</td></tr><tr><td>response_text -> language_string</td><td>Document language code corresponding to the identifier</td><td>String</td></tr><tr><td>response_text -> name</td><td>Document name</td><td>String</td></tr><tr><td>response_text -> parsing_template</td><td>Parsing template used to upload document</td><td>String</td></tr><tr><td>response_text -> source_file</td><td>Source file of the uploaded document, if any.</td><td>String</td></tr><tr><td>response_text -> source_url</td><td>Source URL of the uploaded document, if any.</td><td>String</td></tr><tr><td>response_text -> status</td><td>UPLOADED/ERROR</td><td>String</td></tr><tr><td>response_text -> updated_at</td><td>Updated Datetime of document</td><td>String</td></tr><tr><td>response_text -> updated_by</td><td>User who updated the document</td><td>String</td></tr><tr><td>response_text -> uuid</td><td>Unique identifier of the uploaded document</td><td>String</td></tr><tr><td>status</td><td>true if the document was uploaded successfully</td><td>String</td></tr><tr><td>last_error</td><td>Last error encountered with respect to the document</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases for uploading a document to the Answers skill:

<table><thead><tr><th width="268.0422031374631">Use case</th><th width="498.34526508220097">Request payload</th></tr></thead><tbody><tr><td>Uploading a document using URL</td><td><p>{ </p><p>    "document_group_id": 1, </p><p>     "api_server": "https://mx.avaamo.com", </p><p>      "document": { </p><p>         "name": "Avaamo Docs", </p><p>          "type": "url", </p><p>          "preview_url": "https://docs.avaamo.com/user-guide/",</p><p>          "parsing_template_id": "6"</p><p>     } </p><p>}</p></td></tr><tr><td>Uploading a document using HTML</td><td><p>{</p><p> "document_group_id": 1,</p><p> "document": {</p><p>   "content": "&#x3C;title>Terms of Use&#x3C;/title>&#x3C;body>&#x3C;h1>Privacy Policy&#x3C;/h1>&#x3C;p>Avaamo, Inc. ('Avaamo') provides this Privacy Policy to inform you of our policies and procedures regarding the collection, use and disclosure of Personally Identifiable Information that we may obtain through the use of Avaamo products such as Avaamo Platform ('Software'), applications such as Avaamo Messenger ('Application'), and access to www.avaamo.com, referred to as ('Site').&#x3C;/p>&#x3C;/body>",</p><p>   "name": "Terms of Use",</p><p>   "parsing_template_id": 6,</p><p>   "type": "html",</p><p>   "preview_url": "https://avaamo.ai/privacy/",</p><p>   "attributes": {"product": {"value": "Avaamo", "priority": 0}}</p><p> }</p><p>}</p><p><br></p></td></tr></tbody></table>

## Upload different types of files (pdf, docx, pptx, xlsx) to the Answers knowledge base

<mark style="color:green;">`POST`</mark> `https://mx.avaamo.com/content-ingestion/upload-file`

#### Path Parameters

| Name                                            | Type | Description                                                                                                                                            |
| ----------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mx.avaamo.com<mark style="color:red;">\*</mark> | URL  | <p>Avaamo instance where the data is to be uploaded. Example: <https://m0.avaamo.com></p><p></p><p>Contact Avaamo Support to know the server name.</p> |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | String | <p>Unique access token of the user. <br></p><p>You can get the user access token from the Settings -> Users page.  See <a href="../../../../../manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../../manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../../../build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

#### Request Body

| Name                                                    | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| document\_group\_id<mark style="color:red;">\*</mark>   | Number      | <p>Unique identifier for the document group.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. See <a href="../../manage-avaamo-answers-1/create-document-groups#view-edit-a-document-group">View or edit document groups</a>, for more information.</p>                                                                                                                                                                                                                                                                                                                                                                                                |
| name                                                    | String      | <p>Name of the file.</p><p>Max length: 255 characters. </p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| type                                                    | String      | <p>Type of the file. </p><p></p><p>Supported types: pdf, docx, pptx, xlsx</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| attributes                                              | Key-value   | <p>Define attributes for the uploaded file in your Answers skill to facilitate disambiguation or filtering. </p><p></p><p>Attributes can be metadata of the document. You define attributes in key-value pairs. See <a href="../../manage-avaamo-answers-1/perform-common-actions#defining-attributes-for-documents-or-urls">Defining attributes for documents or URLs</a>, for more information. </p>                                                                                                                                                                                                                                                                                                  |
| language                                                | String      | <p>Language of the uploaded file.</p><p>Default value: en-US</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| parsing\_template                                       | JSON        | <p>Template to be used to parse the document. This is a JSON file that can be configured as a template while parsing a URL with the purpose of better extraction of content from the URL during the parsing process. </p><p></p><p>Default value: default parsing template</p><p></p><p>Contact Avaamo Support to get access to the parsing template repository.  </p><p></p><p>Note instead of defining the parsing template in the document -> parsing\_template object, it is recommended to create the parsing template in the Parsing template page and use the parsing\_template\_id in the API payload. See  <a href="../parsing-templates">Parsing template page</a>, for more information.</p> |
| parsing\_template\_id<mark style="color:red;">\*</mark> | String      | <p>Specify the parsing template identifier that must be used to parse the document. Use the right parsing template according to type of file you are uploading. You can get the identifier from the <a href="../parsing-templates">Parsing template page</a>. </p><p></p><p>Default value: default parsing template identifier is used. </p><p></p><p>Note instead of defining the parsing template in the document -> parsing\_template object, it is recommended to create the parsing template in the Parsing template page and use the parsing\_template\_id in the API payload.</p>                                                                                                                |
| parsing\_template -> template\_json                     | JSON        | Custom template to parse a URL.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| parsing\_template -> key                                | String      | Key for inbuilt parsing template, if not provided custom template is used. See [Parsing template](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/parsing-templates#inbuilt-parsing-templates), for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| file<mark style="color:red;">\*</mark>                  | File object | The actual file that you wish to upload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| parsing\_lib                                            | String      | <p>parsing\_lib for pdf extraction. For tabular parsing use pdftotree. </p><p></p><p>Default: pdfbox</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

{% tabs %}
{% tab title="201: Created Successful request" %}

<pre class="language-json" data-overflow="wrap"><code class="lang-json"><strong>{
</strong>    "MACPIZZA_Policy.pdf": {
        "status": true,
        "response_text": {
            "id": 194658,
            "name": "MACPIZZA_Policy.pdf",
            "uuid": "2ff9d2e1-5897-4d2c-9c5d-5b5d9c144cb6",
            "document_type": "pdf",
            "status": "UPLOADED",
            "language": 1,
            "language_string": "English (en-US)",
            "document_group": 3455,
            "source_url": null,
            "source_file": "&#x3C;&#x3C;source_file_URL_path>>",
            "preview_url": null,
            "document_properties": null,
            "parsing_template": 8,
            "file_type": "application/pdf",
            "last_error": null,
            "updated_at": "2023-07-19T07:26:59.464093Z",
            "created_at": "2023-07-19T07:26:59.464025Z",
            "updated_by": "John Miller"
        }
    }
}
</code></pre>

{% endtab %}

{% tab title="400: Bad Request Bad request indicates payload is wrong" %}

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location 'https://mx.avaamo.com/content-ingestion/upload-file' \
--header 'Access-Token: xxxxxx39e61f488x47xxccd9e6xxxxxx' \
--form 'file=@"/Users/avaamo/Downloads/MacPizza_policy.docx"' \
--form 'document_group_id="34xx"' \
--form 'type="docx"' \
--form 'parsing_template_id="8x"' \
--form 'api_server="https://mx.avaamo.com"'
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
  'url': 'https://mx.avaamo.com/content-ingestion/upload-file',
  'headers': {
    'Access-Token': 'xxxxxx39e61f488x47xxccd9e6xxxxxx'
  },
  formData: {
    'file': {
      'value': fs.createReadStream('/Users/avaamo/Downloads/MacPizza_policy.docx'),
      'options': {
        'filename': 'MacPizza_policy.docx',
        'contentType': null
      }
    },
    'document_group_id': '34xx',
    'type': 'docx',
    'parsing_template_id': '8x',
    'api_server': 'https://mx.avaamo.com'
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
    "MacPizza_policy.docx": {
        "status": true,
        "response_text": {
            "id": 203002,
            "name": "MacPizza_policy.docx",
            "uuid": "d053xxxx-446f-xxxx-9f53-055cfxxxxxxx",
            "document_type": "docx",
            "status": "COMPLETE",
            "language": 1,
            "language_string": "English (en-US)",
            "document_group": 34xx,
            "source_url": null,
            "source_file": "<<source_file_URL_path>>",
            "preview_url": null,
            "document_properties": null,
            "parsing_template": 8x,
            "file_type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "last_error": null,
            "updated_at": "2023-08-07T08:39:27.079826Z",
            "created_at": "2023-07-20T09:49:39.163094Z",
            "updated_by": "John Miller"
        }
    }
}
```

{% endcode %}

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th width="191">Attribute</th><th width="406.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>status</td><td>true if the document was uploaded successfully</td><td>Boolean</td></tr><tr><td>response_text -> id</td><td>Unique file identifier</td><td>String</td></tr><tr><td>response_text -> name</td><td>File name</td><td>String</td></tr><tr><td>response_text -> uuid</td><td>Unique identifier of the uploaded file. This is for internal use only.</td><td>String</td></tr><tr><td>response_text -> document_type</td><td>Type of the document uploaded</td><td>String</td></tr><tr><td>response_text -> document_properties</td><td>Document attributes, if any.</td><td>JSON</td></tr><tr><td>response_text -> status</td><td>UPLOADED/ERROR</td><td>String</td></tr><tr><td>response_text -> language</td><td>Document language identifier</td><td>String</td></tr><tr><td>response_text -> language_string</td><td>Document language code corresponding to the identifier</td><td>String</td></tr><tr><td>response_text -> document_group</td><td>Knowledge pack identifier where file is uploaded</td><td>String</td></tr><tr><td>response_text -> source_file</td><td>Source of the uploaded file</td><td>String</td></tr><tr><td>response_text -> created_at</td><td>Created Datetime of file</td><td>String</td></tr><tr><td>response_text -> file_type</td><td>Type of file uploaded </td><td>String</td></tr><tr><td>response_text -> parsing_template</td><td>Parsing template used to upload file</td><td>String</td></tr><tr><td>response_text -> updated_at</td><td>Updated Datetime of file</td><td>String</td></tr><tr><td>response_text -> updated_by</td><td>User who updated the file</td><td>String</td></tr><tr><td>last_error</td><td>Last error encountered with respect to the document</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases for uploading a document to the Answers skill:

<table><thead><tr><th width="236.9472199894152">Use case</th><th width="498.34526508220097">Request payload</th></tr></thead><tbody><tr><td>Uploading a word document</td><td><pre class="language-bash" data-overflow="wrap"><code class="lang-bash">curl --location 'https://mx.avaamo.com/content-ingestion/upload-file' \
--header 'Access-Token: xxxxxx39e61f488x47xxccd9e6xxxxxx' \
--form 'file=@"/Users/avaamo/Downloads/MacPizza_policy.docx"' \
--form 'document_group_id="34xx"' \
--form 'type="docx"' \
--form 'parsing_template_id="8x"' \
--form 'api_server="https://mx.avaamo.com"'
</code></pre></td></tr></tbody></table>

## Delete the document from the specified document group in the Answers skill.

<mark style="color:red;">`DELETE`</mark> `https://mx.avaamo.com/content-ingestion/delete-document`

#### Path Parameters

| Name                                            | Type | Description                                                                                                                                            |
| ----------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mx.avaamo.com<mark style="color:red;">\*</mark> | URL  | <p>Avaamo instance where the data is to be uploaded. Example: <https://m0.avaamo.com></p><p></p><p>Contact Avaamo Support to know the server name.</p> |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| content-type<mark style="color:red;">\*</mark> | JSON   | application/json                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| access-token<mark style="color:red;">\*</mark> | String | <p>The user access token. <br></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../../manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../../manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information </p><p></p><p>User must have at least edit permission on the agent. See <a href="../../../../build-agents/configure-agents/permissions">Permissions</a>, for more information on agent permissions.</p> |

#### Request Body

| Name                                                  | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| document\_group\_id<mark style="color:red;">\*</mark> | String | <p>Unique identifier for the document group.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. See <a href="../manage-avaamo-answers-1/create-document-groups">Create document groups</a>, for more information.</p>                                                                                                                                                                                                                                                             |
| preview\_url                                          | String | <p>URL used to upload the document to the Answers skill. Use this if you have uploaded a document using a URL and wish to delete the document from the Answers skill. </p><p></p><p>You can get the preview URL from the Document group -> Document -> Edit pop-up window.  </p><p></p><p>You must specify either preview\_url or document\_id in the delete payload request. </p><p>See <a href="../manage-avaamo-answers-1/create-document-groups">Create document groups</a>, for more information.</p>                       |
| document\_id                                          | String | <p>Unique identifier of the uploaded document to the Answers skill. Use this if you have uploaded a document directly to the Answers skill and wish to delete the document from the Answers skill. </p><p></p><p>You can get the document\_id from the Document group -> Document -> Edit pop-up window.  See <a href="../manage-avaamo-answers-1/create-document-groups">Create document groups</a>, for more information.</p><p></p><p>You must specify either preview\_url or document\_id in the delete payload request.</p> |

{% tabs %}
{% tab title="200: OK Successful request" %}

<pre class="language-json"><code class="lang-json"><strong>{
</strong>    "https://docs.avaamo.com/user-guide/": {
        "response_text": {
            "created_at": "2023-07-18T10:34:10.750087Z",
            "document_group": 3455,
            "document_properties": "",
            "document_type": "url",
            "file_type": "url",
            "id": null,
            "language": 1,
            "language_string": "English (en-US)",
            "last_error": null,
            "name": "Avaamo Docs",
            "parsing_template": 6,
            "preview_url": "https://docs.avaamo.com/user-guide/",
            "source_file": null,
            "source_url": "https://docs.avaamo.com/user-guide/",
            "status": "COMPLETE",
            "updated_at": "2023-07-18T10:35:35.719236Z",
            "updated_by": "John Miller",
            "uuid": "c5164053-51e7-4687-98b5-363762d454ac"
        },
        "status": true
    }
}
</code></pre>

{% endtab %}

{% tab title="400: Bad Request Bad request indicates payload is wrong" %}

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location --request DELETE 'https://mx.avaamo.com/content-ingestion/delete-document' \
--header 'Content-Type: application/json' \
--header 'access-token: xxxxxxf69ba5497e96ff614b00xxxxxx' \
--data-raw '{
 "document_group_id": 999,
 "preview_url": "https://avaamo.ai/privacy-policy/"
}'
```

{% endcode %}
{% endtab %}

{% tab title="node.JS" %}

```javascript
var request = require('request');
var options = {
  'method': 'DELETE',
  'url': 'https://mx.avaamo.com/content-ingestion/delete-document',
  'headers': {
    'Content-Type': 'application/json',
    'access-token': 'xxxxxxf69ba5497e96ff614b00xxxxxx'
  },
  body: JSON.stringify({
    "document_group_id": 999,
    "preview_url": "https://avaamo.ai/privacy-policy/"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

{% endtab %}
{% endtabs %}

### Response attributes

The following is a sample API response for uploading a document:

```json
{
    "https://docs.avaamo.com/user-guide/": {
        "response_text": {
            "created_at": "2023-07-18T10:34:10.750087Z",
            "document_group": 3455,
            "document_properties": "",
            "document_type": "url",
            "file_type": "url",
            "id": null,
            "language": 1,
            "language_string": "English (en-US)",
            "last_error": null,
            "name": "Avaamo Docs",
            "parsing_template": 6,
            "preview_url": "https://docs.avaamo.com/user-guide/",
            "source_file": null,
            "source_url": "https://docs.avaamo.com/user-guide/",
            "status": "COMPLETE",
            "updated_at": "2023-07-18T10:35:35.719236Z",
            "updated_by": "John Miller",
            "uuid": "c5164053-51e7-4687-98b5-363762d454ac"
        },
        "status": true
    }
}
```

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th width="191">Attribute</th><th width="406.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>status</td><td>true if the document was uploaded successfully</td><td>Boolean</td></tr><tr><td>response_text -> id</td><td>Unique file identifier</td><td>String</td></tr><tr><td>response_text -> name</td><td>File name</td><td>String</td></tr><tr><td>response_text -> uuid</td><td>Unique identifier of the uploaded file. This is for internal use only.</td><td>String</td></tr><tr><td>response_text -> document_type</td><td>Type of the document uploaded</td><td>String</td></tr><tr><td>response_text -> document_properties</td><td>Document attributes, if any.</td><td>JSON</td></tr><tr><td>response_text -> status</td><td>UPLOADED/ERROR</td><td>String</td></tr><tr><td>response_text -> language</td><td>Document language identifier</td><td>String</td></tr><tr><td>response_text -> language_string</td><td>Document language code corresponding to the identifier</td><td>String</td></tr><tr><td>response_text -> document_group</td><td>Knowledge pack identifier where file is uploaded</td><td>String</td></tr><tr><td>response_text -> source_file</td><td>Source of the uploaded file</td><td>String</td></tr><tr><td>response_text -> created_at</td><td>Created Datetime of file</td><td>String</td></tr><tr><td>response_text -> file_type</td><td>Type of file uploaded </td><td>String</td></tr><tr><td>response_text -> parsing_template</td><td>Parsing template used to upload file</td><td>String</td></tr><tr><td>response_text -> updated_at</td><td>Updated Datetime of file</td><td>String</td></tr><tr><td>response_text -> updated_by</td><td>User who updated the file</td><td>String</td></tr><tr><td>last_error</td><td>Last error encountered with respect to the document</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases for deleting a document from the Answers skill:

| Use case                                             | Request payload                                                                                                                                      |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Delete a document that is uploaded using a URL       | <p>{ </p><p>"document\_group\_id": 999, </p><p>"api\_server": "<https://mx.avaamo.com>", "preview\_url": "<https://avaamo.ai/privacy/>" </p><p>}</p> |
| Delete a document uploaded that is uploaded directly | <p>{ </p><p>"document\_group\_id": 999, </p><p>"api\_server": "<https://mx.avaamo.com>",           "document\_id": 556 </p><p>}</p>                  |

## Update the document name and attributes

<mark style="color:orange;">`PUT`</mark> `https://mx.avaamo.com/content-ingestion/update-document`

#### Path Parameters

| Name                                            | Type | Description                                                                                                                                            |
| ----------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mx.avaamo.com<mark style="color:red;">\*</mark> | URL  | <p>Avaamo instance where the data is to be uploaded. Example: <https://m0.avaamo.com></p><p></p><p>Contact Avaamo Support to know the server name.</p> |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | String | <p>Unique access token of the user. <br></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../../manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../../manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../../../build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |
| content-type<mark style="color:red;">\*</mark> | JSON   | application/json                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

#### Request Body

| Name                                                       | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| document\_group\_id<mark style="color:red;">\*</mark>      | Number      | <p>Unique identifier for the document group.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. </p><p></p><p>See <a href="../manage-avaamo-answers-1/create-document-groups">Create document groups</a>, for more information.</p>                                                                                                                                 |
| document<mark style="color:red;">\*</mark>                 | JSON Object | Document object that needs to be uploaded                                                                                                                                                                                                                                                                                                                                                                          |
| document -> name                                           | String      | <p>Name of the document.</p><p>Max length: 255 characters. </p>                                                                                                                                                                                                                                                                                                                                                    |
| document -> attributes                                     | Key-value   | <p>Define attributes for the uploaded documents or URLs in your Answers skill to facilitate disambiguation or filtering. </p><p></p><p>Attributes can be metadata of the document. You define attributes in key-value pairs. See <a href="../../manage-avaamo-answers-1/perform-common-actions#defining-attributes-for-documents-or-urls">Defining attributes for documents or URLs</a>, for more information.</p> |
| document -> preview\_url<mark style="color:red;">\*</mark> | String      | URL that needs to be opened when user clicks in the response. See [Create document groups](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/create-document-groups), for more information.                                                                                                                                                       |

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
            "language": 1,
            "language_string": "English (en-US)",
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
curl --location --request PUT 'https://mx.avaamo.com/content-ingestion/update-document' \
--header 'access-token: xxxxxxf69ba5497e96ff614b00xxxxxx' \
--header 'Content-Type: application/json' \
--data-raw '{ 
 "document_group_id": 999,
 "document": {
   "name": "Terms of use",
   "type": "url",
   "preview_url": "https://avaamo.ai/privacy-policy/"
 }
}
'
```

{% endcode %}
{% endtab %}

{% tab title="node.JS" %}

```javascript
var request = require('request');
var options = {
  'method': 'PUT',
  'url': 'https://mx.avaamo.com/content-ingestion/update-document',
  'headers': {
    'access-token': 'xxxxxxf69ba5497e96ff614b00xxxxxx',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "document_group_id": 999,
    "document": {
      "name": "Terms of use",
      "type": "url",
      "preview_url": "https://avaamo.ai/privacy-policy/"
    }
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

{% endtab %}
{% endtabs %}

### Response attributes

The following is a sample API response for updating the document:

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
            "language": 1,
            "language_string": "English (en-US)",
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

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th width="191">Attribute</th><th width="406.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>status</td><td>true if the document was uploaded successfully</td><td>Boolean</td></tr><tr><td>response_text -> id</td><td>Unique file identifier</td><td>String</td></tr><tr><td>response_text -> name</td><td>File name</td><td>String</td></tr><tr><td>response_text -> uuid</td><td>Unique identifier of the uploaded file. This is for internal use only.</td><td>String</td></tr><tr><td>response_text -> document_type</td><td>Type of the document uploaded</td><td>String</td></tr><tr><td>response_text -> document_properties</td><td>Document attributes, if any.</td><td>JSON</td></tr><tr><td>response_text -> status</td><td>UPLOADED/ERROR</td><td>String</td></tr><tr><td>response_text -> language</td><td>Document language identifier</td><td>String</td></tr><tr><td>response_text -> language_string</td><td>Document language code corresponding to the identifier</td><td>String</td></tr><tr><td>response_text -> document_group</td><td>Knowledge pack identifier where file is uploaded</td><td>String</td></tr><tr><td>response_text -> source_file</td><td>Source of the uploaded file</td><td>String</td></tr><tr><td>response_text -> created_at</td><td>Created Datetime of file</td><td>String</td></tr><tr><td>response_text -> file_type</td><td>Type of file uploaded </td><td>String</td></tr><tr><td>response_text -> parsing_template</td><td>Parsing template used to upload file</td><td>String</td></tr><tr><td>response_text -> updated_at</td><td>Updated Datetime of file</td><td>String</td></tr><tr><td>response_text -> updated_by</td><td>User who updated the file</td><td>String</td></tr><tr><td>last_error</td><td>Last error encountered with respect to the document</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases for updating documents to the Answers skill:

<table><thead><tr><th width="247.99507811332592">Use case</th><th>Request payload</th></tr></thead><tbody><tr><td>Update the name of the document</td><td><p>{ </p><p>"document_group_id": 1, </p><p>"api_server": "https://mx.avaamo.com", "document": { </p><p>"name": "Avaamo User Manual", </p><p>"type": "url", </p><p>"preview_url": "https://docs.avaamo.com/user-guide/" </p><p>} </p><p>}</p></td></tr></tbody></table>
