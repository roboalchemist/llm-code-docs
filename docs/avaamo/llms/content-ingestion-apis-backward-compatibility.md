# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/answers-rest-apis/content-ingestion-apis-backward-compatibility.md

# Content ingestion APIs (Backward Compatibility)

{% hint style="danger" %}
**Note**: All the content ingestion APIs listed in the article are maintained solely for backward compatibility and are limited to support until version 6.4.0. However, these APIs will soon be marked as deprecated. Starting from version 7.0.0 onwards, it is recommended to transition to an enhanced and more efficient version of content ingestion APIs to ensure improved support. See [Content ingestion APIs (Recommended)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/answers-rest-apis/content-ingestion-apis-recommended), for more information.
{% endhint %}

## Upload document (HTML, URL) to the Answers knowledge base.

<mark style="color:green;">`POST`</mark> `https://answers-ingest.aiavaamo.com/api/document`

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | String | <p>Unique access token of the user. <br></p><p>You can get the user access token from the Settings -> Users page.  See <a href="../../../../../manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../../manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../../../build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |
| content-type<mark style="color:red;">\*</mark> | json   | application/json                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

#### Request Body

| Name                                                       | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| document\_group\_id<mark style="color:red;">\*</mark>      | Number      | <p>Unique identifier for the document group.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. See <a href="../../manage-avaamo-answers-1/create-document-groups#view-edit-a-document-group">View or edit document groups</a>, for more information.</p>                                                                                                            |
| api\_server<mark style="color:red;">\*</mark>              | String      | <p>Avaamo instance where the data is to be uploaded. Example: <https://mx.avaamo.com></p><p></p><p>Contact Avaamo Support to know the server name.</p>                                                                                                                                                                                                                                                              |
| document<mark style="color:red;">\*</mark>                 | JSON Object | Document object that needs to be uploaded                                                                                                                                                                                                                                                                                                                                                                           |
| document -> name<mark style="color:red;">\*</mark>         | String      | <p>Name of the document.</p><p>Max length: 255 characters. </p>                                                                                                                                                                                                                                                                                                                                                     |
| document -> type<mark style="color:red;">\*</mark>         | String      | <p>Type of the document. </p><p>Supported values: html, url</p>                                                                                                                                                                                                                                                                                                                                                     |
| document -> content                                        | String      | <p>Content of the document HTML body/Text/Base64 text of PDF file. </p><p></p><p>This field is mandatory for HTML document types but not required for URLs. </p><p></p><p>Content must in the format: </p><p><code>\<title>Name of document\</title>\<body>valid html content\</body></code></p>                                                                                                                    |
| document -> attributes                                     | Key-value   | <p>Define attributes for the uploaded documents or URLs in your Answers skill to facilitate disambiguation or filtering. </p><p></p><p>Attributes can be metadata of the document. You define attributes in key-value pairs. See <a href="../../manage-avaamo-answers-1/perform-common-actions#defining-attributes-for-documents-or-urls">Defining attributes for documents or URLs</a>, for more information. </p> |
| document -> preview\_url<mark style="color:red;">\*</mark> | String      | <p>URL that needs to be opened when the user clicks in the response. </p><p></p><p>You can get the preview\_url from the Document group -> Document -> View/Edit page. </p><p></p><p></p>                                                                                                                                                                                                                           |
| document -> language                                       | String      | <p>Language of the document.</p><p>Default value: en-US</p>                                                                                                                                                                                                                                                                                                                                                         |
| document -> parsing\_template                              | JSON        | <p>Template to be used to parse the document. This is a JSON file that can be configured as a template while parsing a URL with the purpose of better extraction of content from the URL during the parsing process. </p><p></p><p>Default value: default parsing template</p><p></p><p>Contact Avaamo Support to get access to the parsing template repository. </p>                                               |
| parsing\_template -> template\_json                        | JSON        | Custom template to parse a URL.                                                                                                                                                                                                                                                                                                                                                                                     |
| parsing\_template -> key                                   | String      | Key for inbuilt parsing template, if not provided custom template is used. See [Parsing template](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/parsing-templates#inbuilt-parsing-templates), for more information.                                                                                                                                                                           |

{% tabs %}
{% tab title="200: OK Successful request" %}

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
        "index_pages": 0,
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
{% endtabs %}

{% hint style="success" %}
**Key points**:

* Ensure that the right content is posted during upload as the HTML content is sanitized before processing.
* All content must be present in the following tags: "h1", "h2", "h3", "h4", "h5", "p", "img", "span", "td", "figure", "ol", "ul", "dd", "dt", "a", "table", "details", "summary". This list can be modified by using parsing templates.
* The maximum request size should not exceed 5 MB. Contact Avaamo Support, if the size exceeds the limit.
* Password-protected PDFs are not supported.
* The images inside HTML must be base64 encoded or must be public images.
  {% endhint %}

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request POST 'https://answers-ingest.aiavaamo.com/api/document' \
--header 'access-token: xxxxxxf69ba5497e96ff614b00xxxxxx' \
--header 'Content-Type: application/json' \
--data-raw '{ 
 "document_group_id": 999,
 "api_server": "https://mx.avaamo.com",
 "document": {
   "name": "Avaamo user guide",
   "type": "url",
   "preview_url": "https://docs.avaamo.com/user-guide/"
 }
}
'
```

{% endtab %}

{% tab title="node.JS" %}

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://answers-ingest.aiavaamo.com/api/document',
  'headers': {
    'access-token': 'xxxxxxf69ba5497e96ff614b00xxxxxx',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "document_group_id": 999,
    "api_server": "https://mx.avaamo.com",
    "document": {
      "name": "Avaamo user guide",
      "type": "url",
      "preview_url": "https://docs.avaamo.com/user-guide/"
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
    "chunks": 1,
    "response_text": {
        "created_at": "2022-04-04T06:07:06.429408Z",
        "document_group": 887,
        "document_properties": null,
        "document_type": "url",
        "file_type": "url",
        "id": 17472,
        "index_pages": 0,
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
    "status": true
}
```

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th width="217">Attribute</th><th width="426.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>chunks</td><td>Chunks of the uploaded document </td><td>Integer</td></tr><tr><td>response_text -> created_at</td><td>Created Datetime of document</td><td>String</td></tr><tr><td>response_text -> document_group</td><td>Knowledge pack identifier where document is uploaded</td><td>String</td></tr><tr><td>response_text -> document_type</td><td>Type of the document uploaded</td><td>String</td></tr><tr><td>response_text -> file_type</td><td>Type of file uploaded </td><td>String</td></tr><tr><td>response_text -> id</td><td>Document identifier</td><td>String</td></tr><tr><td>response_text -> language</td><td>Document language</td><td>String</td></tr><tr><td>response_text -> name</td><td>Document name</td><td>String</td></tr><tr><td>response_text -> parsing_template</td><td>Parsing template used to upload document</td><td>String</td></tr><tr><td>response_text -> source_file</td><td>Source file of the uploaded document, if any.</td><td>String</td></tr><tr><td>response_text -> source_url</td><td>Source URL of the uploaded document, if any.</td><td>String</td></tr><tr><td>response_text -> status</td><td>UPLOADED/ERROR</td><td>String</td></tr><tr><td>response_text -> updated_at</td><td>Updated Datetime of document</td><td>String</td></tr><tr><td>response_text -> updated_by</td><td>User who updated the document</td><td>String</td></tr><tr><td>response_text -> uuid</td><td>Unique identifier of the uploaded document</td><td>String</td></tr><tr><td>status</td><td>true if the document was uploaded successfully</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases for uploading a document to the Answers skill:

