# Simulation Framework

**Source:** https://github.com/OpenBMB/AgentVerse

The Simulation Framework allows you to create custom multi-agent environments where agents interact, collaborate, and exhibit emergent behaviors. This framework is ideal for research on agent behavior, games, and social dynamics.

## Overview

The simulation framework enables:
- Custom environment creation with configurable rules
- Multi-agent interaction and coordination
- Observation of emergent behaviors
- Interactive scenarios with agent participation

## Running Simulations

### CLI Example

Launch a pre-built simulation scenario using the CLI:

```bash
agentverse-simulation --task simulation/nlp_classroom_3players
```

This example runs a basic 3-player classroom with professor, student, and teaching assistant.

### GUI Example

Launch a local web-based interface for visualization and interaction:

```bash
agentverse-simulation-gui --task simulation/nlp_classroom_9players
```

After starting the server, visit `http://127.0.0.1:7860/` to view and interact with the environment.

## Built-in Examples

### 1. NLP Classroom

A realistic classroom environment where:
- One agent acts as the professor
- Multiple agents are students
- Students raise their hands to ask questions
- Professor calls on students for their questions

**Run it:**
```bash
agentverse-simulation-gui --task simulation/nlp_classroom_9players
```

### 2. Prisoner's Dilemma

A game-theory scenario featuring:
- Two rational agents facing a strategic choice
- Options to cooperate for mutual benefit or betray for individual gain
- Study of rational decision-making in multi-agent systems

**Run it:**
```bash
agentverse-simulation-gui --task simulation/prisoner_dilemma
```

### 3. Software Design Environment

A collaborative development scenario with:
- Code Writer agent: generates code implementation
- Code Tester agent: runs unit tests and provides feedback
- Code Reviewer agent: reviews code quality
- Iterative refinement process

**Run it:**
```bash
agentverse-simulation-gui --task simulation/sde_team/sde_team_2players
```

### 4. Database Administrator (DBA) Monitoring

A system monitoring scenario where:
- Chief DBA monitors system anomalies (slow queries, locks, crashes)
- Domain expert agents analyze root causes
- Team provides recommendations and optimization solutions
- Chief DBA generates diagnostic reports

**Run it:**
```bash
agentverse-simulation-gui --task simulation/db_diag
```

### 5. Pokemon Game

**Available in [`release-0.1` branch](https://github.com/OpenBMB/AgentVerse/tree/release-0.1)**

An interactive game environment featuring:
- 6 Pokemon Emerald characters (May, Professor Birch, Steven Stone, Maxie, Archie, Joseph)
- Free movement and interaction between agents
- Player can engage with agent characters as another agent
- WASD controls for movement, SPACE for conversation

**Setup:**

1. Launch the local server:
```bash
uvicorn pokemon_server:app --reload --port 10002
```

2. In another terminal, start the UI:
```bash
cd ui
npm install  # Required only on first run
npm run watch
```

Controls: WASD for movement, SPACE to initiate conversation

## Example Simulations with Tools

AgentVerse supports simulations where agents can use external tools:

### NLP Classroom with Tool Usage

```bash
agentverse-simulation-gui --task simulation/nlp_classroom_3players_withtool
```

Students can use Bing search API while attending class.

### Math Problem Solving

```bash
agentverse-simulation-gui --task simulation/math_problem_2players_tools
```

Two agents collaborate using WolframAlpha API for arithmetic problems.

## Configuration Structure

Simulations are configured using YAML files. Basic structure:

```yaml
environment:
  env_type: basic
  max_turns: 10
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
      type: basic

agents:
  - agent_type: conversation
    name: Agent Name
    role_description: Description of agent's role
    memory:
      memory_type: chat_history
    prompt_template: |
      Your prompt here
    llm:
      llm_type: text-davinci-003
      model: text-davinci-003
      temperature: 0.7
      max_tokens: 250
```

## Custom Agent Types

### ConversationAgent

Standard agent for text-based conversation and interaction.

### ToolAgent

Agent with capability to use external tools and APIs (requires BMTools).

## Customization

### Rule Components

The simulation framework abstracts environments into five customizable rule components:

1. **Describer**: Provides environment description to agents each turn
2. **Order**: Defines agent action sequence (sequential, random, concurrent)
3. **Selector**: Filters valid agent messages
4. **Updater**: Updates agent memory with relevant messages
5. **Visibility**: Maintains list of visible agents for each agent

### Creating Custom Scenarios

To create your own simulation:

1. Create a task directory in `agentverse/tasks`
2. Write a `config.yaml` configuration file
3. Implement an output parser for agent responses
4. Register the parser in `agentverse/tasks/__init__.py`

For detailed customization guides, see the main repository documentation.

## Hugging Face Integration

Try AgentVerse simulations online without local installation:

- **HuggingFace Spaces:** https://huggingface.co/spaces/AgentVerse/agentVerse
- Supported scenarios: NLP Classroom, Prisoner's Dilemma
- Requires OpenAI API key

## Community Examples

### ChatEval Integration

The [ChatEval](https://github.com/chanchimin/ChatEval) project implements a multi-agent referee team using AgentVerse to evaluate text generation from different models. Agents debate differences and provide judgments, showing better alignment with human evaluations than baseline approaches.

## Tips for Simulation Design

1. Start with existing examples to understand the framework
2. Test with small agent counts before scaling
3. Configure memory appropriately for context length
4. Use reasonable `max_turns` to prevent infinite loops
5. Customize prompts and rule components for specific scenarios
6. Use tools to enable sophisticated agent behaviors
