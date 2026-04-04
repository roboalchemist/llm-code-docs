# Source: https://docs.jit.io/docs/security-plan-structure-and-components.md

# Security Plan Structure

## Overview

Jit security plans are structured using the following hierarchy:

* A **Plan** is composed of items logically divided into the different layers of the stack.
* An **Item** is composed of one or multiple workflows.
* A **Workflow** is composed of one or multiple jobs.
* A **Job** is composed of one or multiple steps.
* A **Step** executes the **Security Tool**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/948edbf-Screen_Shot_2022-03-13_at_15.08.05.png",
        "Screen Shot 2022-03-13 at 15.08.05.png",
        "Plan Struture overview"
      ],
      "align": "center",
      "caption": "Plan Struture overview"
    }
  ]
}
[/block]

## Plan-as-Code

> ⚠️ Note
>
> Security Plan configuration is managed directly in the Jit platform.\
> As-code configuration is no longer the source of truth and is considered redundant.\
> If you previously used as-code configuration, it has been automatically synced to Jit.\
> Please contact us if anything is unclear or behaves differently than expected.

See the code block below for an example of how the security plan structure is expressed as the plan-as-code YAML file.

```yaml Plan file (example)
name: Minimum Viable Security plan for cloud apps
level: beginner
author: Jit
owners:
  default:
references:
  - https://www.jit.io
tags:
  - mvs
#----------- List of plan items -----------
items:
  - name: Check for code vulnerabilities
    uses: jitsecurity-controls/jit-plans/items/code/code-vulnerability-item.yml@latest

  - name: Check for hard-coded secrets
    uses: jitsecurity-controls/jit-plans/items/code/secret-detection-item.yml@latest

  - name: Check for vulnerable dependencies
    uses: jitsecurity-controls/jit-plans/items/code/dependency-check-item.yml@latest

  - name: Check for infrastructure misconfiguration
    uses: jitsecurity-controls/jit-plans/items/infrastructure/iac-misconfiguration-detection-item.yml@latest
```

YAML files are also used to define plan items and workflows. In the examples below, note how the plan item (first code block) is associated with its constituent security tools via a Jit workflow file (second code block).

```yaml Plan item file (example)
namespace: jit.code
name: Detect code vulnerabilities
description: |
  Static code analysis tools can discover vulnerabilities inside your code before they make their way to production.
summary: |
  Integrate SAST into CI/CD so it automatically runs for every new PR
workflows:
  - uses: jitsecurity-controls/jit-plans/workflows/sast-workflow@latest
tags:
  layer: code
  risk_category: code_vulnerability
  compliance:soc2: CC7.1
```

```yaml Jit workflow file (example)
name: SAST Workflow
jobs:
  static-code-analysis:
    trigger:
      on:
        - pull_request_created
        - pull_request_updated
    runner: github_actions
    steps:
      - name: Run Bandit
        uses: ghcr.io/jitsecurity-controls/control-bandit-slim:latest
        if: "python in ${{ context.languages }}"
        with:
          args: -r /code -f json -q -ll -iii
```