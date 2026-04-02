Source: https://docs.slack.dev/tools/bolt-python/reference/context

# Module slack_bolt.context

All listeners have access to a context dictionary, which can be used to enrich events with additional information. Bolt automatically attaches information that is included in the incoming event, like `user_id`, `team_id`, `channel_id`, and `enterprise_id`.

Refer to [https://docs.slack.dev/tools/bolt-python/concepts/context](https://docs.slack.dev/tools/bolt-python/concepts/context) for details.

## Sub-modules

`[slack_bolt.context.ack](ack/index.html "slack_bolt.context.ack")`

`[slack_bolt.context.assistant](assistant/index.html "slack_bolt.context.assistant")`

`[slack_bolt.context.async_context](async_context.html "slack_bolt.context.async_context")`

`[slack_bolt.context.base_context](base_context.html "slack_bolt.context.base_context")`

`[slack_bolt.context.complete](complete/index.html "slack_bolt.context.complete")`

`[slack_bolt.context.context](context.html "slack_bolt.context.context")`

`[slack_bolt.context.fail](fail/index.html "slack_bolt.context.fail")`

`[slack_bolt.context.get_thread_context](get_thread_context/index.html "slack_bolt.context.get_thread_context")`

`[slack_bolt.context.respond](respond/index.html "slack_bolt.context.respond")`

`[slack_bolt.context.save_thread_context](save_thread_context/index.html "slack_bolt.context.save_thread_context")`

`[slack_bolt.context.say](say/index.html "slack_bolt.context.say")`

`[slack_bolt.context.set_status](set_status/index.html "slack_bolt.context.set_status")`

`[slack_bolt.context.set_suggested_prompts](set_suggested_prompts/index.html "slack_bolt.context.set_suggested_prompts")`

`[slack_bolt.context.set_title](set_title/index.html "slack_bolt.context.set_title")`

## Classes

`class BoltContext (*args, **kwargs)`

Expand source code

```python
class BoltContext(BaseContext):
    """Context object associated with a request from Slack."""

    def to_copyable(self) -> "BoltContext":
        new_dict = {}
        for prop_name, prop_value in self.items():
            if prop_name in self.copyable_standard_property_names:
                # all the standard properties are copiable
                new_dict[prop_name] = prop_value
            elif prop_name in self.non_copyable_standard_property_names:
                # Do nothing with this property (e.g., listener_runner)
                continue
            else:
                try:
                    copied_value = create_copy(prop_value)
                    new_dict[prop_name] = copied_value
                except TypeError as te:
                    self.logger.warning(
                        f"Skipped setting '{prop_name}' to a copied request for lazy listeners "
                        "due to a deep-copy creation error. Consider passing the value not as part of context object "
                        f"(error: {te})"
                    )
        return BoltContext(new_dict)

    # The return type is intentionally string to avoid circular imports
    @property
    def listener_runner(self) -> "ThreadListenerRunner":  # type: ignore[name-defined]
        """The properly configured listener_runner that is available for middleware/listeners."""
        return self["listener_runner"]

    @property
    def client(self) -> WebClient:
        """The `WebClient` instance available for this request.

            @app.event("app_mention")
            def handle_events(context):
                context.client.chat_postMessage(
                    channel=context.channel_id,
                    text="Thanks!",
                )

            # You can access "client" this way too.
            @app.event("app_mention")
            def handle_events(client, context):
                client.chat_postMessage(
                    channel=context.channel_id,
                    text="Thanks!",
                )

        Returns:
            `WebClient` instance
        """
        if "client" not in self:
            self["client"] = WebClient(token=None)
        return self["client"]

    @property
    def ack(self) -> Ack:
        """`ack()` function for this request.

            @app.action("button")
            def handle_button_clicks(context):
                context.ack()

            # You can access "ack" this way too.
            @app.action("button")
            def handle_button_clicks(ack):
                ack()

        Returns:
            Callable `ack()` function
        """
        if "ack" not in self:
            self["ack"] = Ack()
        return self["ack"]

    @property
    def say(self) -> Say:
        """`say()` function for this request.

            @app.action("button")
            def handle_button_clicks(context):
                context.ack()
                context.say("Hi!")

            # You can access "ack" this way too.
            @app.action("button")
            def handle_button_clicks(ack, say):
                ack()
                say("Hi!")

        Returns:
            Callable `say()` function
        """
        if "say" not in self:
            self["say"] = Say(client=self.client, channel=self.channel_id, thread_ts=self.thread_ts)
        return self["say"]

    @property
    def respond(self) -> Optional[Respond]:
        """`respond()` function for this request.

            @app.action("button")
            def handle_button_clicks(context):
                context.ack()
                context.respond("Hi!")

            # You can access "ack" this way too.
            @app.action("button")
            def handle_button_clicks(ack, respond):
                ack()
                respond("Hi!")

        Returns:
            Callable `respond()` function
        """
        if "respond" not in self:
            self["respond"] = Respond(
                response_url=self.response_url,
                proxy=self.client.proxy,
                ssl=self.client.ssl,
            )
        return self["respond"]

    @property
    def complete(self) -> Complete:
        """`complete()` function for this request. Once a custom function's state is set to complete,
        any outputs the function returns will be passed along to the next step of its housing workflow,
        or complete the workflow if the function is the last step in a workflow. Additionally,
        any interactivity handlers associated to a function invocation will no longer be invocable.

            @app.function("reverse")
            def handle_button_clicks(ack, complete):
                ack()
                complete(outputs={"stringReverse":"olleh"})

            @app.function("reverse")
            def handle_button_clicks(context):
                context.ack()
                context.complete(outputs={"stringReverse":"olleh"})

        Returns:
            Callable `complete()` function
        """
        if "complete" not in self:
            self["complete"] = Complete(client=self.client, function_execution_id=self.function_execution_id)
        return self["complete"]

    @property
    def fail(self) -> Fail:
        """`fail()` function for this request. Once a custom function's state is set to error,
        its housing workflow will be interrupted and any provided error message will be passed
        on to the end user through SlackBot. Additionally, any interactivity handlers associated
        to a function invocation will no longer be invocable.

            @app.function("reverse")
            def handle_button_clicks(ack, fail):
                ack()
                fail(error="something went wrong")

            @app.function("reverse")
            def handle_button_clicks(context):
                context.ack()
                context.fail(error="something went wrong")

        Returns:
            Callable `fail()` function
        """
        if "fail" not in self:
            self["fail"] = Fail(client=self.client, function_execution_id=self.function_execution_id)
        return self["fail"]

    @property
    def set_title(self) -> Optional[SetTitle]:
        return self.get("set_title")

    @property
    def set_status(self) -> Optional[SetStatus]:
        return self.get("set_status")

    @property
    def set_suggested_prompts(self) -> Optional[SetSuggestedPrompts]:
        return self.get("set_suggested_prompts")

    @property
    def get_thread_context(self) -> Optional[GetThreadContext]:
        return self.get("get_thread_context")

    @property
    def save_thread_context(self) -> Optional[SaveThreadContext]:
        return self.get("save_thread_context")
```

Context object associated with a request from Slack.

### Ancestors

* [BaseContext](base_context.html#slack_bolt.context.base_context.BaseContext "slack_bolt.context.base_context.BaseContext")
* builtins.dict

### Instance variables

`prop ack : [Ack](ack/ack.html#slack_bolt.context.ack.ack.Ack "slack_bolt.context.ack.ack.Ack")`

Expand source code

```text
@property
def ack(self) -> Ack:
    """`ack()` function for this request.

        @app.action("button")
        def handle_button_clicks(context):
            context.ack()

        # You can access "ack" this way too.
        @app.action("button")
        def handle_button_clicks(ack):
            ack()

    Returns:
        Callable `ack()` function
    """
    if "ack" not in self:
        self["ack"] = Ack()
    return self["ack"]
```

`[slack_bolt.context.ack](ack/index.html "slack_bolt.context.ack")` function for this request.

```text
@app.action("button")
def handle_button_clicks(context):
    context.ack()

# You can access "ack" this way too.
@app.action("button")
def handle_button_clicks(ack):
    ack()
```

## Returns

Callable `[slack_bolt.context.ack](ack/index.html "slack_bolt.context.ack")` function

`prop client : slack_sdk.web.client.WebClient`

Expand source code

```text
@property
def client(self) -> WebClient:
    """The `WebClient` instance available for this request.

        @app.event("app_mention")
        def handle_events(context):
            context.client.chat_postMessage(
                channel=context.channel_id,
                text="Thanks!",
            )

        # You can access "client" this way too.
        @app.event("app_mention")
        def handle_events(client, context):
            client.chat_postMessage(
                channel=context.channel_id,
                text="Thanks!",
            )

    Returns:
        `WebClient` instance
    """
    if "client" not in self:
        self["client"] = WebClient(token=None)
    return self["client"]
```

The `WebClient` instance available for this request.

```text
@app.event("app_mention")
def handle_events(context):
    context.client.chat_postMessage(
        channel=context.channel_id,
        text="Thanks!",
    )

# You can access "client" this way too.
@app.event("app_mention")
def handle_events(client, context):
    client.chat_postMessage(
        channel=context.channel_id,
        text="Thanks!",
    )
```

## Returns

`WebClient` instance

`prop complete : [Complete](complete/complete.html#slack_bolt.context.complete.complete.Complete "slack_bolt.context.complete.complete.Complete")`

Expand source code

```text
@property
def complete(self) -> Complete:
    """`complete()` function for this request. Once a custom function's state is set to complete,
    any outputs the function returns will be passed along to the next step of its housing workflow,
    or complete the workflow if the function is the last step in a workflow. Additionally,
    any interactivity handlers associated to a function invocation will no longer be invocable.

        @app.function("reverse")
        def handle_button_clicks(ack, complete):
            ack()
            complete(outputs={"stringReverse":"olleh"})

        @app.function("reverse")
        def handle_button_clicks(context):
            context.ack()
            context.complete(outputs={"stringReverse":"olleh"})

    Returns:
        Callable `complete()` function
    """
    if "complete" not in self:
        self["complete"] = Complete(client=self.client, function_execution_id=self.function_execution_id)
    return self["complete"]
```

`[slack_bolt.context.complete](complete/index.html "slack_bolt.context.complete")` function for this request. Once a custom function's state is set to complete, any outputs the function returns will be passed along to the next step of its housing workflow, or complete the workflow if the function is the last step in a workflow. Additionally, any interactivity handlers associated to a function invocation will no longer be invocable.

```text
@app.function("reverse")
def handle_button_clicks(ack, complete):
    ack()
    complete(outputs={"stringReverse":"olleh"})

@app.function("reverse")
def handle_button_clicks(context):
    context.ack()
    context.complete(outputs={"stringReverse":"olleh"})
```

## Returns

Callable `[slack_bolt.context.complete](complete/index.html "slack_bolt.context.complete")` function

`prop fail : [Fail](fail/fail.html#slack_bolt.context.fail.fail.Fail "slack_bolt.context.fail.fail.Fail")`

Expand source code

```text
@property
def fail(self) -> Fail:
    """`fail()` function for this request. Once a custom function's state is set to error,
    its housing workflow will be interrupted and any provided error message will be passed
    on to the end user through SlackBot. Additionally, any interactivity handlers associated
    to a function invocation will no longer be invocable.

        @app.function("reverse")
        def handle_button_clicks(ack, fail):
            ack()
            fail(error="something went wrong")

        @app.function("reverse")
        def handle_button_clicks(context):
            context.ack()
            context.fail(error="something went wrong")

    Returns:
        Callable `fail()` function
    """
    if "fail" not in self:
        self["fail"] = Fail(client=self.client, function_execution_id=self.function_execution_id)
    return self["fail"]
```

`[slack_bolt.context.fail](fail/index.html "slack_bolt.context.fail")` function for this request. Once a custom function's state is set to error, its housing workflow will be interrupted and any provided error message will be passed on to the end user through SlackBot. Additionally, any interactivity handlers associated to a function invocation will no longer be invocable.

```text
@app.function("reverse")
def handle_button_clicks(ack, fail):
    ack()
    fail(error="something went wrong")

@app.function("reverse")
def handle_button_clicks(context):
    context.ack()
    context.fail(error="something went wrong")
```

## Returns

Callable `[slack_bolt.context.fail](fail/index.html "slack_bolt.context.fail")` function

`prop get_thread_context : [GetThreadContext](get_thread_context/get_thread_context.html#slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext "slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext") | None`

Expand source code

```text
@property
def get_thread_context(self) -> Optional[GetThreadContext]:
    return self.get("get_thread_context")
```

`prop listener_runner : ThreadListenerRunner`

Expand source code

```text
@property
def listener_runner(self) -> "ThreadListenerRunner":  # type: ignore[name-defined]
    """The properly configured listener_runner that is available for middleware/listeners."""
    return self["listener_runner"]
```

The properly configured listener\_runner that is available for middleware/listeners.

`prop respond : [Respond](respond/respond.html#slack_bolt.context.respond.respond.Respond "slack_bolt.context.respond.respond.Respond") | None`

Expand source code

```text
@property
def respond(self) -> Optional[Respond]:
    """`respond()` function for this request.

        @app.action("button")
        def handle_button_clicks(context):
            context.ack()
            context.respond("Hi!")

        # You can access "ack" this way too.
        @app.action("button")
        def handle_button_clicks(ack, respond):
            ack()
            respond("Hi!")

    Returns:
        Callable `respond()` function
    """
    if "respond" not in self:
        self["respond"] = Respond(
            response_url=self.response_url,
            proxy=self.client.proxy,
            ssl=self.client.ssl,
        )
    return self["respond"]
```

`[slack_bolt.context.respond](respond/index.html "slack_bolt.context.respond")` function for this request.

```text
@app.action("button")
def handle_button_clicks(context):
    context.ack()
    context.respond("Hi!")

# You can access "ack" this way too.
@app.action("button")
def handle_button_clicks(ack, respond):
    ack()
    respond("Hi!")
```

## Returns

Callable `[slack_bolt.context.respond](respond/index.html "slack_bolt.context.respond")` function

`prop save_thread_context : [SaveThreadContext](save_thread_context/save_thread_context.html#slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext "slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext") | None`

Expand source code

```text
@property
def save_thread_context(self) -> Optional[SaveThreadContext]:
    return self.get("save_thread_context")
```

`prop say : [Say](say/say.html#slack_bolt.context.say.say.Say "slack_bolt.context.say.say.Say")`

Expand source code

```text
@property
def say(self) -> Say:
    """`say()` function for this request.

        @app.action("button")
        def handle_button_clicks(context):
            context.ack()
            context.say("Hi!")

        # You can access "ack" this way too.
        @app.action("button")
        def handle_button_clicks(ack, say):
            ack()
            say("Hi!")

    Returns:
        Callable `say()` function
    """
    if "say" not in self:
        self["say"] = Say(client=self.client, channel=self.channel_id, thread_ts=self.thread_ts)
    return self["say"]
```

`[slack_bolt.context.say](say/index.html "slack_bolt.context.say")` function for this request.

```text
@app.action("button")
def handle_button_clicks(context):
    context.ack()
    context.say("Hi!")

# You can access "ack" this way too.
@app.action("button")
def handle_button_clicks(ack, say):
    ack()
    say("Hi!")
```

## Returns

Callable `[slack_bolt.context.say](say/index.html "slack_bolt.context.say")` function

`prop set_status : [SetStatus](set_status/set_status.html#slack_bolt.context.set_status.set_status.SetStatus "slack_bolt.context.set_status.set_status.SetStatus") | None`

Expand source code

```text
@property
def set_status(self) -> Optional[SetStatus]:
    return self.get("set_status")
```

`prop set_suggested_prompts : [SetSuggestedPrompts](set_suggested_prompts/set_suggested_prompts.html#slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts "slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts") | None`

Expand source code

```text
@property
def set_suggested_prompts(self) -> Optional[SetSuggestedPrompts]:
    return self.get("set_suggested_prompts")
```

`prop set_title : [SetTitle](set_title/set_title.html#slack_bolt.context.set_title.set_title.SetTitle "slack_bolt.context.set_title.set_title.SetTitle") | None`

Expand source code

```text
@property
def set_title(self) -> Optional[SetTitle]:
    return self.get("set_title")
```

### Methods

`def to_copyable(self) ‑> [BoltContext](context.html#slack_bolt.context.context.BoltContext "slack_bolt.context.context.BoltContext")`

Expand source code

```python
def to_copyable(self) -> "BoltContext":
    new_dict = {}
    for prop_name, prop_value in self.items():
        if prop_name in self.copyable_standard_property_names:
            # all the standard properties are copiable
            new_dict[prop_name] = prop_value
        elif prop_name in self.non_copyable_standard_property_names:
            # Do nothing with this property (e.g., listener_runner)
            continue
        else:
            try:
                copied_value = create_copy(prop_value)
                new_dict[prop_name] = copied_value
            except TypeError as te:
                self.logger.warning(
                    f"Skipped setting '{prop_name}' to a copied request for lazy listeners "
                    "due to a deep-copy creation error. Consider passing the value not as part of context object "
                    f"(error: {te})"
                )
    return BoltContext(new_dict)
```

### Inherited members

* `**[BaseContext](base_context.html#slack_bolt.context.base_context.BaseContext "slack_bolt.context.base_context.BaseContext")**`:
  * `[actor_enterprise_id](base_context.html#slack_bolt.context.base_context.BaseContext.actor_enterprise_id "slack_bolt.context.base_context.BaseContext.actor_enterprise_id")`
  * `[actor_team_id](base_context.html#slack_bolt.context.base_context.BaseContext.actor_team_id "slack_bolt.context.base_context.BaseContext.actor_team_id")`
  * `[actor_user_id](base_context.html#slack_bolt.context.base_context.BaseContext.actor_user_id "slack_bolt.context.base_context.BaseContext.actor_user_id")`
  * `[authorize_result](base_context.html#slack_bolt.context.base_context.BaseContext.authorize_result "slack_bolt.context.base_context.BaseContext.authorize_result")`
  * `[bot_id](base_context.html#slack_bolt.context.base_context.BaseContext.bot_id "slack_bolt.context.base_context.BaseContext.bot_id")`
  * `[bot_token](base_context.html#slack_bolt.context.base_context.BaseContext.bot_token "slack_bolt.context.base_context.BaseContext.bot_token")`
  * `[bot_user_id](base_context.html#slack_bolt.context.base_context.BaseContext.bot_user_id "slack_bolt.context.base_context.BaseContext.bot_user_id")`
  * `[channel_id](base_context.html#slack_bolt.context.base_context.BaseContext.channel_id "slack_bolt.context.base_context.BaseContext.channel_id")`
  * `[copyable_standard_property_names](base_context.html#slack_bolt.context.base_context.BaseContext.copyable_standard_property_names "slack_bolt.context.base_context.BaseContext.copyable_standard_property_names")`
  * `[enterprise_id](base_context.html#slack_bolt.context.base_context.BaseContext.enterprise_id "slack_bolt.context.base_context.BaseContext.enterprise_id")`
  * `[function_bot_access_token](base_context.html#slack_bolt.context.base_context.BaseContext.function_bot_access_token "slack_bolt.context.base_context.BaseContext.function_bot_access_token")`
  * `[function_execution_id](base_context.html#slack_bolt.context.base_context.BaseContext.function_execution_id "slack_bolt.context.base_context.BaseContext.function_execution_id")`
  * `[inputs](base_context.html#slack_bolt.context.base_context.BaseContext.inputs "slack_bolt.context.base_context.BaseContext.inputs")`
  * `[is_enterprise_install](base_context.html#slack_bolt.context.base_context.BaseContext.is_enterprise_install "slack_bolt.context.base_context.BaseContext.is_enterprise_install")`
  * `[logger](base_context.html#slack_bolt.context.base_context.BaseContext.logger "slack_bolt.context.base_context.BaseContext.logger")`
  * `[matches](base_context.html#slack_bolt.context.base_context.BaseContext.matches "slack_bolt.context.base_context.BaseContext.matches")`
  * `[non_copyable_standard_property_names](base_context.html#slack_bolt.context.base_context.BaseContext.non_copyable_standard_property_names "slack_bolt.context.base_context.BaseContext.non_copyable_standard_property_names")`
  * `[response_url](base_context.html#slack_bolt.context.base_context.BaseContext.response_url "slack_bolt.context.base_context.BaseContext.response_url")`
  * `[standard_property_names](base_context.html#slack_bolt.context.base_context.BaseContext.standard_property_names "slack_bolt.context.base_context.BaseContext.standard_property_names")`
  * `[team_id](base_context.html#slack_bolt.context.base_context.BaseContext.team_id "slack_bolt.context.base_context.BaseContext.team_id")`
  * `[thread_ts](base_context.html#slack_bolt.context.base_context.BaseContext.thread_ts "slack_bolt.context.base_context.BaseContext.thread_ts")`
  * `[token](base_context.html#slack_bolt.context.base_context.BaseContext.token "slack_bolt.context.base_context.BaseContext.token")`
  * `[user_id](base_context.html#slack_bolt.context.base_context.BaseContext.user_id "slack_bolt.context.base_context.BaseContext.user_id")`
  * `[user_token](base_context.html#slack_bolt.context.base_context.BaseContext.user_token "slack_bolt.context.base_context.BaseContext.user_token")`
