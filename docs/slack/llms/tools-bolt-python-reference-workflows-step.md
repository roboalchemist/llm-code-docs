Source: https://docs.slack.dev/tools/bolt-python/reference/workflows/step

# Module slack_bolt.workflows.step

## Sub-modules

`[slack_bolt.workflows.step.async_step](async_step.html "slack_bolt.workflows.step.async_step")`

`[slack_bolt.workflows.step.async_step_middleware](async_step_middleware.html "slack_bolt.workflows.step.async_step_middleware")`

`[slack_bolt.workflows.step.internals](internals.html "slack_bolt.workflows.step.internals")`

`[slack_bolt.workflows.step.step](step.html "slack_bolt.workflows.step.step")`

`[slack_bolt.workflows.step.step_middleware](step_middleware.html "slack_bolt.workflows.step.step_middleware")`

`[slack_bolt.workflows.step.utilities](utilities/index.html "slack_bolt.workflows.step.utilities")`

Utilities specific to steps from apps …

## Classes

`class Complete (*, client: slack_sdk.web.client.WebClient, body: dict)`

Expand source code

```python
class Complete:
    """`complete()` utility to tell Slack the completion of a step from app execution.

        def execute(step, complete, fail):
            inputs = step["inputs"]
            # if everything was successful
            outputs = {
                "task_name": inputs["task_name"]["value"],
                "task_description": inputs["task_description"]["value"],
            }
            complete(outputs=outputs)

        ws = WorkflowStep(
            callback_id="add_task",
            edit=edit,
            save=save,
            execute=execute,
        )
        app.step(ws)

    This utility is a thin wrapper of workflows.stepCompleted API method.
    Refer to https://api.slack.com/methods/workflows.stepCompleted for details.
    """

    def __init__(self, *, client: WebClient, body: dict):
        self.client = client
        self.body = body

    def __call__(self, **kwargs) -> None:
        self.client.workflows_stepCompleted(
            workflow_step_execute_id=self.body["event"]["workflow_step"]["workflow_step_execute_id"],
            **kwargs,
        )
```

`complete()` utility to tell Slack the completion of a step from app execution.

```python
def execute(step, complete, fail):
    inputs = step["inputs"]
    # if everything was successful
    outputs = {
        "task_name": inputs["task_name"]["value"],
        "task_description": inputs["task_description"]["value"],
    }
    complete(outputs=outputs)

ws = WorkflowStep(
    callback_id="add_task",
    edit=edit,
    save=save,
    execute=execute,
)
app.step(ws)
```

