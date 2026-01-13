# Source: https://docs.datadoghq.com/account_management/guide/csv-headers-billing-migration.md

---
title: Migrating to New Plan & Usage CSV Headers the week of February 19, 2024
description: >-
  Update your automation for the new Plan & Usage CSV headers that align cost
  data with in-app displays, effective February 19, 2024.
breadcrumbs: >-
  Docs > Account Management > Account Management Guides > Migrating to New Plan
  & Usage CSV Headers the week of February 19, 2024
source_url: https://docs.datadoghq.com/guide/csv-headers-billing-migration/index.html
---

# Migrating to New Plan & Usage CSV Headers the week of February 19, 2024

The headers for Plan & Usage Cost Chargebacks CSV files will be updated the week of February 19, 2024. The updates align the costs in the CSV file with the cost data shown in-app.

If you have automation that relies on the CSV headers in the cost chargebacks file you download from the Usage page, these headers are changing and your automation needs to be updated. Below is the section where the changes are taking place, and includes an example of the new CSV headers to support the migration.

## Individual Organizations Summary{% #individual-organizations-summary %}

1. [Header Mapping](https://docs.datadoghq.com/account_management/guide/csv_headers/individual-orgs-summary/)
1. Where to download the CSV:

{% image
   source="https://datadog-docs.imgix.net/images/account_management/billing/cost-chargebacks-csv-update.131d49f33886021b1b1e01217bdd07c0.png?auto=format"
   alt="Download CSV in Individual Orgs Summary" /%}
