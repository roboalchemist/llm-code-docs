# Source: https://www.traceloop.com/docs/openllmetry/integrations/dash0.md

# LLM Observability with Dash0 and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/dash0.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=1ea165082123d4e1641114910ba753fe" data-og-width="3024" width="3024" data-og-height="1653" height="1653" data-path="img/integrations/dash0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/dash0.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=6396cdf59aaffc136d6a17afdf2b584e 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/dash0.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=932791acbf9c86186419d33e6f090157 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/dash0.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=45684a84e377ccca311aea70a6e5eaf2 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/dash0.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c8b662fc77bec98df12defd9f994531a 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/dash0.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c2e9f4199586079db7ca92035c4f79b0 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/dash0.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=574bc084fc149df8c6716cff81567bf3 2500w" />
</Frame>

[Dash0](https://www.dash0.com) is an OpenTelemetry-natively observability solution. You can route your traces directly to Dash0's ingest APIs.

```bash  theme={null}
TRACELOOP_BASE_URL="https://ingress.eu-west-1.aws.dash0.com"
TRACELOOP_HEADERS="Authorization=Bearer <YOUR_AUTH_TOKEN>"
```

For more information check out the [documentation](https://www.dash0.com/documentation/dash0/get-started/sending-data-to-dash0).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt