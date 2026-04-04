Source: https://docs.slack.dev/tools/bolt-python/reference/kwargs_injection

# Module slack_bolt.kwargs_injection

For middleware/listener arguments, Bolt does flexible data injection in accordance with their names.

To learn the available arguments, check `[slack_bolt.kwargs_injection.args](args.html "slack_bolt.kwargs_injection.args")`'s API document. For steps from apps, checking `[slack_bolt.workflows.step.utilities](../workflows/step/utilities/index.html "slack_bolt.workflows.step.utilities")` as well should be helpful.

## Sub-modules

`[slack_bolt.kwargs_injection.args](args.html "slack_bolt.kwargs_injection.args")`

`[slack_bolt.kwargs_injection.async_args](async_args.html "slack_bolt.kwargs_injection.async_args")`

`[slack_bolt.kwargs_injection.async_utils](async_utils.html "slack_bolt.kwargs_injection.async_utils")`

`[slack_bolt.kwargs_injection.utils](utils.html "slack_bolt.kwargs_injection.utils")`

## Functions

`def build_required_kwargs(*,   logger: logging.Logger,   required_arg_names: MutableSequence[str],   request: [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   response: [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None,   next_func: Callable[[], None] | None = None,   this_func: Callable | None = None,   error: Exception | None = None,   next_keys_required: bool = True) ‑> Dict[str, Any]`

Expand source code

```python
def build_required_kwargs(
    *,
    logger: logging.Logger,
    required_arg_names: MutableSequence[str],
    request: BoltRequest,
    response: Optional[BoltResponse],
    next_func: Optional[Callable[[], None]] = None,
    this_func: Optional[Callable] = None,
    error: Optional[Exception] = None,  # for error handlers
    next_keys_required: bool = True,  # False for listeners / middleware / error handlers
) -> Dict[str, Any]:
    all_available_args = {
        "logger": logger,
        "client": request.context.client,
        "req": request,
        "request": request,
        "resp": response,
        "response": response,
        "context": request.context,
        # payload
        "body": request.body,
        "options": to_options(request.body),
        "shortcut": to_shortcut(request.body),
        "action": to_action(request.body),
        "view": to_view(request.body),
        "command": to_command(request.body),
        "event": to_event(request.body),
        "message": to_message(request.body),
        "step": to_step(request.body),
        # utilities
        "ack": request.context.ack,
        "say": request.context.say,
        "respond": request.context.respond,
        "complete": request.context.complete,
        "fail": request.context.fail,
        "set_status": request.context.set_status,
        "set_title": request.context.set_title,
        "set_suggested_prompts": request.context.set_suggested_prompts,
        "save_thread_context": request.context.save_thread_context,
        # middleware
        "next": next_func,
        "next_": next_func,  # for the middleware using Python's built-in `next()` function
        # error handler
        "error": error,  # Exception
    }
    if not next_keys_required:
        all_available_args.pop("next")
        all_available_args.pop("next_")

    all_available_args["payload"] = (
        all_available_args["options"]
        or all_available_args["shortcut"]
        or all_available_args["action"]
        or all_available_args["view"]
        or all_available_args["command"]
        or all_available_args["event"]
        or all_available_args["message"]
        or all_available_args["step"]
        or request.body
    )
    for k, v in request.context.items():
        if k not in all_available_args:
            all_available_args[k] = v

    if len(required_arg_names) > 0:
        # To support instance/class methods in a class for listeners/middleware,
        # check if the first argument is either self or cls
        first_arg_name = required_arg_names[0]
        if first_arg_name in {"self", "cls"}:
            required_arg_names.pop(0)
        elif first_arg_name not in all_available_args.keys() and first_arg_name != "args":
            if this_func is None:
                logger.warning(warning_skip_uncommon_arg_name(first_arg_name))
                required_arg_names.pop(0)
            elif inspect.ismethod(this_func):
                # We are sure that we should skip manipulating this arg
                required_arg_names.pop(0)

    kwargs: Dict[str, Any] = {k: v for k, v in all_available_args.items() if k in required_arg_names}
    found_arg_names = kwargs.keys()
    for name in required_arg_names:
        if name == "args":
            if isinstance(request, BoltRequest):
                kwargs[name] = Args(**all_available_args)  # type: ignore[arg-type]
            else:
                logger.warning(f"Unknown Request object type detected ({type(request)})")

        elif name not in found_arg_names:
            logger.warning(f"{name} is not a valid argument")
            kwargs[name] = None
    return kwargs
```

## Classes

`class Args (*,   logger: logging.Logger,   client: slack_sdk.web.client.WebClient,   req: [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest"),   resp: [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse"),   context: [BoltContext](../context/context.html#slack_bolt.context.context.BoltContext "slack_bolt.context.context.BoltContext"),   body: Dict[str, Any],   payload: Dict[str, Any],   options: Dict[str, Any] | None = None,   shortcut: Dict[str, Any] | None = None,   action: Dict[str, Any] | None = None,   view: Dict[str, Any] | None = None,   command: Dict[str, Any] | None = None,   event: Dict[str, Any] | None = None,   message: Dict[str, Any] | None = None,   ack: [Ack](../context/ack/ack.html#slack_bolt.context.ack.ack.Ack "slack_bolt.context.ack.ack.Ack"),   say: [Say](../context/say/say.html#slack_bolt.context.say.say.Say "slack_bolt.context.say.say.Say"),   respond: [Respond](../context/respond/respond.html#slack_bolt.context.respond.respond.Respond "slack_bolt.context.respond.respond.Respond"),   complete: [Complete](../context/complete/complete.html#slack_bolt.context.complete.complete.Complete "slack_bolt.context.complete.complete.Complete"),   fail: [Fail](../context/fail/fail.html#slack_bolt.context.fail.fail.Fail "slack_bolt.context.fail.fail.Fail"),   set_status: [SetStatus](../context/set_status/set_status.html#slack_bolt.context.set_status.set_status.SetStatus "slack_bolt.context.set_status.set_status.SetStatus") | None = None,   set_title: [SetTitle](../context/set_title/set_title.html#slack_bolt.context.set_title.set_title.SetTitle "slack_bolt.context.set_title.set_title.SetTitle") | None = None,   set_suggested_prompts: [SetSuggestedPrompts](../context/set_suggested_prompts/set_suggested_prompts.html#slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts "slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts") | None = None,   get_thread_context: [GetThreadContext](../context/get_thread_context/get_thread_context.html#slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext "slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext") | None = None,   save_thread_context: [SaveThreadContext](../context/save_thread_context/save_thread_context.html#slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext "slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext") | None = None,   next: Callable[[], None],   **kwargs)`

Expand source code

