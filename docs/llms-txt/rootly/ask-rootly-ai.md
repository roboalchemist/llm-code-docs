# Source: https://docs.rootly.com/ai/ask-rootly-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ask Rootly AI

> Interactive AI assistants that help answer questions about the current incident in Slack or analyze incident history and metrics in the web application.

## Overview

Ask Rootly AI provides two complementary AI assistants designed to support responders during incidents and after the fact.

* **Slack Copilot** helps responders ask questions about the *current incident* directly within an incident Slack channel.
* **Web Copilot** enables deeper analysis across *incident history and metrics* in the Rootly web application.

Together, these tools help teams quickly understand what’s happening, communicate clearly, and analyze trends—without replacing human decision-making.

***

## Slack Copilot (Ask Rootly AI in Slack)

Slack Copilot is designed for real-time collaboration during an active incident. By mentioning `@rootly` in a thread within an incident Slack channel, responders can ask questions and receive concise, contextual answers based on the current incident.

**Via Slack in an incident channel: mention `@rootly` in a thread**

<Frame>
  <img alt="Ask Rootly AI in Slack" src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/ai/rootly-ai-2.gif?s=bad189a049040b80c43d28a5c17700f7" width="600" height="259" data-path="images/ai/rootly-ai-2.gif" />
</Frame>

### What Slack Copilot Can Help With

Slack Copilot focuses exclusively on the *current incident* and can:

* Answer questions about what has happened so far
* Identify roles such as the incident commander
* Summarize actions taken and decisions made
* Help draft internal or external communications
* Provide general incident response guidance

Example prompts include:

* What happened?
* What caused the incident?
* Who is the commander?
* What have we tried so far?
* What should I do next?
* Write a customer-facing summary of this incident

Responses are intentionally concise to support fast decision-making.

### Limitations

Slack Copilot cannot:

* Answer questions about historical incidents
* Modify incident properties
* Access data outside the current incident

<Note>
  Slack Copilot is restricted to answering questions about the current incident and general incident management practices.
</Note>

***

## Web Copilot (AI Copilot in the Web Application)

Web Copilot is designed for broader analysis beyond a single incident. It allows users to ask questions across their entire incident history and analyze trends and performance metrics.

**Via the web application: open the AI Copilot interface**

<Frame>
  <img alt="Ask Rootly AI on the web" src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/ai/rootly-ai-1.webp?fit=max&auto=format&n=R81sNIO9rI160XHL&q=85&s=c2f44c35ae83134613e1d76cb16715ad" width="1417" height="894" data-path="images/ai/rootly-ai-1.webp" />
</Frame>

### What Web Copilot Can Help With

Web Copilot can:

* Query incident history using filters such as severity, environment, service, or incident type
* Group incidents by attributes like service, severity, or team
* Calculate metrics such as incident count, MTTR, and MTTM
* Create charts and visualizations
* Answer questions about trends and patterns over time

Example prompts include:

* How many incidents occurred last month?
* What is our average time to resolution for severity 1 incidents?
* Show incidents grouped by service
* Create a chart of incidents over the last quarter

Web Copilot maintains conversation context and is suited for analysis, reporting, and operational insights.

***

## Configuration

Ask Rootly AI features are available to all customers but must be explicitly enabled.

To enable these features, navigate to **Rootly AI** and toggle on **Enable Rootly AI**. Only Admins can configure Rootly AI settings.

Then enable the relevant assistants:

* **Ask Rootly AI** — enables Slack Copilot
* **Rootly AI Copilot** — enables Web Copilot

For best results with Slack Copilot, configure **Slack channel message visibility** to **All messages** or **All messages in Public + pinned in Private**. This allows Rootly AI to access sufficient context when answering questions.

<Frame>
  <img alt="Rootly AI configuration" src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/ai/rootly-ai-3.webp?fit=max&auto=format&n=R81sNIO9rI160XHL&q=85&s=bcdaf7f4f8bd6d94a03c831511fbbfe6" width="1466" height="1923" data-path="images/ai/rootly-ai-3.webp" />
</Frame>

<Note>
  Availability in private incidents depends on your Slack channel message visibility settings. For private incidents, AI features are available only when your channel history scope includes private messages.
</Note>

***

## Troubleshooting

<AccordionGroup>
  <Accordion title="Slack Copilot is not responding" icon="circle-question">
    Ensure **Ask Rootly AI** is enabled in Rootly AI settings. Verify that you are in an incident Slack channel and mentioning `@rootly` within a thread. For private incidents, confirm that Slack channel message visibility settings allow AI access.
  </Accordion>

  <Accordion title="Web Copilot is not available" icon="circle-exclamation">
    Ensure **Rootly AI Copilot** is enabled in Rootly AI settings and that you have access to the Rootly web application.
  </Accordion>

  <Accordion title="Slack Copilot says it can only answer about the current incident" icon="info">
    This is expected behavior. Slack Copilot is intentionally scoped to the current incident only. Use Web Copilot for questions about historical incidents or aggregated metrics.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).