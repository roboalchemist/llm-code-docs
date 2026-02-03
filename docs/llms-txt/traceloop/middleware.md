# Source: https://www.traceloop.com/docs/openllmetry/integrations/middleware.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Middleware and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-1.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=929904890498ef38b068f9c6f9fed3ef" data-og-width="1960" width="1960" data-og-height="1163" height="1163" data-path="img/integrations/middleware-dashboard-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-1.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=67cacbc5297e8ef6e7ff196a760f9b45 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-1.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=d1cdd648d91441ba847fadae2303498c 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-1.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=90ea153bd3e936418b766a17817b94d5 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-1.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=fc823ba558127996402dae82d8e7ee59 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-1.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=ace4e2918b136bbf861fb477c8263201 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-1.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=5f60ac69325fcb7ad022fda1d5a00dbe 2500w" />

  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-2.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=3bdb2a4ef1f6a49ad04954a4bc863852" data-og-width="1960" width="1960" data-og-height="1163" height="1163" data-path="img/integrations/middleware-dashboard-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-2.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=d23302b120a4cb08e5f25bba8fb80dde 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-2.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=d5aefdb0420cede2da77c0c8347a1d3b 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-2.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=d188a90ba565177cf81b38127efacd8c 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-2.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=afee9f53c1888044b6747a000a7134c7 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-2.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=9445778c4eee3149a96321a8b53c064b 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-2.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=740a925218aa8f55c5d511e2e149c492 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-3.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c2612ebde18579daf27bc8e83828623e" data-og-width="1960" width="1960" data-og-height="1163" height="1163" data-path="img/integrations/middleware-dashboard-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-3.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=0b2a1493140adc6dbb37e29660152d2b 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-3.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=af832a102e468f7f8d657bca01dc1ee1 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-3.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=2d59ff615b759954fc226aadf626e3a5 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-3.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=443ab726bc5fb90ec1679699212bf0bf 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-3.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=0d6ee163195714042385de45e5d1a552 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-3.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=b45cb8cc51da805acdf4eab3e5fd4028 2500w" />

  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-4.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=ec51d315d2d68e70ceade635576dc231" data-og-width="1960" width="1960" data-og-height="1163" height="1163" data-path="img/integrations/middleware-dashboard-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-4.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=a778968bffb416e9aeb82ebc590fbb52 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-4.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=f64e1a121c8fde4c61b315164f026afd 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-4.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=26399bfda5d5b8ebe8da0e14acb4df9e 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-4.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=6e927fa5d32a6da02a1dc815d5acbeb4 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-4.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=666fc90b9b48f205f1c334b2649d6ae3 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/middleware-dashboard-4.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=3ff8ac94bcdd8f28dd6eba6b8e883984 2500w" />
</Frame>

To send OpenTelemetry metrics and traces generated by Traceloop from your LLM Application to Middleware, Follow the below steps.

<Steps>
  <Step title="Get your Middleware credentials">
    <Steps>
      1. Sign in to your [Middleware](https://app.middleware.io/) account.
      2. Go to settings and click on API Key. [Link](https://app.middleware.io/settings/api-keys)
      3. Copy and Save the value for `MW_API_KEY` and `MW_TARGET`
    </Steps>
  </Step>

  <Step title="Add the following lines to your application code:">
    <Tabs>
      <Tab title="Python">
        ```python  theme={null}
        from traceloop.sdk import Traceloop

        Traceloop.init(
            app_name="YOUR_APPLICATION_NAME",
            api_endpoint="<MW_TARGET>",
            headers={
                "Authorization": "<MW_API_KEY>",
                "X-Trace-Source": "traceloop",
            },
            resource_attributes={"key": "value"},
        )
        ```
      </Tab>

      <Tab title="Typescript (Node js)">
        ```javascript  theme={null}
        import * as traceloop from "@traceloop/node-server-sdk";
        traceloop.initialize({
          appName: "YOUR_APPLICATION_NAME",
          apiEndpoint: "<MW_TARGET>",
          headers: {
            Authorization: "<MW_API_KEY>",
            "X-Trace-Source": "traceloop",
          },
          resourceAttributes: { "key": "value" },
        });
        ```
      </Tab>
    </Tabs>

    Replace:

    1. `MW_TARGET` with your middleware target url

    * Example - `https://abcde.middleware.io`

    2. `MW_API_KEY` with your middleware api key.

    * Example - nxhqwpbvcmlkjhgfdsazxcvbnmkjhgtyui

    Refer to the Traceloop [Docs](https://www.traceloop.com/docs/introduction) for more advanced configurations and use cases.

    For detailed information on LLM Observability with Middleware and Traceloop, consult Middleware Documentation:
    [LLM Observability Documentation](https://docs.middleware.io/llm-observability/overview).
  </Step>

  <Step title="Visualize in Middleware">
    Once your LLM application is instrumented, you can view the traces, metrics and dashboards in the Middleware LLM Observability section. To access this:

    1. Log in to your Middleware account
    2. Navigate to the [LLM Observability Section](https://app.middleware.io/llm) in the sidebar
  </Step>
</Steps>

***
