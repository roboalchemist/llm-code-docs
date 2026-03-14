# Source: https://plivo.com/docs/aiagent/reports/operations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Operations Overview

> It provides a detailed breakdown of inbound and outbound conversation outcomes

The **Operations Overview report** gives you a real-time and historical breakdown of how conversations are being executed at a system level—across inbound and outbound flows. This report highlights delivery issues, unanswered scenarios, timeouts, and detailed disposition outcomes across your support operation.

Use this report to monitor service reliability, troubleshoot dropped or failed conversations, and assess how well your operational flows are functioning across channels and directions.

## Metrics in this Report

### **Inbound Metrics**

* **Total Inbound Conversations**\
  Count of all inbound interactions.
* **Answered**\
  Number of conversations answered by an agent or AI.
* **Unanswered**\
  Count of conversations where no response was provided.
* **Abandoned**\
  Conversations dropped before handling.
* **Self Resolved**\
  Conversations handled entirely by automation without human involvement.

### **Outbound Metrics**

* **Total Outbound Conversations**\
  Number of outbound contacts initiated.
* **Answered / Unanswered / Failed**\
  Breakdown of successful and failed connections.

### **Callback Requested**

Count of users who requested a callback during or after a conversation.

### **Inbound Unanswered Reasons**

* **Queue Time Out**: The user waited too long in queue.
* **Agent Assignment Failed**: No agent could be assigned.
* **Customer Disconnected**: Caller dropped before connection.

### **Inbound Abandoned Reasons**

* **Out of Business Hour**: Incoming call occurred outside scheduled hours.
* **Enqueue Failed**: System failed to place user in the queue.

## Charts in this Report

Charts automatically load **6 months of data** if no time range is selected. The **"Group data by"** filter determines the time resolution (e.g., monthly, weekly). All charts reflect current filter settings.

* **Abandoned Rate**
  Shows the percentage of conversations that were dropped by users before reaching a response.
* **Unanswered Rate**
  Tracks the percentage of conversations where no reply was given by the agent or AI.
* **Average Handle Time**
  Displays the average duration spent actively handling conversations.
* **Average Wrap-up Time**
  Shows how long agents took to complete post-conversation work.
* **Conversations per Disposition**
  Bar chart showing final outcomes (e.g., Auto-closed, Negotiation Completed), helping you assess resolution trends.

## Conversation Details Table

This table provides a row-by-row view of every conversation within the filtered date range:

* **Conversation ID, Contact Name, Channel, Direction**
* **Disposition & Sub-Dispositions**
* **Agent Name**
* **Timestamps (Start and End)**
* **Conversation Status (e.g., Failed, Unanswered, Self Resolved)**

Use this section to audit specific records, troubleshoot anomalies, or extract granular operational data.

## Filters

You can refine the report using the following filters:

* **Channel**: Filter data by Call, Chat, WhatsApp, or other conversation channels.
* **Direction**: Choose Inbound, Outbound, or both.
* **Time Period**: Select a predefined range (like Last 7 days) or set a custom date.

## Export Options

Each graph in this report supports export options:

* **CSV**: Download the underlying data as a comma-separated file.
* **XLSX**: Export data in Excel spreadsheet format.
* **Image**: Save the current graph view as a PNG snapshot.
