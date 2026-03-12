# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/understanding-data-cubes.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/understanding-data-cubes.md

# Understanding data cubes

Another name for a dimensional model is a cube. Each cube represents one fact table and several dimensional tables. This model should be useful for reporting and analysis on the subject of the data in the fact table. However, if you want to cross-reference this data with another cube (if you need to analyze data across two or more cubes, or need to combine information from two fact tables on the same subject but with different granularity) then you must create a virtual cube. The XML elements that compose a virtual cube are explained in detail below.

**Note:** Virtual cubes cannot presently be created through Pentaho Data Integration's model perspective; you must use Schema Workbench instead.

The **\<CubeUsages>** element specifies the cubes that are imported into the virtual cube. It holds **\<CubeUsage>** elements.

The **\<CubeUsage>** element specifies the base cube that is imported into the virtual cube. Alternatively you can define a **\<VirtualCubeMeasure>** and use similar imports from the base cube without defining a **\<CubeUsage>**.The `cubeName` attribute specifies the name of the base cube. The `ignoreUnrelatedDimensions` attribute determines whether or not the measures from this base cube will have non-joining dimension members pushed to the top level member. This attribute is false by default because it is still experimental.

The **\<VirtualCubeDimension>** element imports a dimension from one of the constituent cubes. If you do not specify the `cubeName` attribute, this means you are importing a shared dimension.

**Note:** If a shared dimension is used more than once in a cube, there is no way to determine which usage of the shared dimension you intend to import.

The **\<VirtualCubeMeasure>** element imports a measure from one of the constituent cubes. It is imported with the same name. If you want to create a formula or rename a measure as you import it, use the **\<CalculatedMember>** element instead.

Virtual cubes are useful for situations where there are fact tables of different granularities (for instance, one Time fact table might be configured on a Day level, another at the Month level), or fact tables of different dimensionalities (for instance one on Products, Time and Customer, another on Products, Time and Warehouse), and you need to present the results to users who don't know how the data is structured.

Any common dimensions, shared dimensions which are used by both constituent cubes, are automatically synchronized. In this example, `[Time]` and `[Products]` are common dimensions. So if the context is (`[Time].[2005].[Q2], [Products].[Productname].[P-51-D Mustang]`), measures from either cube will relate to this context.

Dimensions which only belong to one cube are called non-conforming dimensions. The `[Gender]` dimension is an example of this; it exists in the Sales cube, but not Warehouse. If the context is (`[Gender].[F], [Time].[2005].[Q1]`), it makes sense to ask the value of the `[Unit Sales]` measure (which comes from the `[Sales]` cube) but not the `[Units Ordered]` measure (from `[Warehouse]`). In the context of `[Gender].[F], [Units Ordered]` has value `NULL`.
