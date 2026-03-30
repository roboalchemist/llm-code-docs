# Source: https://www.inngest.com/docs-markdown/platform/monitor/traces

# Traces

Every Inngest function run is automatically traced with no configuration required. Traces are available in both the [DevServer](/docs-markdown/dev-server) and the Inngest Cloud dashboard, giving you a complete picture of what happened during a function execution, including step timing, queue delays, HTTP connection phases, retry attempts, and input/output data.

## Trace View

### Layout

The trace view is a two-panel layout with a resizable divider:

- **Left panel:** Run info header and an interactive timeline of execution bars
- **Right panel:** Contextual details for the selected step or the run itself

Drag the divider between panels to adjust the split to your preference.

![Trace view showing the two-panel layout with timeline bars on the left and step details on the right](/assets/docs-markdown/platform/monitor/traces/trace-overview.webp)

### Run Info

The header at the top of the left panel displays key information about the function run:

- **Function name** with navigation breadcrumbs (App > Function > Run)
- **Run ID**
- **App** and **Function** links
- **Duration:** total time from queued to ended
- **Queued at**, **Started at**, and **Ended at** timestamps
- **AI indicator:** shown when the function uses `step.ai` methods

Actions in the header include **Rerun**, **Cancel** (for in-progress runs), and **Invoke** to re-invoke the function.

## Timeline

The timeline is a waterfall visualization where each bar represents a span in the function execution. Bars are positioned proportionally to their start time and duration relative to the total run. A thin horizontal center line connects the timeline, and time markers at the top show the relative position (0%, 25%, 50%, 75%, 100%).

### Timeline Bars

Each bar in the timeline shows the span name and an icon on the left, its duration on the right, and a colored bar representing its position and length in time.

**Bar types:**

Bar
Description
Visual Style

Run
The top-level function execution
Status-colored solid bar

step.run
A step.run() execution
Status-colored solid bar

step.sleep
A step.sleep() pause
Gray solid bar

step.waitForEvent
A step.waitForEvent() wait
Gray solid bar

step.invoke
A step.invoke() call to another function
Gray solid bar

Inngest
Queue/scheduling delay
Short gray bar

Your server
Server-side execution time
Tall bar with diagonal stripe pattern

Connecting
Connection phase
Dotted outline

Finalization
Post-execution cleanup and state persistence
Short status-colored bar

Extended traces: sub-bars from custom OpenTelemetry spans (see Extended Traces)

Userland span
Custom OpenTelemetry span from your code, nested under "Your server"
Blue solid bar

**Status colors** apply to the run bar and step execution bars:

- Green: Completed successfully
- Red: Failed
- Gray: Cancelled

When a step has both queue delay and execution time, its bar displays as a **compound bar**: a short gray segment (queue delay) immediately followed by a status-colored segment (execution time). This lets you see at a glance how much time was spent waiting vs. executing.

![Timeline bars showing different bar types and styles](/assets/docs-markdown/platform/monitor/traces/bar-styles.webp)

Hovering over any bar shows a tooltip with:

- **Duration:** how long the span took
- **Delay:** queue delay before execution started (when applicable)
- **Start** and **End:** precise timestamps down to milliseconds

### Timing Breakdown

Click the expand arrow on any step bar to reveal how time was spent:

1. **Inngest:** Time in Inngest's queue before your server received the request. Displayed as a short gray bar with a gear icon.
2. **Your server** *(or your organization name)*: Time your server spent executing the step. Displayed as a tall bar with a diagonal stripe pattern and a building icon.

![Timing breakdown showing Inngest queue delay and server execution](/assets/docs-markdown/platform/monitor/traces/timing-breakdown.webp)

This breakdown helps you quickly identify whether latency is caused by queue congestion (Inngest bar) or your application code (server bar).

### Timeline Zoom

For long-running functions with short individual steps, use the **time brush** in the timeline header to zoom into a specific time range:

- **Drag the handles** on either end to narrow the visible window
- **Drag the selected region** to pan across the timeline
- **Click outside the selection** to expand it
- **Click the reset button** to return to the full view (0%–100%)

Time markers update dynamically as you zoom, and all bars rescale to fill the visible window.

![Timeline zoom with the time brush focused on a specific range](/assets/docs-markdown/platform/monitor/traces/timeline-zoom.gif)

## Details Panel

The right panel shows contextual information about whichever item is selected in the timeline. Click a step bar to see step details, or click the root bar to see run-level details.

