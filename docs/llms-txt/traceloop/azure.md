# Source: https://www.traceloop.com/docs/openllmetry/integrations/azure.md

# Azure Application Insights

Traceloop supports sending traces to Azure Application Insights via standard OpenTelemetry integrations.

Review how to setup [OpenTelemetry with Python in Azure Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=python).

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/azure.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=ecfe3e97ec2d052dbfd69b0c4f301376" data-og-width="1849" width="1849" data-og-height="949" height="949" data-path="img/integrations/azure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/azure.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=4c2ca75f71c6b159b95ee541309e35df 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/azure.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=7efd762c983955a1e18094cc3559f176 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/azure.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=790a4cfe37e0e44ca210f131db4e5ef8 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/azure.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=6c1a9d3a2911ac34717410bcc17fd8c7 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/azure.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e36803b394f3b0907a8294c35c33b489 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/azure.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=aa19a1dc53ff72348e29e79623e45fd8 2500w" />
</Frame>

1. Provision an Application Insights instance in the [Azure portal](https://portal.azure.com/).
2. Get your Connection String from the instance - [details here](https://learn.microsoft.com/en-us/azure/azure-monitor/app/sdk-connection-string?tabs=python).
3. Install required packages

```bash  theme={null}
pip install azure-monitor-opentelemetry-exporter traceloop-sdk openai
```

4. Example implementation

```python  theme={null}
import os
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow, task, agent, tool
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Configure the tracer provider to export traces to Azure Application Insights.
# Get your complete connection string from the Azure Portal or CLI.
exporter = AzureMonitorTraceExporter(connection_string="INSERT_CONNECTION_STRING_HERE")

# Pass your exporter to Traceloop
Traceloop.init(app_name="your_app_name", exporter=exporter)


@task(name="joke_creation")
def create_joke():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Tell me a joke about opentelemetry"}],
    )

    return completion.choices[0].message.content

@task(name="signature_generation")
def generate_signature(joke: str):
    completion = client.completions.create(model="davinci-002",
    prompt="add a signature to the joke:\n\n" + joke)

    return completion.choices[0].text

@agent(name="joke_translation")
def translate_joke_to_pirate(joke: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Translate the below joke to pirate-like english:\n\n{joke}"}],
    )

    history_jokes_tool()

    return completion.choices[0].message.content


@tool(name="history_jokes")
def history_jokes_tool():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"get some history jokes"}],
    )

    return completion.choices[0].message.content


@workflow(name="pirate_joke_generator")
def joke_workflow():
    eng_joke = create_joke()
    pirate_joke = translate_joke_to_pirate(eng_joke)
    signature = generate_signature(pirate_joke)
    print(pirate_joke + "\n\n" + signature)
    
if __name__ == "__main__":
    joke_workflow()
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://www.traceloop.com/docs/llms.txt