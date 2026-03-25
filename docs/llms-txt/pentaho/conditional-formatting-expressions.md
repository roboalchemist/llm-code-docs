# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/advanced-topics/applying-conditional-formatting-to-measures-pentaho-analyzer/conditional-formatting-expressions.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/advanced-topics/applying-conditional-formatting-to-measures-pentaho-analyzer/conditional-formatting-expressions.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/applying-conditional-formatting-to-measures-pentaho-analyzer/conditional-formatting-expressions.md

# Conditional formatting expressions

Valid MDX format strings contain properties that apply special rendering for the HTML pivot tables. A format string follows this syntax:

```
| # , # # # | style = red
```

The leading Pipe ( | ) tells Analyzer that this format string contains properties. The '#,###' is the measure's value format, which in this example is one number separated from three further places or decimal places by a comma, for example, '3,667'. The 'style=red' string is a key/value pair; all possible keys and values are explained in the table below.

The following properties are supported by Analyzer:

| Indicator Type | Description                                                                                                                                                               | Values                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| style          | Changes the cell background color.                                                                                                                                        | <ul><li>red</li><li>yellow</li><li>green</li></ul>                                                                                                  |
| arrow          | Shows a trend arrow that points up or down. A value of 'none' will not render the arrow, which is useful when you only want to show one directional arrow instead of two. | <ul><li>up</li><li>down</li><li>none</li></ul>                                                                                                      |
| link           | Creates an HTML link which will open in a new window when clicked in Analyzer.                                                                                            | <ul><li>Can be any browser-renderable URL.</li><li>It must be a fully-qualified URL.</li><li>The URL must be enclosed in quotation marks.</li></ul> |
| image          | Renders a custom image that you specify. This image file must be stored in the `/pentaho-solutions/system/analyzer/resource/image/report/` directory.                     | An image file name, with extension.                                                                                                                 |
