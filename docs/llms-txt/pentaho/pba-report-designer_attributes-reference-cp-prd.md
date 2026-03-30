# Source: https://docs.pentaho.com/pba-report-designer/attributes-reference-cp-prd/index.md

# Index

The following attributes belong to the **index** property:

| Attribute Name      | Purpose                                                                                                                               | Values                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **data-field**      | Defines the field to be used as the **item-data** or **item-key**.                                                                    | Any column field or function                                                     |
| **data-formula**    | Defines an open formula to be used as the **item-data** or **item-key**.                                                              | Formula Make sure that **data-field** is not defined, if this attribute is used. |
| **index-separator** | Defines the separator text that is used between page numbers in the **item-pages** field in the index sub report. It defaults to ",". | String; default is comma (,).                                                    |
| **condensed-style** | Defines whether or not a dash (-) is used between continuous page numbers; for example, `4,5,6,7` display as `4-7`.                   | Boolean; default is false.                                                       |
