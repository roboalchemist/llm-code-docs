# Source: https://www.traceloop.com/docs/openllmetry/integrations/newrelic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM observability with New Relic and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/newrelic.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=1eeb5b1a0c7d698fdf9a03a158a3305b" data-og-width="3042" width="3042" data-og-height="2015" height="2015" data-path="img/integrations/newrelic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/newrelic.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=6788fb73abc5e08ec3e94ab01b4d4d8f 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/newrelic.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=7b9ddb2e6b3165938863768debecef2b 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/newrelic.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=d655fa44a3af9798b25e544eaa91e43e 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/newrelic.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=44adccdb7e5134ebf7ffff8a414a8061 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/newrelic.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=53f5ffcde5a7e77f8de0bf780c50139d 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/newrelic.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c95e508e7262ec6809e1571454343375 2500w" />
</Frame>

Since New Relic natively supports OpenTelemetry, you just need to route the traces to New Relic's endpoint and set the API key:

```bash  theme={null}
TRACELOOP_BASE_URL=https://otlp.nr-data.net:443
TRACELOOP_HEADERS="api-key=<YOUR_NEWRELIC_LICENSE_KEY>"
```

For more information check out the [docs link](https://docs.newrelic.com/docs/more-integrations/open-source-telemetry-integrations/opentelemetry/get-started/opentelemetry-set-up-your-app/#review-settings).
