# Source: https://www.traceloop.com/docs/openllmetry/integrations/hyperdx.md

# LLM Observability with HyperDX and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/hyperdx.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=8b1e640fca13f41af95c00ebb3f72273" data-og-width="1663" width="1663" data-og-height="1061" height="1061" data-path="img/integrations/hyperdx.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/hyperdx.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=7203de519e94d8296ef237c6099b1190 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/hyperdx.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=1ea487ae7ba75ee4b4352f936c2281bb 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/hyperdx.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=feea23e4ba4250a2362503d03990d0e8 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/hyperdx.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=f545e7a9ede36d7a48ea6a087108d3fa 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/hyperdx.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=9eabe54747cc6af03f98ebd42ff55676 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/hyperdx.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=63a0d56cf6f6985aa6264f7372e7b2a1 2500w" />
</Frame>

HyperDX is an [open source observability platform](https://github.com/hyperdxio/hyperdx) that natively supports OpenTelemetry.
Just route the traces to HyperDX's endpoint and set the API key:

```bash  theme={null}
TRACELOOP_BASE_URL=https://in-otel.hyperdx.io
TRACELOOP_HEADERS="authorization=<YOUR_INGESTION_API_KEY>"
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt