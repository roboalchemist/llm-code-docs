Source: https://docs.slack.dev/changelog/2025/10/7/chat-streaming

# New features designed for Slack apps sending AI responses

October 7, 2025

We've introduced a new suite of features to help Slack apps provide an end-user experience typical of LLM tools:

* Slack apps can now stream in their responses to the end user using three new API methods.
* There are new Block Kit components to allow end users to quickly interact with AI responses.
* The Node and Python SDKs have new utilities to streamline integration of these new features.

Read on for more info!

### Streaming messages {#streaming-messages}

Three Web API methods work together to enable Slack apps to provide end users a text streaming experience similar to typical LLM tools:

* The [`chat.startStream`](/reference/methods/chat.startStream) method starts the text stream.
* The [`chat.appendStream`](/reference/methods/chat.appendStream) method appends text to the stream.
* The [`chat.stopStream`](/reference/methods/chat.stopStream) method stops the text stream.

### Interacting with AI responses {#interacting-with-ai-responses}

Three new Block Kit components allow more user interaction with agent responses:

* The [`feedback_buttons`](/reference/block-kit/block-elements/feedback-buttons-element) block element allows users to provide feedback on whether an AI response was positive or negative.

* The [`icon_button`](/reference/block-kit/block-elements/icon-button-element) provides a way for users to quickly trigger actions like deleting AI responses.

* The [`context_actions`](/reference/block-kit/blocks/context-actions-block) block provides a container for these interactive elements.

### Supported by Slack SDKs and Bolt framework {#supported-by-slack-sdks-and-bolt-framework}

The [Python Slack SDK](/tools/python-slack-sdk) and [Node Slack SDK](/tools/node-slack-sdk) each fully support these new features — with a new `streamer` helper utility to aid developers in tying them all together.

Here's a simplified example in Python:

```javascript
streamer = client.chat_stream(    channel=channel_id,    recipient_team_id=team_id,    recipient_user_id=user_id,    thread_ts=thread_ts,)for event in returned_message:    streamer.append(markdown_text=f"{chunk-received-from-llm}")streamer.stop(blocks=feedback_block)
```text

This utility can also be used in the Bolt frameworks based upon these SDKs. Read more in the _Using AI in apps_ section of your preferred Bolt flavor: [Python](/tools/bolt-python/concepts/ai-apps#text-streaming) or [JavaScript](/tools/bolt-js/concepts/ai-apps#text-streaming).

We've also updated our app agent template repos to use these new features. Pick your flavor of Bolt and give it a try.

Get started with the [Bolt for Python agent template](https://github.com/slack-samples/bolt-python-assistant-template):

```text
slack create --template slack-samples/bolt-python-assistant-templateslack run
```text

Get started with the [Bolt for JavaScript agent template](https://github.com/slack-samples/bolt-js-assistant-template):

```text
slack create --template slack-samples/bolt-js-assistant-templateslack run
```text

Read all the details in the [Bolt Python release notes](https://github.com/slackapi/bolt-python/releases/tag/v1.26.0) and [Bolt JS release notes](https://github.com/slackapi/bolt-js/releases/tag/%40slack%2Fbolt%404.5.0).

## Tags:

* [Announcement](/changelog/tags/announcement)
* [New Feature](/changelog/tags/new-feature)
