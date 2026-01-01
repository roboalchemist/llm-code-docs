# AgentVerse Documentation

**Source:** https://github.com/OpenBMB/AgentVerse
**License:** Apache 2.0
**Python Version:** 3.9+

AgentVerse is an open-source framework for deploying and managing multiple LLM-based agents with coordination. It provides two main frameworks for different applications: task-solving and simulation environments.

## Documentation Index

### [01 - Overview](01-overview.md)
Introduction to AgentVerse, key features, project status, and research background.

**Topics:**
- Framework overview (task-solving and simulation)
- Key use cases and applications
- Community resources
- Citation information

### [02 - Installation and Setup](02-installation-and-setup.md)
Complete installation instructions and environment configuration.

**Topics:**
- Manual and pip installation
- OpenAI and Azure API configuration
- vLLM and local model setup
- BMTools and XAgent ToolsServer integration
- FastChat integration for local models

### [03 - Simulation Framework](03-simulation-framework.md)
Building multi-agent simulation environments.

**Topics:**
- Running simulations (CLI and GUI)
- Built-in examples (NLP Classroom, Prisoner's Dilemma, Software Design, DBA, Pokemon)
- Configuration structure
- Agent types (ConversationAgent, ToolAgent)
- Creating custom scenarios
- HuggingFace integration

### [04 - Task-Solving Framework](04-task-solving-framework.md)
Using agents to solve complex problems collaboratively.

**Topics:**
- Running benchmark evaluations
- Single query tasks
- Tool-using multi-agent systems
- Available task examples
- LLM configuration (OpenAI, Azure, vLLM, local)
- Memory management
- Best practices

### [05 - Agent Types and Customization](05-agent-types-and-customization.md)
Agent architecture and creating specialized agents.

**Topics:**
- ConversationAgent capabilities and configuration
- ToolAgent with external tool support
- Memory types and management
- Configuration-based customization
- Code-based customization via inheritance
- Creating specialized agents (Research, Creative, Validator)
- Multi-agent team structures

### [06 - Environment Rules and Customization](06-environment-rules.md)
The five-component rule system for environment customization.

**Topics:**
- Describer: Environment description
- Order: Action sequence
- Selector: Message filtering
- Updater: Memory distribution
- Visibility: Agent perception
- Custom rule implementation
- Complete environment configuration
- Common patterns and best practices

## Quick Start

### Installation

```bash
git clone https://github.com/OpenBMB/AgentVerse.git
cd AgentVerse
pip install -e .
```

### Run a Simulation

```bash
export OPENAI_API_KEY="your_api_key"
agentverse-simulation-gui --task simulation/nlp_classroom_9players
```

Visit `http://127.0.0.1:7860/` to view the simulation.

### Run a Task-Solving Example

```bash
agentverse-tasksolving --task tasksolving/brainstorming
```

## Framework Comparison

| Feature | Simulation | Task-Solving |
|---------|-----------|--------------|
| **Purpose** | Explore agent behaviors and interactions | Solve complex problems collaboratively |
| **Use Cases** | Games, research, social dynamics | Code generation, consulting, problem-solving |
| **Interaction** | Dynamic, real-time environment | Structured problem definition |
| **Tools** | Optional | Common requirement |
| **Output** | Behavior observations | Solution/answer |
| **Best LLMs** | Any capability level | GPT-4 recommended |

## Key Concepts

### Agents

Autonomous entities that:
- Generate responses to prompts
- Maintain conversation memory
- Interact with other agents
- Optionally use external tools

Types:
- **ConversationAgent**: Text generation and reasoning
- **ToolAgent**: Extended with tool capabilities

### Environments

Structured spaces where agents interact, defined by:
- **Rule Components**: Five modular rule types controlling interaction
- **Configuration**: YAML-based environment specification
- **Agents**: Populated with configured agent instances

### Rule Components

Five customizable components defining environment behavior:
1. **Describer**: What agents see
2. **Order**: When agents act
3. **Selector**: Which messages are valid
4. **Updater**: Who sees which messages
5. **Visibility**: Who perceives whom

## LLM Support

AgentVerse supports multiple LLM backends:

- **OpenAI**: GPT-4, GPT-3.5-turbo, etc.
- **Azure OpenAI**: Enterprise OpenAI deployments
- **vLLM**: High-throughput serving of large models
- **Local Models**: LLaMA, Vicunna (via FastChat)

## API Keys Required

- **OpenAI**: For using OpenAI models
- **Azure**: For Azure OpenAI services
- **Bing Search**: For web search in tool-using agents (optional)
- **WolframAlpha**: For mathematical computation (optional)

## Community

- **Discord**: https://discord.gg/gDAXfjMw
- **Twitter**: https://twitter.com/Agentverse71134
- **Hugging Face Spaces**: https://huggingface.co/spaces/AgentVerse/agentVerse
- **GitHub Issues**: https://github.com/OpenBMB/AgentVerse/issues

## Contributing

AgentVerse welcomes contributions in:
- Code development and optimization
- Documentation and tutorials
- Application exploration
- Feedback and suggestions

See the main [GitHub repository](https://github.com/OpenBMB/AgentVerse) for contribution guidelines.

## Research

AgentVerse is based on published research:

- **Main Paper**: [Agentverse: Facilitating multi-agent collaboration and exploring emergent behaviors in agents](https://arxiv.org/abs/2308.10848) - Accepted at ICLR 2024
- **Extension**: [Multi-agent as System](https://arxiv.org/abs/2309.02427)
- **Applications**: Featured in [NVIDIA's blog](https://developer.nvidia.com/blog/building-your-first-llm-agent-application/)

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure you installed with `pip install -e .`
2. **API key errors**: Check environment variables are set correctly
3. **Tool failures**: Verify XAgent ToolsServer is running for tool-using agents
4. **Memory errors**: Reduce `max_tokens` or `max_history_turns`

### Getting Help

- Check GitHub issues for similar problems
- Post in the Discord community
- Open a new GitHub issue with details

## License

AgentVerse is licensed under the Apache 2.0 License. See LICENSE file in the repository.

## Citation

```bibtex
@article{chen2023agentverse,
  title={Agentverse: Facilitating multi-agent collaboration and exploring emergent behaviors in agents},
  author={Chen, Weize and Su, Yusheng and Zuo, Jingwei and Yang, Cheng and Yuan, Chenfei and Qian, Chen and Chan, Chi-Min and Qin, Yujia and Lu, Yaxi and Xie, Ruobing and others},
  journal={arXiv preprint arXiv:2308.10848},
  year={2023}
}
```
