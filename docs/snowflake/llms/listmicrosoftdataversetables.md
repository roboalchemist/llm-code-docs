# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/listmicrosoftdataversetables.md

# ListMicrosoftDataverseTables 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-dataverse-processors-nar

## Description

List Tables from Microsoft Dataverse environments

## Tags

dataverse

## Input Requirement

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Environment URL | URL to Microsoft Dataverse Environment |
| OAuth2 Access Token Provider | Enables managed retrieval of OAuth2 Bearer Token. |
| Tables Filter Strategy | List of table names. Output will be limited to those names if defined. |
| Tables Filter Value | Value of Table Names filter. It is regexp or separated list, depending on selected filtering strategy. |
| Web Client Service Provider | Creates instance of web client. |

## Relationships

| Name | Description |
| --- | --- |
| failure | FlowFile with errors occurred while fetching from Dataverse. |
| success | FlowFile with listed tables from Dataverse. |
