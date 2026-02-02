# Using AI in Apps

The Slack platform offers features tailored for AI agents and assistants. Your apps can [utilize the `Assistant` class](#assistant) for a side-panel view designed with AI in mind, or they can utilize features applicable to messages throughout Slack, like [chat streaming](#text-streaming) and [feedback buttons](#adding-and-handling-feedback).

If you're unfamiliar with using these features within Slack, you may want to read the [API documentation on the subject](/ai/). Then come back here to implement them with Bolt!

## The `Assistant` class instance

**Some features within this guide require a paid plan**

If you don't have a paid workspace for development, you can join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.

The [`Assistant`](/tools/bolt-js/reference#the-assistantconfig-configuration-object) class can be used to handle the incoming events expected from a user interacting with an app in Slack that has the Agents & AI Apps feature enabled.

A typical flow would look like:

1.  [The user starts a thread](#handling-new-thread). The `Assistant` class handles the incoming [`assistant_thread_started`](/reference/events/assistant_thread_started) event.
2.  [The thread context may change at any point](#handling-thread-context-changes). The `Assistant` class can handle any incoming [`assistant_thread_context_changed`](/reference/events/assistant_thread_context_changed) events. The class also provides a default `context` store to keep track of thread context changes as the user moves through Slack.
3.  [The user responds](#handling-user-response). The `Assistant` class handles the incoming [`message.im`](/reference/events/message.im) event.

```js
const assistant = new Assistant({
  /** 
   * (Recommended) A custom ThreadContextStore can be provided, inclusive of methods to 
   * get and save thread context. When provided, these methods will override the `getThreadContext`
   * and `saveThreadContext` utilities that are made available in other Assistant event listeners.
   */
  // threadContextStore: {
  //   get: async ({ context, client, payload }) => {},
  //   save: async ({ context, client, payload }) => {},
  // },
  
  /** 
   * `assistant_thread_started` is sent when a user opens the Assistant container.
   * This can happen via DM with the app or as a side-container within a channel.
   */
  threadStarted: async ({ event, logger, say, setSuggestedPrompts, saveThreadContext }) => {},
  
  /** 
   * `assistant_thread_context_changed` is sent when a user switches channels
   * while the Assistant container is open. If `threadContextChanged` is not
   * provided, context will be saved using the AssistantContextStore's `save`
   * method (either the DefaultAssistantContextStore or custom, if provided).
   */
  threadContextChanged: async ({ logger, saveThreadContext }) => {},
  
  /** 
   * Messages sent from the user to the Assistant are handled in this listener.
   */
  userMessage: async ({ client, context, logger, message, getThreadContext, say, setTitle, setStatus }) => {}
});
```

**Consider the following**

You _could_ go it alone and [listen](/tools/bolt-js/concepts/event-listening) for the `assistant_thread_started`, `assistant_thread_context_changed`, and `message.im` events in order to implement the AI features in your app. That being said, using the `Assistant` class will streamline the process. And we already wrote this nice guide for you!

While the `assistant_thread_started` and `assistant_thread_context_changed` events do provide Slack-client thread context information, the `message.im` event does not. Any subsequent user message events won't contain thread context data. For that reason, Bolt not only provides a way to store thread context — the `threadContextStore` property — but it also provides a `DefaultThreadContextStore` instance that is utilized by default. This implementation relies on storing and retrieving [message metadata](/messaging/message-metadata/) as the user interacts with the app.

If you do provide your own `threadContextStore` property, it must feature `get` and `save` methods.

**Be sure to give the [reference docs](/tools/bolt-js/reference#agents--assistants) a look!**

### Configuring your app to support the `Assistant` class

1.  Within [App Settings](https://api.slack.com/apps), enable the **Agents & AI Apps** feature.
    
2.  Within the App Settings **OAuth & Permissions** page, add the following scopes:
    

-   [`assistant:write`](/reference/scopes/assistant.write)
-   [`chat:write`](/reference/scopes/chat.write)
-   [`im:history`](/reference/scopes/im.history)

3.  Within the App Settings **Event Subscriptions** page, subscribe to the following events:

-   [`assistant_thread_started`](/reference/events/assistant_thread_started)
-   [`assistant_thread_context_changed`](/reference/events/assistant_thread_context_changed)
-   [`message.im`](/reference/events/message.im)

### Handling a new thread

When the user opens a new thread with your AI-enabled app, the [`assistant_thread_started`](/reference/events/assistant_thread_started) event will be sent to your app. Capture this with the `threadStarted` handler to allow your app to respond.

In the example below, the app is sending a message — containing thread context [message metadata](/messaging/message-metadata/) behind the scenes — to the user, along with a single [prompt](/reference/methods/assistant.threads.setSuggestedPrompts).

```js
threadStarted: async ({ event, logger, say, setSuggestedPrompts, saveThreadContext }) => {
    const { context } = event.assistant_thread;

    try {
      /** 
       * Since context is not sent along with individual user messages, it's necessary to keep
       * track of the context of the conversation to better assist the user. Sending an initial
       * message to the user with context metadata facilitates this, and allows us to update it
       * whenever the user changes context (via the `assistant_thread_context_changed` event).
       * The `say` utility sends this metadata along automatically behind the scenes.
       * !! Please note: this is only intended for development and demonstrative purposes.
       */
      await say('Hi, how can I help?');

      await saveThreadContext();

      /** 
       * Provide the user up to 4 optional, preset prompts to choose from.
       *
       * The first `title` prop is an optional label above the prompts that
       * defaults to 'Try these prompts:' if not provided.
       */
      if (!context.channel_id) {
        await setSuggestedPrompts({
          title: 'Start with this suggested prompt:',
          prompts: [
            {
              title: 'This is a suggested prompt',
              message: 'When a user clicks a prompt, the resulting prompt message text '
                + 'can be passed directly to your LLM for processing.\n\n'
                + 'Assistant, please create some helpful prompts I can provide to '
                + 'my users.'
            },
          ],
        });
      }
    } catch (error) {
      console.error(error);
    }
};
```