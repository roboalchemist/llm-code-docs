# Source: https://docs.rootly.com/metrics/customized-dashboards.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Customizing Dashboards

> Create and refine metric panels, apply filters and groupings, compare datasets, and export dashboards for tailored analytics across incidents and on-call operations.

Dashboards are meant to evolve.

As your organization’s incident response matures, the questions you ask will change—from **“How many incidents did we have?”** to **“Which teams are improving fastest?”** to **“Are we reducing time-to-mitigate for SEV0s in production?”**

This page walks through how to customize dashboards in Rootly—from building panels and applying advanced filters, to segmenting results, exporting data, and understanding how caching and permissions impact what you see.

***

# How metric panels work

A **panel** is the building block of every dashboard. Panels can be visual (charts), tabular (tables), or KPI-style (aggregate values). Every panel is defined by a combination of:

* **Display type** (how the data appears)
* **Collection** (what records the panel pulls from)
* **Filters** (which subset of data is included)
* **Aggregation operation** (how results are calculated)
* **Metric key** (what you’re measuring)
* **Grouping** (how results are segmented across categories)
* **One or more datasets** (for comparisons and multi-series charts)

Panels are intentionally modular. Instead of forcing you into rigid metric templates, Rootly separates how data is selected (collection + filters), how it is calculated (operation + key), and how it is displayed (panel type + grouping).

This separation makes dashboards composable. You can reuse the same dataset across different visualizations, compare variations of a metric side-by-side, or refine filters without redesigning the entire dashboard.

<Callout icon="sparkles" color="#7748F6">
  **Think in questions, not charts**

  A good panel starts with a question—then you pick the collection, filters, and metric that answer it. The chart type is the final step, not the first.
</Callout>

***

# Panel types

Rootly supports the following panel types:

* **Line chart**
* **Line stepped chart**
* **Column chart**
* **Stacked column chart**
* **Monitoring chart**
* **Pie chart**
* **Table**
* **Aggregate value**

Each panel type serves a different analytical purpose.

* **Line-based charts** are best for trend analysis.
* **Column charts** emphasize volume comparison.
* **Stacked columns** show composition within totals.
* **Pie charts** surface proportional distribution.
* **Tables** support operational review.
* **Aggregate values** highlight KPIs.

Choosing the right panel type is less about aesthetics and more about cognitive clarity. If the question is about trend, use time-based charts. If it’s about composition, use stacked visualizations. If it’s about accountability, use grouping.

<Callout icon="monitor-waveform" color="#FFFFFF">
  **Monitoring chart**

  Monitoring charts are optimized for time-series monitoring-style data visualization, but still use the same panel configuration model (datasets, filters, group-by, and export).
</Callout>

***

# Collections and access

Panels pull data from a **collection**. Which collections are available depends on your product access (seat type):

* **Alerts**
* **Incidents**
* **Retrospectives**
* **Action Items**
* **Users**

<Callout icon="id-badge" color="#FFC107">
  **Collections are seat-based**

  If you only have an **On-Call** seat, you’ll typically see **Alerts** collections. If you have an **Incident Response** seat, you’ll see additional collections such as **Incidents**, **Retrospectives**, **Action Items**, and **Users**.
</Callout>

***

# Add a metric panel

To add a panel:

1. Go to **Metrics** and open the dashboard you want to edit
2. Click **+ Add Panel**
3. Configure the panel (type, collection, filters, operation, key, etc.)
4. Click **Create**

***

## Example: Number of incidents (production-impacting)

<Callout icon="chart-column" color="#7748F6">
  **Example panel configuration**

  | Field       | Value                                                         |
  | :---------- | :------------------------------------------------------------ |
  | Title       | # of Incidents                                                |
  | Description | Count of production incidents across standard incident kinds. |
  | Type        | Aggregate value                                               |
  | Collection  | Incidents                                                     |
  | Filter by   | Kind = Normal, Kind = Normal sub, Kind = Backfilled           |
  | Operation   | Count                                                         |
  | Key         | Results                                                       |
