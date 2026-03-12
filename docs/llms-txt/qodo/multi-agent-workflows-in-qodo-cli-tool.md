# Source: https://docs.qodo.ai/qodo-documentation/qodo-command/features/multi-agent-workflows-in-qodo-cli-tool.md

# Multi-Agent Workflows in Qodo CLI tool

Qodo CLI tool supports combining multiple agents into workflows through three distinct chaining mechanisms, each optimized for different handoff patterns:

* **Context chaining (`>`)** — next agent receives a task-focused summary of previous step(s)
* **Pipe chaining (`|`)** — next agent receives structured outputs as command arguments
* **Sub-agents** — agents call other agents as tools during execution

This guide uses `review` and `review_ranked` as example agents to illustrate the chaining patterns.

***

### Context Chaining (`>`)

Context chaining runs agents sequentially. Before each agent starts, Qodo preloads a task-focused summary of previous sessions, providing the proper context without explicit wiring.

**Use when:**

* The downstream agent should start with prior conclusions
* The agent can infer its task from context rather than requiring strict inputs

**Syntax:**

```bash
qodo chain "agentA > agentB > agentC"
```

Always quote the chain to prevent shell interpretation of special characters.

**Example:**

```bash
qodo chain "review > review_ranked"
qodo chain "review --set pr=https://github.com/owner/repo/pull/123 > review_ranked"
```

**Note:** If your downstream agent requires specific structured inputs (e.g., `review_ranked` expects `summary` and `findings`), prefer pipe chaining or make those arguments optional.

***

### Pipe Chaining (`|`)

Pipe chaining automatically maps the previous agent's structured output into `--set` arguments for the next agent. This creates a clear data contract between steps.

**Use when:**

* You have explicit field dependencies between agents
* The consuming agent requires specific, structured inputs
* You want deterministic, machine-to-machine handoffs

**How it works:**

The producing agent's `output_schema` fields are mapped to the consuming agent's `arguments`. For example:

```
review outputs:        { "summary": "...", "findings": [...] }
review_ranked receives: --set summary="..." --set findings="[...]"
```

This automatic field mapping makes pipe chaining ideal for structured data handoffs.

**Syntax:**

```bash
# Minimal (auto-pipe structured output)
qodo chain "review | review_ranked"

# With arguments to first step
qodo chain "review --set pr=https://github.com/owner/repo/pull/123 | review_ranked"
```

**Requirements:**

* **Producing agent:** Must define `output_schema` with the fields to pass
* **Consuming agent:** Must define `arguments` with matching names and types

***

### Sub-agents

Sub-agents allow an agent to invoke other agents as tools during its run. Sub-agents execute in child processes but surface all activity in the parent's UI and approval flow.

**Use when:**

* The parent agent should dynamically decide which specialized agents to invoke
* Steps are optional or conditional
* You need a supervisor/specialist delegation pattern

**Implementation:**

Sub-agents are exposed as tools with the naming pattern `subagents__<agent_name>`. The parent agent's instructions determine when and how to invoke them.

**Example orchestrator instructions:**

```
First, run subagents__review with the PR URL. If there are more than 10 
critical findings, run subagents__review_ranked to prioritize the top issues. 
Return a final summary.
```

**Behavior:**

* Sub-agents inherit auto-approvals from the parent
* Non-auto-approved tool calls prompt in the parent's UI
* The currently running agent is not exposed as a sub-agent (prevents recursion)

***

### Pattern Selection

**Context chaining (`>`):**

* The next agent needs awareness of prior work
* Flexible, context-driven handoffs
* The agent can infer the task from the summary

**Pipe chaining (`|`):**

* Strict field dependencies
* Structured, deterministic data flow
* Clear contracts between agents
* **Ideal for workflows like `review → review_ranked` where outputs map to inputs**

**Sub-agents:**

* Dynamic workflow decisions
* Conditional or optional steps
* Hierarchical delegation patterns

**Hybrid approach:** Chain top-level phases with `>` or `|`, and use sub-agents within phases for dynamic delegation.

***

### Example Workflow: Review Pipeline

The following examples demonstrate chaining patterns using `review` and `review_ranked` agents, where:

* `review` produces structured output with `summary` and `findings` fields
* `review_ranked` consumes those fields to prioritize findings

#### Single agent execution

```bash
qodo run review --set pr=https://github.com/owner/repo/pull/123
```

#### Pipe chain (recommended for this pattern)

```bash
qodo chain "review --set pr=https://github.com/owner/repo/pull/123 | review_ranked"
```

This automatically passes `review`'s structured output (`summary` and `findings`) to `review_ranked`'s arguments.

#### Context chain configuration

To use context chaining between these agents, modify `review_ranked`'s argument requirements:

## Make arguments optional to accept context instead of strict inputs

```diff
arguments = [
-  { name = "summary", type = "string", required = true, description = "High-level summary of the PR analysis." },
-  { name = "findings", type = "array", required = true, description = "List of issues findings (each in json format) extracted from a PR unified git diff code review." }
+  { name = "summary", type = "string", required = false, description = "High-level summary of the PR analysis." },
+  { name = "findings", type = "array", required = false, description = "List of issues findings (each in json format) extracted from a PR unified git diff code review." }
 ]
```

Then run:

```bash
qodo chain "review --set pr=https://github.com/owner/repo/pull/123 > review_ranked"
```

**Note:** This modification is primarily for demonstrating context chaining. For production pipelines where strict input validation is critical, keep required arguments and use pipe chaining.

#### Sub-agent orchestration

Create an orchestrator agent that dynamically invokes both agents based on runtime conditions. The orchestrator's instructions might specify:

* When to call `subagents__review`
* Conditions for calling `subagents__review_ranked`
* How to synthesize results

***

### Troubleshooting

#### Shell interpretation issues

Always quote the entire chain string:

```bash
# Correct
qodo chain "review > agent2"

# Incorrect - shell will interpret > as output redirection
qodo chain review > agent2
```

#### Pipe chain missing fields

If `|` reports missing fields:

1. Verify that the producing agent outputs those fields in its `output_schema`
2. Confirm that the consuming agent declares them as `arguments`
3. Ensure field names match exactly (case-sensitive)

#### Passing additional arguments

Use `--set` to provide arguments to specific steps:

```bash
qodo chain "review --set pr=... > review_ranked --set max_findings=5"
```

***

### Command Reference

```bash
# Context chain
qodo chain "agentA > agentB > agentC"

# Pipe chain
qodo chain "agentA | agentB | agentC"

# Arguments to specific steps
qodo chain "agentA --set key=value | agentB --set key=value"
```

***

### Design Principles

* **Use `>` for flexible handoffs** where agents work from a summarized context
* **Use `|` for strict contracts** where exact field mapping is required
* **Use sub-agents for dynamic logic** where runtime conditions determine workflow
* **Validate field mappings** by ensuring output schemas match argument definitions
* **Quote all chains** to avoid shell interpretation issues
