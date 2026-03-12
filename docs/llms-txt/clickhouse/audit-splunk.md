# Source: https://clickhouse.ferndocs.com/integrations/audit-splunk.md

---
sidebar_label: Splunk
slug: /integrations/audit-splunk
keywords:

- clickhouse
- Splunk
- audit
- cloud
description: Store ClickHouse Cloud audit logs into Splunk.
title: Storing ClickHouse Cloud Audit logs into Splunk
doc_type: guide

---

import {PartnerBadge} from '../../../../../components/Badges/PartnerBadge'

<PartnerBadge/>

[Splunk](https://www.splunk.com/) is a data analytics and monitoring platform.

This add-on allows users to store the [ClickHouse Cloud audit logs](/cloud/security/audit-logging) into Splunk. It uses [ClickHouse Cloud API](/cloud/manage/api/api-overview) to download the audit logs.

This add-on contains only a modular input, no additional UI are provided with this add-on.

## Installation

### For Splunk Enterprise [#for-splunk-enterprise]

Download the ClickHouse Cloud Audit Add-on for Splunk from [Splunkbase](https://splunkbase.splunk.com/app/7709).

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d57000ce2b1fa95791575e88be4744eea68662ba89ac43519e1654a92e9b47d1/images/integrations/tools/data-integration/splunk/splunk_001.png" alt="Splunkbase website showing the ClickHouse Cloud Audit Add-on for Splunk download page"/>

In Splunk Enterprise, navigate to Apps -> Manage. Then click on Install app from file.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/db6caaa0151c2bab1d7b5457ae2e49000b576dbc52f2f07c9824e6cb0c9e24a2/images/integrations/tools/data-integration/splunk/splunk_002.png" alt="Splunk Enterprise interface showing the Apps management page with Install app from file option"/>

Select the archived file downloaded from Splunkbase and click on Upload.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f169d8d4dd38a71b245597533a82134e9f367e2d9edda968d1e6be7b9c5a1ddf/images/integrations/tools/data-integration/splunk/splunk_003.png" alt="Splunk app installation dialog for uploading the ClickHouse add-on"/>

If everything goes fine, you should now see the ClickHouse Audit logs application installed. If not, consult the Splunkd logs for any errors.

### Modular input configuration

To configure the modular input, you'll first need information from your ClickHouse Cloud deployment:

- The organization ID
- An admin [API Key](/cloud/manage/openapi)

### Getting information from ClickHouse Cloud [#getting-information-from-clickhouse-cloud]

Log in to the [ClickHouse Cloud console](https://console.clickhouse.cloud/).

Navigate to your Organization -> Organization details. There you can copy the Organization ID.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/66ababe08a441ca1a334acd9f31cfc115b4e3ce4eb183387165bf67797f9c183/images/integrations/tools/data-integration/splunk/splunk_004.png" alt="ClickHouse Cloud console showing the Organization details page with Organization ID"/>

Then, navigate to API Keys from the left-end menu.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/dd459a3f64d28d197de6c9fddd6b3e263850a5decb59705dd468ea9ec32e2b86/images/integrations/tools/data-integration/splunk/splunk_005.png" alt="ClickHouse Cloud console showing the API Keys section in the left navigation menu"/>

Create an API Key, give a meaningful name and select `Admin` privileges. Click on Generate API Key.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f106292590aa9f7f3fbdc3a21d6d5c23ff5c1e9c302e734111a97df4d37b22f6/images/integrations/tools/data-integration/splunk/splunk_006.png" alt="ClickHouse Cloud console showing the API Key creation interface with Admin privileges selected"/>

Save the API Key and secret in a safe place.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ab9667b4c73e5e7711c1e134886590908b300be78b84107d7c14e4cbfe8dfbc1/images/integrations/tools/data-integration/splunk/splunk_007.png" alt="ClickHouse Cloud console showing the generated API Key and secret to be saved"/>

## Configure data input in Splunk [#configure-data-input-in-splunk]

Back in Splunk, navigate to Settings -> Data inputs.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1025dfef52d966af6a60a5cd259a9c9d3a084abaea0ee85c4c1c86f60e72426a/images/integrations/tools/data-integration/splunk/splunk_008.png" alt="Splunk interface showing the Settings menu with Data inputs option"/>

Select the ClickHouse Cloud Audit Logs data input.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/76203c5c8d3d14f3c8881dc069ddf0218f6279a0a9878d5b3be7148c17d46dd5/images/integrations/tools/data-integration/splunk/splunk_009.png" alt="Splunk Data inputs page showing the ClickHouse Cloud Audit Logs option"/>

Click "New" to configure a new instance of the data input.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/587b7286c7e497afcc4f8f3fbf8012aac868efd100a4bf270bf3a435d8006f9c/images/integrations/tools/data-integration/splunk/splunk_010.png" alt="Splunk interface for configuring a new ClickHouse Cloud Audit Logs data input"/>

Once you have entered all the information, click Next.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/95c69f70a555c8992bb3c3285d5416e04a2a217afd32a51fffc2e1115e5470c7/images/integrations/tools/data-integration/splunk/splunk_011.png" alt="Splunk configuration page with completed ClickHouse data input settings"/>

The input is configured, you can start browsing the audit logs.

## Usage

The modular input stores data in Splunk. To view the data, you can use the general search view in Splunk.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/35d9f1e591e3c80dd66c8d7ab04724e23dadf4af597551b13b9f3c3b2149bca7/images/integrations/tools/data-integration/splunk/splunk_012.png" alt="Splunk search interface showing ClickHouse audit logs data"/>