</Callout>

***

# Edit panels

To edit a panel:

1. Open the dashboard in **Metrics**
2. Hover over the panel
3. Click **⋯**
4. Select **Settings**
5. Update configuration and click **Update**

<Callout icon="circle-check" color="#FFFFFF">
  **Validation happens on save**

  Rootly validates your configuration before saving. If you select an invalid key, operation, or filter condition, you’ll see a targeted error message so you can correct it immediately.
</Callout>

***

# Move and resize panels

Dashboards use a grid-based layout.

* Drag a panel to move it
* Drag the corner handle to resize it

Panels are stored as grid coordinates (not pixels), meaning layouts stay consistent across screen sizes.

<Callout icon="grid-2x2" color="#FFC107">
  **Grid defaults**

  Panels default to a grid size of **6 columns wide × 3 rows tall**, with a minimum height enforced for readability.
</Callout>

***

# Filters

Filtering determines *what counts*.

Without intentional filtering, dashboards become noise generators. With thoughtful filtering, they become precision tools.

In Rootly, filtering operates on two layers: global view preferences (personal and temporary) and panel-level filters (persistent and shared). Understanding the difference is critical for designing dashboards that are both flexible and consistent.

* **Dashboard-level filters** (your personal view preferences)
* **Panel-level filters** (saved as part of the panel configuration)

These two layers combine to determine what any panel actually shows.

***

## Dashboard-level filters (view preferences)

Dashboard-level filters apply to **all panels** and are saved **per user**:

* Date range (e.g., Last 30 Days)
* Period (day / week / month / quarter / year)
* Team filters
* Service filters

These are designed for flexible viewing without changing the underlying dashboard for everyone.

<Callout icon="user" color="#7748F6">
  **Your view doesn’t change the dashboard**

  View preferences are personal. Changing your dashboard filters doesn’t edit the dashboard or affect what other viewers see.
</Callout>

***

## Panel-level filters

Panel-level filters are stored with the panel itself and define exactly which records are included in that panel’s dataset.

### Filter conditions (operators)

Depending on the field type, Rootly supports operators like:

* `=` (equals)
* `!=` (not equals)
* `>=` (greater than or equal)
* `<=` (less than or equal)
* `exists` / `not_exists`
* `contains` / `not_contains`
* `assigned` / `unassigned` (incident roles only)

<Callout icon="sliders" color="#FFFFFF">
  **Role-aware filtering**

  Incident roles support `assigned` and `unassigned`, allowing panels like “Incidents missing an Incident Commander” or “SEV0s where Comms Lead is unassigned.”
</Callout>

***

## Filter groups (AND / OR logic)

Filters support grouping logic through **filter groups**.

* **AND** groups require all rules to match
* **OR** groups match if any rule matches

This allows more expressive logic, such as:

* (SEV0 OR SEV1) AND (Environment = Production)
* (Service contains Payments) OR (Functionality contains Checkout)

***

# Group By

**Group By** segments the results inside a panel—turning a single metric into comparative series.

Group By is useful when you want to answer questions like:

* Which teams generate the most incidents?
* Which services have the longest time-to-resolve?
* How do SEV0 counts differ by environment?

Group By:

* Creates multiple series for line/column charts
* Segments pie charts by the grouped field
* Can group by custom fields and incident roles

<Callout icon="diagram-project" color="#FFC107">
  **Group By turns “a metric” into “a comparison”**

  If you’re trying to drive action, group-by is often the difference between a dashboard that reports and a dashboard that informs.
</Callout>

***

# Multiple datasets (comparisons)

Chart panels can include **multiple datasets**.

Each dataset can have:

* A different collection
* Different filters
* Different operations and keys
* A custom series name

This is ideal for side-by-side comparisons, like:

* SEV0 count vs SEV1 count over time
* Time to mitigate vs time to resolve
* Incidents from Team A vs Team B

Multiple datasets are particularly powerful when designing executive dashboards.

