# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/how-to/creating-and-using-stages.md

# Creating And Using Stages

> Learn to create and manage stages in Galileo Protect, enabling structured AI monitoring and progressive error resolution throughout the deployment lifecycle.

[Stages](/galileo/gen-ai-studio-products/galileo-protect/concepts/stage) can be managed centrally (i.e. registered once and updated dynamically) or locally within the application. Stages consist of [Rulesets](/galileo/gen-ai-studio-products/galileo-protect/concepts/ruleset) that are applied during one invocation. A stage can be composed of multiple rulesets, each executed independently and defined as a prioritized list (i.e. order matters). The [Action](/galileo/gen-ai-studio-products/galileo-protect/concepts/action) for the ruleset with the highest priority is chosen for composing the response.

<Info>We recommend defining a stage on your user queries and one on your application's output.</Info>

All stages must have names and belong to a project. The project ID is required to create a stage. The stage ID is returned when the stage is created and is required to invoke the stage. Optionally, you can provide a description of the stage.

<Info>Check out [Concepts > Stages](/galileo/gen-ai-studio-products/galileo-protect/concepts/stage) for the difference between a Central and a Local stage, and when to use each.</Info>

## Creating a Stage

To create a stage, you can use the following code snippet:

```py
import galileo_protect as gp

gp.create_stage(name="my first stage", project_id="<project_id>", description="This is my first stage", type="local")  # type can be "central" or "local", default is "local"
```

If you're using central stages, we recommend including the ruleset definitions during stage creation. This way, you can manage the rulesets centrally and update them without changing the invocation code.

```py
import galileo_protect as gp

gp.create_stage(name="my first stage", project_id="<project_id>", description="This is my first stage", type="central", prioritized_rulesets=[
    {
        "rules": [
            {
                "metric": "pii",
                "operator": "contains",
                "target_value": "ssn",
            },
        ],
        "action": {
            "type": "OVERRIDE",
            "choices": [
                "Personal Identifiable Information detected in the model output. Sorry, I cannot answer that question."
            ],
        },
    },
])
```

If you're using local stages, you can define the rulesets within the `gp.invoke()` function during the invocation instead of the `create_stage` operation.

## Defining and Using Actions

Actions define the operation to perform when a ruleset is triggered when using Galileo Protect. These can be:

1. [Override Action](https://protect.docs.rungalileo.io/?h=status#galileo_protect.OverrideAction): The override action allows configuring various choices from which one is chosen at random when all the rulesets for the stage are triggered.

2. [Passthrough Action](https://protect.docs.rungalileo.io/?h=status#galileo_protect.PassthroughAction): The pass-through action does a simple pass-through of the text. This is the default action in case no other action is defined and used when no rulesets are triggered.

## Subscribing to Events for Actions

Actions include configuration for subscriptions which can be set to event destinations (like webhooks) to HTTP POST requests notifications are sent when the ruleset is triggered. Subscriptions can be configured in actions of any type as:

```py
"action": {
    "type": "OVERRIDE",
    "choices": [
        "Personal Identifiable Information detected in the model output. Sorry, I cannot answer that question."
    ],
    "subscriptions": [{"url": "<your-webhook-url>"}],
}
```

By default, notifications are sent to the subscription when they are triggered, but notifications can be sent based on any of the execution statuses. In the below example, notifications will be sent to the specified webhook if there's an error or the ruleset is not triggered.

```py
"action": {
    "type": "OVERRIDE",
    "choices": [
        "Personal Identifiable Information detected in the model output. Sorry, I cannot answer that question."
    ],
    "subscriptions": [{"statuses": ["error", "not_triggered"], "url": "<your-webhook-url>"}],
}
```

The subscribers are sent HTTP POST requests with a payload that matches the [response from the Protect invocation](https://protect.docs.rungalileo.io/#galileo_protect.Response) and is of schema:

```py
{
  "text": "string",
  "trace_metadata": {
    "id": "string",
    "received_at": 0,
    "response_at": 0,
    "execution_time": -1
  },
  "status": "string"
}
```
