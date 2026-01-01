# Source: https://www.traceloop.com/docs/openllmetry/integrations/kloudmate.md

# LLM Observability with KloudMate and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/kloudmate.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=91ac7c997718ae7637878a85b89446db" data-og-width="1804" width="1804" data-og-height="781" height="781" data-path="img/integrations/kloudmate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/kloudmate.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=6dbcc50b0b1cc9b1378e49846199847a 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/kloudmate.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=729c79b4306ec03bfdc41f056e9f7959 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/kloudmate.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=6eb2f039fc7304fb292bd69669d98a19 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/kloudmate.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=cab8d9219cd5d3106ac2da8e0329f431 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/kloudmate.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=97ff11d109500dd6c1242414604baa94 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/kloudmate.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=344855f33ef209c101c64bcd61a8a822 2500w" />
</Frame>

KloudMate is an [observability platform](https://kloudmate.com/) that natively supports OpenTelemetry, you just need to route the traces to KloudMate OpenTelemetry Collector endpoint and set Authorization header:

```bash  theme={null}
TRACELOOP_BASE_URL="https://otel.kloudmate.com:4318"
TRACELOOP_HEADERS="Authorization=<YOUR_KM_SECRET_KEY>"
```

For more information check out the [docs](https://docs.kloudmate.com/).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt