# Source: https://www.traceloop.com/docs/openllmetry/integrations/groundcover.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with groundcover and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/UL38GgJOBlei-xtG/img/integrations/groundcover.png?fit=max&auto=format&n=UL38GgJOBlei-xtG&q=85&s=60aae2470d21449de61701d918e322d6" data-og-width="3010" width="3010" data-og-height="1458" height="1458" data-path="img/integrations/groundcover.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UL38GgJOBlei-xtG/img/integrations/groundcover.png?w=280&fit=max&auto=format&n=UL38GgJOBlei-xtG&q=85&s=a884400fcb92e905c34f75a430b287cd 280w, https://mintcdn.com/enrolla/UL38GgJOBlei-xtG/img/integrations/groundcover.png?w=560&fit=max&auto=format&n=UL38GgJOBlei-xtG&q=85&s=025659f85bc185f739c7340ecf2d5ba4 560w, https://mintcdn.com/enrolla/UL38GgJOBlei-xtG/img/integrations/groundcover.png?w=840&fit=max&auto=format&n=UL38GgJOBlei-xtG&q=85&s=1a545f4ac0a42a8df83f30bba2546809 840w, https://mintcdn.com/enrolla/UL38GgJOBlei-xtG/img/integrations/groundcover.png?w=1100&fit=max&auto=format&n=UL38GgJOBlei-xtG&q=85&s=0be75a7672840f4ff01f8fd06f22e704 1100w, https://mintcdn.com/enrolla/UL38GgJOBlei-xtG/img/integrations/groundcover.png?w=1650&fit=max&auto=format&n=UL38GgJOBlei-xtG&q=85&s=04508d0918a389754ab819f5d9add706 1650w, https://mintcdn.com/enrolla/UL38GgJOBlei-xtG/img/integrations/groundcover.png?w=2500&fit=max&auto=format&n=UL38GgJOBlei-xtG&q=85&s=b9865fb30744ab2c79b31d6ab40f09a4 2500w" />
</Frame>

[groundcover](https://www.groundcover.com) is a BYOC, eBPF-powered, OpenTelemetry-native complete observability platform.

You have two options for sending traces to groundcover:

## Option 1 - Send directly to the groundcover sensor

No API key required. Saves on networking costs.

```bash  theme={null}
TRACELOOP_BASE_URL=http://groundcover-sensor.groundcover.svc.cluster.local:4318
```

## Option 2 - Send directly to the groundcover BYOC endpoint

Allows sending traces from any runtime, e.g., Docker, serverless, ECS, etc. Requires an ingestion key.

First, [create an ingestion key](https://docs.groundcover.com/use-groundcover/remote-access-and-apis/ingestion-keys#creating-an-ingestion-key).

Then, set the following environment variables:

```bash  theme={null}
TRACELOOP_BASE_URL=https://<GROUNDCOVER_BYOC_ENDPOINT>
TRACELOOP_HEADERS="apikey=<GROUNDCOVER_INGESTION_KEY>"
```

For more information, check out the [groundcover OpenTelemetry documentation](https://docs.groundcover.com/integrations/data-sources/opentelemetry).
