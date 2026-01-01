# Source: https://www.traceloop.com/docs/openllmetry/integrations/axiom.md

# LLM Observability with Axiom and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/axiom.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=cee239b3f53eea321e125efd5698e776" data-og-width="1629" width="1629" data-og-height="1182" height="1182" data-path="img/integrations/axiom.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/axiom.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=9b68a5e9e61edc59bfd22de0a4db4219 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/axiom.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=6982f89c4420672f8ab563212decec78 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/axiom.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=4e59f776669f399c2992b9176180c813 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/axiom.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e09a1e1d916ce5ab69131631c7871c3e 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/axiom.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=5fe08316de042a54616ae67059b17902 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/axiom.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=dc5ec643b14dfff35eb2d98e8ce571f5 2500w" />
</Frame>

Axiom is an [observability platform](https://axiom.co/) that natively supports OpenTelemetry, you just need to route the traces to Axiom's endpoint and set the dataset, and API key:

```bash  theme={null}
TRACELOOP_BASE_URL="https://api.axiom.co"
TRACELOOP_HEADERS="Authorization=Bearer <YOUR_API_KEY>,X-Axiom-Dataset=<YOUR_DATASET>"
```

For more information check out the [docs link](https://axiom.co/docs/send-data/opentelemetry).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt