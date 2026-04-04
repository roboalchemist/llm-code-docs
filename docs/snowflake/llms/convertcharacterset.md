# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/convertcharacterset.md

# ConvertCharacterSet 2025.10.9.21

## Bundle

org.apache.nifi | nifi-standard-nar

## Description

Converts a FlowFile’s content from one character set to another

## Tags

character set, characterset, convert, text

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Input Character Set | The name of the CharacterSet to expect for Input |
| Output Character Set | The name of the CharacterSet to convert to |

## Relationships

| Name | Description |
| --- | --- |
| success |  |
