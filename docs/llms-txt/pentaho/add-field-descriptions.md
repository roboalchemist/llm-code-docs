# Source: https://docs.pentaho.com/pba-schema-workbench/work-with-mondrian-schema/add-field-descriptions.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/work-with-mondrian-schema/add-field-descriptions.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/work-with-mondrian-schema/add-field-descriptions.md

# Add field descriptions

By adding description attributes to your Mondrian schema elements, you can enable tooltip (mouse-over) field descriptions in Analyzer reports.

```
<Level name="Store Country" column="store_country" uniqueMembers="true" caption="%{foodmart.dimension.store.country.caption}" 
            description="%{foodmart.dimension.store.country.description}"/>
```

**CAUTION:**

Remove the line-wrap or this may not work. These variables will not work unless you localize schemas.

This attribute can be set on the following schema elements:

* Level
* Measure
* CalculatedMember
