# Source: https://docs.agent.ai/guides/using-agent-ai/connect-your-calendar.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Calendar Connections & Data Usage

> This document explains how calendar connections work in Agent.ai, what data is accessed, and how that data is used and protected.

## How to Connect Your Calendar

You can connect your calendar in two ways:

### Option 1: From the Connections Page

1. Navigate to the [**Connections**](https://agent.ai/user/connections#configure-meeting-agents) page.
2. Find the calendar section.
3. Click **Connect**.
4. You’ll be redirected to a Composio authorization screen.
5. Choose the calendar account you want to connect.
6. Review the requested permissions and approve access.
7. You’ll be redirected back to [Agent.ai](http://Agent.ai) and your calendar will be connected.

### Option 2: During Agent Setup

1. Run either the **Meeting Prep** or **Meeting Follow-up** agent.
2. If your calendar isn’t connected yet, you’ll be prompted to do so as part of the setup flow.
3. Follow the on-screen steps to authorize access via Composio.

## How to Disconnect Your Calendar or Revoke Access

You can disconnect your calendar at any time using either of the methods below.

### Option 1: From the Connections Page

1. Go to the [**Connections**](https://agent.ai/user/connections#configure-meeting-agents) page.
2. Locate your connected calendar.
3. Click **Disconnect**.

### Option 2: From the Agent Page

1. Open the **Meeting Prep** or **Meeting Follow-up** agent.
2. Click the **settings icon** in the top-right corner of the agent page.
3. Select **Disconnect calendar**.

Once disconnected, agents will no longer be able to access your calendar data.

## What is Composio?

[Agent.ai](http://Agent.ai) uses **Composio** to securely connect your calendar to agents.

Composio is a trusted integration layer that allows you to authorize third‑party tools (like calendars) without sharing your login credentials directly with [Agent.ai](http://Agent.ai). You’ll see Composio referenced during the connection flow because it handles authentication and permission management on your behalf.

## What Information We Access When You Connect Your Calendar

### Meeting Information We Collect

Agents may access the same information that any meeting invitee can see, including:

* Meeting title
* Meeting description
* Location (meeting link or physical address)
* Duration and timing details
* Any other information visible to meeting invitees

This access is limited to what’s required for the agent’s functionality.

## What We **Don’t** Access

We do **not** access:

* Content from other apps or services
* Calendar data beyond what’s needed for agent functionality
* Historical events outside the relevant time window for your agent
* Personal information not directly related to calendar events

## How We Use Your Data

* Meeting data is used **exclusively** to power agent outputs (such as summaries or follow‑ups).
* We do **not** train AI models on your calendar data.
* We do **not** sell or share this data with third parties.
* Data is stored for **5 years** under our current retention policy, unless deleted sooner upon request.

## Your Data Rights

You’re always in control of your data.

* You can request deletion of your data at any time.
* Upon request, we’ll permanently remove all meeting recordings, transcriptions, and associated data.
* To initiate a data deletion request, contact our support team at [support@agent.ai](mailto:support@agent.ai).

We take data privacy seriously and are committed to handling your information responsibly and transparently.
