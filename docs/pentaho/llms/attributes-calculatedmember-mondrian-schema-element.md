# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/about-multidimensional-expression-language/mondrian-schema-element-reference/calculatedmember/attributes-calculatedmember-mondrian-schema-element.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/about-multidimensional-expression-language/mondrian-schema-element-reference/calculatedmember/attributes-calculatedmember-mondrian-schema-element.md

# Attributes

| Attribute    | Data Type | Definition                                                                                                                                                                   |
| ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name         | String    | Name of this calculated member                                                                                                                                               |
| formatString | String    | Format string with which to format cells of this member. See the **Format** class under **mondrian.util** in <https://mondrian.pentaho.com/api/index.html> for more details. |
| caption      | String    | A string being displayed instead of the name. Can be localized from Properties file using **#{propertyname}**.                                                               |
| description  | String    | Description of this calculated member. Can be localized from Properties file using **#{propertyname}**.                                                                      |
| formula      | String    | MDX expression which gives the value of this member. Equivalent to the Formula sub-element.                                                                                  |
| dimension    | String    | Name of the dimension which this member belongs to                                                                                                                           |
| hierarchy    | String    | Name of the hierarchy that this member belongs to                                                                                                                            |
| parent       | String    | Fully-qualified name of the parent member. If not specified, the member will be at the lowest level (besides the 'all' level) in the hierarchy.                              |
| visible      | Boolean   | Whether this member is visible in the user-interface. Default true.                                                                                                          |
