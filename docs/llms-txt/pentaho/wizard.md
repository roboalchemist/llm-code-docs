# Source: https://docs.pentaho.com/pba-report-designer/attributes-reference-cp-prd/wizard.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/attributes-reference-cp-prd/wizard.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/attributes-reference-cp-prd/wizard.md

# Wizard

The following attributes belong to the **wizard** property:

| Attribute Name               | Purpose                                                                                                          | Values                                                                                                                                                  |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **wizard-enabled**           | If enabled, clears out all bands affected by the **generated-content-marker** attribute and starts from scratch. | Boolean; default is true.                                                                                                                               |
| **aggregation-group**        | Defines the group name to aggregate by.                                                                          | String; default is not defined.                                                                                                                         |
| **aggregation-type**         | Defines the function to use to aggregate the field.                                                              | String; default is not defined.                                                                                                                         |
| **generated-content-marker** | Marks the band that you want to insert the wizard's generated content into.                                      | Boolean; default is false.                                                                                                                              |
| **grid-color**               | Defines the hexadecimal border color of the selected element in the **Details** band.                            | String; default is not defined.                                                                                                                         |
| **grid-style**               | Defines the border style of the selected element in the **Details** band.                                        | String; default is not defined. Possible values are: solid, dashed, dot-dash, dot-dot-dash, dotted, double, hidden, none, groove, ridge, inset, outset. |
| **grid-width**               | Defines the border width (in pixels) of the selected element in the **Details** band.                            | Integer; default is not defined.                                                                                                                        |
| **label-detail-header**      | Defines the **Details** band header.                                                                             | String; default is the selected field name.                                                                                                             |
| **only-show-changing-value** | Controls whether the field repeats in the **Details** band.                                                      | Boolean; default is false.                                                                                                                              |