Instead of stacking separate panels vertically (which increases scroll depth and visual load), you can combine related signals into a single comparative visualization. This keeps analysis contextual and reduces cognitive switching between panels.

<Callout icon="layer-group" color="#7748F6">
  **One panel, multiple narratives**

  Multiple datasets let you compare signals without building separate panels—keeping the dashboard compact and the analysis aligned.
</Callout>

***

# Cumulative charts

Certain chart types support **cumulative mode**, which displays running totals over time.

Supported chart types:

* Line chart
* Line stepped chart
* Column chart
* Stacked column chart

Cumulative mode is useful for:

* “Incidents year-to-date”
* “Total alerts this quarter”
* “Action items created this month”

***

# Table panels

Table panels display **raw records** rather than aggregated metrics.

They are useful when you want a dashboard that supports both:

* macro analysis (charts and KPIs), and
* direct operational drill-down (lists of incidents, alerts, or action items)

Table panels support:

* Selecting visible columns
* Including custom fields and incident roles as columns
* Exporting full datasets

<Callout icon="table-columns" color="#FFFFFF">
  **Display vs export limits**

  Tables may display up to **100 rows** in the UI for performance, but exports can include the full dataset.
</Callout>

***

# Aggregate value panels

Aggregate panels display a **single formatted number**—ideal for KPI dashboards.

Examples:

* Total incidents (count)
* Average time-to-resolve (average)
* Total hours worked until mitigated (sum)

These panels are best for:

* Exec summaries
* Weekly reliability reviews
* “Top row” dashboard metrics

Because aggregate panels show a single value, they should be used intentionally and sparingly. They are most effective when placed at the top of a dashboard as summary indicators — supported by deeper analytical panels below.

Think of aggregate panels as headlines. The charts beneath them are the supporting evidence.

***

# Operations and keys

## Operations

Operations vary depending on the collection:

* **Count** — available for all collections
* **Average** — commonly available for Alerts and Incidents
* **Sum** — available for Alerts, Incidents, and Users (and depends on the metric key)

<Callout icon="calculator" color="#FFC107">
  **If you don’t see an operation, it’s usually intentional**

  Some collections only support Count because there isn’t a valid numeric metric to average or sum across records.
</Callout>

## Keys (what you're measuring)

Keys are collection-specific and depend on the operation you select.

### Incidents (examples)

* Count: `results`
* Average/Sum: `triage_time`, `detection_time`, `acknowledge_time`, `mitigation_time`, `resolution_time`, `cancellation_time`, `closed_time`

### Alerts (examples)

* Count: `results`
* Average: `acknowledge_time`, `resolution_time`, `time_between_failure`
* Sum: `acknowledge_time`, `resolve_time`

### Users (examples)

* Count: `results`
* Sum: `hours_worked_until_triaged`, `hours_worked_until_mitigated`, `hours_worked_until_resolved`

***

# Time-based behavior

Dashboards apply time filtering automatically based on the selected date range.

Depending on the collection, Rootly uses different timestamps to scope records (for example, incidents and alerts use their `started_at` timestamps). This ensures charts remain consistent when comparing across dashboards and periods.

Time scoping is applied consistently across collections to ensure analytical integrity. This means comparisons between alerts, incidents, and retros remain aligned when viewing the same date range.

If data appears incomplete or unexpectedly low, the first place to check is always your dashboard-level date range.

<Callout icon="clock" color="#7748F6">
  **Time filtering is automatic**

  Most panels inherit the dashboard’s date range and period grouping. If results seem “missing,” check your dashboard-level date range first.
</Callout>

***

# Exporting dashboards and panels

## Export a dashboard

1. Open the dashboard in **Metrics**
2. Click **⋯**
3. Select **Download PDF**

## Export a panel

1. Hover over the panel
2. Click **⋯**
3. Choose an export format

Supported formats:

* **PDF** (all panel types)
* **CSV** (all panel types)
* **JSON** (all panel types)
* **PNG / JPG** (chart panels only)

