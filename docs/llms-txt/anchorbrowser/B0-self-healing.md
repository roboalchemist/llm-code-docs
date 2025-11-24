# Source: https://docs.anchorbrowser.io/B0-self-healing.md

# Self-healing

> Automatically detect and fix task failures with runtime agent intervention

Self-healing enables your tasks to automatically recover from errors by triggering a runtime agent to complete the execution and generate updated code.

## How self-healing works

When self-healing is enabled, B0 monitors task execution for specific error states. If a self-healing trigger is detected, the system automatically:

<Steps>
  <Step title="Runtime agent intervention">
    A runtime agent takes over the current task execution to complete it successfully.
  </Step>

  <Step title="Agent evaluation">
    The completed task is analyzed and compared against the original code to identify the root cause of the failure.
  </Step>

  <Step title="Code generation">
    A new version of the task code is generated with the necessary fixes applied.
  </Step>

  <Step title="Deployment">
    The updated code can be automatically deployed or manually reviewed before deployment.
  </Step>
</Steps>

## Enable self-healing

Self-healing is configured at the task level. You can enable it when creating or updating a task.

```python  theme={null}
from anchor_sdk import Anchor

anchor = Anchor(api_key="your_api_key")

# Create a task with self-healing enabled
task = anchor.tasks.create(
    name="form_submission",
    prompt="Fill out the contact form on example.com",
    self_healing=True,
    self_healing_config={
        "auto_deploy": True,
        "trigger_on": ["timeout", "element_not_found", "navigation_error"]
    }
)
```

```typescript  theme={null}
import { Anchor } from '@anchor-sdk/client';

const anchor = new Anchor({ apiKey: 'your_api_key' });

// Create a task with self-healing enabled
const task = await anchor.tasks.create({
  name: 'form_submission',
  prompt: 'Fill out the contact form on example.com',
  selfHealing: true,
  selfHealingConfig: {
    autoDeploy: true,
    triggerOn: ['timeout', 'element_not_found', 'navigation_error']
  }
});
```

## Configure self-healing triggers

You can specify which error states should trigger self-healing. By default, common failure scenarios are monitored.

```python  theme={null}
# Configure specific error triggers
task = anchor.tasks.update(
    task_id="task_123",
    self_healing_config={
        "trigger_on": [
            "timeout",
            "element_not_found",
            "navigation_error",
            "authentication_failure",
            "captcha_detected"
        ],
        "max_attempts": 3,
        "auto_deploy": False
    }
)
```

```typescript  theme={null}
// Configure specific error triggers
const task = await anchor.tasks.update({
  taskId: 'task_123',
  selfHealingConfig: {
    triggerOn: [
      'timeout',
      'element_not_found',
      'navigation_error',
      'authentication_failure',
      'captcha_detected'
    ],
    maxAttempts: 3,
    autoDeploy: false
  }
});
```

## Auto-deploy fixes

When `auto_deploy` is enabled, the system automatically deploys the updated code after successful validation. This ensures your tasks continue running without manual intervention.

```python  theme={null}
# Enable auto-deploy for immediate fixes
task = anchor.tasks.create(
    name="data_extraction",
    prompt="Extract product prices from the catalog",
    self_healing=True,
    self_healing_config={
        "auto_deploy": True,
        "validation_required": True
    }
)
```

```typescript  theme={null}
// Enable auto-deploy for immediate fixes
const task = await anchor.tasks.create({
  name: 'data_extraction',
  prompt: 'Extract product prices from the catalog',
  selfHealing: true,
  selfHealingConfig: {
    autoDeploy: true,
    validationRequired: true
  }
});
```

## Monitor self-healing events

Track when self-healing is triggered and review the changes made to your tasks.

```python  theme={null}
# Get self-healing history for a task
healing_events = anchor.tasks.get_healing_events(task_id="task_123")

for event in healing_events:
    print(f"Triggered at: {event.timestamp}")
    print(f"Error type: {event.error_type}")
    print(f"Status: {event.status}")
    print(f"Code version: {event.new_version}")
```

```typescript  theme={null}
// Get self-healing history for a task
const healingEvents = await anchor.tasks.getHealingEvents({ taskId: 'task_123' });

healingEvents.forEach(event => {
  console.log(`Triggered at: ${event.timestamp}`);
  console.log(`Error type: ${event.errorType}`);
  console.log(`Status: ${event.status}`);
  console.log(`Code version: ${event.newVersion}`);
});
```

## Disable self-healing

You can disable self-healing at any time for a specific task.

```python  theme={null}
# Disable self-healing
task = anchor.tasks.update(
    task_id="task_123",
    self_healing=False
)
```

```typescript  theme={null}
// Disable self-healing
const task = await anchor.tasks.update({
  taskId: 'task_123',
  selfHealing: false
});
```

<Info>
  Self-healing uses runtime agents to fix errors, which incurs additional costs. Configure triggers carefully to balance reliability and cost efficiency.
</Info>
