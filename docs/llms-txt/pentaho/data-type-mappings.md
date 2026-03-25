# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/data-type-mappings.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/understanding-pdi-data-types-and-field-metadata/data-type-mappings.md

# Data type mappings

PDI data types map internally to Java data types, so the Java behavior of these data types applies to the associated fields, parameters, and variables used in your transformations and jobs. The following table describes these mappings.

| PDI data type    | Java data type | Description                                                                   |
| ---------------- | -------------- | ----------------------------------------------------------------------------- |
| BigNumber        | BigDecimal     | An arbitrary unlimited precision number.                                      |
| Binary           | Byte\[]        | An array of bytes that contain any type of binary data.                       |
| Boolean          | Boolean        | A boolean value `true` or `false.`                                            |
| Date             | Date           | A date-time value with millisecond precision.                                 |
| Integer          | Long           | A signed long 64-bit integer.                                                 |
| Internet Address | InetAddress    | An Internet Protocol (IP) address.                                            |
| Number           | Double         | A double precision floating point value.                                      |
| String           | String         | A variable unlimited length text encoded in UTF-8 (Unicode).                  |
| Timestamp        | Timestamp      | Allows the specification of fractional seconds to a precision of nanoseconds. |
