# Source: https://docs.lunary.ai/docs/integrations/ollama.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Ollama Integration

Ollama allow you to self-host quickly large language models.
Our SDKs include automatic integrations with Ollama.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={2}>
      <Card title="Python" icon="python" href="/docs/integrations/python/installation">
        Learn how to set up the Python SDK.
      </Card>

      <Card title="Javascript" icon="js" href="/docs/integrations/javascript/installation">
        Learn how to set up the JavaScript SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Monitor Ollama">
    With our SDKs, tracking Ollama calls is super simple.

    <Tabs>
      <Tab title="Python" icon="python">
        ```py  theme={null}
        from openai import OpenAI
        import lunary

        client = OpenAI(
        base_url='http://localhost:11434/v1/', # replace by your Ollama base url
        api_key='ollama', #required but ignored
        )

        lunary.monitor(client)

        chat_completion = client.chat.completions.create(
        messages=[
        {
        'role': 'user',
        'content': 'Say this is a test',
        }
        ],  
         model='llama3.2',
        )

        ```
      </Tab>

      <Tab title="Javascript">
        ```js  theme={null}
        import OpenAI from 'openai'
        import { monitorOpenAI } from "lunary/openai"

        const openai = monitorOpenAI(new OpenAI({
          baseURL: 'http://localhost:11434/v1/', //  replace by your Ollama base url
          apiKey: 'ollama', // required but ignored
        }))

        const chatCompletion = await openai.chat.completions.create({
            messages: [{ role: 'user', content: 'Say this is a test' }],
            model: 'llama3.2',
        })
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>
