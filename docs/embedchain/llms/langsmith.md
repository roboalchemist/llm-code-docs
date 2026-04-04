# Source: https://docs.embedchain.ai/integration/langsmith.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🛠️ LangSmith

> Integrate with Langsmith to debug and monitor your LLM app

Embedchain now supports integration with [LangSmith](https://www.langchain.com/langsmith).

To use LangSmith, you need to do the following steps.

1. Have an account on LangSmith and keep the environment variables in handy
2. Set the environment variables in your app so that embedchain has context about it.
3. Just use embedchain and everything will be logged to LangSmith, so that you can better test and monitor your application.

Let's cover each step in detail.

* First make sure that you have created a LangSmith account and have all the necessary variables handy. LangSmith has a [good documentation](https://docs.smith.langchain.com/) on how to get started with their service.

* Once you have setup the account, we will need the following environment variables

```bash  theme={null}
# Setting environment variable for LangChain Tracing V2 integration.
export LANGCHAIN_TRACING_V2=true

# Setting the API endpoint for LangChain.
export LANGCHAIN_ENDPOINT=https://api.smith.langchain.com

# Replace '<your-api-key>' with your LangChain API key.
export LANGCHAIN_API_KEY=<your-api-key>

# Replace '<your-project>' with your LangChain project name, or it defaults to "default".
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

If you are using Python, you can use the following code to set environment variables

```python  theme={null}
import os

# Setting environment variable for LangChain Tracing V2 integration.
os.environ['LANGCHAIN_TRACING_V2'] = 'true'

# Setting the API endpoint for LangChain.
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'

# Replace '<your-api-key>' with your LangChain API key.
os.environ['LANGCHAIN_API_KEY'] = '<your-api-key>'

# Replace '<your-project>' with your LangChain project name.
os.environ['LANGCHAIN_PROJECT'] = '<your-project>'
```

* Now create an app using Embedchain and everything will be automatically visible in the LangSmith

```python  theme={null}
from embedchain import App

# Initialize EmbedChain application.
app = App()

# Add data to your app
app.add("https://en.wikipedia.org/wiki/Elon_Musk")

# Query your app
app.query("How many companies did Elon found?")
```

* Now the entire log for this will be visible in langsmith.

<img src="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/langsmith.png?fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=06d8ab160f491be049d2c87ffc9ca71a" data-og-width="2880" width="2880" data-og-height="1652" height="1652" data-path="images/langsmith.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/langsmith.png?w=280&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=792f350e1e8b360664b0b47fc1286516 280w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/langsmith.png?w=560&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=c252d56b240bf74e8348abd9b0a58a83 560w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/langsmith.png?w=840&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=57bd37f97838f565475ae5a060214a6c 840w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/langsmith.png?w=1100&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=fc182e82518a6f1a1a88afc4eb9c5903 1100w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/langsmith.png?w=1650&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=8a38f57705c251642b1781508c24873c 1650w, https://mintcdn.com/embedchain/pz6fpRISI4B6JS6w/images/langsmith.png?w=2500&fit=max&auto=format&n=pz6fpRISI4B6JS6w&q=85&s=6a8cdef62a36f7160e1700cfdfaa35d1 2500w" />
