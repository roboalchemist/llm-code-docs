# Source: https://docs.airbyte.com/release_notes/march_2023.md

# March 2023

Copy Page

## [airbyte v0.42.0](https://github.com/airbytehq/airbyte/releases/tag/v0.42.0) to [v0.42.1](https://github.com/airbytehq/airbyte/releases/tag/v0.42.1)[​](#airbyte-v0420-to-v0421 "Direct link to airbyte-v0420-to-v0421")

This page includes new features and improvements to the Airbyte Cloud and Airbyte Open Source platforms.

## **✨ New and improved features**[​](#new-and-improved-features "Direct link to new-and-improved-features")

* **New Sources and Promotions**

  * 🎉 New Source: [Unleash](https://docs.airbyte.com/integrations/sources/unleash) \[low-code CDK] ([#19923](https://github.com/airbytehq/airbyte/pull/19923))
  * 🎉 Source [Twitter](https://docs.airbyte.com/integrations/sources/twitter): to Alpha and in Cloud ([#23832](https://github.com/airbytehq/airbyte/pull/23832))
  * 🎉 Source [Confluence](https://docs.airbyte.com/integrations/sources/confluence): Enabled in cloud and now in Beta ([#23775](https://github.com/airbytehq/airbyte/pull/23775))
  * 🎉 Source [Airtable](https://docs.airbyte.com/integrations/sources/airtable): to GA ([#23763](https://github.com/airbytehq/airbyte/pull/23763))
  * 🎉 Source [Paystack](https://docs.airbyte.com/integrations/sources/paystack): in Cloud
  * 🎉 Source [Google Analytics 4](https://docs.airbyte.com/integrations/sources/google-analytics-data-api): to GA
  * 🎉 Source [Strava](https://docs.airbyte.com/integrations/sources/strava): to Beta
  * 🎉 Source [GCS](https://docs.airbyte.com/integrations/sources/gcs): in Cloud
  * 🎉 Source [ZohoCRM](https://docs.airbyte.com/integrations/sources/zoho-crm): to Alpha and in Cloud
  * 🎉 Source [Yandex Metrica](https://docs.airbyte.com/integrations/sources/yandex-metrica): to Beta and in Cloud
  * 🎉 Source [Salesloft](https://docs.airbyte.com/integrations/sources/salesloft/): to Alpha and in Cloud
  * 🎉 Source [Xero](https://docs.airbyte.com/integrations/sources/xero/): to Beta and in Cloud
  * 🎉 Source [Trello](https://docs.airbyte.com/integrations/sources/trello/): to Beta
  * 🎉 Source [Paystack](https://docs.airbyte.com/integrations/sources/paystack/): to Beta and in Cloud
  * 🎉 Source Trustpilot: in Cloud
  * 🎉 Source [LinkedIn Pages](https://docs.airbyte.com/integrations/sources/linkedin-pages): in Cloud
  * 🎉 Source [Pipedrive](https://docs.airbyte.com/integrations/sources/pipedrive): to Beta and in Cloud ([#23539](https://github.com/airbytehq/airbyte/pull/23539))
  * 🎉 Source [Chargebee](https://docs.airbyte.com/integrations/sources/chargebee): Migrate to YAML ([#21688](https://github.com/airbytehq/airbyte/pull/21688))

* **New Features for Existing Connectors**

  * Redshift Destination: Add SSH Tunnelling Config Option ([#23523](https://github.com/airbytehq/airbyte/pull/23523))
  * 🎉 Source Amazon Seller Partner - Implement reportOptions for all missing reports ([#23606](https://github.com/airbytehq/airbyte/pull/23606))
  * Source Tiktok: allow to filter advertiser in reports ([#23377](https://github.com/airbytehq/airbyte/pull/23377))
  * 🎉 Source Github - added user friendly messages, added AirbyteTracedException config\_error ([#23467](https://github.com/airbytehq/airbyte/pull/23467))
  * 🎉 Destination Weaviate: Support any string based ID and fix issues with additionalProperties ([#22527](https://github.com/airbytehq/airbyte/pull/22527))

* **New Features in Airbyte Platform**

  * 🎉 octavia-cli: add pypi package workflow ([#22654](https://github.com/airbytehq/airbyte/pull/22654))
  * 🪟🎉 Connector builder projects UI (#4774)
  * 🎉 Add stream syncing or resetting state to rows (#5364)

## **🐛 Bug fixes**[​](#-bug-fixes "Direct link to -bug-fixes")

* 🐛 Source Delighted: fix `Date Since`  date-format bug in UI ([#23909](https://github.com/airbytehq/airbyte/pull/23909))
* 🐛 Source Iterable: add retry for 500 - Generic Error, increase `reduce slice max attempts`  ([#23821](https://github.com/airbytehq/airbyte/pull/23821))
* 🐛 Source S3: Make `Advanced Reader Options`and `Advanced Options`truly `Optional`([#23669](https://github.com/airbytehq/airbyte/pull/23669))
* Source Jira: Small fix in the board stream ([#21524](https://github.com/airbytehq/airbyte/pull/21524))
* 🐛 Source Sentry: fix `None` state\_value + other bad `state_values` ([#23619](https://github.com/airbytehq/airbyte/pull/23619))
* 🐛 Source Pinterest: fix for `HTTP - 400 Bad Request`  when requesting data >= 90 days. ([#23649](https://github.com/airbytehq/airbyte/pull/23649))
* 🐛 Source Fauna: fix bug during discover step ([#23583](https://github.com/airbytehq/airbyte/pull/23583))
* 🐛 Prevent crash on copying malformed manifest into yaml editor (#5391)
