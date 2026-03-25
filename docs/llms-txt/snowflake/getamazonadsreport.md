# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getamazonadsreport.md

# GetAmazonAdsReport 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-amazon-ads-processors-nar

## Description

Processor downloading report from Amazon Ads if ready.

## Tags

Amazon, Amazon Ads, report

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Access Token Provider | Service providing OAuth access token. |
| Amazon Advertising Client ID | Client ID of the Amazon Advertising user. |
| Region | Environment from which advertising data will be downloaded. |
| Report ID | ID of the generated report. |
| Report Profile ID | The profile ID associated with an advertising account in a specific marketplace. |
| Web Client Service Provider | Service providing client for REST request execution. |

## Relationships

| Name | Description |
| --- | --- |
| failure | Error FlowFiles transferred when receiving error response from Amazon Ads Reporting API or when an error occurred during response processing. |
| retry | Response FlowFiles transferred when report prepared by Amazon Ads Reporting API is not yet ready to be downloaded. |
| success | Response FlowFiles transferred when receiving COMPLETED response from Amazon Ads Reporting API. |

## Writes attributes

| Name | Description |
| --- | --- |
| mime.type | Mime type of the returned report. |
