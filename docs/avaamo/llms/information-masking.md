# Source: https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking.md

# Information masking

Typically, in certain domains such as Banking, Healthcare, and Finance, a user’s interaction with the agent can capture sensitive details such as the user’s identification number, policy number, email (to name a few). Therefore, it is critical to audit the data and protect data privacy.&#x20;

This article explains the process of masking PII/PHI/GDPR compliance data within the Avaamo Conversational AI system. Information masking in the Avaamo Platform can be configured at two levels:

* [Masking user properties](#masking-user-properties): This masks all the user information details such as email, first name, last name, SSN in all the agent's conversations. User properties, often used to store and reuse user-specific information like Social Security Numbers (SSNs), phone numbers, and email addresses, are also subject to masking. When such data is set using `User.setProperty()`, it is immediately masked if marked as sensitive. Once masked, these values are no longer accessible within the agent’s context, nor are they visible in logs or analytics, helping maintain strict privacy standards and regulatory compliance.
* [Masking agent responses](#masking-agent-responses): This masks all the agent's responses for a node in the conversation flow. Additionally, you can also enable masking of all the user-uploaded files. After masking, the uploaded files cannot be accessed in the Avaamo Platform, as they are physically deleted from the Platform.
  * **User Query Masking**\
    The Avaamo Platform automatically masks sensitive information in the user's messages before processing. This includes details identified through system-recognized entities such as names (`person`), dates (`date`), and predefined user properties like `first_name`. By applying user query masking, the platform ensures that personal or identifiable information is masked, preventing it from being stored or displayed in its original form.
  * **Agent Response Masking**\
    Agent responses can also contain sensitive information, especially when they echo or use dynamic content related to user input. The platform masks agent responses using the same entity recognition logic—covering entities like `person` or `date`—and also masks any user properties referenced in the response. This includes not only text responses but also data presented in files and forms shared by the agent, ensuring comprehensive coverage of potential data exposure points.

## Key points

{% hint style="danger" %}
**Note:** Masking purges the data, making it unrecoverable. The removed PII/ePHI data cannot be restored.
{% endhint %}

1. Contact Avaamo Support to configure masking for your agent. See [Before you begin](#before-you-begin), for more information.
2. When you enable masking for an agent, the information is masked as per the masking configuration details across all the pages such as agent insights, conversation history, and query insights where the information can be viewed. See [Masking toggle](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#enable-information-masking) in the Configuration -> Settings page, for more information on how to enable or disable masking for an agent.
3. If you have deployed your agent in C-IVR or Phone channel and masking is enabled, then the audio files from the user responses are not available in the conversation history, since it can contain PII data.&#x20;
4. If you wish not to record the live agent interactions between users and live agents, then you can disable it using the `Save conversations` toggle button on the `Configuration -> Live agent` page. This feature is particularly useful for organizations handling sensitive data, offering them flexibility to align with internal data governance policies and regulatory requirements. See [Configure live agent](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/switch-to-live-agent/pre-built-live-agent#configure-live-agent), for more information.
5. Masking is always performed only on the information that resides on the Avaamo platform. All data sent to integrations—such as live agent interactions, custom channel interactions, or Microsoft Teams channel interactions—remains within the respective integration platforms and is subject to the data handling policies and rules of those third-party platforms. Avaamo does not have control over or the ability to mask this data.
6. [Storage variables](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/storage) are not masked. As a best practice, it is recommended to clear out all sensitive storage variable information after using it during agent development itself.
7. Currently, information masking is not supported for [Universal agents](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/universal-agent). This implies that if you have a Universal agent with masking enabled for member agents, then even though the responses are masked in the member agents, the same responses remain unmasked in the Universal agent.
8. If you update the masking configuration details, then masking the newly set-up fields is done for the new messages. If you wish to mask the newly set up fields in the previous messages of the conversation, then contact Avaamo Support for further assistance.

## Default masking behavior for new agents

All newly created agents will have data masking enabled by default to better protect Personally Identifiable Information (PII) and ensure compliance with data privacy regulations, right out of the box.

**What’s masked by default**:

{% hint style="success" %}
**Key points:**&#x20;

1. Real-time masking is enabled by default, so any personal information in both your messages and the agent’s replies is automatically masked to keep your data safe.
2. Masking support for `non-English` conversations is currently under continuous evaluation.
   {% endhint %}

By default, the following personal information is automatically masked in real-time:

* Date (example: date of birth)
* email
* person
* phone
* SSN
* first\_name&#x20;
* last\_name
* ip\_address
* Any user-uploaded files

## Before you begin

The following illustration depicts the data masking process flow:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FeAAWON1DXrQt7Q1xdKhv%2FAdd%20a%20subheading%20\(7\).png?alt=media\&token=c1a7e430-5ad2-4dd3-a490-f9c04a68f478)

You must provide the following information to Avaamo Support to configure masking:

1. Provide the agent details such as the agent name and the agent identifier.
2. Provide a list of fields in the agent that must be masked in messages.
3. Provide a list of user attributes such as first name, last name, and other custom user properties, that must be masked.&#x20;
4. By default, when masking is enabled, all the PII data in agent and user messages are masked in the conversation. This masks all the sensitive user information as per your requirement, and such data is not stored in the Avaamo Platform.&#x20;

## Masking user properties

You can configure to mask user information details such as email, first name, last name, and SSN in all the agents' conversations. When you enable masking for an agent, the information is masked as per the masking configuration details across all the pages, such as agent insights, conversation history, and query insights, where the information can be viewed.

### Fields to Mask

By default, masking is enabled for certain fields. If you need to mask additional fields, use the table to specify the fields that should be masked in the Avaamo user interface to ensure compliance and maintain confidentiality.

| Section                        | Field                              | Value / Notes                                           |
| ------------------------------ | ---------------------------------- | ------------------------------------------------------- |
| Agent and Instance Details     | Agent ID                           |                                                         |
|                                | Instance                           |                                                         |
|                                |                                    |                                                         |
| Entities Containing PII        | Default masked system entities     | date, email, person, phone, ssn                         |
|                                | Additional entities (if any)       |                                                         |
|                                |                                    |                                                         |
| User Attributes Containing PII | Default masked user attributes     | first\_name, last\_name, email, phone, ssn, ip\_address |
|                                | Additional attributes / exceptions |                                                         |
|                                |                                    |                                                         |
| Custom Use Cases               | Use case description               |                                                         |
|                                | Masking requirement                |                                                         |
|                                |                                    |                                                         |
| Masking Trigger (default)      | Real-Time Masking                  | Enabled                                                 |
|                                | File Masking                       | Enabled                                                 |
|                                | Response Node Masking              | Enabled                                                 |
|                                |                                    |                                                         |
| Data Retention Period          | Retention Duration                 |                                                         |

### Test masking

After the configuration is completed, you can test the user message masking from your agent. Consider that you wish to mask the following:

* **User email**: My email is <john@gmail.com>. In the agent, click the eye icon to check query insights.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FuX9RpcKfTYPgQ719gBtv%2Fimage.png?alt=media\&token=abbf144e-825c-4354-9462-a37c9c0c49e3)

Similarly, you can verify the masked details in the conversation history and query insights:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M4wxwCWmklD7rqvZx8e%2F-M4x3PvQsN7ZGb23vb-e%2Fuser-message-test-2.png?alt=media\&token=ce74cf20-3199-4c86-b29f-059b19b4dd5f)

* **User's first name and last name when sent in custom channel**: Consider that in the custom channel, the user's first name is sent in the user properties:

```javascript
{
  "channel_uuid": "f33b3814-1535-4e21-807f-a1d2b77585af",
  "locale": "en-US",
  "user": {
    "first_name": "Williamson",
    "last_name": "Smith",
    "uuid": "9ac15843-151d-47fb-8b3d-930b89ce797e"
  },
  "message": {
    "text": "hello"
  }
}
```

In the **Conversation history** page, you can see that the `first_name` and `last_name`in the user conversation is masked,&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLGDkDVabXFEhIJqqo1Oe%2Fassets_-LpXFTiTgns4Ml77XGi3_-M4wxwCWmklD7rqvZx8e_-M4x3hf8Y45CJTEY2hc9_user-message-test-3%20copy.png?alt=media\&token=f3e5e15e-78d1-43fc-ba77-35ebfb56a3d9)

## Masking agent responses

The Avaamo platform offers **masking agent responses** to protect sensitive information such as PII (Personally Identifiable Information) during agent interactions. This functionality ensures that only sensitive data is masked, while the rest of the response remains visible for clarity and debugging.

The system identifies and masks only the portions of the agent response that contain sensitive data. The non-sensitive content is left unmasked, allowing teams to review and understand the flow of the conversation without exposing private information.

{% hint style="info" %}
**Notes**:&#x20;

* This behavior is `enabled by default` for all agents created after the feature rollout. For agents created prior, bot developers can manually enable masking from the [Agent Settings page](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#enable-information-masking), or contact Avaamo Support for assistance.
* If the agent response contains sensitive PII data such as name, account number, or password, then it is recommended to mask the agent responses to protect user privacy.&#x20;
  {% endhint %}

In the **Conversation history** page, you can view that the agent responses are masked. Note that even the original file is masked as **masked.png**. When you click **masked.png**, the original file is no longer available in the Avaamo Platform and cannot be accessed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M52BF21kStG_9196_gg%2F-M52D0fnXuUhx7RhZ8MP%2Fmask-agent-response.png?alt=media\&token=525f4799-ec72-452f-b899-2645bde0abf6)

Similarly, you can also verify the masked details from the **Query insights** page.

## Frequently Asked Questions (FAQs)

### 1. Can masking be reverted?

Once masked, the original unmasked data is not available anywhere in the Avaamo Platform. Hence, masking cannot be reverted.

### 2. How is the PII (Personally identifiable information) data masked if my agent is deployed in the C-IVR channel?

If you have deployed your agent in the C-IVR or Phone channel and masking is enabled, then the audio files from the user responses are not available in the conversation history, since they can contain PII data.&#x20;

### **3. What happens to previous data when masking is enabled after a debugging period is over?**

If masking is enabled after a debugging period, all previously generated data that was unmasked due to masking being disabled will be masked. The platform applies masking to this data, ensuring it aligns with the current configuration.

### 4. If I disable masking, then will all the previous data get unmasked?

Once masked, the data cannot be retrieved back. At a later point in time, if you choose to disable masking, then all the previous data will still remain masked and will not get unmasked. However,  going forward, the conversations after you disable masking will remain unmasked.

### 5. How to audit if all the data has been masked or not?

Avaamo Platform maintains a log of each record that is masked. Contact Avaamo Support for more details before you plan to audit.

### 6. I cannot see the Debug logs option. Why is that?

You can enable or disable the **Debug Logs** option from the **Settings** section in the agent's configuration. Refer [Enable Debug Log](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings), for more information.

### 7. Some of the user names are not getting masked in the user messages. What do I do now?

Avaamo Platform covers the masking of the most commonly used names. However, if you do find certain names that are not getting masked, you can consider one of the following approaches:

1. Create a custom entity with all such names and share the custom entity with Avaamo Support. Avaamo will then enable masking for the custom entity. Configuring masking is a one-time activity and you can continue to add names in the custom entity and all such names will get masked after masking has been set up.
2. &#x20;Periodically share a list of such names with Avaamo Support and we can continuously improve name entity recognition.
