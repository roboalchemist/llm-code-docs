# Source: https://docs.crewai.com/en/enterprise/guides/gmail-trigger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Gmail Trigger

> Trigger automations when Gmail events occur (e.g., new emails, labels).

## Overview

Use the Gmail Trigger to kick off your deployed crews when Gmail events happen in connected accounts, such as receiving a new email or messages matching a label/filter.

<Tip>
  Make sure Gmail is connected in Tools & Integrations and the trigger is
  enabled for your deployment.
</Tip>

## Enabling the Gmail Trigger

1. Open your deployment in CrewAI AMP
2. Go to the **Triggers** tab
3. Locate **Gmail** and switch the toggle to enable

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=10b3ee6296f323168473593b64a1e4c8" alt="Enable or disable triggers with toggle" data-og-width="1984" width="1984" data-og-height="866" height="866" data-path="images/enterprise/trigger-selected.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=27137c8d8c072ece3319e9f4c8ee0185 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=842109fa147a6a91b9f9480e450a8ee0 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5f2cbab1be7662c99854f88496f42b4b 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5fa4240b233d980059d3db96c493fda4 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=37f3001a39aab6400b8df45fad9b5cfa 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/trigger-selected.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b2959938cb0f239a6113c9a8b7aa0356 2500w" />
</Frame>

## Example: Process new emails

When a new email arrives, the Gmail Trigger will send the payload to your Crew or Flow. Below is a Crew example that parses and processes the trigger payload.

```python  theme={null}
@CrewBase
class GmailProcessingCrew:
    @agent
    def parser(self) -> Agent:
        return Agent(
            config=self.agents_config['parser'],
        )

    @task
    def parse_gmail_payload(self) -> Task:
        return Task(
            config=self.tasks_config['parse_gmail_payload'],
            agent=self.parser(),
        )

    @task
    def act_on_email(self) -> Task:
        return Task(
            config=self.tasks_config['act_on_email'],
            agent=self.parser(),
        )
```

The Gmail payload will be available via the standard context mechanisms.

### Testing Locally

Test your Gmail trigger integration locally using the CrewAI CLI:

```bash  theme={null}
# View all available triggers
crewai triggers list

# Simulate a Gmail trigger with realistic payload
crewai triggers run gmail/new_email_received
```

The `crewai triggers run` command will execute your crew with a complete Gmail payload, allowing you to test your parsing logic before deployment.

<Warning>
  Use `crewai triggers run gmail/new_email_received` (not `crewai run`) to
  simulate trigger execution during development. After deployment, your crew
  will automatically receive the trigger payload.
</Warning>

## Monitoring Executions

Track history and performance of triggered runs:

<Frame>
  <img src="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=be7efd03eb810139e42a10815402158d" alt="List of executions triggered by automation" data-og-width="1950" width="1950" data-og-height="1358" height="1358" data-path="images/enterprise/list-executions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=280&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=dbc5685ae07d5239fea0fbd03b24655b 280w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=560&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=b9f8787d340f3d310e37251ac78beab2 560w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=840&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=45d7e191c11f9fa36e7efd63702b0369 840w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1100&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=7ecd2e3076b92d3d697788cd607bb4a8 1100w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=1650&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=d7537721cb056fc8782ce423ea7bcde8 1650w, https://mintcdn.com/crewai/Tp3HEbbp9mp-dy3H/images/enterprise/list-executions.png?w=2500&fit=max&auto=format&n=Tp3HEbbp9mp-dy3H&q=85&s=5e74d26f3f7807001bac975af3fe38af 2500w" />
</Frame>

## Troubleshooting

* Ensure Gmail is connected in Tools & Integrations
* Verify the Gmail Trigger is enabled on the Triggers tab
* Test locally with `crewai triggers run gmail/new_email_received` to see the exact payload structure
* Check the execution logs and confirm the payload is passed as `crewai_trigger_payload`
* Remember: use `crewai triggers run` (not `crewai run`) to simulate trigger execution
