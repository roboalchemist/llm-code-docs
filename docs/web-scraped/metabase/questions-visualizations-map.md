# Source: https://www.metabase.com/docs/latest/questions/visualizations/map

<div>

1.  [Home](/docs/latest/)
2.  [Questions](/docs/latest/questions/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Maps

Metabase has three types of map visualization:

-   [**Pin map**](#pin-map) for putting individual data points on a map using longitude and latitude coordinates;
-   [**Grid map**](#grid-map) for distributing a large number of points over a specified area.
-   [**Region map**](#region-maps) for data broken out by regions, like countries or states. Metabase comes with two built-in maps, but you can upload your own custom regions.

When you select the **Map** visualization setting, Metabase will automatically try and pick the best kind of map to use based on the table or result set, as long as the columns with the geographic data have the [right metadata](../../data-modeling/metadata-editing).

![Map types](../images/map-types.png)

                    width: 100%;
                    height: 0;
                    padding-bottom: 56.25%"}

## Pin map

Pin maps display markers or tiles for individual data points on the map. They work best for displaying small amounts of unaggregated geographic data.

### Pin map data shape

To build a pin map, you need a query that returns a result that has latitude and longitude columns. Metabase will put one pin on the map for each row in your table, based on the latitude and longitude fields. Other data in the rows will be shown in the tooltip, and won't otherwise affect the placement or shape of pins.

![Pin map data shape](../images/pin-data-shape.png) ![Pin map with a tooltip](../images/pin-map-with-tooltip.png)

Note that the tooltips will only be displayed when using the [marker pin type](#choose-pin-type).

### Create a pin map

To create a pin map:

1.  Build a query with latitude and longitude columns for each data point (either in the query builder or using SQL);

2.  Select **Visualization**, and pick **Map**;

3.  If your query results have columns whose field type is set to latitude/longitude in [table metadata](../../data-modeling/metadata-editing#semantic-type), Metabase should build a pin map automatically.

    Otherwise, click on the **Gear** icon to go to visualization settings, choose **Map type: Pin map**, and pick columns that contain latitude and longitude coordinates.

### Choose pin type

Metabase can display individual data points on a map as markers or tiles (small squares).

![Pin types](../images/pin-type.png)

Maps default to markers for results fewer then 1,000 rows, and to tiles for results with 1,000 rows or more.

To change the pin type:

1.  While viewing the map, click the **gear** icon in the bottom left.
2.  In the visualization settings, choose the pin type in the **Pin type** dropdown.
    -   **Markers**. Maps display up to 1,000 markers. If you choose the marker pin type for results with more than 1,000 rows, Metabase will still only display 1,000 markers. Maps default to markers for results fewer then 1,000 rows.
    -   **Tiles**. Maps display up to 2,000 tiles. Maps default to tiles for results greater than 1,000 rows. Tooltips will not be displayed for tiles.

By default, maps can't display more than 2,000 individual unaggregated data points, regardless of the pin type. This limit is the same for every chart displaying unaggregated data in Metabase. To increase the number of data points rendered on charts based on unaggregated queries, you can use the environment variable [`MB_UNAGGREGATED_QUERY_ROW_LIMIT`](../../configuring-metabase/environment-variables#mb_unaggregated_query_row_limit). This setting will affect data points on *all* charts---not just the pin maps---so increasing the limit too much could significantly slow down your Metabase and your browser.

If you need to display a large number of geographic data points, consider using a grid map to display the distribution instead.

## Grid map

Grid map is an aggregated version of the pin map --- like a heatmap for the distribution of pins. Grid map breaks the map into a grid based on latitude/longitude, and then colors each grid cell based on how many data points fall in it.

![Grid map](../images/grid-map.png)

### Grid map data shape

To create a grid map, you need to have a query returning a metric summarized by binned latitude/longitude coordinates.

![Example of data for grid map](../images/latlong-binned-result.png)

If you're writing a query in the query builder, you can choose how to bin latitude/longitude in the **Group by** block. If you're writing a query in SQL, you'll need to add binning logic yourself.

![Binned latitude and longitude in the query builder](../images/bin-by-latlong.png)

### Create a grid map

To create a grid map:

1.  Build a query with summary by binned latitude and longitude columns (either in the query builder or using SQL);

2.  Select **Visualization**, and pick **Map**;

3.  If your query results have columns whose field type is set to latitude/longitude in [table metadata](../../data-modeling/metadata-editing#semantic-type), Metabase should build a grid map automatically.

    Otherwise, click on the **Gear** icon to go to visualization settings, choose **Map type: grid map**, and pick columns that contain latitude and longitude coordinates.

4.  If your query contains several metrics, you can pick the one you want to display in visualization settings.

## Region maps

Region maps display a distribution of aggregated data broken out by regions, like count of users by country.

Metabase comes with two built-in regions: [world map](#world-map) with countries, and the [Unites States map](#united-states-map) with states. Admins can [add custom regions](#custom-regions) in Admin setting.

![Three types of region maps](../images/region-maps.png)

You can disable the default regions by setting the environment variable [`MB_DEFAULT_MAPS_ENABLED`](../../configuring-metabase/environment-variables#mb_default_maps_enabled).

### Region map data shape

To build a region map, you need a query (either a question built with the query builder, or a native query) with at least two columns: the column with the region name and the column with the metric that you want to display by region.

![Region map query example](../images/region-map-query.png)

The region name in the query results must be an exact case-sensitive match to the region name: two-letter country code for world maps, two-letter state code or state name for the United States map, or the [region identifier](../../configuring-metabase/custom-maps) in the custom region.

To build a region map, you must have a column with a region name in your query results, even if your query results also have latitude/longitude coordinates. Metabase can't infer regions from latitude/longitude coordinates, and doesn't check whether the coordinates of a datapoint are consistent with the region for that data point.

### Create a region map

To create a region map:

1.  Build a query with summary by region name (either in the query builder or using SQL).
2.  Select **Visualization**, and pick **Map**;
3.  Choose **Map type: region**;
4.  Pick the region map: world map (built-in), United States (built-in), or
5.  Pick the column with the region name in **Region field**
6.  If your query contains several metrics, you can pick the one you want to display in **Metric field**.

You can change the base color used for the region map, but you can't currently use custom color gradients (for example, red to green), or change how Metabase bins the metric.

### World Map

To visualize your results in the format of a map of the world broken out by country, your result must contain a column with [two-letter ISO country codes](./country-codes), like "US" or "BR", or country names like "United States of America" or "Brazil". For example:

  Country code   Metric
  -------------- --------
  US             36
  BR             25
  IN             62
  RO             78

The country codes in the query results must match the two-letter codes exactly: if the country codes are lowercase or contain extra spaces, Metabase won't recognize them.

If your query result has columns with [semantic type](../../data-modeling/metadata-editing#semantic-type) "Country", Metabase should build a world map automatically. Otherwise, you can choose which columns to use as the country name in the **Region field** visualization setting.

You can connect the country column in the world region map to a "Location" type dashboard filter.

### United States map

Creating a map of the United States from your data requires your results to contain a column that contains names of states or two-letter state codes, for example "NM" or "New Mexico", for example:

  State        Metric
  ------------ --------
  California   45
  New York     56
  Texas        34
  Illinois     67

If your query result has columns with [semantic type](../../data-modeling/metadata-editing#semantic-type) "State", Metabase should build a US map automatically. Otherwise, you can choose which columns to use as the country name in the visualization settings.

You can connect the state column in the US region map to a "Location" type dashboard filter.

### Custom regions

Admins can add more regions - like Brazil states or NYC neighborhoods - by [adding custom GeoJSON maps](../../configuring-metabase/custom-maps) in **Admin settings**. Once custom maps have been added, you'll be able to select them when building a region map in map settings.

![Select a custom region](../images/select-region-map.png)

Your query results must contain a column with values that match the *region identifier* property in the custom map setting (not the region display name).

If you want to connect the region column in a custom region map to a dashboard filter, you'll need to use a "Text or Category" - not "Location" - dashboard filter type.

## Working with maps

### Drill-through

-   **Pin map**: If the pin is linked to other tables, or there's too much information to fit in the tooltip, clicking on the pin will take you to a details page that displays a list of fields, as well as a list of connected tables.
-   **Grid map**: If you click on a grid cell, you'll get an option to zoom in further into a cell.
-   **World region map and US states region maps**: If your unaggregated data also contains latitude/longitude coordinates for each data point (in addition to the region name), then you'll get an option to zoom into a specific region, which will create a grid map of data points in that region binned by latitude/longitude. This only applies to the built-in region maps, not custom region maps.

### Set as default view

On pin and grid maps, the map resets to the default view every time the page is refreshed. To control what is displayed when someone opens a map (e.g. center around a specific point, with a specific level of zoom), adjusted your map orientation. This will be the new default view that the map returns to after a page refresh.

### Draw box to filter

On pin and grid maps, filter boxes allow you to zoom in or filter data by a specific area.

You can click **Draw box to filter** and mouse over the map. To outline a section of the map, hold your mouse down and drag across the map to create a transparent blue box. Once you've outlined your target area, release your mouse, and your map will update to filter for data in the selected area. If you've set a default view, the view will remain stationary. If no default view is set, the view will zoom in on the selected area.

Drawing a box will add filters to your query.

## Customizing map tiles

Admins can customize the background tiles that are used for pin and grid maps, see [Changing the Map tile server](../../configuring-metabase/custom-maps#map-tile-server).

![Default and satellite tiles](../images/map-tiles.png)

Currently, Metabase uses a single tile server per instance. You can't specify different tiles for different maps.

## Limitations

-   Currently, you can't customize the following visualization settings on maps:

    -   The color or pins on a pin map;
    -   The color of bins on the grid map;
    -   The number of size of bins for region maps.

-   You can't combine different types of maps. For example, you can't put pins on a region map.

-   You need to use category (not location) dashboard filter types when connecting custom region maps to dashboard filters.

-   You can't specify different background tiles for different maps.

## When NOT to use a map to visualize geographic data

If the relative locations of regions on the map aren't the main focus of your visualization, consider using a bar or row chart instead. For example, sales by state are often better represented as a row or bar chart rather than a region map.

![Bar chart as alternative to map](../images/map-alternative.png)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/questions/visualizations/map.md) ]