<table><thead><tr><th width="236.9472199894152">Use case</th><th width="498.34526508220097">Request payload</th></tr></thead><tbody><tr><td>Uploading a document using URL</td><td><p>{ </p><p>    "document_group_id": 1, </p><p>     "api_server": "https://mx.avaamo.com", </p><p>      "document": { </p><p>         "name": "Avaamo Docs", </p><p>          "type": "url", </p><p>          "preview_url": "https://docs.avaamo.com/user-guide/" </p><p>     } </p><p>}</p></td></tr><tr><td>Uploading a document directly with HTML content</td><td><p>{ </p><p>   "document_group_id": 1, </p><p>   "api_server": "https://mx.avaamo.com", </p><p>   "document": { </p><p>        "content": "<code>&#x3C;title>Name of document&#x3C;/title>&#x3C;body>&#x3C;p>valid html content&#x3C;/p>&#x3C;/body></code>", </p><p>        "name": "Terms of Use", </p><p>        "type": "html",</p><p>        "preview_url": "https://avaamo.ai/privacy/" </p><p>    } </p><p>}</p></td></tr></tbody></table>

## Delete the document from the specified document group in the Answers skill.

<mark style="color:red;">`DELETE`</mark> `https://answers-ingest.aiavaamo.com/api/document`

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| content-type<mark style="color:red;">\*</mark> | -      | application/json                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| access-token<mark style="color:red;">\*</mark> | String | <p>The user access token. <br></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../../manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../../manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information </p><p></p><p>User must have at least edit permission on the agent. See <a href="../../../../build-agents/configure-agents/permissions">Permissions</a>, for more information on agent permissions.</p> |

