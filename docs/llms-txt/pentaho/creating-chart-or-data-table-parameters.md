# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/set-dashboard-parameters/creating-chart-or-data-table-parameters.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/set-dashboard-parameters/creating-chart-or-data-table-parameters.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/set-dashboard-parameters/creating-chart-or-data-table-parameters.md

# Creating chart or data table parameters

To create a parameter, in the **Value** field, enter the name of the parameter inside curly braces, as in `{Parameter Name}`. In the example below, the designer created a parameter called **{TERRITORY}**; the default value, or source, for the parameter is NA (North America). When a chart or data table renders, it displays data associated with North America. Remember that this a default value. When you enclose a parameter name with curly braces, you are creating a parameter query, which means that users can change the query dynamically by replacing the default value NA with a different territory acronym, (for example, EMEA), when the query runs.

![Filter parameter example](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-d35f088aa6ea478feea88c1b8f7eeacc6dfde2a8%2FPDD_filterparm_sample_ONYX.png?alt=media)

You can define multiple default parameter values by adding a pipe character (|) between the values, as in `NA|EMEA|APAC`.

Suppose a dashboard designer chooses to limit the data to North America (NA) exclusively? In this instance, he or she would not include the curly braces around NA (as shown in the example below), and **Default** (value) is disabled. This is an example of a static query.

![Static query](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-9c5d8d9cc2f4caec0cb78f2408ca5d26e07a8be2%2FPDD_filterparm2_sample_ONYX.png?alt=media)
