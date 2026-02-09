# Source: https://docs.lunary.ai/docs/features/feedback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Feedback Tracking

Use feedback tracking for:

* user's reactions to your chatbot's responses directly on the frontend.
* score LLM outputs directly yourself

You can then use this to filter llm calls and fine-tune your own models based on the data.

Feedback tracking can be done in the backend or directly on the frontend if it's easier for you.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const msgId = thread.trackMessage({
      role: 'assistant',
      content: 'Hello! How can I help you?',
    })

    lunary.trackFeedback(msgId, { thumb: 'up' })
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    msg_id = thread.track_message({
      "role": "assistant",
      "content": "Hello! How can I help you?"
    })

    lunary.track_feedback(msg_id, { "thumb": "up" })
    ```
  </Tab>
</Tabs>

## Example of a React Feedback component

You can also use the feedback method to track user reactions to your chatbot's responses directly on the frontend.

```jsx  theme={null}
<Button onClick={() => lunary.trackFeedback(message.id, { thumb: "up" })}>
  👍
</Button>
```

The `trackFeedback` method takes two arguments:

* `runId`: the ID of the message or run you want to track the feedback on.
* `feedback`: an object containing the feedback data. You can use any key/value pair you want.

## Feedback data

You can send any feedback data you want, as long as it's a valid JSON object.

We recommend using the following keys to ensure that data is displayed correctly in the dashboard.

| Key       | Value            | Preview                    |
| --------- | ---------------- | -------------------------- |
| `thumb`   | `up` or `down`   | 👍 / 👎                    |
| `comment` | arbitrary string | eg. "This is not correct." |

## Removing feedback

To remove feedback, simply pass `null` as the feedback data.

```js  theme={null}
lunary.trackFeedback(message.id, { thumb: null })
```
