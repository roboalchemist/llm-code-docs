# Source: https://docs.datadoghq.com/data_observability/jobs_monitoring/openlineage.md

---
title: Custom Jobs using OpenLineage
description: >-
  Monitor jobs from in-house tools, custom pipelines, and orchestrators that
  don't have native Datadog integrations.
breadcrumbs: >-
  Docs > Data Observability Overview > Data Observability: Jobs Monitoring >
  Custom Jobs using OpenLineage
---

# Custom Jobs using OpenLineage

{% alert level="info" %}
Custom jobs using OpenLineage is in Preview.
{% /alert %}

## Overview{% #overview %}

Custom jobs use the [OpenLineage](https://openlineage.io/) standard to send job and lineage events to Datadog. Use custom jobs when you need to:

- Capture lineage from systems Datadog doesn't integrate with natively, such as in-house tools or custom ETL scripts
- Emit lineage events for jobs or orchestrators where a native Datadog integration isn't available

Replace the hostname in the examples with the relevant [Datadog site](https://openlineage.io/docs/client/python/#predefined-datadog-sites) for your organization. To find your Datadog site, see [Access the Datadog site](https://docs.datadoghq.com/getting_started/site/#access-the-datadog-site). This example uses `datadoghq.com`.

**Note**: To centralize configuration and avoid distributing API keys to every application, you can [set up the Datadog Agent as an OpenLineage proxy](https://docs.datadoghq.com/data_observability/jobs_monitoring/openlineage/datadog_agent_for_openlineage/).

Use one of the following options to send [OpenLineage events](https://openlineage.io/) to Datadog:

{% tab title="Direct HTTP with curl" %}
Send a raw [OpenLineage RunEvent](https://openlineage.io/docs/spec/run-cycle/) as JSON to Datadog's intake endpoint.

```shell
curl -X POST "https://data-obs-intake.datadoghq.com/api/v1/lineage" \
  -H "Authorization: Bearer <DD_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
        "eventTime": "2023-01-01T00:00:00Z",
        "eventType": "START",
        "run": { "runId": "123e4567-e89b-12d3-a456-426614174000" },
        "job": { "namespace": "default", "name": "test-job" },
        "producer": "your-producer-id"
      }'
```

{% /tab %}

{% tab title="OpenLineage Python client (HTTP transport)" %}
Use the [OpenLineage Python client](https://openlineage.io/docs/client/python) with a manually specified HTTP transport.

```python
from datetime import datetime
import uuid
from openlineage.client import OpenLineageClient, OpenLineageClientOptions
from openlineage.client.event_v2 import RunEvent, RunState, Job, Run

client = OpenLineageClient(
    url="https://data-obs-intake.datadoghq.com",
    options=OpenLineageClientOptions(api_key="<DD_API_KEY>")
)

event = RunEvent(
    eventType=RunState.START,
    eventTime=datetime.utcnow().isoformat(),
    run=Run(runId=str(uuid.uuid4())),
    job=Job(namespace="default", name="test-job"),
    producer="your-producer-id"
)

client.emit(event)
```

{% /tab %}

{% tab title="OpenLineage Python client (Datadog transport)" %}
In OpenLineage 1.37.0+, use the [Datadog transport](https://openlineage.io/docs/client/python#datadog-transport) for automatic configuration and optimized event delivery.

```python
from datetime import datetime
import uuid
from openlineage.client import OpenLineageClient
from openlineage.client.event_v2 import RunEvent, RunState, Job, Run
from openlineage.client.transport.datadog import DatadogConfig, DatadogTransport

config = DatadogConfig(
    apiKey="<DD_API_KEY>",
    site="datadoghq.com"  # Change if using a different Datadog site
)

client = OpenLineageClient(transport=DatadogTransport(config))

event = RunEvent(
    eventType=RunState.START,
    eventTime=datetime.utcnow().isoformat(),
    run=Run(runId=str(uuid.uuid4())),
    job=Job(namespace="default", name="test-job"),
    producer="your-producer-id"
)

client.emit(event)
```

{% alert level="info" %}
For Option 3, you can skip `DatadogConfig` by using environment variables:
```shell
export DD_API_KEY=your-datadog-api-key
export DD_SITE=datadoghq.com
export OPENLINEAGE__TRANSPORT__TYPE=datadog
```

```python
client = OpenLineageClient.from_environment()
```

{% /alert %}

{% /tab %}

## Further reading{% #further-reading %}

- [Data Observability Overview](https://docs.datadoghq.com/data_observability/)
- [Set up Datadog Agent for OpenLineage Proxy](https://docs.datadoghq.com/data_observability/jobs_monitoring/openlineage/datadog_agent_for_openlineage/)
