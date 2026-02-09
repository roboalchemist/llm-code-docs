# Source: https://www.traceloop.com/docs/openllmetry/integrations/highlight.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Highlight and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/highlight.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=ddda6554e850a37745325766ac189586" data-og-width="3671" width="3671" data-og-height="1975" height="1975" data-path="img/integrations/highlight.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/highlight.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=eeac0cd40f91128adc5e08a1906e3514 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/highlight.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=31670a3716e3b412c02f331e9675a183 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/highlight.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=d24b681187fbbe4dc20b94394a69e83e 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/highlight.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=354c253e7631a39387e0c7d95ea41ea9 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/highlight.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=7dfe3c09d1c562ae77fc6d94537f5961 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/highlight.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=3827829115f1ac69aaba6044c27af3fc 2500w" />
</Frame>

Since [Highlight](https://www.highlight.io) natively supports OpenTelemetry, you just need to route the traces to Highlights's OTLP endpoint and set the
highlight project id in the headers:

```bash  theme={null}
TRACELOOP_BASE_URL=https://otel.highlight.io:4318
TRACELOOP_HEADERS="x-highlight-project=<YOUR_HIGHLIGHT_PROJECT_ID>"
```
