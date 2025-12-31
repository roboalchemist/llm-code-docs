# Source: https://docs.avaamo.com/user-guide/debug/error-log.md

# Error Log

You can view all the error details that occurred during the execution of responses from the agent. This section helps developers to monitor, filter, and analyze error logs effectively.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FT4NbN6IFYwzP07Vv2VBB%2FScreenshot%202025-04-03%20at%201.14.57%E2%80%AFPM.png?alt=media&#x26;token=82887425-f48f-47fc-a240-315b46a71b27" alt=""><figcaption></figcaption></figure>

**Histogram**

* This graph provides a **visual representation of errors over time**, allowing you to quickly spot patterns or spikes.
* **X-axis:** Displays the dates within the selected range.
* **Y-axis:** Shows the count of errors recorded on each date.

**Log Table**

This table lists the individual error entries in detail. The main columns include:

* **Type:** Specifies the type of error.
* **Skill:** Identifies the skill associated with the error.
* **Timestamp:** Indicates the exact date and time when the error occurred.
* **Actions:** Provides options to interact with each log entry.

### Key features

The error logging system provides a streamlined way to detect, analyze, and resolve issues across your application. Here's how each feature helps improve visibility and troubleshooting:

**Unified Error Log**\
Instead of checking multiple sources, you get a single view that consolidates all API and JavaScript errors. This makes it easier to track down problems without switching between tools or logs.

**Proactive Alerts**\
You don’t have to wait for users to report problems. The system can alert you in real time when something goes wrong, like a sudden increase in latency or a runtime error, so you can respond quickly.

**Deep Insights**\
Each error entry includes detailed metadata, such as the type of error, the skill or component involved, and the exact time it occurred. This helps you understand what went wrong and when. You can also export logs to review them later or share them with your team.

**Integrated Debugger**\
Troubleshooting is faster when everything you need is in one place. The built-in debugger lets you dig into errors directly from the log view, helping you trace the cause and test solutions without switching environments.
