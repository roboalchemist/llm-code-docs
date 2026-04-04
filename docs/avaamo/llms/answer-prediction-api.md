# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/answers-rest-apis/answer-prediction-api.md

# Answer prediction API

## Post a query and get the response from Answers skill

<mark style="color:green;">`POST`</mark> `https://mx.avaamo.com/answers/v2/process-query`

Contact Avaamo Support to know the server name corresponding to your instance.

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | String | <p>User access token. You can get the user access token from the Settings -> Users page. Users must have at least view permission on the agent. </p><p></p><p>See <a href="../../../../../manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../../manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information on how to get the user access token.</p><p></p><p>See <a href="../../../../build-agents/configure-agents/permissions">Permissions</a>, for more information on agent permissions.</p> |

#### Request Body

| Name                                                                     | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| kp\_id<mark style="color:red;">\*</mark>                                 | Array  | <p>The Answers skill Id you want to predict the answer on. You can pass only one skill Id in the query parameter.</p><p></p><p>You can get the skill Id from the View/Edit Document Group pop-up window. See <a href="../../manage-avaamo-answers-1/create-document-groups#view-edit-a-document-group">Document groups</a>, for more information.</p><p></p><p><code>Example: kp\_id = \[123]</code> </p>                                                                                                                                                                                                                                                                                                  |
| query<mark style="color:red;">\*</mark>                                  | String | <p>The query you want to predict the answer of. </p><p></p><p>If you are using this API in a JS node, then you can use <a href="../../customize-your-skill/how-to/use-context/get-last-message">context.last\_message</a> to get the user query.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| query\_id<mark style="color:red;">\*</mark>                              | String | <p>Unique identifier for the query. </p><p></p><p>If you are using this API in a JS node, then you can use <code>context.message\_uuid</code> to get the query identifier.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| query\_insights -> detected\_language <mark style="color:red;">\*</mark> | String | Locale of the user query.  See [Web - Supported languages](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-supported-languages), for more detailed on supported languages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| conversation\_id<mark style="color:red;">\*</mark>                       | String | <p>Unique identifier of the conversation.  </p><p></p><p>You can get the conversation identifier from:</p><p>1. <a href="../../../../../build-agents/debug-agents#using-conversation-history">Conversation history URL </a></p><p>2. <a href="../../../../../../ref/avaamo-platform-api-documentation/message-api#get-agent-messages">Get Messages API  </a></p><p>3. Message object when you are using the <code>Avaamo.onBotMessage</code> <a href="../../../../build-agents/configure-agents/deploy/web-channel/web-channel-callback-functions">callback function in the Web channel</a>.</p><p>4. If you are using this API in a JS node, then you can use <code>context.conversation\_uuid</code></p> |
| request\_uuid<mark style="color:red;">\*</mark>                          | Strinf | Unique identifier of the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

{% tabs %}
{% tab title="200: OK Success" %}

```javascript
{
  "carousel": {
    "cards": [
      {
        "card": {
          "answering_score": 0.37092517817015064,
          "attributes": {},
          "chunk_id": 87223,
          "description": "<div class=\"dockp\"><h1>Privacy Policy</h1><p> </p></div>",
          "doc_id": 9821,
          "hybrid_score": 1.0996794251079722,
          "intent_key": "EeXUNgRR",
          "is_acronym": false,
          "language": "en-US",
          "links": [
            {
              "title": "View More",
              "type": "web_page",
              "url": "https://www.google.com/?web_channel/documents"
            }
          ],
          "page_number": 1,
          "section_headers": [
            {
              "chunk": 87223,
              "header": "Terms of use - Chatbot Platform- Chatbots for Customer Service",
              "id": 163518,
              "rank": 10,
              "text": "Terms of use - Chatbot Platform- Chatbots for Customer Service",
              "translated_text": null
            },
            {
              "chunk": 87223,
              "header": "Privacy Policy",
              "id": 163519,
              "rank": 6,
              "text": "Privacy Policy",
              "translated_text": null
            }
          ],
          "text": false,
          "title": "Privacy policy"
        }
      }
    ],
    "description": "",
    "title": "Response from DocKP Engine"
  },
  "no_answer": false
}
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request POST 'https://mx.avaamo.com/answers/v2/process-query' \
--header 'access-token: bbxxxxxxxxba5497e96ff614xxxxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
    "kp_id": [94],
    "query": "Want to know Avaamo Privacy Policy",
    "query_id": "6",
    "query_insights": {
        "detected_language": "en-US"
    },
    "conversation_id": "d8703795e78bc80e7e646xxxxxxxx",
    "request_uuid": "12345999"
}
'
```