#### Request Body

| Name                                                  | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| document\_group\_id<mark style="color:red;">\*</mark> | String | <p>Unique identifier for the document group.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. See <a href="../manage-avaamo-answers-1/create-document-groups">Create document groups</a>, for more information.</p>                                                                                                                                                                                                                                                             |
| preview\_url                                          | String | <p>URL used to upload the document to the Answers skill. Use this if you have uploaded a document using a URL and wish to delete the document from the Answers skill. </p><p></p><p>You can get the preview URL from the Document group -> Document -> Edit pop-up window.  </p><p></p><p>You must specify either preview\_url or document\_id in the delete payload request. </p><p>See <a href="../manage-avaamo-answers-1/create-document-groups">Create document groups</a>, for more information.</p>                       |
| api\_server<mark style="color:red;">\*</mark>         | String | <p>Avaamo Answers instance. </p><p></p><p>Contact Avaamo Support to get the API server URL.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| document\_id                                          | String | <p>Unique identifier of the uploaded document to the Answers skill. Use this if you have uploaded a document directly to the Answers skill and wish to delete the document from the Answers skill. </p><p></p><p>You can get the document\_id from the Document group -> Document -> Edit pop-up window.  See <a href="../manage-avaamo-answers-1/create-document-groups">Create document groups</a>, for more information.</p><p></p><p>You must specify either preview\_url or document\_id in the delete payload request.</p> |

{% tabs %}
{% tab title="200: OK Successful request" %}

