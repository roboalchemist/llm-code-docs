# Source: https://documentation.onesignal.com/docs/en/integrations.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrations overview

> Connect OneSignal to third-party platforms, sync data with analytics tools, and automate messaging workflows.

OneSignal integrates with a wide range of platforms—from data warehouses and CRMs to analytics and automation tools.

Explore the [full integrations catalog](https://onesignal.com/integrations) or [become a partner](https://onesignal.com/contact-partners). To build your own integration, follow the [partner integration guide](./building-an-integration-with-onesignal-partner-guide).

<Note>
  Need something custom? You can [connect to any database, DMP, or CRM](./database-dmp-crm-integration).

  Looking for webhooks? See [Event Streams](./event-streams) for real-time message events or [Journey webhooks](./journeys-webhook) for user-specific automation.
</Note>

## How to choose an integration

| Goal                                                          | Section                                              |
| ------------------------------------------------------------- | ---------------------------------------------------- |
| Full bidirectional sync (events, audiences, and message data) | [Featured integrations](#featured-integrations)      |
| Send custom events or audience data **into** OneSignal        | [Inbound](#inbound-to-onesignal)                     |
| Export message event data **from** OneSignal                  | [Outbound](#outbound-from-onesignal)                 |
| Track attribution, purchases, or enrich user profiles         | [Attribution & enrichment](#attribution--enrichment) |
| Trigger messages from external workflow tools                 | [Automation](#automation)                            |
| Build apps with native OneSignal support                      | [App creation](#app-creation)                        |

***

## Featured integrations

These integrations support full bidirectional data sync:

* Import custom events into OneSignal
* Sync audience cohorts with OneSignal
* Export message events from OneSignal

<Columns cols={2}>
  <Card title="Mixpanel" icon="chart-mixed" href="./mixpanel">
    Sync cohorts, export message events, and import custom events between Mixpanel and OneSignal.
  </Card>

  <Card title="Amplitude" icon="chart-line" href="./amplitude">
    Sync cohorts, export message events, and import custom events between Amplitude and OneSignal.
  </Card>

  <Card title="Twilio Segment" icon="share-nodes" href="./segment-onesignal-integration">
    Route events, traits, and audiences between Segment and OneSignal in both directions.
  </Card>

  <Card title="HubSpot" icon="address-book" href="./hubspot">
    Trigger messages, create and update users, and sync audience data via HubSpot workflows.
  </Card>
</Columns>

***

## Inbound (to OneSignal)

Import audience data, tags, and custom events from external platforms into OneSignal.

<Tip>
  [Amplitude](./amplitude), [HubSpot](./hubspot), [Mixpanel](./mixpanel), and [Twilio Segment](./segment-onesignal-integration) also support inbound data sync. See [Featured integrations](#featured-integrations).
</Tip>

<Card title="Adobe Audience Manager" icon="users" href="./adobe-audience-manager">
  Import audience segments from Adobe Audience Manager into OneSignal.
</Card>

### Custom event sources

Connect databases, data warehouses, and streaming platforms to import custom events into OneSignal.

<Columns cols={3}>
  <Card title="AlloyDB" icon="database" href="./alloydb">
    Import custom events from your AlloyDB database.
  </Card>

  <Card title="Amazon Athena" icon="database" href="./amazon-athena">
    Query and import custom events from Amazon Athena.
  </Card>

  <Card title="Amazon S3" icon="box-archive" href="./s3">
    Import custom events from S3 buckets.
  </Card>

  <Card title="Apache Kafka" icon="bolt" href="./kafka">
    Stream custom events from Kafka topics.
  </Card>

  <Card title="AWS Redshift" icon="database" href="./amazon-redshift">
    Import custom events from your Redshift data warehouse.
  </Card>

  <Card title="Azure Synapse" icon="database" href="./azure-synapse">
    Import custom events from Azure Synapse Analytics.
  </Card>

  <Card title="ClickHouse" icon="database" href="./clickhouse">
    Import custom events from your ClickHouse database.
  </Card>

  <Card title="Confluent Cloud" icon="bolt" href="./confluent-cloud">
    Stream custom events from Confluent Cloud.
  </Card>

  <Card title="Databricks" icon="cubes" href="./databricks">
    Import custom events from Databricks lakehouses.
  </Card>

  <Card title="Elasticsearch" icon="magnifying-glass" href="./elasticsearch">
    Import custom events from Elasticsearch indices.
  </Card>

  <Card title="Google BigQuery" icon="database" href="./bigquery">
    Import custom events from BigQuery datasets.
  </Card>

  <Card title="Google Cloud SQL" icon="database" href="./google-cloud-sql">
    Import custom events from Cloud SQL instances.
  </Card>

  <Card title="Google Pub/Sub" icon="bolt" href="./google-pubsub">
    Stream custom events from Pub/Sub topics.
  </Card>

  <Card title="Google Sheets" icon="table" href="./google-sheets">
    Import custom events from Google Sheets spreadsheets.
  </Card>

  <Card title="Greenplum" icon="database" href="./greenplum">
    Import custom events from your Greenplum database.
  </Card>

  <Card title="Materialize" icon="database" href="./materialize">
    Import custom events from Materialize streaming views.
  </Card>

  <Card title="Microsoft Fabric" icon="database" href="./microsoft-fabric">
    Import custom events from Microsoft Fabric lakehouses.
  </Card>

  <Card title="MotherDuck" icon="database" href="./motherduck">
    Import custom events from your MotherDuck database.
  </Card>

  <Card title="MySQL" icon="database" href="./mysql">
    Import custom events from your MySQL database.
  </Card>

  <Card title="PostgreSQL" icon="database" href="./postgresql">
    Import custom events from your PostgreSQL database.
  </Card>

  <Card title="SingleStore" icon="database" href="./singlestore">
    Import custom events from your SingleStore database.
  </Card>

  <Card title="Snowflake" icon="snowflake" href="./snowflake">
    Import custom events from your Snowflake warehouse.
  </Card>

  <Card title="SQL Server" icon="database" href="./sql-server">
    Import custom events from your SQL Server database.
  </Card>

  <Card title="Starburst Enterprise" icon="star" href="./starburst-enterprise">
    Import custom events via Starburst Enterprise queries.
  </Card>

  <Card title="Starburst Galaxy" icon="star" href="./starburst-galaxy">
    Import custom events via Starburst Galaxy queries.
  </Card>

  <Card title="Trino" icon="database" href="./trino">
    Import custom events via Trino queries.
  </Card>
</Columns>

***

## Outbound (from OneSignal)

Export message event data from OneSignal to analytics or storage platforms.

<Tip>
  [Amplitude](./amplitude), [Mixpanel](./mixpanel), and [Twilio Segment](./segment-onesignal-integration) also support outbound message event sync. See [Featured integrations](#featured-integrations).
</Tip>

<Columns cols={2}>
  <Card title="Databricks" icon="cubes" href="./databricks">
    Export message events to Databricks lakehouses.
  </Card>

  <Card title="Google BigQuery" icon="database" href="./bigquery">
    Export message events to BigQuery datasets.
  </Card>

  <Card title="Snowflake" icon="snowflake" href="./snowflake">
    Export message events to your Snowflake warehouse.
  </Card>
</Columns>

***

## Attribution & enrichment

Track in-app purchases, attribution, and user traits to enrich subscriber profiles.

<Columns cols={2}>
  <Card title="Adjust" icon="sliders" href="./adjust">
    Sync mobile attribution data with OneSignal.
  </Card>

  <Card title="AppsFlyer" icon="paper-plane" href="https://support.appsflyer.com/hc/en-us/articles/360015926437">
    Sync mobile attribution data from AppsFlyer.
  </Card>

  <Card title="BlueConic" icon="users" href="./blueconic">
    Import audience profiles and segments from BlueConic.
  </Card>

  <Card title="HubSpot" icon="address-book" href="./hubspot">
    Import contact properties and audience data from HubSpot.
  </Card>

  <Card title="RevenueCat" icon="credit-card" href="./revenuecat">
    Sync in-app subscription and purchase data from RevenueCat.
  </Card>
</Columns>

***

## Automation

Trigger push messages and update users from external automation platforms.

<Columns cols={2}>
  <Card title="ActiveCampaign" icon="gears" href="./activecampaign">
    Trigger OneSignal messages from the ActiveCampaign automation canvas.
  </Card>

  <Card title="HubSpot" icon="address-book" href="./hubspot">
    Send messages and update users via HubSpot workflows.
  </Card>
</Columns>

***

## App creation

Build apps with native OneSignal push notification support.

<Columns cols={2}>
  <Card title="FlutterFlow" icon="mobile-screen-button" href="./flutterflow-sdk-setup">
    Build Flutter apps with drag-and-drop and native OneSignal push.
  </Card>

  <Card title="Median" icon="mobile-screen-button" href="https://median.co/docs/onesignal">
    Convert websites into native mobile apps with OneSignal push notifications.
  </Card>

  <Card title="Andromo" icon="mobile-screen-button" href="https://www.andromo.com/docs/setting-up-onesignal-notifications-on-your-andromo-powered-android-app/">
    Build Android apps with Andromo and enable OneSignal push notifications.
  </Card>

  <Card title="Retool" icon="screwdriver-wrench" href="https://docs.retool.com/docs/onesignal-integration">
    Build internal tools with Retool and trigger OneSignal messages.
  </Card>
</Columns>

Built with [Mintlify](https://mintlify.com).
