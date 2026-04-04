# Source: https://docs.lunary.ai/docs/integrations/python/azure-openai.md

# Source: https://docs.lunary.ai/docs/integrations/javascript/azure-openai.md

# Source: https://docs.lunary.ai/docs/integrations/azure-openai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure OpenAI integration

Our Python SDK includes automatic integration with Azure OpenAI.

<Steps>
  <Step n="1" title="Setup the SDK">
    ```bash  theme={null}
    pip install openai lunary
    ```
  </Step>

  <Step n="2" title="Monitor AzureOpenAI">
    With our SDKs, tracking AzureOpenAI calls is super simple.

    ```py  theme={null}
    import os
    from openai import AzureOpenAI
    import lunary 

    API_VERSION = os.environ.get("OPENAI_API_VERSION")
    API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
    AZURE_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
    RESOURCE_NAME = os.environ.get("AZURE_OPENAI_RESOURCE_NAME")


    client = AzureOpenAI(
        api_version=API_VERSION,
        azure_endpoint=AZURE_ENDPOINT,
        api_key=API_KEY
    )
    lunary.monitor(client)

    completion = client.chat.completions.create(
        model=RESOURCE_NAME,
        messages=[
            {
                "role": "user",
                "content": "How do I output all files in a directory using Python?",
            },
        ],
    )
    print(completion.to_json())


    ```
  </Step>
</Steps>
