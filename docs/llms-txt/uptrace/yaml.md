# Source: https://uptrace.dev/raw/features/dashboards/yaml.md

# Dashboard YAML Templates

> Complete reference for the Uptrace dashboard template YAML format, covering metadata, tables, grids, grid items, monitors, and composition.

Uptrace dashboards can be defined as YAML templates. Templates are used for built-in dashboards that ship with Uptrace and for importing/exporting user-created dashboards.

When Uptrace receives new metrics, it checks available templates and automatically creates matching dashboards.

## Template structure

Every template starts with a `schema: v2` header followed by metadata, then optional `table`, `grid_sections`, and `metric_monitors` sections.

```yaml
schema: v2
name: 'Hostmetrics: Overview'
description: Tracks host CPU, memory, and system load.
tags: [otel, infra]
version: v25.04.20
setup_link: https://example.com/setup
doc_link: https://example.com/docs

# Optional: minimum query interval
min_interval: 1m

# Optional: shift the query time window
time_offset: 5m

# Optional: only apply when these metrics exist
require_metrics:
  - metric: system_cpu_utilization
  - library: io.opentelemetry.instrumentation.system
    metric: system_cpu_time

table_grid_items:
  # ... summary widgets above the table

table:
  # ... table dashboard definition

grid_sections:
  # ... grid dashboard rows

metric_monitors:
  # ... bundled alert monitors
```

