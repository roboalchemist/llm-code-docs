# Source: https://clickhouse.ferndocs.com/integrations/mitzu.md

---
sidebar_label: Mitzu
slug: /integrations/mitzu
keywords:

- clickhouse
- Mitzu
- connect
- integrate
- ui
description: Mitzu is a no-code warehouse-native product analytics application.
title: Connecting Mitzu to ClickHouse
doc_type: guide
integration:
- support_level: partner
- category: data_visualization

---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

Mitzu is a no-code, warehouse-native product analytics application. Similar to tools like Amplitude, Mixpanel, and PostHog, Mitzu empowers users to analyze product usage data without requiring SQL or Python expertise.

However, unlike these platforms, Mitzu does not duplicate the company's product usage data. Instead, it generates native SQL queries directly on the company's existing data warehouse or lake.

## Goal [#goal]

In this guide, we are going to cover the following:

- Warehouse-native product analytics
- How to integrate Mitzu to ClickHouse

<Tip title="Example datasets">
If you do not have a data set to use for Mitzu, you can work with NYC Taxi Data.
This dataset is available in ClickHouse Cloud or [can be loaded with these instructions](/getting-started/example-datasets/nyc-taxi).
</Tip>

This guide is just a brief overview of how to use Mitzu. You can find more detailed information in the [Mitzu documentation](https://docs.mitzu.io/).

## 1. Gather your connection details [#1-gather-your-connection-details]

<ConnectionDetails />

## 2. Sign in or sign up to Mitzu [#2-sign-in-or-sign-up-to-mitzu]

As a first step, head to [https://app.mitzu.io](https://app.mitzu.io) to sign up.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/458644788ab590fc9601905d343b4dbb402e2c7b3b996ba384e8235f4e41f933/images/integrations/data-visualization/mitzu_01.png" alt="Mitzu sign-in page with email and password fields" />

## 3. Configure your workspace [#3-configure-your-workspace]

After creating an organization, follow the `Set up your workspace` onboarding guide in the left sidebar. Then, click on the `Connect Mitzu with your data warehouse` link.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5ac09c04525325b0fcec3e3903628fb8cf19253afdd48c1bc0ebe38cfcbef621/images/integrations/data-visualization/mitzu_02.png" alt="Mitzu workspace setup page showing onboarding steps" />

## 4. Connect Mitzu to ClickHouse [#4-connect-mitzu-to-clickhouse]

First, select ClickHouse as the connection type and set the connection details. Then, click the `Test connection & Save` button to save the settings.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/97d2701c1090b7ce82828673af6c45b75d5ea5856601bf5f18b3be268e8dba74/images/integrations/data-visualization/mitzu_03.png" alt="Mitzu connection setup page for ClickHouse with configuration form" />

## 5. Configure event tables [#5-configure-event-tables]

Once the connection is saved, select the `Event tables` tab and click the `Add table` button. In the modal, select your database and the tables you want to add to Mitzu.

Use the checkboxes to select at least one table and click on the `Configure table` button. This will open a modal window where you can set the key columns for each table.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c1d82602afd50f6f76d63709dd06ad6adc24569d6ca121935774204749386006/images/integrations/data-visualization/mitzu_04.png" alt="Mitzu table selection interface showing database tables" />
<br/>

> To run product analytics on your ClickHouse setup, you need to > specify a few key columns from your table.
>
> These are the following:
>
> - **User id** - the column for the unique identifier for the users.
> - **Event time** - the timestamp column of your events.
> - Optional[**Event name**] - This column segments the events if the table contains multiple event types.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f0c62e980d02169de95f42d925aa63b9877c8686c9aa1707d37061f34e8ac677/images/integrations/data-visualization/mitzu_05.png" alt="Mitzu event catalog configuration showing column mapping options" />
<br/>
Once all tables are configured, click on the `Save & update event catalog` button, and  Mitzu will find all events and their properties from the above-defined table. This step may take up to a few minutes, depending on the size of your dataset.

## 4. Run segmentation queries [#4-run-segmentation-queries]

User segmentation in Mitzu is as easy as in Amplitude, Mixpanel, or PostHog.

The Explore page has a left-hand selection area for events, while the top section allows you to configure the time horizon.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c1e6da736e9766b650f7acff8cc622ad3432b469f280456c344e1784e4c6f633/images/integrations/data-visualization/mitzu_06.png" alt="Mitzu segmentation query interface with event selection and time configuration" />

<br/>

<Tip title="Filters and Breakdown">
Filtering is done as you would expect: pick a property (ClickHouse column) and select the values from the dropdown that you want to filter.
You can choose any event or user property for breakdowns (see below for how to integrate user properties).
</Tip>

## 5. Run funnel queries [#5-run-funnel-queries]

Select up to 9 steps for a funnel. Choose the time window within which your users can complete the funnel.
Get immediate conversion rate insights without writing a single line of SQL code.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/0f1580992536dd969f2e7b183e2b58114550f38abd898d7f3ac66c23254d197a/images/integrations/data-visualization/mitzu_07.png" alt="Mitzu funnel analysis view showing conversion rates between steps" />

<br/>

<Tip title="Visualize trends">
Pick `Funnel trends` to visualize funnel trends over time.
</Tip>

## 6. Run retention queries [#6-run-retention-queries]

Select up to 2 steps for a retention rate calculation. Choose the retention window for the recurring window for
Get immediate conversion rate insights without writing a single line of SQL code.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7577391d7d53e750d9ea5fd6e2ca30934fc0abf40537b6ebad1c7af44825a6bd/images/integrations/data-visualization/mitzu_08.png" alt="Mitzu retention analysis showing cohort retention rates" />

<br/>

<Tip title="Cohort retention">
Pick `Weekly cohort retention` to visualize how your retention rates change over time.
</Tip>

## 7. Run journey queries [#7-run-journey-queries]

Select up to 9 steps for a funnel. Choose the time window within which your users can finish the journey. The Mitzu journey chart gives you a visual map of every path users take through the selected events.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f5aea8b923126527bb1967c9a1a43bcffac7a40dc26601a4b28027923ec36c9f/images/integrations/data-visualization/mitzu_09.png" alt="Mitzu journey visualization showing user path flow between events" />
<br/>

<Tip title="Break down steps">
You can select a property for the segment `Break down` to distinguish users within the same step.
</Tip>

<br/>

## 8. Run revenue queries [#8-run-revenue-queries]

If revenue settings are configured, Mitzu can calculate the total MRR and subscription count based on your payment events.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/99ce90f68eb745ef65804a16b013a9a8c11c3366749959ff31940df2ab91bd0b/images/integrations/data-visualization/mitzu_10.png" alt="Mitzu revenue analysis dashboard showing MRR metrics" />

## 9. SQL native [#9-sql-native]

Mitzu is SQL Native, which means it generates native SQL code from your chosen configuration on the Explore page.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1afa1856dba645efc8348f2e8029ebe9fbcd80eef65bc5a36d874e429e390ab7/images/integrations/data-visualization/mitzu_11.png" alt="Mitzu SQL code generation view showing native ClickHouse query" />

<br/>

<Tip title="Continue your work in a BI tool">
If you encounter a limitation with Mitzu UI, copy the SQL code and continue your work in a BI tool.
</Tip>

## Mitzu support [#mitzu-support]

If you are lost, feel free to contact us at [support@mitzu.io](email://support@mitzu.io)

Or you our Slack community [here](https://join.slack.com/t/mitzu-io/shared_invite/zt-1h1ykr93a-_VtVu0XshfspFjOg6sczKg)

## Learn more [#learn-more]

Find more information about Mitzu at [mitzu.io](https://mitzu.io)

Visit our documentation page at [docs.mitzu.io](https://docs.mitzu.io)
