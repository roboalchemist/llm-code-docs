# Source: https://docs.pentaho.com/analyzer-external-javascript-api/using-pentaho-analyzer-external-javascript-api-cp/visualizations-and-gembar-ids-pentaho-analyzer-external-javascript-api.md

# Visualizations and Gembar IDs

Analyzer comes with many visualizations which can each be used to display your data in a variety of ways. This article discusses the different types of visualizations and which gembar IDs are supported.

## Pivot Table

Displays your data in a table format, consisting of rows and columns.

Visualization ID: `pivot`

| Gembar ID | UI Label | Description                                      | Field Type |
| --------- | -------- | ------------------------------------------------ | ---------- |
| rows      | Rows     | The rows which populate the data in the table    | Levels     |
| columns   | Columns  | The columns which populate the data in the table | Levels     |
| measures  | Measures | The data represented in the table                | Measures   |

## Column

A vertical bar chart.

Visualization ID: `ccc_bar`

| Gembar ID | UI Label    | Description                                                        | Field Type |
| --------- | ----------- | ------------------------------------------------------------------ | ---------- |
| rows      | X-Axis      | The data displayed along the x-axis                                | Levels     |
| columns   | Series      | The categories which are then visualized as bars                   | Levels     |
| measures  | Measures    | The data represented in the chart                                  | Measures   |
| multi     | Multi-Chart | The level which will make multiple charts display in the same view | Levels     |

## Stacked Column

A vertical bar chart which allows you to provide multiple series categories, which are stacked upon each other.

Visualization ID: `ccc_barstacked`

| Gembar ID | UI Label    | Description                                                        | Field Type |
| --------- | ----------- | ------------------------------------------------------------------ | ---------- |
| rows      | X-Axis      | The data displayed along the x-axis                                | Levels     |
| columns   | Color Stack | Multiple Series categories, which are stacked on top each other    | Levels     |
| measures  | Measures    | The data represented in the chart                                  | Measures   |
| multi     | Multi-Chart | The level which will make multiple charts display in the same view | Levels     |

## 100% Stacked Column

A vertical bar chart which allows you to provide multiple series categories, which are stacked upon each other. Bars fill the entire chart and are a relative value representation.

Visualization ID: `ccc_barnormalized`

| Gembar ID | UI Label    | Description                                                        | Field Type |
| --------- | ----------- | ------------------------------------------------------------------ | ---------- |
| rows      | X-Axis      | The data displayed along the x-axis                                | Levels     |
| columns   | Color Stack | Multiple Series categories, which are stacked on top each other    | Levels     |
| measures  | Measures    | The data represented in the chart                                  | Measures   |
| multi     | Multi-Chart | The level which will make multiple charts display in the same view | Levels     |

## Column-Line Combo

Displays a vertical bar chart combined with a line chart in the same visualization.

Visualization ID: `ccc_barline`

| Gembar ID    | UI Label           | Description                                                        | Field Type |
| ------------ | ------------------ | ------------------------------------------------------------------ | ---------- |
| rows         | X-Axis             | The data displayed along the x-axis                                | Levels     |
| columns      | Series             | The categories which are then visualized as bars and lines         | Levels     |
| measures     | Measures - Columns | The data represented in the chart for the columns                  | Measures   |
| measuresLine | Measures - Line    | The data represented in the chart for the lines                    | Measures   |
| multi        | Multi-Chart        | The level which will make multiple charts display in the same view | Levels     |

## Bar

A horizontal bar chart.

Visualization ID: `ccc_horzbar`

| Gembar ID | UI Label    | Description                                                        | Field Type |
| --------- | ----------- | ------------------------------------------------------------------ | ---------- |
| rows      | Y-Axis      | The data displayed along the y-axis                                | Levels     |
| columns   | Series      | The categories which are then visualized as bars                   | Levels     |
| measures  | Measures    | The data represented in the chart                                  | Measures   |
| multi     | Multi-Chart | The level which will make multiple charts display in the same view | Levels     |

## Stacked Bar

A horizontal bar chart which allows you to provide multiple series categories, which are stacked upon each other.

Visualization ID: `ccc_horzbarstacked`

| Gembar ID | UI Label    | Description                                                        | Field Type |
| --------- | ----------- | ------------------------------------------------------------------ | ---------- |
| rows      | Y-Axis      | The data displayed along the y-axis                                | Levels     |
| columns   | Color Stack | Multiple Series categories, which are stacked on top each other    | Levels     |
| measures  | Measures    | The data represented in the chart                                  | Measures   |
| multi     | Multi-Chart | The level which will make multiple charts display in the same view | Levels     |

## 100% Stacked Bar

A horizontal bar chart which allows you to provide multiple series categories, which are stacked upon each other. Bars fill the entire chart and are a relative value representation.

Visualization ID: `ccc_horzbarnormalized`

| Gembar ID | UI Label    | Description                                                        | Field Type |
| --------- | ----------- | ------------------------------------------------------------------ | ---------- |
| rows      | Y-Axis      | The data displayed along the y-axis                                | Levels     |
| columns   | Color Stack | Multiple Series categories, which are stacked on top each other    | Levels     |
| measures  | Measures    | The data represented in the chart                                  | Measures   |
| multi     | Multi-Chart | The level which will make multiple charts display in the same view | Levels     |

## Line

A line chart.

Visualization ID: `ccc_line`

| Gembar ID | UI Label    | Description                                                        | Field Type |
| --------- | ----------- | ------------------------------------------------------------------ | ---------- |
| rows      | X-Axis      | The data displayed along the x-axis                                | Levels     |
| columns   | Series      | The categories which are then visualized as lines                  | Levels     |
| measures  | Measures    | The data represented in the chart                                  | Measures   |
| multi     | Multi-Chart | The level which will make multiple charts display in the same view | Levels     |

## Area

An area chart.

Visualization ID: `ccc_area`

| Gembar ID | UI Label    | Description                                                                       | Field Type |
| --------- | ----------- | --------------------------------------------------------------------------------- | ---------- |
| rows      | X-Axis      | The data displayed along the x-axis                                               | Levels     |
| columns   | Series      | The categories which are then visualized as lines with the area filled underneath | Levels     |
| measures  | Measures    | The data represented in the chart                                                 | Measures   |
| multi     | Multi-Chart | The level which will make multiple charts display in the same view                | Levels     |

## Pie

A pie chart.

Visualization ID: `ccc_pie`

| Gembar ID | UI Label  | Description                                                            | Field Type |
| --------- | --------- | ---------------------------------------------------------------------- | ---------- |
| rows      | Slices    | The level which is displayed as slices of the pie chart                | Levels     |
| columns   | Multi-Pie | The level which will make multiple pie charts display in the same view | Levels     |
| measures  | Measures  | The data represented in the chart                                      | Measures   |

## Sunburst

A sunburst chart, which is a a multi-leveled pie chart. Each outer ring is a subset of the inner ring.

Visualization ID: `ccc_sunburst`

| Gembar ID | UI Label    | Description                                                          | Field Type |
| --------- | ----------- | -------------------------------------------------------------------- | ---------- |
| rows      | Slices      | The levels which will be displayed as tiers of slices of a pie chart | Levels     |
| size      | Size By     | The measure by which the slices are sized                            | Measures   |
| multi     | Multi-Chart | The level which will make multiple charts display in the same view   | Levels     |

## Scatter Chart Visualization

A scatter plot, which allows you to color and size the dots relative to different measures.

Visualization ID: `ccc_scatter`

| Gembar ID | UI Label    | Description                                                                       | Field Type |
| --------- | ----------- | --------------------------------------------------------------------------------- | ---------- |
| x         | X-Axis      | The data displayed along the x-axis                                               | Measures   |
| y         | Y-Axis      | The data displayed along the y-axis                                               | Measures   |
| rows      | Points      | The measures by which the points are drawn in relation to the x and y axis values | Levels     |
| color     | Color By    | The measure by which the points are colored                                       | Levels     |
| size      | Size By     | The measure by which the points are relatively sized                              | Measures   |
| multi     | Multi-Chart | The level which will make multiple charts display in the same view                | Levels     |

## Heat Grid Visualization

A multi-dimensional box plot where values are colored relative to measures.

Visualization ID: `ccc_heatgrid`

| Gembar ID | UI Label | Description                                          | Field Type |
| --------- | -------- | ---------------------------------------------------- | ---------- |
| rows      | X-Axis   | The data displayed along the x-axis                  | Levels     |
| columns   | Y-Axis   | The data displayed along the y-axis                  | Levels     |
| color     | Color By | The measure by which the points are colored          | Measures   |
| size      | Size By  | The measure by which the points are relatively sized | Measures   |

## Geo Map Visualization

A map based visualization where addresses can be plotted, but can also be colored and sized relative measures.

Visualization ID: `open_layers`

| Gembar ID | UI Label     | Description                                           | Field Type |
| --------- | ------------ | ----------------------------------------------------- | ---------- |
| rows      | Geography    | The levels which will show up on the map as locations | Levels     |
| color     | Color By     | The measure by which the points are colored           | Measures   |
| size      | Size By      | The measure by which the points are relatively sized  | Measures   |
| columns   | Other Fields | Additional criteria by which points are constrained   | Levels     |
