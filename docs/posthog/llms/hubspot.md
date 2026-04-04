# Source: https://posthog.com/docs/data-warehouse/sources/hubspot.md

# Source: https://posthog.com/docs/cdp/destinations/hubspot.md

# Source: https://posthog.com/docs/cdp/sources/hubspot.md

# Linking Hubspot as a source - Docs

The HubSpot connector can link contacts, companies, deals, emails, meetings, quotes, and tickets to PostHog.

To link Hubspot:

1.  Go to the [Data pipeline page](https://app.posthog.com/data-management/sources) and the sources tab in PostHog
2.  Click **New source** and select Hubspot
3.  Select the Hubspot account you want to link and click **Connect app**
4.  *Optional:* Add a prefix to your table names
5.  Select the tables you want to import (incremental/append syncs are not supported for HubSpot tables.)
6.  Click **Import**

The data warehouse then starts syncing your Hubspot data. You can see details, progress, and rows synced in the [data pipeline sources tab](https://app.posthog.com/data-management/sources).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better