{% endtab %}

{% tab title="node JS" %}

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://mx.avaamo.com/answers/v2/process-query',
  'headers': {
    'access-token': 'bbxxxxxxxxba5497e96ff614xxxxxx',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "kp_id": [
      94
    ],
    "query": "Want to know Avaamo Privacy Policy",
    "query_id": "6",
    "query_insights": {
      "detected_language": "en-US"
    },
    "conversation_id": "d8703795e78bc80e7e646xxxxxxxx",
    "request_uuid": "12345999"
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

The following is a sample API response:

```json
{
  "carousel": {
    "cards": [
      {
        "card": {
          "answering_score": 0.37092517817015064,
          "attributes": {},
          "chunk_id": 87223,
          "description": "<div class=\"dockp\"><h1>Privacy Policy</h1><p> </p></div>",
          "doc_id": 9821,
          "hybrid_score": 1.0996794251079722,
          "intent_key": "EeXUNgRR",
          "is_acronym": false,
          "language": "en-US",
          "links": [
            {
              "title": "View More",
              "type": "web_page",
              "url": "https://www.google.com/?web_channel/documents"
            }
          ],
          "page_number": 1,
          "section_headers": [
            {
              "chunk": 87223,
              "header": "Terms of use - Chatbot Platform- Chatbots for Customer Service",
              "id": 163518,
              "rank": 10,
              "text": "Terms of use - Chatbot Platform- Chatbots for Customer Service",
              "translated_text": null
            },
            {
              "chunk": 87223,
              "header": "Privacy Policy",
              "id": 163519,
              "rank": 6,
              "text": "Privacy Policy",
              "translated_text": null
            }
          ],
          "text": false,
          "title": "Privacy policy"
        }
      }
    ],
    "description": "",
    "title": "Response from DocKP Engine"
  },
  "no_answer": false
}
```

#### Response Body <a href="#id-1t0r81mh1spp" id="id-1t0r81mh1spp"></a>

<table><thead><tr><th>Attribute</th><th width="348"> Description</th><th>Type</th></tr></thead><tbody><tr><td>Carousel -> Cards</td><td>Array of the response predicted for the given user query.</td><td>Array of JSON Object</td></tr></tbody></table>

#### Card response object&#x20;

<table><thead><tr><th>Attribute</th><th width="344.44871794871796">Description</th><th>Type</th></tr></thead><tbody><tr><td>chunk_id</td><td>Unique chunk identifier</td><td>String</td></tr><tr><td>description</td><td>Description of the response returned</td><td>String</td></tr><tr><td>doc_id</td><td>Unique document identifier</td><td>String</td></tr><tr><td>intent_key</td><td>Unique intent identifier of the matched response.</td><td>String</td></tr><tr><td>language</td><td>Indicates the language of the response</td><td>String</td></tr><tr><td>links</td><td>View more link array of the matched response.</td><td>Array of JSON Object</td></tr><tr><td>section_headers</td><td>Section headers array from the knowledge base of the matched response in the document.</td><td>Array of JSON Object</td></tr></tbody></table>

### Examples

The following is a sample POST request to use Answer prediction API:

```json
{
    "kp_id": [94],
    "query": "Want to know Avaamo Privacy Policy",
    "query_id": "6",
    "query_insights": {
        "detected_language": "en-US"
    },
    "conversation_id": "xxxxxxxxe78bc80e7e6467ccxxxxxxxx",
    "request_uuid": "12345999"
}
```
