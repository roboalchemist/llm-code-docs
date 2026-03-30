# Source: https://console.groq.com/docs/crewai

---
description: Learn how to use CrewAI with Groq to orchestrate fast, scalable teams of AI agents for complex workflows and rapid decision-making.
title: CrewAI + Groq: High-Speed Agent Orchestration - GroqDocs
image: https://console.groq.com/og_cloudv5.jpg
---

## [CrewAI + Groq: High-Speed Agent Orchestration](#crewai--groq-highspeed-agent-orchestration)

CrewAI is a framework that enables the orchestration of multiple AI agents with specific roles, tools, and goals as a cohesive team to accomplish complex tasks and create sophisticated workflows.

Agentic workflows require fast inference due to their complexity. Groq's fast inference optimizes response times for CrewAI agent teams, enabling rapid autonomous decision-making and collaboration for:

* **Fast Agent Interactions:** Leverage Groq's fast inference speeds via Groq API for efficient agent communication
* **Reliable Performance:** Consistent response times across agent operations
* **Scalable Multi-Agent Systems:** Run multiple agents in parallel without performance degradation
* **Simple Integration:** Get started with just a few lines of code

### [Python Quick Start (2 minutes to hello world)](#python-quick-start-2-minutes-to-hello-world)

#### [1\. Install the required packages:](#1-install-the-required-packages)

curl

```
pip install crewai groq
```

#### [2\. Configure your Groq API key:](#2-configure-your-groq-api-key)

curl

```
export GROQ_API_KEY="your-api-key"
```

#### [3\. Create your first Groq-powered CrewAI agent:](#3-create-your-first-groqpowered-crewai-agent)

In CrewAI, **agents** are autonomous entities you can design to perform specific roles and achieve particular goals while **tasks** are specific assignments given to agents that detail the actions they need to perform to achieve a particular goal. Tools can be assigned as tasks.

Python

```
from crewai import Agent, Task, Crew, LLM

# Initialize Large Language Model (LLM) of your choice (see all models on our Models page)
llm = LLM(model="groq/llama-3.1-70b-versatile")

# Create your CrewAI agents with role, main goal/objective, and backstory/personality
summarizer = Agent(
    role='Documentation Summarizer', # Agent's job title/function
    goal='Create concise summaries of technical documentation', # Agent's main objective
    backstory='Technical writer who excels at simplifying complex concepts', # Agent's background/expertise
    llm=llm, # LLM that powers your agent
    verbose=True # Show agent's thought process as it completes its task
)

translator = Agent(
    role='Technical Translator',
    goal='Translate technical documentation to other languages',
    backstory='Technical translator specializing in software documentation',
    llm=llm,
    verbose=True
)

# Define your agents' tasks
summary_task = Task(
    description='Summarize this React hook documentation:\n\nuseFetch(url) is a custom hook for making HTTP requests. It returns { data, loading, error } and automatically handles loading states.',
    expected_output="A clear, concise summary of the hook's functionality",
    agent=summarizer # Agent assigned to task
)

translation_task = Task(
    description='Translate the summary to Turkish',
    expected_output="Turkish translation of the hook documentation",
    agent=translator,
    dependencies=[summary_task] # Must run after the summary task
)

# Create crew to manage agents and task workflow
crew = Crew(
    agents=[summarizer, translator], # Agents to include in your crew
    tasks=[summary_task, translation_task], # Tasks in execution order
    verbose=True
)

result = crew.kickoff()
print(result)
```

When you run the above code, you'll see that you've created a summarizer agent and a translator agent working together to summarize and translate documentation! This is a simple example to get you started, but the agents are also able to use tools, which is a powerful combination for building agentic workflows.

**Challenge**: Update the code to add an agent that will write up documentation for functions its given by the user!

### [Advanced Model Configuration](#advanced-model-configuration)

For finer control over your agents' responses, you can easily configure additional model parameters. These settings help you balance between creative and deterministic outputs, control response length, and manage token usage:

Python

```
llm = LLM(
    model="llama-3.1-70b-versatile",
    temperature=0.5,
    max_completion_tokens=1024,
    top_p=0.9,
    stop=None,
    stream=False,
)
```

For more robust documentation and further resources, including using CrewAI agents with tools for building a powerful agentic workflow, see the following:

* [Official Documentation: CrewAI](https://docs.crewai.com/concepts/llms)
* [Groq API Cookbook: CrewAI Mixture of Agents Tutorial](https://github.com/groq/groq-api-cookbook/tree/main/tutorials/crewai-mixture-of-agents)
* [Webinar: Build CrewAI Agents with Groq](https://youtu.be/Q3fh0sWVRX4?si=fhMLPsBF5OBiMfjD)