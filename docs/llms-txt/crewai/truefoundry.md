# Source: https://docs.crewai.com/en/observability/truefoundry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TrueFoundry Integration

TrueFoundry provides an enterprise-ready [AI Gateway](https://www.truefoundry.com/ai-gateway) which can integrate with agentic frameworks like CrewAI and provides governance and observability for your AI Applications. TrueFoundry AI Gateway serves as a unified interface for LLM access, providing:

* **Unified API Access**: Connect to 250+ LLMs (OpenAI, Claude, Gemini, Groq, Mistral) through one API
* **Low Latency**: Sub-3ms internal latency with intelligent routing and load balancing
* **Enterprise Security**: SOC 2, HIPAA, GDPR compliance with RBAC and audit logging
* **Quota and cost management**: Token-based quotas, rate limiting, and comprehensive usage tracking
* **Observability**: Full request/response logging, metrics, and traces with customizable retention

## How TrueFoundry Integrates with CrewAI

### Installation & Setup

<Steps>
  <Step title="Install CrewAI">
    ```bash  theme={null}
    pip install crewai
    ```
  </Step>

  <Step title="Get TrueFoundry Access Token">
    1. Sign up for a [TrueFoundry account](https://www.truefoundry.com/register)
    2. Follow the steps here in [Quick start](https://docs.truefoundry.com/gateway/quick-start)
  </Step>

  <Step title="Configure CrewAI with TrueFoundry">
        <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=746c0bd23a77535f35b0b2bcf3320bf5" alt="TrueFoundry Code Configuration" data-og-width="2940" width="2940" data-og-height="1664" height="1664" data-path="images/new-code-snippet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=1d7f4e8883760766aa1ae1274fba2ffe 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4604432c1e1121d24c3fa6ad93bc0bd9 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=8dd95282de37aa70090ac61a00b6e1bb 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=920a67bee38e979c770d775195b60864 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4173b6e99ed12b00b54bf3f222589863 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/new-code-snippet.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=176dd84222c8c1a6f40af3e0adb88e37 2500w" />

    ```python  theme={null}
    from crewai import LLM

    # Create an LLM instance with TrueFoundry AI Gateway
    truefoundry_llm = LLM(
        model="openai-main/gpt-4o",  # Similarly, you can call any model from any provider
        base_url="your_truefoundry_gateway_base_url",
        api_key="your_truefoundry_api_key"
    )

    # Use in your CrewAI agents
    from crewai import Agent

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=truefoundry_llm,
            verbose=True
        )
    ```
  </Step>
</Steps>

### Complete CrewAI Example

```python  theme={null}
from crewai import Agent, Task, Crew, LLM

# Configure LLM with TrueFoundry
llm = LLM(
    model="openai-main/gpt-4o",
    base_url="your_truefoundry_gateway_base_url", 
    api_key="your_truefoundry_api_key"
)

# Create agents
researcher = Agent(
    role='Research Analyst',
    goal='Conduct detailed market research',
    backstory='Expert market analyst with attention to detail',
    llm=llm,
    verbose=True
)

writer = Agent(
    role='Content Writer', 
    goal='Create comprehensive reports',
    backstory='Experienced technical writer',
    llm=llm,
    verbose=True
)

# Create tasks
research_task = Task(
    description='Research AI market trends for 2024',
    agent=researcher,
    expected_output='Comprehensive research summary'
)

writing_task = Task(
    description='Create a market research report',
    agent=writer,
    expected_output='Well-structured report with insights',
    context=[research_task]
)

# Create and execute crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

result = crew.kickoff()
```

### Observability and Governance

Monitor your CrewAI agents through TrueFoundry's metrics tab:
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=33755ff848cb457e162e806c20c98216" alt="TrueFoundry metrics" data-og-width="3840" width="3840" data-og-height="1984" height="1984" data-path="images/gateway-metrics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=49a01b5e5bcc0429efd529860c020c10 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=3f47f171146339690e3516a892020626 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=857541d282cce3557f796ade097be01c 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=2f2b883b00e823ceb25ae1b747c656a4 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9ddee789557bdbaacec42fd405180458 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/gateway-metrics.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e9097f84b482e5c4da153d2d0271e6bf 2500w" />

With Truefoundry's AI gateway, you can monitor and analyze:

* **Performance Metrics**: Track key latency metrics like Request Latency, Time to First Token (TTFS), and Inter-Token Latency (ITL) with P99, P90, and P50 percentiles
* **Cost and Token Usage**: Gain visibility into your application's costs with detailed breakdowns of input/output tokens and the associated expenses for each model
* **Usage Patterns**: Understand how your application is being used with detailed analytics on user activity, model distribution, and team-based usage
* **Rate limit and Load balancing**: You can set up rate limiting, load balancing and fallback for your models

## Tracing

For a more detailed understanding on tracing, please see [getting-started-tracing](https://docs.truefoundry.com/docs/tracing/tracing-getting-started).For tracing, you can add the Traceloop SDK:
For tracing, you can add the Traceloop SDK:

```bash  theme={null}
pip install traceloop-sdk
```

```python  theme={null}
from traceloop.sdk import Traceloop

# Initialize enhanced tracing
Traceloop.init(
    api_endpoint="https://your-truefoundry-endpoint/api/tracing",
    headers={
        "Authorization": f"Bearer {your_truefoundry_pat_token}",
        "TFY-Tracing-Project": "your_project_name",
    },
)
```

This provides additional trace correlation across your entire CrewAI workflow.
<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=90623834e0ba9f4ccb09890f6824912d" alt="TrueFoundry CrewAI Tracing" data-og-width="3024" width="3024" data-og-height="1720" height="1720" data-path="images/tracing_crewai.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d05099079060dfd1588ac0c8de28e07b 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=645362e069e687f7dc6fd6c44a97a4ef 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=aac6d42bbd2f457b59f6a4b22d6a7be1 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=7f166e1329cef8da8c1e07a38dc75506 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6e91cffda555b8cc7ce1800ed1b508b1 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/tracing_crewai.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=bf6296110bd62d9bb30ae2d0822d4b8d 2500w" />
