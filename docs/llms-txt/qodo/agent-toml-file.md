# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/workflows/agent-toml-file.md

# Agent TOML File

Every agent - whether created by you or provided out-of-the-box - is defined by a **TOML file**.

This file contains everything the agent needs to function:

* Its instructions
* What tools it can access
* Optional arguments and configuration
* Execution behavior
* Output structure

These TOML files form the foundation of how agents behave and interact with your project.

### Where Agent Files Are Stored

All agent TOML files are stored in a centralized location on your machine:

```
~/.qodo/agents/
```

**This directory is automatically created and managed by Qodo.**

When you start using agents in Qodo IDE plugin, Qodo loads and displays agents based on the TOML files it finds in this folder.
