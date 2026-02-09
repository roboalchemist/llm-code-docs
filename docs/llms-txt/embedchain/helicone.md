# Source: https://docs.embedchain.ai/integration/helicone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🧊 Helicone

> Implement Helicone, the open-source LLM observability platform, with Embedchain. Monitor, debug, and optimize your AI applications effortlessly.

Get started with [Helicone](https://www.helicone.ai/), the open-source LLM observability platform for developers to monitor, debug, and optimize their applications.

To use Helicone, you need to do the following steps.

## Integration Steps

<Steps>
  <Step title="Create an account + Generate an API Key">
    Log into [Helicone](https://www.helicone.ai) or create an account. Once you have an account, you
    can generate an [API key](https://helicone.ai/developer).

    <Note>
      Make sure to generate a [write only API key](helicone-headers/helicone-auth).
    </Note>
  </Step>

  <Step title="Set base_url in the your code">
    You can configure your base\_url and OpenAI API key in your codebase

    <CodeGroup>
      ```python main.py theme={null}
      import os
      from embedchain import App

      # Modify the base path and add a Helicone URL
      os.environ["OPENAI_API_BASE"] = "https://oai.helicone.ai/{YOUR_HELICONE_API_KEY}/v1"
      # Add your OpenAI API Key
      os.environ["OPENAI_API_KEY"] = "{YOUR_OPENAI_API_KEY}"

      app = App()

      # Add data to your app
      app.add("https://en.wikipedia.org/wiki/Elon_Musk")

      # Query your app
      print(app.query("How many companies did Elon found? Which companies?"))
      ```
    </CodeGroup>
  </Step>

  <Step title="Now you can see all passing requests through Embedchain in Helicone">
    <img src="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/helicone-embedchain.png?fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=3455738c4278b838b11f36648ad33be4" alt="Embedchain requests" data-og-width="3024" width="3024" data-og-height="1538" height="1538" data-path="images/helicone-embedchain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/helicone-embedchain.png?w=280&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=c4565530813ffda0d501f9b81e3356a4 280w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/helicone-embedchain.png?w=560&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=628666c3e6a3aa1d444aaeb1bd990190 560w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/helicone-embedchain.png?w=840&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=9d14eb377a4dd3c7d249695c901e6e72 840w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/helicone-embedchain.png?w=1100&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=885a6e26b9e78186d360619e3bb86a8f 1100w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/helicone-embedchain.png?w=1650&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=f9e5c35a8f38cde1ee1c08fd4694bd30 1650w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/helicone-embedchain.png?w=2500&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=5ebe76bd1b5ab86e2fd8d15c2a5c1258 2500w" />
  </Step>
</Steps>

Check out [Helicone](https://www.helicone.ai) to see more use cases!
