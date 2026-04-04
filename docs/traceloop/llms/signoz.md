# Source: https://www.traceloop.com/docs/openllmetry/integrations/signoz.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with SigNoz and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/signoz.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=a8564fd1662ca4c77fcc0e2c317267d3" data-og-width="1675" width="1675" data-og-height="1061" height="1061" data-path="img/integrations/signoz.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/signoz.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=a85773904b6697013d4f9dd0d409b240 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/signoz.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=24864cc6cd0e49b0db991431fdaae2b9 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/signoz.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=f7757bd2c3250184ac22571f4893df4e 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/signoz.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=5700334774352d8717025cb5ab7a3356 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/signoz.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=dcc924c2fc66a76a567252bb9e644be4 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/signoz.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=810b49bf69500803f670dcf12a7b7f31 2500w" />
</Frame>

SigNoz is an [open-source observability platform](https://github.com/signoz/signoz).

### With SigNoz cloud

Since SigNoz natively supports OpenTelemetry, you just need to route the traces to SigNoz's endpoint and set the
ingestion key (note no `https` in the URL):

```bash  theme={null}
TRACELOOP_BASE_URL=ingest.{region}.signoz.cloud
TRACELOOP_HEADERS="signoz-access-token=<SIGNOZ_INGESTION_KEY>"
```

Where `region` depends on the choice of your SigNoz cloud region:

| Region | Endpoint                   |
| ------ | -------------------------- |
| US     | ingest.us.signoz.cloud:443 |
| IN     | ingest.in.signoz.cloud:443 |
| EU     | ingest.eu.signoz.cloud:443 |

Validate your configuration by [following these instructions](https://signoz.io/docs/instrumentation/python/#validating-instrumentation-by-checking-for-traces)

### With Self-Hosted version

Once you have an up and running instance of SigNoz, use the following environment variables to export your traces:

```bash  theme={null}
TRACELOOP_BASE_URL="http://localhost:4318"
```
