# Source: https://clickhouse.ferndocs.com/integrations/rocketbi.md

---
sidebar_label: Rocket BI
sidebar_position: 131
slug: /integrations/rocketbi
keywords:

- clickhouse
- RocketBI
- connect
- integrate
- ui
description: >-
  RocketBI is a self-service business intelligence platform that helps you
  quickly analyze data, build drag-n-drop visualizations and collaborate with
  colleagues right on your web browser.
title: Integrate Rocket BI with ClickHouse
doc_type: guide

---

import {CommunityMaintainedBadge} from "@site/components/Badges/CommunityMaintainedBadge"

<CommunityMaintainedBadge/>

In this guide, you will install and build a simple dashboard using Rocket.BI .
This is the dashboard:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/80ee43edab73f2955ebbadf2607863e1c139ea93047bb00ffba1698b556f229a/images/integrations/data-visualization/rocketbi_01.gif" alt="Rocket BI dashboard showing sales metrics with charts and KPIs" />
<br/>

You can checkout [the Dashboard via this link.](https://demo.rocket.bi/dashboard/sales-dashboard-7?token=7eecf750-cbde-4c53-8fa8-8b905fec667e)

## Install [#install]

Start RocketBI with our pre-built docker images.

Get docker-compose.yml and configuration file:

```bash
wget https://raw.githubusercontent.com/datainsider-co/rocket-bi/main/docker/docker-compose.yml
wget https://raw.githubusercontent.com/datainsider-co/rocket-bi/main/docker/.clickhouse.env
```

Edit .clickhouse.env, add clickhouse server information.

Start RocketBI by run command: ``` docker-compose up -d . ```

Open browser, go to ```localhost:5050```, login with this account: ```hello@gmail.com/123456```

To build from source or advanced configuration you could check it here [Rocket.BI Readme](https://github.com/datainsider-co/rocket-bi/blob/main/README.md)

## Let's build the dashboard [#lets-build-the-dashboard]

In Dashboard, you will find your reportings, start visualization by clicking **+New**

You can build **unlimited dashboards** & draw **unlimited charts** in a dashboard.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/395fbdd3a6c12bb521ceab923737f6cb7f9767d3e208806b83f2e4bc7cd12542/images/integrations/data-visualization/rocketbi_02.gif" alt="Animation showing the process of creating a new chart in Rocket BI" />
<br/>

See hi-res tutorial on Youtube: [https://www.youtube.com/watch?v=TMkdMHHfvqY](https://www.youtube.com/watch?v=TMkdMHHfvqY)

### Build the chart controls [#build-the-chart-controls]

#### Create a metrics control [#create-a-metrics-control]

In the Tab filter, select metric fields you want to use. Make sure to keep check on aggregation setting.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/94bdea5b3a8a721bee8606c898311f9c69690090543313f52c68eb10f1108664/images/integrations/data-visualization/rocketbi_03.png" alt="Rocket BI metrics control configuration panel showing selected fields and aggregation settings" />
<br/>

Rename filters & Save Control to Dashboard

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/0be32333f9fb21fcee6ac656360df3d9f712facb8e249f505d606c4bb82a39a1/images/integrations/data-visualization/rocketbi_04.png" alt="Metrics control with renamed filters ready to save to dashboard" />

#### Create a date type control [#create-a-date-type-control]

Choose a Date field as Main Date column:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/71314fefee2b72f64844d6ee50cf4385f4c0da1f69e17b5c29e969f7496fa688/images/integrations/data-visualization/rocketbi_05.png" alt="Date field selection interface in Rocket BI showing available date columns" />
<br/>

Add duplicate variants with different lookup ranges. For example, Year, Monthly, Daily date or Day of Week.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f811be4b7eb7b28cdd39370fefc6147b9e0f60aa2035efede22b73e5f5075ef9/images/integrations/data-visualization/rocketbi_06.png" alt="Date range configuration showing different time period options like year, month, and day" />
<br/>

Rename filters & Save Control to Dashboard

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/078c63c9577f367517cb4be9f06ba4579e7eaaa151c7e425303476fb2f0cd829/images/integrations/data-visualization/rocketbi_07.png" alt="Date range control with renamed filters ready to save to dashboard" />

### Now, let build the Charts [#now-let-build-the-charts]

#### Pie chart: sales metrics by regions [#pie-chart-sales-metrics-by-regions]

Choose Adding new chart, then Select Pie Chart

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5c2e274dfeffdd8bdd0f2055a711002ed506ef234888d6533c17bb30ee8ee1ca/images/integrations/data-visualization/rocketbi_08.png" alt="Chart type selection panel with pie chart option highlighted" />
<br/>

First Drag & Drop the column "Region" from the Dataset to Legend Field

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4146c2f33addff6bcbccee777309bc61f66edd74b7fdb862f837fe239c1d4fef/images/integrations/data-visualization/rocketbi_09.png" alt="Drag and drop interface showing Region column being added to legend field" />
<br/>

Then, change to Chart Control Tab

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5600d003703c2e91d3439361e577921b4a7664a152f1af82fcee5dab5bce2d62/images/integrations/data-visualization/rocketbi_10.png" alt="Chart control tab interface showing visualization configuration options" />
<br/>

Drag & Drop the Metrics Control into Value Field

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/a661e170d508fc5a2c90987ddede78305138a91d7a79a4ca5db15a31cf336cbc/images/integrations/data-visualization/rocketbi_11.png" alt="Metrics control being added to the value field of the pie chart" />
<br/>

(you can also use Metrics Control as Sorting)

Navigate to Chart Setting for further customization

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/3c786f2e2acd8443305dccde7be37fb99ba3c6167b31a656c209c05bdb37305a/images/integrations/data-visualization/rocketbi_12.png" alt="Chart settings panel showing customization options for the pie chart" />
<br/>

For example, change Data label to Percentage

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7735802257c2704c17a14245c9dde5cec3d867ec2b23ca286f4fcc8264946506/images/integrations/data-visualization/rocketbi_13.png" alt="Data label settings being changed to show percentages on the pie chart" />
<br/>

Save & Add the Chart to Dashboard

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c3739bc43ed8550ccc47b224949e61b06e018ce2a5dd4297739cff8e5ee87e7f/images/integrations/data-visualization/rocketbi_14.png" alt="Dashboard view showing the newly added pie chart with other controls" />

#### Use date control in a time-series chart [#use-date-control-in-a-time-series-chart]

Let Use a Stacked Column Chart

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9890274579d644f8e807c5aaa7a495f04162696c995187c144e990812b81cb0c/images/integrations/data-visualization/rocketbi_15.png" alt="Stacked column chart creation interface with time-series data" />
<br/>

In Chart Control, use Metrics Control as Y-axis & Date Range as X-axis

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/512e7ecca10583f5e97f9464893f2003e4e079f0782e629a84e0634858b456cc/images/integrations/data-visualization/rocketbi_16.png" alt="Chart control configuration showing metrics on Y-axis and date range on X-axis" />
<br/>

Add Region column in to Breakdown

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/a7094f0e30f61b69812f188d1845b398a653082b98b33f3b93ed21a04796715e/images/integrations/data-visualization/rocketbi_17.png" alt="Region column being added as breakdown dimension in the stacked column chart" />
<br/>

Adding Number Chart as KPIs & glare-up the Dashboard

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b4908569c7e204836a9d19436200d94156682f7b20ea033cdcf968563554152a/images/integrations/data-visualization/rocketbi_18.png" alt="Complete dashboard with KPI number charts, pie chart, and time-series visualization" />
<br/>

Now, you had successfully build your 1st dashboard with rocket.BI
