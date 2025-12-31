# Source: https://docs.deepconverse.com/product-docs/conversational-flow-builder/conversation-blocks/salesforce-blocks/live-agent-handover.md

# Live Agent Handover

The **Live Agent Handover** block allows you to handoff customers to a Salesforce Live Agent. In addition to the handover you can associate cases and contacts. You also have the ability to prefill fields on the [LiveChatTranscript](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_livechattranscript.htm) object.

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2FTIZE2eN7iyNJz77GMLVA%2Fimage.png?alt=media&#x26;token=bb596a81-40f4-408b-a908-7b381f6b3de0" alt=""><figcaption><p>Salesforce - Live Agent Handover Node</p></figcaption></figure>

By default the following are the required fields which can either be populated directly or with parameters.

1. Live Agent Url
2. Salesforce Organization Id
3. Deployment Id
4. Button Id

<figure><img src="https://534431549-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FbO3m8ycFG8xg77R5w9dH%2Fuploads%2F0VeyrjIlia8j8zqI1TsY%2Fimage.png?alt=media&#x26;token=935ebab5-1511-4958-9911-8a72bb8d187c" alt=""><figcaption></figcaption></figure>

Optional fields include the following:

| Field         | Description                                                                                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Case Id       | The Salesforce Case object to associate with the transcript. This should be created prior to handoff if the association is needed                                   |
| Contact Id    | The Salesforce Contact object to associate with the transcript. This should be created prior to handoff if the association is needed                                |
| Custom Fields | These are key value pairs to be set on the LiveChatTranscript object. These can be either the default Salesforce fields or any custom fields added into the object. |

On the completion of the chat the flow would move forward to the next node. Completion can happen with the following scenarios:

1. Chat ended by agent
2. Chat ended by user
3. Disconnect from user (Abandonment leading to ending of chat after a timeout)
