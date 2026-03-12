# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/generatejson.md

# GenerateJSON 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-record-generation-nar

## Description

Produces a batch of JSON Objects with random field values based on a configurable JSON Schema.

## Tags

JSON, JSON Schema, generate, random

## Input Requirement

FORBIDDEN

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Batch Size | Number of records generated per FlowFile produced |
| JSON Schema | JSON Schema version 2020-12 describing an object with properties indicating type and format for each field |
| Output Structure | Structure for writing batches of records to each FlowFile |

## Relationships

| Name | Description |
| --- | --- |
| success | FlowFiles with generated JSON records |
