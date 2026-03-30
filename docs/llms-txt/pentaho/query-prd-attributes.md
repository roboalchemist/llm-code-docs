# Source: https://docs.pentaho.com/pba-report-designer/attributes-reference-cp-prd/query-prd-attributes.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/attributes-reference-cp-prd/query-prd-attributes.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/attributes-reference-cp-prd/query-prd-attributes.md

# Query

The following attributes belong to the **query** property:

| Attribute Name      | Purpose                                                                                                                                       | Values                                                        |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **name**            | Assigns a name to the selected query. If you are using a JDBC Custom data source, you can type the entire query directly into the name field. | String; no default value.                                     |
| **row-limit**       | Row limit for the query.                                                                                                                      | Integer; default value is -1, meaning there is no hard limit. |
| **time-out**        | Timeout limit for the query.                                                                                                                  | Integer; default value is 0, meaning there is no timeout.     |
| **design-time-out** | Timeout limit when running from Report Designer.                                                                                              | Integer; default value is 0, meaning there is no timeout.     |
