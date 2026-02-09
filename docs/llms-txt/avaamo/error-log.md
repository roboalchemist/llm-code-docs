# Source: https://docs.avaamo.com/user-guide/debug/error-log.md

# Error Log

You can view all the error details that occurred during the execution of responses from the agent. This section helps developers to monitor, filter, and analyze error logs effectively.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F9ZpwqBgNZJ629Nurpqnz%2Fimage.png?alt=media&#x26;token=2e434270-8ac8-4ef0-80a4-885c148a8745" alt=""><figcaption></figcaption></figure>

#### **Histogram**

* This graph provides a **visual representation of errors over time**, allowing you to spot patterns or spikes quickly.
* **X-axis:** Displays the dates within the selected range.
* **Y-axis:** Shows the count of errors recorded on each date.

#### **Filter Error logs**&#x20;

**By type:**

Use the filter dropdown to view only **Errors** or only **Warnings**. Select the required option from the dropdown to apply the filter.

**By skill type**

Use the **Skill type** filter to view JS errors for a specific skill. Select a skill from the dropdown (which lists all skills associated with the agent) to narrow down the error list.

**By date:**

Use the date filter to view Error logs within a specific date range (up to 90 days). By default, the page shows errors from the last 30 days.

Click the date picker and choose one of the preset ranges, Last 30 days, Previous 15 days, or Today, or select **Custom Range**. For a custom range, pick a start date, drag to the end date, and click **Apply**.

#### **Search JS error logs**

Use the **Search** option to find error logs by entering a **conversation\_uuid** or **conversation\_session\_ID**. This helps you quickly locate specific conversations and troubleshoot issues more efficiently.

#### **Log Table**

This table lists the individual error entries in detail. The main columns include:

* **Type:** Specifies the type of error.
* **Skill:** Identifies the skill associated with the error.
* **Conversation UUID:** A unique identifier for the conversation.
* **Conversation Session ID:** Unique identifier assigned to each conversation session between a user and an agent.
* **Timestamp:** Indicates the exact date and time when the error occurred.
* **Actions:** Provides options to interact with each log entry. Click `View` to see details.

### Key features

The error logging system provides a streamlined way to detect, analyze, and resolve issues across your application. Here's how each feature helps improve visibility and troubleshooting:

**Unified Error Log**\
Instead of checking multiple sources, you get a single view that consolidates all API and JavaScript errors. This makes it easier to troubleshoot issues without switching between tools or logs.

**Proactive Alerts**\
You don’t have to wait for users to report problems. The system can alert you in real time when issues arise, such as a sudden latency spike or a runtime error, so you can respond quickly.

**Deep Insights**\
Each error entry includes detailed metadata, such as the error type, the skill or component involved, and the exact time it occurred. This helps you understand what went wrong and when. You can also export logs for later review or share them with your team.

**Integrated Debugger**\
Troubleshooting is faster when everything you need is in one place. The built-in debugger lets you dig into errors directly from the log view, helping you trace the cause and test solutions without switching environments.
