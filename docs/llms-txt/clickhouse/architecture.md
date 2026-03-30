# Source: https://clickhouse.ferndocs.com/click-stack/use-cases/observability/clickstack/architecture.md

# Source: https://clickhouse.ferndocs.com/open-source/development/architecture.md

# Source: https://clickhouse.ferndocs.com/cloud/reference/architecture.md

# Source: https://clickhouse.ferndocs.com/cloud/reference/byoc/architecture.md

---
title: Architecture
slug: /cloud/reference/byoc/architecture
sidebar_label: Architecture
keywords:
  - BYOC
  - cloud
  - bring your own cloud
description: Deploy ClickHouse on your own cloud infrastructure
doc_type: reference
---

Metrics and logs are stored within the customer's BYOC VPC. Logs are currently stored in locally in EBS. In a future update, logs will be stored in LogHouse, which is a ClickHouse service in the customer's BYOC VPC. Metrics are implemented via a Prometheus and Thanos stack stored locally in the customer's BYOC VPC.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/aab1044cfff530cdedba515aafe8ada1e3c218dc54dc8332782f5e573c41abdd/images/cloud/reference/byoc-1.png" alt="BYOC Architecture"/>

