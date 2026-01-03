# Source: https://www.traceloop.com/docs/integrations/posthog.md

# Posthog

> Connect Traceloop to Posthog to combine LLM insights with your product analytics

Connecting Traceloop to Posthog can be done by following these steps:

<Steps>
  <Step title="Get the needed data from Posthog">
    Go to your Posthog instance settings and get the following data:

    * API URL (should be something like `https://us.i.posthog.com`)
    * Project API key (should be in the format `phc_-<key>`)
  </Step>

  <Step title="Set up the Integration within Traceloop">
    Go to the [integrations page](https://app.traceloop.com/settings/integrations) within Traceloop and click on the Posthog card.

    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=35ac5fe45caf3c3530228c0a3b0bff35" data-og-width="2570" width="2570" data-og-height="1536" height="1536" data-path="img/traceloop-integrations/integrations-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=280&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=7808c9d3c6effed886279981cedd62ef 280w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=560&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=c34accf8f8506402b2a1206d1fbc9bb1 560w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=840&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=da7f7d0802920e44a2b77dad15c5e0e5 840w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=1100&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=7bc22776339cf7dc4fb8fdd1d8fae87d 1100w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=1650&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=cbbd5dc3dfc7c05bbde8a7d5c072b623 1650w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-light.png?w=2500&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=6f81b4b7119103acf0aa0e70b5be2dfc 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=23c023f1759a68c3fd35cf8d58b5e4e2" data-og-width="2570" width="2570" data-og-height="1536" height="1536" data-path="img/traceloop-integrations/integrations-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=280&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=7e01c6589cfc972a43bcbe0b5cb9ac43 280w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=560&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=2277536bbdef309a55006740413c2bd5 560w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=840&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=77276213c59309e1e435bae21852f088 840w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=1100&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=8fb7db7d10a5a5b0ac27b72e654c12dd 1100w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=1650&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=6a91559b2ce8ad7173298530618e21db 1650w, https://mintcdn.com/enrolla/pLLlNcf8Qyyp9R0l/img/traceloop-integrations/integrations-dark.png?w=2500&fit=max&auto=format&n=pLLlNcf8Qyyp9R0l&q=85&s=b5f88909d17b892d0e2a6bc6a0233bc3 2500w" />
    </Frame>
  </Step>

  <Step title="Fill in the form">
    Fill in the data you got from Posthog. Choose the environment you want to connect to Posthog and click on "Enable".

    <Frame>
      <img className="block dark:hidden" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-light.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=a1fb090cc7ba9861de483fbfb2f415fd" data-og-width="3024" width="3024" data-og-height="1807" height="1807" data-path="img/traceloop-integrations/posthog-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-light.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=09353a6fe2ad0902f66e04d5f9f98092 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-light.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=60ab41c155a36b19d7941543b5a76c38 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-light.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=431b7fb1fb8ef5d44dc0eecad86c6ca2 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-light.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=82151fda3d78b4d1f1c6515221352de8 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-light.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=aaa9f6e686f9fd640eaa95c18aeaeee5 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-light.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=650d7d3735dea738963406a65e7e4b5f 2500w" />

      <img className="hidden dark:block" src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-dark.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=cbb35b1346f438ac29dc3166ceb62228" data-og-width="3005" width="3005" data-og-height="1801" height="1801" data-path="img/traceloop-integrations/posthog-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-dark.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=dd1e1a62e3663225c7755a755277dab4 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-dark.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=194dc74f216052676ab53220be23abc7 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-dark.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=e1d98c1b13e363d00e1a90875685406d 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-dark.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=1873606fa8294a7e25b894486509312e 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-dark.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=f9a95d146326ea645a68beed1afb7e90 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-dark.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=6c4c2279b571a7f75d0a1de29673805d 2500w" />
    </Frame>
  </Step>
</Steps>

**That's it!**

Go to your Posthog instance, click "Activity" and search for events named `traceloop span`.

You can then create a new dashboard from the "LLM Metrics - Traceloop" template to visualize the data.

<Frame>
  <img src="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-result.png?fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=a7ac3ec7d419d08964c981d15789798c" data-og-width="1619" width="1619" data-og-height="1062" height="1062" data-path="img/traceloop-integrations/posthog-result.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-result.png?w=280&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=92dada6eaa3fd060cbc86aecd6e965a6 280w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-result.png?w=560&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=87d2c7b2c184818f67a3101db7dcaae9 560w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-result.png?w=840&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=e89cd13fc2abc56e8cee7f0467d7e429 840w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-result.png?w=1100&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=2b11d75fb13d0f8b97e522087e02915e 1100w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-result.png?w=1650&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=637e2c22dac14bf939a82002801390cd 1650w, https://mintcdn.com/enrolla/GspX1ocwd1gETLy0/img/traceloop-integrations/posthog-result.png?w=2500&fit=max&auto=format&n=GspX1ocwd1gETLy0&q=85&s=2809ac33a86e1683caaeeb85c3bbe654 2500w" />
</Frame>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt