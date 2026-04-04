# Source: https://docs.prefect.io/v3/how-to-guides/automations/creating-automations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# How to create automations

> Learn how to define automations that trigger actions based on events.

export const automations = {
  cli: "https://docs.prefect.io/v3/api-ref/cli/automation",
  api: "https://app.prefect.cloud/api/docs#tag/Automations",
  tf: "https://registry.terraform.io/providers/PrefectHQ/prefect/latest/docs/resources/automation"
};

export const COMBINED = ({name, hrefTF, hrefAPI, hrefCLI}) => <p>You can manage {name} with the <a href={hrefCLI}>Prefect CLI</a>, <a href={hrefTF}>Terraform provider</a>, or <a href={hrefAPI}>Prefect API</a>.</p>;

## Create an automation

On the **Automations** page, select the **+** icon to create a new automation. You'll be prompted to configure:

* A [trigger](/v3/concepts/automations#triggers) condition that causes the automation to execute.
* One or more [actions](/v3/concepts/automations#actions) carried out by the automation.
* Details about the automation, such as a name and description.

<COMBINED name="automations" hrefTF={automations.tf} hrefAPI={automations.api} hrefCLI={automations.cli} />

### Create automations with the CLI

You can create automations from YAML or JSON files using the Prefect CLI:

```bash  theme={null}
# Create from a YAML file
prefect automation create --from-file automation.yaml
# or use the short form
prefect automation create -f automation.yaml

# Create from a JSON file  
prefect automation create --from-file automation.json

# Create from a JSON string
prefect automation create --from-json '{"name": "my-automation", "trigger": {...}, "actions": [...]}'
# or use the short form
prefect automation create -j '{"name": "my-automation", "trigger": {...}, "actions": [...]}'
```

#### Single automation example

Here's an example YAML file that creates an automation to cancel long-running flows:

```yaml  theme={null}
name: Cancel Long Running Flows
description: Cancels flows running longer than 5 minutes
enabled: true
trigger:
  type: event
  posture: Proactive
  expect:
    - prefect.flow-run.Completed
  threshold: 1
  within: 300  # 5 minutes
  for_each:
    - prefect.resource.id
actions:
  - type: cancel-flow-run
```

#### Multiple automations example

You can also create multiple automations at once by using the `automations:` key. If any automation fails to create, the command will continue with the remaining automations and report both successes and failures:

```yaml  theme={null}
automations:
  - name: Cancel Long Running Flows
    description: Cancels flows running longer than 30 minutes
    enabled: true
    trigger:
      type: event
      posture: Reactive
      expect:
        - prefect.flow-run.Running
      threshold: 1
      for_each:
        - prefect.resource.id
    actions:
      - type: cancel-flow-run
        
  - name: Notify on Flow Failure
    description: Send notification when flows fail
    enabled: true
    trigger:
      type: event
      posture: Reactive
      expect:
        - prefect.flow-run.Failed
      threshold: 1
    actions:
      - type: send-notification
        subject: "Flow Failed: {{ event.resource.name }}"
        body: "Flow run {{ event.resource.name }} has failed."
```

Or as a JSON array:

```json  theme={null}
[
  {
    "name": "First Automation",
    "trigger": {...},
    "actions": [...]
  },
  {
    "name": "Second Automation", 
    "trigger": {...},
    "actions": [...]
  }
]
```

### Create automations with the Python SDK

You can create and access any automation with the Python SDK's `Automation` class and its methods.

```python  theme={null}
from prefect.automations import Automation
from prefect.events.schemas.automations import EventTrigger
from prefect.events.actions import CancelFlowRun

# creating an automation
automation = Automation(
    name="woodchonk",
    trigger=EventTrigger(
        expect={"animal.walked"},
        match={
            "genus": "Marmota",
            "species": "monax",
        },
        posture="Reactive",
        threshold=3,
    ),
    actions=[CancelFlowRun()],
).create()

# reading the automation
automation = Automation.read(id=automation.id)
# or by name
automation = Automation.read(name="woodchonk")
```


Built with [Mintlify](https://mintlify.com).