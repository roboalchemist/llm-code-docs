# Source: https://www.traceloop.com/docs/openllmetry/integrations/service-now.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Service Now Cloud Observability and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/service-now.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=5b455cd683b8be512371e2450af36da2" data-og-width="1071" width="1071" data-og-height="480" height="480" data-path="img/integrations/service-now.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/service-now.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=7865d921b2e03afcf2902f916c674094 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/service-now.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=5b07ede3c7cdf823b8fe5c2d6aa418d1 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/service-now.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=1cab0526e8442a22baa9222c71bd19e6 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/service-now.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=964176c835fea8a143f892f7de4bdd23 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/service-now.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=975b4a18bb701a244a32fec0f52fdf4a 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/service-now.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=028af3aa0a60f827c0eb4859068d2a1a 2500w" />
</Frame>

Since Service Now Cloud Observability natively supports OpenTelemetry, you just need to route the traces to Service Now Cloud Observability's endpoint and set the
access token:

```bash  theme={null}
TRACELOOP_BASE_URL=https://ingest.lightstep.com
TRACELOOP_HEADERS="lightstep-access-token=<YOUR_ACCESS_TOKEN>"
```
