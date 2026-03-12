# Source: https://docs.pentaho.com/pba-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-4-add-geo-map-support-to-a-mondrian-schema.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-4-add-geo-map-support-to-a-mondrian-schema.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-4-add-geo-map-support-to-a-mondrian-schema.md

# Step 4: Add Geo Map support to a Mondrian schema

The Geo Map visualization in Analyzer requires both a Geo Service that provides coordinate data (delivered through a Pentaho Server Pentaho-geo plugin), and special Mondrian schema annotations and member properties.

Only the levels marked with Geographical roles (via annotations) can be added to a Geo Map visualization in Analyzer. During the rendering process, the visualization will call the Pentaho-geo plugin in the Pentaho Server to look up coordinates that correspond with the level.

## Annotations

First, find all levels that describe location data, then add the appropriate annotations as shown and explained below:

```
<Level name="CITY" column="CITY" type="String" uniqueMembers="false">
  <Annotations>
    <Annotation name="Data.Role">Geography</Annotation>
    <Annotation name="Geo.Role">city</Annotation>
  </Annotations>
</Level>
```

**Data.Role**: Indicates the type of level. Presently, the only valid data role type is Geography.

**Geo.Role**: Specifies the geographical classification (city, state, zip, etc.). While there are built-in types used in the Data Source Wizard and PDI modelers, the values are arbitrary. You could specify a "city" type and, as long as the service provides data for this classification, it will work.

**Note:** In the above example, the city role retrieves centroid coordinates.

## Member properties

In addition to retrieving coordinates from the Geo Service, the location **Geo.Role** value defines a level with member properties supplying latitude and longitude values. Levels that are tagged with location must also provide two member properties with the exact names of Latitude and Longitude that point to the column in the database which contains these values for the level.

```
<Level name="LatTest" column="CUSTOMERNUMBER" type="Numeric" uniqueMembers="false">
  <Annotations>
    <Annotation name="Data.Role">Geography</Annotation>
    <Annotation name="Geo.Role">location</Annotation>
  </Annotations>
  <Property name="Latitude" column="CUSTLAT" type="Numeric" />
  <Property name="Longitude" column="CUSTLON" type="Numeric"/>
</Level>
```
