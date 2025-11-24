# Source: https://docs.crewai.com/en/enterprise/features/agent-repositories.md

# Agent Repositories

> Learn how to use Agent Repositories to share and reuse your agents across teams and projects

Agent Repositories allow enterprise users to store, share, and reuse agent definitions across teams and projects. This feature enables organizations to maintain a centralized library of standardized agents, promoting consistency and reducing duplication of effort.

<Frame>
    <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=c2064b8fc57a99dfb8124909b64e0f9d" alt="Agent Repositories" data-og-width="2826" width="2826" data-og-height="1804" height="1804" data-path="images/enterprise/agent-repositories.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=7757e2436d6e4e78349c5116b86ab130 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e9a1e9ed00dd1bcbba6f6fb132877c3c 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=ff4130e977495a27747b10d1591d36da 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=8579f5426a73f5fdc9fc9cb8e27b48c1 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=823d4391f0bc0f6e6dd110d1ad1a0936 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/agent-repositories.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=3f7c480281557b5878d469cdb554bc8d 2500w" />
</Frame>

## Benefits of Agent Repositories

* **Standardization**: Maintain consistent agent definitions across your organization
* **Reusability**: Create an agent once and use it in multiple crews and projects
* **Governance**: Implement organization-wide policies for agent configurations
* **Collaboration**: Enable teams to share and build upon each other's work

## Creating and Use Agent Repositories

1. You must have an account at CrewAI, try the [free plan](https://app.crewai.com).
2. Create agents with specific roles and goals for your workflows.
3. Configure tools and capabilities for each specialized assistant.
4. Deploy agents across projects via visual interface or API integration.

<Frame>
    <img src="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=837a5d30ad32f8cd5e0bda08638c4c4d" alt="Agent Repositories" data-og-width="3434" width="3434" data-og-height="2266" height="2266" data-path="images/enterprise/create-agent-repository.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=280&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=e9c4e5cb3e880f3fb28aa098d06eec7b 280w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=560&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=1710435d332fcd75ac8ee3dc0fe37a0b 560w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=840&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=ccba8e2687317ebbf5aee8e29832d5eb 840w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=1100&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=f7f51e57c76fea4f276be1c70e868620 1100w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=1650&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=0b74c722fb36c470635d3ade22c53cde 1650w, https://mintcdn.com/crewai/Grq_Qb7_m8o-TQ5O/images/enterprise/create-agent-repository.png?w=2500&fit=max&auto=format&n=Grq_Qb7_m8o-TQ5O&q=85&s=f69253ad1472a9f6bad48c3627f7b5d1 2500w" />
</Frame>

### Loading Agents from Repositories

You can load agents from repositories in your code using the `from_repository` parameter to run locally:

```python  theme={null}
from crewai import Agent

# Create an agent by loading it from a repository
# The agent is loaded with all its predefined configurations
researcher = Agent(
    from_repository="market-research-agent"
)
```

### Overriding Repository Settings

You can override specific settings from the repository by providing them in the configuration:

```python  theme={null}
researcher = Agent(
    from_repository="market-research-agent",
    goal="Research the latest trends in AI development",  # Override the repository goal
    verbose=True  # Add a setting not in the repository
)
```

### Example: Creating a Crew with Repository Agents

```python  theme={null}
from crewai import Crew, Agent, Task

# Load agents from repositories
researcher = Agent(
    from_repository="market-research-agent"
)

writer = Agent(
    from_repository="content-writer-agent"
)

# Create tasks
research_task = Task(
    description="Research the latest trends in AI",
    agent=researcher
)

writing_task = Task(
    description="Write a comprehensive report based on the research",
    agent=writer
)

# Create the crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

# Run the crew
result = crew.kickoff()
```

### Example: Using `kickoff()` with Repository Agents

You can also use repository agents directly with the `kickoff()` method for simpler interactions:

```python  theme={null}
from crewai import Agent
from pydantic import BaseModel
from typing import List

# Define a structured output format
class MarketAnalysis(BaseModel):
    key_trends: List[str]
    opportunities: List[str]
    recommendation: str

# Load an agent from repository
analyst = Agent(
    from_repository="market-analyst-agent",
    verbose=True
)

# Get a free-form response
result = analyst.kickoff("Analyze the AI market in 2025")
print(result.raw)  # Access the raw response

# Get structured output
structured_result = analyst.kickoff(
    "Provide a structured analysis of the AI market in 2025",
    response_format=MarketAnalysis
)

# Access structured data
print(f"Key Trends: {structured_result.pydantic.key_trends}")
print(f"Recommendation: {structured_result.pydantic.recommendation}")
```

## Best Practices

1. **Naming Convention**: Use clear, descriptive names for your repository agents
2. **Documentation**: Include comprehensive descriptions for each agent
3. **Tool Management**: Ensure that tools referenced by repository agents are available in your environment
4. **Access Control**: Manage permissions to ensure only authorized team members can modify repository agents

## Organization Management

To switch between organizations or see your current organization, use the CrewAI CLI:

```bash  theme={null}
# View current organization
crewai org current

# Switch to a different organization
crewai org switch <org_id>

# List all available organizations
crewai org list
```

<Note>
  When loading agents from repositories, you must be authenticated and switched to the correct organization. If you receive errors, check your authentication status and organization settings using the CLI commands above.
</Note>
