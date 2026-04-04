# Source: https://docs.datadoghq.com/dashboards/guide/widget_colors.md

---
title: Selecting the right colors for your graphs
description: >-
  Choose appropriate colors for graph series to ensure clear data distinction
  and effective troubleshooting for teams.
breadcrumbs: >-
  Docs > Dashboards > Graphing Guides > Selecting the right colors for your
  graphs
---

# Selecting the right colors for your graphs

In Datadog graphs, color is the primary method by which you can distinguish between series of data. Selecting the right color for your graph ensures that your teammates can parse data in your graphs, draw insights, and troubleshoot effectively.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/colors_top.5b5aa95b82f69f4cebbe02e53cbbb64f.png?auto=format"
   alt="Under the heading 'Graph your data', the user is selecting from a list of color palettes." /%}

## Types of color palettes{% #types-of-color-palettes %}

### Categorical palettes{% #categorical-palettes %}

Categorical palettes are best used for data that needs to be differentiated, but does not follow a natural orderâfor example, availability zones.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/2_alphabet.c4b8906622f0333038b20a8145bebf0c.png?auto=format"
   alt="A palette showing letters A B C D E F G, where each letter is a different hue." /%}

#### Classic{% #classic %}

The default Classic palette uses a set of six distinct colors optimized for readability. Colors assigned to series repeat if the number of series exceeds six. Adjacent series typically have distinct colors. However, in rare conditions, adjacent series could use the same color if intermediate series have no value for partial timeframes.

The Classic color palette has visual accessibility support.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/3_classic_palette.1fb6dabdf783fb35697478aa0a4535c9.png?auto=format"
   alt="An overview of what the Classic palette looks like for a donut graph and a stacked bar graph." /%}

#### Consistent/Semantic{% #consistentsemantic %}

The Consistent palette assigns a fixed color consistently to a series of data, based on its tav value. This makes it easier to correlate data across different charts. However, it **does not** guarantee unique colors for adjacent data series within the same widget, and it does not have accessibility support. For more information, see [Understanding Duplicate Colors in the Consistent Palette](https://docs.datadoghq.com/dashboards/guide/consistent_color_palette).

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/4_consistent_palette.3e615aab25d15342d0b4d74dd092e9a1.png?auto=format"
   alt="A color palette for the Consistent/Semantic palette." /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/5_consistent_interface.b62440f0751ae621cc3311d560e6b2d7.png?auto=format"
   alt="Consistent palette bar graphs." /%}

For a small subset of compatible tags, Datadog automatically recognizes the meaning behind each series of data. In this case, the Consistent color palette appears as a Semantic color palette, which uses color to represent meaning. For instance, the color red may represent an error. See [Compatible Semantic Tags](https://docs.datadoghq.com/dashboards/guide/compatible_semantic_tags) for a list of supported tags.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/6_semantic_interface.fac6dfe1cbc3394486680a66bd5db5a1.png?auto=format"
   alt="Semantic palette bar graph." /%}

### Diverging palettes{% #diverging-palettes %}

Use a Diverging palette when you need to emphasize the difference in values within a data set. Diverging palettes are best suited to data that has a natural order and a natural midpoint. For example: the amount of change in memory utilization, from -100% to +100%, with a natural midpoint at 0%.

There are two Diverging palette options: cool (green and blue) or warm (interpolates between yellow and orange).



{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/7_divergent_palette.7a774927250142d25ab81d9825275c27.png?auto=format"
   alt="A palette showing -3 -2 -1 0 1 2 3, with different color gradients on both ends." /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/8_divergent_graphs.2eab86faa172a723a2c9a795131ed247.png?auto=format"
   alt="Diverging palette graphs." /%}



### Sequential palettes{% #sequential-palettes %}

Use a Sequential palettes when you need to emphasize that different series in your dataset have something in common. This palette works well for data that has a natural order, such as the CPU utilization (from 0% to 100%) of a group of hosts.

Color options include purple, orange, gray, red, green, and blue.

When combined with color overrides, the Sequential palettes help you to distinguish results from multiple queries in a single chart.



{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/9_sequential_palette.f9b40d91a0f1fd11306e096484955893.png?auto=format"
   alt="A palette showing 1 2 3 4 5 6 7, where the colors are a gradient." /%}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/10_sequential_graphs.07c69aa90e00d19c148764a9af8bb2ac.png?auto=format"
   alt="Sequential palette graphs." /%}



## Color overrides{% #color-overrides %}

Color overrides allow you to assign a single color of your choice to each query. This is particularly useful when distinguishing the results from multiple queries in a single chart.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/11_overrides.2ad38ee89f9394a8c06f2b3af8fff930.png?auto=format"
   alt="The panel that allows a user to configure color overrides." /%}

**Note**: If your query aggregates by a tag (for instance, using 'sum by' or 'avg by'), you can only select a palette override. This prevents different series from using the same color, preserving readability.

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/12_palette_and_color_override_comparison.49a4390fc211e1303e0ca6c12f052270.png?auto=format"
   alt="A side-by-side comparison of the color override and palette override dropdown panels." /%}

## Accessibility settings{% #accessibility-settings %}

Datadog offers accessible color modes for graphs to cater to visual needs, including color vision deficiency, low visual acuity, and contrast sensitivity. Selecting an accessible color mode renders all graphs with the Classic palette in a set of accessible colors catered to a specific vision need. You can set an accessible color mode from the [User Preferences page](https://app.datadoghq.com/personal-settings/preferences).

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/colors/visual_accessibility.db3896c7f4c12eea97113b8435f13bfb.png?auto=format"
   alt="Available visual accessibility options: Default, protanopia (difficulty distinguishing greens and reds), deuteranopia (difficulty distinguishing between reds, greens, and yellows), tritanopia (difficulty distinguishing blues and greens), high contrast (increased separation between colors for lower visual acuity), low saturation (decreased contrast for visual contrast sensitivity)." /%}