<Callout icon="image" color="#FFFFFF">
  **Charts only for image export**

  PNG/JPG exports are only available for chart-based panels. Tables and aggregate value panels export via PDF/CSV/JSON instead.
</Callout>

***

# Duplicate a panel

1. Hover the panel
2. Click **⋯**
3. Select **Duplicate**

Duplicated panels:

* Copy all configuration (filters, keys, operations, display type)
* Are renamed to **Copy of `{original title}`**
* Appear in a default grid position (you’ll likely want to reposition it)

***

# Full screen view

Full screen mode is ideal for TVs or wallboards.

1. Open the dashboard
2. Click the full screen icon (top-right)
3. Press **ESC** or click the icon again to exit

Full screen mode:

* Hides sidebar navigation
* Maximizes panel readability
* Optimizes spacing for large displays

***

# Performance, caching, and limits

Dashboards are optimized for responsiveness, which includes caching and record limits.

<Callout icon="bolt" color="#7748F6">
  **Caching is a feature, not a bug**

  Panel data is cached (typically \~15 minutes). If you recently changed incident data, it may take **15–20 minutes** to appear—especially with auto-refresh enabled.
</Callout>

Caching allows dashboards to load quickly even when queries involve large datasets. While this introduces slight delay in reflecting recent changes, it ensures consistent performance across organizations with high incident volume.

In practice, dashboards are optimized for strategic and operational review — not second-by-second monitoring.

Additional constraints you may encounter:

* Panel queries are limited (often **10,000 records** by default, higher with feature flags)
* Panel titles are limited in length (to keep dashboards scannable)
* Table panels cap visible rows for UI performance (exports can include full datasets)

***

# Best practices

## Build dashboards with intent

Dashboards should map to a recurring cadence:

* Weekly team reliability review
* Monthly executive metrics
* Incident program retrospectives
* On-call operational readiness

If a dashboard isn’t tied to a workflow, it tends to go stale.

## Prefer fewer, stronger panels

A dashboard with 6–10 focused panels is typically more useful than one with 25 panels competing for attention.

When in doubt:

* duplicate the dashboard,
* specialize it,
* keep each one opinionated.

## Use Group By as your default “depth tool”

If a metric is actionable, it usually has an owner. Grouping metrics by teams, services, or incident types makes accountability visible without requiring extra dashboards.

***

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Why don’t I see all collections?" icon="id-card">
    Collections are seat-based. Users with only an **On-Call** seat typically see **Alerts**, while users with **Incident Response** access see additional collections like **Incidents**, **Retrospectives**, **Action Items**, and **Users**.
  </Accordion>

  <Accordion title="Why can’t I export a table panel as PNG?" icon="image-slash">
    PNG and JPG export formats are available only for chart-based panels. Tables and aggregate values can still be exported as **PDF**, **CSV**, or **JSON**.
  </Accordion>

  <Accordion title="Why do my changes take time to show up?" icon="hourglass-half">
    Panel results are cached for performance. Changes to underlying data may take **15–20 minutes** to appear depending on cache refresh and any auto-refresh settings.
  </Accordion>

  <Accordion title="Can I filter and group by custom fields?" icon="brackets-curly">
    Yes. Panels support filtering and grouping by custom fields. Custom fields can also be used in tables as columns for drill-down workflows.
  </Accordion>

  <Accordion title="What’s the difference between dashboard filters and panel filters?" icon="sliders">
    Dashboard filters are **your personal view preferences** (date range, period, team/service filters) and apply across all panels without changing the dashboard for other users. Panel filters are stored **inside the panel configuration** and define the panel’s dataset for everyone who views it.
  </Accordion>
</AccordionGroup>

***

<Callout icon="life-ring" color="#FFC107">
  **Need help designing dashboards that actually get used?**

  If you’re not sure how to structure panels, groupings, or comparisons, contact us at **[support@rootly.com](mailto:support@rootly.com)** or use **`/rootly support`** in Slack.
</Callout>


Built with [Mintlify](https://mintlify.com).