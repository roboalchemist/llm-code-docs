# Source: https://docs.crewai.com/en/enterprise/guides/automation-triggers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Triggers Overview

> Understand how CrewAI AMP triggers work, how to manage them, and where to find integration-specific playbooks

CrewAI AMP triggers connect your automations to real-time events across the tools your teams already use. Instead of polling systems or relying on manual kickoffs, triggers listen for changes—new emails, calendar updates, CRM status changes—and immediately launch the crew or flow you specify.

<Frame>
    <img src="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=c31a4b9031f0f517fdce3baa48471f58" alt="Automation Triggers Overview" data-og-width="1024" width="1024" data-og-height="1024" height="1024" data-path="images/enterprise/crew_connectors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=280&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=9e592d155e388bb67d003b26884dc081 280w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=560&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=0c8aa20b2dc82de9ea3d2da6920e4195 560w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=840&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=782fe13ea53120f6d2f8e643a7a7b838 840w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=1100&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=780cd735280c569e6e93caa8262b12d1 1100w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=1650&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=08bfe86a58ca08ec36ae67dca4aa5cf9 1650w, https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/enterprise/crew_connectors.png?w=2500&fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=e2bbe3b0fe0234001e030b501fa4d76c 2500w" />
</Frame>

### Integration Playbooks

Deep-dive guides walk through setup and sample workflows for each integration:

<CardGroup cols={2}>
  <Card title="Gmail Trigger" icon="envelope">
    <a href="/en/enterprise/guides/gmail-trigger">Enable crews when emails arrive or threads update.</a>
  </Card>

  {" "}

  <Card title="Google Calendar Trigger" icon="calendar-days">
    <a href="/en/enterprise/guides/google-calendar-trigger">
      React to calendar events as they are created, updated, or cancelled.
    </a>
  </Card>

  {" "}

  <Card title="Google Drive Trigger" icon="folder-open">
    <a href="/en/enterprise/guides/google-drive-trigger">
      Handle Drive file uploads, edits, and deletions.
    </a>
  </Card>

  {" "}

  <Card title="Outlook Trigger" icon="envelope-open">
    <a href="/en/enterprise/guides/outlook-trigger">
      Automate responses to new Outlook messages and calendar updates.
    </a>
  </Card>

  {" "}

  <Card title="OneDrive Trigger" icon="cloud">
    <a href="/en/enterprise/guides/onedrive-trigger">
      Audit file activity and sharing changes in OneDrive.
    </a>
  </Card>

  {" "}

  <Card title="Microsoft Teams Trigger" icon="comments">
    <a href="/en/enterprise/guides/microsoft-teams-trigger">
      Kick off workflows when new Teams chats start.
    </a>
  </Card>

  {" "}

  <Card title="HubSpot Trigger" icon="hubspot">
    <a href="/en/enterprise/guides/hubspot-trigger">
      Launch automations from HubSpot workflows and lifecycle events.
    </a>
  </Card>

  {" "}

  <Card title="Salesforce Trigger" icon="salesforce">
    <a href="/en/enterprise/guides/salesforce-trigger">
      Connect Salesforce processes to CrewAI for CRM automation.
    </a>
  </Card>

  {" "}

  <Card title="Slack Trigger" icon="slack">
    <a href="/en/enterprise/guides/slack-trigger">
      Start crews directly from Slack slash commands.
    </a>
  </Card>

  <Card title="Zapier Trigger" icon="bolt">
    <a href="/en/enterprise/guides/zapier-trigger">Bridge CrewAI with thousands of Zapier-supported apps.</a>
  </Card>
</CardGroup>

## Trigger Capabilities

With triggers, you can:

* **Respond to real-time events** - Automatically execute workflows when specific conditions are met
* **Integrate with external systems** - Connect with platforms like Gmail, Outlook, OneDrive, JIRA, Slack, Stripe and more
* **Scale your automation** - Handle high-volume events without manual intervention
* **Maintain context** - Access trigger data within your crews and flows

