# Source: https://docs.agent.ai/actions/invoke_other_agent.md

# Invoke Other Agent

## Overview

Trigger another agent to perform additional processing or data handling within workflows.

### Use Cases

* **Multi-Agent Workflows**: Delegate tasks to specialized agents.
* **Cross-Functionality**: Utilize existing agent capabilities for enhanced results.

<iframe width="560" height="315" src="https://www.youtube.com/embed/DqWPxjlsT6o?si=uf7kUR209DgbpGpT" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### Agent ID

* **Description**: Enter the ID of the agent to invoke.
* **Example**: "agent\_123" or "data\_processor."
* **Required**: Yes

### Parameters

* **Description**: Specify parameters for the agent as key-value pairs, one per line.
* **Example**: "action=update" or "user\_id=567."
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the agent's response.
* **Example**: "agent\_output" or "result\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes
