# Source: https://www.traceloop.com/docs/openllmetry/integrations/honeycomb.md

# LLM Observability with Honeycomb and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/honeycomb.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=16703d0789a86d2092051d4d8181533c" data-og-width="1684" width="1684" data-og-height="1029" height="1029" data-path="img/integrations/honeycomb.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/honeycomb.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=a53dab25a378d8cd651f7ab5d7c6214d 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/honeycomb.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=a5a26d96448eb641783f14253e5584b0 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/honeycomb.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e8863887adc3c15bd9eaa22dc99ac57c 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/honeycomb.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=bbe12597e17a298c7422e00887a41a3f 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/honeycomb.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=4425109bbf89f5e3b0a215aa29e606cb 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/honeycomb.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c7d32bb20c7a5440f00d6b4c625baec0 2500w" />
</Frame>

Since Honeycomb natively supports OpenTelemetry, you just need to route the traces to Honeycomb's endpoint and set the
API key:

```bash  theme={null}
TRACELOOP_BASE_URL=https://api.honeycomb.io
TRACELOOP_HEADERS="x-honeycomb-team=<YOUR_API_KEY>"
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt