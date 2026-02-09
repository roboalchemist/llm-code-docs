# Source: https://docs.helicone.ai/other-integrations/dify.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Dify

> Dify is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production. Here is how to get Observability and logs for your dify instance.

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

## Introduction

Dify is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features and more, letting you quickly go from prototype to production.

## Integration Steps

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).

    <Note>
      Make sure to generate a [write only API key](helicone-headers/helicone-auth).
    </Note>
  </Step>

  <Step title="Configure API Base in Dify to use Helicone">
    Choose whichever provider you are using that is [supported by Helicone](/getting-started/integration-method/gateway#approved-domains). Here is an example using OpenAI.

    <Frame caption="Set your API base to the Helicone API URL with your API key in the path.">
      <img src="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/integrations/dify.png?fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=3ea08f4b5844ad4f38c379d4a5c08b39" alt="dify example" data-og-width="1368" width="1368" data-og-height="886" height="886" data-path="images/integrations/dify.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/integrations/dify.png?w=280&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=004648b5dd43c0a1847ac54e4e6e7994 280w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/integrations/dify.png?w=560&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=06ddb9e02493afba01c214c3e440c843 560w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/integrations/dify.png?w=840&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=fd8d3ca1856f4efa70cf48983a56c3cd 840w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/integrations/dify.png?w=1100&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=4d4d5485f4ce3609bc13199d86729503 1100w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/integrations/dify.png?w=1650&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=e2147b8a8acc61889e40bd25d0eccae3 1650w, https://mintcdn.com/helicone/NVRJN0bOLLl-z8a0/images/integrations/dify.png?w=2500&fit=max&auto=format&n=NVRJN0bOLLl-z8a0&q=85&s=87ac7550f2f83bc6e4e0d27603203a8a 2500w" />
    </Frame>

    It's that simple!
  </Step>
</Steps>

Check out the [Open Devin GitHub repository](https://github.com/OpenDevin/OpenDevin) for more information and examples.
