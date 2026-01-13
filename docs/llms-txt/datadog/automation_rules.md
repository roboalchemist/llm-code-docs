# Source: https://docs.datadoghq.com/incident_response/case_management/automation_rules.md

---
title: Case automation rules
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Case Management > Case automation rules
source_url: https://docs.datadoghq.com/case_management/automation_rules/index.html
---

# Case automation rules

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Case Automation Rules streamline your incident management workflow by automatically triggering actions when specific conditions are met, allowing teams to standardize their response processes.

You can define automated actions based on three key triggers:

- **Case creation** - Automatically assign new cases to on-call team members
- **Status changes** - Trigger follow-up actions when cases move between states
- **Attribute changes** - Respond instantly when case properties like priority are modified

These capabilities deliver faster response times while reducing manual effort. Teams can focus on problem-solving instead of ticket management, ensuring consistent case handling with full audit transparency for compliance and visibility.

## Configuring automation rules{% #configuring-automation-rules %}

To configure automation rules:

1. Navigate to **[Case Management > Settings](https://app.datadoghq.com/cases/settings)**.
1. Select the project you want to create automation rules for.
1. Select **Automation**.
1. Click **New Rule**.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/case_management/automation_rules/create_case_automation_rule.8769f9bbcd715b171cf1deabdf437012.png?auto=format"
   alt="Screenshot of the Create Automation Rule dialog in a case management system. The dialog includes steps to set when to evaluate the rule, specify workflow for rule match, name the rule, and set its status." /%}

Add the following to your configuration:

1. **Define a trigger** - Choose when an automation rule should run:
   1. Upon case creation
   1. When a case's status changes
   1. When a case attribute is added or deleted
1. **Select a workflow** - Leverage [Workflow Automation](https://docs.datadoghq.com/service_management/workflows/) to automate actions such as:
   1. Assigning the case to a team member
   1. Adding comments
   1. Closing a resolved case
1. **Enable and name your rule** - Set a descriptive name for the rule and choose to enable or disable it.

## Further reading{% #further-reading %}

- [Learn more about Case management](https://docs.datadoghq.com/incident_response/case_management)
