# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/history.md

# history

Context history is an array of message history with details such as created date and time, actual message, and the sender of the message generated during the execution of the user’s intent in the agent's flow. The following is a sample JSON of history details in context object:

```yaml
"history": [
    {
      "created_at": 1566282974986,
      "last_message": "i want to order cheese pan pizza",
      "last_message_schema_identifier": "output_14",
      "last_message_sent_by": "user"
    }
  ]
```

| **Attribute**                     | **Description**                                                                   | **Type**      |
| --------------------------------- | --------------------------------------------------------------------------------- | ------------- |
| created\_at                       | Indicates timestamp of the message sent by the user to the agent in milliseconds. | UTC Timestamp |
| last\_message                     | Indicates the last message sent to the agent.                                     | String        |
| last\_message\_schema\_identifier | Indicates the node identifier of the last message.                                | String        |
| last\_message\_sent\_by           | Indicates the user who sent the last message to the agent.                        | String        |

{% hint style="info" %}
**Note**: You can view upto the last 20 messages in the context.history object.
{% endhint %}
