# Source: https://docs.rootly.com/ai/ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Discover how Rootly AI supports incident response with proactive guidance, concise summaries, and conversational workflows across the incident lifecycle.

Rootly AI applies generative AI across the entire incident lifecycle, from the moment an alert fires through post-incident analysis. Rather than acting as a separate tool, Rootly AI is embedded directly into incident workflows, helping responders understand what is happening, decide what to do next, and document outcomes with minimal manual effort.

Rootly AI provides proactive guidance, accurate summaries, and contextual insights using simple conversational prompts in both Slack and the web application. All AI capabilities are designed to fit naturally into existing incident response processes without disrupting established workflows.

<Callout icon="brain" color="#FBCFE8">
  Rootly AI is designed to augment incident responders, not replace them. It provides context, suggestions, and summaries while keeping humans in control of decisions and actions.
</Callout>

<Frame>
  <img alt="Rootly AI overview" src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/ai/ai-overview.gif?s=b059f47286d76a465654c2701097f70a" width="600" height="259" data-path="images/ai/ai-overview.gif" />
</Frame>

## What Rootly AI Can Do

Rootly AI supports a focused set of capabilities that map directly to common incident-response needs. Each feature can be used independently and is available when both enabled at the team level and permitted for the specific incident based on privacy settings.

### Generated Incident Titles

Rootly AI can automatically generate concise, descriptive incident titles based on available incident context. This helps teams quickly understand the nature of an incident without manually crafting a summary under pressure. Titles are designed to be short, consistent, and informative, making dashboards, timelines, and retrospectives easier to scan.

### Incident Summarization

Incident Summarization produces a single, coherent summary of what happened during an incident. The summary is generated from incident metadata, timeline events, alerts, action items, and relevant communications. It is intended to capture the problem, impact, trigger or cause when available, resolution steps, and key participants in plain language.

Summaries can be generated and updated during an active incident or after resolution, automatically improving as more information becomes available. Summaries can be generated using `/rootly summary` in Slack or the **Generate Summary** button in the web application.

### Incident Catchup

Incident Catchup helps responders who join an incident after it has already started quickly get oriented. Instead of scrolling through long Slack threads, responders can request a catchup summary that reflects the current state of the incident.

Responders can request a catchup summary using `/rootly catchup` in Slack or the catchup feature in the web application. This is especially useful for long-running or high-severity incidents with heavy communication volume.

### Mitigation and Resolution Summaries

When an incident transitions through key lifecycle stages such as mitigation, resolution, cancellation, or closure, Rootly AI can assist by drafting short explanations of what actions were taken and why. These summaries help ensure that incident timelines and retrospectives accurately reflect decision-making and outcomes without requiring responders to write detailed explanations during or after an incident.

### Ask Rootly AI

Ask Rootly AI allows responders to ask contextual questions using natural language.

In Slack, this appears as a conversational assistant within the incident channel that answers questions about the current incident. In the web application, the AI Copilot enables questions across incident history and aggregated metrics, with the ability to query, filter, group, and visualize incident data.

This capability can be used to understand what has happened so far, identify next steps, draft communications, or analyze trends across incidents.

### Rootly AI Editor

The Rootly AI Editor is available in all text fields throughout the platform, including incident descriptions, summaries, communications, retrospectives, and more. It helps improve written content by fixing grammar, simplifying language, expanding details, or shortening text while preserving meaning.

### Virtual Meeting Bot

Rootly AI can automatically join incident bridge calls on supported meeting platforms including Zoom, Google Meet, Webex, and Microsoft Teams. During meetings, it captures live transcripts and produces post-meeting summaries.

These transcripts and summaries are attached to the incident and can be incorporated into AI-generated summaries and retrospectives.

## Privacy, Security, and Control

Rootly AI is designed with privacy and data isolation as first-class principles. All AI functionality is controlled through team-level settings, allowing organizations to opt in or out of individual features.

AI access is evaluated on a per-incident basis and respects incident visibility and Slack message-scoping rules. For private incidents, AI features are only available when explicitly permitted by configuration.

Sensitive information such as links, emails, and passwords is automatically redacted before being sent to AI providers, and all requests are authenticated and scoped to the requesting organization.

Organizations can also bring their own LLM API keys, including OpenAI or IBM Watsonx, for additional data privacy and segmentation.

<Callout icon="shield" color="#FEF3C7">
  Rootly AI never uses customer data to train models or improve results for other customers. Data sent to AI providers is used solely to deliver Rootly AI functionality.
</Callout>

## Learn More

* [Generated Incident Title](/ai/generated-incident-title)
* [Incident Summarization](/ai/incident-summarization)
* [Incident Catchup](/ai/incident-catchup)
* [Mitigation and Resolution Summary](/ai/mitigation-and-resolution-summary)
* [Ask Rootly AI](/ai/ask-rootly-ai)
* [Rootly AI Editor](/ai/rootly-ai-editor)
* [Virtual Meeting Bot](/ai/ai-meeting-bot)

***

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Is Rootly AI always enabled for incidents?" icon="circle-question">
    No. Rootly AI is controlled through team-level configuration settings and can be enabled or disabled per feature. AI access is also evaluated on a per-incident basis and respects incident visibility and privacy rules.
  </Accordion>

  <Accordion title="Does Rootly AI take actions or change incident data?" icon="hand">
    No. Rootly AI does not take actions or modify incident properties automatically. It provides suggestions, summaries, and contextual guidance while keeping responders fully in control of decisions and updates.
  </Accordion>

  <Accordion title="Is customer data used to train AI models?" icon="lock">
    No. Rootly AI never uses customer data to train models or improve results for other customers. Data sent to AI providers is used solely to deliver Rootly AI functionality.
  </Accordion>

  <Accordion title="Can Rootly AI be used in private incidents?" icon="shield">
    Rootly AI can be used in private incidents only when explicitly permitted by configuration. Access depends on incident visibility settings and Slack message scope controls.
  </Accordion>

  <Accordion title="Where can I configure Rootly AI settings?" icon="gear">
    Rootly AI settings are managed at the team level in the Rootly web application. Each AI capability can be enabled or disabled independently.
  </Accordion>
</AccordionGroup>

***

<Callout icon="life-ring" color="#FFC107">
  **Need help or have a question?**

  Contact us anytime at **[support@rootly.com](mailto:support@rootly.com)**, use the `/rootly support` Slack command, or visit **Getting Help** to start a chat.
</Callout>


Built with [Mintlify](https://mintlify.com).