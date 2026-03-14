# Source: https://docs.airbyte.com/release_notes/april_2023.md

# April 2023

Copy Page

## [airbyte v0.43.0](https://github.com/airbytehq/airbyte/releases/tag/v0.43.0) to [v0.44.3](https://github.com/airbytehq/airbyte/releases/tag/v0.44.3)[​](#airbyte-v0430-to-v0443 "Direct link to airbyte-v0430-to-v0443")

This page includes new features and improvements to the Airbyte Cloud and Airbyte Open Source platforms.

## **✨ New and improved features**[​](#new-and-improved-features "Direct link to new-and-improved-features")

* **New Sources and Promotions**

  * 🎉 New Destination: SelectDB ([#20881](https://github.com/airbytehq/airbyte/pull/20881))
  * 🎉 Source Intercom: migrate from Python CDK to Declarative YAML (Low Code) ([#23013](https://github.com/airbytehq/airbyte/pull/23013))
  * 🎉 New Source: Azure Blob Storage (publish) ([#24767](https://github.com/airbytehq/airbyte/pull/24767))

* **New Features for Existing Connectors**

  * 🎉 Source TikTok Marketing - Add country\_code and platform audience reports ([#22134](https://github.com/airbytehq/airbyte/pull/22134))
  * 🎉 Source Orb: Add invoices incremental stream ([#24737](https://github.com/airbytehq/airbyte/pull/24737))
  * 🎉 Source Sentry: add stream `releases` ([#24768](https://github.com/airbytehq/airbyte/pull/24768))
  * Source Klaviyo: adds stream Templates ([#23236](https://github.com/airbytehq/airbyte/pull/23236))
  * Source Hubspot: new stream Email Subscriptions ([#22910](https://github.com/airbytehq/airbyte/pull/22910))

* **New Features in Airbyte Platform**

  * 🎉 Connector builder: Add transformations (#5630)
  * 🎉 Display per-stream error messages on stream-centric status page (#5793)
  * 🎉 Validate security of OSS installations on setup (#5583)
  * 🎉 Connector builder: Set default schema (#5813)
  * 🎉 Connector builder error handler (#5637)
  * 🎉 Connector builder: Create user input in new stream modal (#5812)
  * 🎉 Connector builder: Better UI for cursor pagination (#6083)
  * 🎉 Connector builder: User configurable list for list partition router (#6076)
  * 🎉 Stream status page updates (#6099)
  * 🎉 Connector builder: Better form for incremental sync (#6003)
  * 🎉 Connector builder: Allow importing manifests with parameters in authenticator (#6213)

## **🐛 Bug fixes**[​](#-bug-fixes "Direct link to -bug-fixes")

* 🐛 Source Zendesk Chat: fix remove too high min/max. definition [#23833](https://github.com/airbytehq/airbyte/issues/23833) 🚨 ([#24190](https://github.com/airbytehq/airbyte/pull/24190))
* 🐛 Disable Sync buttons for disabled connections (#5622)
* 🐛 Connector builder: Fix duration suggestion (#5857)
* 🐛 Connector builder: Prevent read request with wrong / missing stream name (#5939)
* 🐛 Fix query parameters in APIs (#5882)
* 🐛 Date picker: Avoid time column text overflow (#6210)
* 🐛 Connector Builder: avoid crash when loading builder if there is already data (#6155)
* 🐛 Connector builder: Allow changing user input key (#6167)
