# Source: https://docs.axonius.com/docs/system-lifecycle-and-discovery-log-charts-2.md

# System Lifecycle and Discovery Log Charts

The **System Lifecycle** chart shows information about the Discovery Cycle that is currently running, or the last **discovery cycle**, if a cycle is not currently running.

The **Discovery Log** chart shows the last five  Discovery Cycles. The most recent  Discovery Cycle appears first in the list.

## System Lifecycle Chart

<Image alt="SystemLifeCycleChartUp" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SystemLifeCycleChartUp.png" />

The **System Lifecycle** chart displays the progress of the discovery cycle and the current phase in the cycle.

During a Discovery Cycle, in the Fetch Assets and in the Fetch Scanner Assets discovery phases hover over the chart to display the fetch status for each adapter that is pending.
The System Lifecycle chart also displays information regarding:

* The number of hours until the next automatic discovery cycle starts.
* The last discovery cycle's start and end timestamps.
* The duration of the cycle.
* The time the next cycle is due to start.

For more details, see [Discovery Cycle](/docs/discovery-cycle).

<Image alt="InspectLogs" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/InspectLogs.png" />

From the **Inspect Logs** list you can:

* Click **Adapters Fetch History** to open the **Adapters Fetch History** page filtered by this **Discovery Cycle** and see detailed information about the fetch status of each adapter being fetched by Axonius. To learn more, see [Adapters Fetch History](/docs/adapters-fetch-history).

* Click **Activity Log** to open the **Activity Logs** page filtered by this **Discovery Cycle** and see detailed information about the events in this **Discovery Cycle**. To learn more, see [Activity Logs Page](/docs/activity-logs-page).

* Click **Enforcement Run History** to open the Enforcement Run History page filtered by this **Discovery Cycle** and see detailed information about the events in this **Discovery Cycle**. To learn more, see [Viewing Enforcement Set Run History](/docs/view-ec-set-history).

## Discovery Log Chart

The **Discovery Log** chart shows the last five Discovery Cycles.

<Image alt="DiscoveryLogChart-Dates.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DiscoveryLogChart-Dates.png" />

Click the arrow next to any of the Discovery Cycles to see all of the phases of that cycle.

<Image alt="DiscoveryLogChart-Dates-Open.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DiscoveryLogChart-Dates-Open.png" />

You can see detailed information about when the stage started, when it ended, and how long it took. To investigate a stage, click any three-dot menu to the right and then **[Activity Log](/docs/activity-logs-page)**, **[Adapter Fetch History](/docs/adapters-fetch-history)**, or **[Enforcment Run History](/docs/view-ec-set-history)** to open those pages filtered by the cycle.

<Image alt="DiscoveryLogChart-Dates-Links.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DiscoveryLogChart-Dates-Links.png" />

* **Adapter Fetch History** is only relevant for steps that involve **Adapter Fetch**.

<br />