## Managing Triggers

### Viewing Available Triggers

To access and manage your automation triggers:

1. Navigate to your deployment in the CrewAI dashboard
2. Click on the **Triggers** tab to view all available trigger integrations

<Frame caption="Example of available automation triggers for a Gmail deployment">
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5de0e753bcb9db2e7f2e126354741de8" alt="List of available automation triggers" data-og-width="2012" width="2012" data-og-height="862" height="862" data-path="images/enterprise/list-available-triggers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=0b860cce01d60455055d5de942eaf93d 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=10d7cb945ddb53606092a0206e415e2e 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f522f52cf2749038b5654ece72450589 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=f5d89c0da9816cf78e15004f0c82018f 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=bc4ed659f02b96f8312170a00a7ee7f0 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-available-triggers.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=18ed2c13e60731bfb784abd2f403ef01 2500w" />
</Frame>

This view shows all the trigger integrations available for your deployment, along with their current connection status.

### Enabling and Disabling Triggers

Each trigger can be easily enabled or disabled using the toggle switch:

<Frame caption="Enable or disable triggers with toggle">
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=10b3ee6296f323168473593b64a1e4c8" alt="Enable or disable triggers with toggle" data-og-width="1984" width="1984" data-og-height="866" height="866" data-path="images/enterprise/trigger-selected.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=27137c8d8c072ece3319e9f4c8ee0185 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=842109fa147a6a91b9f9480e450a8ee0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5f2cbab1be7662c99854f88496f42b4b 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fa4240b233d980059d3db96c493fda4 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=37f3001a39aab6400b8df45fad9b5cfa 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b2959938cb0f239a6113c9a8b7aa0356 2500w" />
</Frame>

* **Enabled (blue toggle)**: The trigger is active and will automatically execute your deployment when the specified events occur
* **Disabled (gray toggle)**: The trigger is inactive and will not respond to events

Simply click the toggle to change the trigger state. Changes take effect immediately.

### Monitoring Trigger Executions

Track the performance and history of your triggered executions:

<Frame caption="List of executions triggered by automation">
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=be7efd03eb810139e42a10815402158d" alt="List of executions triggered by automation" data-og-width="1950" width="1950" data-og-height="1358" height="1358" data-path="images/enterprise/list-executions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=dbc5685ae07d5239fea0fbd03b24655b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9f8787d340f3d310e37251ac78beab2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=45d7e191c11f9fa36e7efd63702b0369 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7ecd2e3076b92d3d697788cd607bb4a8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7537721cb056fc8782ce423ea7bcde8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5e74d26f3f7807001bac975af3fe38af 2500w" />
</Frame>

## Building Trigger-Driven Automations

Before building your automation, it's helpful to understand the structure of trigger payloads that your crews and flows will receive.

### Trigger Setup Checklist

Before wiring a trigger into production, make sure you:

* Connect the integration under **Tools & Integrations** and complete any OAuth or API key steps
* Enable the trigger toggle on the deployment that should respond to events
* Provide any required environment variables (API tokens, tenant IDs, shared secrets)
* Create or update tasks that can parse the incoming payload within the first crew task or flow step
* Decide whether to pass trigger context automatically using `allow_crewai_trigger_context`
* Set up monitoring—webhook logs, CrewAI execution history, and optional external alerting

### Testing Triggers Locally with CLI

The CrewAI CLI provides powerful commands to help you develop and test trigger-driven automations without deploying to production.

#### List Available Triggers

View all available triggers for your connected integrations:

```bash  theme={null}
crewai triggers list
```

This command displays all triggers available based on your connected integrations, showing:

* Integration name and connection status
* Available trigger types
* Trigger names and descriptions

#### Simulate Trigger Execution

Test your crew with realistic trigger payloads before deployment:

```bash  theme={null}
crewai triggers run <trigger_name>
```

For example:

```bash  theme={null}
crewai triggers run microsoft_onedrive/file_changed
```

