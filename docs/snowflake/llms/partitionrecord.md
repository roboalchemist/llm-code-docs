# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/partitionrecord.md

# PartitionRecord 2025.10.9.21

## Bundle

org.apache.nifi | nifi-standard-nar

## Description

Splits, or partitions, record-oriented data based on the configured fields in the data. One or more properties must be added. The name of the property is the name of an attribute to add. The value of the property is a RecordPath to evaluate against each Record. Two records will go to the same outbound FlowFile only if they have the same value for each of the given RecordPaths. Because we know that all records in a given output FlowFile have the same value for the fields that are specified by the RecordPath, an attribute is added for each field. See Additional Details on the Usage page for more information and examples.

## Tags

bin, group, organize, partition, record, recordpath, rpath, segment, split

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| record-reader | Specifies the Controller Service to use for reading incoming data |
| record-writer | Specifies the Controller Service to use for writing out the records |

## Relationships

| Name | Description |
| --- | --- |
| failure | If a FlowFile cannot be partitioned from the configured input format to the configured output format, the unchanged FlowFile will be routed to this relationship |
| original | Once all records in an incoming FlowFile have been partitioned, the original FlowFile is routed to this relationship. |
| success | FlowFiles that are successfully partitioned will be routed to this relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| record.count | The number of records in an outgoing FlowFile |
| mime.type | The MIME Type that the configured Record Writer indicates is appropriate |
| fragment.identifier | All partitioned FlowFiles produced from the same parent FlowFile will have the same randomly generated UUID added for this attribute |
| fragment.index | A one-up number that indicates the ordering of the partitioned FlowFiles that were created from a single parent FlowFile |
| fragment.count | The number of partitioned FlowFiles generated from the parent FlowFile |
| segment.original.filename | The filename of the parent FlowFile |
| <dynamic property name> | For each dynamic property that is added, an attribute may be added to the FlowFile. See the description for Dynamic Properties for more information. |

## Use cases

|  |
| --- |
| Separate records into separate FlowFiles so that all of the records in a FlowFile have the same value for a given field or set of fields. |
| Separate records based on whether or not they adhere to a specific criteria |

## See also

* [org.apache.nifi.processors.standard.ConvertRecord](convertrecord.md)
* [org.apache.nifi.processors.standard.QueryRecord](queryrecord.md)
* [org.apache.nifi.processors.standard.SplitRecord](splitrecord.md)
* [org.apache.nifi.processors.standard.UpdateRecord](updaterecord.md)