### Step Details

Selecting a step bar opens the step details panel with:

**Header:**

- Step name with a collapsible section toggle
- **Attempt badge:** shows "Attempt N" when the step has been retried (highlighted in the step's status color)
- **Rerun from step** button: re-execute the function starting from this step

**Timing:**

- **Queued at**, **Started at**, **Ended at:** precise timestamps
- **Delay:** how long the step waited in the queue
- **Duration:** total execution time
- **Step type:** displayed as a code badge (e.g., `step.run`, `step.invoke`)

**Step-type-specific fields:**

| Step Type            | Fields Shown                                                                                   |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| `step.invoke`        | Function ID, triggering event ID, triggered run ID, timeout, timed out status, return event ID |
| `step.sleep`         | Sleep until datetime                                                                           |
| `step.waitForEvent`  | Event name, match expression, timeout, timed out status, matched event ID                      |
| `step.waitForSignal` | Signal name, timeout, timed out status                                                         |

**Tabs** (shown below the timing section):

- **Input:** The step's input data as formatted JSON
- **Output:** The step's return value as formatted JSON
- **Error details:** Error message and body (shown when the step failed, auto-selected as default tab)
- **Headers:** Response headers returned by your SDK endpoint
- **Metadata:** Structured key-value tables for span metadata (custom metadata, AI metadata, warnings)

![Step details panel showing timing info, step-specific fields, and I/O tabs](/assets/docs-markdown/platform/monitor/traces/step-detail.webp)

For a `step.invoke`, the details panel also shows the invoked function, triggering event ID, triggered run ID, timeout, and return event ID:

![Step details panel for a step.invoke showing invoke-specific fields](/assets/docs-markdown/platform/monitor/traces/step-detail-invoke.webp)

### Run Details

Selecting the root bar (or when no step is selected) shows the run details panel:

**Trigger information** (varies by trigger type):

| Trigger Type | Fields Shown                                     |
| ------------ | ------------------------------------------------ |
| **Event**    | Event name, event ID, received at timestamp      |
| **Cron**     | Cron expression, cron ID, triggered at timestamp |
| **Batch**    | Event name, batch ID, received at timestamp      |

**Actions:**

- **Invoke** button: re-invoke the function with a custom payload

**Tabs:**

- **Input:** The triggering event payload as formatted JSON (includes a "Send to Dev Server" action in DevServer mode)
- **Output:** The function's return value
- **Error details:** Error message and body (when the run failed)
- **Metadata:** Run-level span metadata

![Run details panel showing trigger information and event payload](/assets/docs-markdown/platform/monitor/traces/run-detail.webp)

### Retry Attempts

When a step fails and is retried, the step details panel shows an **attempt badge** next to the step name (e.g., "Attempt 2"). The badge is colored to match the step's status: red for a failed attempt, green for a successful retry.

Each retry attempt is a separate span in the timeline, so you can compare timing and output across attempts to understand what changed between retries.

## Extended Traces&#x20;

Extended Traces bring [OpenTelemetry](https://opentelemetry.io/)-powered distributed tracing to your Inngest functions, capturing visibility beyond Inngest's built-in steps, including external API calls, database queries, and third-party service interactions.

### What's Included

When you enable Extended Traces, Inngest automatically instruments your functions to capture:

- **External service calls:** HTTP requests, database queries, and third-party API interactions
- **Performance bottlenecks:** Identify slow operations across your entire execution path
- **Distributed context:** Full trace propagation across your stack

### How They Appear

Extended trace spans appear as child bars in the timeline, nested under your server's execution. These spans are visually distinct and labeled with the operation they represent.

Clicking an extended trace span shows the **Attributes** tab in the details panel with:

- **Span name** and **kind** (client, server, internal, etc.)
- **Service name**
- **OpenTelemetry attributes:** all span attributes displayed as key-value pairs (internal Inngest attributes are filtered out)

![Extended traces showing userland spans nested in the timeline with the attributes panel open](/assets/docs-markdown/platform/monitor/traces/extended-traces.webp)

> **Note:** Extended Traces automatically capture spans from popular libraries including HTTP clients, database drivers, and more. See the full list of automatic instrumentation.

### Get Started

Extended Traces are available in TypeScript as an opt-in feature. Get started in a few minutes by configuring the Extended Traces middleware.

[Get started with Extended Traces]("/docs-markdown/reference/typescript/extended-traces")