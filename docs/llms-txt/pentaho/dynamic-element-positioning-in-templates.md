# Source: https://docs.pentaho.com/pba-report-designer/create-report-design-wizard-templates-cp/dynamic-element-positioning-in-templates.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/create-report-design-wizard-templates-cp/dynamic-element-positioning-in-templates.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-report-design-wizard-templates-cp/dynamic-element-positioning-in-templates.md

# Dynamic element positioning in templates

Use the following methods to accommodate for multiple page sizes in reports:

## Percentages

Express the height, width, x position, and y position in percentages.

## Block, inline, or row

Switch the band’s layout mode from canvas to either block, inline or row:

| layout-mode | value                                                                                                                                                       |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Canvas      | Uses the x and y position to place the element in the band.                                                                                                 |
| Block       | Stacks elements vertically according to the layer order in a band; width is set to 100%.                                                                    |
| Inline      | Stacks elements horizontally according to the layer order in a band; width is determined by the length of the text in the field, and wraps within the band. |
| Row         | Stacks elements horizontally in one row according to the layer order in the band.                                                                           |

## Dynamic height message elements

Set `dynamic-height=true` on message elements. This will allow the element size to grow according to line height. Also, setting the following Reporting engine configuration option will allow the element size to grow according to the font size used:

```
org.pentaho.reporting.engine.classic.core.layout.​fontrenderer.UseMaxCharBounds = true
```

## Proportional column widths

To support varying window sizes in a Web browser, enable the use of proportional column widths so that the resulting table will have a width of 100% and the columns will have the proportional equivalent of their static widths as width. The relevant Reporting engine option to set this globally is:

```
org.pentaho.reporting.engine.classic.core.modules.​output.table.html.ProportionalColumnWidths = true
```