### Top-level fields

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        schema
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      Must be <code>
        "v2"
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      Human-readable dashboard title
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        description
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Summary of the dashboard's purpose
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        tags
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      Categorization labels (see <a href="#tags">
        Tags
      </a>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        version
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      Revision in <code>
        vYY.MM.DD
      </code>
      
       format (e.g., <code>
        v25.04.20
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setup_link
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      URL to instrumentation/setup instructions
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        doc_link
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      URL to documentation
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        min_interval
      </code>
    </td>
    
    <td>
      duration
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Minimum query interval (e.g., <code>
        1m
      </code>
      
      , <code>
        5m
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        time_offset
      </code>
    </td>
    
    <td>
      duration
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Shifts query time window (e.g., <code>
        5m
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        require_metrics
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Metrics that must exist before the template is applied
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        table_grid_items
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Summary widgets shown above the table
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        table
      </code>
    </td>
    
    <td>
      object
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Table dashboard definition
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        grid_query
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      MQL query for grid variables
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        grid_variables
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Variable names extracted from <code>
        grid_query
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        include_grid_sections
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      no
    </td>
    
    <td>
      References to other templates (see <a href="#template-composition">
        Composition
      </a>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        grid_sections
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Grid section definitions
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        metric_monitors
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Metric monitors bundled with the template
    </td>
  </tr>
</tbody>
</table>

## Metrics and queries

Metrics and queries appear throughout the template (tables, grid items, monitors). They follow the same pattern everywhere.

### Metrics

The `metrics` field declares metric aliases using MQL syntax:

```yaml
metrics:
  - system_cpu_utilization as $cpu_util
  - system_memory_usage as $mem_usage
```

Each entry takes the form `metric_name as $alias`. The alias (prefixed with `$`) is used in queries.

### Query

The `query` field is a list of MQL clauses. Splitting across lines improves readability -- clauses are joined into a single query during processing.

```yaml
query:
  - group by host_name
  - avg($cpu_util) as cpu_avg
  - sum($mem_usage{state="used"}) as mem_used
  - where device !~ "loop"
```

Common clause patterns:

- **Aggregations**: `avg($x)`, `sum($x)`, `max($x)`, `min($x)`, `p50($x)`, `p75($x)`, `p90($x)`, `p99($x)`
- **Rate functions**: `perMin(sum($x))`, `perSec(sum($x))`
- **Counting**: `histogram_count($x)`, `uniq($x, attr_name)`
- **Grouping**: `group by attr_name`, `group by attr1, attr2`
- **Filtering**: `where attr = "value"`, `where attr !~ "pattern"`
- **Aliasing**: `sum($x) as my_alias`
- **Inline grouping**: `avg($x) as y group by state`
- **Attribute filtering**: `$metric{state="used"}`, `$metric{direction=read}`
- **Arithmetic**: `sum($a) / sum($b) as ratio`

## Table dashboards

The `table` section defines a table view where each row leads to the grid dashboard filtered by the row's group-by attributes.

```yaml
table:
  metrics:
    - system_cpu_utilization as $cpu_util
    - system_memory_usage as $mem_usage
  query:
    - group by host_name
    - avg($cpu_util) as cpu_util
    - sum($mem_usage{state="used"}) as mem_used
  columns:
    cpu_util: { unit: utilization }
    mem_used: { unit: bytes }
  variables: [deployment_environment, service_name]
```

### Table fields

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        metrics
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      MQL metric expressions
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        query
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      MQL query clauses
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        columns
      </code>
    </td>
    
    <td>
      map
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Per-column display settings (shorthand format)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        overrides
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Per-column visual property overrides (structured format)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        variables
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Query variable names for parameterized filtering
    </td>
  </tr>
</tbody>
</table>

### Column settings (shorthand)

The `columns` map provides a compact syntax for column formatting:

```yaml
columns:
  cpu_util: { unit: utilization }
  mem_used: { unit: bytes, color: red }
  availability: { unit: utilization, agg_func: avg }
  max_latency: { unit: milliseconds, agg_func: max, display: bar }
```

Available column properties:

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        unit
      </code>
    </td>
    
    <td>
      Display unit (e.g., <code>
        bytes
      </code>
      
      , <code>
        utilization
      </code>
      
      , <code>
        seconds
      </code>
      
      , <code>
        nanoseconds
      </code>
      
      , <code>
        milliseconds
      </code>
      
      , <code>
        1
      </code>
      
      , or custom like <code>
        span/min
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        color
      </code>
    </td>
    
    <td>
      Display color
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        agg_func
      </code>
    </td>
    
    <td>
      Aggregation function (e.g., <code>
        sum
      </code>
      
      , <code>
        avg
      </code>
      
      , <code>
        max
      </code>
      
      , <code>
        last
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        display
      </code>
    </td>
    
    <td>
      Column display mode: <code>
        value
      </code>
      
       (default), <code>
        sparkline
      </code>
      
      , or <code>
        bar
      </code>
      
      . Can also be a map: <code>
        {mode: bar, min: 0, max: 1}
      </code>
    </td>
  </tr>
</tbody>
</table>

### Column overrides (structured)

The `overrides` format provides more control:

```yaml
overrides:
  - column: cpu_util
    properties:
      - name: unit
        value: utilization
      - name: color
        value: red
```

## Table grid items

`table_grid_items` are summary widgets displayed above the main table. They support the same grid item types as `grid_sections` items (gauge, text, chart, table, heatmap).

```yaml
table_grid_items:
  - title: Number of hosts
    type: text
    metrics:
      - system_memory_usage as $mem_usage
    query:
      - uniq($mem_usage, host_name) as num_host
    text: ${num_host} hosts

  - title: Memory utilization
    type: gauge
    metrics:
      - system_memory_usage as $mem_usage
    query:
      - sum($mem_usage{state!="free"}) / sum($mem_usage) as mem_util
    columns:
      mem_util: { unit: utilization }
```

## Grid dashboards

The `grid_sections` section defines a classic grid of charts organized in collapsible rows.

```yaml
grid_sections:
  - title: General
    items:
      - title: CPU utilization
        metrics:
          - system_cpu_utilization as $cpu_util
        query:
          - avg($cpu_util)

      - title: RAM usage
        metrics:
          - system_memory_usage as $mem_usage
        query:
          - sum($mem_usage) group by state
        columns:
          mem_usage: { unit: bytes }
        fill_opacity: 0.1
```

Each row has a `title` and a list of `items`.

## Grid item types

Grid items are the building blocks of both `grid_sections` and `table_grid_items`. The `type` field determines the kind of widget. When `type` is omitted, it defaults to `chart`.

### Common fields

All grid item types share these fields:

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        title
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      Display heading
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        description
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Explanation shown below the title
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        type
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      One of: <code>
        chart
      </code>
      
       (default), <code>
        table
      </code>
      
      , <code>
        heatmap
      </code>
      
      , <code>
        gauge
      </code>
      
      , <code>
        text
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        width
      </code>
    </td>
    
    <td>
      int
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Grid column span
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        height
      </code>
    </td>
    
    <td>
      int
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Grid section span
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        x_axis
      </code>
    </td>
    
    <td>
      int
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Horizontal grid position
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        y_axis
      </code>
    </td>
    
    <td>
      int
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Vertical grid position
    </td>
  </tr>
</tbody>
</table>

### Chart

Charts are the default grid item type. They render time-series data as line, bar, or scatter plots.

```yaml
- title: CPU time
  # type: chart (default, can be omitted)
  metrics:
    - system_cpu_time as $cpu_time
  query:
    - perMin(sum($cpu_time)) as cpu_time group by state
  fill_opacity: 0.1
```

#### Chart-specific fields

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        metrics
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      MQL metric expressions
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        query
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      MQL query clauses
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        chart
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Chart type: <code>
        line
      </code>
      
       (default), <code>
        bar
      </code>
      
      , <code>
        scatter
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        fill_opacity
      </code>
    </td>
    
    <td>
      float
    </td>
    
    <td>
      Area fill opacity, 0 to 1
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        stack
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Stacking mode: <code>
        ""
      </code>
      
       (none) or <code>
        "all"
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        columns
      </code>
    </td>
    
    <td>
      map
    </td>
    
    <td>
      Per-metric display settings with <code>
        unit
      </code>
      
       and <code>
        color
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        legend
      </code>
    </td>
    
    <td>
      object
    </td>
    
    <td>
      Legend configuration (see below)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        properties
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      Visual properties (see <a href="#visual-properties">
        Visual properties
      </a>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        overrides
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      Per-timeseries overrides (see <a href="#timeseries-overrides">
        Timeseries overrides
      </a>
      
      )
    </td>
  </tr>
</tbody>
</table>

#### Legend configuration

```yaml
legend:
  type: table     # "none", "list", or "table"
  placement: bottom # "bottom" or "right"
  values: [avg, min, max, last]
  items_per_page: 10
```

### Table

Table grid items render query results in a tabular format.

```yaml
- title: Slowest groups
  type: table
  metrics:
    - uptrace_tracing_spans as $spans
  query:
    - group by _group_id
    - group by _system
    - p50($spans)
```

#### Table-specific fields

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        metrics
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      MQL metric expressions
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        query
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      MQL query clauses
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        columns
      </code>
    </td>
    
    <td>
      map
    </td>
    
    <td>
      Per-column display settings (same as <a href="#column-settings-shorthand">
        table columns
      </a>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        overrides
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      Per-column visual property overrides
    </td>
  </tr>
</tbody>
</table>

### Heatmap

Heatmaps visualize the distribution of a single histogram metric over time.

```yaml
- title: Span duration heatmap
  type: heatmap
  metric: uptrace_tracing_spans
  unit: milliseconds
```

#### Heatmap-specific fields

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        metric
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Single metric name (not an alias)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        unit
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Display unit
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        query
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      Optional MQL query clauses for filtering
    </td>
  </tr>
</tbody>
</table>

### Gauge

Gauges display a single aggregated value, optionally with value mappings for status indicators.

```yaml
- title: Status
  type: gauge
  metrics:
    - httpcheck_status as $status
  query:
    - sum($status{http_status_class="2xx"})
  value_mappings:
    - op: gte
      value: 1
      text: UP
      color: green
    - op: eq
      value: 0
      text: DOWN
      color: red
    - op: any
      text: UNKNOWN
      color: gray
```

#### Gauge-specific fields

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        metrics
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      MQL metric expressions
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        query
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      MQL query clauses
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        columns
      </code>
    </td>
    
    <td>
      map
    </td>
    
    <td>
      Per-column settings with <code>
        unit
      </code>
      
       and <code>
        agg_func
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        overrides
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      Per-column visual property overrides
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        value_mappings
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      Maps values to labels and colors
    </td>
  </tr>
</tbody>
</table>

#### Value mappings

Value mappings are evaluated in order. The first matching rule wins.

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        op
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Comparison operator: <code>
        any
      </code>
      
      , <code>
        eq
      </code>
      
      , <code>
        lt
      </code>
      
      , <code>
        lte
      </code>
      
      , <code>
        gt
      </code>
      
      , <code>
        gte
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        value
      </code>
    </td>
    
    <td>
      number
    </td>
    
    <td>
      Threshold value (not required for <code>
        any
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        text
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Display label
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        color
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Display color
    </td>
  </tr>
</tbody>
</table>

### Text

Text items render a Go template string with metric data, useful for summary counts and labels.

```yaml
- title: Host count
  type: text
  metrics:
    - process_runtime_go_goroutines as $goroutines
  query:
    - uniq($goroutines, host_name) as num_host
  text: ${num_host} hosts
```

#### Text-specific fields

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        metrics
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      MQL metric expressions
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        query
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      MQL query clauses
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        text
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Template string using <code>
        ${column_name}
      </code>
      
       placeholders
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        columns
      </code>
    </td>
    
    <td>
      map
    </td>
    
    <td>
      Per-column settings with <code>
        unit
      </code>
      
       and <code>
        agg_func
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        overrides
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      Per-column visual property overrides
    </td>
  </tr>
</tbody>
</table>

## Visual properties

Visual properties control chart appearance. They can be set via shorthand fields (`chart`, `fill_opacity`, `stack`) or the `properties` list.

```yaml
properties:
  - name: chartType
    value: bar
  - name: fillOpacity
    value: 0.3
  - name: stack
    value: all
```

| Property        | Type    | Values                   |<br />


| --------------- | ------- | ------------------------ | ----------- | ------------------- |<br />


| `chartType`     | string  | `line`, `bar`, `scatter` |<br />


| `stack`         | string  | `""` (off), `all`        |<br />


| `connectNulls`  | boolean | `true`, `false`          |<br />


| `lineWidth`     | number  | Line thickness           |<br />


| `fillOpacity`   | number  | 0 to 1                   |<br />


| `symbolSize`    | number  | Data point symbol size   |<br />


| `symbol`        | string  | Symbol name              |<br />


| `color`         | string  | Color name               |<br />


| `colorScheme`   | string  | Color scheme name        |<br />


| `unit`          | string  | Display unit             |<br />


| `aggFunc`       | string  | Aggregation function     |<br />


| `columnDisplay` | object  | `{mode: "value"          | "sparkline" | "bar", min?, max?}` |

## Timeseries overrides

Chart items support per-timeseries overrides that apply visual properties to specific series:

```yaml
overrides:
  - matchers:
      - target: metric   # "metric" or "timeseries"
        value: cpu_idle
    properties:
      - name: unit
        value: utilization
      - name: color
        value: blue
```

The `target` field specifies what to match:

- `metric` -- matches by metric/column name
- `timeseries` -- matches by timeseries label

## Metric monitors

The `metric_monitors` section bundles alert monitors with the dashboard:

```yaml
metric_monitors:
  - key: cpu_usage
    name: CPU usage
    metrics:
      - system_cpu_load_average_15m as $load_avg_15m
      - system_cpu_time as $cpu_time
    query:
      - avg($load_avg_15m) / uniq($cpu_time, cpu) as cpu_util
      - group by host_name
    column_unit: utilization
    max_allowed_value: 3
    num_eval_points: 10
    trend_agg_func: last
```

### Monitor fields

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Required
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        key
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      Unique monitor identifier within the template
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      Human-readable title
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        metrics
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      MQL metric expressions
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        query
      </code>
    </td>
    
    <td>
      list
    </td>
    
    <td>
      yes
    </td>
    
    <td>
      MQL query clauses
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        status
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      <code>
        active
      </code>
      
       (default) or <code>
        paused
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        column
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Metric column to evaluate
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        column_unit
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Display unit for the column
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        min_allowed_value
      </code>
    </td>
    
    <td>
      number
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Lower threshold -- values below this trigger an alert
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        max_allowed_value
      </code>
    </td>
    
    <td>
      number
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Upper threshold -- values above this trigger an alert
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        num_eval_points
      </code>
    </td>
    
    <td>
      int
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Number of recent data points to evaluate
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        trend_agg_func
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Aggregation function for trend detection (e.g., <code>
        last
      </code>
      
      )
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        trend_sensitivity
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Sensitivity of trend detection
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        bounds_source
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      How anomaly bounds are calculated
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        resolution
      </code>
    </td>
    
    <td>
      duration
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Data point interval
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        absent_points
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Missing data handling: <code>
        alert
      </code>
      
       to alert on missing data
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        time_offset
      </code>
    </td>
    
    <td>
      duration
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Shifts the evaluation window
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        notify_everyone_by_email
      </code>
    </td>
    
    <td>
      boolean
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Email all project members on alert
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        repeat_interval
      </code>
    </td>
    
    <td>
      object
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Notification repeat interval configuration
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        flapping
      </code>
    </td>
    
    <td>
      object
    </td>
    
    <td>
      no
    </td>
    
    <td>
      Flapping detection parameters
    </td>
  </tr>
</tbody>
</table>

## Template composition

Templates can include grid sections from other templates using `include_grid_sections`. This enables modular dashboard composition:

```yaml
# Parent: uptrace.dotnet.10.all.yml
schema: v2
name: '.NET: All'
tags: [otel, app]
version: v25.04.20

table:
  metrics:
    - process_runtime_dotnet_gc_heap_size as $heap_size
  query:
    - group by service_name
    - sum($heap_size) as heap_size

include_grid_sections:
  - uptrace.dotnet.20.gc
  - uptrace.dotnet.30.runtime
  - uptrace.dotnet.40.thread_pool
```

Each entry references another template by filename (without `.yml`). The child template's `grid_sections` are appended to the parent's.

## Metric requirements

The `require_metrics` field controls when a template is activated. It appears at the top level of the template:

```yaml
require_metrics:
  - metric: system_cpu_utilization
  - library: io.opentelemetry.instrumentation.system
    metric: system_cpu_time
```

<table>
<thead>
  <tr>
    <th>
      Field
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        library
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Instrumentation library name (optional)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        metric
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      Metric name that must exist
    </td>
  </tr>
</tbody>
</table>

## Tags

Tags categorize dashboards for filtering. Use one data source tag and 1-3 category tags.

### Data source tags

- `otel` -- OpenTelemetry metrics
- `prom` -- Prometheus metrics

### Category tags

- `infra` -- System resources (CPU, RAM, disk, network)
- `network` -- Network-specific metrics
- `db` -- Database systems (PostgreSQL, MySQL, Redis)
- `app` -- Application runtimes (Go, .NET, Java, JVM)
- `k8s` -- Kubernetes resources
- `tracing` -- Distributed tracing and spans
- `logs` -- Log aggregation
- `messaging` -- Message queues (Kafka)
- `self_monitoring` -- Uptrace internal metrics (no data source tag needed)

```yaml
tags: [otel, infra]         # Host metrics
tags: [otel, app, db]       # Go SQL client
tags: [otel, k8s, infra]    # Kubernetes infrastructure
tags: [self_monitoring]      # Uptrace self-monitoring
```

## Template ID and filename

The template ID is derived from the filename:

- `uptrace.hostmetrics.10.overview.yml` becomes ID `uptrace.hostmetrics.overview`
- The numeric suffix (e.g., `10`) is stripped from the ID and used as a display priority

## Validation

Templates are validated in two ways:

1. **YAML parsing** with `DisallowUnknownField` catches typos and unknown keys.
2. **JSON Schema validation** against `schema.json` ensures structural correctness.

To validate templates:

```bash
go run cmd/cloud/main.go dashboard validate_templates
```

## Full example

```yaml
schema: v2
name: 'HTTP Check: Endpoints'
description: Monitors HTTP endpoint availability and response times.
tags: [otel, infra]
version: v25.04.20
setup_link: https://example.com/setup

table_grid_items:
  - title: Successful checks
    type: text
    text: ${num_up} out of ${num_all}
    metrics:
      - httpcheck_status as $status
    query:
      - uniq($status{http_status_class="2xx"}) as num_all
      - uniq($status{http_status_class="2xx", _value=1}) as num_up

table:
  metrics:
    - httpcheck_status as $status
    - httpcheck_duration as $duration
  query:
    - group by http_url
    - group by host_name
    - sum($status{http_status_class="2xx"}) / sum($status) as availability
    - avg($duration)
  columns:
    availability: { unit: utilization, agg_func: avg }

grid_sections:
  - title: Gauges
    items:
      - title: Status
        type: gauge
        metrics:
          - httpcheck_status as $status
        query:
          - sum($status{http_status_class="2xx"})
        value_mappings:
          - op: gte
            value: 1
            text: UP
            color: green
          - op: eq
            value: 0
            text: DOWN
            color: red
          - op: any
            text: UNKNOWN
            color: gray

  - title: General
    items:
      - title: HTTP check result
        metrics:
          - httpcheck_status as $status
        query:
          - $status group by http_status_code

      - title: HTTP check duration
        metrics:
          - httpcheck_duration as $duration
        query:
          - avg($duration)

      - title: Span duration heatmap
        type: heatmap
        metric: uptrace_tracing_spans
        unit: milliseconds

metric_monitors:
  - key: http_check_is_down
    name: HTTP check is down
    metrics:
      - httpcheck_status as $status
    query:
      - sum($status{http_status_class="2xx"}) as status_2xx
      - group by http_url
      - group by host_name
    min_allowed_value: 1
    max_allowed_value: 1
    num_eval_points: 1
    absent_points: alert
    trend_agg_func: last
```