```javascript
{
     "status": true
}

// status as true indicates that the document is deleted successfully
```

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request DELETE 'https://answers-ingest.aiavaamo.com/api/document' \
--header 'Content-Type: application/json' \
--header 'access-token: xxxxxxf69ba5497e96ff614b00xxxxxx' \
--data-raw '{
 "document_group_id": 999,
 "api_server": "https://mx.avaamo.com",
 "preview_url": "https://avaamo.ai/privacy-policy/"
}'
```

{% endtab %}

{% tab title="node.JS" %}

```javascript
var request = require('request');
var options = {
  'method': 'DELETE',
  'url': 'https://answers-ingest.aiavaamo.com/api/document',
  'headers': {
    'Content-Type': 'application/json',
    'access-token': 'xxxxxxf69ba5497e96ff614b00xxxxxx'
  },
  body: JSON.stringify({
    "document_group_id": 999,
    "api_server": "https://mx.avaamo.com",
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

### Examples

The following table lists a few sample use cases for deleting a document from the Answers skill:

| Use case                                             | Request payload                                                                                                                                      |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Delete a document that is uploaded using a URL       | <p>{ </p><p>"document\_group\_id": 999, </p><p>"api\_server": "<https://mx.avaamo.com>", "preview\_url": "<https://avaamo.ai/privacy/>" </p><p>}</p> |
| Delete a document uploaded that is uploaded directly | <p>{ </p><p>"document\_group\_id": 999, </p><p>"api\_server": "<https://mx.avaamo.com>",           "document\_id": 556 </p><p>}</p>                  |

## Update the document name and attributes

<mark style="color:orange;">`PUT`</mark> `https://answers-ingest.aiavaamo.com/api/document`

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | String | <p>Unique access token of the user. <br></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../../manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../../manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../../../build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |
| content-type<mark style="color:red;">\*</mark> | json   | application/json                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

#### Request Body

| Name                                                       | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| document\_group\_id<mark style="color:red;">\*</mark>      | Number      | <p>Unique identifier for the document group.</p><p></p><p>You can get the document group identifier from the Document group -> View/Edit page. </p><p></p><p>See <a href="../manage-avaamo-answers-1/create-document-groups">Create document groups</a>, for more information.</p>                                                                                                                                 |
| api\_server<mark style="color:red;">\*</mark>              | String      | <p>Avaamo instance where the data is to be uploaded. </p><p>Example: <https://mx.avaamo.com></p>                                                                                                                                                                                                                                                                                                                   |
| document<mark style="color:red;">\*</mark>                 | JSON Object | Document object that needs to be uploaded                                                                                                                                                                                                                                                                                                                                                                          |
| document -> name                                           | String      | <p>Name of the document.</p><p>Max length: 255 characters. </p>                                                                                                                                                                                                                                                                                                                                                    |
| document -> attributes                                     | Key-value   | <p>Define attributes for the uploaded documents or URLs in your Answers skill to facilitate disambiguation or filtering. </p><p></p><p>Attributes can be metadata of the document. You define attributes in key-value pairs. See <a href="../../manage-avaamo-answers-1/perform-common-actions#defining-attributes-for-documents-or-urls">Defining attributes for documents or URLs</a>, for more information.</p> |
| document -> preview\_url<mark style="color:red;">\*</mark> | String      | URL that needs to be opened when user clicks in the response. See [Create document groups](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/create-document-groups), for more information.                                                                                                                                                       |

{% tabs %}
{% tab title="200: OK Successful request" %}

```json
{
    "response_text": {
        "https://docs.avaamo.com/user-guide/": {
            "status": true
        }
    },
    "status": true
}
// status as "true" indicates that the update was successful
```

{% endtab %}
{% endtabs %}

### Code request snippets <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request PUT 'https://answers-ingest.aiavaamo.com/api/document' \
--header 'access-token: xxxxxxf69ba5497e96ff614b00xxxxxx' \
--header 'Content-Type: application/json' \
--data-raw '{ 
 "document_group_id": 999,
 "api_server": "https://mx.avaamo.com",
 "document": {
   "name": "Terms of use",
   "type": "url",
   "preview_url": "https://avaamo.ai/privacy-policy/"
 }
}
'
```

{% endtab %}

{% tab title="node.JS" %}

```javascript
var request = require('request');
var options = {
  'method': 'PUT',
  'url': 'https://answers-ingest.aiavaamo.com/api/document',
  'headers': {
    'access-token': 'xxxxxxf69ba5497e96ff614b00xxxxxx',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "document_group_id": 999,
    "api_server": "https://mx.avaamo.com",
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
    "response_text": {
        "https://docs.avaamo.com/user-guide/": {
            "status": true
        }
    },
    "status": true
}
```

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th width="133.63414634146343">Attribute</th><th width="492">Description</th><th>Type</th></tr></thead><tbody><tr><td>status</td><td><code>true</code> if the document is updated successfully else <code>false</code>.</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases for updating documents to the Answers skill:

<table><thead><tr><th width="247.99507811332592">Use case</th><th>Request payload</th></tr></thead><tbody><tr><td>Update the name of the document</td><td><p>{ </p><p>"document_group_id": 1, </p><p>"api_server": "https://mx.avaamo.com", "document": { </p><p>"name": "Avaamo User Manual", </p><p>"type": "url", </p><p>"preview_url": "https://docs.avaamo.com/user-guide/" </p><p>} </p><p>}</p></td></tr></tbody></table>
