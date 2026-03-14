# Source: https://plivo.com/docs/aiagent/reports/customermetrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Customer Metrics

> It provides a overview of how customers engage with your support channels

The **Customer Metrics** report gives you a high-level view of how customers are experiencing conversations with your AI agents and human teams. This report helps you assess responsiveness, satisfaction, and conversation quality across all channels—Call, WhatsApp, and Chat—over a selected time period.

Use this report to identify friction in response times, dropped conversations, or issues with resolution quality. It’s especially useful for tracking SLAs, support efficiency, and areas for automation improvement.

## Metrics in this Report

### **1. Average Response Time**

At a glance, see how long your team or AI agent takes to respond to customers. This metric reflects the tie to first response, and is displayed agent as a numeric value (in minutes and seconds) and over time as a bar graph segmented by channel.

### **2. Unanswered Rate**

This shows the percentage of customer-initiated conversations that didn’t receive a response. You’ll see the rate as a percentage, and a corresponding line graph tracking changes over time, helping you spot if customers are being ignored during peak hours.

### **3. Abandoned Rate**

Measures how often customers drop off before any meaningful interaction begins. Shown as a **percentage metric** and a timeline graph, this helps identify when your system might be too slow or unengaging.

### **4. Conversations Under 5 Minutes**

Tracks the number of conversations that lasted less than five minutes, typically indicating either fast resolutions or disengaged users. You’ll see the raw count displayed alongside a visual trend over time.

### **5. Average CSAT (Customer Satisfaction Score)**

If CSAT collection is enabled, this shows the **average rating** customers gave at the end of their conversations. It reflects qualitative sentiment and is displayed as a numeric score (e.g., 4.5 / 5). If not enough data is available, you’ll see “No Data.”

## Charts on this Report

All charts in this report automatically display data for the last 6 months if no specific time range is selected. The time breakdown of each chart—such as daily, weekly, or monthly—is controlled by the "Group data by" filter. Charts dynamically update based on the applied filters (e.g., channel, direction, CSAT score), ensuring that the visualizations reflect only the relevant subset of data.

* **Average Response Time (Bar Graph)**\
  Compare response speed across Call, WhatsApp, and Chat on a period basis.
* **Average Unanswered Wait Time (Dot Plot)**\
  Shows how long users typically waited before abandoning the session.
* **Transfer Rate (Line Graph)**\
  Tracks how often conversations are transferred to another agent or queue.
* **Unanswered Rate (Line + Cumulative Graph)**\
  Shows how the unanswered rate changes over time, with a cumulative trend.
* **Abandoned Rate (Timeline Graph)**\
  Highlights trends in drop-off behavior before response.
* **Conversations by Disposition (Stacked Bar Chart)**\
  Categorizes conversations by final state—e.g., completed, abandoned, short, etc.
* **Conversations per Direction (Bar Chart)**\
  Shows the count of inbound vs. outbound conversations per day.
* **Conversation Time Buckets (Grouped Bar Chart)**\
  Segments all conversations by their duration: 0 min, \<1 min, \<5 min, >5 min.

## Filter Options

At the top of the report, you can customize your view using the following filters:

* **Date Range**: View data from a predefined window (e.g., last 7 days) or select custom start and end dates.
* **Group Data By**: Choose how to group results—Hourly, Daily, Weekly, or Monthly.
* **Channel**: Filter by the channel through which the conversation happened (e.g., Call, WhatsApp, Chat).
* **Direction**: Choose to view inbound or outbound conversations.

## Export Options

Each graph in this report supports export options:

* **CSV**: Download the underlying data as a comma-separated file.
* **XLSX**: Export data in Excel spreadsheet format.
* **Image**: Save the current graph view as a PNG snapshot.

***

This report is ideal for CX leads, support managers, or automation strategists who want a clear picture of customer responsiveness. It also helps identify if your AI agents are improving service levels or if human escalation is happening too often.