This utility is a thin wrapper of workflows.stepCompleted API method. Refer to [https://api.slack.com/methods/workflows.stepCompleted](https://api.slack.com/methods/workflows.stepCompleted) for details.

`class Configure (*, callback_id: str, client: slack_sdk.web.client.WebClient, body: dict)`

Expand source code

```python
class Configure:
    """`configure()` utility to send the modal view in Workflow Builder.

        def edit(ack, step, configure):
            ack()

            blocks = [
                {
                    "type": "input",
                    "block_id": "task_name_input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "name",
                        "placeholder": {"type": "plain_text", "text": "Add a task name"},
                    },
                    "label": {"type": "plain_text", "text": "Task name"},
                },
            ]
            configure(blocks=blocks)

        ws = WorkflowStep(
            callback_id="add_task",
            edit=edit,
            save=save,
            execute=execute,
        )
        app.step(ws)

    Refer to https://docs.slack.dev/legacy/legacy-steps-from-apps/ for details.
    """

    def __init__(self, *, callback_id: str, client: WebClient, body: dict):
        self.callback_id = callback_id
        self.client = client
        self.body = body

    def __call__(self, *, blocks: Optional[Sequence[Union[dict, Block]]] = None, **kwargs) -> None:
        self.client.views_open(
            trigger_id=self.body["trigger_id"],
            view={
                "type": "workflow_step",
                "callback_id": self.callback_id,
                "blocks": blocks,
                **kwargs,
            },
        )
```

`configure()` utility to send the modal view in Workflow Builder.

```python
def edit(ack, step, configure):
    ack()

    blocks = [
        {
            "type": "input",
            "block_id": "task_name_input",
            "element": {
                "type": "plain_text_input",
                "action_id": "name",
                "placeholder": {"type": "plain_text", "text": "Add a task name"},
            },
            "label": {"type": "plain_text", "text": "Task name"},
        },
    ]
    configure(blocks=blocks)

ws = WorkflowStep(
    callback_id="add_task",
    edit=edit,
    save=save,
    execute=execute,
)
app.step(ws)
```

Refer to [https://docs.slack.dev/legacy/legacy-steps-from-apps/](https://docs.slack.dev/legacy/legacy-steps-from-apps/) for details.

`class Fail (*, client: slack_sdk.web.client.WebClient, body: dict)`

Expand source code

```python
class Fail:
    """`fail()` utility to tell Slack the execution failure of a step from app.

        def execute(step, complete, fail):
            inputs = step["inputs"]
            # if something went wrong
            error = {"message": "Just testing step failure!"}
            fail(error=error)

        ws = WorkflowStep(
            callback_id="add_task",
            edit=edit,
            save=save,
            execute=execute,
        )
        app.step(ws)

    This utility is a thin wrapper of workflows.stepFailed API method.
    Refer to https://api.slack.com/methods/workflows.stepFailed for details.
    """

    def __init__(self, *, client: WebClient, body: dict):
        self.client = client
        self.body = body

    def __call__(
        self,
        *,
        error: dict,
    ) -> None:
        self.client.workflows_stepFailed(
            workflow_step_execute_id=self.body["event"]["workflow_step"]["workflow_step_execute_id"],
            error=error,
        )
```

`fail()` utility to tell Slack the execution failure of a step from app.

```python
def execute(step, complete, fail):
    inputs = step["inputs"]
    # if something went wrong
    error = {"message": "Just testing step failure!"}
    fail(error=error)

ws = WorkflowStep(
    callback_id="add_task",
    edit=edit,
    save=save,
    execute=execute,
)
app.step(ws)
```

This utility is a thin wrapper of workflows.stepFailed API method. Refer to [https://api.slack.com/methods/workflows.stepFailed](https://api.slack.com/methods/workflows.stepFailed) for details.

`class Update (*, client: slack_sdk.web.client.WebClient, body: dict)`

Expand source code

```python
class Update:
    """`update()` utility to tell Slack the processing results of a `save` listener.

        def save(ack, view, update):
            ack()

            values = view["state"]["values"]
            task_name = values["task_name_input"]["name"]
            task_description = values["task_description_input"]["description"]

            inputs = {
                "task_name": {"value": task_name["value"]},
                "task_description": {"value": task_description["value"]}
            }
            outputs = [
                {
                    "type": "text",
                    "name": "task_name",
                    "label": "Task name",
                },
                {
                    "type": "text",
                    "name": "task_description",
                    "label": "Task description",
                }
            ]
            update(inputs=inputs, outputs=outputs)

        ws = WorkflowStep(
            callback_id="add_task",
            edit=edit,
            save=save,
            execute=execute,
        )
        app.step(ws)

    This utility is a thin wrapper of workflows.stepFailed API method.
    Refer to https://api.slack.com/methods/workflows.updateStep for details.
    """

    def __init__(self, *, client: WebClient, body: dict):
        self.client = client
        self.body = body

    def __call__(self, **kwargs) -> None:
        self.client.workflows_updateStep(
            workflow_step_edit_id=self.body["workflow_step"]["workflow_step_edit_id"],
            **kwargs,
        )
```

`update()` utility to tell Slack the processing results of a `save` listener.

```python
def save(ack, view, update):
    ack()

    values = view["state"]["values"]
    task_name = values["task_name_input"]["name"]
    task_description = values["task_description_input"]["description"]

    inputs = {
        "task_name": {"value": task_name["value"]},
        "task_description": {"value": task_description["value"]}
    }
    outputs = [
        {
            "type": "text",
            "name": "task_name",
            "label": "Task name",
        },
        {
            "type": "text",
            "name": "task_description",
            "label": "Task description",
        }
    ]
    update(inputs=inputs, outputs=outputs)

ws = WorkflowStep(
    callback_id="add_task",
    edit=edit,
    save=save,
    execute=execute,
)
app.step(ws)
```

This utility is a thin wrapper of workflows.stepFailed API method. Refer to [https://api.slack.com/methods/workflows.updateStep](https://api.slack.com/methods/workflows.updateStep) for details.

`class WorkflowStep (*,   callback_id: str | Pattern,   edit: Callable[..., [BoltResponse](../../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | [Listener](../../listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener") | Sequence[Callable],   save: Callable[..., [BoltResponse](../../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | [Listener](../../listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener") | Sequence[Callable],   execute: Callable[..., [BoltResponse](../../response/response.html#slack_bolt.response.response.BoltResponse "slack_bolt.response.response.BoltResponse") | None] | [Listener](../../listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener") | Sequence[Callable],   app_name: str | None = None,   base_logger: logging.Logger | None = None)`

Expand source code

```python
class WorkflowStep:
    callback_id: Union[str, Pattern]
    """The Callback ID of the step from app"""
    edit: Listener
    """`edit` listener, which displays a modal in Workflow Builder"""
    save: Listener
    """`save` listener, which accepts workflow creator's data submission in Workflow Builder"""
    execute: Listener
    """`execute` listener, which processes step from app execution"""

    def __init__(
        self,
        *,
        callback_id: Union[str, Pattern],
        edit: Union[Callable[..., Optional[BoltResponse]], Listener, Sequence[Callable]],
        save: Union[Callable[..., Optional[BoltResponse]], Listener, Sequence[Callable]],
        execute: Union[Callable[..., Optional[BoltResponse]], Listener, Sequence[Callable]],
        app_name: Optional[str] = None,
        base_logger: Optional[Logger] = None,
    ):
        """
        Deprecated:
            Steps from apps for legacy workflows are now deprecated.
            Use new custom steps: https://docs.slack.dev/workflows/workflow-steps/

        Args:
            callback_id: The callback_id for this step from app
            edit: Either a single function or a list of functions for opening a modal in the builder UI
                When it's a list, the first one is responsible for ack() while the rest are lazy listeners.
            save: Either a single function or a list of functions for handling modal interactions in the builder UI
                When it's a list, the first one is responsible for ack() while the rest are lazy listeners.
            execute: Either a single function or a list of functions for handling step from app executions
                When it's a list, the first one is responsible for ack() while the rest are lazy listeners.
            app_name: The app name that can be mainly used for logging
            base_logger: The logger instance that can be used as a template when creating this step's logger
        """
        self.callback_id = callback_id
        app_name = app_name or __name__
        self.edit = self.build_listener(
            callback_id=callback_id,
            app_name=app_name,
            listener_or_functions=edit,
            name="edit",
            base_logger=base_logger,
        )
        self.save = self.build_listener(
            callback_id=callback_id,
            app_name=app_name,
            listener_or_functions=save,
            name="save",
            base_logger=base_logger,
        )
        self.execute = self.build_listener(
            callback_id=callback_id,
            app_name=app_name,
            listener_or_functions=execute,
            name="execute",
            base_logger=base_logger,
        )

    @classmethod
    def builder(cls, callback_id: Union[str, Pattern], base_logger: Optional[Logger] = None) -> WorkflowStepBuilder:
        """
        Deprecated:
            Steps from apps for legacy workflows are now deprecated.
            Use new custom steps: https://docs.slack.dev/workflows/workflow-steps/
        """
        return WorkflowStepBuilder(
            callback_id,
            base_logger=base_logger,
        )

    @classmethod
    def build_listener(
        cls,
        callback_id: Union[str, Pattern],
        app_name: str,
        listener_or_functions: Union[Listener, Callable, List[Callable]],
        name: str,
        matchers: Optional[List[ListenerMatcher]] = None,
        middleware: Optional[List[Middleware]] = None,
        base_logger: Optional[Logger] = None,
    ) -> Listener:
        if listener_or_functions is None:
            raise BoltError(f"{name} listener is required (callback_id: {callback_id})")

        if isinstance(listener_or_functions, Callable):
            listener_or_functions = [listener_or_functions]

        if isinstance(listener_or_functions, Listener):
            return listener_or_functions
        elif isinstance(listener_or_functions, list):
            matchers = matchers if matchers else []
            matchers.insert(
                0,
                cls._build_primary_matcher(
                    name,
                    callback_id,
                    base_logger=base_logger,
                ),
            )
            middleware = middleware if middleware else []
            middleware.insert(
                0,
                cls._build_single_middleware(
                    name,
                    callback_id,
                    base_logger=base_logger,
                ),
            )
            functions = listener_or_functions
            ack_function = functions.pop(0)
            return CustomListener(
                app_name=app_name,
                matchers=matchers,
                middleware=middleware,
                ack_function=ack_function,
                lazy_functions=functions,
                auto_acknowledgement=name == "execute",
                base_logger=base_logger,
            )
        else:
            raise BoltError(f"Invalid {name} listener: {type(listener_or_functions)} detected (callback_id: {callback_id})")

    @classmethod
    def _build_primary_matcher(
        cls,
        name: str,
        callback_id: Union[str, Pattern],
        base_logger: Optional[Logger] = None,
    ) -> ListenerMatcher:
        if name == "edit":
            return workflow_step_edit(callback_id, base_logger=base_logger)
        elif name == "save":
            return workflow_step_save(callback_id, base_logger=base_logger)
        elif name == "execute":
            return workflow_step_execute(callback_id, base_logger=base_logger)
        else:
            raise ValueError(f"Invalid name {name}")

    @classmethod
    def _build_single_middleware(
        cls,
        name: str,
        callback_id: Union[str, Pattern],
        base_logger: Optional[Logger] = None,
    ) -> Middleware:
        if name == "edit":
            return _build_edit_listener_middleware(callback_id, base_logger=base_logger)
        elif name == "save":
            return _build_save_listener_middleware(base_logger=base_logger)
        elif name == "execute":
            return _build_execute_listener_middleware(base_logger=base_logger)
        else:
            raise ValueError(f"Invalid name {name}")
```

## Deprecated

Steps from apps for legacy workflows are now deprecated. Use new custom steps: [https://docs.slack.dev/workflows/workflow-steps/](https://docs.slack.dev/workflows/workflow-steps/)

## Args

## `callback_id`

The callback\_id for this step from app

## `edit`

Either a single function or a list of functions for opening a modal in the builder UI When it's a list, the first one is responsible for ack() while the rest are lazy listeners.

## `save`

Either a single function or a list of functions for handling modal interactions in the builder UI When it's a list, the first one is responsible for ack() while the rest are lazy listeners.

## `execute`

Either a single function or a list of functions for handling step from app executions When it's a list, the first one is responsible for ack() while the rest are lazy listeners.

## `app_name`

The app name that can be mainly used for logging

## `base_logger`

The logger instance that can be used as a template when creating this step's logger

### Class variables

`var callback_id : str | Pattern`

The Callback ID of the step from app

`var edit : [Listener](../../listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener")`

`edit` listener, which displays a modal in Workflow Builder

`var execute : [Listener](../../listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener")`

`execute` listener, which processes step from app execution

`var save : [Listener](../../listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener")`

`save` listener, which accepts workflow creator's data submission in Workflow Builder

### Static methods

`def build_listener(callback_id: str | Pattern,   app_name: str,   listener_or_functions: [Listener](../../listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener") | Callable | List[Callable],   name: str,   matchers: List[[ListenerMatcher](../../listener_matcher/listener_matcher.html#slack_bolt.listener_matcher.listener_matcher.ListenerMatcher "slack_bolt.listener_matcher.listener_matcher.ListenerMatcher")] | None = None,   middleware: List[[Middleware](../../middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")] | None = None,   base_logger: logging.Logger | None = None) ‑> [Listener](../../listener/listener.html#slack_bolt.listener.listener.Listener "slack_bolt.listener.listener.Listener")`

`def builder(callback_id: str | Pattern, base_logger: logging.Logger | None = None) ‑> [WorkflowStepBuilder](step.html#slack_bolt.workflows.step.step.WorkflowStepBuilder "slack_bolt.workflows.step.step.WorkflowStepBuilder")`

## Deprecated

Steps from apps for legacy workflows are now deprecated. Use new custom steps: [https://docs.slack.dev/workflows/workflow-steps/](https://docs.slack.dev/workflows/workflow-steps/)

`class WorkflowStepMiddleware (step: [WorkflowStep](step.html#slack_bolt.workflows.step.step.WorkflowStep "slack_bolt.workflows.step.step.WorkflowStep"))`

Expand source code

```python
class WorkflowStepMiddleware(Middleware):
    """Base middleware for step from app specific ones"""

    def __init__(self, step: WorkflowStep):
        self.step = step

    def process(
        self,
        *,
        req: BoltRequest,
        resp: BoltResponse,
        # As this method is not supposed to be invoked by bolt-python users,
        # the naming conflict with the built-in one affects
        # only the internals of this method
        next: Callable[[], BoltResponse],
    ) -> Optional[BoltResponse]:

        if self.step.edit.matches(req=req, resp=resp):
            resp = self._run(self.step.edit, req, resp)
            if resp is not None:
                return resp
        elif self.step.save.matches(req=req, resp=resp):
            resp = self._run(self.step.save, req, resp)
            if resp is not None:
                return resp
        elif self.step.execute.matches(req=req, resp=resp):
            resp = self._run(self.step.execute, req, resp)
            if resp is not None:
                return resp

        return next()

    @staticmethod
    def _run(
        listener: Listener,
        req: BoltRequest,
        resp: BoltResponse,
    ) -> Optional[BoltResponse]:
        resp, next_was_not_called = listener.run_middleware(req=req, resp=resp)
        if next_was_not_called:
            return None

        return req.context.listener_runner.run(
            request=req,
            response=resp,
            listener_name=get_name_for_callable(listener.ack_function),
            listener=listener,
        )
```

Base middleware for step from app specific ones

### Ancestors

* [Middleware](../../middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")

### Inherited members

* `**[Middleware](../../middleware/middleware.html#slack_bolt.middleware.middleware.Middleware "slack_bolt.middleware.middleware.Middleware")**`:
  * `[name](../../middleware/middleware.html#slack_bolt.middleware.middleware.Middleware.name "slack_bolt.middleware.middleware.Middleware.name")`
  * `[process](../../middleware/middleware.html#slack_bolt.middleware.middleware.Middleware.process "slack_bolt.middleware.middleware.Middleware.process")`
