# Source: https://docs.xano.com/ai-tools/agents/opentelemetry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using OpenTelemetry with AI Agents

> Learn how to integrate OpenTelemetry with AI agents for enhanced observability and monitoring.

## What is OpenTelemetry?

Connect Xano agents to platforms like Langfuse, LangChain, or Braintrust to make your agent runs easier to understand and improve. After you add your API key, Xano will automatically send agent activity to your chosen tool so you can view run history, trace what happened step-by-step, spot failures or slowdowns, and iterate on prompts and workflows with more confidence.

## Which platforms are supported?

* [Langfuse](https://www.langfuse.com/)
* [LangChain](https://langchain.com/)
* [Braintrust](https://www.braintrust.dev/)

## Which one should I use?

The best choice is simply the one that fits how your team already builds and improves agents. If you’re already using one of these tools, start there. If not, pick the platform whose UI and workflow feel most natural for how you want to review runs, debug issues, and track improvements. And because the setup is just an API key, you can try one, see how it feels, and switch later in Xano with just a couple of clicks.

## Setting up the Integration

### Langfuse

[Langfuse](https://www.langfuse.com/) is an open-source observability platform designed specifically for AI applications. It provides tools to monitor, trace, and analyze the performance of AI agents, making it easier to identify bottlenecks and optimize their behavior.

In Langfuse, create an organization.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/YF1Dc5xzAEpDcwwK/images/opentelemetry-20251202-165253.png?fit=max&auto=format&n=YF1Dc5xzAEpDcwwK&q=85&s=14026a8e24c9f5b8f24d1e4e175ee184" alt="opentelemetry-20251202-165253" width="1260" height="464" data-path="images/opentelemetry-20251202-165253.png" />
</Frame>

Create a new project within your organization.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/YF1Dc5xzAEpDcwwK/images/opentelemetry-20251202-165333.png?fit=max&auto=format&n=YF1Dc5xzAEpDcwwK&q=85&s=e2b1a0bf3cc813beedb3ba99eef744f1" alt="opentelemetry-20251202-165333" width="774" height="479" data-path="images/opentelemetry-20251202-165333.png" />
</Frame>

From your project settings, click on "API Keys" -> "Create new API keys". The API keys created can only be viewed once, so make sure to copy them somewhere safe if you want to refer to them later.

In Xano, head to your agent, and click <span class="ui-bubble">Setup OpenTelemetry Integration</span> under the "Details" tab.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/YF1Dc5xzAEpDcwwK/images/opentelemetry-20251202-165931.png?fit=max&auto=format&n=YF1Dc5xzAEpDcwwK&q=85&s=1d94ab261ffef2efac43b70c09540674" alt="opentelemetry-20251202-165931" width="1151" height="1104" data-path="images/opentelemetry-20251202-165931.png" />
</Frame>

Check the <span class="ui-bubble">Enable</span> box, and fill in your secret key, public key, and base URL from Langfuse.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/YF1Dc5xzAEpDcwwK/images/opentelemetry-20251202-170030.png?fit=max&auto=format&n=YF1Dc5xzAEpDcwwK&q=85&s=66e7dc895301ec7ce5df6e4a4b90910a" alt="opentelemetry-20251202-170030" width="682" height="662" data-path="images/opentelemetry-20251202-170030.png" />
</Frame>

For future executions of your agent, you'll see metrics and traces being sent to Langfuse, where you can analyze them in detail.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/opentelemetry-20251202-170326.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=17ace4de57503df454e2de426fd6c3c8" alt="opentelemetry-20251202-170326" width="1255" height="1017" data-path="images/opentelemetry-20251202-170326.png" />
</Frame>

### LangChain

[LangChain](https://langchain.com/) is a popular framework for building AI applications. It provides built-in support for OpenTelemetry, allowing developers to easily instrument their AI agents for observability.

Create a new project in LangChain, and generate an API key.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/opentelemetry-20251202-170618.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=a3bdd0184443d5dcbff322b6fdee80ba" alt="opentelemetry-20251202-170618" width="1180" height="603" data-path="images/opentelemetry-20251202-170618.png" />
</Frame>

In Xano, head to your agent, and click <span class="ui-bubble">Setup OpenTelemetry Integration</span> under the "Details" tab.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/YF1Dc5xzAEpDcwwK/images/opentelemetry-20251202-165931.png?fit=max&auto=format&n=YF1Dc5xzAEpDcwwK&q=85&s=1d94ab261ffef2efac43b70c09540674" alt="opentelemetry-20251202-165931" width="1151" height="1104" data-path="images/opentelemetry-20251202-165931.png" />
</Frame>

Check the <span class="ui-bubble">Enable</span> box, and fill in your API key from LangChain.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/opentelemetry-20251202-170706.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=b01979da064c57d136b15c86bf4e92d5" alt="opentelemetry-20251202-170706" width="685" height="499" data-path="images/opentelemetry-20251202-170706.png" />
</Frame>

For future executions of your agent, you'll see metrics and traces being sent to LangChain, where you can analyze them in detail.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/opentelemetry-20251202-171020.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=e2fbf1c001bb5df83ee0af351577f347" alt="opentelemetry-20251202-171020" width="1265" height="756" data-path="images/opentelemetry-20251202-171020.png" />
</Frame>

### Braintrust

[Braintrust](https://www.braintrust.dev/) is another observability platform that supports OpenTelemetry for AI applications. It offers features like real-time monitoring, tracing, and alerting to help developers maintain the performance of their AI agents.

In Braintrust, create a new organization.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/opentelemetry-20251202-171222.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=fa67cdab19d2a7dad5a6e0b625d2091e" alt="opentelemetry-20251202-171222" width="683" height="279" data-path="images/opentelemetry-20251202-171222.png" />
</Frame>

Choose **Trace an existing app**

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/opentelemetry-20251202-171255.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=080ea0fe1e007a992eaef05dc9cb4084" alt="opentelemetry-20251202-171255" width="705" height="383" data-path="images/opentelemetry-20251202-171255.png" />
</Frame>

Choose **OpenTelemetry** as your integration method and copy your API key.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/opentelemetry-20251202-171413.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=5692eeba4c4244adce33d52588c7f746" alt="opentelemetry-20251202-171413" width="850" height="1316" data-path="images/opentelemetry-20251202-171413.png" />
</Frame>

In Xano, head to your agent, and click <span class="ui-bubble">Setup OpenTelemetry Integration</span> under the "Details" tab.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/YF1Dc5xzAEpDcwwK/images/opentelemetry-20251202-165931.png?fit=max&auto=format&n=YF1Dc5xzAEpDcwwK&q=85&s=1d94ab261ffef2efac43b70c09540674" alt="opentelemetry-20251202-165931" width="1151" height="1104" data-path="images/opentelemetry-20251202-165931.png" />
</Frame>

Select **Braintrust** from the dropdown, and fill in your API key and project name.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/opentelemetry-20251202-171537.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=da8210e9c1e96fda27c60fad13ce5490" alt="opentelemetry-20251202-171537" width="701" height="595" data-path="images/opentelemetry-20251202-171537.png" />
</Frame>

For future executions of your agent, you'll see metrics and traces being sent to Braintrust, where you can analyze them in detail.

<Frame>
    <img src="https://mintcdn.com/xano-997cb9ee/AXl-sU83thfbeKWS/images/opentelemetry-20251202-171556.png?fit=max&auto=format&n=AXl-sU83thfbeKWS&q=85&s=c9a0af5c2698e27e3279a766451f3353" alt="opentelemetry-20251202-171556" width="1249" height="967" data-path="images/opentelemetry-20251202-171556.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).