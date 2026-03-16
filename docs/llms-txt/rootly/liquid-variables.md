# Source: https://docs.rootly.com/collaborative-retrospectives/liquid-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Liquid Variables in Retrospectives

> Learn how to use the Liquid templating engine in retrospective documents and templates to dynamically populate incident data, format content, and create consistent post-incident reviews.

## Overview

Rootly supports the [Liquid](https://shopify.github.io/liquid/) templating engine in retrospective documents and templates. Liquid allows you to insert dynamic placeholders like `{{ incident.title }}` or `{{ incident.severity }}` that automatically resolve to actual incident data when the retrospective is published or exported.

This is especially valuable because retrospective documents often reference the same incident data repeatedly (title, severity, duration, commander, etc.), and the most common failure mode is simple: people copy-paste incorrectly or forget to update values when the incident changes.

Typical uses include:

* Pre-filling retrospective templates with incident metadata
* Referencing incident data without manual copy-paste
* Ensuring consistency when exporting to external systems (Google Docs, Confluence, Notion)
* Creating reusable templates that adapt to each incident automatically

<Info>
  Liquid variables in retrospectives use the same syntax and variable names as [Incident Variables](https://www.notion.so/liquid/incident-variables) in Workflows. If you're familiar with Liquid in Workflows, the same variables are available in the retrospective editor.
</Info>

## Liquid Variables vs Liquid Blocks

Rootly provides two ways to use Liquid in retrospectives:

| Feature        | Liquid Variables                        | Liquid Blocks                                 |
| -------------- | --------------------------------------- | --------------------------------------------- |
| **Insert via** | Type `{{`                               | Type `/liquid`                                |
| **Scope**      | Inline (within text)                    | Block-level (standalone section)              |
| **Syntax**     | `{{ variable }}` with filters           | Full Liquid: `{% if %}`, `{% for %}`, filters |
| **Display**    | Inline chip                             | Edit/Preview panel                            |
| **Best for**   | Inserting dynamic values into sentences | Conditional content, loops, multi-line logic  |

**Use Liquid Variables when** you need to insert a single dynamic value into your text, like "The incident commander was `{{ incident.commander.name }}`."

**Use Liquid Blocks when** you need conditional logic, loops, or multi-line templates—for example, showing different content based on severity or listing all action items.

***

## How to Insert Liquid Variables

### In the Editor

1. **Start typing a variable:** Type `{{` anywhere in the editor to trigger the variable autocomplete.
2. **Filter and select:** Continue typing to filter available variables (e.g., `{{ incident.ti` shows `incident.title`).
3. **Insert the variable:** Click or press Enter to insert the selected variable.
4. **Variable appears as a chip:** The variable displays as a visual chip in the editor, showing the variable name.

### In Templates

Templates support Liquid variables in the same way. When a template is inserted into a retrospective, variables remain as placeholders until the retrospective is published or exported.

<Info>
  Variables in templates allow you to create reusable structures that automatically adapt to each incident to help eliminate manual data entry and reduce errors.
</Info>

### Examples

#### Get the incident title and severity

Expression: `{{ incident.title }} ({{ incident.severity }})`

Sample result: "Database connection timeout (SEV1)"

#### Format a timestamp

Expression: `{{ incident.started_at | date: "%Y-%m-%d %H:%M" }}`

Sample result: "2024-03-15 14:32"

[Reference](https://shopify.github.io/liquid/filters/date/)

#### Get the incident commander's name

Expression: `{{ incident.commander.name }}`

Sample result: "Jane Smith"

#### Build a resource link

Expression: `[Slack Channel]({{ incident.slack_channel_url }})`

Sample result: "[Slack Channel](https://slack.com/archives/C123456)"

<Info>
  Liquid variables are organized by the data they reference. For the complete list of available variables use our [Liquid Markup explorer](https://rootly.com/account/help/liquid-explorer).
</Info>

***

## Liquid Blocks

Liquid Blocks are standalone template sections that support the full Liquid templating language, including conditionals (`{% if %}`), loops (`{% for %}`), and all Liquid filters. They're ideal when you need more than simple variable substitution.

### How to Insert a Liquid Block

1. **Open the slash menu:** Type `/liquid` anywhere in the editor.
2. **Select Liquid Block:** Choose "Liquid Block" from the slash command menu.
3. **Write your template:** Enter your Liquid code in the editor panel that appears.
4. **Preview your output:** Click **Preview** to see the rendered result with real incident data.
5. **Edit as needed:** Toggle back to **Edit** to make changes. The preview updates each time you switch.

<Tip>
  The Preview mode renders your template using actual incident data, so you can verify your logic works correctly before publishing.
</Tip>

### When to Use Liquid Blocks

Liquid Blocks are particularly useful for:

* **Conditional content** based on incident properties (severity, status, etc.)
* **Looping through collections** like action items, services, or team members
* **Complex formatting** that requires multiple variables and logic
* **Reusable template sections** that adapt based on incident context

### Examples

#### Conditional severity messaging

```liquid  theme={null}
{% if incident.severity == "critical" %}
🚨 **CRITICAL INCIDENT** - This incident required immediate escalation and executive notification.
{% elsif incident.severity == "high" %}
⚠️ **High Priority** - This incident impacted production systems and required urgent response.
{% else %}
📋 This incident followed standard response procedures.
{% endif %}
```

#### Loop through action items

```
### Action Items

{% for item in incident.action_items %}
- [{{ item.status }}] {{ item.summary }}
  - **Owner:** {{ item.owner.name }}
  - **Due:** {{ item.due_at | date: "%B %d, %Y" }}
{% endfor %}
```

#### Conditional sections with fallbacks

```
{% if incident.resolved_at %}
**Resolution Time:** {{ incident.resolved_at | date: "%B %d, %Y at %I:%M %p" }}
**Total Duration:** {{ incident.duration }}
{% else %}
⏳ *This incident is still ongoing.*
{% endif %}
```

#### Dynamic team summary

```
### Response Team

{% if incident.commander %}
- **Incident Commander:** {{ incident.commander.name }}
{% endif %}
{% if incident.communication_lead %}
- **Communication Lead:** {{ incident.communication_lead.name }}
{% endif %}
{% for responder in incident.responders %}
- {{ responder.name }} ({{ responder.role }})
{% endfor %}
```

<Info>
  Liquid Blocks have access to all the same variables available to Liquid Variables. Use the [Liquid Markup explorer](https://rootly.com/account/help/liquid-explorer) to see the complete list.
</Info>

### Error Handling

If your Liquid template contains a syntax error, the Preview mode will display an error message describing the issue. Common errors include:

* Unclosed tags (`{% if %}` without `{% endif %}`)
* Undefined variables (check spelling and availability)
* Invalid filter syntax

Fix the error in Edit mode and preview again to verify.

***

## How Variables Resolve

In the editor, variables appear as visual **chips** showing their names, and Liquid Blocks show as editable panels. When you publish or export (to Google Docs, Confluence, etc.), both resolve to their current values, so the final document shows real data instead of placeholders.

<Info>
  Variables always resolve to the **current** value at the time of publish or export. If incident data changes after publishing, the retrospective retains the original resolved values.
</Info>

## Best Practices

* **Use variables for inline values, blocks for logic:** Keep simple insertions as Liquid Variables; use Liquid Blocks when you need conditionals or loops.
* **Use variables in templates:** Templates with variables create consistent retrospectives that auto-populate incident data, eliminating manual entry and reducing errors.
* **Prefer data blocks for timeline/follow-ups:** The `/timeline` and `/followups` data blocks provide richer, interactive display compared to timeline variables.
* \*\*Use the \*\*`default`**filter for optional data:**  If a variable might be empty (e.g., no Jira ticket), use `{{ incident.jira_issue_url | default: "N/A" }}` to provide a fallback.
* **Use role variables for accountability:** Including `{{ incident.commander.name }}` makes ownership clear in the published document.
* **Keep templates DRY:** Define common sections once in a template and let variables fill in the incident-specific details.
* **Preview Liquid Blocks before publishing:** Use the Preview toggle to verify conditional logic and loops render correctly with your incident data.

## Frequently Asked Questions

<Accordion title="Why did my variable resolve to N/A?">
  The referenced data doesn't exist for this incident. For example, `{{ incident.jira_issue_url }}` is empty if no Jira ticket is linked. Use the `default` filter to provide a fallback value.
</Accordion>

<Accordion title="Can I use Liquid logic (if/for) in retrospectives?">
  Yes! Use **Liquid Blocks** for full Liquid logic including conditionals and loops. Type `/liquid` to insert a Liquid Block. Standard **Liquid Variables** (inserted via `{{`) support only variable interpolation and filters.
</Accordion>

<Accordion title="Are these the same variables available in Workflows?">
  Yes. Retrospective Liquid variables use the same syntax and variable names as [Incident Variables](https://www.notion.so/liquid/incident-variables) in Workflows. If you're familiar with Liquid in Workflows, the same variables work in retrospectives.
</Accordion>

<Accordion title="Can I format dates differently?">
  Yes. Use the `date` filter with a format string: `{{ incident.started_at | date: "%B %d, %Y" }}` produces "March 15, 2024". See the [Liquid date filter reference](https://shopify.github.io/liquid/filters/date/) for format options.
</Accordion>

<Accordion title="What's the difference between Liquid Variables and Liquid Blocks?">
  Liquid Variables are inline placeholders for single values (inserted via `{{`). Liquid Blocks are standalone sections that support full Liquid templating including conditionals and loops (inserted via `/liquid`). Use variables for simple value insertion; use blocks when you need logic.
</Accordion>

<Accordion title="Can I nest Liquid Blocks?">
  No, Liquid Blocks are atomic units in the editor. However, you can use nested Liquid logic (like `{% if %}` inside `{% for %}`) within a single Liquid Block.
</Accordion>


Built with [Mintlify](https://mintlify.com).