# Source: https://docs.pentaho.com/pba-schema-workbench/work-with-mondrian-schema/add-business-groups.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/work-with-mondrian-schema/add-business-groups.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/work-with-mondrian-schema/add-business-groups.md

# Add business groups

The available fields list in Analyzer organizes fields in folders according to the **AnalyzerBusinessGroup** annotation. To implement business groups, add these annotations to your member definitions appropriately. If no annotation is specified, then the group defaults to Measures for measures and the hierarchy name/caption for attributes.

Below is an example that puts Years, Quarters and Months into a Time Periods business group:

```
...
<Level name="Years" ... >
   <Annotations><Annotation name="AnalyzerBusinessGroup">Time Periods</Annotation></Annotations>
</Level>
<Level name="Quarters" ... >
   <Annotations><Annotation name="AnalyzerBusinessGroup">Time Periods</Annotation></Annotations>
</Level>
<Level name="Months" ... >
   <Annotations><Annotation name="AnalyzerBusinessGroup">Time Periods</Annotation></Annotations>
</Level>
...
```

The **AnalyzerBusinessGroup** annotation is supported on the following schema elements:

* Level
* Measure
* CalculatedMember
* VirtualCubeMeasure
