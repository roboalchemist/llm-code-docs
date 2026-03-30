# Set up model
openai_gpt4o_mini = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=ChatGPTConfig(temperature=0.2).as_dict(),
)
```

## 📹 Monitoring AI Agents with AgentOps

```python Python theme={null}
import agentops
agentops.init(default_tags=["CAMEL cookbook"])
```

```
🖇 AgentOps: Replay: https://app.agentops.ai/drilldown?session_id=e1d4ca98-f21d-4f65-b4b1-
<agentops.session.Session at 0x7abe5582dcc0>
```

## 🛰️ Access Real Time Data with Dappier

Dappier is a powerful tool that connects LLMs to real-time, rights-cleared data from trusted sources, specializing in domains like web search, finance, and news. It delivers enriched, prompt-ready data, empowering AI with verified and up-to-date information for diverse applications. In this section, we will search for the latest news related to CAMEL AI as an example.

```python Python theme={null}
from camel.toolkits import DappierToolkit