```python
class Args:
    """All the arguments in this class are available in any middleware / listeners.
    You can inject the named variables in the argument list in arbitrary order.

        @app.action("link_button")
        def handle_buttons(ack, respond, logger, context, body, client):
            logger.info(f"request body: {body}")
            ack()
            if context.channel_id is not None:
                respond("Hi!")
            client.views_open(
                trigger_id=body["trigger_id"],
                view={ ... }
            )

    Alternatively, you can include a parameter named `args` and it will be injected with an instance of this class.

        @app.action("link_button")
        def handle_buttons(args):
            args.logger.info(f"request body: {args.body}")
            args.ack()
            if args.context.channel_id is not None:
                args.respond("Hi!")
            args.client.views_open(
                trigger_id=args.body["trigger_id"],
                view={ ... }
            )

    """

    client: WebClient
    """`slack_sdk.web.WebClient` instance with a valid token"""
    logger: Logger
    """Logger instance"""
    req: BoltRequest
    """Incoming request from Slack"""
    resp: BoltResponse
    """Response representation"""
    request: BoltRequest
    """Incoming request from Slack"""
    response: BoltResponse
    """Response representation"""
    context: BoltContext
    """Context data associated with the incoming request"""
    body: Dict[str, Any]
    """Parsed request body data"""
    # payload
    payload: Dict[str, Any]
    """The unwrapped core data in the request body"""
    options: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.options` listener"""
    shortcut: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.shortcut` listener"""
    action: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.action` listener"""
    view: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.view` listener"""
    command: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.command` listener"""
    event: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.event` listener"""
    message: Optional[Dict[str, Any]]  # payload alias
    """An alias for payload in an `@app.message` listener"""
    # utilities
    ack: Ack
    """`ack()` utility function, which returns acknowledgement to the Slack servers"""
    say: Say
    """`say()` utility function, which calls `chat.postMessage` API with the associated channel ID"""
    respond: Respond
    """`respond()` utility function, which utilizes the associated `response_url`"""
    complete: Complete
    """`complete()` utility function, signals a successful completion of the custom function"""
    fail: Fail
    """`fail()` utility function, signal that the custom function failed to complete"""
    set_status: Optional[SetStatus]
    """`set_status()` utility function for AI Agents & Assistants"""
    set_title: Optional[SetTitle]
    """`set_title()` utility function for AI Agents & Assistants"""
    set_suggested_prompts: Optional[SetSuggestedPrompts]
    """`set_suggested_prompts()` utility function for AI Agents & Assistants"""
    get_thread_context: Optional[GetThreadContext]
    """`get_thread_context()` utility function for AI Agents & Assistants"""
    save_thread_context: Optional[SaveThreadContext]
    """`save_thread_context()` utility function for AI Agents & Assistants"""
    # middleware
    next: Callable[[], None]
    """`next()` utility function, which tells the middleware chain that it can continue with the next one"""
    next_: Callable[[], None]
    """An alias of `next()` for avoiding the Python built-in method overrides in middleware functions"""

    def __init__(
        self,
        *,
        logger: logging.Logger,
        client: WebClient,
        req: BoltRequest,
        resp: BoltResponse,
        context: BoltContext,
        body: Dict[str, Any],
        payload: Dict[str, Any],
        options: Optional[Dict[str, Any]] = None,
        shortcut: Optional[Dict[str, Any]] = None,
        action: Optional[Dict[str, Any]] = None,
        view: Optional[Dict[str, Any]] = None,
        command: Optional[Dict[str, Any]] = None,
        event: Optional[Dict[str, Any]] = None,
        message: Optional[Dict[str, Any]] = None,
        ack: Ack,
        say: Say,
        respond: Respond,
        complete: Complete,
        fail: Fail,
        set_status: Optional[SetStatus] = None,
        set_title: Optional[SetTitle] = None,
        set_suggested_prompts: Optional[SetSuggestedPrompts] = None,
        get_thread_context: Optional[GetThreadContext] = None,
        save_thread_context: Optional[SaveThreadContext] = None,
        # As this method is not supposed to be invoked by bolt-python users,
        # the naming conflict with the built-in one affects
        # only the internals of this method
        next: Callable[[], None],
        **kwargs,  # noqa
    ):
        self.logger: logging.Logger = logger
        self.client: WebClient = client
        self.request = self.req = req
        self.response = self.resp = resp
        self.context: BoltContext = context

        self.body: Dict[str, Any] = body
        self.payload: Dict[str, Any] = payload
        self.options: Optional[Dict[str, Any]] = options
        self.shortcut: Optional[Dict[str, Any]] = shortcut
        self.action: Optional[Dict[str, Any]] = action
        self.view: Optional[Dict[str, Any]] = view
        self.command: Optional[Dict[str, Any]] = command
        self.event: Optional[Dict[str, Any]] = event
        self.message: Optional[Dict[str, Any]] = message

        self.ack: Ack = ack
        self.say: Say = say
        self.respond: Respond = respond
        self.complete: Complete = complete
        self.fail: Fail = fail

        self.set_status = set_status
        self.set_title = set_title
        self.set_suggested_prompts = set_suggested_prompts
        self.get_thread_context = get_thread_context
        self.save_thread_context = save_thread_context

        self.next: Callable[[], None] = next
        self.next_: Callable[[], None] = next
```

All the arguments in this class are available in any middleware / listeners. You can inject the named variables in the argument list in arbitrary order.

```text
@app.action("link_button")
def handle_buttons(ack, respond, logger, context, body, client):
    logger.info(f"request body: {body}")
    ack()
    if context.channel_id is not None:
        respond("Hi!")
    client.views_open(
        trigger_id=body["trigger_id"],
        view={ ... }
    )
```

Alternatively, you can include a parameter named `[slack_bolt.kwargs_injection.args](args.html "slack_bolt.kwargs_injection.args")` and it will be injected with an instance of this class.