This command:

* Executes your crew locally
* Passes a complete, realistic trigger payload
* Simulates exactly how your crew will be called in production

<Warning>
  **Important Development Notes:**

  * Use `crewai triggers run <trigger>` to simulate trigger execution during development
  * Using `crewai run` will NOT simulate trigger calls and won't pass the trigger payload
  * After deployment, your crew will be executed with the actual trigger payload
  * If your crew expects parameters that aren't in the trigger payload, execution may fail
</Warning>

### Triggers with Crew

Your existing crew definitions work seamlessly with triggers, you just need to have a task to parse the received payload:

```python  theme={null}
@CrewBase
class MyAutomatedCrew:
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
        )

    @task
    def parse_trigger_payload(self) -> Task:
        return Task(
            config=self.tasks_config['parse_trigger_payload'],
            agent=self.researcher(),
        )

    @task
    def analyze_trigger_content(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_trigger_data'],
            agent=self.researcher(),
        )
```

The crew will automatically receive and can access the trigger payload through the standard CrewAI context mechanisms.

<Note>
  Crew and Flow inputs can include `crewai_trigger_payload`. CrewAI
  automatically injects this payload: - Tasks: appended to the first task's
  description by default ("Trigger Payload: {crewai_trigger_payload}") - Control
  via `allow_crewai_trigger_context`: set `True` to always inject, `False` to
  never inject - Flows: any `@start()` method that accepts a
  `crewai_trigger_payload` parameter will receive it
</Note>

### Integration with Flows

For flows, you have more control over how trigger data is handled:

#### Accessing Trigger Payload

All `@start()` methods in your flows will accept an additional parameter called `crewai_trigger_payload`:

```python  theme={null}
from crewai.flow import Flow, start, listen

class MyAutomatedFlow(Flow):
    @start()
    def handle_trigger(self, crewai_trigger_payload: dict = None):
        """
        This start method can receive trigger data
        """
        if crewai_trigger_payload:
            # Process the trigger data
            trigger_id = crewai_trigger_payload.get('id')
            event_data = crewai_trigger_payload.get('payload', {})

            # Store in flow state for use by other methods
            self.state.trigger_id = trigger_id
            self.state.trigger_type = event_data

            return event_data

        # Handle manual execution
        return None

    @listen(handle_trigger)
    def process_data(self, trigger_data):
        """
        Process the data from the trigger
        """
        # ... process the trigger
```

#### Triggering Crews from Flows

When kicking off a crew within a flow that was triggered, pass the trigger payload as it:

```python  theme={null}
@start()
def delegate_to_crew(self, crewai_trigger_payload: dict = None):
    """
    Delegate processing to a specialized crew
    """
    crew = MySpecializedCrew()

    # Pass the trigger payload to the crew
    result = crew.crew().kickoff(
        inputs={
            'a_custom_parameter': "custom_value",
            'crewai_trigger_payload': crewai_trigger_payload
        },
    )

    return result
```

## Troubleshooting

**Trigger not firing:**

* Verify the trigger is enabled in your deployment's Triggers tab
* Check integration connection status under Tools & Integrations
* Ensure all required environment variables are properly configured

**Execution failures:**

* Check the execution logs for error details
* Use `crewai triggers run <trigger_name>` to test locally and see the exact payload structure
* Verify your crew can handle the `crewai_trigger_payload` parameter
* Ensure your crew doesn't expect parameters that aren't included in the trigger payload

**Development issues:**

* Always test with `crewai triggers run <trigger>` before deploying to see the complete payload
* Remember that `crewai run` does NOT simulate trigger calls—use `crewai triggers run` instead
* Use `crewai triggers list` to verify which triggers are available for your connected integrations
* After deployment, your crew will receive the actual trigger payload, so test thoroughly locally first

Automation triggers transform your CrewAI deployments into responsive, event-driven systems that can seamlessly integrate with your existing business processes and tools.
