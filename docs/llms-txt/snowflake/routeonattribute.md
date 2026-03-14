# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/routeonattribute.md

# RouteOnAttribute 2025.10.9.21

## Bundle

org.apache.nifi | nifi-standard-nar

## Description

Routes FlowFiles based on their Attributes using the Attribute Expression Language

## Tags

Attribute Expression Language, Expression Language, Regular Expression, attributes, detect, filter, find, regex, regexp, routing, search, string, text

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Routing Strategy | Specifies how to determine which relationship to use when evaluating the Expression Language |

## Relationships

| Name | Description |
| --- | --- |
| unmatched | FlowFiles that do not match any user-define expression will be routed here |

## Writes attributes

| Name | Description |
| --- | --- |
| RouteOnAttribute.Route | The relation to which the FlowFile was routed |

## Use cases

|  |
| --- |
| Route data to one or more relationships based on its attributes using the NiFi Expression Language. |
| Keep data only if its attributes meet some criteria, such as its filename ends with .txt. |
| Discard or drop a file based on attributes, such as filename. |

## Use Cases Involving Other Components

|  |
| --- |
| Route record-oriented data based on whether or not the record’s values meet some criteria |