```text
@app.action("link_button")
def handle_buttons(args):
    args.logger.info(f"request body: {args.body}")
    args.ack()
    if args.context.channel_id is not None:
        args.respond("Hi!")
    args.client.views_open(
        trigger_id=args.body["trigger_id"],
        view={ ... }
    )
```

### Class variables

`var ack : [Ack](../context/ack/ack.html#slack_bolt.context.ack.ack.Ack "slack_bolt.context.ack.ack.Ack")`

`ack()` utility function, which returns acknowledgement to the Slack servers

`var action : Dict[str, Any] | None`

An alias for payload in an `@app.action` listener

`var body : Dict[str, Any]`

Parsed request body data

`var client : slack_sdk.web.client.WebClient`

`slack_sdk.web.WebClient` instance with a valid token

`var command : Dict[str, Any] | None`

An alias for payload in an `@app.command` listener

`var complete : [Complete](../context/complete/complete.html#slack_bolt.context.complete.complete.Complete "slack_bolt.context.complete.complete.Complete")`

`complete()` utility function, signals a successful completion of the custom function

`var context : [BoltContext](../context/context.html#slack_bolt.context.context.BoltContext "slack_bolt.context.context.BoltContext")`

Context data associated with the incoming request

`var event : Dict[str, Any] | None`

An alias for payload in an `@app.event` listener

`var fail : [Fail](../context/fail/fail.html#slack_bolt.context.fail.fail.Fail "slack_bolt.context.fail.fail.Fail")`

`fail()` utility function, signal that the custom function failed to complete

`var get_thread_context : [GetThreadContext](../context/get_thread_context/get_thread_context.html#slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext "slack_bolt.context.get_thread_context.get_thread_context.GetThreadContext") | None`

`get_thread_context()` utility function for AI Agents & Assistants

`var logger : logging.Logger`

Logger instance

`var message : Dict[str, Any] | None`

An alias for payload in an `@app.message` listener

`var next : Callable[[], None]`

`next()` utility function, which tells the middleware chain that it can continue with the next one

`var next_ : Callable[[], None]`

An alias of `next()` for avoiding the Python built-in method overrides in middleware functions

`var options : Dict[str, Any] | None`

An alias for payload in an `@app.options` listener

`var payload : Dict[str, Any]`

The unwrapped core data in the request body

`var req : [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest")`

Incoming request from Slack

`var request : [BoltRequest](../request/request.html#slack_bolt.request.request.BoltRequest "slack_bolt.request.request.BoltRequest")`

Incoming request from Slack

`var resp : [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")`

Response representation

`var respond : [Respond](../context/respond/respond.html#slack_bolt.context.respond.respond.Respond "slack_bolt.context.respond.respond.Respond")`

`respond()` utility function, which utilizes the associated `response_url`

`var response : [BoltResponse](../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse")`

Response representation

`var save_thread_context : [SaveThreadContext](../context/save_thread_context/save_thread_context.html#slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext "slack_bolt.context.save_thread_context.save_thread_context.SaveThreadContext") | None`

`save_thread_context()` utility function for AI Agents & Assistants

`var say : [Say](../context/say/say.html#slack_bolt.context.say.say.Say "slack_bolt.context.say.say.Say")`

`say()` utility function, which calls `chat.postMessage` API with the associated channel ID

`var set_status : [SetStatus](../context/set_status/set_status.html#slack_bolt.context.set_status.set_status.SetStatus "slack_bolt.context.set_status.set_status.SetStatus") | None`

`set_status()` utility function for AI Agents & Assistants

`var set_suggested_prompts : [SetSuggestedPrompts](../context/set_suggested_prompts/set_suggested_prompts.html#slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts "slack_bolt.context.set_suggested_prompts.set_suggested_prompts.SetSuggestedPrompts") | None`

`set_suggested_prompts()` utility function for AI Agents & Assistants

`var set_title : [SetTitle](../context/set_title/set_title.html#slack_bolt.context.set_title.set_title.SetTitle "slack_bolt.context.set_title.set_title.SetTitle") | None`

`set_title()` utility function for AI Agents & Assistants

`var shortcut : Dict[str, Any] | None`

An alias for payload in an `@app.shortcut` listener

`var view : Dict[str, Any] | None`

An alias for payload in an `@app.view` listener
