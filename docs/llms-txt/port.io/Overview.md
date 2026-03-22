# Source: https://docs.port.io/workflows/overview.md

# Source: https://docs.port.io/workflows/build-workflows/action-nodes/integration-actions/overview.md

# Source: https://docs.port.io/solutions/security/overview.md

# Source: https://docs.port.io/solutions/resource-self-service/overview.md

# Source: https://docs.port.io/solutions/overview.md

# Source: https://docs.port.io/solutions/incident-management/overview.md

# Source: https://docs.port.io/solutions/engineering-intelligence/overview.md

# Source: https://docs.port.io/solutions/autonomous-ticket-resolution/overview.md

# Source: https://docs.port.io/search-and-query/overview.md

# Source: https://docs.port.io/scorecards/overview.md

# Source: https://docs.port.io/getting-started/overview.md

# Source: https://docs.port.io/customize-pages-dashboards-and-plugins/dashboards/overview.md

# Source: https://docs.port.io/build-your-software-catalog/overview.md

# Source: https://docs.port.io/build-your-software-catalog/custom-integration/ocean-custom-integration/overview.md

# Source: https://docs.port.io/ai-interfaces/port-ai/overview.md

# Source: https://docs.port.io/ai-interfaces/port-ai/llm-providers-management/overview.md

# Source: https://docs.port.io/ai-interfaces/overview.md

# Source: https://docs.port.io/ai-interfaces/ai-agents/overview.md

# Source: https://docs.port.io/actions-and-automations/overview.md

# Overview

One of Port's core offerings is the ability to automate and simplify the processes and routines of your developers.<br /><!-- -->This is done using two powerful tools:

## 1. Actions[â](#1-actions "Direct link to 1. Actions")

Actions are executable pieces of logic that developers or AI agents can run. You can create a wide range of personalized, controlled actions to scaffold a service, provision a cloud resource, or any other logic that serves your organization. Actions drive developer productivity by providing a consistent and repeatable way to perform common tasks, all with guardrails like manual approvals or consumption policies to comply with organizational standards.

For more information and instructions for creating self-service actions, click [here](/actions-and-automations/create-self-service-experiences/.md).

## 2. Automations[â](#2-automations "Direct link to 2. Automations")

Use events in your infrastructure as triggers to run custom workflows. Automations can be used to enforce policies, send notifications, or run any other logic you wish.<br /><!-- -->They are a safe and efficient way to perform routine and repetitive tasks, freeing up your team to focus on other priorities.

For more information and instructions for defining automations, click [here](/actions-and-automations/define-automations/.md).

**ð¡ Don't have a Port account yet?**

<!-- -->

[**Sign up**](https://app.getport.io) **for free**

## Comparison[â](#comparison "Direct link to Comparison")

Technically speaking, the difference between self-service actions and automations is the **trigger**:

* **Self-service actions** are triggered manually by a user, and are typically used for tasks that require user input and/or approval. Actions can have defined user inputs.
* **Automations** are triggered by events in your infrastructure, and are typically used for tasks that are routine and repetitive. Automations do not have user inputs.

### Identical backend & progress reflection[â](#identical-backend--progress-reflection "Direct link to Identical backend & progress reflection")

#### Backend[â](#backend "Direct link to Backend")

For both self-service actions and automations, you define the logic that runs when the action is triggered.<br /><!-- -->Port supports a wide range of backend options to execute your logic, including GitHub workflows, Jenkins pipelines, custom webhooks, and more.

The same backend infrastructure is used for self-service actions and automations, making the backend part of the process identical for both.

For more information about available backends and how to set them up, click [here](/actions-and-automations/setup-backend/.md).

#### Progress reflection[â](#progress-reflection "Direct link to Progress reflection")

When an action or automation is triggered, Port creates an "Action run" object that represents the execution. You can interact with this object to get/set the status of the run, view/add logs, and more.

This object is identical for both self-service actions and automations.

For more information about the "Action run" object and how to interact with it, click [here](/actions-and-automations/reflect-action-progress/.md).
