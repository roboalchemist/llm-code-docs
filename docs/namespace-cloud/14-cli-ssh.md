# nsc ssh

Establish secure SSH connections to ephemeral environments.

## Overview

This tool establishes secure SSH connections to previously created ephemeral environments while maintaining end-to-end encryption without exposing hosts directly to the internet.

## Basic Usage

```bash
nsc ssh [--tag <name>] [-A] [<id>] [command]
```

## Quick Access Methods

- Provide an environment ID to connect directly
- Omit the ID to see an interactive list of your environments
- Execute commands remotely without entering an interactive session

## Example Workflow

```bash
# Create an environment
nsc create

# Connect using the returned ID
nsc ssh 85a32emcg99ii

# Run remote commands
nsc ssh 85a32emcg99ii ls /
nsc ssh 85a32emcg99ii pwd
```

## Options

**--tag <name>**: Connects to an existing named environment, or creates one if it doesn't exist

**-A**: Forwards your local SSH agent to the remote environment

## Advanced Usage

Execute commands directly without entering an interactive session:

```bash
nsc ssh 85a32emcg99ii "echo 'Hello from Namespace'"
```

## Connection Details

The command streamlines container-enabled terminal access, allowing you to jump into a working environment within seconds.
