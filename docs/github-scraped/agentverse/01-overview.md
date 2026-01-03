# AgentVerse Overview

**Source:** https://github.com/OpenBMB/AgentVerse

AgentVerse is an open-source Python framework designed to facilitate the deployment of multiple LLM-based agents in various applications. It provides comprehensive support for building multi-agent systems that can collaborate, coordinate, and achieve complex tasks.

## Key Features

AgentVerse primarily provides two frameworks:

### 1. Task-Solving Framework
A framework that assembles multiple agents as an automatic multi-agent system to collaboratively accomplish corresponding tasks.

- Enables multi-agent systems to work together on complex problems
- Based on research from [AgentVerse-Tasksolving](https://arxiv.org/pdf/2308.10848.pdf) and [Multi-agent as system](https://arxiv.org/abs/2309.02427)
- Applications: software development systems, consulting systems, code generation, and more

**Notable Use Cases:**
- Software design and implementation with code writer, tester, and reviewer agents
- Problem solving with specialized agents using tools
- Humaneval benchmark testing
- Brainstorming tasks with multiple agents

### 2. Simulation Framework
Allows users to set up custom environments to observe behaviors among, or interact with, multiple agents.

- Applications: games, social behavior research of LLM-based agents, custom environments
- Note: The project is refactoring the simulation code. For stable simulation-only features, use the [`release-0.1`](https://github.com/OpenBMB/AgentVerse/tree/release-0.1) branch

**Notable Examples:**
- NLP Classroom: Multi-agent classroom environment with professor and students
- Prisoner's Dilemma: Strategic interaction between agents
- Software Design Environment: Collaborative code development
- Database Administrator (DBA) Monitoring: Multi-agent database diagnostics
- Pokemon Game: Interactive game environment with agent NPCs

## Project Status

- **License:** Apache 2.0
- **Python Version Required:** 3.9+
- **Build Status:** Active CI/CD pipeline
- **Code Style:** Black formatted
- **Paper Accepted:** ICLR 2024
- **Latest Update:** Featured in NVIDIA's blog (March 2024) - "Building Your First LLM Agent Application"

## Community & Support

- **Discord:** https://discord.gg/gDAXfjMw
- **Twitter:** https://twitter.com/Agentverse71134
- **Hugging Face:** https://huggingface.co/spaces/AgentVerse/agentVerse
- **Email:** agentverse2@gmail.com
- **Research Paper:** https://arxiv.org/abs/2308.10848

## Citation

If you use AgentVerse in your research, please cite:

```bibtex
@article{chen2023agentverse,
  title={Agentverse: Facilitating multi-agent collaboration and exploring emergent behaviors in agents},
  author={Chen, Weize and Su, Yusheng and Zuo, Jingwei and Yang, Cheng and Yuan, Chenfei and Qian, Chen and Chan, Chi-Min and Qin, Yujia and Lu, Yaxi and Xie, Ruobing and others},
  journal={arXiv preprint arXiv:2308.10848},
  year={2023}
}
```

## Contributors

**Project Leaders:**
- Weize Chen (chenweize1998@gmail.com)
- Yusheng Su (yushengsu.thu@gmail.com)

**Core Contributors:**
The project welcomes contributions in multiple areas including code development, documentation, application exploration, and community feedback.
