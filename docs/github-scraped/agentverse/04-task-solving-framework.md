# Task-Solving Framework

**Source:** https://github.com/OpenBMB/AgentVerse

The Task-Solving Framework assembles multiple agents as an automatic multi-agent system to collaboratively accomplish complex tasks. This framework is ideal for real-world applications like software development, consulting, code generation, and problem-solving.

## Overview

The task-solving framework enables:
- Automatic coordination of multiple specialized agents
- Collaborative problem-solving and code generation
- Tool usage for web browsing, file operations, and computations
- Benchmark evaluation on standard datasets
- Support for various LLM backends (OpenAI, Azure, vLLM, local models)

## Key Applications

- **Software Development**: Automated code writing, testing, and reviewing
- **Code Generation**: Solving programming challenges and benchmarks
- **Consulting Systems**: Multi-expert systems providing comprehensive solutions
- **Problem Solving**: Complex tasks requiring multiple specialized agents
- **Tool Usage**: Agents using browsers, notebooks, search APIs, and more

## Running Task-Solving Examples

### Benchmark Evaluation

Evaluate agents on standard benchmarks like HumanEval:

```bash
agentverse-benchmark --task tasksolving/humaneval/gpt-3.5 \
    --dataset_path data/humaneval/test.jsonl \
    --overwrite
```

**Configuration path:** `agentverse/tasks/tasksolving/humaneval/gpt-3.5/config.yaml`

### Single Query Tasks

Run agents on specific problems (task defined in config file):

```bash
agentverse-tasksolving --task tasksolving/brainstorming
```

**Configuration path:** `agentverse/tasks/tasksolving/brainstorming/gpt-3.5/config.yaml`

### Tool-Using Tasks

For multi-agent systems using external tools (web browser, Jupyter, Bing search, etc.):

#### 1. Set up XAgent ToolsServer

Follow the [XAgent ToolsServer setup guide](https://github.com/OpenBMB/XAgent#%EF%B8%8F-build-and-setup-toolserver) to build and run the ToolServer.

#### 2. Run Tool-Using Task

```bash
agentverse-tasksolving --task tasksolving/tool_using/24point
```

Additional tool-using tasks are provided in `agentverse/tasks/tasksolving/tool_using/`.

## Available Tasks

### Code Generation Tasks

Located in `agentverse/tasks/tasksolving/`:

- **humaneval/**: Code generation on standard HumanEval benchmarks
- **brainstorming/**: Creative problem-solving with multiple agents
- **commongen/**: Common sense generation tasks
- **sde_team/**: Software development with code writer, tester, reviewer

### Tool-Using Tasks

Located in `agentverse/tasks/tasksolving/tool_using/`:

Demonstrates how multiple agents can coordinate to use various tools:
- Web browsing
- File system operations
- Jupyter notebook execution
- Bing search integration
- WolframAlpha computation

Examples include:
- `24point`: Mathematical game solving
- Custom problem-solving tasks

## Configuration Structure

Task-solving configurations specify agent roles, LLM settings, and environment parameters:

```yaml
environment:
  env_type: tasksolving
  max_turns: 30
  rule:
    order:
      type: sequential
    visibility:
      type: all
    selector:
      type: basic
    updater:
      type: basic
    describer:
      type: task_describer

agents:
  - agent_type: conversation
    name: Code Writer
    role_description: You are an expert programmer...
    prompt_template: |
      Your specialized prompt here
    llm:
      llm_type: gpt-4
      model: gpt-4
      temperature: 0.7
      max_tokens: 2000

  - agent_type: tool_agent
    name: Code Tester
    role_description: You review and test code...
    tools: [bash_tool, python_tool]
    llm:
      llm_type: gpt-4
      model: gpt-4
```

## LLM Configuration

### OpenAI Models

```yaml
llm:
  llm_type: openai
  model: gpt-4
  temperature: 0.7
  max_tokens: 2000
```

### Azure OpenAI

```yaml
llm:
  llm_type: azure
  model: gpt-4-deployment-name
  temperature: 0.7
  max_tokens: 2000
```

### vLLM (Local Large Models)

```yaml
llm:
  llm_type: vllm
  model: llama-2-70b-chat-hf
  temperature: 0.7
  max_tokens: 2000
```

Configure environment variables:
```bash
export VLLM_API_KEY="your_api_key"
export VLLM_API_BASE="http://localhost:8000"
```

### Local Models (FastChat)

```yaml
llm:
  llm_type: local
  model: llama-2-7b-chat-hf
  temperature: 0.7
  max_tokens: 2000
```

See [Installation and Setup](02-installation-and-setup.md) for local model configuration.

## Framework Required Modules

The task-solving framework uses:

```
- agentverse
  - agents
    - simulation_agent
  - environments
    - tasksolving_env
```

## Agent Types

### ConversationAgent

Standard agent for dialogue and problem-solving tasks.

**Capabilities:**
- Text generation and reasoning
- Memory management
- Prompt templating
- LLM integration

### ToolAgent

Agent with external tool usage capabilities (requires BMTools and XAgent ToolsServer).

**Capabilities:**
- Everything from ConversationAgent
- Tool invocation and orchestration
- Complex multi-step problem solving
- File and system operations

## Memory Management

Agents support multiple memory types:

```yaml
memory:
  memory_type: chat_history  # Stores full conversation history
```

Future enhancements will support more sophisticated memory strategies.

## Output Parsing

Agents generate structured outputs that are parsed by custom parsers. Example format:

```
Action: Write Code
Action Input:
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

Parsers extract structured information from agent outputs for task evaluation.

## Customization Guidelines

### Creating Custom Task-Solving Scenarios

1. Create task directory: `agentverse/tasks/tasksolving/your_task/`
2. Define configuration: `config.yaml`
3. Implement output parser for agent responses
4. Register parser in `agentverse/tasks/__init__.py`

### Customizing Agents

Inherit from `BaseAgent` class for specialized agent behavior:

```python
class CustomAgent(BaseAgent):
    def __init__(self, name, role_description, ...):
        super().__init__(name, role_description, ...)

    def generate_response(self, prompt):
        # Custom response generation logic
        pass
```

### Customizing Environments

For specialized task-solving environments, inherit from `BaseEnvironment` and implement custom execution logic.

## Best Practices

1. **Agent Roles**: Clearly define specialized roles for each agent
2. **Prompts**: Craft detailed prompts that guide agent behavior
3. **Temperature**: Use lower temperatures (0.3-0.5) for deterministic tasks, higher (0.7-0.9) for creative tasks
4. **Context Length**: Monitor max_tokens to ensure complete outputs
5. **Tool Integration**: Test tools before multi-agent execution
6. **Evaluation**: Use standardized benchmarks to measure performance
7. **Iteration**: Start with simple tasks, progressively add complexity

## Related Work

The Task-Solving Framework is based on research published in:

- [AgentVerse: Facilitating Multi-Agent Collaboration](https://arxiv.org/abs/2308.10848) - ICLR 2024
- [Multi-agent as System](https://arxiv.org/abs/2309.02427)

See the research paper for detailed algorithms and performance comparisons.

## Troubleshooting

### Agents Not Responding

1. Check LLM API credentials and rate limits
2. Verify prompt templates are valid
3. Check agent memory and context length settings

### Tools Not Working

1. Ensure XAgent ToolsServer is running
2. Verify tool configuration in agent definition
3. Check tool API credentials and permissions

### Low Performance

1. Improve prompt engineering
2. Experiment with different agent roles and specializations
3. Adjust temperature and max_tokens
4. Use stronger models (GPT-4 vs GPT-3.5)
