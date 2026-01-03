# Source: https://docs.lunary.ai/docs/features/conversations.md

# Chats & Threads

Record and replay chat conversations in your chatbot app. Helps you understand where your chatbot falls short and how to improve it.

Chats integrate seamlessly with traces by reconciliating messages with LLM calls and agents.

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=6764f1443a7417b7d752f6484fdcd18f" alt="Feedback tracking" data-og-width="1922" width="1922" data-og-height="1262" height="1262" data-path="media/docs/features/chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=8e8412742ab184e816f1e3aecf1ce0e9 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=6554a7bea616a99b3ff11ff35f1ee270 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=7bfcbaf14273aa2bfb7235090580e745 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a0fdd8e227b94724bb60f40d5751f3eb 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=36741dbee9f37c12b07109e3d14b131d 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/chat.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=26ab09411248ab88aed1919de9e81ac7 2500w" />

You can record chats in the backend or directly on the frontend if it's easier for you.

## Setup the SDK

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="/docs/integrations/python/installation">
    Learn how to install the Python SDK.
  </Card>

  <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
    Learn how to install the JS SDK.
  </Card>
</CardGroup>

## Open a thread

Start by opening a thread.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const thread = lunary.openThread()
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    thread = lunary.open_thread()
    ```
  </Tab>
</Tabs>

You can resume an existing thread by passing an ID from an existing thread.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    // Save `thread.id` somewhere
    const thread = lunary.openThread({
      id: 'your-thread-id'; // Replace with your actual thread ID
    })
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    # Save `thread.id` somewhere
    existing_thread_id = 'your-thread-id'  # Replace with your actual thread ID
    thread = lunary.open_thread(existing_thread_id)
    ```
  </Tab>
</Tabs>

You can also add tags to a thread by passing a object with a `tags` param:

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const thread = lunary.openThread({
      tags: ['support']
    })
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    thread = lunary.open_thread(existing_thread_id, tags=['support'])
    ```
  </Tab>
</Tabs>

## Track messages

Now you can track messages. The supported roles are `assistant`, `user`, `system`, & `tool`.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    thread.trackMessage({
      role: 'user',
      content: 'Hello, please help me'
    })

    thread.trackMessage({
    role: 'assistant',
    content: 'Hello, how can I help you?'
    })

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    thread.track_message({
      "role": "user",
      "content": "Hello, please help me"
    })

    thread.track_message({
      "role": "assistant",
      "content": "Hello, how can I help you?"
    })
    ```
  </Tab>
</Tabs>

## Track custom events

You can track custom events that happen within your chatbot. This can include things like:

* opening a document
* clicking a button
* submitting a form
* user activity or inactivity
* other events that you want to track

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    thread.trackEvent("event-name")

    // you can also track additional metadata
    thread.trackEvent("open-document", {
    documentName: "my-document.pdf",
    })

    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    thread.track_event("event-name")

    # you can also use the following optional parameters
    thread.track_event("event-name", user_id="user1", user_props={"email": "hello@test.com"}, metadata={})
    ```
  </Tab>
</Tabs>

## Capture user feedback

Finally, you can track user feedback on bot replies:

The ID is the same as the one returned by `trackMessage`.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const msgId = thread.trackMessage({
      role: "assistant",
      content: "Hope you like my answers :)"
    })

    lunary.trackFeedback(msgId, { thumb: "up" })

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    msg_id = thread.track_message({
      "role": "assistant",
      "content": "Hope you like my answers :)"
    })

    lunary.track_feedback(msg_id, { "thumb": "up" })
    ```
  </Tab>
</Tabs>

To remove feedback, pass `null` as the feedback data.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    lunary.trackFeedback(msgId, { thumb: null })
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    lunary.track_feedback(msg_id, { "thumb": None })
    ```
  </Tab>
</Tabs>

## Reconciliate with LLM calls & agents

To take full advantage of Lunary's tracing capabilities, you can reconcile your LLM and agents runs with the messages.

We will automatically reconciliate messages with runs.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const msgId = thread.trackMessage({ role: "user", content: "Hello!" });

    const res = await openai.chat.completions
      .create({
        model: "gpt-4o",
        temperature: 1,
        messages: [message],
      })
      .setParent(msgId);

    thread.trackMessage({
      role: "assistant",
      content: res.choices[0].message.content,
    });
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    msg_id = thread.track_message({ "role": "user", "content": "Hello!" })

    chat_completion = client.chat.completions.create(
        messages=[message],
        model="gpt-4o",
        parent=msg_id
    )

    thread.track_message(
        {"role": "assistant", "content": chat_completion.choices[0].message.content})
    ```
  </Tab>
</Tabs>

If you're using LangChain or agents behind your chatbot, you can inject the current message id into context as a parent:

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const msgId = thread.trackMessage({ role: "user", content: "Hello!" });

    // In your backend, inject the message id into the context

    const agent = lunary.wrapAgent(function ChatbotAgent(query) {
      // your custom code...
    });

    await agent("Hello!").setParent(msgId);
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={null}
    msg_id = thread.track_message({ "role": "user", "content": "Hello!" })

    # In your backend, inject the message id into the context

    with lunary.parent(msg_id):
        # your custom code...
        pass
    ```
  </Tab>
</Tabs>

Note that *it's safe* to pass the message ID from your frontend to your backend, if you're tracking chats directly on the frontend for example.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt