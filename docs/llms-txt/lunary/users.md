# Source: https://docs.lunary.ai/docs/features/users.md

# User Tracking

Identify your users, track their cost, conversations and more.

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=d933944893652c32975b66fa049e19dd" alt="User tracking" data-og-width="1364" width="1364" data-og-height="404" height="404" data-path="media/docs/features/users.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=2d4571a9de34629899572cd8e28d19a4 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=57c55c90863b1c7ca4121989ae1f65c7 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=712c73f55b5747ee7cbae3d4b0b107df 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=0059266523892d1d8cbe090c882b0138 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=8f1720eecb018c94e023e7d9227076a6 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/features/users.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=953d9997bcd53a9d4896bbe25baae419 2500w" />

The strict minimum to enable user tracking is to report a `userId`, however you can report any property you'd like such as an email or name using an `userProps` object.

## Tracking users with the backend SDK

<CardGroup cols={2}>
  <Card title="Python" icon="python" href="/docs/integrations/python/installation">
    Learn how to install the Python SDK.
  </Card>

  <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
    Learn how to install the JS SDK.
  </Card>
</CardGroup>

### Identify OpenAI calls

The easiest way to get started tracking users is to send user data with your OpenAI API call.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const res = await openai.chat.completions.create({
      model: "gpt-4o",
      messages: [{ role: "user", content: "Hello" }],
      user: "user123",
      userProps: { name: "John" },
    })
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    chat_completion = client.chat.completions.create(
      model="gpt-4o", 
      messages=[{"role": "user", "content": "Hello"}],
      user_id="user123",
      user_props={ "name": "John" }
    )
    ```
  </Tab>
</Tabs>

If you're using LangChain, you can similarly pass user data as metadata.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    const chat = new ChatOpenAI({
      callbacks: [new LunaryHandler()],
    });

    const res = await chat.call([new HumanMessage("Hello!")], {
    metadata: {
    userId: "123",
    userProps: { name: "John" },
    },
    });

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    handler = LunaryCallbackHandler()

    chat = ChatOpenAI(
      callbacks=[handler],
      metadata={
        "user_id": "user123"
      },  # Assigning user ids to models in the metadata
    )
    ```
  </Tab>
</Tabs>

### Advanced: Inject user into context

When tracking traces, you can inject user data into the context using the `identify` methods. This will cascade down to all the child runs.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    async function TranslatorAgent(input) {
      // Some AI queries
      // Everything done in this context will be tracked with the user
    }

    // Wrap the agent with the monitor
    const translate = lunary.wrapAgent(TranslatorAgent)

    // Using identify to inject the user into the context
    const res = await translate(`Hello, what's your name?`)
    .identify("user123", { email: "email@example.org" })

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    import lunary

    def my_agent():
      # Some AI queries
      # Everything done in this context will be tracked with the user

    def main():
      # Using identify to inject the user into the context
      with lunary.identify('user123', user_props={"email": "email@example.org"}):
        my_agent()
    ```
  </Tab>
</Tabs>

## Identifying users on the frontend

If you are [tracking chat messages](/docs/features/chats) or [feedback](/docs/features/feedback) on the frontend, you can use the `identify` method to identify the user there.

```js  theme={null}
lunary.identify("user123", {
  email: "test@example.org",
});
```

## Identifying Threads

If you are using [threads](/docs/features/threads) to track conversations, you can pass `userId` and `userProps` to the `openThread` method.

```js  theme={null}
const thread = await lunary.openThread({
  userId: "user123",
  userProps: { name: "John" },
});
```

## User Properties

While you can track any property you'd like, we recommend using the following ones:

| Property | Description                             |
| -------- | --------------------------------------- |
| `name`   | Name of the user                        |
| `email`  | Email of the user                       |
| `avatar` | URL to an avatar                        |
| `group`  | Group or company ID the user belongs to |


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt