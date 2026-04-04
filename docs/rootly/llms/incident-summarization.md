# Source: https://docs.rootly.com/ai/incident-summarization.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Incident Summarization

> Generate AI-powered summaries of the current incident that capture the problem, impact, resolution steps, and key participants in a single coherent overview.

## Overview

Incident Summarization generates a concise, single-paragraph summary of the current incident using the information available at the time of generation. Rootly AI compiles context from incident metadata, alerts, timeline events, action items, and communications to produce a clear narrative that helps responders quickly understand what happened and how it was addressed.

Summaries can be generated during an active incident or after resolution. As more details are added over time, the summary can be regenerated to reflect the most accurate and up-to-date state of the incident.

## How to Generate an Incident Summary

You can generate or regenerate an incident summary from both the web application and Slack.

### Via the Web

Within an incident, click **Generate Summary** to create a summary using Rootly AI.

<Frame>
  <img alt="Generate incident summary in web UI" src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/ai/inc-sum.gif?s=d2a780b849b387381a7ffcb8906e2a44" width="600" height="259" data-path="images/ai/inc-sum.gif" />
</Frame>

### Via Slack

In an incident Slack channel, run `/rootly summary` to generate a summary. You can regenerate the summary at any point as the incident evolves.

<Frame>
  <img alt="Generate incident summary in Slack" src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/ai/inc-sum-1.webp?fit=max&auto=format&n=R81sNIO9rI160XHL&q=85&s=120f42e09ca803d61eb6ced4d601e0a5" width="890" height="556" data-path="images/ai/inc-sum-1.webp" />
</Frame>

## What’s Included in the Summary

The generated summary is designed to capture the most important incident details in plain language. Depending on what information is available, the summary may include the incident problem, customer impact, trigger or cause, steps taken to mitigate or resolve the issue, and the people involved along with their roles.

When configured, the summary may also include an automatically appended attributes list, such as meeting links, severity, affected environments and services, and selected custom form field values.

## How It Works

Rootly AI generates the summary by analyzing the incident’s current context. This may include incident attributes such as severity, environments, services, labels, and incident types, along with form field selections, action items, timeline events, and alert data.

If permitted by your privacy settings, Rootly AI may also incorporate relevant Slack channel messages and meeting transcripts to improve summary quality and completeness. For best results, configure **Slack channel message visibility** to **All messages** or **All messages in Public + pinned in Private**.

If there is not enough information available to produce a meaningful summary, Rootly will indicate that additional incident context is required.

## Configuration

Incident Summarization is available to all customers but must be explicitly enabled.

To enable this feature, navigate to **Rootly AI** and toggle on **Enable Rootly AI**. Only Admins can enable Rootly AI features. Ensure that **Incident summarization** is enabled.

To ensure the best results, configure **Slack channel message visibility** to **All messages** or **All messages in Public + pinned in Private**. This allows Rootly AI to access sufficient context from Slack communications when generating summaries. These settings can be updated at any time from **Rootly AI** configuration.

<Frame>
  <img alt="Rootly AI incident summarization configuration" src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/ai/inc-sum-2.webp?fit=max&auto=format&n=R81sNIO9rI160XHL&q=85&s=de70a0e6465105f51cb8dc41fd024a6a" width="1507" height="1964" data-path="images/ai/inc-sum-2.webp" />
</Frame>

<Note>
  Incident summarization in private incidents depends on your Slack channel message visibility settings. For private incidents, AI features are available only when your channel history scope includes private messages.
</Note>

## Best Practices

<AccordionGroup>
  <Accordion title="Generate early, regenerate often" icon="rotate">
    Generate an initial summary when the incident starts, then regenerate it as more details emerge. As timeline events, alerts, and resolution steps are added, the summary becomes more accurate and useful.
  </Accordion>

  <Accordion title="Include sufficient incident context" icon="list-check">
    Timeline events, action items, alerts, and relevant Slack communications significantly improve summary quality. Providing clear and complete context helps Rootly AI produce more accurate summaries.
  </Accordion>

  <Accordion title="Use summaries for responder catchup" icon="users">
    The `/rootly catchup` command uses the same summarization technology to help new responders quickly understand long-running incidents without needing to read the full incident history.
  </Accordion>
</AccordionGroup>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Why can’t Rootly AI generate a summary?" icon="circle-question">
    If you see a message indicating that *“The incident report does not provide enough information to summarize”*, add more context such as an incident summary or description, associated alerts, timeline updates, or action items and try again. In private incidents, confirm that Slack channel message visibility settings allow AI access.
  </Accordion>

  <Accordion title="Why is the summary missing important details?" icon="circle-exclamation">
    The summary can only include information that exists in the incident context at the time it is generated. Add or update key incident details such as impact, mitigation steps, resolution notes, or relevant timeline events, then regenerate the summary. If Slack messages or meeting transcripts are expected to be included, confirm that privacy settings permit their use.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).