# Agent Types and Customization

**Source:** https://github.com/OpenBMB/AgentVerse

AgentVerse provides built-in agent types and supports extensive customization for specialized applications. This guide covers agent types, memory systems, and how to create custom agents.

## Built-in Agent Types

### ConversationAgent

The standard agent type for text-based dialogue and reasoning tasks.

**Features:**
- Natural language generation and understanding
- Memory management through chat history
- Configurable prompts and role descriptions
- Integration with multiple LLM backends
- Support for tool-less interactions

**Example Configuration:**

```yaml
agents:
  - agent_type: conversation
    name: Code Reviewer
    role_description: |
      You are an expert code reviewer with 10+ years of experience.
      Your job is to review code quality, identify bugs, and suggest improvements.
    memory:
      memory_type: chat_history
    prompt_template: |
      You are ${role}.
      Your task: Review the following code
      ${context}
      Provide detailed feedback.
    llm:
      llm_type: gpt-4
      model: gpt-4
      temperature: 0.3
      max_tokens: 1000
```

**Methods:**
- `generate_response()`: Main method for generating agent responses
- `update_memory()`: Stores messages and conversation history
- `fill_prompt_template()`: Instantiates prompt templates with context

### ToolAgent

Specialized agent with capability to use external tools and APIs (requires BMTools and XAgent).

**Features:**
- All ConversationAgent capabilities
- External tool invocation
- Multi-step problem solving with tool chains
- Complex task execution
- System interaction (file operations, code execution, web browsing)

**Example Configuration:**

```yaml
agents:
  - agent_type: tool_agent
    name: Research Agent
    role_description: |
      You are a research agent capable of searching the web,
      reading documents, and synthesizing information.
    tools:
      - web_search
      - file_reader
      - summarizer
    memory:
      memory_type: chat_history
    prompt_template: |
      You have access to the following tools:
      ${tools}
      Task: ${task}
    llm:
      llm_type: gpt-4
      model: gpt-4
      temperature: 0.5
      max_tokens: 2000
```

**Available Tools (via XAgent):**
- Web browsing and search
- File system operations
- Code execution (Jupyter notebooks)
- Shell commands
- Mathematical computation
- API interactions

## Memory Types

### chat_history

Stores the complete conversation history for the agent.

```yaml
memory:
  memory_type: chat_history
```

**Behavior:**
- Maintains sequential message history
- Includes both agent outputs and external inputs
- Used for context in subsequent turns
- Respects context length limits of the LLM

**Example Memory Structure:**

```
[
  {"role": "user", "content": "Write a function to sort an array"},
  {"role": "assistant", "content": "def sort_array(arr): ..."},
  {"role": "user", "content": "Add error handling"},
  {"role": "assistant", "content": "def sort_array(arr): ..."}
]
```

### Future Memory Types

The roadmap includes:
- Vector similarity-based memory
- Hierarchical memory (summary + details)
- Experience replay memory
- Semantic memory

## Customizing Agents

### Method 1: Configuration-Based Customization

For most use cases, customize agents through configuration files:

**1. Define Role and Behavior via Prompt Template:**

```yaml
prompt_template: |
  You are ${role_name}.
  Your responsibilities:
  ${responsibilities}

  Context: ${context}

  Guidelines:
  - Be concise but thorough
  - Provide actionable feedback
  - Ask clarifying questions when needed
```

**2. Adjust LLM Parameters:**

```yaml
llm:
  llm_type: gpt-4
  model: gpt-4
  temperature: 0.3      # Lower for consistency
  max_tokens: 1500      # For detailed responses
  top_p: 0.9           # Nucleus sampling
  frequency_penalty: 0.5
```

**3. Configure Memory Strategy:**

```yaml
memory:
  memory_type: chat_history
  # Future: enable advanced memory strategies
```

### Method 2: Code-Based Customization

For advanced customization, inherit from `BaseAgent`:

```python
from agentverse.agents import BaseAgent

class CustomSearchAgent(BaseAgent):
    """Custom agent with specialized search capabilities."""

    def __init__(self, name, role_description, llm_config, tools=None):
        super().__init__(name, role_description, llm_config)
        self.tools = tools or []
        self.search_cache = {}

    def generate_response(self, prompt):
        """Generate response with custom logic."""
        # Pre-process prompt
        processed_prompt = self._preprocess(prompt)

        # Call parent LLM
        response = super().generate_response(processed_prompt)

        # Post-process if tool-related
        if self._should_use_tool(response):
            response = self._execute_tool(response)

        return response

    def _preprocess(self, prompt):
        """Custom preprocessing logic."""
        # Add search context
        if "search" in prompt.lower():
            context = self._get_cached_searches()
            return f"{prompt}\n\nRecent searches: {context}"
        return prompt

    def _should_use_tool(self, response):
        """Check if response triggers tool usage."""
        return "[TOOL:" in response or "[SEARCH:" in response

    def _execute_tool(self, response):
        """Execute embedded tool commands."""
        # Parse and execute tool calls
        # Return augmented response
        pass
```

