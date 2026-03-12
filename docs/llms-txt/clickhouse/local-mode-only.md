# Source: https://clickhouse.ferndocs.com/click-stack/use-cases/observability/clickstack/deployment/local-mode-only.md

---
slug: /use-cases/observability/clickstack/deployment/local-mode-only
title: Local Mode Only
pagination_prev: null
pagination_next: null
sidebar_position: 5
description: Deploying ClickStack with Local Mode Only - The ClickHouse Observability Stack
doc_type: guide
keywords:

- clickstack
- deployment
- setup
- configuration
- observability

---

import {BetaBadge} from '../../../../components/Badges/BetaBadge'

Similar to the [all-in-one image](/use-cases/observability/clickstack/deployment/docker-compose), this comprehensive Docker image bundles all ClickStack components:

- **ClickHouse**
- **HyperDX**
- **OpenTelemetry (OTel) collector** (exposing OTLP on ports `4317` and `4318`)
- **MongoDB** (for persistent application state)

**However, user authentication is disabled for this distribution of HyperDX**

### Suitable for [#suitable-for]

- Demos
- Debugging
- Development where HyperDX is used

## Deployment steps [#deployment-steps]

<br/>

<Steps headerLevel="h3">

### Deploy with Docker [#deploy-with-docker]

Local mode deploys the HyperDX UI on port 8080.

```shell
docker run -p 8080:8080 docker.hyperdx.io/hyperdx/hyperdx-local
```

### Navigate to the HyperDX UI [#navigate-to-hyperdx-ui]

Visit [http://localhost:8080](http://localhost:8080) to access the HyperDX UI.

**You will not be prompted to create a user, as authentication is not enabled in this deployment mode.**

Connect to your own external ClickHouse cluster e.g. ClickHouse Cloud.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/00714b1c533be4301a47920a26282bd45ebee2b7f4b139d24d596bdce0932d15/images/use-cases/observability/hyperdx-2.png" alt="Create login"/>

Create a source, retain all default values, and complete the `Table` field with the value `otel_logs`. All other settings should be auto-detected, allowing you to click `Save New Source`.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c373c33fe70d529b950d1b2d33757510ebd27eaf18aca25a0882df8a30a08de8/images/use-cases/observability/hyperdx-logs.png" alt="Create logs source"/>

</Steps>

## JSON type support [#json-type-support]

<BetaBadge/>

ClickStack has beta support for the [JSON type](/interfaces/formats/JSON) from version `2.0.4`.

For the benefits of this type see [Benefits of the JSON type](/use-cases/observability/clickstack/ingesting-data/otel-collector#benefits-json-type).

In order to enable support for the JSON type users must set the following environment variables:

- `OTEL_AGENT_FEATURE_GATE_ARG='--feature-gates=clickhouse.json'` - enables support in the OTel collector, ensuring schemas are created using the JSON type.
- `BETA_CH_OTEL_JSON_SCHEMA_ENABLED=true` - enables support in the HyperDX application, allowing JSON data to be queried.

For the local mode only image, users only need to set the `BETA_CH_OTEL_JSON_SCHEMA_ENABLED=true` parameter e.g.

```shell
docker run -e BETA_CH_OTEL_JSON_SCHEMA_ENABLED=true -p 8080:8080 docker.hyperdx.io/hyperdx/hyperdx-local
```
