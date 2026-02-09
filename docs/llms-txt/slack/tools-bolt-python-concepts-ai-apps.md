# Using AI in Apps

The Slack platform offers features tailored for AI agents and assistants. Your apps can [utilize the `Assistant` class](#assistant) for a side-panel view designed with AI in mind, or they can utilize features applicable to messages throughout Slack, like [chat streaming](#text-streaming) and [feedback buttons](#adding-and-handling-feedback).

If you're unfamiliar with using these features within Slack, you may want to read the [API documentation on the subject](/ai/). Then come back here to implement them with Bolt!

## The `Assistant` class instance

<div class="theme-admonition theme-admonition-info">
<span class="admonitionIcon"><svg viewBox="0 0 14 16"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg></span>
<span class="admonitionContent">Some features within this guide require a paid plan</span>
</div>

The [`Assistant`](/tools/bolt-python/reference#the-assistantconfig-configuration-object) class can be used to handle the incoming events expected from a user interacting with an app in Slack that has the Agents & AI Apps feature enabled.

A typical flow would look like:

1.  [The user starts a thread](#handling-new-thread). The `Assistant` class handles the incoming [`assistant_thread_started`](/reference/events/assistant_thread_started) event.
2.  [The thread context may change at any point](#handling-thread-context-changes). The `Assistant` class can handle any incoming [`assistant_thread_context_changed`](/reference/events/assistant_thread_context_changed) events. The class also provides a default `context` store to keep track of thread context changes as the user moves through Slack.
3.  [The user responds](#handling-user-response). The `Assistant` class handles the incoming [`message.im`](/reference/events/message.im) event.

```python
assistant = Assistant()

# This listener is invoked when a human user opened an assistant thread
@assistant.thread_started
def start_assistant_thread(
    say: Say,
    get_thread_context: GetThreadContext,
    set_suggested_prompts: SetSuggestedPrompts,
    logger: logging.Logger,
):
    try:
        # This listener is invoked when the human user sends a reply in the assistant thread
    @assistant.user_message
    def respond_in_assistant_thread(
        client: WebClient,
        context: BoltContext,
        get_thread_context: GetThreadContext,
        logger: logging.Logger,
        payload: dict,
        say: Say,
        set_status: SetStatus,
    ):
        try:
            # Enable this assistant middleware in your Bolt app
            app.use(assistant)
```

<div class="theme-admonition theme-admonition-info">
<span class="admonitionIcon"><svg viewBox="0 0 14 16"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg></span>
<span class="admonitionContent">Consider the following</span>
</div>

<p>You _could_ go it alone and [listen](/tools/bolt-python/concepts/event-listening) for the `assistant_thread_started`, `assistant_thread_context_changed`, and `message.im` events in order to implement the AI features in your app. That being said, using the `Assistant` class will streamline the process. And we already wrote this nice guide for you!</p>

While the `assistant_thread_started` and `assistant_thread_context_changed` events do provide Slack-client thread context information, the `message.im` event does not. Any subsequent user message events won't contain thread context data. For that reason, Bolt not only provides a way to store thread context — the `threadContextStore` property — but it also provides a `DefaultThreadContextStore` instance that is utilized by default. This implementation relies on storing and retrieving [message metadata](/messaging/message-metadata/) as the user interacts with the app.

If you do provide your own `threadContextStore` property, it must feature `get` and `save` methods.

<div class="theme-admonition theme-admonition-tip">
<span class="admonitionIcon"><svg viewBox="0 0 12 16"><path fill-rule="evenodd" d="M6.5 0C3.48 0 1 2.19 1 5c0 .92.55 2.25 1 3 1.34 2.25 1.78 2.78 2 4v1h5v-1c.22-1.22.66-1.75 2-4 .45-.75 1-2.08 1-3 0-2.81-2.48-5-5.5-5zm3.64 7.48c-.25.44-.47.8-.67 1.11-.86 1.41-1.25 2.06-1.45 3.23-.02.05-.02.11-.02.17H5c0-.06 0-.13-.02-.17-.2-1.17-.59-1.83-1.45-3.23-.2-.31-.42-.67-.67-1.11C2.44 6.78 2 5.65 2 5c0-2.2 2.02-4 4.5-4 1.22 0 2.36.42 3.22 1.19C10.55 2.94 11 3.94 11 5c0 .66-.44 1.78-.86 2.48zM4 14h5c-.23 1.14-1.3 2-2.5 2s-2.27-.86-2.5-2z"></path></svg></span>
<span class="admonitionContent">Refer to the [reference docs](https://docs.slack.dev/tools/bolt-python/reference/kwargs_injection/args.html) to learn the available listener arguments.</span>
</div>

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

When the user opens a new thread with your AI-enabled app, the [`assistant_thread_started`](/reference/events/assistant_thread_started) event will be sent to your app.

<div class="theme-admonition theme-admonition-tip">
<span class="admonitionIcon"><svg viewBox="0 0 12 16"><path fill-rule="evenodd" d="M6.5 0C3.48 0 1 2.19 1 5c0 .92.55 2.25 1 3 1.34 2.25 1.78 2.78 2 4v1h5v-1c.22-1.22.66-1.75 2-4 .45-.75 1-2.08 1-3 0-2.81-2.48-5-5.5-5zm3.64 7.48c-.25.44-.47.8-.67 1.11-.86 1.41-1.25 2.06-1.45 3.23-.02.05-.02.11-.02.17H5c0-.06 0-.13-.02-.17-.2-1.17-.59-1.83-1.45-3.23-.2-.31-.42-.67-.67-1.11C2.44 6.78 2 5.65 2 5c0-2.2 2.02-4 4.5-4 1.22 0 2.36.42 3.22 1.19C10.55 2.94 11 3.94 11 5c0 .66-.44 1.78-.86 2.48zM4 14h5c-.23 1.14-1.3 2-2.5 2s-2.27-.86-2.5-2z"></path></svg></span>
<span class="admonitionContent">When a user opens an app thread while in a channel, the channel info is stored as the thread's `AssistantThreadContext` data.</span>
</div>

<p>You can grab that info by using the `get_thread_context` utility, as subsequent user message event payloads won't include the channel info.</p>

```python
assistant = Assistant()

@assistant.thread_started
def start_assistant_thread(
    say: Say,
    get_thread_context: GetThreadContext,
    set_suggested_prompts: SetSuggestedPrompts,
    logger: logging.Logger,
):
    try:
        say("How can I help you?")
        prompts: List[Dict[str, str]] = [
            {
                "title": "Suggest names for my Slack app",
                "message": "Can you suggest a few names for my Slack app? The app helps my teammates better organize information and plan priorities and action items.",
            },
        ]
        thread_context = get_thread_context()
        if thread_context is not None and thread_context.channel_id is not None:
            summarize_channel = {
                "title": "Summarize the referred channel",
                "message": "Can you generate a brief summary of the referred channel?",
            }
            prompts.append(summarize_channel)
        set_suggested_prompts(prompts=prompts)
    except Exception as e:
        logger.exception(f"Failed to handle an assistant_thread_started event: {e}", e)
        say(f":warning: Something went wrong! ({e})")
```

You can send more complex messages to the user — see [block kit](#block-kit).