Register custom agent:

```python
# In agentverse/agents/__init__.py
from .custom_agents import CustomSearchAgent

__all__ = [
    'ConversationAgent',
    'ToolAgent',
    'CustomSearchAgent',  # Register here
]
```

Use in config:

```yaml
agents:
  - agent_type: custom_search
    name: Smart Researcher
    role_description: You are a research expert...
```

## Advanced Configuration

### Multi-Agent Team Structure

Define specialized team for complex tasks:

```yaml
agents:
  # Planner agent
  - agent_type: conversation
    name: Project Manager
    role_description: You organize and plan the project...
    prompt_template: |
      Create a structured plan for: ${task}
      Output format:
      1. Objectives
      2. Milestones
      3. Resource requirements
    llm:
      llm_type: gpt-4
      model: gpt-4
      temperature: 0.3
      max_tokens: 1500

  # Domain expert agent
  - agent_type: conversation
    name: Technical Lead
    role_description: You provide technical guidance and validation...
    llm:
      llm_type: gpt-4
      model: gpt-4
      temperature: 0.4
      max_tokens: 2000

  # Tool-using agent
  - agent_type: tool_agent
    name: Implementation Agent
    role_description: You execute technical tasks using available tools...
    tools: [code_executor, file_manager, api_client]
    llm:
      llm_type: gpt-4
      model: gpt-4
      temperature: 0.5
      max_tokens: 3000

  # Quality assurance agent
  - agent_type: conversation
    name: QA Specialist
    role_description: You test solutions and validate requirements...
    llm:
      llm_type: gpt-4
      model: gpt-4
      temperature: 0.3
      max_tokens: 1500
```

### Dynamic Temperature Tuning

Adjust temperature per agent based on task:

```yaml
# For consistency (code review)
temperature: 0.1

# For creativity (brainstorming)
temperature: 0.9

# For balanced (general reasoning)
temperature: 0.5
```

### Context Management

Manage context windows for long conversations:

```yaml
llm:
  llm_type: gpt-4
  model: gpt-4
  max_tokens: 2000          # Output limit
  context_window: 8000      # Input limit

memory:
  memory_type: chat_history
  max_history_turns: 10     # Keep last 10 turns only
  # Future: summarize older context
```

## Creating Specialized Agent Classes

### Research Agent

Specialized for information gathering and synthesis:

```python
class ResearchAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sources = []
        self.verified_facts = []

    def generate_response(self, prompt):
        # First: gather information
        sources = self._search_sources(prompt)

        # Second: generate response with sources
        response = super().generate_response(
            f"{prompt}\n\nSources: {sources}"
        )

        # Third: cite sources in response
        return self._add_citations(response)
```

### Creative Agent

Specialized for brainstorming and creative tasks:

```python
class CreativeAgent(BaseAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.llm_config['temperature'] = 0.8
        self.llm_config['top_p'] = 0.95

    def generate_response(self, prompt):
        # Add creativity prompts
        enhanced_prompt = f"{prompt}\n\nBe creative and generate multiple ideas."
        response = super().generate_response(enhanced_prompt)

        # Extract and format ideas
        return self._format_ideas(response)
```

### Validator Agent

Specialized for quality assurance:

```python
class ValidatorAgent(BaseAgent):
    def generate_response(self, prompt):
        response = super().generate_response(prompt)

        # Check response quality
        issues = self._validate_response(response)
        if issues:
            return f"Issues found:\n{issues}\n\nRevised response:\n{response}"
        return response
```

## Best Practices

1. **Clear Role Descriptions**: Write detailed, specific role descriptions
2. **Prompt Engineering**: Invest time in crafting effective prompts
3. **Temperature Selection**: Match temperature to task type
4. **Memory Management**: Balance context length with information retention
5. **Tool Selection**: Carefully choose tools for ToolAgents
6. **Error Handling**: Implement graceful degradation for tool failures
7. **Monitoring**: Log agent responses for quality analysis
8. **Testing**: Test agents individually before multi-agent scenarios

## Troubleshooting

### Agent Ignoring Instructions

- Increase specificity in prompt template
- Lower temperature for consistency
- Add explicit output format requirements

### Memory Issues

- Reduce max_history_turns if context overflows
- Use summarization for long conversations
- Clear memory between unrelated tasks

### Tool Failures

- Verify tool configuration and credentials
- Add error handling in agent logic
- Implement tool execution timeouts
- Log tool calls for debugging
