# Source: https://docs.avaamo.com/user-guide/release-notes/v7.0.0/release-notes-v7.0.0.md

# Release notes v7.0.0

The Avaamo Conversational AI Platform v7.0.0 release includes 2 new products, 4 enhancements, 1 change, and 2 deprecation notices distributed as follows:

**New products:** This release includes the introduction of the 2 products:

1. [Introducing Live agent console](https://docs.avaamo.com/user-guide/release-notes/v7.0.0/introducing-live-agent-console)
2. [Introducing Outreach](https://docs.avaamo.com/user-guide/release-notes/v7.0.0/introducing-outreach)

**Enhancements**: This release includes enhancements related to the following existing features:

<table><thead><tr><th width="145">Module</th><th>Enhancements</th></tr></thead><tbody><tr><td>MS Teams Channel</td><td><ul><li><a href="#broadcast-messages-via-ms-teams-using-a-new-ms-teams-send-api">Broadcast messages via MS Teams using a new MS Teams Send API</a></li></ul></td></tr><tr><td>Answers </td><td><ul><li><a href="#support-for-uploading-microsoft-word-and-powerpoint-documents">Support for uploading Microsoft Word and Powerpoint documents</a></li><li><a href="#improved-ingestion-of-documents-with-custom-parsing-templates">Improved ingestion of documents with custom parsing templates</a></li><li><a href="#improved-accuracy-for-small-to-medium-sized-answers-skill">Improved accuracy for small to medium-sized Answers skill</a></li></ul></td></tr></tbody></table>

**Changes:** This release includes changes related to the endpoints of Content Ingestion APIs. See [Content Ingestion APIs](#content-ingestion-apis), for more information.

{% hint style="danger" %}
**Deprecation notices**: In this release, note the following deprecation notices:&#x20;

* `Conversation ID` column in the Live agent chat transcript export.&#x20;
* `from_date`, `to_date`, and `utc_offset` query parameters in the following Analytics APIs:
  * Successful messages
  * User sessions
  * Messages
  * Unhandled messages
* `See`[Deprecation notices](#deprecation-notices), for more information.
  {% endhint %}

## Enhancements

### Broadcast messages via MS Teams using a new MS Teams Send API

In this release, as a part of MS Teams channel enhancement, a new REST API - **MS Teams channel Send API** has been introduced.

This API allows you to post or broadcast messages via the MS Teams channel without user intervention or activity. Since this is a REST API, it comes with the various advantages of REST API and can be easily integrated with any enterprise application where REST API integration is applicable.&#x20;

{% code overflow="wrap" %}

```json
// API Signature

https://cx.avaamo.com/teams/<<channel_uuid>>/send.json

// Sample cURL request

curl -X POST \
https://cx.avaamo.com/teams/79459364-d221-xxxx-9eab-6636xxxxxxx/send.json \
-H 'content-type: application/json' \
-d '{ 
   "first_name": "John",
   "last_name": "Jacob",
   "emp_id": "1234",
   "email": "jacob.john@abc.com",
   "message": {
      "text": "Your message goes here."
   }
 }'

```

{% endcode %}

Using this API, you can post a message via the MS Teams channel to the specified email. After a successful request, a conversation is established and can be tracked using `email`  from the Conversation history page. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/conversation-history), for more information.

In the earlier release, if you had to broadcast a message via the MS Teams channel, the only way was to configure a campaign via the MS Teams channel and then post the message via a campaign. With the new `MS Teams Send API`, "Broadcasting messages to users" is de-coupled from campaigns and made interoperable across different systems. See [Microsoft Teams Send API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/microsoft-teams-send-api), for more information.

As a part of the new `MS Teams Send API,` the ability to authenticate users before sending messages via `MS Teams Send API` has been provided with the **Custom user authentication** option in the MS Teams channel page.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHAf1cZ5fWyjEgJgm9qZA%2Fimage.png?alt=media&#x26;token=c081b828-7565-478b-b3a8-2cac9e522700" alt=""><figcaption></figcaption></figure>

Note that this option works only with the `MS Teams Send API` and you can use this option along with the new [MS Teams Send API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/microsoft-teams-send-api) to authenticate users in the [User authentication handler](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#ms-teams-channel) before sending MS Teams message. This helps secure communication between the user and the agent via the MS Teams channel.&#x20;

See [MS Teams channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams), for more information. Also see [Custom user authentication](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#ms-teams-channel), for an example.

### Support for uploading Microsoft Word and PowerPoint documents

In this release, the Answers skill has been enhanced with the ability to upload Microsoft Word (.docx) and Microsoft Powerpoint (.pptx) documents both via UI and via Content ingestion APIs.

The following illustration shows a Microsoft Word document successfully uploaded to the Answers knowledge base via UI:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FbkXTkt6UnTmJgPmQ8Xqn%2Fimage.png?alt=media&#x26;token=ad84430a-3804-4452-ae56-c09bc644a331" alt=""><figcaption></figcaption></figure>

See [Upload documents](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/add-document-or-url-1), for more information.

To upload files such as Microsoft Word, Microsoft Powerpoint, or Microsoft Excel the content ingestion API has been enhanced with a new Upload file API:

```bash
// API endpoint

https://mx.avaamo.com/content-ingestion/upload-file

// Sample cURL request

curl --location --request PUT 'https://mx.avaamo.com/content-ingestion/upload-file' \
--header 'access-token: xxxxxxxxx61f48829a47ccdxxxxxxxxx' \
--form 'file=@"/Users/avaamo/Desktop/MACPIZZA_Policy.docx"' \
--form 'document_group_id="34xx"' \
--form 'type="pdf"' \
--form 'parsing_template_id="87"'sh
```

See [Content ingestion APIs](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/answers-rest-apis/content-ingestion-apis-recommended), for more information.

To support the ingestion of the documents, two new parsing templates for Microsoft Word and Microsoft PowerPoint are included in the in-built parsing template list. When you are uploading .docx or .pptx documents via Content ingestion APIs, you can use the corresponding parsing template identifier to facilitate seamless ingestion of the documents to the Answers knowledge base:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FX1bq8DBOSxqiLQVCzhb8%2Fimage.png?alt=media&#x26;token=0239a87f-eada-4db3-b0c4-a0568c26d311" alt=""><figcaption></figcaption></figure>

See [Parsing templates](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/parsing-templates), for more information.

### Improved ingestion of documents with custom parsing templates

In this release, the ingestion of documents that require custom parsing templates has been improved with the ability to pass the `Custom parsing template identifier` in the Content Ingestion APIs. This eliminates the need for specifying the parsing JSON in the API which is tedious, cannot be reused, and error-prone.

Instead, you can configure custom parsing templates in the Answers skill and then simply use the parsing template identifier in the Content ingestion APIs. This promotes better reusability, is less error-prone, and can be maintained efficiently.

See [Content ingestion APIs (Recommended)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/answers-rest-apis/content-ingestion-apis-recommended), for more information.

### Improved accuracy for small to medium-sized Answers skill

In this release, the NLP boost option in the Answering mechanism has been improved with better accuracy. The NLP boost option is best suited for small to medium-sized Answers skills (upto 4000 chunks).&#x20;

See [Answering mechanism configuration](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/configure-answers-skill#answering-mechanism), for more information.

## Changes

### Content Ingestion APIs

In this release, with the view of streamlining and providing better support, note the following endpoint changes in Content Ingestion APIs:

<table><thead><tr><th width="145.33333333333331">Action</th><th width="259">Old API Endpoint</th><th>New API Endpoint</th></tr></thead><tbody><tr><td>Upload document</td><td><p><code>https://answers-ingest.aiavaamo.com/api/document</code> </p><p><code>ACTION: POST</code></p></td><td><code>https://mx.avaamo.com/content-ingestion/parse-document</code></td></tr><tr><td>Delete document</td><td><p><code>https://answers-ingest.aiavaamo.com/api/document</code> </p><p><code>ACTION: DELETE</code></p></td><td><code>https://mx.avaamo.com/content-ingestion/delete-document</code></td></tr><tr><td>Update document</td><td><p><code>https://answers-ingest.aiavaamo.com/api/document</code> </p><p><code>ACTION: PUT</code></p></td><td><code>https://mx.avaamo.com/content-ingestion/update-document</code></td></tr></tbody></table>

{% hint style="danger" %}
**Note**: Although the older Content ingestion APIs continue to work as-is in v7.0, they will have limited support and will soon be marked as deprecated. Starting from version 7.0.0 onwards, it is recommended to transition to an enhanced and more efficient version of content ingestion APIs to ensure improved support. See [Content ingestion APIs (Recommended)](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/answers-rest-apis/content-ingestion-apis-recommended), for more information.
{% endhint %}

## Deprecation notices&#x20;

### Conversation ID column in Agent Chat transcript export&#x20;

In this release, with the view of streamlining the Agent chat transcript CSV export report, the Conversation ID column is deprecated in the report. The conversation ID column is an internal column only and hence it is not useful for users who are downloading the report.

See [Agent chat transcript](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent#agent-chat-transcript), for more information.

#### When is the support completely stopped?

This feature will be removed from the next release onwards.

#### What action to take?

In case you are using the deprecated CSV column names for any further processing, ensure that the right column name and values are used from the v7.0.0 release onwards.

### from\_date, to\_date, UTC\_offset query parameters in Analytics APIs

In this release, with the view of streamlining and providing consistent query parameters in the Analytics APIs, the `from_date`, `to_date`, and `utc_offset` query parameters are deprecated in the following Analytics APIs and consolidated into two new date query parameters `from_timetoken` and `to_timetoken` to filter data based on date:

* [Successful messages](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/successful-messages)
* [User sessions](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/user-sessions)
* [Messages](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/messages)
* [Unhandled messages](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/unhandled-messages)

`from_timetoken` and `to_timetoken` allows you to filter based on the Unix Epoch timestamp and is used in all other REST APIs provided by the Avaamo Conversation AI Platform. See [Note on Epoch timestamp in REST APIs](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/quick-overview#note-of-epoch-timestamp-in-rest-apis), for more information on the benefits of using Epoch time.

#### When is the support completely stopped?

This feature will be removed from the next release onwards.

#### What action to take?

In case you are using the deprecated query parameters in any further data processing, ensure that the right query parameters are used from the v7.0.0 release onwards.
