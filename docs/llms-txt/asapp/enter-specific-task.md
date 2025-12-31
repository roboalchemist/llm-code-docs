# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/enter-specific-task.md

# Enter a Specific Task

> Learn how to enter a specific task for GenerativeAgent

When GenerativeAgent analyzes a conversation, by default, it will automatically select the appropriate task and follow its instruction.

If your system already knows which task to use, you can specify it by using the `taskName` attribute in the [`/analyze` request](/apis/generativeagent/analyze-conversation).

```bash  theme={null}
curl --request POST \
  --url https://api.sandbox.asapp.com/generativeagent/v1/analyze \
  --header 'Content-Type: application/json' \
  --header 'asapp-api-id: <api-key>' \
  --header 'asapp-api-secret: <api-key>' \
  --data '{
  "conversationId": "01BX5ZZKBKACTAV9WEVGEMMVS0",
  "message": {
    "text": "Hello, I would like to upgrade my internet plan to GOLD.",
    "sender": {
      "role": "agent",
      "externalId": 123
    },
    "timestamp": "2021-11-23T12:13:14.555Z"
  },
  "taskName": "UpgradePlan",
}'
```
